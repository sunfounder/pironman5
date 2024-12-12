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

1. Über kompatible Systeme
-------------------------------

Systeme, die den Test auf dem Raspberry Pi 5 bestanden haben:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Über die Ein-/Aus-Taste
--------------------------

Die Ein-/Aus-Taste führt die Funktion der Ein-/Aus-Taste des Raspberry Pi 5 aus und funktioniert genauso wie diese.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Herunterfahren**

  * Wenn Sie das Raspberry Pi **Bookworm Desktop**-System verwenden, können Sie die Ein-/Aus-Taste zweimal schnell hintereinander drücken, um herunterzufahren. 
  * Wenn Sie das Raspberry Pi **Bookworm Lite**-System verwenden, drücken Sie die Ein-/Aus-Taste einmal, um das Herunterfahren einzuleiten.
  * Für einen erzwungenen Neustart halten Sie die Ein-/Aus-Taste gedrückt.

* **Einschalten**

  * Wenn das Raspberry Pi-Board heruntergefahren, aber noch mit Strom versorgt ist, drücken Sie die Taste einmal, um es einzuschalten.

* Wenn Sie ein System verwenden, das keine Ausschaltfunktion unterstützt, können Sie die Taste 5 Sekunden lang gedrückt halten, um einen erzwungenen Neustart durchzuführen, und einmal drücken, um das Gerät aus dem ausgeschalteten Zustand einzuschalten.

3. Über die Luftstromrichtung
-------------------------------

Der Luftstrom im Pironman 5-Gehäuse ist sorgfältig optimiert, um die Kühlungseffizienz zu maximieren. Kühle Luft gelangt hauptsächlich durch die GPIO-Schnittstelle und andere kleine Öffnungen ins Gehäuse, um eine gleichmäßige Zirkulation zu gewährleisten. Danach wird sie durch den Tool Cooler geleitet, der mit einem Hochleistungslüfter die internen Temperaturen reguliert, und schließlich durch die beiden RGB-Lüfter an der Seitenwand abgeführt.

Für eine detaillierte Demonstration sehen Sie sich bitte das Video an:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Ihr Browser unterstützt das Video-Tag nicht.
        </video>
    </div>

4. Unterstützt der Pironman 5 Retro-Gaming-Systeme?
------------------------------------------------------

Ja, er ist kompatibel. Die meisten Retro-Gaming-Systeme sind jedoch optimierte Versionen, die keine zusätzliche Software installieren und ausführen können. Diese Einschränkung kann dazu führen, dass einige Komponenten des Pironman 5, wie das OLED-Display, die beiden RGB-Lüfter und die 4 RGB-LEDs, nicht richtig funktionieren, da diese Komponenten die Installation der Softwarepakete des Pironman 5 erfordern.

.. note::

   Das Batocera.linux-System ist jetzt vollständig kompatibel mit dem Pironman 5. Batocera.linux ist eine Open-Source- und völlig kostenlose Retro-Gaming-Distribution.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

5. OLED-Bildschirm funktioniert nicht?
---------------------------------------

Wenn der OLED-Bildschirm nicht angezeigt wird oder fehlerhaft angezeigt wird, führen Sie die folgenden Schritte zur Fehlerbehebung durch:

#. Stellen Sie sicher, dass das FPC-Kabel des OLED-Bildschirms sicher angeschlossen ist. Es wird empfohlen, den OLED-Bildschirm neu zu verbinden und das Gerät dann einzuschalten.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

#. Überprüfen Sie, ob der Raspberry Pi ein kompatibles Betriebssystem verwendet. Der Pironman 5 unterstützt nur die folgenden Systeme:  

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Wenn Sie ein nicht unterstütztes System installiert haben, folgen Sie der Anleitung, um ein kompatibles Betriebssystem zu installieren: :ref:`install_the_os`.

#. Wenn der OLED-Bildschirm zum ersten Mal eingeschaltet wird, kann er nur Pixelblöcke anzeigen. Sie müssen den Anweisungen in :ref:`set_up_pironman5` folgen, um die Konfiguration abzuschließen, bevor er ordnungsgemäße Informationen anzeigen kann.

#. Verwenden Sie den folgenden Befehl, um zu prüfen, ob die I2C-Adresse ``0x3C`` des OLEDs erkannt wird:  

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Wenn die I2C-Adresse ``0x3C`` erkannt wird, starten Sie den Pironman 5-Dienst mit diesem Befehl neu:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Aktivieren Sie I2C, wenn die Adresse nicht erkannt wird:

     * Bearbeiten Sie die Konfigurationsdatei mit folgendem Befehl:

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Fügen Sie folgende Zeile am Ende der Datei hinzu:

       .. code-block:: shell


         dtparam=i2c_arm=on

     * Speichern Sie die Datei mit ``Ctrl+X``, dann ``Y`` und schließen Sie. Starten Sie den Pironman 5 neu und prüfen Sie, ob das Problem behoben ist.

Wenn das Problem nach Durchführung der obigen Schritte weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

6. NVMe PIP-Modul funktioniert nicht?
---------------------------------------

1. Stellen Sie sicher, dass das FPC-Kabel, das das NVMe PIP-Modul mit dem Raspberry Pi 5 verbindet, sicher angeschlossen ist.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

2. Überprüfen Sie, ob Ihre SSD ordnungsgemäß am NVMe PIP-Modul befestigt ist.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

3. Prüfen Sie den Status der LEDs des NVMe PIP-Moduls:

   Nachdem alle Verbindungen bestätigt wurden, schalten Sie den Pironman 5 ein und beobachten Sie die beiden Anzeigen am NVMe PIP-Modul:  

   * **PWR LED**: Sollte leuchten.  
   * **STA LED**: Sollte blinken, um den normalen Betrieb anzuzeigen.  

   .. image:: img/nvme_pip_leds.png  

   * Wenn die **PWR LED** leuchtet, die **STA LED** jedoch nicht blinkt, bedeutet dies, dass die NVMe SSD vom Raspberry Pi nicht erkannt wird.  
   * Wenn die **PWR LED** aus ist, überbrücken Sie die "Force Enable"-Pins (J4) am Modul. Wenn die **PWR LED** leuchtet, könnte dies auf ein loses FPC-Kabel oder eine nicht unterstützte Systemkonfiguration für NVMe hinweisen.

     .. image:: img/nvme_pip_j4.png  

4. Stellen Sie sicher, dass auf Ihrer NVMe SSD ein Betriebssystem ordnungsgemäß installiert ist. Siehe: :ref:`install_the_os`.

5. Wenn die Verkabelung korrekt ist und das Betriebssystem installiert wurde, die NVMe SSD jedoch weiterhin nicht bootet, versuchen Sie, von einer Micro-SD-Karte zu booten, um die Funktionalität anderer Komponenten zu überprüfen. Sobald dies bestätigt ist, fahren Sie fort mit: :ref:`configure_boot_ssd`.

Wenn das Problem nach Durchführung der obigen Schritte weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

7. RGB-LEDs funktionieren nicht?
---------------------------------

#. Die beiden Pins auf dem IO-Expander oberhalb von J9 werden verwendet, um die RGB-LEDs mit GPIO10 zu verbinden. Stellen Sie sicher, dass die Jumperkappe auf diesen beiden Pins ordnungsgemäß angebracht ist.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Überprüfen Sie, ob der Raspberry Pi ein kompatibles Betriebssystem verwendet. Der Pironman 5 unterstützt nur die folgenden Betriebssysteme:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Wenn Sie ein nicht unterstütztes Betriebssystem installiert haben, folgen Sie der Anleitung, um ein kompatibles Betriebssystem zu installieren: :ref:`install_the_os`.

#. Führen Sie den Befehl ``sudo raspi-config`` aus, um das Konfigurationsmenü zu öffnen. Navigieren Sie zu **3 Interfacing Options** -> **I3 SPI** -> **YES**, klicken Sie dann auf **OK** und **Finish**, um SPI zu aktivieren. Starten Sie den Pironman 5 nach der Aktivierung von SPI neu.

Wenn das Problem nach Durchführung der oben genannten Schritte weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

8. Wie deaktiviert man das Web-Dashboard?
------------------------------------------

Sobald Sie die Installation des Moduls ``pironman5`` abgeschlossen haben, können Sie auf das :ref:`view_control_dashboard` zugreifen.

