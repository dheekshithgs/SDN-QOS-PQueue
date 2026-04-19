# SDN-Based QoS Priority Controller (Mininet + POX)

## Overview

This project demonstrates how Quality of Service (QoS) can be implemented using Software Defined Networking (SDN). Traffic is classified based on TCP port numbers and assigned different bandwidth using Open vSwitch (OVS) queues controlled by a POX controller.

---

## Objective

- Classify traffic using TCP ports  
- Assign different priorities to traffic  
- Demonstrate bandwidth control using SDN  

---

## Background Theory

### QoS (Quality of Service)

QoS is a mechanism used to manage network resources by giving different priorities to different types of traffic. Instead of treating all traffic equally, QoS ensures that important traffic gets better performance.

In this project, QoS is used to control **bandwidth allocation**.

---

### SDN (Software Defined Networking)

SDN separates the network into two layers:

- **Control Plane** → decides how traffic should flow (controller)  
- **Data Plane** → forwards packets (switch)  

This allows centralized control over the network.

---

### OpenFlow

OpenFlow is the protocol that connects the controller and the switch. It uses:

- **Match** → identify packets (e.g., TCP port)  
- **Action** → define what to do (forward, enqueue, etc.)  

---

### QoS in Open vSwitch

Open vSwitch implements QoS using queues:

- Queue 1 → high bandwidth  
- Queue 2 → low bandwidth  

The controller assigns traffic to these queues using OpenFlow rules.

---

## System Architecture

- Mininet → Network emulator  
- Open vSwitch → Data plane  
- POX → Controller  

---

## Traffic Policy

| Port | Priority | Queue | Bandwidth |
|------|--------|------|----------|
| 5001 | High   | 1    | ~9 Mbps  |
| 5002 | Low    | 2    | ~1 Mbps  |


---

## How the System Works

1. Controller starts and listens for switches  
2. Switch connects to controller  
3. Controller installs flow rules:
   - Port 5001 → Queue 1  
   - Port 5002 → Queue 2  
4. Queues are configured in OVS  
5. Traffic is generated using iperf  
6. Switch enforces bandwidth based on queues  

---

## Setup Requirements

- Mininet  
- Open vSwitch  
- Python3  
- POX Controller  
- iperf  

---
