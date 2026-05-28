.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _max_view_control_commands:

Steuerung mit Befehlen
========================================
Neben der Anzeige von Daten des Pironman 5 MAX und der Steuerung verschiedener Gerate uber das Dashboard kannst du diese auch uber Befehle steuern.

.. note::

  * Beim **Home Assistant**-System kannst du den Pironman 5 MAX nur uber das Dashboard uberwachen und steuern, indem du die Webseite unter ``http://<ip>:34001`` offnest.

.. * Beim **Batocera.linux**-System kannst du den Pironman 5 MAX nur uber Befehle uberwachen und steuern. Es ist wichtig zu beachten, dass Anderungen an der Konfiguration einen Neustart des Dienstes mit ``pironman5 restart`` erfordern, damit sie wirksam werden.

Anzeige der Basiskonfigurationen
-----------------------------------

Das ``pironman5``-Modul bietet grundlegende Konfigurationen fur Pironman, die du mit folgendem Befehl anzeigen kannst.

.. code-block:: shell

  sudo pironman5 -c

Die Standardkonfigurationen erscheinen wie folgt:

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
          "gpio_fan_led_pin": 0,
          "gpio_fan_led_state": "follow",
          "debug_level": "INFO"
      }
  }

Passe diese Konfigurationen nach deinen Bedurfnissen an.

Verwende ``pironman5`` oder ``pironman5 -h`` fur Anweisungen.

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl [{debug,info,warning,error,critical}]] [--background [BACKGROUND]] [-rd] [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-od [OLED_DISK]] [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]]
                          [{start,restart,stop}]

  Pironman 5 MAX command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Database retention days
    -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                          Debug level
    -rd, --remove-dashboard
                          Remove dashboard
    -cp, --config-path [CONFIG_PATH]
                          Config path
    -eh, --enable-history [ENABLE_HISTORY]
                          Enable history, True/true/on/On/1 or False/false/off/Off/0
    -re, --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rs, --rgb-style [RGB_STYLE]
                          RGB style: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
    -rc, --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u, --temperature-unit [{C,F}]
                          Temperature unit
    -gm, --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp, --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -fl, --gpio-fan-led [GPIO_FAN_LED]
                          GPIO fan LED state on/off/follow
    -fp, --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                          GPIO fan LED pin
    -oe, --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          OLED pages, split by ',': mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds

  Subcommands:
    {start,stop,launch-browser}
      start               Start Pironman5
      stop                Stop Pironman5
      launch-browser      Launch browser

.. note::

   Jedes Mal, wenn du den Status von ``pironman5.service`` anderst, musst du den Dienst neu starten, damit die Konfigurationsanderungen wirksam werden.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Uberprufe den Status des ``pironman5``-Programms mit dem ``systemctl``-Tool.

  .. code-block:: shell

     sudo systemctl status pironman5.service

* Alternativ kannst du die vom Programm generierten Log-Dateien einsehen.

  .. code-block:: shell

     cat /var/log/pironman5/pironman5.log


Steuerung der RGB-LEDs
-------------------------

Das Board verfugt uber 4 WS2812 RGB-LEDs, die eine anpassbare Steuerung bieten. Du kannst sie ein- oder ausschalten, die Farbe andern, die Helligkeit anpassen, die Anzeigemodi wechseln und die Geschwindigkeit der Anderungen festlegen.

.. note::

   Jedes Mal, wenn du den Status von ``pironman5.service`` anderst, musst du den Dienst neu starten, damit die Konfigurationsanderungen wirksam werden.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Um den Ein- und Aus-Zustand der RGB-LEDs zu andern, verwende ``true``, um die RGB-LEDs einzuschalten, und ``false``, um sie auszuschalten.

  .. code-block:: shell

     sudo pironman5 -re true

* Um die Farbe zu andern, gib die gewunschten hexadezimalen Farbwerte ein, wie z.B. ``fe1a1a``.

  .. code-block:: shell

     sudo pironman5 -rc fe1a1a

* Um die Helligkeit der RGB-LED zu andern (Bereich: ``0 ~ 100``):

  .. code-block:: shell

     sudo pironman5 -rb 100

