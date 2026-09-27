# Homelab Firewall Rules

## Design Principles
- Default deny (least privilege)
- VLAN-based network segmentation
- Stateful firewall (allow ESTABLISHED, RELATED traffic)
- Explicit allow rules for required services only
- Centralised DNS Enforcement (all clients must use Pi-Hole as a DNS server)
- Logging on critical rules

---

## VLAN 10 – Core / Management (172.16.10.0/24)
**Purpose:** Administrative access & Pi-hole

| From | To | Destination | Action | Port | Note |
|------|--------|-------------|-----------------|------------|----------------|
| VLAN 20 Subnet | 172.16.10.3 | Allow | 53 | Allows VLAN 20 to make DNS requests |
| VLAN 30 Subnet | 172.16.10.3 | Allow | 53 | Allows VLAN 30 to make DNS requests |
| 172.16.20.2 | VLAN 10 Subnet | Allow | All | Access from Private PC in VLAN 20 |
| VLAN 10 Subnet | * | Allow | All | Allows machines to reach the internet |
| *	|	VLAN 10 Subnet | Block | All | Default Inbound Deny |

---

## VLAN 20 – General Network (172.16.1.0/24)
**Purpose:** User devices

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | VLAN20 | 172.16.2.3 (Splunk Server) | 22, 3389, 5900, 80, 443, 8000 | Access to lab servers (Splunk, RDP, web interfaces) |
| Allow | VLAN20 | 172.16.2.4 (Wazuh Server) | 1514, 1515, 55000, 9200 | Communication with EDR server |
| Allow | VLAN20 | 172.16.2.5 (Nessus Server) | 8834, 443 | Vulnerability scanner access |
| Allow | VLAN20 | 172.16.0.3 (Pi-Hole) | DNS (TCP/UDP 53) | Forward all DNS queries through Pi-hole |
| Allow | VLAN20 | 172.16.1.1 (PFSense) | NTP (UDP 123) | Time Management |
| Allow | 172.16.1.2 (Main Desktop) | VLAN30 | SSH (TCP 22), RDP (TCP 3389), VNC (TCP 5900) | Home Lab Management |
| Allow | VLAN20 | WAN | Any | Normal outbound traffic |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## VLAN 30 – Homelab / Servers (172.16.2.0/24)
**Purpose:** Servers and security tooling

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | 172.16.2.3 (Splunk Server) | VLAN10 | 8088, 8089, 9997, 8191 | Log ingestion from firewall / management |
| Allow | 172.16.2.4 (Wazuh Server) | VLAN20 | 1514, 1515, 55000, 9200 | EDR communication with general network |
| Allow | 172.16.2.5 (Nessus Server) | VLAN20 | 8834, 443 | Vulnerability scanning / reporting |
| Allow | 172.16.2.6 (Windows Server 2022) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | 172.16.2.7 (Windows 11 Workstation) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | 172.16.2.8 (Kali Linux) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | VLAN30 | 172.16.0.3 (Pi-Hole) | DNS (TCP/UDP 53) | Forward all DNS queries through Pi-hole |
| Allow | VLAN30 | 172.16.2.1 (PFSense) | NTP (UDP 123) | Time Management |
| Deny | 172.16.2.9 (Metasploitable) | WAN | Any | Isolate vulnerable system |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## VLAN 40 – IoT (172.16.3.0/24)
**Purpose:** Isolated smart devices

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | VLAN40 | 172.16.0.3 (Pi-Hole) | DNS (TCP/UDP 53) | Forward all DNS queries through Pi-hole |
| Allow | VLAN40 | WAN | DNS, HTTP/HTTPS | Limited outbound access for updates / cloud services |
| Allow | VLAN40 | 172.16.3.1 (PFSense) | NTP (UDP 123) | Time Management |
| Deny | VLAN40 | Internal VLANs | Any | Prevent IoT devices from accessing user / management networks |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## Notes
- All rules are **top-down processed**; specific allow rules must come before general deny.
- Pi-hole is centralized on VLAN10 to serve DNS requests for VLANs 10, 20, and 40. It queries WAN recursively.
- Default deny ensures a least-privilege posture.
