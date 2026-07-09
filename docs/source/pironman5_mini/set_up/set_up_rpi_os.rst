.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Konfiguration unter Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

.. image:: ../img/pironman5_mini_pic.jpg
    :width: 400
    :align: center

Wenn du Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf deinem Raspberry Pi installiert hast, musst du den Pironman 5 Mini über die Befehlszeile konfigurieren. Nachfolgend findest du detaillierte Anleitungen.

.. note::

  Bevor du mit der Konfiguration fortfährst, musst du deinen Raspberry Pi starten und dich anmelden.
  Wenn du dir nicht sicher bist, wie du dich anmeldest, kannst du die offizielle Website von Raspberry Pi besuchen: |link_rpi_get_start|.


.. _safe_shutdown_mini:

1. Konfiguration des Herunterfahrens zur Deaktivierung der GPIO-Stromversorgung
---------------------------------------------------------------------------------

Um zu verhindern, dass der über den GPIO des Raspberry Pi gespeiste RGB-Lüfter nach dem Herunterfahren weiterläuft, ist es wichtig, den Raspberry Pi so zu konfigurieren, dass die GPIO-Stromversorgung deaktiviert wird.

#. Öffne das EEPROM-Konfigurationstool:

   .. code-block::

      sudo raspi-config

#. Gehe zu **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Wähle **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Speichere die Änderungen. Du wirst aufgefordert, einen Neustart durchzuführen, damit die neuen Einstellungen wirksam werden.


.. _install_pironman5_module_mini:

2. Installation des Moduls ``pironman5``
-----------------------------------------------------------

.. .. note::

..    Für „Lite“-Systeme installiere zunächst Werkzeuge wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. Lade das Modul ``pironman5`` von GitHub herunter und installiere es.

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash



   .. note::

      1. Wenn du **Ubuntu** verwendest, installiere zuerst ``curl``: ``sudo apt install curl -y``

      2. Wenn du die Pironman-5-Serie zusammen mit **PiPower 5** verwendest, führe stattdessen den folgenden Befehl aus:

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash -s -- --pipower5

#. Wähle nach dem Ausführen des Installationsprogramms dein Pironman-5-Modell aus (1~4).

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

   #. Nach erfolgreichem Start des Pironman 5 Mini überprüfe, ob die folgenden Komponenten ordnungsgemäß funktionieren.

   * **Einschaltknopf**

     * Kurz drücken: Einschalten.
     * 2 Sekunden gedrückt halten: Sicheres Herunterfahren (erfordert :ref:`safe_shutdown_mini`).
     * 5 Sekunden gedrückt halten: Erzwungenes Herunterfahren.

   * **WS2812 RGB-LEDs**

     * Leuchten blau mit einem Atemeffekt.

   * **RGB-Lüfter**

     * Standardmäßig auf **Always On** (immer an) eingestellt.
     * Der Arbeitsmodus kann über Befehle oder das Dashboard geändert werden. Siehe :ref:`cc_control_fan_mini`.

   * **CPU-Lüfter (Active Cooler-Lüfter)**

     * Passt die Geschwindigkeit automatisch an die CPU-Temperatur an.
     * Standard-Lüfterkurve:

       * < 50°C: Aus (0 %)
       * 50°C+: Niedrig (30 %)
       * 60°C+: Mittel (50 %)
       * 67,5°C+: Hoch (70 %)
       * 75°C+: Volle Geschwindigkeit (100 %)

#. Verwende ``systemctl``, um den ``pironman5.service`` zu verwalten.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Ersetze ``restart`` je nach Bedarf durch ``start``, ``stop`` oder ``status``, um den Dienst zu verwalten.

.. note::

   Der Pironman 5 Mini ist jetzt einsatzbereit.

   Für erweiterte Steuerungs- und Dashboard-Funktionen siehe :ref:`control_commands_dashboard_mini`.
