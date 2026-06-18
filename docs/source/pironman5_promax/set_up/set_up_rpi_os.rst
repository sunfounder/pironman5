
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_set_up_pi_os:

Configuration sur Raspberry Pi/Ubuntu/Kali/Homebridge OS
==============================================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devrez configurer le Pironman 5 Pro MAX en utilisant la ligne de commande. Des tutoriels détaillés sont disponibles ci-dessous :

.. note::

  Avant de configurer, vous devez démarrer et vous connecter à votre Raspberry Pi. Si vous ne savez pas comment vous connecter, vous pouvez visiter le site officiel de Raspberry Pi : |link_rpi_get_start|.

.. _safe_shutdown_promax:

Configuration de l'arrêt pour désactiver l'alimentation GPIO
------------------------------------------------------------

Pour éviter que l'écran OLED et les Ventilateurs GPIO, alimentés par le GPIO du Raspberry Pi, ne restent actifs après l'arrêt, il est essentiel de configurer le Raspberry Pi pour désactiver l'alimentation GPIO.

#. Ouvrez l'outil de configuration EEPROM :

   .. code-block::

      sudo raspi-config

#. Naviguez vers **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Sélectionnez **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Enregistrez les modifications. Un redémarrage vous sera demandé pour que les nouveaux paramètres prennent effet.

.. _promax_download_pironman5_module:

Téléchargement et installation du module ``pironman5``
-----------------------------------------------------------

.. .. note::

..    Pour les systèmes lite, installez d'abord des outils comme ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

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

   Au redémarrage, le ``pironman5.service`` démarrera automatiquement. Voici les principales configurations du Pironman 5 Pro MAX :

   * L'écran OLED affiche le CPU, la RAM, l'utilisation du disque, la température du CPU et l'adresse IP du Raspberry Pi.
   * Quatre LEDs RGB WS2812 s'allumeront en bleu avec un mode de respiration.

#. Vous pouvez utiliser l'outil ``systemctl`` pour ``démarrer``, ``arrêter``, ``redémarrer`` ou vérifier le ``statut`` de ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart`` : Utilisez cette commande pour appliquer les modifications apportées aux paramètres du Pironman 5 Pro MAX.
   * ``start/stop`` : Activez ou désactivez le ``pironman5.service``.
   * ``status`` : Vérifiez l'état de fonctionnement du programme ``pironman5`` en utilisant l'outil ``systemctl``.

.. note::

   À ce stade, vous avez configuré avec succès le Pironman 5 Pro MAX, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`control_commands_dashboard_promax`.
