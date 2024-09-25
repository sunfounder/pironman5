# Pironman 5

Pironman 5 case

Quick Links:

- [Pironman 5](#pironman-5)
  - [About Pironman5](#about-pironman5)
  - [Links](#links)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Update](#update)
  - [Compatible Systems](#compatible-systems)
    - [Ubuntu 24.04 server eth0 and wifi not work](#ubuntu-2404-server-eth0-and-wifi-not-work)
    - [Debug](#debug)
  - [About SunFounder](#about-sunfounder)
  - [Contact us](#contact-us)

## About Pironman5

## Links

- SunFounder Online Store &emsp; <https://www.sunfounder.com/>
- Documentation &emsp; <https://docs.sunfounder.com/en/latest/>

## Installation

For systems that don't have git, python3 pre-installed you need to install them first

```bash
sudo apt-get update
sudo apt-get install git python3 -y
```

Execute the installation script

```bash
cd ~
git clone https://github.com/sunfounder/pironman5.git
cd ~/pironman5
sudo python3 install.py
```

## Usage

-

## Update

<https://github.com/sunfounder/pironman5/blob/main/CHANGELOG.md>

## Compatible Systems

Systems that passed the test on the Raspberry Pi 5:

System | is compatible ?
:---   | :---  
Raspberry Pi OS Desktop - bookworm (32/64 bit) | &#x2705;
Raspberry Pi OS lite - bookworm (32/64 bit) | &#x2705;
Ubuntu Desktop 24.04 (64 bit) | &#x2705;
Ubuntu Server 24.04 (64 bit) | &#x2705;
Kali Linux 2024-05-15 | GPIO Fan Not Working
Home Assistant OS 12.3 | &#x2705;
Homebridge | &#x2705;
Batocera Linux | &#x2705;

### Ubuntu 24.04 server eth0 and wifi not work

https://www.reddit.com/r/Ubuntu/comments/1d0s8v5/ubuntu_2404_server_on_my_raspberry_pi_5_and_eth0/


### Debug

Command log:

```bash
cd ~/pironman5
sudo /opt/pironman5/venv/bin/pip3 uninstall pironman5 -y
sudo /opt/pironman5/venv/bin/pip3 install .

cd ~/pm_dashboard
sudo /opt/pironman5/venv/bin/pip3 uninstall pm_dashboard -y
sudo /opt/pironman5/venv/bin/pip3 install .

cd ~/pm_auto
sudo /opt/pironman5/venv/bin/pip3 uninstall pm_auto -y
sudo /opt/pironman5/venv/bin/pip3 install .

cd ~/sf_rpi_status
sudo /opt/pironman5/venv/bin/pip3 uninstall sf_rpi_status -y
sudo /opt/pironman5/venv/bin/pip3 install .

sudo systemctl stop pironman5
sudo systemctl start pironman5
sudo systemctl restart pironman5
sudo pironman5 start

sudo /opt/pironman5/venv/bin/python3

```

## About SunFounder

SunFounder is a company focused on STEAM education with products like open source robots, development boards, STEAM kit, modules, tools and other smart devices distributed globally. In SunFounder, we strive to help elementary and middle school students as well as hobbyists, through STEAM education, strengthen their hands-on practices and problem-solving abilities. In this way, we hope to disseminate knowledge and provide skill training in a full-of-joy way, thus fostering your interest in programming and making, and exposing you to a fascinating world of science and engineering. To embrace the future of artificial intelligence, it is urgent and meaningful to learn abundant STEAM knowledge.

## Contact us

website:
    www.sunfounder.com

E-mail:
    service@sunfounder.com
