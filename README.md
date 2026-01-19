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

## Phase 1 – Networking *(Current Phase)*

This phase focuses on building a solid networking foundation. The goal is to properly segment the network using VLANs, improve security, and gain hands-on experience that aligns with my **Network+ studies**.

### Devices in this phase:
- **Cisco Catalyst 3750 Switch**
- [**Raspberry Pi** running **Pi-hole**](https://github.com/Andur1n/Homelab/blob/main/Pi-Hole/Readme.md)
- **ThinkCentre M720q** with an additional **Intel I210 NIC**, functioning as a **pfSense firewall**

This setup allows:
- Network segmentation using VLANs
- DNS filtering and monitoring
- Firewall rules and traffic inspection
- Real-world networking practice alongside certification study

---

## Phase 2 – Server

In this phase, a dedicated server will be introduced to host multiple virtual machines and security tools.

### Hardware:
- **Dell Optiplex 7060**
- Intel i5 CPU
- 64GB RAM

### Planned VMs and services:
- **Splunk** – SIEM monitoring
- **Wazuh** – Endpoint detection and response
- **Nessus** – Vulnerability scanning
- **Windows Server 2022** – Active Directory
- **Windows 11** – Domain-joined workstation
- **Kali Linux**
- **Metasploitable**

This list isn’t definitive, but it provides a solid foundation for building attack and defence scenarios.

---

## Phase 3 – Extras & Further Improvements

Once the core environment is stable (though homelabs are never really “finished”), the plan is to expand with some nice-to-have additions.

### Potential additions:
- **Ubiquiti Access Point**
  - Proper Wi-Fi coverage
  - Centralised management, likely hosted on the server
- **NAS**
  - 2TB–4TB storage
  - Split usage:
    - Plex media storage
    - Photo and general file storage

---

## Final Notes

This repository will continue to evolve as the homelab grows.  
Configuration details, diagrams, lessons learned, and troubleshooting notes will be added as each phase progresses.
