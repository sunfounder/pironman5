
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Expanseur d'E/S
================

.. image:: img/io_board.png


LEDs RGB
------------

.. image:: img/io_board_rgb.png

La carte comporte 18 LEDs RGB adressables WS2812B : 6 sur la carte et 12 intégrées dans les Ventilateurs GPIO, offrant un contrôle personnalisable. Les utilisateurs peuvent les allumer ou les éteindre, changer la couleur, ajuster la luminosité, changer les modes d'affichage et régler la vitesse des changements.

Broche de contrôle RGB
-------------------------

La LED RGB est pilotée par SPI et connectée à **GPIO10**, qui est également la broche SPI MOSI. Les deux broches indiquées sont utilisées pour connecter la LED RGB à GPIO10. Si non nécessaire, le cavalier peut être retiré.

  .. image:: img/io_board_rgb_pin.png

Broches RGB OUT
-------------------------

.. image:: img/io_board_rgb_out.png

Les LEDs RGB WS2812 prennent en charge la connexion en série, permettant l'ajout d'une bande LED RGB externe. Connectez la broche **SIG** à la broche **DIN** de la bande externe pour l'extension.

La carte comporte 18 LEDs RGB adressables WS2812B : 6 sur la carte et 12 intégrées dans les Ventilateurs GPIO. Connectez des LEDs supplémentaires et mettez à jour le nombre en utilisant :

.. code-block:: shell

  sudo pironman5 --rgb-led-count [quantité]

Exemple :

.. code-block:: shell

  sudo pironman5 --rgb-led-count 24

Connecteur de l'écran OLED
----------------------------

Le connecteur de l'écran OLED, avec une adresse 0x3C, est une caractéristique clé.

.. image:: img/io_board_oled.png

Si l'écran OLED n'affiche rien ou affiche incorrectement, vous pouvez suivre ces étapes pour résoudre le problème :

Vérifiez si le câble FPC de l'écran OLED est correctement connecté.

#. Utilisez la commande suivante pour visualiser les journaux d'exécution du programme et vérifier les messages d'erreur.

    .. code-block:: shell

        cat /var/log/pironman5/pironman5.log

#. Alternativement, utilisez la commande suivante pour vérifier si l'adresse i2c 0x3C de l'OLED est reconnue :

    .. code-block:: shell

        sudo i2cdetect -y 1

#. Si les deux premières étapes ne révèlent aucun problème, essayez de redémarrer le service pironman5 pour voir si cela résout le problème.

    .. code-block:: shell

        sudo systemctl restart pironman5.service

Récepteur infrarouge
---------------------------

.. image:: img/io_board_receiver.png

* **Modèle** : IRM-56384, fonctionnant à 38KHz.
* **Connexion** : Le récepteur IR se connecte à **GPIO13**.
* **D7** : Un indicateur de réception infrarouge qui clignote lors de la détection d'un signal.
* **J6** : Une broche pour activer la fonction infrarouge. Par défaut, un cavalier est inséré pour une fonctionnalité immédiate. Retirez le cavalier pour libérer GPIO13 si le récepteur IR n'est pas utilisé.

Pour utiliser le récepteur IR, vérifiez sa connexion et installez le module nécessaire :

* Testez la connexion :

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Installez le module ``lirc`` :

  .. code-block:: shell

    sudo apt-get install lirc -y

* Maintenant, testez le récepteur IR en exécutant la commande suivante.

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Après avoir exécuté la commande, appuyez sur un bouton de la télécommande, et le code de ce bouton sera affiché.

Broches des Ventilateurs GPIO
------------------------------------------------

.. image:: img/io_board_pin_fan.png

La carte d'expansion E/S prend en charge jusqu'à trois Ventilateurs du CPU 5V. Tous les ventilateurs sont contrôlés ensemble.

Le signal de commande des ventilateurs est connecté au port **FAN IN** sur la carte d'expansion E/S, puis sorti par les trois ports de ventilateur dédiés. Ces ports sont numérotés de haut en bas comme **REAR UPPER**, **REAR LOWER** et **CPU FAN**. Veuillez les connecter conformément à la sérigraphie, sinon cela affectera le contrôle RGB sur le ventilateur.

En-têtes de broches
----------------------------------------

.. image:: img/io_board_pin_header.png

Deux connecteurs d'en-tête à angle droit étendent les GPIO du Raspberry Pi, mais notez que le récepteur IR, la LED RGB et le ventilateur occupent certaines broches. Retirez les cavaliers correspondants pour utiliser ces broches pour d'autres fonctions.

.. list-table::
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 MAX
    - Raspberry Pi 5
  * - Récepteur IR (Optionnel)
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - Ventilateur (Optionnel)
    - GPIO6
  * - FLED (Optionnel)
    - GPIO5
  * - RGB (Optionnel)
    - GPIO10
