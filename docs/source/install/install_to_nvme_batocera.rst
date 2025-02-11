.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_to_nvme_ubuntu:

Installer le système d'exploitation sur un SSD NVMe
==========================================================

Si vous utilisez un SSD NVMe et disposez d'un adaptateur pour connecter le SSD NVMe à votre ordinateur pour l'installation du système, vous pouvez suivre le tutoriel suivant pour une installation rapide.

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Composants requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Carte Micro SD et lecteur

.. _update_bootloader:

1. Mettre à jour le bootloader
----------------------------------

Tout d'abord, vous devez mettre à jour le bootloader du Raspberry Pi 5 pour démarrer à partir du NVMe avant de tester l'USB puis la carte SD.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    À cette étape, il est recommandé d'utiliser une carte Micro SD de secours. Écrivez d'abord le bootloader sur cette carte Micro SD, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage à partir d'un périphérique NVMe.
    
    Alternativement, vous pouvez écrire directement le bootloader sur votre appareil NVMe, puis l'insérer dans le Raspberry Pi pour changer la méthode de démarrage. Ensuite, connectez le SSD NVMe à un ordinateur pour installer le système d'exploitation et, une fois l'installation terminée, réinsérez-le dans le Raspberry Pi.

#. Insérez votre carte Micro SD ou SSD NVMe de secours dans votre ordinateur ou portable à l'aide d'un lecteur.

#. Dans l'outil |link_rpi_imager|, cliquez sur **Appareil Raspberry Pi** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Dans l'onglet **Système d'exploitation**, faites défiler vers le bas et sélectionnez **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. Sélectionnez **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Sélectionnez **NVMe/USB Boot** pour permettre au Raspberry Pi 5 de démarrer à partir du NVMe avant de tester l'USB puis la carte SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      


#. Dans l'option **Stockage**, sélectionnez le périphérique de stockage approprié pour l'installation.

   .. note::

      Assurez-vous de sélectionner le bon périphérique de stockage. Pour éviter toute confusion, déconnectez tout autre périphérique de stockage si plusieurs sont connectés.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Vous pouvez maintenant cliquer sur **SUIVANT**. Si le périphérique de stockage contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Cliquez sur **Oui** si aucune sauvegarde n'est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Bientôt, vous serez informé que **NVMe/USB Boot** a été écrit sur votre périphérique de stockage.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Maintenant, vous pouvez insérer votre carte Micro SD ou SSD NVMe dans le Raspberry Pi. Après avoir alimenté le Raspberry Pi avec un adaptateur de type C, le bootloader de la carte Micro SD ou du SSD NVMe sera écrit dans l'EEPROM du Raspberry Pi.

.. note::

    Par la suite, le Raspberry Pi démarrera à partir du NVMe avant de tester l'USB puis la carte SD. 
    
    Éteignez le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.


2. Installer le système d'exploitation sur le SSD NVMe
------------------------------------------------------------

Vous pouvez maintenant installer le système d'exploitation sur votre SSD NVMe.

**Étapes**

#. Tout d'abord, accédez à la page de téléchargement |link_batocera_download|, sélectionnez **Raspberry Pi 5 B**, et cliquez pour télécharger.

   .. image:: img/batocera_download.png
      :width: 90%
      

#. Insérez votre carte SD dans votre ordinateur ou portable à l'aide d'un lecteur.

#. Dans l'outil |link_rpi_imager|, cliquez sur l'onglet **Système d'exploitation**.

   .. image:: img/os_choose_os.png
      :width: 90%
      
#. Faites défiler vers le bas de la page et sélectionnez **Utiliser un fichier personnalisé**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%
      

#. Choisissez le fichier système que vous venez de télécharger, ``batocera-xxx-xx-xxxxxxxx.img.gz``, puis cliquez sur **Ouvrir**.

   .. image:: img/batocera_os_choose.png
      :width: 90%
      

#. Dans l'option **Stockage**, sélectionnez le périphérique de stockage approprié pour l'installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      


#. Vous pouvez maintenant cliquer sur **SUIVANT**. Si le périphérique de stockage contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Cliquez sur **Oui** si aucune sauvegarde n'est nécessaire.

   .. image:: img/nvme_erase.png
      :width: 90%
      

#. Lorsque vous voyez le message "Écriture réussie", votre image a été entièrement écrite et vérifiée. Vous êtes maintenant prêt à démarrer un Raspberry Pi depuis le SSD NVMe !

