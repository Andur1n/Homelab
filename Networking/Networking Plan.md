# Networking Plan

This document outlines the current and planned network layout for the home lab environment. It includes VLANs, subnets, pfSense interfaces, switch ports, and connected devices. Future expansions like IoT and Wi-Fi are also accounted for.

---

## 1. Edge / Internet

- **ISP Router**
  - IP: `192.168.1.1` (LAN)
  - Provides Internet access
  - Temporary Wi-Fi until Ubiquiti AP is deployed
  - Handles DHCP for 192.168.1.x devices

---

## 2. Core / Management VLAN (VLAN10)

- **Subnet:** `172.16.0.0/24`
- **Gateway:** pfSense `172.16.0.1`
- **Switch IP:** `172.16.0.2`
- **Switch Port:** 24 → pfSense connection (trunk)
- **Purpose:** Management and administration of the lab network
- **Notes:**
  - Trunks all VLANs to pfSense virtual interfaces
  - Only admin devices should have access

---

## 3. General Network VLAN (VLAN20)

- **Subnet:** `172.16.1.0/24`
- **Gateway:** pfSense `172.16.1.1`
- **Switch Ports:** 1-4
- **Devices:**
  - Den-Main PC (DHCP)
  - Jen-Main PC (DHCP)
- **Purpose:** Home / general devices
- **Notes:**
  - DHCP managed by pfSense
  - VLAN isolated from lab and management VLANs

---

## 4. Lab Network VLAN (VLAN30)

- **Subnet:** `172.16.2.0/24`
- **Gateway:** pfSense `172.16.2.1`
- **Switch Ports:** 5-10
- **Devices:**
  - Raspberry Pi 5 (Pi-hole) → `172.16.2.2`
  - Lab Server → `172.16.2.3`
- **DHCP Pool:** Reserve `172.16.2.2 – 172.16.2.15` for static devices
- **Purpose:** Dedicated lab environment for cybersecurity and testing
- **Notes:**
  - pfSense handles DHCP and firewall rules for lab VLAN
  - VLAN isolated from general/home devices

---

## 5. IoT / Future VLAN (VLAN40)

- **Subnet:** `172.16.3.0/24`
- **Gateway:** pfSense `172.16.3.1`
- **Switch Ports:** Reserved / future use
- **Purpose:** IoT and wireless networks via Ubiquiti AP
- **Notes:**
  - VLAN will be tagged to Ubiquiti SSIDs when deployed
  - Fully isolated from lab and general VLANs

![Networking Diagram](https://github.com/Andur1n/Homelab/blob/main/Networking/Networking%20Diagram.png)

---

## 6. Summary Notes

- All VLANs trunked to pfSense, which handles routing, DHCP, and firewall rules.
- VLANs are designed with `/24` subnets for simplicity and scalability.
- Management VLAN (VLAN10) is strictly for switch and firewall administration.
- Lab VLAN (VLAN30) is isolated to contain vulnerable machines and testing environments.
- Future expansions include IoT VLAN, NAS, and wireless networks.
- Reserved DHCP addresses prevent collisions with static devices.
- Diagram to be added below once drawn.

---

## 7. Future Considerations

- Upgrade pfSense port to Gigabit SFP to free physical port
- Deploy Ubiquiti AP and map SSIDs to VLANs
- Add NAS and Plex server with separate VLANs
- Monitor VLAN traffic with pfSense logging, Wazuh, and Splunk

---

