from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_ConnectionUp(event):
    log.info("Switch connected: %s", event.connection)

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.connection.dpid

    mac_to_port.setdefault(dpid, {})

    src = packet.src
    dst = packet.dst
    in_port = event.port

    log.info("Packet: %s -> %s", src, dst)

    # Learn MAC
    mac_to_port[dpid][src] = in_port

    # 🚫 BLOCK TRAFFIC FROM h1 (10.0.0.1)
    ip_packet = packet.find('ipv4')
    if ip_packet and str(ip_packet.srcip) == "10.0.0.1":
        log.info("🚫 Blocking traffic from h1")
        return

    # Forwarding logic
    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]
    else:
        out_port = of.OFPP_FLOOD

    actions = [of.ofp_action_output(port=out_port)]

    # Install flow rule
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet, in_port)
    msg.actions = actions
    msg.idle_timeout = 10
    msg.hard_timeout = 30

    event.connection.send(msg)

    # Send packet out
    packet_out = of.ofp_packet_out()
    packet_out.data = event.ofp
    packet_out.actions = actions
    packet_out.in_port = in_port

    event.connection.send(packet_out)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("🚀 Delay Measurement SDN Controller Running")