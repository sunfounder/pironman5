.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Explorez plus en profondeur l’univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Bénéficiez de l’aide de notre équipe et de la communauté pour résoudre les problèmes après-vente et les défis techniques.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Accédez en avance aux annonces de nouveaux produits et à des aperçus inédits.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et des événements spéciaux pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_copy_sd_to_nvme_rpi:

Copier le système d’exploitation de la carte Micro SD vers un SSD NVMe
========================================================================

Si vous possédez un SSD NVMe sans adaptateur pour le connecter à votre ordinateur, vous pouvez utiliser une autre méthode : commencez par installer le système sur une carte Micro SD. Une fois le Pironman 5 MAX démarré avec succès, vous pourrez transférer le système de la carte Micro SD vers le SSD NVMe.

* Commencez par suivre les étapes décrites ici : :ref:`max_install_os_sd_rpi`.
* Ensuite, démarrez votre Raspberry Pi et connectez-vous. Si vous ne savez pas comment faire, consultez le site officiel de Raspberry Pi : |link_rpi_get_start|.

Une fois ces étapes terminées, suivez les instructions ci-dessous.


1. Activer le PCIe
--------------------

Par défaut, le connecteur PCIe est désactivé.

* Pour l’activer, éditez le fichier ``/boot/firmware/config.txt`` :

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* Ajoutez ensuite la ligne suivante :

  .. code-block:: shell

    # Activer le connecteur PCIe externe.
    dtparam=pciex1

* Un alias plus explicite pour ``pciex1`` existe ; vous pouvez donc ajouter alternativement ``dtparam=nvme`` au fichier ``/boot/firmware/config.txt``.

  .. code-block:: shell

    dtparam=nvme

.. * La connexion est certifiée pour la vitesse Gen 2.0 (5 GT/s), mais vous pouvez forcer l’utilisation de Gen 3.0 (10 GT/s) avec ces lignes :

..   .. code-block:: shell

..     # Forcer la vitesse Gen 3.0
..     dtparam=pciex1_gen=3

..   .. warning::

..     Le Raspberry Pi 5 n’est pas certifié pour la Gen 3.0, ce qui peut entraîner une instabilité lors de la connexion à certains périphériques PCIe.

* Vous devez désactiver le délai de démarrage PCIe afin que le Raspberry Pi puisse détecter le disque NVMe situé derrière le commutateur PCIe au démarrage. Ajoutez la ligne suivante dans ``/boot/firmware/config.txt`` :

  .. code-block:: shell

    dtparam=pciex1_no_10s=on


* Appuyez sur ``Ctrl + X``, ``Y``, puis ``Entrée`` pour enregistrer les modifications.


**ORDRE DE DÉMARRAGE**

Si vous avez installé deux disques NVMe avec un système, vous pouvez choisir celui à démarrer en modifiant la ligne ``ROOT=PARTUUID=xxxxxxxxx`` dans le fichier ``/boot/firmware/cmdline.txt``. Pour identifier l’UUID des disques, utilisez :

.. code-block:: shell

   ls /dev/disk/by-id/


2. Installer le système d’exploitation sur le SSD
-----------------------------------------------------

Deux options s’offrent à vous pour installer un OS sur le SSD :

**Copier le système depuis la carte Micro SD vers le SSD**

#. Connectez un écran ou utilisez VNC Viewer pour accéder au bureau. Cliquez ensuite sur **logo Raspberry Pi** -> **Accessoires** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png


#. Sélectionnez les bons périphériques dans **Source** et **Destination**. Attention à ne pas les inverser.

   .. image:: img/ssd_copy_from.png

#. Activez l’option "NOUVEAUX UUID de partitions" pour éviter les conflits de montage ou de démarrage.

   .. image:: img/ssd_copy_uuid.png

#. Cliquez sur **Démarrer**.

   .. image:: img/ssd_copy_click_start.png

#. Un message vous avertira que le contenu du SSD sera effacé. Sauvegardez vos données avant de cliquer sur Oui.

   .. image:: img/ssd_copy_erase.png

#. Patientez pendant la copie jusqu’à ce qu’elle soit terminée.


**Installer le système avec Raspberry Pi Imager**

