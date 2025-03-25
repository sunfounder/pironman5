兼容的 NVMe SSD
========================

兼容的 NVMe SSD
---------------------------

* ADATA Legend 700
* ADATA Legend 800
* AData XPG SX8200 Pro

* Axe Memory Generic Drive

* Crucial P2 M.2
* Crucial P3 M.2
* Crucial P3 Plus M.2

* Inland PCIe NVMe SSD

* KIOXIA EXCERIA NVMe SSD
* KIOXIA EXCERIA G2 NVMe SSD

* Kingston KC3000
* Kingston NV2

* Lexar NM710
* Lexar NM620

* Netac NV3000 NVMe SSD
* Netac NV2000 NVMe SSD

* Origin Inception TLC830 Pro NVMe SSD
* Ortial ON-750-128 NVME SSD

* Pineberry Pi Pinedrive (2280)

* PNY CS1030

* Sabrent Rocket 4.0
* Sabrent Rocket Nano

* Samsung 970 EVO Plus
* Samsung 980
* Samsung 980 Pro
* Samsung 990 Pro

* Team MP33

* Western Digital SN850
* Western Digital SN740
* Western Digital SN570
* Western Digital SN530
* Western Digital Black SN750 SE (Phison 控制器)
* Western Digital Blue SN550 系列（如果你知道如何安装最新的 rpi-eeprom-updates，pieeprom-2024-01-24.bin 修复了 Western Digital Blue SN550 nvme 启动问题，参考 https://forums.raspberrypi.com/viewtopic.php?t=364327。）

* XPG GAMMIX S70 BLADE
* XPG SX8200 Pro


不兼容的 NVMe SSD
--------------------------

我们建议避免使用以下配备 Phison 控制器的 NVMe SSD 驱动器，因为它们已被证明与系统不兼容：

* WD Blue SN580 系列
* Western Digital Green SN350 系列
* Western Digital Black SN850 系列
* Western Digital Black SN770
* WD BLACK 8TB SN850X
* Inland tn446 nvme 驱动器
* Corsair MP600 SSD
* Samsung PM991
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* SN350 和 SN570 特别会导致 RPi 5 无法启动。
* 其他配备相同 Phison 控制器的 NVMe SSD 驱动器
