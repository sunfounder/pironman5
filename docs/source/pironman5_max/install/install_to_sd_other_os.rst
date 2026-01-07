.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_to_sd_other_max:

Installation du système d’exploitation sur une carte Micro SD
==================================================================

Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour installer le système sur votre carte Micro SD.


**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur de cartes

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installer le système d’exploitation sur la carte microSD
-------------------------------------------------------------------

1. Insérez votre carte microSD dans votre ordinateur à l’aide d’un lecteur de cartes.  
   Avant de continuer, sauvegardez toutes les données importantes présentes sur la carte, car elles seront effacées.

   .. image:: img/insert_sd.png
      :width: 90%

2. Lorsque **Raspberry Pi Imager** s’ouvre, vous verrez la page **Device**.  
   Sélectionnez votre modèle de **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

3. Allez dans la section **OS**, faites défiler jusqu’en bas de la page et sélectionnez votre système d’exploitation.

   .. note::

      * Pour **Ubuntu**, cliquez sur **Other general-purpose OS** → **Ubuntu**, puis sélectionnez  
        **Ubuntu Desktop 24.04 LTS (64-bit)** ou **Ubuntu Server 24.04 LTS (64-bit)**.
      * Pour **Kali Linux**, **Home Assistant** et **Homebridge**, cliquez sur  
        **Other specific-purpose OS**, puis sélectionnez le système correspondant.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Dans la section **Storage**, sélectionnez votre carte microSD.  
   Pour plus de sécurité, il est recommandé de débrancher les autres périphériques de stockage USB afin que seule la carte microSD apparaisse dans la liste.

   .. image:: img/imager_storage.png
      :width: 90%

#. Cliquez sur **NEXT**.

   .. note::

      * Pour les systèmes qui **ne peuvent pas être préconfigurés**, cliquer sur **NEXT** ignorera l’étape **Customisation** et passera directement à **Writing**, où le système d’exploitation est écrit sur la carte microSD.
      * Pour les systèmes qui **prennent en charge la préconfiguration**, suivez les étapes de **Customisation** afin de configurer des options telles que le **Hostname**, le **WiFi** et l’**activation de SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Lorsque la fenêtre contextuelle **« Write Successful »** apparaît, l’image a été entièrement écrite et vérifiée. Vous pouvez maintenant retirer la carte microSD en toute sécurité et l’utiliser pour démarrer votre Raspberry Pi.