Si vous avez installé la version avec interface graphique sur la carte Micro SD, vous pouvez utiliser un outil d’imagerie comme Raspberry Pi Imager pour graver le système sur le SSD. L’exemple suivant utilise Raspberry Pi OS Bookworm.

#. Connectez un écran ou accédez au bureau via VNC Viewer. Cliquez sur **logo Raspberry Pi** -> **Accessoires** -> **Imager**.

   .. image:: img/ssd_imager.png


#. Dans |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez **Raspberry Pi 5**.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Choisissez le **système d’exploitation** recommandé.

   .. image:: img/ssd_os.png
      :width: 90%

#. Sélectionnez le SSD NVMe dans **Stockage**.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Cliquez sur **SUIVANT**, puis sur **MODIFIER LES PARAMÈTRES** pour personnaliser le système.

   .. note::

      Si vous avez un écran connecté, vous pouvez passer cette étape et cliquer sur « Oui » pour lancer l’installation. Les réglages pourront être ajustés plus tard.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Définissez un **hostname** pour le Raspberry Pi.

   .. note::

      Le nom d’hôte permet d’identifier votre Raspberry Pi sur le réseau : ``<hostname>.local`` ou ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png


#. Créez un **Username** et un **Password** pour l’administrateur.

   .. note::

      Choisissez un mot de passe sécurisé, car le système ne possède pas de mot de passe par défaut.

   .. image:: img/os_set_username.png


#. Configurez le Wi-Fi avec le **SSID** et le **Password** de votre réseau.

   .. note::

      Définissez le ``Wireless LAN country`` à l’aide du code alpha-2 à deux lettres de la norme `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre localisation.

   .. image:: img/os_set_wifi.png

#. Pour accéder au Raspberry Pi à distance, **enable SSH** dans l’onglet **Services**.

   * Pour **password authentication**, utilisez le nom d’utilisateur et le mot de passe définis dans l’onglet **General**.  
   * Pour l’authentification par clé publique, sélectionnez « Autoriser uniquement l’authentification par clé publique ». Si vous possédez une clé RSA, elle sera utilisée. Sinon, cliquez sur « Exécuter SSH-keygen » pour générer une nouvelle paire de clés.

   .. image:: img/os_enable_ssh.png



#. Dans le menu **Options**, vous pouvez activer la lecture audio à la fin, l’éjection automatique ou la télémétrie.

   .. image:: img/os_options.png

#. Une fois la personnalisation terminée, cliquez sur **Enregistrer**, puis sur **Oui** pour appliquer les réglages.

   .. image:: img/os_click_yes.png
      :width: 90%

#. Si le SSD NVMe contient déjà des données, pensez à les sauvegarder. Cliquez sur **Oui** si vous êtes prêt à effacer.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Une fois le message "Écriture réussie" affiché, votre système est prêt à démarrer depuis le SSD NVMe !

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _max_configure_boot_ssd:

3. Configurer le démarrage depuis le SSD
--------------------------------------------

Cette section vous guide pour configurer votre Raspberry Pi afin qu’il démarre directement depuis un SSD NVMe, offrant des temps de démarrage plus rapides et de meilleures performances.

#. Ouvrez un terminal et lancez la configuration :

   .. code-block:: shell

      sudo raspi-config

#. Dans le menu ``raspi-config`` , naviguez avec les flèches jusqu’à **Advanced Options**, puis appuyez sur ``Enter``.

   .. image:: img/nvme_open_config.png

#. Dans **Advanced Options**, sélectionnez **Boot Order** pour définir la priorité des périphériques.

   .. image:: img/nvme_boot_order.png

#. Choisissez ensuite **NVMe/USB boot**, pour prioriser le démarrage depuis un SSD NVMe ou un périphérique USB.

   .. image:: img/nvme_boot_nvme.png

#. Une fois la sélection faite, appuyez sur **Finish** ou utilisez **Escape** pour quitter l’outil.

   .. image:: img/nvme_boot_ok.png

#. Pour appliquer les nouveaux paramètres de démarrage, redémarrez votre Raspberry Pi en exécutant la commande ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

Après redémarrage, le Raspberry Pi devrait désormais démarrer directement depuis le SSD NVMe connecté, offrant ainsi des performances et une durabilité accrues.


