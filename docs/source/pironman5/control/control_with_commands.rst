.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _view_control_commands:

Steuerung mit Befehlen
========================================
Zusätzlich zur Anzeige von Daten des Pironman 5 und der Steuerung verschiedener Geräte über das Dashboard können Sie diese auch über Befehle steuern.

.. note::

  * Für das **Home Assistant**-System können Sie den Pironman 5 nur über das Dashboard überwachen und steuern, indem Sie die Webseite unter ``http://<ip>:34001`` öffnen.
  * Für das **Batocera.linux**-System können Sie den Pironman 5 nur über Befehle überwachen und steuern. Es ist wichtig zu beachten, dass alle Änderungen an der Konfiguration einen Neustart des Dienstes mit ``pironman5 restart`` erfordern, damit sie wirksam werden.


Anzeige der Grundkonfigurationen
-----------------------------------

Das ``pironman5``-Modul bietet Grundkonfigurationen für den Pironman, die Sie mit folgendem Befehl überprüfen können.

.. code-block:: shell

  pironman5 -c

Die Standardkonfigurationen werden wie folgt angezeigt:

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

Passen Sie diese Konfigurationen nach Ihren Bedürfnissen an.

Verwenden Sie ``pironman5`` oder ``pironman5 -h`` für Anweisungen.

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format with or without # (e.g. #FF0000 or 00aabb)
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

.. note::

  Jedes Mal, wenn Sie den Status von ``pironman5.service`` ändern, müssen Sie den folgenden Befehl verwenden, damit die Konfigurationsänderungen wirksam werden.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Überprüfen Sie den Status des ``pironman5``-Programms mit dem Tool ``systemctl``.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternativ können Sie die von dem Programm generierten Protokolldateien inspizieren.

  .. code-block:: shell

    cat /opt/pironman5/log


Steuerung der RGB-LEDs
---------------------------
Das Board verfügt über 4 WS2812 RGB-LEDs, die individuell gesteuert werden können. Benutzer können sie ein- oder ausschalten, die Farbe ändern, die Helligkeit anpassen, die Anzeigemodi wechseln und die Geschwindigkeit der Änderungen festlegen.
.. note::


  Jedes Mal, wenn Sie den Status von ``pironman5.service`` ändern, müssen Sie den folgenden Befehl verwenden, damit die Konfigurationsänderungen wirksam werden.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Um den Ein- und Ausschaltzustand der RGB-LEDs zu ändern, verwenden Sie ``true`` zum Einschalten und ``false`` zum Ausschalten.

.. code-block:: shell

  pironman5 -re true

* Um die Farbe zu ändern, geben Sie die gewünschte Hexadezimalfarbe ein, z.B. ``fe1a1a``.

.. code-block:: shell

  pironman5 -rc fe1a1a

* Um die Helligkeit der RGB-LEDs zu ändern (Bereich: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rb 100

* Um die RGB-LED-Anzeigemodi zu wechseln, wählen Sie aus den Optionen: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Wenn Sie den RGB-LED-Anzeigemodus auf ``rainbow``, ``rainbow_reverse`` oder ``hue_cycle`` setzen, können Sie die Farbe nicht mit ``pironman5 -rc`` einstellen.

.. code-block:: shell

  pironman5 -rs breathing

* Um die Geschwindigkeit der Änderungen anzupassen (Bereich: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rp 80

* Die Standardkonfiguration umfasst 4 RGB-LEDs. Schließen Sie zusätzliche LEDs an und aktualisieren Sie die Anzahl mit:

.. code-block:: shell

  pironman5 -rl 12

.. _cc_control_fan:

Steuerung der RGB-Lüfter
------------------------------
Das IO-Erweiterungsboard unterstützt bis zu zwei 5V Nicht-PWM-Lüfter. Beide Lüfter werden zusammen gesteuert. 

.. note::

  Jedes Mal, wenn Sie den Status von ``pironman5.service`` ändern, müssen Sie den folgenden Befehl verwenden, damit die Konfigurationsänderungen wirksam werden.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Sie können Befehle verwenden, um den Betriebsmodus der beiden RGB-Lüfter zu konfigurieren. Diese Modi bestimmen, unter welchen Bedingungen die RGB-Lüfter aktiviert werden. 

Wenn der Modus auf **1: Leistung** eingestellt ist, werden die RGB-Lüfter bei 50°C aktiviert.

.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Leise**: Die RGB-Lüfter werden bei 70°C aktiviert.
* **3: Ausgewogen**: Die RGB-Lüfter werden bei 67,5°C aktiviert.
* **2: Kühl**: Die RGB-Lüfter werden bei 60°C aktiviert.
* **1: Leistung**: Die RGB-Lüfter werden bei 50°C aktiviert.
* **0: Immer An**: Die RGB-Lüfter sind immer eingeschaltet.

* Wenn Sie den Steuerungspin des RGB-Lüfters auf verschiedene Pins des Raspberry Pi anschließen, können Sie den folgenden Befehl verwenden, um die Pinnummer zu ändern.

.. code-block:: shell

  sudo pironman5 -gp 18


Überprüfung des OLED-Bildschirms
-----------------------------------

Nachdem Sie die Bibliothek ``pironman5`` installiert haben, zeigt der OLED-Bildschirm die CPU-, RAM-, Festplattenauslastung, die CPU-Temperatur und die IP-Adresse des Raspberry Pi an und zeigt diese jedes Mal beim Neustart an.

Wenn Ihr OLED-Bildschirm keine Inhalte anzeigt, überprüfen Sie zunächst, ob das FPC-Kabel des OLED ordnungsgemäß angeschlossen ist.

Anschließend können Sie das Protokoll des Programms überprüfen, um zu sehen, was das Problem sein könnte, indem Sie den folgenden Befehl ausführen.

.. code-block:: shell

  cat /var/log/pironman5/

Oder überprüfen Sie, ob die i2c-Adresse des OLED 0x3C erkannt wird:

.. code-block:: shell

  i2cdetect -y 1

Überprüfung des Infrarot-Empfängers
---------------------------------------


* Installieren Sie das Modul ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Testen Sie nun den IR-Empfänger, indem Sie den folgenden Befehl ausführen. 

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Nach Ausführung des Befehls drücken Sie eine Taste auf der Fernbedienung und der Code dieser Taste wird angezeigt.
