.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


.. _copy_sd_to_nvme_max:

Copier le système d’exploitation de la carte Micro SD vers le SSD NVMe
=========================================================================

Si vous disposez d’un SSD NVMe mais que vous n’avez pas d’adaptateur pour le connecter à votre ordinateur, vous pouvez utiliser une troisième méthode : installer d’abord le système sur votre carte Micro SD. Une fois que le Pironman 5 MAX a démarré avec succès, vous pourrez ensuite transférer le système de la carte Micro SD vers le SSD NVMe.

* Tout d’abord, vous devez effectuer :ref:`install_os_sd_rpi_max`.
* Ensuite, démarrez votre Raspberry Pi et connectez-vous. Si vous ne savez pas comment vous connecter, vous pouvez consulter le site officiel de Raspberry Pi : |link_rpi_get_start|.

Veuillez terminer les étapes ci-dessus avant de poursuivre avec les instructions ci-dessous.


1. Activer le PCIe
--------------------

Par défaut, le connecteur PCIe n’est pas activé.

* Pour l’activer, ouvrez le fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Ajoutez ensuite la ligne suivante au fichier.

  .. code-block:: shell
  
    # Activer le connecteur PCIe externe
    dtparam=pciex1
  
* Il existe un alias plus facile à mémoriser pour ``pciex1`` ; vous pouvez donc également ajouter ``dtparam=nvme`` dans le fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    dtparam=nvme

.. * La connexion est certifiée pour des vitesses Gen 2.0 (5 GT/s), mais vous pouvez forcer le mode Gen 3.0 (10 GT/s) en ajoutant les lignes suivantes dans votre fichier ``/boot/firmware/config.txt``.

..   .. code-block:: shell
  
..     # Forcer les vitesses Gen 3.0
..     dtparam=pciex1_gen=3
  
..   .. warning::
  
..     Le Raspberry Pi 5 n’est pas certifié pour des vitesses Gen 3.0, et les connexions aux périphériques PCIe à ces vitesses peuvent être instables.

* Vous devez désactiver le délai de démarrage PCIe afin que le Raspberry Pi puisse détecter le disque NVMe derrière le commutateur PCIe au démarrage. Ajoutez la ligne suivante au fichier ``/boot/firmware/config.txt`` :

   .. code-block:: shell

      dtparam=pciex1_no_10s=on


* Appuyez sur ``Ctrl + X``, puis ``Y`` et ``Entrée`` pour enregistrer les modifications.


**BOOT_ORDER**

Si vous avez installé deux disques système NVMe et que vous devez choisir celui sur lequel démarrer,  
vous pouvez modifier ``ROOT=PARTUUID=xxxxxxxxx`` dans le fichier ``/boot/firmware/cmdline.txt`` en remplaçant l’UUID par celui du disque à partir duquel vous souhaitez démarrer. Vous pouvez trouver l’UUID du disque à l’aide de la commande suivante :

.. code-block:: shell

   ls /dev/disk/by-id/

.. start_copy_nvme

2. Installer le système d’exploitation sur le SSD
----------------------------------------------------

Il existe deux méthodes pour installer un système d’exploitation sur le SSD :

**Copier le système de la carte Micro SD vers le SSD**

#. Connectez un écran ou accédez au bureau du Raspberry Pi via VNC Viewer. Cliquez ensuite sur **logo Raspberry Pi** -> **Accessories** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png
      
    
#. Assurez-vous de sélectionner correctement les périphériques **Copy From** et **Copy To**. Veillez à ne pas les intervertir.

   .. image:: img/ssd_copy_from.png
      
#. N’oubliez pas de sélectionner « NEW Partition UUIDs » afin de garantir que le système puisse distinguer correctement les périphériques, évitant ainsi les conflits de montage et les problèmes de démarrage.

   .. image:: img/ssd_copy_uuid.png
    
#. Après la sélection, cliquez sur **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Un message vous indiquera que le contenu du SSD sera effacé. Assurez-vous d’avoir sauvegardé vos données avant de cliquer sur Yes. Patientez quelques instants : la copie sera alors terminée.

**Installer le système avec Raspberry Pi Imager**

Si votre carte Micro SD contient une version bureau du système, vous pouvez utiliser un outil d’imagerie (comme Raspberry Pi Imager) pour graver le système sur le SSD. Cet exemple utilise Raspberry Pi OS Bookworm, mais d’autres systèmes peuvent nécessiter l’installation préalable de l’outil d’imagerie.

#. Connectez un écran ou accédez au bureau du Raspberry Pi via VNC Viewer. Cliquez ensuite sur **logo Raspberry Pi** -> **Accessories** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Insérez votre carte Micro SD dans votre ordinateur à l’aide d’un lecteur de cartes. Sauvegardez toutes les données importantes avant de continuer.

   .. image:: img/insert_sd.png
      :width: 90%

#. Lorsque Raspberry Pi Imager s’ouvre, vous verrez la page **Device**. Sélectionnez votre modèle de Raspberry Pi 5 dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

#. Allez dans la section **OS** et choisissez l’option recommandée **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

#. Dans la section **Storage**, sélectionnez votre **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_max:

3. Configurer le démarrage depuis le SSD
--------------------------------------------

Dans cette section, nous allons configurer votre Raspberry Pi pour démarrer directement depuis un SSD NVMe, offrant des temps de démarrage plus rapides et de meilleures performances par rapport à une carte SD. Suivez attentivement les étapes ci-dessous :

#. Tout d’abord, ouvrez un terminal sur votre Raspberry Pi et exécutez la commande suivante pour accéder à l’interface de configuration :.

   .. code-block:: shell

      sudo raspi-config

#. Dans le menu ``raspi-config``, utilisez les touches fléchées pour naviguer et sélectionner **Advanced Options**. Appuyez sur ``Entrée`` pour accéder aux paramètres avancés.

   .. image:: img/nvme_open_config.png

#. Dans **Advanced Options**, sélectionnez **Boot Order**. Ce paramètre vous permet de définir l’ordre dans lequel votre Raspberry Pi recherche les périphériques amorçables.

   .. image:: img/nvme_boot_order.png

#. Ensuite, choisissez **NVMe/USB boot**. Cela indique au Raspberry Pi de donner la priorité au démarrage depuis des SSD ou des disques NVMe connectés en USB, plutôt que depuis d’autres options comme la carte SD.

   .. image:: img/nvme_boot_nvme.png

#. Après avoir sélectionné l’ordre de démarrage, appuyez sur **Finish** pour quitter raspi-config. Vous pouvez également utiliser la touche **Escape** pour fermer l’outil de configuration.

   .. image:: img/nvme_boot_ok.png

#. Pour appliquer les nouveaux paramètres de démarrage, redémarrez votre Raspberry Pi en exécutant ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

Après le redémarrage, le Raspberry Pi devrait maintenant tenter de démarrer depuis le SSD NVMe connecté, vous offrant ainsi de meilleures performances et une durabilité accrue pour votre système.

.. end_copy_nvme
