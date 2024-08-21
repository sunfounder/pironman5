.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und festlichen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

FAQ
============

Web-Dashboard deaktivieren?
------------------------------------------------------

Sobald Sie die Installation des ``pironman5`` Moduls abgeschlossen haben, können Sie auf das :ref:`view_control_dashboard` zugreifen.

Wenn Sie diese Funktion nicht benötigen und die CPU- und RAM-Auslastung reduzieren möchten, können Sie das Dashboard während der Installation von ``pironman5`` deaktivieren, indem Sie das Flag ``--disable-dashboard`` hinzufügen.

.. code-block:: shell

  sudo python3 install.py --disable-dashboard

Wenn Sie bereits ``pironman 5`` installiert haben, können Sie das ``dashboard`` Modul und ``influxdb`` entfernen und anschließend pironman5 neu starten, um die Änderungen anzuwenden:

.. code-block:: shell

  /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
  sudo apt purge influxdb
  sudo systemctl restart pironman5

Unterstützt der Pironman 5 Retro-Gaming-Systeme?
------------------------------------------------------
Ja, er ist kompatibel. Allerdings sind die meisten Retro-Gaming-Systeme abgespeckte Versionen, die keine zusätzliche Software installieren und ausführen können. Diese Einschränkung kann dazu führen, dass einige Komponenten des Pironman 5, wie das OLED-Display, die beiden RGB-Lüfter und die 4 RGB-LEDs, nicht ordnungsgemäß funktionieren, da diese Komponenten die Installation von Softwarepaketen des Pironman 5 erfordern.


.. note::

    Das Batocera.linux-System ist jetzt vollständig kompatibel mit dem Pironman 5. Batocera.linux ist eine Open-Source- und vollständig kostenlose Retro-Gaming-Distribution.

    * :ref:`install_batocera`
    * :ref:`set_up_batocera`

Wie steuert man die Komponenten mit dem Befehl ``pironman5``?
----------------------------------------------------------------------
Sie können dem folgenden Tutorial folgen, um die Komponenten des Pironman 5 mit dem Befehl ``pironman5`` zu steuern.

* :ref:`view_control_commands`

Wie ändert man die Bootreihenfolge des Raspberry Pi per Befehl?
------------------------------------------------------------------

Wenn Sie bereits bei Ihrem Raspberry Pi angemeldet sind, können Sie die Bootreihenfolge über Befehle ändern. Detaillierte Anweisungen finden Sie hier:

* :ref:`configure_boot_ssd`


Wie kann man die Bootreihenfolge mit dem Raspberry Pi Imager ändern?
-------------------------------------------------------------------------

Zusätzlich zur Änderung der ``BOOT_ORDER`` in der EEPROM-Konfiguration können Sie auch den **Raspberry Pi Imager** verwenden, um die Bootreihenfolge Ihres Raspberry Pi zu ändern.

Es wird empfohlen, für diesen Schritt eine Ersatzkarte zu verwenden.

* :ref:`update_bootloader`

Wie kopiert man das System von der SD-Karte auf eine NVMe-SSD?
-----------------------------------------------------------------

Wenn Sie eine NVMe-SSD haben, aber keinen Adapter, um Ihre NVMe mit Ihrem Computer zu verbinden, können Sie das System zunächst auf Ihrer Micro-SD-Karte installieren. Sobald der Pironman 5 erfolgreich gestartet ist, können Sie das System von Ihrer Micro-SD-Karte auf Ihre NVMe-SSD kopieren. Detaillierte Anweisungen finden Sie hier:

* :ref:`copy_sd_to_nvme_rpi`


OLED-Display funktioniert nicht?
--------------------------------------

Wenn das OLED-Display nicht funktioniert oder fehlerhaft anzeigt, können Sie die folgenden Schritte befolgen, um das Problem zu beheben:

Überprüfen Sie, ob das FPC-Kabel des OLED-Displays richtig angeschlossen ist.

#. Verwenden Sie den folgenden Befehl, um die Protokolle des Programms anzuzeigen und nach Fehlermeldungen zu suchen.

   .. code-block:: shell

      cat /opt/pironman5/log

#. Alternativ können Sie den folgenden Befehl verwenden, um zu überprüfen, ob die i2c-Adresse des OLEDs 0x3C erkannt wird:

   .. code-block:: shell
        
        sudo i2cdetect -y 1

#. Wenn die ersten beiden Schritte keine Probleme aufzeigen, versuchen Sie, den pironman5-Dienst neu zu starten, um zu sehen, ob das Problem dadurch behoben wird.

   .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _openssh_powershell:

OpenSSH über PowerShell installieren
-----------------------------------------

Wenn Sie versuchen, sich über den Befehl ``ssh <Benutzername>@<Hostname>.local`` (oder ``ssh <Benutzername>@<IP-Adresse>``) mit Ihrem Raspberry Pi zu verbinden und die folgende Fehlermeldung erscheint:

    .. code-block::

        ssh: Der Begriff 'ssh' wurde nicht als Name eines Cmdlets, einer Funktion, einer Skriptdatei oder eines ausführbaren Programms erkannt. Überprüfen Sie die Schreibweise des Namens, oder ob der Pfad korrekt angegeben wurde, und versuchen Sie es erneut.

Dies bedeutet, dass Ihr Betriebssystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Sie müssen es daher manuell installieren, indem Sie dem folgenden Tutorial folgen.

#. Geben Sie ``powershell`` in die Suchleiste auf Ihrem Windows-Desktop ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im erscheinenden Menü ``Als Administrator ausführen``.

   .. image:: img/powershell_ssh.png
      :width: 90%

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

#. Es wird Ihnen angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Wenn die obige Meldung nicht erscheint, bedeutet dies, dass Ihr Windows-System immer noch zu alt ist. In diesem Fall wird empfohlen, ein Drittanbieter-SSH-Tool wie |link_putty| zu installieren.

#. Starten Sie PowerShell neu und führen Sie es weiterhin als Administrator aus. Sie sollten nun in der Lage sein, sich mit dem Befehl ``ssh`` bei Ihrem Raspberry Pi anzumelden. Es wird Ihnen aufgefordert, das zuvor eingerichtete Passwort einzugeben.

   .. image:: img/powershell_login.png
