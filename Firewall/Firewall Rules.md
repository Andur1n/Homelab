# Homelab Firewall Rules

## Design Principles
- Default deny (least privilege)
- VLAN-based network segmentation
- Stateful firewall (allow ESTABLISHED, RELATED traffic)
- Explicit allow rules for required services only
- Logging on critical rules

---

## VLAN 10 – Core / Management (172.16.0.0/24)
**Purpose:** Administrative access & Pi-hole

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | VLAN10 | VLAN30 | SSH (22), RDP (3389), HTTPS (443) | Management access to lab servers |
| Allow | VLAN10 | Pi-hole (172.16.0.3) | DNS (TCP/UDP 53) | Management queries to Pi-hole |
| Allow | Pi-hole (172.16.0.3) | WAN | DNS (TCP/UDP 53) | Recursive DNS resolution for all VLANs |
| Allow | VLAN10 | WAN | DNS, HTTPS | Admin outbound access |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## VLAN 20 – General Network (172.16.1.0/24)
**Purpose:** User devices

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | VLAN20 | VLAN30 | 22, 3389, 5900, 80, 443, 8000 | Access to lab servers (Splunk, RDP, web interfaces) |
| Allow | VLAN20 | Wazuh | 1514, 1515, 55000, 9200 | Communication with EDR server |
| Allow | VLAN20 | Nessus | 8834, 443 | Vulnerability scanner access |
| Allow | VLAN20 | Pi-hole (172.16.0.3) | DNS (TCP/UDP 53) | Forward all DNS queries through Pi-hole |
| Allow | VLAN20 | WAN | DNS, HTTP/HTTPS | Normal outbound traffic |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## VLAN 30 – Homelab / Servers (172.16.2.0/24)
**Purpose:** Servers and security tooling

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | Proxmox (172.16.2.2) | VLAN10 | SSH/RDP/HTTPS | Management access to Proxmox host |
| Allow | Splunk (172.16.2.3) | VLAN10 | 8088, 8089, 9997, 8191 | Log ingestion from firewall / management |
| Allow | Wazuh (172.16.2.4) | VLAN20 | 1514, 1515, 55000, 9200 | EDR communication with general network |
| Allow | Nessus (172.16.2.5) | VLAN20 | 8834, 443 | Vulnerability scanning / reporting |
| Allow | Windows Server 2022 (172.16.2.6) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | Windows 11 (172.16.2.7) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | Kali Linux (172.16.2.8) | WAN | Updates / package repos | Outbound traffic for updates |
| Allow | VLAN20 → VLAN30 | VLAN30 | DNS (TCP/UDP 53) | Forwarded DNS requests from users |
| Allow | VLAN40 → VLAN30 | VLAN30 | DNS (TCP/UDP 53) | Forwarded DNS requests from IoT devices |
| Deny | Metasploitable (172.16.2.9) | WAN | Any | Isolate vulnerable system |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## VLAN 40 – IoT (172.16.3.0/24)
**Purpose:** Isolated smart devices

| Rule | Source | Destination | Ports / Protocols | Description |
|------|--------|-------------|-----------------|------------|
| Allow | VLAN40 | Pi-hole (172.16.0.3) | DNS (TCP/UDP 53) | Forward all DNS queries through Pi-hole |
| Allow | VLAN40 | WAN | DNS, HTTP/HTTPS | Limited outbound access for updates / cloud services |
| Deny | VLAN40 | Internal VLANs | Any | Prevent IoT devices from accessing user / management networks |
| Deny | Any | Any | Any | Default deny all other traffic |

---

## Notes
- VLAN numbering is arbitrary; adjust based on your environment.
- All rules are **top-down processed**; specific allow rules must come before general deny.
- Pi-hole is centralized on VLAN10 to serve DNS requests for VLANs 10, 20, and 40. It queries WAN recursively.
- Default deny ensures a least-privilege posture.
- VLAN30 device IPs start at `.2` for Proxmox, then increment sequentially.
