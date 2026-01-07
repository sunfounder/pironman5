.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Installation de Raspberry Pi OS
================================================================================

Vous pouvez choisir une méthode d’installation en fonction de la disponibilité d’une carte Micro SD ou d’un SSD NVMe.

**Utiliser uniquement une carte Micro SD**

  Si vous utilisez uniquement une carte Micro SD, vous pouvez simplement suivre la première méthode ci-dessous.

**Utiliser un SSD M.2 NVMe**

  * Si vous disposez d’un **boîtier adaptateur M.2 NVMe**, vous pouvez connecter votre SSD à votre ordinateur à l’aide de cet adaptateur et suivre la deuxième méthode pour installer le système d’exploitation.  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * Si vous ne disposez pas de l’adaptateur présenté ci-dessus, vous pouvez d’abord installer le système d’exploitation sur une carte Micro SD en utilisant la première méthode, puis utiliser la troisième méthode pour copier le système depuis la carte Micro SD vers votre SSD M.2 NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi