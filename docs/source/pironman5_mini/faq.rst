.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Expertenhilfe**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung durch unser Team und die Community.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erfahre frühzeitig von neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Sichere dir exklusive Rabatte auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an Aktionen und Gewinnspielen zu Feiertagen teil.

    👉 Bereit für neue Projekte? Klicke [|link_sf_facebook|] und werde noch heute Teil der Community!

FAQ
============

1. Zu den kompatiblen Betriebssystemen
----------------------------------------

Getestete Systeme auf dem Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Zum Power-Button
-----------------------

Der Power-Button entspricht dem Ein-/Aus-Schalter des Raspberry Pi 5 und funktioniert genauso.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Herunterfahren**

  * Beim Raspberry Pi **Bookworm Desktop** zweimal kurz drücken zum Herunterfahren.
  * Beim **Bookworm Lite** einmal drücken zum Herunterfahren.
  * Zum Erzwingen eines Hard-Shutdown: Taste gedrückt halten.

* **Einschalten**

  * Wenn der Raspberry Pi ausgeschaltet, aber mit Strom versorgt ist, genügt ein kurzer Tastendruck zum Einschalten.

* Bei Systemen ohne Softwareunterstützung für den Power-Button: Taste 5 Sekunden halten zum Ausschalten, danach kurzer Tastendruck zum Einschalten.

3. Zum Raspberry Pi AI HAT+
----------------------------------------------------

Das Raspberry Pi AI HAT+ ist nicht kompatibel mit dem Pironman 5.

   .. image::  img/output3.png
    :width: 400

Das Raspberry Pi AI Kit kombiniert das Raspberry Pi M.2 HAT+ mit dem Hailo AI-Beschleunigungsmodul.

   .. image::  img/output2.jpg
    :width: 400

Du kannst das Hailo AI-Modul aus dem Kit entfernen und direkt im NVMe-PIP-Modul des Pironman 5 Mini verwenden.

   .. .. image::  img/output4.png
   ..      :width: 800

4. Unterstützt der Pironman 5 Mini Retro-Gaming-Systeme?
--------------------------------------------------------------

Ja, ist kompatibel. Allerdings können viele Retro-Gaming-Systeme keine zusätzliche Software installieren, was dazu führen kann, dass Funktionen wie der RGB-Lüfter oder die 4 RGB-LEDs nicht funktionieren, da sie auf zusätzliche Software angewiesen sind.


5. RGB-LEDs funktionieren nicht?
--------------------------------------

#. Überprüfe die Jumper-Kappe über J9 – sie muss korrekt auf den Pins sitzen, die GPIO10 mit den RGB-LEDs verbinden.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Vergewissere dich, dass ein kompatibles Betriebssystem installiert ist:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Bei inkompatiblen Systemen: Siehe :ref:`install_the_os_mini`.

#. Führe den Befehl ``sudo raspi-config`` aus, um das Konfigurationsmenü zu öffnen. Navigiere zu **3 Interfacing Options** -> **I3 SPI** -> **YES**, und klicke dann auf **OK** und **Finish**, um SPI zu aktivieren. Starte anschließend den Pironman 5 neu.

Wenn das Problem weiterhin besteht, sende bitte eine E-Mail an service@sunfounder.com. Wir antworten dir schnellstmöglich.

6. CPU-Lüfter funktioniert nicht?
----------------------------------------------

Der CPU-Lüfter arbeitet nur, wenn die eingestellte Temperaturschwelle erreicht ist.

**Lüftergeschwindigkeitsregelung basierend auf der Temperatur**

Der PWM-Lüfter passt seine Geschwindigkeit dynamisch an die Temperatur des Raspberry Pi 5 an:

* **Unter 50°C**: Lüfter bleibt aus (0 %).
* **Bei 50°C**: Niedrige Geschwindigkeit (30 %).
* **Bei 60°C**: Mittlere Geschwindigkeit (50 %).
* **Bei 67,5°C**: Hohe Geschwindigkeit (70 %).
* **Ab 75°C**: Maximale Geschwindigkeit (100 %).

