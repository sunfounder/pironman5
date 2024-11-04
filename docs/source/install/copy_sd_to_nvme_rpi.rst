.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _copy_sd_to_nvme_rpi:

Copier l'OS de la carte Micro SD vers le SSD NVMe
==================================================================

Si vous disposez d'un SSD NVMe mais que vous n'avez pas d'adaptateur pour le connecter à votre ordinateur, vous pouvez choisir une troisième approche: installez d'abord le système sur votre carte Micro SD. Une fois que le Pironman 5 a démarré avec succès, vous pouvez transférer le système de votre carte Micro SD vers votre SSD NVMe.

* Commencez par :ref:`install_os_sd_rpi`.
* Ensuite, démarrez et connectez-vous à votre Raspberry Pi. Si vous ne savez pas comment vous connecter, vous pouvez consulter le site officiel de Raspberry Pi: |link_rpi_get_start|.

Terminez ces étapes avant de poursuivre avec les instructions ci-dessous.


1. Activer le PCIe
--------------------

Par défaut, le connecteur PCIe n'est pas activé.

* Pour l'activer, vous devez ouvrir le fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Ajoutez ensuite la ligne suivante au fichier. 

  .. code-block:: shell
  
    # Activer le connecteur PCIe externe.
    dtparam=pciex1
  
* Un alias plus mémorable pour ``pciex1`` existe, vous pouvez donc également ajouter ``dtparam=nvme`` au fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    dtparam=nvme

* La connexion est certifiée pour des vitesses Gen 2.0 (5 GT/sec), mais vous pouvez la forcer à Gen 3.0 (10 GT/sec) en ajoutant les lignes suivantes à votre fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    # Forcer les vitesses Gen 3.0
    dtparam=pciex1_gen=3
  
  .. warning::
  
    Le Raspberry Pi 5 n'est pas certifié pour les vitesses Gen 3.0, et les connexions aux périphériques PCIe à ces vitesses peuvent être instables.

* Appuyez sur ``Ctrl + X``, ``Y`` et ``Entrée`` pour enregistrer les modifications.


2. Installer l'OS sur le SSD
----------------------------------------

Il existe deux façons d'installer un système d'exploitation sur le SSD :

**Copier le Système de la Carte Micro SD vers le SSD**

#. Connectez un écran ou accédez au bureau du Raspberry Pi via VNC Viewer. Puis cliquez sur **Logo Raspberry Pi** -> **Accessoires** -> **Copieur de carte SD**.

   .. image:: img/ssd_copy.png
      
    
#. Assurez-vous de sélectionner les bons périphériques **Copier de** et **Copier vers**. Faites attention à ne pas les confondre.

   .. image:: img/ssd_copy_from.png
      
#. Après avoir fait la sélection, cliquez sur **Démarrer**.

   .. image:: img/ssd_copy_start.png

#. Un message vous avertira que le contenu du SSD sera effacé. Sauvegardez vos données avant de cliquer sur Oui.

   .. image:: img/ssd_copy_erase.png

#. Patientez un moment, et la copie sera terminée.


**Installer le Système avec Raspberry Pi Imager**

Si votre carte Micro SD a une version de bureau du système installée, vous pouvez utiliser un outil d'imagerie (comme Raspberry Pi Imager) pour graver le système sur le SSD. Cet exemple utilise Raspberry Pi OS Bookworm, mais d'autres systèmes peuvent nécessiter l'installation préalable de l'outil d'imagerie.

#. Connectez un écran ou accédez au bureau du Raspberry Pi via VNC Viewer. Puis cliquez sur **Logo Raspberry Pi** -> **Accessoires** -> **Imager**.

   .. image:: img/ssd_imager.png

      
#. Dans |link_rpi_imager|, cliquez sur **Périphérique Raspberry Pi** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Sélectionnez **Système d'exploitation** et optez pour la version recommandée du système d'exploitation.

   .. image:: img/ssd_os.png
      :width: 90%
    
#. Dans l'option **Stockage**, sélectionnez votre SSD NVMe inséré.

   .. image:: img/nvme_storage.png
      :width: 90%
    
