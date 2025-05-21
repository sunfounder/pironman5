.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Plongez dans l’univers du Raspberry Pi, d’Arduino et d’ESP32 avec d’autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Bénéficiez de l’aide de notre communauté et de notre équipe pour résoudre les problèmes après-vente et relever les défis techniques.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Profitez d’un accès anticipé aux annonces de nouveaux produits et à des aperçus inédits.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des campagnes promotionnelles.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Configuration sur Raspberry Pi OS / Ubuntu / Kali / Homebridge
================================================================

Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devrez configurer le Pironman 5 via la ligne de commande. Des tutoriels détaillés sont disponibles ci-dessous :

.. note::

  Avant de procéder à la configuration, vous devez démarrer votre Raspberry Pi et vous y connecter. Si vous ne savez pas comment faire, consultez le site officiel de Raspberry Pi : |link_rpi_get_start|.


Configuration de l'arrêt pour désactiver l'alimentation GPIO
-----------------------------------------------------------------------
Pour éviter que l’écran OLED et les ventilateurs RGB, alimentés par les broches GPIO du Raspberry Pi, restent actifs après l’arrêt du système, il est essentiel de configurer la désactivation de l’alimentation GPIO.

#. Modifiez manuellement le fichier de configuration ``EEPROM`` avec la commande suivante :

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e


#. Modifiez la valeur du paramètre ``POWER_OFF_ON_HALT`` en ``1``. Exemple :

   .. code-block:: shell

     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Appuyez sur ``Ctrl + X``, ``Y`` puis sur ``Entrée`` pour enregistrer les modifications.


Téléchargement et installation du module ``pironman5``
-------------------------------------------------------------

#. Pour les systèmes minimalistes, commencez par installer les outils nécessaires comme ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Téléchargez ensuite le code depuis GitHub et installez le module ``pironman5`` :

   .. code-block:: shell

      cd ~
      git clone https://github.com/sunfounder/pironman5.git
      cd ~/pironman5
      sudo python3 install.py

   Une fois l’installation réussie, redémarrez le système pour finaliser l’activation. Suivez les instructions affichées à l’écran.

   Au redémarrage, le service ``pironman5.service`` se lancera automatiquement. Voici les principales fonctionnalités activées :

   * L’écran OLED affiche l’utilisation du CPU, de la RAM, du disque, la température du processeur et l’adresse IP du Raspberry Pi.
   * Quatre LED RGB WS2812 s’allument en bleu avec un effet de respiration.

   .. note::

      Les ventilateurs RGB ne s’activent que si la température atteint 60 °C. Pour modifier ce seuil, consultez :ref:`cc_control_fan`.

#. Vous pouvez utiliser l’outil ``systemctl`` pour ``démarrer``, ``arrêter``, ``redémarrer`` ou vérifier le ``statut`` de ``pironman5.service``.

   .. code-block:: shell

     sudo systemctl restart pironman5.service

   * ``restart`` : applique les nouvelles configurations du Pironman 5.
   * ``start/stop`` : permet d’activer ou de désactiver le service ``pironman5.service``.
   * ``status`` : affiche l’état actuel du service via l’outil ``systemctl``.

