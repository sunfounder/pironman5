.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez au cœur de l’univers Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l’aide de notre équipe et de la communauté.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Soyez parmi les premiers informés des nouveaux produits et aperçus.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et événements promotionnels pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_view_control_commands:

Contrôle via Commandes
========================================
En plus d’afficher les données du Pironman 5 et de contrôler divers appareils via le tableau de bord, vous pouvez également utiliser des commandes pour les piloter.

.. note::

  * Pour le système **Home Assistant**, vous ne pouvez surveiller et contrôler le Pironman 5 qu’à travers le tableau de bord, accessible à l’adresse ``http://<ip>:34001``.
  * Pour le système **Batocera.linux**, le contrôle du Pironman 5 s’effectue uniquement via des commandes. Notez que toute modification de la configuration nécessite un redémarrage du service via la commande ``pironman5 restart`` pour être prise en compte.

Afficher les configurations de base
---------------------------------------

Le module ``pironman5`` propose des configurations de base pour le Pironman, que vous pouvez consulter à l’aide de la commande suivante :

.. code-block:: shell

  pironman5 -c

Les configurations par défaut s’affichent ainsi :

.. code-block::

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

Personnalisez ces paramètres selon vos besoins.

Utilisez ``pironman5`` ou ``pironman5 -h`` pour obtenir de l’aide.

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc RGB_COLOR] [-rb RGB_BRIGHTNESS] [-rs {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}] [-rp RGB_SPEED] [-re RGB_ENABLE]
                          [-rl RGB_LED_COUNT] [-u {C,F}] [-gm GPIO_FAN_MODE] [-gp GPIO_FAN_PIN]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc RGB_COLOR, --rgb-color RGB_COLOR
                          RGB color
    -rb RGB_BRIGHTNESS, --rgb-brightness RGB_BRIGHTNESS
                          RGB brightness
    -rs {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}, --rgb-style {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}
                          RGB style
    -rp RGB_SPEED, --rgb-speed RGB_SPEED
                          RGB speed
    -re RGB_ENABLE, --rgb-enable RGB_ENABLE
                          RGB enable
    -rl RGB_LED_COUNT, --rgb-led-count RGB_LED_COUNT
                          RGB LED count
    -u {C,F}, --temperature-unit {C,F}
                          Temperature unit
    -gm GPIO_FAN_MODE, --gpio-fan-mode GPIO_FAN_MODE
                          GPIO fan mode, 0-4, ['Always On', 'Performance', 'Cool', 'Balanced', 'Quiet']
    -gp GPIO_FAN_PIN, --gpio-fan-pin GPIO_FAN_PIN
                          GPIO fan pin



.. note::

  À chaque modification de l’état du service ``pironman5.service``, vous devez exécuter la commande suivante pour appliquer les changements :

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Vérifiez l’état du programme ``pironman5`` à l’aide de l’outil ``systemctl`` :

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Vous pouvez également consulter les fichiers journaux générés par le programme :

  .. code-block:: shell

    ls /var/log/pironman5/


Contrôle des LEDs RGB
----------------------
La carte dispose de 4 LEDs RGB WS2812 entièrement personnalisables. Vous pouvez les allumer ou les éteindre, changer leur couleur, ajuster leur luminosité, modifier le mode d'affichage, et régler la vitesse des effets.

.. note::

  Chaque modification de l’état de ``pironman5.service`` nécessite l'exécution de la commande suivante pour appliquer les changements :

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Pour allumer ou éteindre les LEDs RGB, utilisez ``true`` pour allumer et ``false`` pour éteindre :

.. code-block:: shell

  pironman5 -re true

* Pour changer leur couleur, indiquez une valeur hexadécimale, par exemple ``fe1a1a`` :

.. code-block:: shell

  pironman5 -rc fe1a1a

* Pour ajuster la luminosité (plage : 0 ~ 100%) :

.. code-block:: shell

  pironman5 -rb 100

* Pour modifier le mode d’affichage RGB, choisissez parmi : ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` :

.. note::

  Si vous sélectionnez ``rainbow``, ``rainbow_reverse`` ou ``hue_cycle``, vous ne pourrez pas définir la couleur via ``pironman5 -rc``.

.. code-block:: shell

  pironman5 -rs breathing

* Pour ajuster la vitesse des effets (plage : 0 ~ 100%) :

.. code-block:: shell

  pironman5 -rp 80

* Par défaut, 4 LEDs RGB sont utilisées. Pour en connecter davantage, indiquez le nombre :

.. code-block:: shell

  pironman5 -rl 12

.. _max_cc_control_fan:

Contrôle des ventilateurs RGB
---------------------------------
La carte d’extension IO prend en charge jusqu’à deux ventilateurs 5V non-PWM, contrôlés simultanément.

.. note::

  Chaque modification de l’état de ``pironman5.service`` nécessite l'exécution de la commande suivante pour appliquer les changements :

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Utilisez la commande suivante pour configurer le mode de fonctionnement des ventilateurs RGB, selon la température de déclenchement souhaitée.

Par exemple, le mode **1 : Performance** active les ventilateurs à partir de 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet** : activation à 70°C  
* **3: Balanced** : activation à 67,5°C  
* **2: Cool** : activation à 60°C  
* **1: Performance** : activation à 50°C  
* **0: Always On** : les ventilateurs restent toujours allumés  

* Si la broche de contrôle des ventilateurs est connectée à une autre broche du Raspberry Pi, vous pouvez la modifier ainsi :

.. code-block:: shell

  sudo pironman5 -gp 18


Vérification de l’écran OLED
-----------------------------------

Une fois la bibliothèque ``pironman5`` installée, l’écran OLED affiche les informations CPU, RAM, utilisation du disque, température CPU et l’adresse IP du Raspberry Pi à chaque redémarrage.

Si l’écran OLED ne montre rien, vérifiez d’abord la connexion du câble FPC.

Vous pouvez ensuite consulter le journal du programme pour diagnostiquer le problème :

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

Ou vérifiez si l’adresse i2c 0x3C de l’écran OLED est détectée :

.. code-block:: shell

  i2cdetect -y 1

Vérification du récepteur infrarouge
---------------------------------------



* Installez le module ``lirc`` :

  .. code-block:: shell

    sudo apt-get install lirc -y

* Testez maintenant le récepteur IR en exécutant la commande suivante :

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Une fois la commande lancée, appuyez sur un bouton de la télécommande, et son code s'affichera à l'écran.

