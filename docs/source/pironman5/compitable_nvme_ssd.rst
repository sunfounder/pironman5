.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _compitable_nvme_ssd_5:

.. start_compatible_nvme_ssd

Compatible NVMe SSDs
========================

Verified Working SSDs
---------------------------

The following NVMe SSD models have been reported by users to work successfully with Raspberry Pi 5 and Pironman5 series. These results are based on community testing and real-world usage reports.

Compatibility may still vary depending on Raspberry Pi OS version, kernel version, EEPROM firmware, SSD firmware, power supply quality, and workload conditions.

.. list-table:: Verified Compatible NVMe SSDs
   :widths: 20 50 20
   :header-rows: 1

   * - Brand
     - Model
     - Capacity
   * - ADATA
     - XPG SPECTRIX S40G RGB
     - 256GB / 512GB
   * - ADATA
     - LEGEND 850 Lite
     - 512GB
   * - ADATA
     - LEGEND 700
     - 256GB
   * - Acer
     - FA100
     - 512GB
   * - Bestoss
     - GM528
     - 1TB
   * - Crucial
     - P1
     - 1TB
   * - Crucial
     - P2
     - 512GB / 1TB
   * - Crucial
     - P3
     - 1TB
   * - Crucial
     - P3 Plus
     - 512GB / 1TB / 2TB
   * - Crucial
     - P310
     - 512GB / 1TB / 2TB / 4TB+
   * - Crucial
     - T500
     - 512GB
   * - Ediloca
     - EN600 PRO
     - 256GB
   * - Fanxiang
     - S500 Pro
     - 256GB
   * - Fanxiang
     - S501
     - 1TB
   * - HUADISK
     - NVMe M.2 SSD
     - 256GB
   * - Intel
     - 660p SSDPEKNW512G8
     - 512GB
   * - KingSpec
     - M.2 NVMe SSD
     - 1TB
   * - Kingston
     - SNV2S
     - 512GB / 1TB
   * - Kingston
     - SNV3S
     - 1TB
   * - Kingston
     - Fury Renegade SFYRS500G
     - 512GB
   * - KIOXIA
     - EXCERIA M.2 NVMe SSD
     - 512GB
   * - Lexar
     - NM610 PRO
     - 512GB / 1TB / 2TB
   * - Lexar
     - NM620
     - 1TB
   * - Lexar
     - NM790
     - 4TB
   * - ORICO
     - J10
     - 256GB / 2TB
   * - ORICO
     - D10
     - 2TB
   * - Raspberry Pi
     - Raspberry Pi NVMe M.2 SSD
     - 512GB
   * - PNY
     - CS1031
     - 256GB
   * - PNY
     - XLR8 CS3040
     - 1TB
   * - Samsung
     - 970 EVO Plus
     - 512GB / 1TB / 2TB
   * - Samsung
     - 980
     - 250GB / 512GB / 1TB
   * - Samsung
     - 980 PRO
     - 1TB / 2TB
   * - Samsung
     - 990 EVO
     - 2TB
   * - Samsung
     - 990 EVO Plus
     - 512GB / 1TB
   * - Samsung
     - 990 PRO
     - 1TB
   * - Samsung
     - PM981
     - 512GB
   * - Samsung
     - MZ9LQ256HBJD PM991
     - 256GB
   * - Silicon Power
     - SP256GBP34A60M28
     - 256GB
   * - Toshiba
     - THNSN5256GPU7
     - 256GB
   * - TeamGroup
     - MP33 TM8FP6002T0C101
     - 2TB
   * - TeamGroup
     - MP33 Pro TM8FPD512G0C101
     - 512GB
   * - Transcend
     - MTE400S
     - 1TB
   * - Western Digital
     - WD Blue SN580
     - 512GB
   * - Western Digital
     - WD Blue SN550
     - 256GB

   
Generally Stable
------------------------

These SSD models have been widely tested and are generally stable with Raspberry Pi 5 and Pironman NVMe configurations.

* ADATA Legend 700
* ADATA Legend 800
* AData XPG SX8200 Pro
* Inland PCIe NVMe SSD
* KIOXIA EXCERIA NVMe SSD
* KIOXIA EXCERIA G2 NVMe SSD
* Kingston KC3000
* Kingston NV2
* Lexar NM710
* Lexar NM620
* Netac NV3000 NVMe SSD
* Netac NV2000 NVMe SSD
* Pineberry Pi Pinedrive (2280)
* PNY CS1030
* Sabrent Rocket 4.0
* Sabrent Rocket Nano
* Samsung 970 EVO Plus
* Samsung 980
* Samsung 980 Pro
* Samsung 990 Pro
* TeamGroup MP33
* Western Digital Blue SN550
* Western Digital SN530
* Western Digital SN570
* Western Digital Black SN750 SE
* XPG GAMMIX S70 BLADE
* XPG SX8200 Pro


Compatible (May Vary)
-----------------------------

These SSD models may work correctly in many setups, but compatibility or stability may vary depending on workload, firmware version, Raspberry Pi EEPROM version, power supply quality, or PCIe configuration.

* Crucial P2 M.2
* Crucial P3 M.2
* Crucial P3 Plus
* Crucial P310
* WD Blue SN580 series
* Western Digital Black SN770
* Western Digital Black SN850 series
* WD BLACK SN850X
* Samsung PM991
* Corsair MP600 SSD
* WD Blue SN5000 NVMe SSD
  (Detected successfully, but some users reported read/write errors unless PCIe is forced to Gen3 and ASPM is disabled using ``pcie_aspm=off``.)


Not Recommended (Potential Instability)
-------------------------------------------------

The following SSDs or controllers may cause PCIe resets, I/O errors, disconnects, or boot instability on Raspberry Pi 5 PCIe interfaces.

* SSDs using Phison E27T / E21 controllers
* Western Digital SN740
* WD BLACK 8TB SN850X
* Inland TN446 NVMe SSD
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* Other NVMe SSDs using the same Phison controller families


**Compatibility Notes**

* NVMe compatibility may vary depending on Raspberry Pi OS version, kernel version, EEPROM firmware, SSD firmware, and power supply quality.
* A high-quality 5V/5A USB-C power supply is strongly recommended, especially for high-capacity or high-performance SSDs.
* Some SSDs may work correctly as secondary storage but show instability when used as the boot drive.
* User-reported successful operation does not always guarantee long-term stability under sustained workloads.

.. end_compatible_nvme_ssd