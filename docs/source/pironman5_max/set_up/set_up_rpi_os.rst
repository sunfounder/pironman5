.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Experten-Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorabinformationen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_set_up_pi_os:

Einrichtung unter Raspberry Pi/Ubuntu/Kali/Homebridge OS
============================================================

Wenn du Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf deinem Raspberry Pi installiert hast, musst du Pironman 5 MAX über die Kommandozeile konfigurieren. Ausführliche Anleitungen findest du weiter unten:

.. note::

  Vor der Konfiguration musst du deinen Raspberry Pi hochfahren und dich anmelden. Wenn du nicht weißt, wie das geht, besuche die offizielle Raspberry Pi Website: |link_rpi_get_start|.


Abschalten konfigurieren, um GPIO-Stromversorgung zu deaktivieren
---------------------------------------------------------------------

Damit das OLED-Display und die RGB-Lüfter nach dem Herunterfahren nicht weiter über die GPIO-Pins mit Strom versorgt werden, muss der Raspberry Pi entsprechend konfiguriert werden.

#. Öffne die ``EEPROM``-Konfigurationsdatei mit folgendem Befehl:

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. Ändere den Eintrag ``POWER_OFF_ON_HALT`` im Dokument zu ``1``. Beispiel:

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Drücke ``Ctrl + X``, dann ``Y`` und ``Enter``, um die Änderungen zu speichern.


Herunterladen und Installieren des ``pironman5``-Moduls
----------------------------------------------------------

#. Für Lite-Systeme müssen zunächst Tools wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw. installiert werden.
  
   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Lade den Code von GitHub herunter und installiere das ``pironman5``-Modul.

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Nach erfolgreicher Installation ist ein Neustart des Systems erforderlich, um die Änderungen zu übernehmen. Folge der Aufforderung zum Reboot auf dem Bildschirm.

   Nach dem Neustart wird der Dienst ``pironman5.service`` automatisch gestartet. Die Hauptfunktionen von Pironman 5 MAX sind:

   * Das OLED-Display zeigt CPU-, RAM- und Speichernutzung, CPU-Temperatur sowie die IP-Adresse des Raspberry Pi an.
   * Vier WS2812-RGB-LEDs leuchten in Blau mit dem Effekt „Breathing“.

   .. note::

     Die RGB-Lüfter beginnen erst ab einer Temperatur von 60 °C zu rotieren. Für unterschiedliche Aktivierungstemperaturen siehe: :ref:`max_cc_control_fan`.

#. Du kannst das Tool ``systemctl`` verwenden, um den Dienst ``pironman5.service`` zu ``starten``, ``stoppen``, ``neustarten`` oder dessen ``Status`` abzufragen.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service

   * ``restart``: Nutze diesen Befehl, um Änderungen an den Einstellungen von Pironman 5 MAX zu übernehmen.
   * ``start/stop``: Aktiviert oder deaktiviert den ``pironman5.service``.
   * ``status``: Prüft den aktuellen Status des ``pironman5``-Programms über ``systemctl``.
