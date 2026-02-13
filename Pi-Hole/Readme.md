# Pi-Hole

## Intro

First step of the homelab! I started off with this as I thought it would be a nice little project: easy to implement in my already existing network for the time being and a good way to build further on my Linux knowledge.  

Had a massive win as well — my boss provided us with £150 worth of Amazon vouchers for Christmas. I purchased the following kit to get started:

- Raspberry Pi 5 – 4GB RAM  
- 60GB Micro-SD Card  
- USB-C Power Plug  
- Case  
- Mini-HDMI to HDMI Cable

If you're thinking of picking up a kit yourself I used the starter kit below.

[iRasptek Starter Kit for Raspberry Pi 5 RAM 4GB - 64GB Edition of OS-Bookworm Pre-Loaded (Red&White Case)](https://www.amazon.co.uk/dp/B0D1CT4KZS?ref=ppx_yo2ov_dt_b_fed_asin_title)

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

## Update - 13/02/2026

We've officially been running Pi-hole for 1.5 months now as our DNS server, and we’ve not had any issues accessing anything we’ve needed.

About three weeks ago, I tried moving my main PC to Fedora Linux; however, this introduced too many complications in terms of how I use my desktop on a daily basis.

In the end, I decided to move back to Windows 11. On the fresh install, I did run the PowerShell script below, which disables a lot of Microsoft tracking features as well as removes much of the bloatware that comes with Windows 11.

[Raphire - Win11Debloat](https://github.com/Raphire/Win11Debloat)

Since then, over the last three weeks, I’ve seen a significant drop in the block percentage — from around 60% down to 41.3%. I might also look at running this script on my partner's PC to see whether this further reduces the number of blocked requests.

![Current Stats](https://github.com/Andur1n/Homelab/blob/main/Pi-Hole/Stats.png)

In the meantime I have purchased a bigger case as well as installed the POE hat on the Raspberry Pi as show below to future proof it and save that extra power cord needed. Below are the links of the POE Hat and case.

- [POE Hat](https://thepihut.com/products/power-over-ethernet-hat-g-for-raspberry-pi-5)
- [Case](https://thepihut.com/products/highpi-pro-5s-case-for-raspberry-pi-5)

![POE Hat](https://github.com/Andur1n/Homelab/blob/main/Pi-Hole/POE%20Hat.jpg)
