.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances et projets autour de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Bénéficiez de l’aide de notre communauté et de notre équipe pour résoudre les problèmes techniques et après-vente.
    - **Apprendre & Partager** : Échangez des conseils et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Soyez parmi les premiers à découvrir nos nouveaux produits.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à nos concours et événements promotionnels pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_install_to_nvme_ubuntu:

Installation du système d’exploitation sur un SSD NVMe
================================================================

Si vous utilisez un SSD NVMe et disposez d’un adaptateur pour le connecter à votre ordinateur, vous pouvez suivre ce tutoriel pour une installation rapide.

**Matériel requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur de carte



1. Mise à jour du bootloader
----------------------------------

Vous devez d’abord mettre à jour le bootloader du Raspberry Pi 5 pour qu’il démarre depuis le NVMe avant de tenter un démarrage via USB, puis via la carte SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    À cette étape, il est recommandé d’utiliser une carte Micro SD dédiée. Commencez par écrire le bootloader sur cette carte, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage depuis un périphérique NVMe.
    
    Vous pouvez aussi écrire le bootloader directement sur le SSD NVMe, puis l’insérer dans le Raspberry Pi pour modifier sa méthode de démarrage. Ensuite, connectez le SSD NVMe à un ordinateur pour y installer le système d’exploitation, puis réinsérez-le dans le Raspberry Pi une fois l’installation terminée.

#. Insérez la carte Micro SD ou le SSD NVMe dans votre ordinateur via un lecteur.

#. Dans le |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans le menu déroulant.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Dans l’onglet **Operating System**, faites défiler vers le bas et sélectionnez **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. Choisissez **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Sélectionnez **NVMe/USB Boot** pour permettre au Raspberry Pi 5 de démarrer depuis le NVMe avant d’essayer l’USB, puis la carte SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Dans l’option **Storage**, sélectionnez le périphérique de stockage à utiliser pour l’installation.

   .. note::

      Assurez-vous de sélectionner le bon périphérique de stockage. Pour éviter toute confusion, déconnectez les autres supports de stockage si plusieurs sont branchés.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Cliquez ensuite sur **NEXT**. Si le support contient déjà des données, pensez à les sauvegarder avant de poursuivre. Cliquez sur **Yes** si aucune sauvegarde n’est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%


#. Une fois terminé, un message vous confirmera que **NVMe/USB Boot** a été correctement écrit sur votre support.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Vous pouvez maintenant insérer votre carte Micro SD ou votre SSD NVMe dans le Raspberry Pi. Après l’avoir alimenté avec un adaptateur Type C, le bootloader sera automatiquement écrit dans la mémoire EEPROM du Raspberry Pi.

.. note::

    Le Raspberry Pi démarrera désormais depuis le NVMe avant d’essayer l’USB, puis la carte SD. 
    
    Éteignez le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.


2. Installer le système d’exploitation sur le SSD NVMe
-----------------------------------------------------------------

Vous pouvez maintenant installer le système d’exploitation sur votre SSD NVMe.

**Étapes**

#. Rendez-vous sur la page |link_batocera_download|, sélectionnez **Raspberry Pi 5 B**, puis lancez le téléchargement.

   .. image:: img/batocera_download.png
      :width: 90%


#. Décompressez le fichier téléchargé ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Insérez votre carte SD dans votre ordinateur via un lecteur.

#. Dans le |link_rpi_imager|, cliquez sur l’onglet **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler jusqu’en bas et sélectionnez **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. Sélectionnez le fichier système que vous venez de décompresser, ``batocera-xxx-xx-xxxxxxxx.img``, puis cliquez sur **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Dans l’option **Storage**, sélectionnez le bon périphérique pour l’installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. Cliquez ensuite sur **NEXT**. Si le disque contient déjà des données, assurez-vous de les sauvegarder pour éviter toute perte. Cliquez sur **Yes** si aucune sauvegarde n’est nécessaire.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Lorsque le message "Write Successful" s’affiche, l’image système a été écrite et vérifiée avec succès. Vous êtes maintenant prêt à démarrer votre Raspberry Pi depuis le SSD NVMe !
