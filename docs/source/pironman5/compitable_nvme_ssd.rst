.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _compitable_nvme_ssd_5:

.. start_compatible_nvme_ssd

SSD NVMe compatibles
======================

Modèles vérifiés (fonctionnels)
---------------------------------

Les modèles de SSD NVMe suivants ont été signalés par les utilisateurs comme fonctionnant avec le Raspberry Pi 5 et la gamme Pironman5. Ces résultats reposent sur des tests communautaires et des retours d'utilisation réels.

La compatibilité peut néanmoins varier selon la version de Raspberry Pi OS, la version du noyau, le firmware EEPROM, le firmware du SSD, la qualité de l'alimentation et les conditions de charge.

.. list-table:: SSD NVMe vérifiés comme compatibles
   :widths: 20 50 20
   :header-rows: 1

   * - Marque
     - Modèle
     - Capacité
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
   * - SanDisk
     - Optimus GX 7100 (SDSP71500GAN)
     - 500GB
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

Généralement stables
----------------------

Ces modèles de SSD ont été largement testés et sont généralement stables avec les configurations Raspberry Pi 5 et Pironman NVMe.

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


Compatibles (variable)
------------------------

Ces modèles peuvent fonctionner correctement dans de nombreuses configurations, mais leur compatibilité ou leur stabilité peut varier selon la charge de travail, la version du firmware, la version de l'EEPROM du Raspberry Pi, la qualité de l'alimentation ou la configuration PCIe.

* Crucial P2 M.2
* Crucial P3 M.2
* Crucial P3 Plus
* Crucial P310
* Série WD Blue SN580
* Western Digital Black SN770
* Série Western Digital Black SN850
* WD BLACK SN850X
* Samsung PM991
* Corsair MP600 SSD
* WD Blue SN5000 NVMe SSD
  (Détecté correctement, mais certains utilisateurs ont signalé des erreurs de lecture/écriture sauf si le PCIe est forcé en Gen3 et l'ASPM désactivé via ``pcie_aspm=off``.)


Non recommandés (instabilité potentielle)
-------------------------------------------

Les SSD ou contrôleurs suivants peuvent provoquer des réinitialisations PCIe, des erreurs d'E/S, des déconnexions ou une instabilité au démarrage sur les interfaces PCIe du Raspberry Pi 5.

* Les SSD utilisant les contrôleurs Phison E27T / E21
* Western Digital SN740
* WD BLACK 8TB SN850X
* Inland TN446 NVMe SSD
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* Autres SSD NVMe utilisant les mêmes familles de contrôleurs Phison


**Remarques sur la compatibilité**

* La compatibilité NVMe peut varier selon la version de Raspberry Pi OS, la version du noyau, le firmware EEPROM, le firmware du SSD et la qualité de l'alimentation.
* Une alimentation USB-C 5V/5A de bonne qualité est fortement recommandée, en particulier pour les SSD de grande capacité ou haute performance.
* Certains SSD peuvent fonctionner correctement comme stockage secondaire mais montrer de l'instabilité lorsqu'ils sont utilisés comme disque de démarrage.
* Un fonctionnement réussi signalé par les utilisateurs ne garantit pas toujours une stabilité à long terme sous des charges soutenues.

.. end_compatible_nvme_ssd
