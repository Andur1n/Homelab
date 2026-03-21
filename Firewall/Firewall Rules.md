# Homelab Firewall Rules

## Design Principles
- Default deny (least privilege)
- VLAN-based network segmentation
- Stateful firewall (allow ESTABLISHED, RELATED traffic)
- Explicit allow rules for required services only
- Centralised DNS Enforcement (all clients must use Pi-Hole as a DNS server)
- Logging on critical rules

---

## VLAN 10 – Core / Management (172.16.0.0/24)
**Purpose:** Administrative access & Pi-hole

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | VLAN10 | Pi-hole (172.16.0.3) | DNS (TCP/UDP 53) | Management queries to Pi-hole |
| Allow | VLAN10 | WAN | HTTP/HTTPS (TCP 80 & 443) | Update services |
| Allow | VLAN10 | 172.16.0.1 (PFSense) | NTP (UDP 123) | Time Management |
| Allow | Pi-hole (172.16.0.3) | WAN | DNS (TCP/UDP 53) | Recursive DNS resolution for all VLANs |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## VLAN 20 – General Network (172.16.1.0/24)
**Purpose:** User devices

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | VLAN20 | Splunk Server (172.16.2.3) | 22, 3389, 5900, 80, 443, 8000 | Access to lab servers (Splunk, RDP, web interfaces) |
| Allow | VLAN20 | Wazuh Server (172.16.2.4) | 1514, 1515, 55000, 9200 | Communication with EDR server |
| Allow | VLAN20 | Nessus Server(172.16.2.5) | 8834, 443 | Vulnerability scanner access |
| Allow | VLAN20 | Pi-hole (172.16.0.3) | DNS (TCP/UDP 53) | Forward all DNS queries through Pi-hole |
| Allow | VLAN20 | 172.16.1.1 (PFSense) | NTP (UDP 123) | Time Management |
| Allow | Main Desktop (172.16.1.2) | VLAN30 | SSH (TCP 22), RDP (TCP 3389), VNC (TCP 5900) | Home Lab Management |
| Allow | VLAN20 | WAN | Any | Normal outbound traffic |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## VLAN 30 – Homelab / Servers (172.16.2.0/24)
**Purpose:** Servers and security tooling

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | Splunk (172.16.2.3) | VLAN10 | 8088, 8089, 9997, 8191 | Log ingestion from firewall / management |
| Allow | Wazuh (172.16.2.4) | VLAN20 | 1514, 1515, 55000, 9200 | EDR communication with general network |
| Allow | Nessus (172.16.2.5) | VLAN20 | 8834, 443 | Vulnerability scanning / reporting |
| Allow | Windows Server 2022 (172.16.2.6) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | Windows 11 (172.16.2.7) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | Kali Linux (172.16.2.8) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | VLAN30 | Pi-hole (172.16.0.3) | DNS (TCP/UDP 53) | Forward all DNS queries through Pi-hole |
| Allow | VLAN30 | 172.16.2.1 (PFSense) | NTP (UDP 123) | Time Management |
| Deny | Metasploitable (172.16.2.9) | WAN | Any | Isolate vulnerable system |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## VLAN 40 – IoT (172.16.3.0/24)
**Purpose:** Isolated smart devices

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | VLAN40 | Pi-hole (172.16.0.3) | DNS (TCP/UDP 53) | Forward all DNS queries through Pi-hole |
| Allow | VLAN40 | WAN | DNS, HTTP/HTTPS | Limited outbound access for updates / cloud services |
| Allow | VLAN40 | 172.16.3.1 (PFSense) | NTP (UDP 123) | Time Management |
| Deny | VLAN40 | Internal VLANs | Any | Prevent IoT devices from accessing user / management networks |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## Notes
- All rules are **top-down processed**; specific allow rules must come before general deny.
- Pi-hole is centralized on VLAN10 to serve DNS requests for VLANs 10, 20, and 40. It queries WAN recursively.
- Default deny ensures a least-privilege posture.
