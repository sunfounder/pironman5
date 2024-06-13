.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _set_up_pironman5:

Set Up Pironman5 on Raspberry Pi/Ubuntu/Kali OS
==================================================

.. note::

  Bevor Sie die Konfiguration vornehmen, müssen Sie sich beim Raspberry Pi anmelden können, entweder durch Anschließen eines Bildschirms oder über eine Remote-Anmeldung. Unten finden Sie das Tutorial zur Anmeldung beim Raspberry Pi OS. Für Ubuntu- und Kali-Systeme müssen Sie auf zusätzliche Ressourcen zurückgreifen.

  * :ref:`login_rpi`


Konfiguration des Herunterfahrens zur Deaktivierung der GPIO-Stromversorgung
-------------------------------------------------------------------------------------
Um zu verhindern, dass der OLED-Bildschirm und die RGB-Lüfter, die über den Raspberry Pi GPIO mit Strom versorgt werden, nach dem Herunterfahren aktiv bleiben, ist es wichtig, den Raspberry Pi so zu konfigurieren, dass die GPIO-Stromversorgung deaktiviert wird.

* Bearbeiten Sie die ``EEPROM``-Konfigurationsdatei manuell mit diesem Befehl:

  .. code-block:: shell

    sudo rpi-eeprom-config -e

* Ändern Sie die Einstellung ``POWER_OFF_ON_HALT`` in der Datei auf ``1``. Zum Beispiel:

  .. code-block:: shell

    BOOT_UART=1
    POWER_OFF_ON_HALT=1
    BOOT_ORDER=0xf41

* Drücken Sie ``Ctrl + X``, ``Y`` und ``Enter``, um die Änderungen zu speichern.


Herunterladen und Installieren des ``pironman5`` Moduls
-------------------------------------------------------------

.. note::

  Für Lite-Systeme installieren Sie zunächst Werkzeuge wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.
  
  .. code-block:: shell
  
    sudo apt-get update
    sudo apt-get install git -y
    sudo apt-get install python3 python3-pip python3-setuptools -y

Laden Sie den Code von GitHub herunter und installieren Sie das ``pironman5``-Modul.

.. code-block:: shell

  cd ~
  git clone https://github.com/sunfounder/pironman5.git
  cd ~/pironman5
  sudo python3 install.py

Nach erfolgreicher Installation ist ein Systemneustart erforderlich, um die Installation zu aktivieren. Befolgen Sie die Neustartaufforderung auf dem Bildschirm.

Nach dem Neustart startet der ``pironman5.service`` automatisch. Hier sind die Hauptkonfigurationen für |link_pironman5|:

  * Der OLED-Bildschirm zeigt CPU, RAM, Speichernutzung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.
  * Vier WS2812-RGB-LEDs leuchten in Blau im Atemmodus.
  * Die RGB-Lüfter aktivieren sich bei 60°C.

Sie können das ``systemctl``-Tool verwenden, um ``pironman5.service`` zu ``starten``, ``stoppen``, ``neu zu starten`` oder den ``Status`` zu überprüfen.

.. code-block:: shell

  sudo systemctl restart pironman5.service

* ``restart``: Verwenden Sie diesen Befehl, um Änderungen an den Einstellungen des Pironman 5 anzuwenden.
* ``start/stop``: Aktivieren oder deaktivieren Sie den ``pironman5.service``.
* ``status``: Überprüfen Sie den Betriebsstatus des ``pironman5``-Programms mit dem ``systemctl``-Tool.

.. note::

  * Als nächstes können Sie die Komponenten des |link_pironman5| über das Dashboard anzeigen und steuern, siehe :ref:`view_control_dashboard`.
  * Wenn Sie Befehle verwenden möchten, siehe :ref:`view_control_commands`.