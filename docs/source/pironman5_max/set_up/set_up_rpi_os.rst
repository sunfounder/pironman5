.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances et vos projets autour de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes techniques et après-vente grâce à l’aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des conseils et tutoriels pour renforcer vos compétences.
    - **Avant-premières exclusives** : Profitez d’un accès anticipé aux annonces et démonstrations de nouveaux produits.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et offres promotionnelles pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_set_up_pi_os:

Configuration sur Raspberry Pi/Ubuntu/Kali/Homebridge OS
=================================================================

Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devez configurer le Pironman 5 MAX via la ligne de commande. Vous trouverez ci-dessous les tutoriels détaillés :

.. note::

  Avant de procéder à la configuration, démarrez et connectez-vous à votre Raspberry Pi. Si vous ne savez pas comment faire, consultez le site officiel de Raspberry Pi : |link_rpi_get_start|.


Configuration de l'extinction pour désactiver l'alimentation des GPIO
--------------------------------------------------------------------------

Pour éviter que l’écran OLED et les ventilateurs RGB, alimentés par les broches GPIO du Raspberry Pi, restent actifs après l’arrêt du système, il est nécessaire de configurer l’extinction de l’alimentation GPIO.

#. Modifiez manuellement le fichier de configuration de la ``EEPROM`` avec la commande suivante :

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. Modifiez le paramètre ``POWER_OFF_ON_HALT`` et définissez-le à ``1``. Exemple :

   .. code-block:: shell

     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Appuyez sur ``Ctrl + X``, puis ``Y`` et ``Entrée`` pour enregistrer les modifications.


Téléchargement et installation du module ``pironman5``
-----------------------------------------------------------

#. Pour les systèmes Lite, commencez par installer les outils nécessaires : ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Téléchargez ensuite le code depuis GitHub et installez le module ``pironman5`` :

   .. code-block:: shell

      cd ~
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Une fois l’installation réussie, un redémarrage du système est nécessaire. Suivez l’invite affichée pour redémarrer.

   Au redémarrage, le service ``pironman5.service`` démarrera automatiquement. Voici les principales fonctions activées :

   * L’écran OLED affiche l’utilisation CPU, RAM, Disque, la température du CPU, et l’adresse IP du Raspberry Pi.
   * Quatre LED RGB WS2812 s’allument en bleu avec un effet « respiration » (breathing).

   .. note::

     Les ventilateurs RGB ne tournent que si la température atteint 60 °C. Pour modifier cette température, consultez : :ref:`max_cc_control_fan`.

#. Vous pouvez utiliser l’outil ``systemctl`` pour ``start``, ``stop``, ``restart`` ou vérifier le ``status`` de ``pironman5.service`` :

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart`` : applique les modifications de configuration.
   * ``start/stop`` : active ou désactive le service ``pironman5.service``.
   * ``status`` : vérifie l’état de fonctionnement du programme ``pironman5`` via ``systemctl``.

.. note::

   À ce stade, vous avez correctement configuré le Pironman 5 MAX, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`control_commands_dashboard_max`.
