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

## 2. Management VLAN (VLAN10)

- **Subnet:** `172.16.10.0/24`
- **Gateway:** pfSense `172.16.10.1`
- **Switch IP:** `172.16.10.2`
- **Switch Port:** Port 6 and 7, Port 8 is the trunked uplink to PFSense
- **Raspberry 5 - Pi-Hole IP:** `172.16.10.3`
- **Purpose:** Management and administration of the whole network while Pi-Hole functions as a DNS server forwarding non-blocked requests to `1.1.1.1` and `1.0.0.1`.
- **Notes:**
  - Trunks all VLANs to pfSense virtual interfaces
  - Only admin devices should have access#
  - Using a SFP Ethernet Switch for the Trunked connection from the PFSense Firewall.

---

## 3. Private VLAN (VLAN20)

- **Subnet:** `172.16.20.0/24`
- **Gateway:** pfSense `172.16.20.1`
- **Switch Ports:** Port 1 and 2
- **Devices:**
  - Main PC 1 (172.16.20.2)
  - Main PC 2 (DHCP)
- **Purpose:** Home / general devices
- **Notes:**
  - DHCP managed by pfSense in VLAN10
  - DNS managed by Pi-Hole in VLAN10
  - Static IP on desktop to allow management of the homelab via desktop.

---

## 4. Lab Network VLAN (VLAN30)

- **Subnet:** `172.16.30.0/24`
- **Gateway:** pfSense `172.16.30.1`
- **Switch Ports:** Port 3 and 4
- **Devices:**
  - Physical Proxmox Server - `172.16.30.2`
  - Splunk – `172.16.30.3`
  - Wazuh – `172.16.30.4`
  - Nessus – `172.16.30.5`
  - Windows Server 2022 – `172.16.30.6`
  - Windows 11 – `172.16.30.7`
  - Kali Linux – `172.16.30.8`
  - Metasploitable - `172.16.30.9`
- **DHCP Pool:** Reserve `172.16.30.2 – 172.16.30.15` for Physical Server + VM's running within the lab server as well as future proof this.
- **Purpose:** Dedicated lab environment for cybersecurity and testing
- **Notes:**
  - DHCP managed by pfSense in VLAN10
  - DNS managed by Pi-Hole in VLAN10

---

## 5. IoT / Future VLAN (VLAN40)

- **Subnet:** `172.16.40.0/24`
- **Gateway:** pfSense `172.16.40.1`
- **Switch Ports:** Port 5
- **Purpose:** Segregated IoT devices.
- **Notes:**
  - Completely separated from other VLAN's and relying on public DNS resolvers.
---

## 6. Summary Notes

- All VLANs trunked to pfSense, which handles routing, DHCP, and firewall rules.
- VLANs are designed with `/24` subnets for simplicity and scalability.
- Management VLAN (VLAN10) is strictly for switch, firewall and DNS administration.
- Future expansions include IoT VLAN, NAS, and wireless networks.
- Reserved DHCP addresses prevent collisions with static devices.

---

## 7. Future Considerations

- Deploy Ubiquiti AP and map SSIDs to VLANs
- Add NAS and Plex server with separate VLANs
- Monitor VLAN traffic with pfSense logging, Wazuh, and Splunk
- Seperate services (Wazuh, Nessus and Splunk) from VLAN30 into it's own VLAN.

---

![Networking Diagram](https://github.com/Andur1n/Homelab/blob/main/Networking/Network%20Diagram%20-%20Updated.png)
