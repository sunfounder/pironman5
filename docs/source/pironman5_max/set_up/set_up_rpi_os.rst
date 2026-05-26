.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_os_max:

Configuration sur Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
==================================================================

.. image:: ../img/pironman5_max.jpg
    :width: 400
    :align: center


Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devrez configurer le Pironman 5 MAX en ligne de commande.

.. note::

  Avant la configuration, vous devez démarrer et vous connecter à votre Raspberry Pi. Si vous ne savez pas comment vous connecter, vous pouvez consulter le site officiel de Raspberry Pi : |link_rpi_get_start|.


.. _safe_shutdown_max:

1. Configuration de l'arrêt pour désactiver l'alimentation GPIO
----------------------------------------------------------------------------------------

Pour éviter que l'écran OLED et les ventilateurs GPIO, alimentés par le GPIO du Raspberry Pi, ne restent actifs après l'arrêt, il est essentiel de configurer le Raspberry Pi pour désactiver l'alimentation GPIO.

#. Ouvrez l'outil de configuration EEPROM :

   .. code-block::

      sudo raspi-config

#. Naviguez vers **Options avancées → A12 Comportement à l'arrêt**.

   .. image:: img/shutdown_behaviour.png

#. Sélectionnez **B1 Alimentation complètement coupée...**.

   .. image:: img/run_power_off.png

#. Enregistrez les modifications. Vous serez invité à redémarrer pour que les nouveaux paramètres prennent effet.


.. _install_pironman5_module_max:

2. Installation du module ``pironman5``
-----------------------------------------------------------

.. note::

   Pour les systèmes Raspberry Pi OS Lite, installez d'abord les outils nécessaires tels que ``git`` et ``python3``.

   .. code-block:: shell

      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Téléchargez et installez le module ``pironman5`` depuis GitHub.

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

   .. note::

      Si vous utilisez la série Pironman 5 avec PiPower 5, exécutez plutôt la commande suivante :

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --pipower5

#. Après avoir lancé l'installateur, sélectionnez votre modèle Pironman 5 (1~4).

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. Une fois l'installation terminée, redémarrez le Raspberry Pi comme demandé. Le premier démarrage peut prendre jusqu'à 30 secondes le temps que les services s'initialisent.

#. Une fois le Pironman 5 MAX démarré avec succès, vérifiez que les composants suivants fonctionnent correctement.

   * **Écran OLED**

     * Affiche l'utilisation du CPU, de la RAM, la température du CPU et l'adresse IP.
     * S'éteint automatiquement après 10 secondes.
     * Appuyez brièvement sur le bouton d'alimentation pour réveiller l'écran ou changer de page.

   * **Bouton d'alimentation**

     * Appui bref : Allumer / réveiller l'OLED / changer de page OLED.
     * Maintenir 2 secondes : Arrêt sécurisé (nécessite :ref:`safe_shutdown_max`).
     * Maintenir 5 secondes : Arrêt forcé.

   * **LED RGB WS2812**

     * S'allument en bleu avec un effet de respiration.

   * **Deux ventilateurs GPIO**

     * Réglés en mode **Toujours activé** par défaut.
     * Le mode de fonctionnement peut être modifié via des commandes ou le tableau de bord.

   * **Ventilateur CPU (ventilateur du refroidisseur tour)**

     * Ajuste automatiquement sa vitesse en fonction de la température du CPU.
     * Courbe par défaut du ventilateur :

       * < 50°C : Arrêt (0 %)
       * 50°C+ : Basse (30 %)
       * 60°C+ : Moyenne (50 %)
       * 67,5°C+ : Élevée (70 %)
       * 75°C+ : Pleine vitesse (100 %)

      * :ref:`faq_pwm_fan_max`

#. Utilisez ``systemctl`` pour gérer le ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Remplacez ``restart`` par ``start``, ``stop`` ou ``status`` selon vos besoins pour gérer le service.

.. note::

   Le Pironman 5 est maintenant prêt à l'emploi.

   Pour les contrôles avancés et les fonctionnalités du tableau de bord, consultez :ref:`control_commands_dashboard_max`.
