.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _copy_sd_to_nvme_promax:

Copier le système d'exploitation de la carte Micro SD vers le SSD NVMe
======================================================================================

Si vous possédez un SSD NVMe mais que vous n'avez pas d'adaptateur pour le connecter à votre ordinateur, vous pouvez opter pour une troisième approche : installer initialement le système sur votre carte Micro SD. Après le démarrage réussi du Pironman 5 Pro MAX, vous pouvez ensuite transférer le système de votre carte Micro SD vers votre SSD NVMe.

* Tout d'abord, vous devez :ref:`install_os_sd_rpi_promax`.
* Ensuite, démarrez et connectez-vous à votre Raspberry Pi. Si vous ne savez pas comment vous connecter, vous pouvez visiter le site officiel de Raspberry Pi : |link_rpi_get_start|.

Effectuez les étapes ci-dessus avant de suivre les instructions ci-dessous.

1. Activer PCIe
--------------------

Par défaut, le connecteur PCIe n'est pas activé.

* Pour l'activer, vous devez ouvrir le fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* Ajoutez ensuite la ligne suivante au fichier.

  .. code-block:: shell

    # Enable the PCIe External connector.
    dtparam=pciex1

* Un alias plus mémorisable pour ``pciex1`` existe, vous pouvez donc également ajouter ``dtparam=nvme`` au fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell

    dtparam=nvme

* Vous devrez désactiver le délai de démarrage PCIe afin que le Raspberry Pi puisse détecter le lecteur NVMe derrière le commutateur PCIe au démarrage. Ajoutez la ligne suivante à ``/boot/firmware/config.txt`` :

   .. code-block:: shell

      dtparam=pciex1_no_10s=on

* Appuyez sur ``Ctrl + X``, ``Y`` et ``Entrée`` pour enregistrer les modifications.

**BOOT_ORDER**

Si vous avez installé deux disques système NVMe et que vous devez choisir lequel démarrer, vous pouvez modifier le ``ROOT=PARTUUID=xxxxxxxxx`` dans le fichier ``/boot/firmware/cmdline.txt`` en l'UUID du disque que vous souhaitez démarrer. Vous pouvez trouver l'UUID du disque avec la commande suivante :

.. code-block:: shell

   ls /dev/disk/by-id/

.. start_copy_nvme

2. Installer le système d'exploitation sur le SSD
-------------------------------------------------------------

Il existe deux façons d'installer un système d'exploitation sur le SSD :

**Copier le système de la carte Micro SD vers le SSD**

#. Connectez un écran ou accédez au bureau Raspberry Pi via VNC Viewer. Cliquez ensuite sur **Logo Raspberry Pi** -> **Accessoires** -> **Copieur de carte SD**.

   .. image:: img/ssd_copy.png

#. Assurez-vous de sélectionner les bons périphériques **Copier depuis** et **Copier vers**. Veillez à ne pas les mélanger.

   .. image:: img/ssd_copy_from.png

#. N'oubliez pas de sélectionner « Nouveaux UUID de partition » pour garantir que le système puisse correctement distinguer les périphériques, évitant ainsi les conflits de montage et les problèmes de démarrage.

   .. image:: img/ssd_copy_uuid.png

#. Après la sélection, cliquez sur **Démarrer**.

   .. image:: img/ssd_copy_click_start.png

#. Un message vous avertira que le contenu du SSD sera effacé. Assurez-vous de sauvegarder vos données avant de cliquer sur Oui. Attendez un certain temps, la copie sera terminée.

**Installer le système avec Raspberry Pi Imager**

Si votre carte Micro SD a une version bureau du système installée, vous pouvez utiliser un outil d'imagerie (comme Raspberry Pi Imager) pour graver le système sur le SSD. Cet exemple utilise Raspberry Pi OS bookworm, mais d'autres systèmes peuvent nécessiter l'installation préalable de l'outil d'imagerie.

#. Connectez un écran ou accédez au bureau Raspberry Pi via VNC Viewer. Cliquez ensuite sur **Logo Raspberry Pi** -> **Accessoires** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Insérez votre carte microSD dans votre ordinateur à l'aide d'un lecteur de carte. Sauvegardez toutes les données importantes avant de continuer.

   .. image:: img/insert_sd.png
      :width: 90%

#. Lorsque Raspberry Pi Imager s'ouvre, vous verrez la page **Périphérique**. Sélectionnez votre modèle Raspberry Pi 5 dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

#. Allez dans la section **Système d'exploitation** et choisissez l'option recommandée **Raspberry Pi OS (64-bit)**.

   .. warning::

      Veillez à choisir une version **64 bits**. Si vous installez un système **32 bits**, certains paquets ne sont disponibles que pour ``aarch64`` (64 bits), et certaines fonctionnalités risquent de ne pas s’installer ou de ne pas fonctionner correctement.

   .. image:: img/imager_os.png
      :width: 90%

#. Dans la section **Stockage**, sélectionnez votre **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_promax:

3. Configurer le démarrage depuis le SSD
--------------------------------------------

Dans cette section, nous allons configurer votre Raspberry Pi pour qu'il démarre directement depuis un SSD NVMe, offrant des temps de démarrage plus rapides et des performances améliorées par rapport à une carte SD. Suivez attentivement ces étapes :

#. Tout d'abord, ouvrez un terminal sur votre Raspberry Pi et exécutez la commande suivante pour accéder à l'interface de configuration :

   .. code-block:: shell

      sudo raspi-config

#. Dans le menu ``raspi-config``, utilisez les touches fléchées pour naviguer et sélectionnez **Options avancées**. Appuyez sur ``Entrée`` pour accéder aux paramètres avancés.

   .. image:: img/nvme_open_config.png

#. Dans **Options avancées**, sélectionnez **Ordre de démarrage**. Ce paramètre vous permet de spécifier l'ordre dans lequel votre Raspberry Pi recherche les périphériques amorçables.

   .. image:: img/nvme_boot_order.png

#. Ensuite, choisissez **Démarrage NVMe/USB**. Cela indique au Raspberry Pi de prioriser le démarrage depuis des SSD connectés en USB ou des lecteurs NVMe par rapport à d'autres options, comme la carte SD.

   .. image:: img/nvme_boot_nvme.png

#. Après avoir sélectionné l'ordre de démarrage, appuyez sur **Terminer** pour quitter raspi-config. Vous pouvez également utiliser la touche **Échap** pour fermer l'outil de configuration.

   .. image:: img/nvme_boot_ok.png

#. Pour appliquer les nouveaux paramètres de démarrage, redémarrez votre Raspberry Pi en exécutant ``sudo reboot``.

   .. code-block:: shell

      sudo reboot

   .. image:: img/nvme_boot_reboot.png

Après le redémarrage, le Raspberry Pi devrait maintenant tenter de démarrer à partir de votre SSD NVMe connecté, vous offrant des performances et une durabilité améliorées pour votre système.

.. end_copy_nvme