#. Cliquez sur **SUIVANT** puis sur **MODIFIER LES PARAMÈTRES** pour personnaliser vos paramètres OS.

   .. note::

      Si vous avez un moniteur pour votre Raspberry Pi, vous pouvez ignorer les étapes suivantes et cliquer sur 'Oui' pour commencer l'installation. Ajustez les autres paramètres plus tard sur le moniteur.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Définissez un **nom d'hôte** pour votre Raspberry Pi.

   .. note::

      Le nom d'hôte est l'identifiant réseau de votre Raspberry Pi. Vous pouvez accéder à votre Pi en utilisant ``<hostname>.local`` ou ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png
      

#. Créez un **Nom d'utilisateur** et un **Mot de passe** pour le compte administrateur du Raspberry Pi.

   .. note::

      Créer un nom d'utilisateur et un mot de passe uniques est essentiel pour sécuriser votre Raspberry Pi, qui n'a pas de mot de passe par défaut.

   .. image:: img/os_set_username.png
      

#. Configurez le réseau sans fil en fournissant le **SSID** et le **Mot de passe** de votre réseau.

   .. note::

      Réglez le ``pays du réseau sans fil`` sur le code alpha2 à deux lettres `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre emplacement.

   .. image:: img/os_set_wifi.png

#. Pour vous connecter à distance à votre Raspberry Pi, **activez SSH** dans l'onglet **Services**.

   * Pour **l'authentification par mot de passe**, utilisez le nom d'utilisateur et le mot de passe de l'onglet **Général**.
   * Pour l'authentification par clé publique, choisissez "Autoriser uniquement l'authentification par clé publique". Si vous avez une clé RSA, elle sera utilisée. Sinon, cliquez sur "Exécuter SSH-keygen" pour générer une nouvelle paire de clés.

   .. image:: img/os_enable_ssh.png

      

#. Le menu **Options** vous permet de configurer le comportement d'Imager pendant une écriture, notamment pour jouer un son à la fin, éjecter le support une fois terminé et activer la télémétrie.

   .. image:: img/os_options.png
    
#. Lorsque vous avez terminé de saisir les paramètres de personnalisation de l'OS, cliquez sur **Enregistrer** pour sauvegarder votre personnalisation. Ensuite, cliquez sur **Oui** pour les appliquer lors de l'écriture de l'image.

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. Si le SSD NVMe contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Continuez en cliquant sur **Oui** si aucune sauvegarde n'est nécessaire.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Lorsque vous voyez le message "Écriture réussie", votre image a été complètement écrite et vérifiée. Vous êtes maintenant prêt à démarrer un Raspberry Pi à partir du SSD NVMe !

   .. image:: img/nvme_install_finish.png
      :width: 90%
      

.. _configure_boot_ssd:

3. Configuration du démarrage depuis le SSD
-----------------------------------------------------

Dans cette section, nous allons configurer votre Raspberry Pi pour démarrer directement depuis un SSD NVMe, offrant des temps de démarrage plus rapides et des performances accrues par rapport à une carte SD. Suivez attentivement les étapes suivantes :

#. Tout d'abord, ouvrez un terminal sur votre Raspberry Pi et exécutez la commande suivante pour accéder à l'interface de configuration :

  .. code-block:: shell

      sudo raspi-config

#. Dans le menu ``raspi-config``, utilisez les touches fléchées pour sélectionner **Advanced Options**. Appuyez sur ``Entrée`` pour accéder aux paramètres avancés.

   .. image:: img/nvme_open_config.png

#. À l'intérieur de **Advanced Options**, sélectionnez **Boot Order**. Ce paramètre vous permet de spécifier l'ordre dans lequel votre Raspberry Pi recherche les périphériques amorçables.

   .. image:: img/nvme_boot_order.png

#. Ensuite, choisissez **NVMe/USB boot**. Cela indique au Raspberry Pi de prioriser le démarrage à partir de SSD connectés via USB ou de disques NVMe par rapport aux autres options, telles que la carte SD.

   .. image:: img/nvme_boot_nvme.png

#. Après avoir sélectionné l'ordre de démarrage, appuyez sur **Finish** pour quitter ``raspi-config``. Vous pouvez également utiliser la touche **Échap** pour fermer l'outil de configuration.

   .. image:: img/nvme_boot_ok.png

#. Pour appliquer les nouveaux paramètres de démarrage, redémarrez votre Raspberry Pi en exécutant :

   .. code-block:: shell

      sudo reboot

   .. image:: img/nvme_boot_reboot.png

Après le redémarrage, votre Raspberry Pi devrait tenter de démarrer depuis le SSD NVMe connecté, vous offrant des performances et une durabilité accrues pour votre système.





