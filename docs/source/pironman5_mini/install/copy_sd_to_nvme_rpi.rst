.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Bénéficiez de l’aide de notre communauté et de notre équipe pour résoudre vos problèmes techniques et après-vente.
    - **Apprendre et partager** : Échangez des astuces et tutoriels pour renforcer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces et démonstrations de nouveaux produits.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et événements spéciaux à l’occasion des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _copy_sd_to_nvme_rpi_mini:

Copier le système de la carte Micro SD vers un SSD NVMe
==================================================================

Si vous disposez d’un SSD NVMe mais que vous ne possédez pas d’adaptateur pour le connecter à votre ordinateur, vous pouvez utiliser une autre méthode : installez d’abord le système sur la carte Micro SD. Une fois que le Pironman 5 Mini démarre correctement, vous pourrez transférer le système vers le SSD NVMe.

* Commencez par :ref:`install_os_sd_rpi_mini`.
* Ensuite, démarrez et connectez-vous à votre Raspberry Pi. Si vous ne savez pas comment vous connecter, consultez le site officiel du Raspberry Pi : |link_rpi_get_start|.

Assurez-vous d’avoir terminé les étapes ci-dessus avant de poursuivre.


1. Activer le PCIe
--------------------

Par défaut, le connecteur PCIe est désactivé.

* Pour l’activer, ouvrez le fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Ajoutez la ligne suivante au fichier :

  .. code-block:: shell
  
    # Activer le connecteur PCIe externe
    dtparam=pciex1
  
* Il existe un alias plus mémorable pour ``pciex1`` ; vous pouvez donc ajouter ``dtparam=nvme`` dans ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    dtparam=nvme

* La connexion est certifiée pour des vitesses Gen 2.0 (5 GT/s), mais vous pouvez la forcer en Gen 3.0 (10 GT/s) en ajoutant les lignes suivantes dans votre fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    # Forcer la vitesse Gen 3.0
    dtparam=pciex1_gen=3
  
  .. warning::
  
    Le Raspberry Pi 5 n’est pas certifié pour la vitesse Gen 3.0, et des instabilités peuvent survenir avec certains périphériques PCIe.

* Appuyez sur ``Ctrl + X``, puis ``Y`` et ``Entrée`` pour enregistrer.


2. Installer le système d’exploitation sur le SSD
--------------------------------------------------------

Deux méthodes sont disponibles :

**Copier le système de la carte Micro SD vers le SSD**

#. Connectez un écran ou accédez au bureau via VNC Viewer. Cliquez sur **Logo Raspberry Pi** -> **Accessoires** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png
      

#. Sélectionnez correctement les options **Copier depuis** et **Copier vers**. Ne les inversez pas.

   .. image:: img/ssd_copy_from.png
      
#. Cochez l’option "NOUVEAUX UUID de partition" pour éviter les conflits de montage ou de démarrage.

   .. image:: img/ssd_copy_uuid.png
    
#. Cliquez sur **Démarrer**.

   .. image:: img/ssd_copy_click_start.png

#. Un message vous informera que le contenu du SSD sera effacé. Sauvegardez vos données avant de cliquer sur Oui.

   .. image:: img/ssd_copy_erase.png

#. Patientez pendant la copie.

**Utiliser Raspberry Pi Imager pour installer le système**

Si votre carte Micro SD contient une version avec interface graphique du système, vous pouvez utiliser un outil de gravure d’image (comme Raspberry Pi Imager) pour installer le système sur le SSD. Cet exemple utilise Raspberry Pi OS Bookworm, mais d'autres systèmes peuvent nécessiter l'installation préalable de l'outil de gravure.

#. Connectez un écran ou accédez au bureau via VNC Viewer. Puis cliquez sur **Logo Raspberry Pi** -> **Accessoires** -> **Imager**.

   .. image:: img/ssd_imager.png


#. Dans |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez **Raspberry Pi 5**.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Choisissez le **Système d’exploitation** recommandé.

   .. image:: img/ssd_os.png
      :width: 90%

#. Dans l’onglet **Stockage**, sélectionnez le SSD NVMe inséré.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Cliquez sur **SUIVANT**, puis **MODIFIER LES PARAMÈTRES** pour personnaliser votre système.

   .. note::

      Si vous utilisez un écran, vous pouvez ignorer ces étapes et cliquer sur 'Oui' pour lancer l’installation. Vous pourrez ajuster les paramètres plus tard.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Définissez un **nom d’hôte** pour votre Raspberry Pi.

   .. note::

      Le nom d’hôte est l’identifiant réseau de votre Pi. Vous pourrez y accéder via ``<hostname>.local`` ou ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png


#. Créez un **nom d’utilisateur** et un **mot de passe** pour le compte administrateur.

   .. note::

      Il est important de définir un mot de passe personnalisé car aucun mot de passe par défaut n’est fourni.

   .. image:: img/os_set_username.png


#. Configurez le réseau sans fil en entrant votre **SSID** et votre **mot de passe**.

   .. note::

      Définissez le ``Wireless LAN country`` en utilisant le code alpha-2 à deux lettres de la norme `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre localisation.

   .. image:: img/os_set_wifi.png

#. Pour activer la connexion à distance, cochez **enable SSH** dans l’onglet **Services**.

   * Pour l’authentification par mot de passe, utilisez ceux définis dans l’onglet **Général**.
   * Pour l’authentification par clé, cochez "Autoriser uniquement l’authentification par clé publique".

   .. image:: img/os_enable_ssh.png



#. Dans **Options**, vous pouvez activer la lecture d’un son à la fin, l’éjection automatique et la télémétrie.

   .. image:: img/os_options.png

#. Une fois les réglages terminés, cliquez sur **Enregistrer**, puis **Oui** pour appliquer.

   .. image:: img/os_click_yes.png
      :width: 90%

#. Si le SSD NVMe contient déjà des données, sauvegardez-les. Cliquez sur **Oui** pour poursuivre sans sauvegarde.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Quand vous voyez le message "Écriture réussie", l’image a bien été gravée. Vous pouvez démarrer depuis le SSD !

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _configure_boot_ssd_mini:

3. Configurer le démarrage depuis le SSD
-------------------------------------------

Cette section vous guide pour configurer le démarrage direct sur un SSD NVMe afin d’accélérer le démarrage et améliorer les performances.

#. Ouvrez un terminal sur le Raspberry Pi et exécutez :

   .. code-block:: shell

      sudo raspi-config

#. Dans le menu ``raspi-config``, allez dans **Options avancées** avec les flèches, puis appuyez sur ``Entrée``.

   .. image:: img/nvme_open_config.png

#. Sélectionnez **Ordre de démarrage** dans **Options avancées**.

   .. image:: img/nvme_boot_order.png

#. Choisissez **Démarrage NVMe/USB** pour prioriser les SSD connectés par USB ou NVMe.

   .. image:: img/nvme_boot_nvme.png

#. Appuyez sur **Terminer** pour quitter raspi-config. Vous pouvez aussi appuyer sur **Échap**.

   .. image:: img/nvme_boot_ok.png

#. Pour appliquer les nouveaux paramètres de démarrage, redémarrez votre Raspberry Pi en exécutant la commande ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

Au redémarrage, votre Raspberry Pi devrait désormais démarrer depuis le SSD NVMe connecté, offrant des performances et une fiabilité accrues.
