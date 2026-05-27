
.. start_compatible_nvme_ssd

兼容的 NVMe SSD
========================

已验证可正常工作的 SSD
---------------------------

以下 NVMe SSD 型号已由用户报告可在 Raspberry Pi 5 和 Pironman5 系列上成功使用。这些结果基于社区测试和实际使用反馈。

兼容性仍可能因 Raspberry Pi OS 版本、内核版本、EEPROM 固件、SSD 固件、电源质量和工作负载条件而异。

.. list-table:: 已验证兼容的 NVMe SSD
   :widths: 20 50 20
   :header-rows: 1

   * - 品牌
     - 型号
     - 容量
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


总体稳定
------------------------

以下 SSD 型号已广泛测试，在 Raspberry Pi 5 和 Pironman NVMe 配置中通常表现稳定。

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


兼容（可能因人而异）
-----------------------------

以下 SSD 型号在许多设置中可能正常工作，但兼容性或稳定性可能因工作负载、固件版本、Raspberry Pi EEPROM 版本、电源质量或 PCIe 配置而异。

* Crucial P2 M.2
* Crucial P3 M.2
* Crucial P3 Plus
* Crucial P310
* WD Blue SN580 系列
* Western Digital Black SN770
* Western Digital Black SN850 系列
* WD BLACK SN850X
* Samsung PM991
* Corsair MP600 SSD
* WD Blue SN5000 NVMe SSD
  （可成功检测，但部分用户报告除非强制 PCIe 为 Gen3 并使用 ``pcie_aspm=off`` 禁用 ASPM，否则会出现读写错误。）


不推荐（潜在不稳定）
-------------------------------------------------

以下 SSD 或控制器可能在 Raspberry Pi 5 PCIe 接口上导致 PCIe 重置、I/O 错误、断开连接或启动不稳定。

* 使用 Phison E27T / E21 控制器的 SSD
* Western Digital SN740
* WD BLACK 8TB SN850X
* Inland TN446 NVMe SSD
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* 其他使用相同 Phison 控制器系列的 NVMe SSD


**兼容性说明**

* NVMe 兼容性可能因 Raspberry Pi OS 版本、内核版本、EEPROM 固件、SSD 固件和电源质量而异。
* 强烈建议使用高质量的 5V/5A USB-C 电源适配器，尤其对于大容量或高性能 SSD。
* 某些 SSD 作为辅助存储可能正常工作，但在用作启动盘时可能表现出不稳定性。
* 用户报告的成功操作并不总能保证在持续工作负载下的长期稳定性。

.. end_compatible_nvme_ssd
