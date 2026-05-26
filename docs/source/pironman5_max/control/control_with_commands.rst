.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _max_view_control_commands:

Contrôler avec des commandes
========================================
En plus de pouvoir consulter les données du Pironman 5 MAX et de contrôler divers appareils via le tableau de bord, vous pouvez également utiliser des commandes pour les gérer.

.. note::

  * Pour le système **Home Assistant**, vous pouvez uniquement surveiller et contrôler le Pironman 5 MAX via le tableau de bord en ouvrant la page web à l'adresse ``http://<ip>:34001``.

Consulter les configurations de base
----------------------------------------

Le module ``pironman5`` propose des configurations de base pour Pironman, que vous pouvez consulter avec la commande suivante.

.. code-block:: shell

  sudo pironman5 -c

Les configurations standard apparaissent comme suit :

.. code-block::

  {
      "system": {
          "data_interval": 1,
          "database_retention_days": 30,
          "temperature_unit": "C",
          "enable_history": true,
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "rgb_enable": true,
          "rgb_color": "#0a1aff",
          "rgb_brightness": 100,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_led_count": 4,
          "rgb_led_count_min": 4,
          "gpio_fan_pin": 6,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "on",
          "gpio_fan_led_pin": 5,
          "debug_level": "INFO"
      }
  }

Personnalisez ces configurations selon vos besoins.

Utilisez ``pironman5`` ou ``pironman5 -h`` pour les instructions.

.. code-block::


  usage: pironman5-service [-h] [-v] [-c] [-dl [{debug,info,warning,error,critical}]] [--background [BACKGROUND]] [-rd] [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-oe [OLED_ENABLE]]
                          [-od [OLED_DISK]] [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]]
                          [{start,restart,stop}]

  Pironman 5 - Interface en ligne de commande

  arguments positionnels :
    {start,restart,stop}  Commande

  options :
    -h, --help            Afficher ce message d'aide et quitter
    -v, --version         Afficher la version
    -c, --config          Afficher la configuration
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Jours de rétention de la base de données
    -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                          Niveau de débogage
    -rd, --remove-dashboard
                          Supprimer le tableau de bord
    -cp, --config-path [CONFIG_PATH]
                          Chemin de configuration
    -eh, --enable-history [ENABLE_HISTORY]
                          Activer l'historique, True/true/on/On/1 ou False/false/off/Off/0
    -re, --rgb-enable [RGB_ENABLE]
                          Activer RGB True/False
    -rs, --rgb-style [RGB_STYLE]
                          Style RGB : ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
    -rc, --rgb-color [RGB_COLOR]
                          Couleur RGB en format hexadécimal sans # (ex. 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          Luminosité RGB 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          Vitesse RGB 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          Nombre de LED RGB (entier)
    -u, --temperature-unit [{C,F}]
                          Unité de température
    -gm, --gpio-fan-mode [GPIO_FAN_MODE]
                          Mode ventilateur GPIO, 0: Toujours activé, 1: Performance, 2: Frais, 3: Équilibré, 4: Silencieux
    -gp, --gpio-fan-pin [GPIO_FAN_PIN]
                          Broche du ventilateur GPIO
    -oe, --oled-enable [OLED_ENABLE]
                          Activer OLED True/true/on/On/1 ou False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Rotation de l'écran OLED, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          Pages OLED, séparées par ',': mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          Délai de veille OLED en secondes

  Sous-commandes :
    {start,stop,launch-browser}
      start               Démarrer Pironman5
      stop                Arrêter Pironman5
      launch-browser      Lancer le navigateur

.. note::

   Chaque fois que vous modifiez l'état de ``pironman5.service``, vous devez utiliser la commande suivante pour que les modifications de configuration prennent effet.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Vérifiez l'état du programme ``pironman5`` à l'aide de l'outil ``systemctl``.

  .. code-block:: shell

     sudo systemctl status pironman5.service

* Vous pouvez également consulter les fichiers journaux générés par le programme.

  .. code-block:: shell

     cat /var/log/pironman5/pironman5.log


Contrôler les LED RGB
----------------------
La carte dispose de 4 LED RGB WS2812, offrant un contrôle personnalisable. Les utilisateurs peuvent les allumer ou les éteindre, changer la couleur, régler la luminosité, changer les modes d'affichage des LED RGB et définir la vitesse des changements.