* Um die Anzeigemodi der RGB-LED zu wechseln, wahle aus:

  ``solid`` / ``breathing`` / ``flow`` / ``flow_reverse`` / ``rainbow`` / ``rainbow_reverse`` / ``hue_cycle``

  .. note::

     Wenn der RGB-LED-Anzeigemodus auf ``rainbow``, ``rainbow_reverse`` oder ``hue_cycle`` eingestellt ist, wird die Farbeinstellung mit ``pironman5 -rc`` nicht wirksam.

  .. code-block:: shell

     sudo pironman5 -rs breathing

* Um die Geschwindigkeit der Anderungen zu andern (Bereich: ``0 ~ 100``):

  .. code-block:: shell

     sudo pironman5 -rp 80

* Die Standardkonfiguration umfasst 4 RGB-LEDs. Schliee zusatzliche LEDs an und aktualisiere die Anzahl mit:

  .. code-block:: shell

     sudo pironman5 -rl 12


.. _cc_control_fan_max:

Steuerung der GPIO-Lufter
---------------------------

Das IO-Erweiterungsboard unterstutzt bis zu zwei 5V-Nicht-CPU-Lufter. Beide Lufter werden gemeinsam gesteuert.

.. note::

   Jedes Mal, wenn du den Status von ``pironman5.service`` anderst, musst du den Dienst neu starten, damit die Konfigurationsanderungen wirksam werden.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Du kannst den Betriebsmodus der beiden GPIO-Lufter uber einen Befehl konfigurieren. Diese Modi bestimmen die Temperaturschwelle, bei der die GPIO-Lufter aktiviert werden.

  Wenn der Modus auf **1: Performance** eingestellt ist, werden die GPIO-Lufter bei ``50 °C`` aktiviert.

  .. code-block:: shell

     sudo pironman5 -gm 3

* **4: Quiet**: Die GPIO-Lufter werden bei ``70 °C`` aktiviert.
* **3: Balanced**: Die GPIO-Lufter werden bei ``67,5 °C`` aktiviert.
* **2: Cool**: Die GPIO-Lufter werden bei ``60 °C`` aktiviert.
* **1: Performance**: Die GPIO-Lufter werden bei ``50 °C`` aktiviert.
* **0: Always On**: Die GPIO-Lufter sind immer eingeschaltet.

* Wenn du den Steuerpin des Lufters an verschiedene Pins des Raspberry Pi anschlie't, kannst du den folgenden Befehl verwenden, um die Pin-Nummer zu andern.

  .. code-block:: shell

     sudo pironman5 -gp 18

* Um den LED-Modus der GPIO-Lufter zu konfigurieren:

  .. code-block:: shell

     sudo pironman5 -fl follow

  Mogliche Werte: ``on``, ``off``, ``follow``.


Uber den CPU-Lufter
------------------------

Der CPU-Lufter wird an einen dedizierten 4-Pin-PWM-Lufteranschluss auf dem Raspberry Pi 5 angeschlossen.

Die standardmaige Steuerungsstrategie ist ein firmwaregesteuertes, mehrstufiges intelligentes Drehzahlanpassungssystem, das auf der CPU-Temperatur basiert. Wenn du einen offiziellen oder kompatiblen PWM-Lufter verwendest und ihn korrekt anschlie't, passt das System die Luftergeschwindigkeit automatisch an die Anderungen der CPU-Temperatur an (ab ``50 °C``), ohne dass ein manueller Eingriff erforderlich ist.


Uberprufung des OLED-Bildschirms
-----------------------------------

Nachdem du die ``pironman5``-Bibliothek installiert hast, zeigt der OLED-Bildschirm nach jedem Neustart automatisch CPU-Auslastung, RAM-Auslastung, Festplattennutzung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.

Wenn dein OLED-Bildschirm keine Inhalte anzeigt, uberprufe zunachst, ob das FPC-Kabel des OLED richtig angeschlossen ist.

Uberprufe dann das Programmprotokoll mit dem folgenden Befehl:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

Du kannst auch uberprufen, ob die I2C-Adresse ``0x3C`` des OLED erkannt wird:

.. code-block:: shell

   i2cdetect -y 1


Uberprufung des Infrarot-Empfangers
---------------------------------------

* Installiere das ``lirc``-Modul:

  .. code-block:: shell

     sudo apt-get install lirc -y

* Teste den IR-Empfanger mit dem folgenden Befehl:

  .. code-block:: shell

     mode2 -d /dev/lirc0

* Nachdem du den Befehl ausgefuhrt hast, drucke eine Taste auf der Fernbedienung. Der entsprechende IR-Code wird im Terminal angezeigt.