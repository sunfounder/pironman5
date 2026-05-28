.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_commands_5:

Steuerung mit Befehlen
========================================
Zusätzlich zur Anzeige von Daten des Pironman 5 und der Steuerung verschiedener Geräte über das Dashboard kannst du auch Befehle zur Steuerung verwenden.

.. note::

  * Für das **Home Assistant**-System kannst du den Pironman 5 nur über das Dashboard überwachen und steuern, indem du die Webseite unter ``http://<ip>:34001`` öffnest.

.. * Für das **Batocera.linux**-System kannst du den Pironman 5 nur über Befehle überwachen und steuern. Es ist wichtig zu beachten, dass alle Änderungen an der Konfiguration einen Neustart des Dienstes mit ``pironman5 restart`` erfordern, damit sie wirksam werden.


Anzeige der Grundkonfigurationen
-----------------------------------

Das ``pironman5``-Modul bietet Grundkonfigurationen für den Pironman, die du mit folgendem Befehl überprüfen kannst.

.. code-block:: shell

  sudo pironman5 -c

Die Standardkonfigurationen werden wie folgt angezeigt:

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
          "debug_level": "INFO"
      }
  }

Passe diese Konfigurationen nach deinen Bedürfnissen an.

Verwende ``pironman5`` oder ``pironman5 -h`` für Anweisungen.

.. code-block::


  usage: pironman5-service [-h] [-v] [-c] [-dl [{debug,info,warning,error,critical}]] [--background [BACKGROUND]] [-rd] [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-oe [OLED_ENABLE]]
                          [-od [OLED_DISK]] [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]]
                          [{start,restart,stop}]

  Pironman 5 command line interface

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

   Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den Dienst neu starten, damit die Konfigurationsänderungen wirksam werden.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Überprüfe den Status des ``pironman5``-Programms mit dem Tool ``systemctl``.

  .. code-block:: shell

     sudo systemctl status pironman5.service

* Alternativ kannst du die vom Programm generierten Protokolldateien einsehen.

  .. code-block:: shell

     cat /var/log/pironman5/pironman5.log


Steuerung der RGB-LEDs
-----------------------

Das Board verfügt über 4 WS2812 RGB-LEDs, die individuell gesteuert werden können. Du kannst sie ein- oder ausschalten, die Farbe ändern, die Helligkeit anpassen, die Anzeigemodi wechseln und die Geschwindigkeit der Änderungen festlegen.

.. note::

   Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den Dienst neu starten, damit die Konfigurationsänderungen wirksam werden.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Um den Ein- und Ausschaltzustand der RGB-LEDs zu ändern, verwende ``true`` zum Einschalten oder ``false`` zum Ausschalten.

  .. code-block:: shell

     sudo pironman5 -re true

* Um die Farbe der RGB-LEDs zu ändern, gib den gewünschten Hexadezimalfarbwert ein, z. B. ``fe1a1a``.

  .. code-block:: shell

     sudo pironman5 -rc fe1a1a

* Um die Helligkeit der RGB-LEDs zu ändern (Bereich: ``0 ~ 100``):

  .. code-block:: shell

     sudo pironman5 -rb 100

* Um die RGB-LED-Anzeigemodi zu wechseln, wähle aus:

  ``solid`` / ``breathing`` / ``flow`` / ``flow_reverse`` / ``rainbow`` / ``rainbow_reverse`` / ``hue_cycle``

  .. note::

     Wenn der RGB-LED-Anzeigemodus auf ``rainbow``, ``rainbow_reverse`` oder ``hue_cycle`` eingestellt ist, wird die Farbeinstellung mit ``pironman5 -rc`` nicht wirksam.

  .. code-block:: shell

     sudo pironman5 -rs breathing

* Um die Animationsgeschwindigkeit der RGB-LEDs zu ändern (Bereich: ``0 ~ 100``):

  .. code-block:: shell

     sudo pironman5 -rp 80

* Die Standardkonfiguration umfasst 4 RGB-LEDs. Wenn du zusätzliche LEDs anschließt, aktualisiere die Anzahl mit:

  .. code-block:: shell

     sudo pironman5 -rl 12


.. _cc_control_fan:

Steuerung der GPIO-Lüfter
-------------------------

Das IO-Erweiterungsboard unterstützt bis zu zwei 5V Nicht-CPU-Lüfter. Beide Lüfter werden zusammen gesteuert.

.. note::

   Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den Dienst neu starten, damit die Konfigurationsänderungen wirksam werden.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Du kannst Befehle verwenden, um den Betriebsmodus der beiden GPIO-Lüfter zu konfigurieren. Diese Modi bestimmen die Temperaturschwelle, bei der die GPIO-Lüfter aktiviert werden.

  Wenn der Modus auf **1: Performance** eingestellt ist, werden die GPIO-Lüfter bei ``50 °C`` aktiviert.

  .. code-block:: shell

     sudo pironman5 -gm 3

* **4: Quiet**: Die GPIO-Lüfter werden bei ``70 °C`` aktiviert.
* **3: Balanced**: Die GPIO-Lüfter werden bei ``67,5 °C`` aktiviert.
* **2: Cool**: Die GPIO-Lüfter werden bei ``60 °C`` aktiviert.
* **1: Performance**: Die GPIO-Lüfter werden bei ``50 °C`` aktiviert.
* **0: Always On**: Die GPIO-Lüfter sind immer eingeschaltet.

* Wenn du den Steuerpin des RGB-Lüfters an einen anderen GPIO-Pin des Raspberry Pi anschließt, kannst du die Pinnummer wie folgt ändern:

  .. code-block:: shell

     sudo pironman5 -gp 18


Über den CPU-Lüfter
------------------------

Der CPU-Lüfter wird an einen dedizierten 4-Pin-CPU-Lüfteranschluss auf dem Raspberry Pi 5 angeschlossen.

Die standardmäßige Steuerungsstrategie ist ein firmwaregesteuertes, mehrstufiges intelligentes Drehzahlanpassungssystem, das auf der CPU-Temperatur basiert. Wenn du einen offiziellen oder kompatiblen CPU-Lüfter verwendest und ihn korrekt anschließt, passt das System die Lüftergeschwindigkeit automatisch an die Änderungen der CPU-Temperatur an (ab ``50 °C``), ohne dass ein manueller Eingriff erforderlich ist.


Überprüfung des OLED-Bildschirms
-----------------------------------

Wenn die Bibliothek ``pironman5`` installiert ist, zeigt der OLED-Bildschirm nach jedem Neustart automatisch CPU-Auslastung, RAM-Auslastung, Festplattenauslastung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.

Wenn der OLED-Bildschirm keine Inhalte anzeigt, überprüfe zunächst, ob das OLED-FPC-Kabel ordnungsgemäß angeschlossen ist.

Überprüfe dann das Programmprotokoll mit dem folgenden Befehl:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

Du kannst auch überprüfen, ob die OLED-I2C-Adresse ``0x3C`` erkannt wird:

.. code-block:: shell

   i2cdetect -y 1


Überprüfung des Infrarot-Empfängers
---------------------------------------

* Installiere das Modul ``lirc``:

  .. code-block:: shell

     sudo apt-get install lirc -y

* Teste den IR-Empfänger mit dem folgenden Befehl:

  .. code-block:: shell

     mode2 -d /dev/lirc0

* Nachdem du den Befehl ausgeführt hast, drücke eine Taste auf der Fernbedienung. Der entsprechende IR-Code wird im Terminal angezeigt.