Wenn Sie diese Funktion nicht benötigen und die CPU- und RAM-Auslastung reduzieren möchten, können Sie das Dashboard während der Installation von ``pironman5`` deaktivieren, indem Sie das Flag ``--disable-dashboard`` hinzufügen.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Wenn Sie ``pironman5`` bereits installiert haben, können Sie das Modul ``dashboard`` und ``influxdb`` entfernen und anschließend ``pironman5`` neu starten, um die Änderungen zu übernehmen:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

9. Wie steuert man Komponenten mit dem ``pironman5``-Befehl?
-------------------------------------------------------------

Sie können dem folgenden Tutorial folgen, um die Komponenten des Pironman 5 mit dem Befehl ``pironman5`` zu steuern.

* :ref:`view_control_commands`

10. Wie ändert man die Boot-Reihenfolge des Raspberry Pi mit Befehlen?
----------------------------------------------------------------------

Wenn Sie bereits bei Ihrem Raspberry Pi angemeldet sind, können Sie die Boot-Reihenfolge mit Befehlen ändern. Detaillierte Anweisungen finden Sie hier:

* :ref:`configure_boot_ssd`

11. Wie ändert man die Boot-Reihenfolge mit dem Raspberry Pi Imager?
-----------------------------------------------------------------------

Zusätzlich zur Änderung der ``BOOT_ORDER`` in der EEPROM-Konfiguration können Sie auch den **Raspberry Pi Imager** verwenden, um die Boot-Reihenfolge Ihres Raspberry Pi zu ändern.

Es wird empfohlen, für diesen Schritt eine Ersatzkarte zu verwenden.

* :ref:`update_bootloader`

12. Wie kopiert man das System von der SD-Karte auf eine NVMe SSD?
-------------------------------------------------------------------

Wenn Sie eine NVMe SSD haben, jedoch keinen Adapter, um diese mit Ihrem Computer zu verbinden, können Sie das System zunächst auf Ihrer Micro-SD-Karte installieren. Sobald der Pironman 5 erfolgreich gestartet ist, können Sie das System von Ihrer Micro-SD-Karte auf Ihre NVMe SSD kopieren. Detaillierte Anweisungen finden Sie hier:

* :ref:`copy_sd_to_nvme_rpi`

13. Wie entfernt man die Schutzfolie von den Acrylplatten?
------------------------------------------------------------

Im Lieferumfang sind zwei Acrylplatten enthalten, die auf beiden Seiten mit einer gelben/transparente Schutzfolie bedeckt sind, um Kratzer zu vermeiden. Die Schutzfolie kann etwas schwer zu entfernen sein. Verwenden Sie einen Schraubendreher, um die Ecken vorsichtig abzukratzen, und ziehen Sie dann die gesamte Folie ab.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

14. Wie installiert man OpenSSH über PowerShell?
--------------------------------------------------

Wenn Sie den Befehl ``ssh <Benutzername>@<Hostname>.local`` (oder ``ssh <Benutzername>@<IP-Adresse>``) verwenden, um eine Verbindung zu Ihrem Raspberry Pi herzustellen, aber die folgende Fehlermeldung angezeigt wird:

    .. code-block::

        ssh: Der Begriff 'ssh' wird nicht als Name eines Cmdlets, einer Funktion, einer Skriptdatei oder eines ausführbaren Programms erkannt. Überprüfen Sie die Schreibweise des Namens oder ob der Pfad korrekt ist, und versuchen Sie es erneut.

Dies bedeutet, dass Ihr Computersystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Sie müssen es manuell installieren, indem Sie dem folgenden Tutorial folgen:

#. Geben Sie ``powershell`` in das Suchfeld auf Ihrem Windows-Desktop ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im angezeigten Menü die Option ``Als Administrator ausführen``.

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

#. Es wird nun angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Wenn die obige Aufforderung nicht angezeigt wird, bedeutet dies, dass Ihr Windows-System immer noch zu alt ist. In diesem Fall wird empfohlen, ein Drittanbieter-SSH-Tool wie |link_putty| zu installieren.

#. Starten Sie PowerShell jetzt neu und führen Sie es weiterhin als Administrator aus. An diesem Punkt können Sie sich mit dem Befehl ``ssh`` bei Ihrem Raspberry Pi anmelden, wobei Sie aufgefordert werden, das zuvor eingerichtete Passwort einzugeben.

   .. image:: img/powershell_login.png

