.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Explorez plus en profondeur le monde du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre équipe et de la communauté.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et des offres promotionnelles pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] pour nous rejoindre dès aujourd’hui !

.. _install_to_sd_ubuntu_mini:

Installation du système d'exploitation sur une carte Micro SD
=================================================================

Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour installer le système sur celle-ci.


**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur de cartes

**Étapes**

#. Rendez-vous tout d'abord sur la page |link_batocera_download|, sélectionnez **Raspberry Pi 5 B** puis cliquez sur le bouton de téléchargement.

   .. image:: img/batocera_download.png
      :width: 90%


#. Décompressez le fichier téléchargé ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Insérez votre carte SD dans votre ordinateur à l’aide d’un lecteur de cartes.


#. Dans l’application |link_rpi_imager|, cliquez sur l’onglet **Système d’exploitation**.


   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler vers le bas de la page et sélectionnez **Utiliser une image personnalisée**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. Sélectionnez le fichier système que vous venez de décompresser, ``batocera-xxx-xx-xxxxxxxx.img``, puis cliquez sur **Ouvrir**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Cliquez sur **Choisir un support** et sélectionnez le périphérique de stockage adéquat pour l'installation.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Cliquez ensuite sur **SUIVANT**. Si le périphérique de stockage contient déjà des données, assurez-vous d’effectuer une sauvegarde avant de continuer. Cliquez sur **Oui** si aucune sauvegarde n’est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%


#. Une fois le message "Écriture réussie" affiché, cela signifie que l’image a bien été écrite et vérifiée. Vous êtes maintenant prêt à démarrer un Raspberry Pi à partir de la carte Micro SD !
