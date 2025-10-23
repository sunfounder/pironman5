.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!


Einrichtung auf Raspberry Pi/Ubuntu/Kali/Homebridge OS
=============================================================

Wenn Sie Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf Ihrem Raspberry Pi installiert haben, müssen Sie den Pironman 5 über die Kommandozeile konfigurieren. Detaillierte Tutorials finden Sie unten:

.. note::

  Bevor Sie mit der Konfiguration beginnen, müssen Sie Ihren Raspberry Pi starten und sich anmelden. Falls Sie nicht wissen, wie Sie sich anmelden können, besuchen Sie die offizielle Raspberry Pi-Website: |link_rpi_get_start|.


Konfiguration zum Ausschalten der GPIO-Stromversorgung
---------------------------------------------------------------
Um zu verhindern, dass der OLED-Bildschirm und die RGB-Lüfter, die über die GPIO-Pins des Raspberry Pi mit Strom versorgt werden, nach dem Herunterfahren aktiv bleiben, ist es wichtig, den Raspberry Pi so zu konfigurieren, dass die GPIO-Stromversorgung deaktiviert wird.

#. Bearbeiten Sie die ``EEPROM``-Konfigurationsdatei manuell mit diesem Befehl:

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. Ändern Sie die Einstellung ``POWER_OFF_ON_HALT`` in der Datei auf ``1``. Zum Beispiel:

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Drücken Sie ``Ctrl + X``, ``Y`` und ``Enter``, um die Änderungen zu speichern.


Herunterladen und Installieren des ``pironman5`` Moduls
-----------------------------------------------------------

#. Für Lite-Systeme installieren Sie zunächst Tools wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.
  
   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Laden Sie anschließend den Code von GitHub herunter und installieren Sie das ``pironman5``-Modul.

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Nach erfolgreicher Installation ist ein Systemneustart erforderlich, um die Installation zu aktivieren. Befolgen Sie die Bildschirmanweisungen zum Neustart.
   
   Nach dem Neustart wird der ``pironman5.service`` automatisch gestartet. Hier sind die Hauptkonfigurationen für den Pironman 5:
   
   * Der OLED-Bildschirm zeigt CPU, RAM, Festplattennutzung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.
   * Vier WS2812 RGB-LEDs leuchten in Blau im Atmungsmodus auf.
   
   .. note::
    
     RGB-Lüfter drehen sich nicht, bevor die Temperatur 60°C erreicht. Für andere Aktivierungstemperaturen siehe :ref:`cc_control_fan`.

#. Sie können das ``systemctl``-Tool verwenden, um den ``pironman5.service`` zu ``starten``, ``stoppen``, ``neustarten`` oder den ``Status`` zu überprüfen.

  .. code-block:: shell

      sudo systemctl restart pironman5.service

  * ``restart``: Verwenden Sie diesen Befehl, um Änderungen an den Einstellungen von Pironman 5 anzuwenden.
  * ``start/stop``: Aktivieren oder deaktivieren Sie den ``pironman5.service``.
  * ``status``: Überprüfen Sie den Betriebsstatus des ``pironman5``-Programms mit dem ``systemctl``-Tool.


.. note::

   Zu diesem Zeitpunkt haben Sie den Pironman 5 erfolgreich eingerichtet, und er ist einsatzbereit.
   
   Für die erweiterte Steuerung seiner Komponenten siehe bitte :ref:`control_commands_dashboard_5`.
