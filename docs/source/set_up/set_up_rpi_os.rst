.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et surmontez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _set_up_pironman5:

Configuration sur Raspberry Pi/Ubuntu/Kali/Homebridge OS
================================================================

Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devrez configurer le Pironman 5 en utilisant la ligne de commande. Des tutoriels détaillés sont disponibles ci-dessous :

.. note::

  Avant de procéder à la configuration, vous devez démarrer et vous connecter à votre Raspberry Pi. Si vous ne savez pas comment vous connecter, vous pouvez consulter le site officiel de Raspberry Pi : |link_rpi_get_start|.


Configuration de l'extinction pour désactiver l'alimentation GPIO
-----------------------------------------------------------------------
Pour éviter que l'écran OLED et les ventilateurs RGB, alimentés par le GPIO du Raspberry Pi, restent actifs après l'extinction, il est essentiel de configurer le Raspberry Pi pour désactiver l'alimentation GPIO.

* Modifiez manuellement le fichier de configuration ``EEPROM`` avec cette commande :

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e


* Modifiez le paramètre ``POWER_OFF_ON_HALT`` dans le fichier en le réglant sur ``1``. Par exemple :

  .. code-block:: shell

    BOOT_UART=1
    POWER_OFF_ON_HALT=1
    BOOT_ORDER=0xf41

* Appuyez sur ``Ctrl + X``, ``Y`` puis ``Entrée`` pour enregistrer les modifications.


Téléchargement et installation du module ``pironman5``
-------------------------------------------------------------

.. note::

  Pour les systèmes légers, commencez par installer des outils tels que ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
  
   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

Ensuite, téléchargez le code depuis GitHub et installez le module ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone https://github.com/sunfounder/pironman5.git
      cd ~/pironman5
      sudo python3 install.py

Après une installation réussie, un redémarrage du système est nécessaire pour activer l'installation. Suivez l'invite de redémarrage affichée à l'écran.

Au redémarrage, le ``pironman5.service`` démarrera automatiquement. Voici les principales configurations pour le Pironman 5 :

  * L'écran OLED affiche l'utilisation du CPU, de la RAM, du disque, la température du CPU et l'adresse IP du Raspberry Pi.
  * Quatre LED RGB WS2812 s'allument en bleu avec un mode respiration.
  * Les ventilateurs RGB s'activeront à 60°C.

Vous pouvez utiliser l'outil ``systemctl`` pour ``démarrer``, ``arrêter``, ``redémarrer`` ou vérifier le ``statut`` du ``pironman5.service``.

.. code-block:: shell

  sudo systemctl restart pironman5.service

* ``restart`` : Utilisez cette commande pour appliquer les modifications apportées aux paramètres du pironman 5.
* ``start/stop`` : Activez ou désactivez le ``pironman5.service``.
* ``status`` : Vérifiez le statut opérationnel du programme ``pironman5`` à l'aide de l'outil ``systemctl``.

