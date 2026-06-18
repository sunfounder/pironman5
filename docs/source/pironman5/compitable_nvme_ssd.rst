.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _compitable_nvme_ssd_5:

.. start_compatible_nvme_ssd

互換性のあるNVMe SSD
========================

動作確認済みSSD
---------------------------

以下のNVMe SSDモデルは、Raspberry Pi 5およびPironman5シリーズで正常に動作することがユーザーから報告されています。これらの結果はコミュニティテストと実際の使用報告に基づいています。

互換性は、Raspberry Pi OSのバージョン、カーネルバージョン、EEPROMファームウェア、SSDファームウェア、電源の品質、およびワークロード条件によって異なる場合があります。

.. list-table:: 動作確認済みNVMe SSD
   :widths: 20 50 20
   :header-rows: 1

   * - ブランド
     - モデル
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


一般的に安定
------------------------

これらのSSDモデルは広くテストされており、Raspberry Pi 5およびPironman NVMe構成で一般的に安定しています。

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


互換性あり（変動する可能性あり）
--------------------------------

これらのSSDモデルは多くのセットアップで正しく動作する可能性がありますが、互換性や安定性は、ワークロード、ファームウェアバージョン、Raspberry Pi EEPROMバージョン、電源品質、またはPCIe構成によって異なる場合があります。

* Crucial P2 M.2
* Crucial P3 M.2
* Crucial P3 Plus
* Crucial P310
* WD Blue SN580シリーズ
* Western Digital Black SN770
* Western Digital Black SN850シリーズ
* WD BLACK SN850X
* Samsung PM991
* Corsair MP600 SSD
* WD Blue SN5000 NVMe SSD
  （検出は成功しますが、PCIeをGen3に強制し、 ``pcie_aspm=off`` を使用してASPMを無効にしないと、一部のユーザーから読み取り/書き込みエラーが報告されています。）


非推奨（不安定の可能性）
-------------------------------------------------

以下のSSDまたはコントローラーは、Raspberry Pi 5のPCIeインターフェースでPCIeリセット、I/Oエラー、切断、または起動の不安定性を引き起こす可能性があります。

* Phison E27T / E21 コントローラーを使用するSSD
* Western Digital SN740
* WD BLACK 8TB SN850X
* Inland TN446 NVMe SSD
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* 同じPhisonコントローラーファミリーを使用するその他のNVMe SSD


**互換性に関する注意事項**

* NVMeの互換性は、Raspberry Pi OSのバージョン、カーネルバージョン、EEPROMファームウェア、SSDファームウェア、および電源品質によって異なる場合があります。
* 高品質の5V/5A USB-C電源を強く推奨します。特に大容量または高性能SSDを使用する場合に重要です。
* 一部のSSDはセカンダリストレージとして正常に動作しても、ブートドライブとして使用すると不安定になる場合があります。
* ユーザーから報告された正常動作は、持続的なワークロード下での長期的な安定性を常に保証するものではありません。

.. end_compatible_nvme_ssd
