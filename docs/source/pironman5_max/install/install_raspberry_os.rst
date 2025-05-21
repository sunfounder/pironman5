.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances et projets autour de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Obtenez de l’aide pour résoudre les problèmes techniques ou liés au service après-vente grâce à notre équipe et notre communauté.
    - **Apprendre & Partager** : Échangez des conseils et tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d’un accès anticipé aux annonces et aperçus de nouveaux produits.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos dernières innovations.
    - **Promotions festives et cadeaux** : Participez à des concours et événements promotionnels tout au long de l’année.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès maintenant !

Installer Raspberry Pi OS
================================================================================

La méthode d'installation dépend du support dont vous disposez : carte Micro SD ou SSD NVMe.

* L’installation directe sur un SSD NVMe nécessite une étape supplémentaire par rapport à une carte Micro SD : vous devez mettre à jour le bootloader du Raspberry Pi, qui démarre par défaut sur la carte Micro SD. Mettez à jour le bootloader pour qu’il privilégie le démarrage depuis le SSD NVMe.
* Si vous possédez un SSD NVMe mais pas d’adaptateur pour le connecter à votre ordinateur, envisagez une troisième option : commencez par installer le système sur votre carte Micro SD. Une fois le Pironman 5 démarré avec succès, vous pourrez copier le système de la carte Micro SD vers le SSD NVMe.


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi