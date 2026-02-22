# PFSense Firewall – ThinkCentre M720q

## 📘 Intro

When looking for a firewall solution, the goal was to find one that would give me the most freedom of choice/options while also keeping the price low and avoiding vendor lock-in. After some research, I landed on **PFSense** as it’s free, open source, and I’ve got some light experience setting it up from back in my servicedesk role.

Considered Alternatives:
- OPNsense
- Ubiquiti Gateway
- Cisco ASA

> ⚠️ **Note:** This is a living document and not definitive. It may expand further as the lab evolves and grows.

---

## 🖥️ Hardware

For hardware, I landed on a **ThinkCentre M720q**. Over the last few months I’ve grown very fond of the idea of having a lab running on micro form factor PCs, and even the older 8th generation machines are very affordable and still pack a punch. I wasn’t too bothered about the idea of an i3 processor; however, I did decide to go with **16GB of RAM** to future-proof it.

**Specs:**

- Intel i3-8100T Processor  
- 16GB DDR4-2666MHz  
- 240GB NVMe SSD Storage  

As the PC will be functioning as a firewall, it requires a second network port. This was another reason I chose the M720q, as it supports an **extension riser**, allowing installation of an additional PCIe network card.

I went with an **Intel i210 NIC**. My priority was supporting high-speed connectivity across the network, so it needed to support **1Gb speeds**, which matches my current home network limit. Installation was straightforward and the card was recognised immediately in the BIOS.

> Minor nitpick: there’s no screw securing the card in place. Not a major issue, as it doesn’t move once the case lid is closed.

![Install](https://github.com/Andur1n/Homelab/blob/main/Firewall/install.jpg)

---

## 💿 Installation

First I updated the BIOS of the M720q via the Windows that was already installed on the device. This upgraded it to version **M1UKT78A/1.0.0.120**.

I downloaded the ISO image from the PFSense website and created a bootable USB using **Rufus**. The first issue I encountered was the firewall freezing during boot from USB with the below error.

![Boot Error](https://github.com/Andur1n/Homelab/blob/main/Firewall/error.jpg)

After some troubleshooting, I discovered PFSense can hang while initializing wireless interfaces. Disabling the wireless card in BIOS (not needed anyway) resolved the problem and allowed installation to proceed.

The installation itself was straightforward:

- Configured it to act as its own **DHCP server**
- Set ISP router as **WAN**
- Assigned LAN and WAN interfaces

After installation, the firewall rebooted into the CLI menu. It initially assigned the same subnet range to both WAN and LAN. I temporarily left this as-is and swapped the WAN/LAN cables so the firewall treated the ISP router as LAN. This allowed access to the web interface from my laptop for configuration for the time being.

![Main Menu](https://github.com/Andur1n/Homelab/blob/main/Firewall/post-install.jpg)

---

## 🎯 Initial Configuration Goals

- Create VLANs **10, 20, 30, 40**
- Configure LAN subinterfaces for each VLAN
- Configure DHCP scopes per VLAN
- Disable main LAN interface
- Configure trunk port to communicate with Cisco3750 switch
- Create baseline firewall rules for inter-VLAN + WAN access (to refine later)

During VLAN setup, I was prompted to assign QoS priorities. I configured them as:

1. **Highest priority** — Core infrastructure (switch, firewall, Pi-hole)
2. **Medium priority** — Gaming PCs
3. **Lower priority** — All other traffic

Everything was successfully configured and communicating as intended.

---

## 🧩 Challenges

The biggest issue (which took about **3–4 hours** to troubleshoot) was a test PC failing to obtain an IP address. It kept assigning itself a **169.x.x.x** APIPA address, indicating it sent a DHCP Discover but never received an Offer.

I initially suspected:

- Active parent interface conflicting with subinterfaces
- Firewall misconfiguration

In classic troubleshooting fashion, the firewall wasn’t the problem at all.

The real issue was that the **switch IP address didn’t match the firewall subnet**, meaning they couldn’t communicate. Once corrected, DHCP worked immediately and everything functioned as expected.

---

## 🏁 Conclusion

This was a really fun project, although it took quite a bit of time to get everything dialed in. The PFSense firewall has far more functionality than I expected (and it’s free!), and I’m confident that without having completed Network+ and Packet Tracer labs beforehand, I would have struggled to configure this successfully.

---

## 📌 Future Improvements

- Harden firewall rules  
- Add monitoring + logging stack  
- Implement network segmentation policies  
- Introduce IDS/IPS testing  

---
## Tested On:

- pfSense CE 2.8.1
- BIOS version M1UKT78A/1.0.0.120
