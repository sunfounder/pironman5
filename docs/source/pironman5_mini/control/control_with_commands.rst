.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour explorer plus en profondeur l’univers du Raspberry Pi, d’Arduino et de l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez vos problèmes après-vente et défis techniques avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des conseils et tutoriels pour faire progresser vos compétences.
    - **Aperçus exclusifs** : Soyez les premiers à découvrir nos nouveaux produits et avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et événements spéciaux pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _view_control_commands_mini:

Contrôle par commandes
========================================
En plus de visualiser les données du Pironman 5 Mini et de contrôler divers périphériques via le tableau de bord, vous pouvez également utiliser des commandes pour les piloter.

.. note::

  * Pour le système **Home Assistant**, vous ne pouvez surveiller et contrôler le Pironman 5 Mini qu’en accédant au tableau de bord à l’adresse ``http://<ip>:34001``.
  * Toute modification de la configuration nécessite un redémarrage du service à l’aide de la commande ``pironman5 restart`` pour être prise en compte.

Afficher les configurations de base
----------------------------------------

Le module ``pironman5`` propose une configuration de base du Pironman, que vous pouvez consulter avec la commande suivante :

.. code-block:: shell

  sudo pironman5 -c

La configuration par défaut est la suivante :

.. code-block::

  {
      "system": {
          "rgb_color": "feff00",
          "rgb_brightness": 30,
          "rgb_style": "hue_cycle",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 12,
          "temperature_unit": "C",
          "gpio_fan_pin": 5,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "follow",
          "gpio_fan_led_pin": 6
      }
  }

Adaptez cette configuration selon vos besoins.

Utilisez ``pironman5`` ou ``pironman5 -h`` pour afficher l’aide.

.. code-block::

 usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] 
                          [{start,restart,stop}]Add commentMore actions

  Pironman 5 command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                          Debug level
    --background [BACKGROUND]
                          Run in background
    -rd, --remove-dashboard
                          Remove dashboard
    -cp [CONFIG_PATH], --config-path [CONFIG_PATH]
                          Config path
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                          GPIO fan LED state on/off/follow
    -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                          GPIO fan LED pin




.. note::

  À chaque modification de l’état du ``pironman5.service``, vous devez exécuter la commande suivante pour appliquer les changements :

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Vérifiez l’état du programme ``pironman5`` avec l’outil ``systemctl`` :

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Ou consultez les journaux générés par le programme :

  .. code-block:: shell

    ls /var/log/pironman5/
    cat /var/log/pironman5/main.log

Contrôler les LED RGB
--------------------------
La carte dispose de 4 LED RGB WS2812 contrôlables. Vous pouvez les activer ou désactiver, changer la couleur, ajuster la luminosité, modifier le style d’affichage et la vitesse de transition.

.. note::

  Chaque fois que vous modifiez l’état de ``pironman5.service``, vous devez exécuter la commande suivante pour que les changements de configuration prennent effet.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Pour allumer ou éteindre les LED RGB : ``true`` pour activer, ``false`` pour désactiver :

.. code-block:: shell

  sudo pironman5 -re true

* Pour changer la couleur, entrez une valeur hexadécimale, ex. : ``fe1a1a`` :

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Pour ajuster la luminosité des LED RGB (0 à 100 %) :

.. code-block:: shell

  sudo pironman5 -rb 100

* Pour modifier le style d’affichage RGB, choisissez parmi : ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` :

.. note::

  Si vous choisissez ``rainbow``, ``rainbow_reverse`` ou ``hue_cycle``, vous ne pourrez pas définir manuellement la couleur via ``sudo pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Pour régler la vitesse de transition (0 à 100 %) :

.. code-block:: shell

  sudo pironman5 -rp 80

* Par défaut, 4 LED RGB sont configurées. Pour connecter plus de LED, mettez à jour le nombre :

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_mini:

Contrôler le ventilateur RGB
---------------------------------
La carte d’extension prend en charge un ventilateur 5V non-PWM.

.. note::

  Après toute modification, redémarrez le service :

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Vous pouvez configurer le mode de fonctionnement du ventilateur RGB selon les conditions de déclenchement souhaitées.

Par exemple, en mode **1: Performance**, le ventilateur s’active à 50°C :


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Silencieux** : activation à 70°C  
* **3: Équilibré** : activation à 67,5°C  
* **2: Froid** : activation à 60°C  
* **1: Performance** : activation à 50°C  
* **0: Toujours actif** : le ventilateur reste en marche

* Si la broche de commande du ventilateur RGB est connectée à une autre broche GPIO, utilisez cette commande pour la modifier :

.. code-block:: shell

  sudo pironman5 -gp 18
