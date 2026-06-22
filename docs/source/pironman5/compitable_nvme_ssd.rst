.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _compitable_nvme_ssd_5:

.. start_compatible_nvme_ssd

SSD NVMe Compatibles
========================

SSDs Verificados como Compatibles
-----------------------------------

Los siguientes modelos de SSD NVMe han sido reportados por usuarios como funcionales con Raspberry Pi 5 y la serie Pironman5. Estos resultados se basan en pruebas de la comunidad e informes de uso real.

La compatibilidad puede variar según la versión del sistema operativo Raspberry Pi, la versión del kernel, el firmware EEPROM, el firmware del SSD, la calidad de la fuente de alimentación y las condiciones de carga de trabajo.

.. list-table:: SSDs NVMe Verificados como Compatibles
   :widths: 20 50 20
   :header-rows: 1

   * - Marca
     - Modelo
     - Capacidad
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


Generalmente Estables
------------------------

Estos modelos de SSD han sido ampliamente probados y son generalmente estables con Raspberry Pi 5 y configuraciones NVMe de Pironman.

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


Compatibles (Pueden Variar)
-----------------------------

Estos modelos de SSD pueden funcionar correctamente en muchas configuraciones, pero la compatibilidad o estabilidad puede variar según la carga de trabajo, la versión del firmware, la versión del EEPROM de Raspberry Pi, la calidad de la fuente de alimentación o la configuración PCIe.

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
  (Detectado correctamente, pero algunos usuarios reportaron errores de lectura/escritura a menos que PCIe se fuerce a Gen3 y ASPM se desactive usando ``pcie_aspm=off``.)


No Recomendados (Posible Inestabilidad)
-------------------------------------------------

Los siguientes SSDs o controladores pueden causar reinicios PCIe, errores de E/S, desconexiones o inestabilidad de arranque en las interfaces PCIe de Raspberry Pi 5.

* SSDs que utilizan controladores Phison E27T / E21
* Western Digital SN740
* WD BLACK 8TB SN850X
* Inland TN446 NVMe SSD
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* Otros SSDs NVMe que utilizan las mismas familias de controladores Phison


**Notas de Compatibilidad**

* La compatibilidad NVMe puede variar según la versión del sistema operativo Raspberry Pi, la versión del kernel, el firmware EEPROM, el firmware del SSD y la calidad de la fuente de alimentación.
* Se recomienda encarecidamente una fuente de alimentación USB-C de alta calidad de 5V/5A, especialmente para SSDs de alta capacidad o alto rendimiento.
* Algunos SSDs pueden funcionar correctamente como almacenamiento secundario pero mostrar inestabilidad cuando se usan como unidad de arranque.
* El funcionamiento exitoso reportado por los usuarios no siempre garantiza estabilidad a largo plazo bajo cargas de trabajo sostenidas.

.. end_compatible_nvme_ssd
