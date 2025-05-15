.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 – gemeinsam mit Gleichgesinnten.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um deine Kenntnisse auszubauen.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produkten und erhalte exklusive Einblicke.
    - **Spezielle Rabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an Gewinnspielen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _view_control_commands_mini:

Steuerung per Befehle
========================================
Neben der grafischen Steuerung des Pironman 5 Mini über das Dashboard kannst du auch direkt per Kommandozeile auf die Funktionen zugreifen.

.. note::

  * Beim Einsatz mit **Home Assistant** erfolgt die Steuerung ausschließlich über das Dashboard unter ``http://<ip>:34001``.
  * Beachte: Änderungen an der Konfiguration werden erst nach einem Neustart des Dienstes mit ``pironman5 restart`` wirksam.

Grundkonfiguration anzeigen
-----------------------------------

Das Modul ``pironman5`` bietet grundlegende Konfigurationen, die du mit folgendem Befehl einsehen kannst:

.. code-block:: shell

  pironman5 -c

Die Standardkonfiguration sieht wie folgt aus:

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

Diese Einstellungen kannst du nach deinen Anforderungen anpassen.

Rufe ``pironman5`` oder ``pironman5 -h`` auf, um die Optionen einzusehen.

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]]
                                [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]]
                                [--background [BACKGROUND]]
                                [{start,restart,stop}]

  Pironman5 Mini

  ositional arguments:
   {start,restart,stop}  Command

  ptions:
   -h, --help            show this help message and exit
   -v, --version         Show version
   -c, --config          Show config
   -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                         Debug level
   -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                         RGB color in hex format without # (e.g. 00aabb)
   -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                         RGB brightness 0-100
   -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                         RGB style
   -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                         RGB speed 0-100
   -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                         RGB enable True/False
   -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                         RGB LED count int
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
   --background [BACKGROUND]
                         Run in background
.. note::

  Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, muss der Dienst mit folgendem Befehl neu gestartet werden:

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Überprüfe den Status von ``pironman5`` mit ``systemctl``:

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Oder sieh dir die Protokolle an:

  .. code-block:: shell

    ls /var/log/pironman5/
    cat /var/log/pironman5/main.log

RGB-LEDs steuern
----------------------
Das Board verfügt über vier WS2812-RGB-LEDs, die sich flexibel anpassen lassen. Du kannst sie ein- oder ausschalten, Farben ändern, Helligkeit regeln, Anzeigemodi wählen und die Wechselgeschwindigkeit einstellen.

.. note::

  Konfigurationsänderungen werden erst nach Neustart des Dienstes wirksam: ``pironman5.service``

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Zum Ein- oder Ausschalten der RGB-LEDs – ``true`` für AN, ``false`` für AUS:

.. code-block:: shell

  pironman5 -re true

* Zur Änderung der Farbe im Hex-Format, z. B. ``fe1a1a``:

.. code-block:: shell

  pironman5 -rc fe1a1a

* Zur Einstellung der Helligkeit (0–100 %):

.. code-block:: shell

  pironman5 -rb 100

* Zur Auswahl des Anzeigemodus: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``

.. note::

  Bei Auswahl von ``rainbow``, ``rainbow_reverse`` oder ``hue_cycle`` kann die Farbe nicht manuell gesetzt werden.

.. code-block:: shell

  pironman5 -rs breathing

* Zur Einstellung der Wechselgeschwindigkeit (0–100 %):

.. code-block:: shell

  pironman5 -rp 80

* Standardmäßig sind 4 RGB-LEDs konfiguriert. Wenn du weitere anschließt, aktualisiere die Anzahl:

.. code-block:: shell

  pironman5 -rl 12

.. _cc_control_fan_mini:

RGB-Lüfter steuern
---------------------
Die IO-Erweiterungsplatine unterstützt einen 5V-Lüfter ohne PWM.

.. note::

  Änderungen am Lüfterbetrieb erfordern ebenfalls einen Dienstneustart: ``pironman5.service``

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Du kannst den Modus des RGB-Lüfters mit folgendem Befehl setzen – er bestimmt, ab welcher Temperatur der Lüfter startet.

Zum Beispiel: Modus **1: Performance** aktiviert den Lüfter bei 50 °C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Leise** – Aktiv bei 70 °C  
* **3: Ausgewogen** – Aktiv bei 67,5 °C  
* **2: Kühl** – Aktiv bei 60 °C  
* **1: Performance** – Aktiv bei 50 °C  
* **0: Immer an** – Lüfter läuft permanent

* Falls du den Steuerpin des RGB-Lüfters an einen anderen GPIO anschließt, kannst du diesen wie folgt anpassen:

.. code-block:: shell

  sudo pironman5 -gp 18
