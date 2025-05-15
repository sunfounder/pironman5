.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Entdecken Sie gemeinsam mit anderen Technikbegeisterten die spannende Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Erhalten Sie kompetente Hilfe bei technischen Problemen und Herausforderungen nach dem Kauf – durch unsere Community und unser Support-Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps, Anleitungen und Erfahrungen aus, um Ihre Kenntnisse gezielt zu erweitern.
    - **Exklusive Vorschauen**: Profitieren Sie von frühem Zugang zu Produktneuheiten und Vorabinformationen.
    - **Sonderrabatte**: Sichern Sie sich exklusive Rabatte auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nehmen Sie an spannenden Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns Neues zu entdecken und zu entwickeln? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!


Einrichtung auf Raspberry Pi/Ubuntu/Kali/Homebridge OS
=============================================================

Wenn Sie Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf Ihrem Raspberry Pi verwenden, müssen Sie den Pironman 5 über die Kommandozeile konfigurieren. Detaillierte Anleitungen finden Sie unten:

.. note::

  Bevor Sie mit der Einrichtung beginnen, starten Sie bitte Ihren Raspberry Pi und melden sich an. Falls Sie nicht wissen, wie das funktioniert, besuchen Sie die offizielle Raspberry Pi-Webseite: |link_rpi_get_start|.


Konfiguration zur Deaktivierung der GPIO-Stromversorgung
---------------------------------------------------------------
Um zu verhindern, dass das OLED-Display und die RGB-Lüfter, die über die GPIO-Pins mit Strom versorgt werden, nach dem Herunterfahren weiterlaufen, sollten Sie den Raspberry Pi so konfigurieren, dass die GPIO-Stromversorgung deaktiviert wird.

#. Öffnen Sie die ``EEPROM``-Konfigurationsdatei zur Bearbeitung mit folgendem Befehl:

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. Setzen Sie den Parameter ``POWER_OFF_ON_HALT`` in der Datei auf ``1``. Zum Beispiel:

   .. code-block:: shell

     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Speichern Sie die Änderungen mit ``Ctrl + X``, anschließend ``Y`` und bestätigen Sie mit ``Enter``.


Herunterladen und Installieren des ``pironman5``-Moduls
-----------------------------------------------------------

#. Installieren Sie bei Lite-Systemen zunächst die benötigten Tools wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Laden Sie anschließend den Quellcode von GitHub herunter und installieren Sie das ``pironman5``-Modul.

   .. code-block:: shell

      cd ~
      git clone https://github.com/sunfounder/pironman5.git
      cd ~/pironman5
      sudo python3 install.py

   Nach erfolgreicher Installation ist ein Neustart des Systems erforderlich, um die Konfiguration zu aktivieren. Folgen Sie den Anweisungen auf dem Bildschirm.

   Beim nächsten Start wird der Dienst ``pironman5.service`` automatisch geladen. Die Hauptfunktionen des Pironman 5 umfassen:

   * Das OLED-Display zeigt Informationen zu CPU, RAM, Speicherplatz, CPU-Temperatur und IP-Adresse des Raspberry Pi an.
   * Die vier WS2812 RGB-LEDs leuchten im blauen Atemmodus.

   .. note::

     Die RGB-Lüfter starten erst bei einer Temperatur von 60 °C. Für Anpassungen der Einschaltgrenze siehe :ref:`cc_control_fan`.

#. Sie können das Tool ``systemctl`` verwenden, um den Dienst ``pironman5.service`` zu ``starten``, ``stoppen``, ``neustarten`` oder den ``Status`` abzufragen.

  .. code-block:: shell

      sudo systemctl restart pironman5.service

  * ``restart``: Übernehmen Sie Änderungen an den Einstellungen von Pironman 5.
  * ``start/stop``: Aktivieren oder deaktivieren Sie den ``pironman5.service``.
  * ``status``: Prüfen Sie den aktuellen Status des ``pironman5``-Dienstes mit dem ``systemctl``-Tool.
