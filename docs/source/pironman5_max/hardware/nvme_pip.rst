.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur le Raspberry Pi, l’Arduino et l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Bénéficiez de l’aide de notre équipe et de notre communauté pour résoudre les problèmes après-vente et relever les défis techniques.
    - **Apprendre & partager** : Échangez des conseils et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Soyez informé(e) en avant-première des nouveaux produits et obtenez un aperçu de ce qui arrive.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et à des offres spéciales pendant les fêtes.

    👉 Prêt(e) à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Carte Pi5 NVMe PIP double
==========================

La carte périphérique PCIe Dual NVMe (PIP), telle que définie par la Fondation Raspberry Pi, est une carte adaptateur PCIe spécialement conçue pour les disques SSD NVMe.

L'interface PCIe du Raspberry Pi 5 offre par défaut un seul canal Gen2 x1 (bande passante de 500 Mo/s). L'intégration de la puce ASM1182e permet de l'étendre à deux canaux Gen2 x1 indépendants pour connecter deux périphériques M.2 M-key (tels que deux SSD M.2 NVMe ou un SSD M.2 NVMe + un accélérateur M.2 Hailo-8/8LAI). Il est toutefois à noter que la carte périphérique PCIe Dual NVMe ne prend pas en charge la Gen 3.

Elle prend en charge quatre tailles différentes de SSD NVMe : 2230, 2242, 2260 et 2280, tous compatibles avec un emplacement M.2 M-key.

.. image:: img/nvme_pip.png

* La carte se connecte via une nappe FFC inversée 16P 0,5 mm ou un câble FPC personnalisé avec impédance adaptée.
* **STA** : Témoin d’état (LED).
* **PWR** : Témoin d’alimentation (LED).
* L’alimentation intégrée en 3,3V peut délivrer jusqu’à 3A. Cependant, l’interface PCIe du Raspberry Pi est limitée à 5V/1A (soit 5W). Une alimentation supplémentaire peut être fournie via le connecteur J3 à partir d'une source 5V.
* **FORCE ENABLE** : L’alimentation intégrée est activée par un signal de commutation provenant de l’interface PCIe. Une fois le Raspberry Pi sous tension, ce signal permet d’activer l’alimentation 3,3V. Si le système ne prend pas en charge ce signal, ou pour d’autres raisons, vous pouvez forcer l’activation de l’alimentation 3,3V en soudant les deux pastilles flottantes de J4 (FORCE ENABLE).

À propos des modèles
---------------------------

Les SSD M.2 sont réputés pour leur compacité. Ils se distinguent principalement par leur type d'encoche (clé) et l'interface utilisée. Voici les principaux types :

* **SSD M.2 SATA** : utilisent l’interface SATA, comme les SSD 2,5", mais dans un format M.2. Leur vitesse est limitée par la norme SATA III à environ 600 Mo/s. Compatibles avec les ports B et M key.
* **SSD M.2 NVMe** : utilisent le protocole NVMe via des lignes PCIe, offrant des vitesses bien supérieures aux SSD M.2 SATA. Idéaux pour les usages intensifs tels que les jeux, le montage vidéo ou les traitements de données. Ces SSD nécessitent généralement un port M key. Ils exploitent l’interface PCIe (Peripheral Component Interconnect Express) dans ses versions 3.0, 4.0 ou 5.0. Chaque génération double la vitesse de transfert. Le Raspberry Pi 5 utilise l’interface PCIe 3.0, capable d’atteindre jusqu’à 3500 Mo/s.

Il existe trois types de clés : B key, M key et B+M key. Le B+M key combine les fonctions des deux précédentes, remplaçant généralement le B key seul. Voir l’illustration ci-dessous.

.. image:: img/ssd_key.png


En général, les SSD SATA sont au format B+M key (compatibles avec les ports B et M), tandis que les SSD NVMe PCIe x4 sont en M key.

.. image:: img/ssd_model2.png

À propos de la longueur
----------------------------

Les modules M.2 existent en plusieurs tailles et peuvent aussi servir pour le Wi-Fi, WWAN, Bluetooth, GPS et NFC.

Le Pironman 5 MAX prend en charge quatre longueurs de SSD M.2 NVMe (PCIe Gen 2.0 / Gen 3.0) : 2230, 2242, 2260 et 2280. Le « 22 » désigne la largeur en mm et les deux chiffres suivants indiquent la longueur. Plus le module est long, plus il peut contenir de puces NAND, et donc offrir plus de capacité.


.. image:: img/m2_ssd_size.png
  :width: 600

