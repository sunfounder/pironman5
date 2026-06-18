.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_pi_os:

Einrichtung unter Raspberry Pi/Ubuntu/Kali/Homebridge OS
=======================================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Wenn Sie Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf Ihrem Raspberry Pi installiert haben, müssen Sie den Pironman 5 Pro MAX über die Befehlszeile konfigurieren. Ausführliche Tutorials finden Sie unten:

.. note::

  Bevor Sie mit der Konfiguration beginnen, müssen Sie Ihren Raspberry Pi hochfahren und sich anmelden. Wenn Sie nicht wissen, wie Sie sich anmelden, besuchen Sie die offizielle Raspberry Pi-Website: |link_rpi_get_start|.


.. _safe_shutdown_promax:

1. Konfiguration des Herunterfahrens zur Deaktivierung der GPIO-Stromversorgung
---------------------------------------------------------------------------------

Um zu verhindern, dass der OLED-Bildschirm und die RGB-Lüfter, die über die GPIOs des Raspberry Pi mit Strom versorgt werden, nach dem Herunterfahren aktiv bleiben, ist es wichtig, den Raspberry Pi für die Deaktivierung der GPIO-Stromversorgung zu konfigurieren.

#. Öffnen Sie das EEPROM-Konfigurationstool:

   .. code-block::

      sudo raspi-config

#. Navigieren Sie zu **Erweiterte Optionen → A12 Herunterfahrmodus**.

   .. image:: img/shutdown_behaviour.png

#. Wählen Sie **B1 Vollständige Abschaltung**.

   .. image:: img/run_power_off.png

#. Speichern Sie die Änderungen. Sie werden aufgefordert, neu zu starten, damit die neuen Einstellungen wirksam werden.


.. _install_pironman5_module_promax:

2. Installation des Moduls ``pironman5``
-----------------------------------------------------------

.. .. note::

..    Installieren Sie für Lite-Systeme zunächst Tools wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. Laden Sie das Modul ``pironman5`` von GitHub herunter und installieren Sie es.

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash



   .. note::

      1. Wenn Sie **Ubuntu** verwenden, installieren Sie zuerst ``curl``: ``sudo apt install curl -y``

      2. Wenn Sie die Pironman-5-Serie zusammen mit **PiPower 5** verwenden, führen Sie stattdessen den folgenden Befehl aus:

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --pipower5

#. Wählen Sie nach dem Ausführen des Installationsprogramms Ihr Pironman-5-Modell aus (1~4).

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. Sobald die Installation abgeschlossen ist, starten Sie den Raspberry Pi wie aufgefordert neu. Der erste Start kann bis zu 30 Sekunden dauern, während die Dienste initialisiert werden.

   #. Nach erfolgreichem Start des Pironman 5 Pro MAX überprüfen Sie, ob die folgenden Komponenten ordnungsgemäß funktionieren.

   * **OLED-Bildschirm**

     * Zeigt CPU-Auslastung, RAM-Auslastung, CPU-Temperatur und IP-Adresse an.
     * Schaltet sich nach 10 Sekunden automatisch aus.
     * Drücken Sie kurz den Einschaltknopf, um den Bildschirm zu aktivieren oder die Seiten zu wechseln.

   * **Einschaltknopf**

     * Kurz drücken: Einschalten / OLED aktivieren / OLED-Seite wechseln.
     * 2 Sekunden gedrückt halten: Sicheres Herunterfahren (erfordert :ref:`safe_shutdown_promax`).
     * 5 Sekunden gedrückt halten: Erzwungenes Herunterfahren.

   * **WS2812 RGB-LEDs**

     * Leuchten blau mit einem Atemeffekt.

   * **PWM-Lüfter**

     * Standardmäßig auf **Always On** (immer an) eingestellt.
     * Der Arbeitsmodus kann über Befehle oder das Dashboard konfiguriert werden.

   * **CPU-Lüfter (Tower-Cooler-Lüfter)**

     * Passt die Geschwindigkeit automatisch an die CPU-Temperatur an.
     * Standard-Lüfterkurve:

       * < 50°C: Aus (0 %)
       * 50°C+: Niedrig (30 %)
       * 60°C+: Mittel (50 %)
       * 67,5°C+: Hoch (70 %)
       * 75°C+: Volle Geschwindigkeit (100 %)

#. Verwenden Sie ``systemctl``, um den ``pironman5.service`` zu verwalten.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Ersetzen Sie ``restart`` je nach Bedarf durch ``start``, ``stop`` oder ``status``, um den Dienst zu verwalten.

.. note::

   Der Pironman 5 Pro MAX ist jetzt einsatzbereit.

   Informationen zur erweiterten Steuerung und zu Dashboard-Funktionen finden Sie unter :ref:`control_commands_dashboard_promax`.