.. note::

  Chaque fois que vous modifiez l'état de ``pironman5.service``, vous devez utiliser la commande suivante pour que les modifications de configuration prennent effet.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Pour modifier l'état d'activation des LED RGB, utilisez ``true`` pour les allumer ou ``false`` pour les éteindre.

.. code-block:: shell

  sudo pironman5 -re true

* Pour changer leur couleur, saisissez la valeur hexadécimale souhaitée, telle que ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Pour modifier la luminosité des LED RGB (plage : 0 ~ 100 %) :

.. code-block:: shell

  sudo pironman5 -rb 100

* Pour changer les modes d'affichage des LED RGB, choisissez parmi : ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` :

.. note::

  Si vous réglez le mode d'affichage des LED RGB sur ``rainbow``, ``rainbow_reverse`` ou ``hue_cycle``, vous ne pourrez pas définir la couleur avec ``pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Pour modifier la vitesse de changement (plage : 0 ~ 100 %) :

.. code-block:: shell

  sudo pironman5 -rp 80

* La configuration par défaut comprend 4 LED RGB. Connectez des LED supplémentaires et mettez à jour le nombre avec :

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_max:

Contrôler les ventilateurs GPIO
-----------------------------------
La carte d'extension IO prend en charge jusqu'à deux ventilateurs 5V non-CPU. Les deux ventilateurs sont contrôlés ensemble.

.. note::

  Chaque fois que vous modifiez l'état de ``pironman5.service``, vous devez utiliser la commande suivante pour que les modifications de configuration prennent effet.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Vous pouvez configurer le mode de fonctionnement des deux ventilateurs GPIO à l'aide de commandes. Ces modes déterminent les conditions dans lesquelles les ventilateurs GPIO s'activeront.

Par exemple, si réglé sur le mode **1: Performance**, les ventilateurs GPIO s'activeront à 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Silencieux** : Les ventilateurs GPIO s'activeront à 70°C.
* **3: Équilibré** : Les ventilateurs GPIO s'activeront à 67,5°C.
* **2: Frais** : Les ventilateurs GPIO s'activeront à 60°C.
* **1: Performance** : Les ventilateurs GPIO s'activeront à 50°C.
* **0: Toujours activé** : Les ventilateurs GPIO resteront toujours allumés.

* Si vous connectez la broche de contrôle du ventilateur RGB à une autre broche GPIO du Raspberry Pi, vous pouvez changer le numéro de broche avec :

  .. code-block:: shell

     sudo pironman5 -gp 18


À propos du ventilateur CPU
------------------------------

Le ventilateur CPU se connecte à un port dédié 4 broches pour ventilateur CPU sur le Raspberry Pi 5.

Sa stratégie de contrôle par défaut est un schéma intelligent de réglage de vitesse à plusieurs niveaux géré par le firmware, basé sur la température du CPU. Lorsque vous utilisez un ventilateur CPU officiel ou compatible et que vous le connectez correctement, le système ajustera automatiquement la vitesse du ventilateur en fonction des changements de température du CPU (à partir de ``50°C``) sans nécessiter d'intervention manuelle.


Vérifier l'écran OLED
---------------------------

Lorsque la bibliothèque ``pironman5`` est installée, l'écran OLED affiche automatiquement l'utilisation du CPU, de la RAM, du disque, la température du CPU et l'adresse IP du Raspberry Pi après chaque redémarrage.

Si l'écran OLED n'affiche aucun contenu, vérifiez d'abord si le câble FPC de l'OLED est correctement connecté.

Inspectez ensuite le journal du programme à l'aide de la commande suivante :

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

Vous pouvez également vérifier si l'adresse I2C ``0x3C`` de l'OLED est détectée :

.. code-block:: shell

   i2cdetect -y 1


Vérifier le récepteur infrarouge
---------------------------------------

* Installez le module ``lirc`` :

  .. code-block:: shell

     sudo apt-get install lirc -y

* Testez le récepteur IR à l'aide de la commande suivante :

  .. code-block:: shell

     mode2 -d /dev/lirc0

* Après avoir exécuté la commande, appuyez sur un bouton de la télécommande. Le code IR correspondant s'affichera dans le terminal.
