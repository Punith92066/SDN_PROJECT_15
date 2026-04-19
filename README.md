# 📡 SDN-Based Network Delay Measurement Tool (Mininet + POX)

## 📌 Project Overview

This project demonstrates a **Software Defined Networking (SDN)** solution using **Mininet** and a **POX controller** to measure and analyze network delay (latency) while dynamically controlling traffic.

The controller implements **flow rule logic (match-action)** and handles **PacketIn events** to manage packet forwarding and filtering.

---

## 🎯 Objectives

* Measure **network delay (RTT)** using ping
* Demonstrate **controller–switch interaction**
* Implement **flow rules using OpenFlow**
* Show **traffic control (allow/block) using SDN**
* Analyze network performance (latency, throughput)

---

## 🏗️ Network Topology

Linear topology with 3 hosts and 2 switches:

```
h1 —— s1 —— h2 —— s2 —— h3
```

* Hosts: h1, h2, h3
* Switches: s1, s2
* Controller: POX (remote)

---

## ⚙️ Technologies Used

* Mininet (network emulation)
* POX Controller
* OpenFlow Protocol
* ovs-ofctl (flow inspection)
* ping (latency measurement)
* iperf (throughput measurement)

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
sudo apt update
sudo apt install mininet
git clone https://github.com/noxrepo/pox.git
```

---

### 2. Start POX Controller

```bash
cd pox
./pox.py misc.delay_project
```

---

### 3. Run Mininet

```bash
sudo mn --topo linear,3 --controller=remote,ip=127.0.0.1,port=6633
```

---

## 🧠 Controller Logic

The POX controller performs:

* Learning switch behavior (MAC learning)
* Handles `PacketIn` events
* Installs flow rules dynamically
* Implements traffic filtering (blocking)

### Key Features:

* Match packets based on source IP
* Forward packets to correct port
* Drop packets for blocked hosts

---

## 🧪 Test Scenarios

### ✅ Scenario 1: Normal Communication

**Command:**

```bash
mininet> pingall
```

**Expected Output:**

* 0% packet loss
* Successful communication between all hosts

**Latency Test:**

```bash
mininet> h1 ping -c 5 h3
```

**Observation:**

* Low RTT (Round Trip Time)

---

### ❌ Scenario 2: Blocked Traffic (SDN Control)

Controller blocks traffic from **h1**

**Command:**

```bash
mininet> h1 ping h3
```

**Expected Output:**

* 100% packet loss
* No communication

**Verification:**

```bash
mininet> h2 ping h3
```

* Works normally (only h1 is blocked)

---

## 📊 Performance Analysis

### 🔹 Latency Measurement

```bash
h1 ping h3
```

* Measures RTT
* Indicates network delay

---

### 🔹 Throughput Measurement

```bash
mininet> h1 iperf h3
```

* Shows bandwidth
* Fails when traffic is blocked

---

### 🔹 Flow Table Inspection

```bash
sudo ovs-ofctl dump-flows s1
```

**Observation:**

* Flow entries installed dynamically
* Packet counts increase with traffic

---

## 📸 Proof of Execution

Include screenshots of:

* ping results
* iperf results
* flow table output
* controller logs

---

## 📈 Observations

* SDN controller dynamically controls packet forwarding
* Blocking rules affect network behavior instantly
* Latency depends on network conditions and topology
* Flow tables update based on traffic patterns

---

## 🧪 Validation

| Scenario        | Expected Result   |
| --------------- | ----------------- |
| Normal          | Successful ping   |
| Blocked         | 100% packet loss  |
| iperf (normal)  | Bandwidth visible |
| iperf (blocked) | Connection fails  |

---

## 🎓 Conclusion

This project demonstrates:

* Centralized control using SDN
* Dynamic traffic management
* Real-time network monitoring
* Delay measurement using simple tools

It highlights how SDN can be used for:

* Traffic engineering
* Network security (blocking/filtering)
* Performance optimization

---

## 📚 References

* Mininet Documentation
* POX Controller Documentation
* OpenFlow Specification

---
