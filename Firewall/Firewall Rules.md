# Homelab Firewall Rules

## Design Principles
- Default deny (least privilege)
- VLAN-based network segmentation
- Stateful firewall (allow ESTABLISHED, RELATED traffic)
- Centralised DNS Enforcement (all clients must use Pi-Hole as a DNS server except IoT)
- Logging on critical rules

---

## VLAN 10 – Core / Management (172.16.10.0/24)
**Purpose:** Administrative access & Pi-hole

| From | To | Action | Port | Note |
|------|--------|-------------|-----------------|------------|
| VLAN 20 Subnet | 172.16.10.3 | Allow | 53 | Allows VLAN 20 to make DNS requests |
| VLAN 30 Subnet | 172.16.10.3 | Allow | 53 | Allows VLAN 30 to make DNS requests |
| 172.16.20.2 | VLAN 10 Subnet | Allow | All | Access from Private PC in VLAN 20 |
| VLAN 10 Subnet | * | Allow | All | Allows machines to reach the internet |
| *	|	VLAN 10 Subnet | Block | All | Default Inbound Deny |

---

## VLAN 20 – General Network (172.16.20.0/24)
**Purpose:** User devices, Gaming Server and NAS

| From | To | Action | Port | Note |
|------|--------|-------------|-----------------|------------|
| VLAN 20 Subnet | 172.16.10.3 | Allow | 53 | Allows devices to make DNS requests with Pi-Hole on VLAN 10 |
| VLAN 20 Subnet | * | Allow | All | Allows machines to reach the internet |
| * | VLAN 20 Subnet | Block | All | Default Inbound Deny |

---

## VLAN 30 – Homelab / Servers (172.16.30.0/24)
**Purpose:** Lab, Security Tools etc.

| From | To | Action | Port | Note |
|------|--------|-------------|-----------------|------------|
| VLAN 30 Subnet | 172.16.10.3 | Allow | 53 | Allows devices to make DNS requests with Pi-Hole on VLAN 10 |
| 172.16.20.2 | VLAN 30 Subnet | Allow | All | Access from Private PC in VLAN 20 |
| VLAN 30 Subnet | VLAN 10 Subnet | Block | All | Block devices from talking to VLAN 10 - General Rule |
| VLAN 30 Subnet | VLAN 20 Subnet | Block | All | Block devices from talking to VLAN 20 - General Rule |
| VLAN 30 Subnet | VLAN 40 Subnet | Block | All | Block devices from talking to VLAN 40 - General Rule |
| VLAN 30 Subnet | * | Allow | All | Allows machines to reach the internet |
| * | VLAN 30 Subnet | Block | All | Default Inbound Deny |


---

## VLAN 40 – IoT (172.16.3.0/24)
**Purpose:** Isolated smart devices

| From | To | Action | Port | Note |
|------|--------|-------------|-----------------|------------|
| VLAN 40 Subnet | VLAN 10 Subnet | Block | All | Block devices from talking to VLAN 10 - General Rule |
| VLAN 40 Subnet | VLAN 20 Subnet | Block | All | Block devices from talking to VLAN 20 - General Rule |
| VLAN 40 Subnet | VLAN 30 Subnet | Block | All | Block devices from talking to VLAN 30 - General Rule |
| VLAN 40 Subnet | * | Allow | All | Allows machines to reach the internet |
| * | VLAN 40 Subnet | Block | All | Default Inbound Deny |


---

## Notes
- All rules are **top-down processed**; specific allow rules must come before general deny.
- Pi-hole is centralized on VLAN10 to serve DNS requests for VLANs 10, 20, and 40. It queries WAN recursively.
- Default deny ensures a least-privilege posture.
