.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Pi5 NVMe PIP
=================

Le Pi5 NVMe PIP (carte d'extension PCIe), tel que défini par la Fondation Raspberry Pi, est une carte adaptateur PCIe conçue spécifiquement pour les disques SSD NVMe. Elle prend en charge quatre tailles différentes de SSD NVMe: 2230, 2242, 2260 et 2280, tous compatibles avec un emplacement M.2 M key.

.. image:: img/nvme_pip.png

* La carte se connecte via un câble FFC inversé 16P 0,5 mm ou un câble FPC personnalisé avec une impédance adaptée.
* **STA**: Un indicateur LED de statut.
* **PWR**: Un indicateur LED d'alimentation.
* L'alimentation embarquée en 3,3V peut fournir jusqu'à 3A en sortie. Cependant, étant donné que l'interface PCIe du Raspberry Pi est limitée à fournir une sortie de 5V/1A (équivalent à 5W), une alimentation supplémentaire de 3,3V/3A peut être fournie via le connecteur J3 à partir d'une source de 5V.
* **FORCE ENABLE**: L'alimentation embarquée est activée par le signal de commutation de l'interface PCIe. Une fois le Raspberry Pi alimenté, il envoie un signal pour activer l'alimentation 3,3V. Si certains systèmes ne prennent pas en charge le signal de commutation, ou pour d'autres raisons, vous pouvez court-circuiter J4 FORCE ENABLE en soudant un fil entre les deux pastilles flottantes pour forcer l'alimentation 3,3V embarquée à alimenter le NVMe.

À propos du modèle
---------------------------

Les SSD M.2, connus pour leur petite taille, existent en plusieurs types principalement différenciés par leur encoche et l'interface qu'ils utilisent. Voici les principaux types :

* **SSD M.2 SATA**: Ces disques utilisent l'interface SATA, similaire aux SSD SATA 2,5 pouces, mais dans un format plus petit M.2. Ils sont limités par les vitesses maximales du SATA III, environ 600 Mo/s. Ces SSD sont compatibles avec les emplacements M.2 à clés B et M.
* **SSD M.2 NVMe**: Ces SSD utilisent le protocole NVMe sur des lignes PCIe et sont beaucoup plus rapides que les SSD M.2 SATA. Ils sont adaptés aux applications nécessitant des vitesses de lecture/écriture élevées telles que les jeux, le montage vidéo et les tâches intensives en données. Ces SSD nécessitent généralement des emplacements à clé M. Ils utilisent l'interface PCIe (Peripheral Component Interconnect Express), avec différentes versions telles que 3.0, 4.0 et 5.0. Chaque nouvelle version de PCIe double efficacement la vitesse de transfert des données de la précédente. Cependant, le Raspberry Pi 5 utilise une interface PCIe 3.0, capable de fournir des vitesses de transfert allant jusqu'à 3500 Mo/s.

Les SSD M.2 existent en trois types principaux: clé B, clé M et clé B+M. Toutefois, plus tard, la clé B+M a été introduite, combinant les fonctionnalités des clés B et M. En conséquence, elle a remplacé la clé B autonome. Veuillez vous référer à l'image ci-dessous.

.. image:: img/ssd_key.png

En général, les SSD M.2 SATA sont à clé B+M (ils peuvent s'insérer dans les sockets pour modules à clé B et M), tandis que les SSD M.2 NVMe pour PCIe 3.0 x4 sont à clé M.

.. image:: img/ssd_model2.png

À propos de la longueur
----------------------------

Les modules M.2 existent en différentes tailles et peuvent également être utilisés pour le Wi-Fi, WWAN, Bluetooth, GPS et NFC.

Le Pironman 5 prend en charge quatre tailles de SSD NVMe M.2 (PCIe Gen 2.0 / PCIe Gen 3.0) en fonction de leur nom: 2230, 2242, 2260 et 2280. Le "22" correspond à la largeur en millimètres (mm), et les deux chiffres suivants à la longueur. Plus le lecteur est long, plus il peut contenir de puces NAND, et donc offrir une plus grande capacité.

.. image:: img/m2_ssd_size.png
  :width: 600
