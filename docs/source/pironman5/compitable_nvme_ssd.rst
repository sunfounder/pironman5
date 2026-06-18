.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _compitable_nvme_ssd_5:

.. start_compatible_nvme_ssd

NVMe SSD compatibili
========================

SSD verificati funzionanti
----------------------------

I seguenti modelli di SSD NVMe sono stati segnalati dagli utenti come funzionanti con Raspberry Pi 5 e la serie Pironman5. Questi risultati si basano su test della community e segnalazioni di utilizzo reale.

La compatibilità può comunque variare in base alla versione di Raspberry Pi OS, alla versione del kernel, al firmware EEPROM, al firmware dell'SSD, alla qualità dell'alimentazione e alle condizioni di carico di lavoro.

.. list-table:: SSD NVMe compatibili verificati
   :widths: 20 50 20
   :header-rows: 1

   * - Marca
     - Modello
     - Capacità
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


Generalmente stabili
------------------------

Questi modelli di SSD sono stati ampiamente testati e sono generalmente stabili con Raspberry Pi 5 e configurazioni NVMe Pironman.

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


Compatibili (possono variare)
-------------------------------

Questi modelli di SSD potrebbero funzionare correttamente in molte configurazioni, ma la compatibilità o la stabilità possono variare in base al carico di lavoro, alla versione del firmware, alla versione EEPROM del Raspberry Pi, alla qualità dell'alimentazione o alla configurazione PCIe.

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
  (Rilevato con successo, ma alcuni utenti hanno segnalato errori di lettura/scrittura a meno che PCIe non sia forzato a Gen3 e ASPM sia disabilitato usando ``pcie_aspm=off``.)


Non consigliati (potenziale instabilità)
-------------------------------------------------

I seguenti SSD o controller possono causare reset PCIe, errori di I/O, disconnessioni o instabilità di avvio sulle interfacce PCIe del Raspberry Pi 5.

* SSD che utilizzano controller Phison E27T / E21
* Western Digital SN740
* WD BLACK 8TB SN850X
* Inland TN446 NVMe SSD
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* Altri SSD NVMe che utilizzano le stesse famiglie di controller Phison


**Note sulla compatibilità**

* La compatibilità NVMe può variare in base alla versione di Raspberry Pi OS, alla versione del kernel, al firmware EEPROM, al firmware dell'SSD e alla qualità dell'alimentazione.
* Si consiglia vivamente un alimentatore USB-C di alta qualità da 5V/5A, specialmente per SSD di alta capacità o prestazioni elevate.
* Alcuni SSD potrebbero funzionare correttamente come archiviazione secondaria ma mostrare instabilità se utilizzati come disco di avvio.
* Il funzionamento riuscito segnalato dagli utenti non garantisce sempre la stabilità a lungo termine sotto carichi di lavoro sostenuti.

.. end_compatible_nvme_ssd
