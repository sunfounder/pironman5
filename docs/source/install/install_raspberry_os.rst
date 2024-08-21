.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Installer Raspberry Pi OS
================================================================================

Vous pouvez choisir la méthode d'installation en fonction de si vous avez une carte Micro SD ou un SSD NVMe à disposition.

* L'installation directe sur le SSD NVMe implique une étape supplémentaire par rapport à l'installation sur la carte Micro SD: vous devez mettre à jour le bootloader du Raspberry Pi, car celui-ci démarre par défaut à partir de la carte Micro SD. Mettez à jour le bootloader pour prioriser le démarrage depuis le SSD NVMe.
* Si vous avez un SSD NVMe mais que vous ne disposez pas d'un adaptateur pour le connecter à votre ordinateur, envisagez une troisième option: installez d'abord le système sur votre carte Micro SD. Une fois que le Pironman 5 a démarré avec succès, vous pourrez copier le système de votre carte Micro SD vers votre SSD NVMe.


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi