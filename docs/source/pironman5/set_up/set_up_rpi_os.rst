.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




Konfiguration unter Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
==================================================================

.. image:: ../img/pironman5_pic.jpg
    :width: 400
    :align: center


Wenn du Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf deinem Raspberry Pi installiert hast, musst du den Pironman 5 über die Befehlszeile konfigurieren.

.. note::

  Bevor du mit der Konfiguration fortfährst, musst du deinen Raspberry Pi starten und dich anmelden.
  Wenn du dir nicht sicher bist, wie du dich anmeldest, kannst du die offizielle Website von Raspberry Pi besuchen: |link_rpi_get_start|.


.. _safe_shutdown_5:

1. Konfiguration des Herunterfahrens zur Deaktivierung der GPIO-Stromversorgung
--------------------------------------------------------------------------------

Um zu verhindern, dass der OLED-Bildschirm und die GPIO-Lüfter, die vom GPIO des Raspberry Pi mit Strom versorgt werden, nach dem Herunterfahren aktiv bleiben, muss der Raspberry Pi für die Deaktivierung der GPIO-Stromversorgung konfiguriert werden.

#. Öffne das EEPROM-Konfigurationstool:

   .. code-block::

      sudo raspi-config

#. Navigiere zu **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Wähle **B1 Full Power Off...**.

   .. image:: img/run_power_off.png

#. Speichere die Änderungen. Du wirst aufgefordert, einen Neustart durchzuführen, damit die neuen Einstellungen wirksam werden.


.. _install_pironman5_module_5:

2. Installation des Moduls ``pironman5``
----------------------------------------

.. note::

   Für Raspberry Pi OS Lite-Systeme installiere zunächst die erforderlichen Werkzeuge wie ``git`` und ``python3``.

   .. code-block:: shell

      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Lade das Modul ``pironman5`` von GitHub herunter und installiere es.

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

   .. note::

      Wenn du die Pironman-5-Serie zusammen mit PiPower 5 verwendest, führe stattdessen den folgenden Befehl aus:

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --pipower5

#. Nach dem Ausführen des Installationsprogramms wähle dein Pironman-5-Modell (1~4).

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. Sobald die Installation abgeschlossen ist, starte den Raspberry Pi wie aufgefordert neu. Der erste Start kann bis zu 30 Sekunden dauern, während die Dienste initialisiert werden.

#. Nachdem Pironman 5 erfolgreich gestartet ist, überprüfe, ob die folgenden Komponenten ordnungsgemäß funktionieren.

   * **OLED-Bildschirm**

     * Zeigt CPU-Auslastung, RAM-Auslastung, CPU-Temperatur und IP-Adresse an.
     * Schaltet sich nach 10 Sekunden automatisch aus.
     * Drücke kurz den Netzschalter, um den Bildschirm zu aktivieren oder die Seiten zu wechseln.

   * **Netzschalter**

     * Kurz drücken: Einschalten / OLED aufwecken / OLED-Seite wechseln.
     * 2 Sekunden gedrückt halten: Sicheres Herunterfahren (erfordert :ref:`safe_shutdown_5`).
     * 5 Sekunden gedrückt halten: Erzwungenes Herunterfahren.

   * **WS2812 RGB-LEDs**

     * Leuchten blau mit einem Atmungseffekt.

   * **Zwei GPIO-Lüfter**

     * Standardmäßig auf **Always On** (immer eingeschaltet) eingestellt.
     * Der Arbeitsmodus kann über Befehle oder das Dashboard geändert werden.


   * **CPU-Lüfter (Tower-Cooler-Lüfter)**

     * Passt die Geschwindigkeit automatisch an die CPU-Temperatur an.
     * Standard-Lüfterkennlinie:

       * < 50 °C: Aus (0 %)
       * 50 °C+: Niedrig (30 %)
       * 60 °C+: Mittel (50 %)
       * 67,5 °C+: Hoch (70 %)
       * 75 °C+: Volle Geschwindigkeit (100 %)

#. Verwende ``systemctl``, um den ``pironman5.service`` zu verwalten.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Ersetze ``restart`` je nach Bedarf durch ``start``, ``stop`` oder ``status``, um den Dienst zu verwalten.

.. note::

   Pironman 5 ist jetzt einsatzbereit.

   Für erweiterte Steuerungen und Dashboard-Funktionen siehe :ref:`control_commands_dashboard_5`.