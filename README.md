# Homelab

This repository documents my homelab journey and serves as a way to showcase my progression into Cybersecurity, including the challenges, learning moments, and hands-on experience that come with building and maintaining a home lab.

---

## The Goal

The main goal of this homelab (besides it being really cool) is to create a contained environment where I can:

- Simulate security events
- Learn and experiment with common cybersecurity tools
- Build hands-on experience across networking, monitoring, and defensive security

A secondary goal is to improve and restructure my home network to make it more functional and secure.

Things I want to achieve here include:
- Proper Wi-Fi segregation between home and guest networks
- A NAS so my partner can store her *millions* of photos without paying for Google Drive
- A Plex server to digitise DVDs/Blu-rays and make them accessible at any time

---

## So, What’s the Plan?

The homelab will be built in **three phases**, each with a specific focus.

---

## Phase 1 – Networking ✔️

This phase focuses on building a solid networking foundation. The goal is to properly segment the network using VLANs, improve security, and gain hands-on experience that aligns with my **Network+ studies**.

### Devices in this phase:
- ~~[**Cisco Catalyst 3750 Switch**](https://github.com/Andur1n/Homelab/blob/main/Switch/README.md)~~
- [**Mikrotik - CRS112-8P-4S-IN**]
- [**Raspberry Pi** running **Pi-hole**](https://github.com/Andur1n/Homelab/blob/main/Pi-Hole/README.md)
- [**ThinkCentre M720q**](https://github.com/Andur1n/Homelab/blob/main/Firewall/README.md) with an additional **Intel I210 NIC**, functioning as a **pfSense firewall**

This setup allows:
- Network segmentation using VLANs
- DNS filtering and monitoring
- Firewall rules and traffic inspection
- Real-world networking practice alongside certification study

---

## Phase 2 – Server *(Currently in progress)*

In this phase, a dedicated server will be introduced to host multiple virtual machines and security tools.

### Hardware:

**Dell Optiplex 3090** - Gaming Server
- Intel i5 CPU (10th Generation)
- 16GB RAM
- 500GB NVME

**Dell Poweredge T140** - Lab Server
- Intel Xeon processor E-2200
- 16GB RAM - (looking to upgrade to 32GB of RAM. Expensive as it's ECC RAM)
- 2.5TB of HDD Storage

**QNAP TS-231P3 NAS** - Local NAS for file storage
- 4TB Storage (2x 2TB HDD configured in RAID 1)
- 4GB SODIMM DDR3
- 32-bit ARM processor


### Planned VMs and services:

- **Splunk** – SIEM monitoring
- **Wazuh** – Endpoint detection and response
- **Nessus** – Vulnerability scanning
- **Windows Server 2022** – Active Directory
- **Windows 11** – Domain-joined workstation
- **Kali Linux**
- **Metasploitable**
- **Minecraft Server** - Move it from a local VM to a server
- **Bitwarden Password Manager**

This list isn’t definitive, but it provides a solid foundation for building attack and defence scenarios.

---

## Phase 3 – Extras & Further Improvements

Once the core environment is stable (though homelabs are never really “finished”), the plan is to expand with some nice-to-have additions.

### Potential additions:
- **Ubiquiti Access Point**
  - Proper Wi-Fi coverage
  - Centralised management, likely hosted on the server

---

## Final Notes

This repository will continue to evolve as the homelab grows.  
Configuration details, diagrams, lessons learned, and troubleshooting notes will be added as each phase progresses.
