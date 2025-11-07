.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes techniques et après-vente avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des conseils et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces et démonstrations de nouveaux produits.
    - **Réductions exclusives** : Profitez de remises spéciales sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et événements pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _install_to_nvme_ubuntu_mini:

Installation du système d’exploitation sur un SSD NVMe
===========================================================

Si vous utilisez un SSD NVMe et disposez d’un adaptateur pour le connecter à votre ordinateur, vous pouvez suivre ce tutoriel pour effectuer une installation rapide.

**Composants nécessaires**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur de cartes


1. Mettre à jour le bootloader
----------------------------------

Commencez par mettre à jour le bootloader du Raspberry Pi 5 afin qu’il démarre depuis le NVMe, puis depuis l’USB et enfin depuis la carte SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    À cette étape, il est recommandé d’utiliser une carte Micro SD de rechange. Commencez par y écrire le bootloader, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage depuis un périphérique NVMe.

    En alternative, vous pouvez écrire le bootloader directement sur le SSD NVMe, puis l’insérer dans le Raspberry Pi pour modifier la méthode de démarrage. Ensuite, connectez le SSD à l’ordinateur pour y installer le système d’exploitation, puis réinsérez-le dans le Raspberry Pi.

#. Insérez votre carte Micro SD de rechange ou SSD NVMe dans l’ordinateur via un lecteur de cartes.

#. Dans le |link_rpi_imager|, cliquez sur **Appareil Raspberry Pi** et sélectionnez **Raspberry Pi 5** dans la liste.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Dans l’onglet **Système d’exploitation**, faites défiler vers le bas et sélectionnez **Images utilitaires diverses**.

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. Choisissez **Bootloader (famille Pi 5)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Sélectionnez **Démarrage NVMe/USB** pour permettre au Raspberry Pi 5 de démarrer en priorité depuis le NVMe, puis depuis l’USB et enfin depuis la carte SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Dans l’option **Stockage**, sélectionnez le périphérique sur lequel écrire.

   .. note::

      Assurez-vous de choisir le bon support. Pour éviter toute confusion, déconnectez les autres périphériques de stockage si nécessaire.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Cliquez sur **SUIVANT**. Si le support contient déjà des données, sauvegardez-les. Cliquez sur **Oui** pour continuer sans sauvegarde.

   .. image:: img/os_continue.png
      :width: 90%


#. Une fois l’écriture terminée, un message vous confirmera que **NVMe/USB Boot** a bien été écrit sur votre support.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Insérez maintenant votre carte Micro SD ou SSD NVMe dans le Raspberry Pi. Après avoir alimenté le Raspberry Pi avec un adaptateur USB-C, le bootloader sera écrit dans l’EEPROM du Raspberry Pi.

.. note::

    Ensuite, le Raspberry Pi démarrera d’abord depuis le NVMe, puis depuis l’USB, et enfin depuis la carte SD.

    Éteignez le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.


2. Installer le système d’exploitation sur le SSD NVMe
-----------------------------------------------------------

Vous pouvez maintenant installer le système d’exploitation sur le SSD NVMe.

**Étapes**

#. Accédez à la page |link_batocera_download|, sélectionnez **Raspberry Pi 5 B**, puis téléchargez l’image.

   .. image:: img/batocera_download.png
      :width: 90%


#. Décompressez le fichier téléchargé ``batocera-xxx-xx-xxxxxxxx.img.gz``.


#. Insérez votre carte SD dans l’ordinateur à l’aide d’un lecteur.

#. Ouvrez |link_rpi_imager|, puis cliquez sur l’onglet **Système d’exploitation**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler jusqu’en bas et sélectionnez **Utiliser une image personnalisée**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. Sélectionnez le fichier image que vous venez de décompresser, ``batocera-xxx-xx-xxxxxxxx.img``, puis cliquez sur **Ouvrir**.


   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Dans l’onglet **Stockage**, choisissez le SSD NVMe comme périphérique de destination.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. Cliquez sur **SUIVANT**. Si le support contient des données, assurez-vous d’en faire une sauvegarde. Cliquez sur **Oui** si aucune sauvegarde n’est nécessaire.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Une fois le message "Écriture réussie" affiché, l’image a bien été gravée et vérifiée. Vous êtes maintenant prêt à démarrer votre Raspberry Pi depuis le SSD NVMe !
