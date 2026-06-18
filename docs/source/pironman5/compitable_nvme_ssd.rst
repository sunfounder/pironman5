.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _compitable_nvme_ssd_5:

.. start_compatible_nvme_ssd

SSD NVMe compatibles
========================

**Recommandé (Stable)**

Ces modèles de SSD ont été testés et sont généralement stables avec les configurations Raspberry Pi 5 et Pironman NVMe.

* ADATA Legend 700
* ADATA Legend 800
* AData XPG SX8200 Pro

* Axe Memory Generic Drive

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

* TeamGroup MP33

* Western Digital SN570
* Western Digital SN530
* Western Digital Black SN750 SE
* Western Digital Blue SN550 series (Si vous savez comment installer les dernières mises à jour rpi-eeprom, le pieeprom-2024-01-24.bin a résolu le problème de démarrage nvme du Western Digital Blue SN550. Référez-vous à https://forums.raspberrypi.com/viewtopic.php?t=364327.)

* XPG GAMMIX S70 BLADE
* XPG SX8200 Pro


**Compatible (Peut Varier)**

Ces modèles peuvent fonctionner correctement dans de nombreuses configurations, mais certains utilisateurs ont signalé des différences occasionnelles de compatibilité ou de stabilité selon la charge de travail ou la configuration du système.


* Crucial P2 M.2
* Crucial P3 M.2



**Non Recommandé (Instabilité Potentielle)**

Ces modèles ou contrôleurs peuvent provoquer des réinitialisations NVMe, des erreurs d'E/S ou des déconnexions du disque sur les interfaces PCIe du Raspberry Pi 5, et ne sont donc pas recommandés.

* Les SSD utilisant les contrôleurs Phison E27T / E21
* Crucial P310
* Crucial P3 Plus M.2
* Western Digital SN740
* Western Digital Black SN770
* Série WD Blue SN580
* Série Western Digital Green SN350
* Série Western Digital Black SN850
* WD BLACK 8TB SN850X
* Inland tn446 nvme drive
* Corsair MP600 SSD
* Samsung PM991
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* Autres SSD NVMe équipés du même contrôleur Phison

.. end_compatible_nvme_ssd