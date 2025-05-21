.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Bénéficiez de l’aide de notre communauté et de notre équipe pour résoudre vos problèmes techniques et après-vente.
    - **Apprendre et partager** : Échangez des conseils et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces et présentations de nouveaux produits.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et événements promotionnels durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _install_batocera_mini:

Installation de Batocera Linux
======================================================

|link_batocera| est une distribution de rétro-gaming open source et entièrement gratuite, que l’on peut copier sur une clé USB ou une carte SD, dans le but de transformer n’importe quel ordinateur ou nano-ordinateur en console de jeu, de manière temporaire ou permanente.

Vous pouvez choisir la méthode d’installation selon que vous disposez d’une carte Micro SD ou d’un SSD NVMe.

L’installation directe sur un SSD NVMe nécessite une étape supplémentaire par rapport à l’installation sur carte Micro SD : vous devez mettre à jour le bootloader du Raspberry Pi, qui démarre par défaut depuis la carte Micro SD. Il faut donc le configurer pour qu’il privilégie le démarrage depuis le SSD NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

