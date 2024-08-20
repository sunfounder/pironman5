.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_batocera:

Installer Batocera Linux
======================================================

|link_batocera| est une distribution de rétro-gaming open source et entièrement gratuite qui peut être copiée sur une clé USB ou une carte SD afin de transformer temporairement ou définitivement n'importe quel ordinateur/nano-ordinateur en console de jeu.

Vous pouvez choisir la méthode d'installation en fonction du support que vous avez à disposition, que ce soit une carte Micro SD ou un SSD NVMe.

L'installation directe sur le SSD NVMe implique une étape supplémentaire par rapport à l'installation sur la carte Micro SD : vous devez mettre à jour le bootloader du Raspberry Pi, car celui-ci est configuré par défaut pour démarrer à partir de la carte Micro SD. Mettez à jour le bootloader pour prioriser le démarrage à partir du SSD NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

