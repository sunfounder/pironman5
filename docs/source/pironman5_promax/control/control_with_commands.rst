
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_view_control_commands:

Contrôle via Commandes
========================================
En plus de visualiser les données du Pironman 5 Pro MAX et de contrôler divers périphériques via le Tableau de Bord, vous pouvez également utiliser des commandes pour les contrôler.

Afficher les configurations de base
-----------------------------------

Le module ``pironman5`` offre des configurations de base pour Pironman, que vous pouvez consulter avec la commande suivante.

.. code-block:: shell

  sudo pironman5 -c

Les configurations standard apparaissent comme suit :

.. code-block::

  {
      "system": {
          "data_interval": 1,
          "enable_history": true,
          "rgb_color": "#ff3dbe",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 18,
          "temperature_unit": "C",
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "default_dashboard_page": "small",
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "debug_level": "INFO"
      }
  }

Personnalisez ces configurations selon vos besoins.

Utilisez ``pironman5`` ou ``pironman5 -h`` pour obtenir des instructions.

.. code-block::

  usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]]
                  [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-oe [OLED_ENABLE]]
                  [-or [{0,180}]] [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                  {start,stop,launch-browser} ...

  Interface de ligne de commande Pironman 5 Pro Max

  options:
    -h, --help            Affiche ce message d'aide et quitte
    -v, --version         Affiche la version
    -c, --config          Affiche la configuration
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Jours de conservation de la base de données
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
                          Couleur RGB au format hexadécimal sans # (par exemple 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          Luminosité RGB 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          Vitesse RGB 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          Nombre de LEDs RGB int
    -u, --temperature-unit [{C,F}]
                          Unité de température
    -oe, --oled-enable [OLED_ENABLE]
                          Activer OLED True/true/on/On/1 ou False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Définir la rotation de l'écran OLED, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          Pages OLED, séparées par ',' : mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          Délai de mise en veille de l'OLED en secondes

  Sous-commandes :
    {start,stop,launch-browser}
      start               Démarrer Pironman5
      stop                Arrêter Pironman5
      launch-browser      Lancer le navigateur

.. note::

  Chaque fois que vous modifiez l'état de ``pironman5.service``, vous devez utiliser la commande suivante pour que les modifications de configuration prennent effet.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Vérifiez l'état du programme ``pironman5`` en utilisant l'outil ``systemctl``.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternativement, inspectez les fichiers journaux générés par le programme.

  .. code-block:: shell

    ls /var/log/pironman5/

Contrôle des LEDs RGB
----------------------
La carte comporte 18 LEDs RGB adressables WS2812B : 6 sur la carte et 12 intégrées dans les Ventilateurs GPIO. Les utilisateurs peuvent contrôler l'alimentation, la couleur, la luminosité, les modes d'affichage, la vitesse d'animation et le nombre de LEDs actives.

.. note::

  Après avoir modifié la configuration de ``pironman5.service``, vous devez redémarrer le service pour que les modifications prennent effet :

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* **Activer/Désactiver les LEDs RGB** : Utilisez ``true`` pour allumer, ``false`` pour éteindre.

.. code-block:: shell

  sudo pironman5 -re true

* **Changer la couleur** : Définissez une couleur en utilisant une valeur hexadécimale (sans le `#`), par exemple ``fe1a1a`` pour le rouge.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* **Ajuster la luminosité** : Définissez la luminosité de 0% à 100%.

.. code-block:: shell

  sudo pironman5 -rb 75

* **Changer le mode d'affichage** : Choisissez parmi plusieurs modes d'animation :

  * ``solid`` : Couleur statique.
  * ``breathing`` : Atténuation progressive en pulsation.
  * ``flow`` / ``flow_reverse`` : Flux de couleur dans une direction.
  * ``rainbow`` / ``rainbow_reverse`` : Cycle à travers un spectre arc-en-ciel.
  * ``hue_cycle`` : Cycle fluide à travers les valeurs de teinte.

.. code-block:: shell

  sudo pironman5 -rs breathing

.. note::

  Lorsque vous utilisez les modes ``rainbow``, ``rainbow_reverse`` ou ``hue_cycle``, la couleur définie via ``pironman5 -rc`` sera remplacée par le cycle de couleurs automatique du mode.

* **Ajuster la vitesse d'animation** : Contrôlez la vitesse des effets de 0% (la plus lente) à 100% (la plus rapide).

.. code-block:: shell

  sudo pironman5 -rp 50

* **Définir le nombre de LEDs** : Le système contrôle par défaut 18 LEDs. Si vous avez étendu la chaîne avec des LEDs WS2812B externes supplémentaires, mettez à jour le nombre total en conséquence.

.. code-block:: shell

  sudo pironman5 -rl 12

Ventilateur
--------------------------------

Ces ventilateurs se connectent à un port dédié pour Ventilateur du CPU 4 broches sur le Raspberry Pi 5. Leur stratégie de contrôle par défaut est un schéma d'ajustement de vitesse intelligent à plusieurs niveaux géré par le firmware, basé sur la température du CPU. Cela signifie que lorsque vous utilisez un Ventilateur du CPU officiel ou compatible et que vous le connectez correctement, le système ajustera automatiquement la vitesse du ventilateur en fonction des changements de température du CPU (commençant à fonctionner au-dessus de 50°C) sans aucune intervention manuelle de votre part.

Vérifier l'écran OLED
-----------------------------------

L'écran OLED de 0,96" affiche les informations système (CPU, RAM, Disque, Température, IP) par défaut après l'installation de la bibliothèque ``pironman5`` et le redémarrage.

Si l'écran OLED est vide :

1. Assurez-vous que le câble FPC de l'OLED est solidement connecté à la carte mère.
2. Vérifiez les journaux de service pour détecter les erreurs :

    .. code-block:: shell

      sudo journalctl -u pironman5.service -f

    Ou vérifiez le journal spécifique de l'OLED :

    .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

3. Vérifiez que l'OLED est détectée sur le bus I2C (adresse `0x3C`) :

    .. code-block:: shell

      i2cdetect -y 1

**Commandes de configuration OLED**

* **Activer/Désactiver l'OLED** : Allumez ou éteignez l'écran OLED.

    .. code-block:: shell

      sudo pironman5 -oe false

* **Pivoter l'affichage** : Définissez l'orientation de l'écran à ``0`` (par défaut) ou ``180`` degrés.

    .. code-block:: shell

      sudo pironman5 -or 180

* **Configurer les pages d'affichage** : Choisissez les pages d'informations à parcourir. Les pages sont : ``mix`` (aperçu), ``performance`` (CPU/RAM détaillé), ``ips`` (IP réseau), ``disk`` (stockage). Séparez les pages multiples par des virgules.

    .. code-block:: shell

      sudo pironman5 -op mix,ips,disk

* **Définir le délai de mise en veille** : Définissez le nombre de secondes d'inactivité avant que l'OLED ne s'éteigne (0 = jamais en veille).

    .. code-block:: shell

      sudo pironman5 -os 120

Vérifier le récepteur infrarouge
---------------------------------------

Le récepteur IR intégré permet le contrôle via une télécommande.

1. Installez le logiciel requis :

    .. code-block:: shell

      sudo apt-get install lirc -y

2. Testez le récepteur. Exécutez la commande suivante, puis pointez une télécommande vers le boîtier et appuyez sur des boutons. Vous devriez voir une sortie de code brut.

    .. code-block:: shell

      mode2 -d /dev/lirc0

3. Pour configurer des mappages de boutons de télécommande spécifiques (par exemple, pour Kodi ou Volumio), vous devrez configurer le fichier `/etc/lirc/lircd.conf` avec les codes de votre télécommande.

Commandes système générales
----------------------------

* **Afficher la version** : Affiche la version du package ``pironman5`` installé.

.. code-block:: shell

  sudo pironman5 -v

* **Afficher la configuration actuelle** : Affiche tous les paramètres actuels.

.. code-block:: shell

  sudo pironman5 -c

* **Définir l'unité de température** : Basculer entre Celsius (``C``) et Fahrenheit (``F``) pour les affichages de température.

.. code-block:: shell

  sudo pironman5 -u F

* **Configurer la journalisation des données** :

  * **Définir les jours de conservation de la base de données** : Contrôle le nombre de jours de conservation des données historiques (comme les journaux de température).

    .. code-block:: shell

      sudo pironman5 -drd 30

  * **Activer/Désactiver la journalisation de l'historique** : Active ou désactive la collecte de données.

    .. code-block:: shell

      sudo pironman5 -eh false

* **Définir la verbosité de la journalisation** : Ajustez le niveau de détail des journaux système. Options : ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``.

.. code-block:: shell

  sudo pironman5 -dl DEBUG

* **Supprimer le tableau de bord web** : Désinstalle l'interface de gestion web optionnelle.

.. code-block:: shell

  sudo pironman5 -rd

* **Spécifier un chemin de configuration personnalisé** : Utilisez un fichier de configuration à partir d'un emplacement non standard.

.. code-block:: shell

  sudo pironman5 -cp /home/pi/my_custom_config.json

Sous-commandes de gestion des services
-------------------------------------------------------

* **Démarrer le service Pironman5** : Démarre manuellement le service d'arrière-plan qui gère les LEDs, le ventilateur, l'OLED, etc.

.. code-block:: shell

  sudo pironman5 start

* **Arrêter le service Pironman5** : Arrête proprement le service d'arrière-plan.

.. code-block:: shell

  sudo pironman5 stop

* **Lancer le tableau de bord web dans le navigateur** : Si le tableau de bord web est installé, cette commande l'ouvrira dans votre navigateur par défaut.

.. code-block:: shell

  sudo pironman5 launch-browser
