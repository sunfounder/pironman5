.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Configuration sur Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

.. image:: ../img/pironman5_mini_pic.jpg
    :width: 400
    :align: center

Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devrez configurer le Pironman 5 Mini en utilisant la ligne de commande. Vous trouverez ci-dessous des tutoriels détaillés.

.. note::

  Avant de procéder à la configuration, vous devez démarrer et vous connecter à votre Raspberry Pi.
  Si vous n'êtes pas sûr de la procédure de connexion, vous pouvez visiter le site officiel de Raspberry Pi : |link_rpi_get_start|.


.. _safe_shutdown_mini:

1. Configuration de l'arrêt pour désactiver l'alimentation GPIO
-----------------------------------------------------------------

Pour éviter que le ventilateur RGB, alimenté par le GPIO du Raspberry Pi, ne reste actif après l'arrêt, il est essentiel de configurer le Raspberry Pi pour désactiver l'alimentation GPIO.

#. Ouvrez l'outil de configuration EEPROM :

   .. code-block::

      sudo raspi-config

#. Accédez à **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Sélectionnez **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Enregistrez les modifications. Il vous sera demandé de redémarrer afin que les nouveaux paramètres prennent effet.


.. _install_pironman5_module_mini:

2. Installation du module ``pironman5``
-----------------------------------------------------------

.. .. note::

..    Pour les systèmes « lite », installez d'abord des outils comme ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. Téléchargez et installez le module ``pironman5`` depuis GitHub.

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash



   .. note::

      1. Si vous utilisez **Ubuntu**, installez ``curl`` d'abord : ``sudo apt install curl -y``

      2. Si vous utilisez la série Pironman 5 avec **PiPower 5**, exécutez plutôt la commande suivante :

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

   #. Après le démarrage réussi du Pironman 5 Mini, vérifiez que les composants suivants fonctionnent correctement.

   * **Bouton d'alimentation**

     * Appui bref : Allumer.
     * Maintenir pendant 2 secondes : Arrêt sécurisé (nécessite :ref:`safe_shutdown_mini`).
     * Maintenir pendant 5 secondes : Arrêt forcé.

   * **LEDs RGB WS2812**

     * S'allument en bleu avec un effet de respiration.

   * **Ventilateur RGB**

     * Réglé sur le mode **Toujours activé** par défaut.
     * Le mode de fonctionnement peut être modifié via des commandes ou le Tableau de bord. Voir :ref:`cc_control_fan_mini`.

   * **Ventilateur du CPU (ventilateur de refroidissement actif)**

     * Ajuste automatiquement la vitesse en fonction de la température du CPU.
     * Courbe du ventilateur par défaut :

       * < 50°C : Arrêt (0 %)
       * 50°C+ : Faible (30 %)
       * 60°C+ : Moyen (50 %)
       * 67,5°C+ : Élevé (70 %)
       * 75°C+ : Pleine vitesse (100 %)

#. Utilisez ``systemctl`` pour gérer le ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Remplacez ``restart`` par ``start``, ``stop`` ou ``status`` selon vos besoins pour gérer le service.

.. note::

   Le Pironman 5 Mini est maintenant prêt à être utilisé.

   Pour les contrôles avancés et les fonctionnalités du tableau de bord, consultez :ref:`control_commands_dashboard_mini`.
