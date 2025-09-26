.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum der Community beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitig Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Genieße exklusive Preisnachlässe auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an festlichen Aktionen und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu erschaffen? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _set_up_pironman5_mini:

Einrichtung unter Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

Wenn du Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf deinem Raspberry Pi installiert hast, musst du den Pironman 5 Mini über die Kommandozeile konfigurieren. Ausführliche Anleitungen findest du unten:

.. note::

  Vor der Konfiguration musst du dein Raspberry Pi starten und dich anmelden. Wenn du dir unsicher bist, wie das funktioniert, besuche bitte die offizielle Raspberry Pi Website: |link_rpi_get_start|.


Konfiguration zum Deaktivieren der GPIO-Stromversorgung beim Herunterfahren
--------------------------------------------------------------------------------------
Um zu verhindern, dass der über GPIO mit Strom versorgte RGB-Lüfter nach dem Herunterfahren weiterhin läuft, sollte der Raspberry Pi entsprechend konfiguriert werden.

#. Bearbeite die ``EEPROM``-Konfigurationsdatei manuell mit folgendem Befehl:

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. Ändere in der Datei den Wert von ``POWER_OFF_ON_HALT`` auf ``1``. Beispiel:

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Drücke ``Ctrl + X``, ``Y`` und ``Enter``, um die Änderungen zu speichern.


Herunterladen und Installieren des ``pironman5``-Moduls
-----------------------------------------------------------

#. Installiere bei Lite-Systemen zunächst die erforderlichen Tools wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Lade anschließend den Code von GitHub herunter und installiere das ``pironman5``-Modul.

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Nach erfolgreicher Installation ist ein Systemneustart erforderlich, um die Installation zu aktivieren. Folge der Aufforderung zum Reboot auf dem Bildschirm.

   Nach dem Neustart wird der Dienst ``pironman5.service`` automatisch gestartet. Die wichtigsten Konfigurationen des Pironman 5 sind:

   * Vier WS2812-RGB-LEDs leuchten blau im Atemmodus.

   .. note::

     Der RGB-Lüfter dreht sich erst, wenn die Temperatur 60 °C erreicht. Für andere Aktivierungstemperaturen siehe :ref:`cc_control_fan_mini`.

#. Du kannst das Tool ``systemctl`` verwenden, um ``pironman5.service`` zu ``starten``, ``stoppen``, ``neuzustarten`` oder den ``Status`` zu überprüfen.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``: Mit diesem Befehl werden Änderungen an den Einstellungen des Pironman 5 Mini übernommen.
   * ``start/stop``: Aktiviert oder deaktiviert den Dienst ``pironman5.service``.
   * ``status``: Zeigt mit ``systemctl`` den aktuellen Status des ``pironman5``-Programms an.


.. note::

   An diesem Punkt haben Sie den Pironman 5 Mini erfolgreich eingerichtet, und er ist einsatzbereit.
   
   Für die erweiterte Steuerung seiner Komponenten verweisen wir auf :ref:`control_commands_dashboard_mini`.
