# SDN-Based QoS Priority Controller

## Overview

This project demonstrates how Quality of Service (QoS) can be implemented using Software Defined Networking (SDN). Traffic is classified based on TCP port numbers and assigned different bandwidth using Open vSwitch (OVS) queues controlled by a POX controller.

---

## Objective

- Classify traffic using TCP ports  
- Assign different priorities to traffic  
- Demonstrate bandwidth control using SDN  

---

## System Architecture

- Mininet → Network emulator  
- Open vSwitch → Data plane (switch)  
- POX → Controller (control plane)  


---

## Traffic Policy

| Port | Priority | Queue | Bandwidth |
|------|--------|------|----------|
| 5001 | High   | 1    | ~9 Mbps  |
| 5002 | Low    | 2    | ~1 Mbps  |

---

## Project Structure
sdn-qos-pox/
- topo.py
- qos_controller.py
- README.md
- screenshots/
