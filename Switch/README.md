# Cisco WS-C3750-24PS-S

## 📘 Intro

Every good home lab needs a proper switch. As my ISP router only had 4 ports and no VLAN flexibility, it was time to take a deeper dive into switches and how they work.

---

## 🖥️ Hardware

I came to the conclusion fairly early that I wanted a Cisco switch. The main reason behind this is that I’ve seen them used a lot in enterprise environments, and the Net+ exam touches on the commands ever so slightly. My goal with the switch was to learn networking commands and how to properly configure a Cisco switch in the process.

I had the following requirements:

- It needs VLAN capabilities  
- I need to be able to SSH into the device remotely to configure it  
- It needs to have PoE so I can run my Pi-hole (which now has a PoE hat) from the switch rather than it occupying a power socket  
- It needs to have Gigabit ports at minimum  

I quickly found three switches that caught my eye:

- Catalyst 2960  
- Catalyst 3750  
- Catalyst 3850  

The 2960 was written off pretty quickly due to not having Gigabit ports, which would have limited speeds to 100 Mbps maximum. The choice was then between the 3750 and its newer brother, the 3850. Although the 3850 is newer and a noticeable jump in price, I decided to stick with the 3750 for the time being — a decision I later regretted (see conclusion for details).

---

## 💿 Installation

The 3750 arrived, and after some light troubleshooting I discovered the previous owner had fully reset it to factory defaults (generally a good thing). However, this meant there was no way to remotely manage the switch without using an RS-232 serial cable. I purchased one, which allowed me to enable SSH and communicate with the switch remotely.

We then ran into the next challenge. Because the switch is quite old (late 2000s), it uses SHA-1 for SSH encryption, which is no longer considered secure in 2026. Modern Linux systems disable this method by default. I therefore had to modify my SSH config file (`~/.ssh/config`) and add the following entry:

```
Host old-device
HostName 192.168.1.10
User admin
HostKeyAlgorithms +ssh-rsa
PubkeyAcceptedAlgorithms +ssh-rsa
KexAlgorithms +diffie-hellman-group1-sha1
```

After this, I was finally able to access the switch and manage it remotely.

From there, I started by creating VLANs and assigning them to ports using the following commands:

- `interface <interface name><interface number>` — selects the interface you want to modify  
- `switchport mode trunk` — tells the switch to trunk VLAN traffic over this interface. On modern switches this often trunks all VLANs automatically, but on older switches you must define them manually  
- `switchport trunk allowed vlan <VLAN IDs>` — specifies which VLANs can be trunked over the interface  
- `switchport access vlan <VLAN ID>` — assigns the interface to a specific VLAN  

These were the main commands I used to configure the switch. For full configuration details, refer to the [config file](https://github.com/Andur1n/Homelab/blob/main/Switch/Current%20Config.txt) and [VLAN report](https://github.com/Andur1n/Homelab/blob/main/Switch/VLAN%20Brief.txt).

The only issue I ran into during setup was that the switch wouldn’t communicate properly with the firewall. After some troubleshooting, I discovered the IP range configured on the switch interface didn’t match the firewall subnet. Once I corrected that, they communicated immediately.

---

### SFP Side Note

This switch has two SFP ports. I found a cheap SFP module on Amazon and decided to use it for the uplink port. After further reading, I realised I was quite lucky that it worked — Cisco devices can be picky about third-party SFP modules, although older generation switches tend to be more flexible.

![SFP Picture](https://github.com/Andur1n/Homelab/blob/main/Switch/SFP.jpg)

---

## 🏁 Conclusion

Setting this up was easier than configuring the firewall, likely because I’d already spent around 20 hours in Packet Tracer for Net+, where I forced myself to configure everything via CLI. That learning definitely paid off — most commands are now stuck in my head and I only needed to look up the occasional one. I’d be interested to see how this compares when working with newer Cisco switches.

Now to the decision that made me regret buying the 3750:

**It’s loud. Very loud.**

I’ve even put it in a cupboard and it can still be heard. It’s also quite power hungry. After doing the calculations, it would cost roughly **£150 per year** to run 24/7. To top it off, the 24 non-uplink ports are limited to **100 Mbps**, whereas I originally thought they were all Gigabit.

I considered upgrading to a 3850 later, as it would solve the speed limitation, but that model is even more power hungry.

For the final version of the network, I may look at something like a smaller managed switch instead — quieter, more efficient, and still capable of Gigabit + PoE. If expansion is needed later, I could always add a larger enterprise switch and only power it on when required.

---

**To be continued.**
