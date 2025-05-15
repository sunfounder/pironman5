.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche gemeinsam mit Gleichgesinnten noch tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenhilfe**: Erhalte Unterstützung bei Problemen nach dem Kauf und technischen Herausforderungen – durch unsere Community und unser Support-Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erfahre als Erste:r von neuen Produkten und genieße exklusive Einblicke.
    - **Besondere Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Aktionen & Gewinnspiele**: Nimm an saisonalen Events und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde heute noch Mitglied!

FAQ
============

Wie deaktiviere ich das Web-Dashboard?
------------------------------------------------------

Nach erfolgreicher Installation des ``pironman5``-Moduls kannst du auf das :ref:`max_view_control_dashboard` zugreifen.

Wenn du diese Funktion nicht benötigst und CPU- sowie RAM-Auslastung reduzieren möchtest, kannst du das Dashboard bereits während der Installation von ``pironman5`` mit dem Parameter ``--disable-dashboard`` deaktivieren.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Wenn ``pironman 5`` bereits installiert ist, kannst du das ``dashboard``-Modul und ``influxdb`` deinstallieren und anschließend pironman5 neu starten, um die Änderungen zu übernehmen:

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

Unterstützt der Pironman 5 Retro-Gaming-Systeme?
------------------------------------------------------
Ja, der Pironman 5 ist kompatibel. Die meisten Retro-Gaming-Systeme sind jedoch stark optimiert und erlauben keine nachträgliche Installation zusätzlicher Software. Daher funktionieren einige Komponenten des Pironman 5 – wie das OLED-Display, die beiden RGB-Lüfter und die vier RGB-LEDs – möglicherweise nicht korrekt, da sie auf die Installation spezifischer Softwarepakete angewiesen sind.


.. note::

    Das System Batocera.linux ist jetzt vollständig mit dem Pironman 5 kompatibel. Batocera.linux ist eine quelloffene und vollkommen kostenlose Retro-Gaming-Distribution.

    * :ref:`max_install_batocera`
    * :ref:`max_set_up_batocera`

Wie kann ich Komponenten mit dem ``pironman5``-Befehl steuern?
----------------------------------------------------------------------
In der folgenden Anleitung erfährst du, wie du mit dem ``pironman5``-Befehl die Komponenten des Pironman 5 steuerst:

* :ref:`max_view_control_commands`

Wie kann ich die Boot-Reihenfolge des Raspberry Pi per Befehl ändern?
----------------------------------------------------------------------------

Wenn du bereits am Raspberry Pi angemeldet bist, kannst du die Boot-Reihenfolge per Kommandozeile anpassen. Eine detaillierte Anleitung findest du hier:

* :ref:`max_configure_boot_ssd`


Wie kann ich die Boot-Reihenfolge mit dem Raspberry Pi Imager ändern?
--------------------------------------------------------------------------

Neben der direkten Änderung des ``BOOT_ORDER`` in der EEPROM-Konfiguration kannst du auch den **Raspberry Pi Imager** verwenden, um die Boot-Reihenfolge zu verändern.

Für diesen Schritt wird empfohlen, eine separate SD-Karte zu verwenden.

* :ref:`max_update_bootloader`

Wie kopiere ich das System von der SD-Karte auf eine NVMe-SSD?
--------------------------------------------------------------------

Wenn du eine NVMe-SSD besitzt, aber keinen Adapter zur Verbindung mit deinem Computer hast, kannst du das System zunächst auf einer Micro-SD-Karte installieren. Sobald der Pironman 5 erfolgreich gestartet ist, kannst du das System von der SD-Karte auf die NVMe-SSD übertragen. Eine detaillierte Anleitung findest du hier:


* :ref:`max_copy_sd_to_nvme_rpi`


OLED-Display funktioniert nicht?
------------------------------------

Wenn das OLED-Display nichts anzeigt oder falsche Inhalte darstellt, folge diesen Schritten zur Fehlerbehebung:

Stelle sicher, dass das FPC-Kabel des OLED-Displays korrekt angeschlossen ist.

#. Verwende den folgenden Befehl, um die Programmlogs zu überprüfen und nach Fehlermeldungen zu suchen:

   .. code-block:: shell

      cat /opt/pironman5/log

#. Alternativ kannst du prüfen, ob die I2C-Adresse 0x3C des OLED erkannt wird:

   .. code-block:: shell

        sudo i2cdetect -y 1

#. Falls keine Fehler erkennbar sind, versuche den Dienst pironman5 neu zu starten:


   .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _max_openssh_powershell:

OpenSSH über PowerShell installieren
----------------------------------------

Wenn du versuchst, dich mit dem Befehl ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) mit deinem Raspberry Pi zu verbinden, aber folgende Fehlermeldung erscheint:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Dann bedeutet das, dass auf deinem System `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Folge dieser Anleitung, um es manuell zu installieren:

#. Tippe ``powershell`` in die Windows-Suche, klicke mit der rechten Maustaste auf ``Windows PowerShell`` und wähle ``Run as administrator``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Führe den folgenden Befehl aus, um ``OpenSSH.Client`` zu installieren:

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach der Installation wird folgende Ausgabe angezeigt:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Überprüfe die Installation mit folgendem Befehl:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Nun sollte angezeigt werden, dass ``OpenSSH.Client`` erfolgreich installiert wurde:

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Falls diese Ausgabe nicht erscheint, ist dein Windows-System möglicherweise zu alt. In diesem Fall wird empfohlen, ein alternatives SSH-Tool wie |link_putty| zu verwenden.

#. Starte PowerShell neu und führe sie erneut als Administrator aus. Du solltest dich nun über den Befehl ``ssh`` mit deinem Raspberry Pi verbinden können. Du wirst zur Eingabe deines zuvor festgelegten Passworts aufgefordert.

   .. image:: img/powershell_login.png



Kann ich die Funktionen des Pironman 5 weiterhin nutzen, wenn ich OMV installiert habe?
--------------------------------------------------------------------------------------------------------

Ja, OpenMediaVault wird auf dem Raspberry-Pi-System installiert. Folge anschließend den Schritten unter :ref:`max_set_up_pi_os`, um die Einrichtung fortzusetzen.