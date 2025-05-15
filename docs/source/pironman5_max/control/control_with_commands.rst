.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_view_control_commands:

Steuerung mit Befehlen
========================================
Neben der Anzeige von Daten des Pironman 5 und der Steuerung verschiedener Geräte über das Dashboard, kannst du diese auch über Befehle steuern.

.. note::

  * Beim **Home Assistant**-System kannst du den Pironman 5 nur über das Dashboard überwachen und steuern, indem du die Webseite unter ``http://<ip>:34001`` öffnest.
  * Beim **Batocera.linux**-System kannst du den Pironman 5 nur über Befehle überwachen und steuern. Es ist wichtig zu beachten, dass Änderungen an der Konfiguration einen Neustart des Dienstes mit ``pironman5 restart`` erfordern, damit sie wirksam werden.

Anzeige der Basiskonfigurationen
-----------------------------------

Das ``pironman5``-Modul bietet grundlegende Konfigurationen für Pironman, die du mit folgendem Befehl anzeigen kannst.

.. code-block:: shell

  pironman5 -c

Die Standardkonfigurationen erscheinen wie folgt:

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

Passe diese Konfigurationen nach deinen Bedürfnissen an.

Verwende ``pironman5`` oder ``pironman5 -h`` für Anweisungen.

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

  Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den folgenden Befehl verwenden, um die Konfigurationsänderungen wirksam zu machen.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Überprüfe den Status des ``pironman5``-Programms mit dem ``systemctl``-Tool.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternativ kannst du die vom Programm generierten Log-Dateien einsehen.

  .. code-block:: shell

    ls /var/log/pironman5/


Steuerung der RGB-LEDs
-------------------------

Das Board verfügt über 4 WS2812 RGB-LEDs, die eine anpassbare Steuerung bieten. Benutzer können sie ein- oder ausschalten, die Farbe ändern, die Helligkeit anpassen, die RGB-LED-Anzeigemodi wechseln und die Geschwindigkeit der Änderungen festlegen.

.. note::

  Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den folgenden Befehl verwenden, um die Konfigurationsänderungen wirksam zu machen.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Um den Ein- und Aus-Zustand der RGB-LEDs zu ändern, verwende ``true``, um die RGB-LEDs einzuschalten, und ``false``, um sie auszuschalten.

.. code-block:: shell

  pironman5 -re true

* Um die Farbe zu ändern, gib die gewünschten hexadezimalen Farbwerte ein, wie z.B. ``fe1a1a``.

.. code-block:: shell

  pironman5 -rc fe1a1a

* Um die Helligkeit der RGB-LED zu ändern (Bereich: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rb 100

* Um die Anzeigemodi der RGB-LED zu wechseln, wähle aus den Optionen: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Wenn du den RGB-LED-Anzeigemodus auf ``rainbow``, ``rainbow_reverse`` oder ``hue_cycle`` einstellst, kannst du die Farbe nicht mit ``pironman5 -rc`` festlegen.

.. code-block:: shell

  pironman5 -rs breathing

* Um die Geschwindigkeit der Änderungen zu ändern (Bereich: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rp 80

* Die Standardkonfiguration umfasst 4 RGB-LEDs. Schließe zusätzliche LEDs an und aktualisiere die Anzahl mit:

.. code-block:: shell

  pironman5 -rl 12

.. _max_cc_control_fan:

Steuerung der RGB-Lüfter
---------------------------

Das IO-Erweiterungsboard unterstützt bis zu zwei 5V-Nicht-PWM-Lüfter. Beide Lüfter werden gemeinsam gesteuert.

.. note::

  Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den folgenden Befehl verwenden, um die Konfigurationsänderungen wirksam zu machen.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Du kannst den Betriebmodus der beiden RGB-Lüfter über einen Befehl konfigurieren. Diese Modi bestimmen, unter welchen Bedingungen die RGB-Lüfter aktiviert werden.

Zum Beispiel, wenn auf **1: Performance**-Modus eingestellt, werden die RGB-Lüfter bei 50°C aktiviert.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: Die RGB-Lüfter werden bei 70°C aktiviert.
* **3: Balanced**: Die RGB-Lüfter werden bei 67,5°C aktiviert.
* **2: Cool**: Die RGB-Lüfter werden bei 60°C aktiviert.
* **1: Performance**: Die RGB-Lüfter werden bei 50°C aktiviert.
* **0: Always On**: Die RGB-Lüfter sind immer eingeschaltet.

* Wenn du den Steuerpin des RGB-Lüfters an verschiedene Pins des Raspberry Pi anschließt, kannst du den folgenden Befehl verwenden, um die Pin-Nummer zu ändern.

.. code-block:: shell

  sudo pironman5 -gp 18


Überprüfung des OLED-Bildschirms
-----------------------------------

Nachdem du die ``pironman5``-Bibliothek installiert hast, zeigt der OLED-Bildschirm die CPU-Auslastung, RAM, Festplattennutzung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an und zeigt diese Informationen bei jedem Neustart an.

Wenn dein OLED-Bildschirm keine Inhalte anzeigt, überprüfe zunächst, ob das FPC-Kabel des OLED richtig angeschlossen ist.

Danach kannst du das Programmlog überprüfen, um zu sehen, was das Problem sein könnte, mit folgendem Befehl.

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

Oder überprüfe, ob die i2c-Adresse 0x3C des OLED erkannt wird:

.. code-block:: shell

  i2cdetect -y 1

Überprüfung des Infrarot-Empfängers
---------------------------------------



* Installiere das ``lirc``-Modul:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Teste nun den IR-Empfänger, indem du den folgenden Befehl ausführst.

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Nachdem du den Befehl ausgeführt hast, drücke eine Taste auf der Fernbedienung, und der Code dieser Taste wird angezeigt.

