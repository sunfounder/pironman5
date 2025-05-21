.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour explorer plus en profondeur les univers de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Bénéficiez de l’aide de notre équipe et de la communauté pour résoudre les problèmes techniques ou après-vente.
    - **Apprendre & Partager** : Échangez astuces et tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Accédez en exclusivité aux annonces de nouveaux produits et à des aperçus privilégiés.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et offres spéciales pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] pour nous rejoindre dès aujourd’hui !

.. _max_install_batocera:

Installer Batocera Linux
======================================================

|link_batocera| est une distribution rétro-gaming open-source et totalement gratuite, conçue pour transformer temporairement ou définitivement un ordinateur ou nano-ordinateur en console de jeu. Elle peut être copiée sur une clé USB ou une carte SD.

Le choix de la méthode d’installation dépend du support dont vous disposez : carte Micro SD ou SSD NVMe.

L’installation directe sur un SSD NVMe nécessite une étape supplémentaire par rapport à l’installation sur carte Micro SD : il faut mettre à jour le bootloader du Raspberry Pi, qui par défaut démarre depuis la carte Micro SD. Mettez à jour le bootloader afin de prioriser le démarrage depuis le SSD NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

