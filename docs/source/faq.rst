.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

FAQ
============

Wie man Komponenten mit dem ``pironman5`` Befehl steuert
----------------------------------------------------------------------
Sie können das folgende Tutorial verwenden, um die Komponenten des Pironman 5 mit dem ``pironman5`` Befehl zu steuern.

* :ref:`view_control_commands`

Wie man die Startreihenfolge des Raspberry Pi mit Befehlen ändert
------------------------------------------------------------------------------------

Wenn Sie bereits in Ihren Raspberry Pi eingeloggt sind, können Sie die Startreihenfolge mit Befehlen ändern. Detaillierte Anweisungen sind wie folgt:

* :ref:`configure_boot_ssd`

Wie man die Startreihenfolge mit dem Raspberry Pi Imager ändert
----------------------------------------------------------------------------

Neben der Änderung der ``BOOT_ORDER`` in der EEPROM-Konfiguration können Sie auch den **Raspberry Pi Imager** verwenden, um die Startreihenfolge Ihres Raspberry Pi zu ändern.

Es wird empfohlen, für diesen Schritt eine Ersatzkarte zu verwenden.

* :ref:`update_bootloader`

Wie man das System von der SD-Karte auf eine NVMe SSD kopiert
-----------------------------------------------------------------------------

Wenn Sie eine NVMe SSD haben, aber keinen Adapter, um Ihre NVMe mit Ihrem Computer zu verbinden, können Sie das System zuerst auf Ihrer Micro SD-Karte installieren. Sobald der Pironman 5 erfolgreich hochgefahren ist, können Sie das System von Ihrer Micro SD-Karte auf Ihre NVMe SSD kopieren. Detaillierte Anweisungen sind wie folgt:

* :ref:`boot_from_ssd`

OLED-Bildschirm funktioniert nicht?
-----------------------------------------------

Wenn der OLED-Bildschirm nicht anzeigt oder falsch anzeigt, können Sie die folgenden Schritte zur Fehlerbehebung ausführen:

Überprüfen Sie, ob das FPC-Kabel des OLED-Bildschirms ordnungsgemäß angeschlossen ist.

#. Verwenden Sie den folgenden Befehl, um die Programmlogs anzuzeigen und auf Fehlermeldungen zu überprüfen.

    .. code-block:: shell

        cat /opt/pironman5/log

#. Alternativ können Sie den folgenden Befehl verwenden, um zu überprüfen, ob die I2C-Adresse 0x3C des OLED erkannt wird:
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. Wenn die ersten beiden Schritte keine Probleme aufdecken, versuchen Sie, den pironman5-Dienst neu zu starten, um zu sehen, ob das Problem dadurch behoben wird.

    .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _openssh_powershell:

OpenSSH über PowerShell installieren
----------------------------------------

Wenn Sie ``ssh <Benutzername>@<hostname>.local`` (oder ``ssh <Benutzername>@<IP-Adresse>``) verwenden, um sich mit Ihrem Raspberry Pi zu verbinden, aber die folgende Fehlermeldung erscheint:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

bedeutet dies, dass Ihr Computersystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Sie müssen der folgenden Anleitung folgen, um es manuell zu installieren.

#. Geben Sie ``powershell`` in das Suchfeld Ihres Windows-Desktops ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im erscheinenden Menü ``Als Administrator ausführen``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Verwenden Sie den folgenden Befehl, um ``OpenSSH.Client`` zu installieren.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach der Installation wird die folgende Ausgabe zurückgegeben.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Überprüfen Sie die Installation mit dem folgenden Befehl.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Es wird Ihnen nun angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Wenn die obige Aufforderung nicht erscheint, bedeutet dies, dass Ihr Windows-System immer noch zu alt ist. Es wird empfohlen, ein Drittanbieter-SSH-Tool wie |link_putty| zu installieren.

#. Starten Sie nun PowerShell neu und führen Sie es weiterhin als Administrator aus. An diesem Punkt können Sie sich mit dem Befehl ``ssh`` bei Ihrem Raspberry Pi anmelden, wobei Sie aufgefordert werden, das zuvor eingerichtete Passwort einzugeben.

    .. image:: img/powershell_login.png
