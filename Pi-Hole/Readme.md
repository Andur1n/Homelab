# Pi-Hole

## Intro

First step of the homelab! I started off with this as I thought it would be a nice little project: easy to implement in my already existing network for the time being and a good way to build further on my Linux knowledge.  

Had a massive win as well — my boss provided us with £150 worth of Amazon vouchers for Christmas. I purchased the following kit to get started:

- Raspberry Pi 5 – 4GB RAM  
- 60GB Micro-SD Card  
- USB-C Power Plug  
- Case  
- Mini-HDMI to HDMI Cable  

---

## Setting up the Raspberry Pi

The kit is great and comes with Debian Bookworm pre-installed on the MicroSD card, which saves quite a bit of time installing Linux on the device.  

First step: create a user account and update the device:

```bash
sudo apt update
sudo apt upgrade
```

After 5–10 minutes, the device was fully up to date. Next, I needed to set a static IP address. Originally I tried using `ifconfig`, but this produced some error messages.

The learning moment here was my first proper introduction to `SystemD`. Since around 2015, all modern Linux distributions use SystemD, which manages key services on Linux and interacts with the kernel. Following some research, I found that nmtui provides a manual interface in the Linux CLI, which allowed me to make the required network configuration.

For now, I set a static IP on Wi-Fi only, because I currently don’t have free ethernet ports on my ISP router. Down the line, I plan to expand the homelab with a bigger switch and give the Raspberry Pi a PoE hat (they’re only £15), which would allow me to get rid of the power plug in a future setup.

I’m also a sucker for centralized management: I enabled `SSH` and `VNC` on the device and added the entries to Remote Desktop Manager on my laptop. Highly recommended — it’s free for personal use, super customizable, and lets you manage all local devices, access methods, and passwords in one place.

---

## Setting up Pi-Hole

Installation was straightforward using the following bash commands:

```bash
git clone --depth 1 https://github.com/pi-hole/pi-hole.git Pi-hole
cd "Pi-hole/automated install/"
sudo bash basic-install.sh
```

Once installed, I confirmed the device was working by accessing its web portal via HTTP.

Next, I logged into my ISP router and forwarded all DNS traffic to the Pi-Hole, setting it to make recursive requests to **1.1.1.1** and **1.0.0.1** (Cloudflare). This immediately started showing traffic.

After 2 weeks of running the device, I can confirm ads are drastically reduced. We still get the occasional ad on Chromecast or Twitch, but they’re much shorter (though I might be imagining this).

---

## Blocklists

My brother recommended adding this blocklist:

[Hagezi Blocklist](https://github.com/hagezi/dns-blocklists)

I’ve been running it for two weeks and it currently blocks about 65% of all DNS requests. So far, neither me nor my partner have had any problems accessing sites we need. Interestingly, the biggest offender is Microsoft Services, responsible for almost 13,000 of the 30,000 blocked requests.

As I’m planning to switch my gaming rig to Fedora Linux, I wonder if the percentage of blocked requests will drop. 

To be continued…
