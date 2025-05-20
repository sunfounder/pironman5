.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours**: Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_to_sd_ubuntu:

Installation du système d'exploitation sur une carte Micro SD
===================================================================

Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour installer le système sur votre carte Micro SD.

**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur


**Étapes**

#. Tout d'abord, accédez à la page |link_batocera_download|, sélectionnez **Raspberry Pi 5 B**, puis cliquez pour télécharger.

   .. image:: img/batocera_download.png
      :width: 90%
      

#. Insérez votre carte SD dans votre ordinateur ou votre portable à l'aide d'un lecteur.

#. Dans l'outil |link_rpi_imager|, cliquez sur l'onglet **Système d'exploitation**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler jusqu'en bas de la page et sélectionnez **Utiliser un fichier personnalisé**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%
      

#. Choisissez le fichier système que vous venez de télécharger, ``batocera-xxx-xx-xxxxxxxx.img.gz``, puis cliquez sur **Ouvrir**.

   .. image:: img/batocera_os_choose.png
      :width: 90%
      

#. Cliquez sur **Choisir un stockage** et sélectionnez le périphérique de stockage approprié pour l'installation.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Vous pouvez maintenant cliquer sur **SUIVANT**. Si le périphérique de stockage contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Cliquez sur **Oui** si aucune sauvegarde n'est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Lorsque vous voyez le message "Écriture réussie", votre image a été entièrement écrite et vérifiée. Vous êtes maintenant prêt à démarrer un Raspberry Pi depuis la carte Micro SD !