Weitere Details findest du hier: :ref:`fan_mini`

7. Wie kann man das Web-Dashboard deaktivieren?
------------------------------------------------------

Nach der Installation des Moduls ``pironman5`` kannst du auf das :ref:`view_control_dashboard_mini` zugreifen.

Wenn du diese Funktion nicht benötigst und CPU-/RAM-Auslastung reduzieren möchtest, kannst du das Dashboard während der Installation mit dem Flag ``--disable-dashboard`` deaktivieren:

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Wenn du ``pironman 5`` bereits installiert hast, kannst du das ``dashboard``-Modul und ``influxdb`` entfernen und anschließend ``pironman5`` neu starten:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

8. Wie steuert man Komponenten mit dem Befehl ``pironman5``?
----------------------------------------------------------------------
Eine Anleitung zur Steuerung der Komponenten des Pironman 5 mit dem Befehl ``pironman5`` findest du unter:

* :ref:`view_control_commands_mini`

9. Wie ändert man die Boot-Reihenfolge des Raspberry Pi per Kommandozeile?
--------------------------------------------------------------------------------

Wenn du bereits auf deinem Raspberry Pi angemeldet bist, kannst du die Boot-Reihenfolge über Befehle ändern. Anleitung:

* :ref:`configure_boot_ssd_mini`


10. Wie kann man die Boot-Reihenfolge mit dem Raspberry Pi Imager ändern?
-------------------------------------------------------------------------------

Zusätzlich zur Änderung der ``BOOT_ORDER`` in der EEPROM-Konfiguration kannst du auch den **Raspberry Pi Imager** nutzen, um die Boot-Reihenfolge zu ändern.

Wir empfehlen, hierfür eine Ersatzkarte zu verwenden.

* :ref:`update_bootloader_mini`

11. Wie kopiert man das System von der SD-Karte auf eine NVMe-SSD?
--------------------------------------------------------------------

Wenn du eine NVMe-SSD besitzt, aber keinen Adapter zur Verbindung mit deinem Computer hast, kannst du das System zunächst auf eine Micro-SD-Karte installieren. Nach erfolgreichem Start des Pironman 5 kannst du das System auf die NVMe-SSD übertragen.


* :ref:`copy_sd_to_nvme_rpi_mini`

12. Wie entfernt man die Schutzfolie von den Acrylplatten?
----------------------------------------------------------------

Dem Set liegen zwei Acrylplatten bei, die beidseitig mit einer gelben oder transparenten Schutzfolie versehen sind, um Kratzer zu vermeiden. Die Folie lässt sich unter Umständen schwer abziehen. Verwende einen Schraubendreher, um vorsichtig eine Ecke anzuheben und dann die Folie langsam abzuziehen.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center



.. _openssh_powershell_mini:

13. Wie installiert man OpenSSH über PowerShell?
----------------------------------------------------

Wenn du den Befehl ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) ausführst und folgende Fehlermeldung erhältst:

.. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Das bedeutet, dass dein Computersystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Du musst der folgenden Anleitung folgen, um es manuell zu installieren.

#. Gib ``powershell`` in die Windows-Suchleiste ein, rechtsklicke auf ``Windows PowerShell`` und wähle ``Run as administrator``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Installiere ``OpenSSH.Client`` mit folgendem Befehl:

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach erfolgreicher Installation erscheint:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Überprüfe die Installation mit:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Es wird nun angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Wenn dies nicht erscheint, ist dein Windows zu alt. Verwende stattdessen ein Tool wie |link_putty|.

#. Starte PowerShell neu (wieder als Administrator) und verbinde dich dann mit dem ``ssh``-Befehl mit deinem Raspberry Pi. Du wirst zur Eingabe deines Passworts aufgefordert.

   .. image:: img/powershell_login.png
