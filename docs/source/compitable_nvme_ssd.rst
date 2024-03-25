Compitable NVME SSD
========================

Compitable NVME SSD
---------------------------

* ADATA Legend 700
* ADATA Legend 800
* AData XPG SX8200 Pro

* Axe Memory Generic Drive

* Crucial P2 M.2
* Crucial P3 M.2
* Crucial P3 Plus M.2

* Inland PCIe NVMe SSD

* KIOXIA EXCERIA NVME SSD
* KIOXIA EXCERIA G2 NVME SSD

* Kingston KC3000
* Kingston NV2

* Lexar NM710
* Lexar NM620

* Netac NV3000 NVMe SSD
* Netac NV2000 NVMe SSD

* Origin Inception TLC830 Pro NVMe SSD

* Pineberry Pi Pinedrive (2280)

* PNY CS1030

* Sabrent Rocket 4.0
* Sabrent Rocket Nano

* Samsung 970 EVO Plus
* Samsung 980
* Samsung 980 Pro

* Team MP33

* Western Digital SN850
* Western Digital SN740
* Western Digital SN570
* Western Digital SN530
* Western Digital Black SN750 SE (Phison Controller)
* Western Digital Blue SN550/SN580 series (If you know how to install latest rpi-eeprom-updates, pieeprom-2024-01-24.bin fixed the Western Digital Blue SN550 nvme boot issue Refer to https://forums.raspberrypi.com/viewtopic.php?t=364327.)

* XPG GAMMIX S70 BLADE
* XPG SX8200 Pro


Uncompitable NVME SSD
--------------------------

We recommend avoiding the following NVMe SSD drives which is equipped with a Phison controller due to their proven incompatibility:

* Western Digital Green SN350 series
* Western Digital Black SN850 series
* Western Digital Black SN770
* Inland tn446 nvme drive
* Corsair MP600 SSD
* Samsung PM991
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* SN350 and SN570 prevented the RPi 5 from booting at all especially.
* Other NVMe SSD drivers equipped with the same Phison controller