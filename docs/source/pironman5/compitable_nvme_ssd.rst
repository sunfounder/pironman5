.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. start_compatible_nvme_ssd

Kompatible NVMe SSDs
========================

Bestätigt funktionierende SSDs
-------------------------------

Die folgenden NVMe-SSD-Modelle wurden von Benutzern als erfolgreich mit Raspberry Pi 5 und der Pironman5-Serie arbeitend gemeldet. Diese Ergebnisse basieren auf Community-Tests und realen Nutzungsberichten.

Die Kompatibilität kann je nach Raspberry Pi OS-Version, Kernel-Version, EEPROM-Firmware, SSD-Firmware, Stromversorgungsqualität und Arbeitslastbedingungen variieren.

.. list-table:: Bestätigt kompatible NVMe-SSDs
   :widths: 20 50 20
   :header-rows: 1

   * - Marke
     - Modell
     - Kapazität
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


Allgemein stabil
------------------------

Diese SSD-Modelle wurden umfassend getestet und sind im Allgemeinen stabil mit Raspberry Pi 5 und Pironman NVMe-Konfigurationen.

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


Kompatibel (Kann variieren)
-----------------------------

Diese SSD-Modelle können in vielen Konfigurationen korrekt funktionieren, aber die Kompatibilität oder Stabilität kann je nach Arbeitslast, Firmware-Version, Raspberry Pi EEPROM-Version, Stromversorgungsqualität oder PCIe-Konfiguration variieren.

* Crucial P2 M.2
* Crucial P3 M.2
* Crucial P3 Plus
* Crucial P310
* WD Blue SN580 Serie
* Western Digital Black SN770
* Western Digital Black SN850 Serie
* WD BLACK SN850X
* Samsung PM991
* Corsair MP600 SSD
* WD Blue SN5000 NVMe SSD
  (Erfolgreich erkannt, aber einige Benutzer berichteten von Lese-/Schreibfehlern, es sei denn, PCIe wird auf Gen3 erzwungen und ASPM mit ``pcie_aspm=off`` deaktiviert.)


Nicht empfohlen (Potenzielle Instabilität)
-------------------------------------------------

Die folgenden SSDs oder Controller können auf PCIe-Schnittstellen des Raspberry Pi 5 PCIe-Resets, E/A-Fehler, Verbindungsabbrüche oder Boot-Instabilität verursachen.

* SSDs mit Phison E27T / E21 Controllern
* Western Digital SN740
* WD BLACK 8TB SN850X
* Inland TN446 NVMe SSD
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* Andere NVMe-SSDs mit denselben Phison-Controller-Familien


**Kompatibilitätshinweise**

* Die NVMe-Kompatibilität kann je nach Raspberry Pi OS-Version, Kernel-Version, EEPROM-Firmware, SSD-Firmware und Stromversorgungsqualität variieren.
* Eine hochwertige 5V/5A USB-C-Stromversorgung wird dringend empfohlen, insbesondere für SSDs mit hoher Kapazität oder hoher Leistung.
* Einige SSDs können als sekundärer Speicher korrekt funktionieren, zeigen jedoch Instabilität, wenn sie als Boot-Laufwerk verwendet werden.
* Ein von Benutzern gemeldeter erfolgreicher Betrieb garantiert nicht immer langfristige Stabilität unter Dauerlast.

.. end_compatible_nvme_ssd