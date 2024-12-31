.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in Raspberry Pi, Arduino und ESP32 ein.

    **Warum mitmachen?**

    - **Experten-Support**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugriff auf Produktankündigungen und Vorschauen.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

FAQ
============

1. Über kompatible Systeme
-----------------------------

Systeme, die auf dem Raspberry Pi 5 getestet wurden:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Über den Netzschalter
---------------------------

Der Netzschalter des Pironman 5 funktioniert wie der Netzschalter des Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Herunterfahren**

  * Beim Betrieb des Raspberry Pi **Bookworm Desktop**-Systems können Sie den Netzschalter zweimal schnell hintereinander drücken, um das Gerät herunterzufahren.
  * Beim Betrieb des Raspberry Pi **Bookworm Lite**-Systems drücken Sie den Netzschalter einmal, um das Gerät herunterzufahren.
  * Für einen erzwungenen Shutdown halten Sie den Netzschalter gedrückt.

* **Einschalten**

  * Wenn das Raspberry Pi-Board heruntergefahren, aber noch mit Strom versorgt ist, drücken Sie den Netzschalter einmal, um es einzuschalten.

* Wenn Ihr System keinen Shutdown-Knopf unterstützt, halten Sie den Knopf 5 Sekunden lang gedrückt, um einen erzwungenen Shutdown durchzuführen, und drücken Sie einmal, um es aus dem ausgeschalteten Zustand einzuschalten.

3. Über die Luftstromrichtung
--------------------------------

Der Luftstrom im Pironman 5-Gehäuse ist sorgfältig ausgelegt, um die Kühlleistung zu maximieren. Kühle Luft tritt hauptsächlich über die GPIO-Schnittstelle und andere kleine Öffnungen ein und wird durch den Tool Cooler mit einem Hochleistungsventilator geregelt, bevor sie durch die zwei RGB-Lüfter an der Seitenwand ausgestoßen wird.

Für eine detaillierte Demonstration siehe Video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Ihr Browser unterstützt das Video-Tag nicht.
        </video>
    </div>

4. Über die Kupferrohrenden des Tower Coolers
---------------------------------------------

Die U-förmigen Wärmerohre oben am Tower Cooler sind gepresst, damit die Kupferrohre durch die Aluminiumlamellen passen – ein normaler Produktionsprozess.

   .. image:: img/tower_cooler1.png

5. Unterstützt der Pironman 5 Retro-Gaming-Systeme?
---------------------------------------------------

Ja, er ist kompatibel. Allerdings können die meisten Retro-Gaming-Systeme keine zusätzliche Software installieren und ausführen. Diese Einschränkung kann dazu führen, dass einige Komponenten des Pironman 5, wie das OLED-Display, die zwei RGB-Lüfter und die vier RGB-LEDs, nicht ordnungsgemäß funktionieren, da diese Komponenten die Installation der Softwarepakete des Pironman 5 erfordern.

.. note::

   Das System Batocera.linux ist jetzt vollständig kompatibel mit dem Pironman 5. Batocera.linux ist eine Open-Source- und völlig kostenlose Retro-Gaming-Distribution.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

6. OLED-Bildschirm funktioniert nicht?
----------------------------------------

Wenn der OLED-Bildschirm nicht anzeigt oder fehlerhaft anzeigt, führen Sie folgende Schritte aus:

#. Stellen Sie sicher, dass das FPC-Kabel des OLED-Bildschirms sicher angeschlossen ist. Es wird empfohlen, den Bildschirm neu zu verbinden und das Gerät dann einzuschalten.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

#. Bestätigen Sie, dass das Raspberry Pi ein kompatibles Betriebssystem ausführt. Unterstützte Systeme sind in :ref:`install_the_os` beschrieben.

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Wenn Sie ein nicht unterstütztes System installiert haben, folgen Sie der Anleitung, um ein kompatibles Betriebssystem zu installieren: :ref:`install_the_os`.

#. Wenn der OLED-Bildschirm zum ersten Mal eingeschaltet wird, kann er nur Pixelblöcke anzeigen. Sie müssen den Anweisungen in :ref:`set_up_pironman5` folgen, um die Konfiguration abzuschließen, bevor er ordnungsgemäße Informationen anzeigen kann.

#. Verwenden Sie den folgenden Befehl, um die I2C-Adresse ``0x3C`` zu prüfen:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Falls erkannt, starten Sie den Dienst mit folgendem Befehl neu:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Aktivieren Sie I2C, falls die Adresse nicht erkannt wird:
     * Bearbeiten Sie die Konfigurationsdatei mit folgendem Befehl:

     .. code-block:: shell

         sudo nano /boot/firmware/config.txt
         
     * Fügen Sie folgende Zeile am Ende der Datei hinzu:

       .. code-block:: shell


         dtparam=i2c_arm=on

     * Speichern Sie die Datei mit ``Ctrl+X``, dann ``Y`` und schließen Sie. Starten Sie den Pironman 5 neu und prüfen Sie, ob das Problem behoben ist.

#. Wenn das Problem weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com.

7. NVMe PIP-Modul funktioniert nicht?
----------------------------------------

1. Stellen Sie sicher, dass das FPC-Kabel, das das NVMe PIP-Modul mit dem Raspberry Pi 5 verbindet, sicher befestigt ist.

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

3. Überprüfen Sie den Status der LEDs des NVMe PIP-Moduls:

   Nach dem Bestätigen aller Verbindungen schalten Sie den Pironman 5 ein und beobachten Sie die beiden Anzeigen auf dem NVMe PIP-Modul:

   * **PWR-LED**: Sollte leuchten.  
   * **STA-LED**: Sollte blinken, um einen normalen Betrieb anzuzeigen.  

   .. image:: img/nvme_pip_leds.png  

   * Wenn die **PWR-LED** leuchtet, aber die **STA-LED** nicht blinkt, bedeutet dies, dass die NVMe-SSD nicht vom Raspberry Pi erkannt wird.  
   * Wenn die **PWR-LED** nicht leuchtet, überbrücken Sie die "Force Enable"-Pins (J4) auf dem Modul. Wenn die **PWR-LED** aufleuchtet, könnte dies auf ein loses FPC-Kabel oder eine nicht unterstützte Systemkonfiguration für NVMe hinweisen.

     .. image:: img/nvme_pip_j4.png  

4. Vergewissern Sie sich, dass Ihr NVMe-SSD ein ordnungsgemäß installiertes Betriebssystem hat. Siehe: :ref:`install_the_os`.

5. Wenn die Verkabelung korrekt ist und das Betriebssystem installiert ist, die NVMe-SSD jedoch weiterhin nicht bootet, versuchen Sie, von einer Micro-SD-Karte zu booten, um die Funktionalität anderer Komponenten zu überprüfen. Fahren Sie anschließend fort mit: :ref:`configure_boot_ssd`.

Wenn das Problem nach Durchführung der oben genannten Schritte weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

8. RGB-LEDs funktionieren nicht?
-----------------------------------

#. Die beiden Pins auf dem IO-Expander oberhalb von J9 werden verwendet, um die RGB-LEDs mit GPIO10 zu verbinden. Stellen Sie sicher, dass die Jumperkappe auf diesen beiden Pins korrekt angebracht ist.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Vergewissern Sie sich, dass der Raspberry Pi ein kompatibles Betriebssystem verwendet. Der Pironman 5 unterstützt nur die folgenden OS-Versionen:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Wenn Sie ein nicht unterstütztes Betriebssystem installiert haben, folgen Sie der Anleitung, um ein kompatibles Betriebssystem zu installieren: :ref:`install_the_os`.

#. Führen Sie den Befehl ``sudo raspi-config`` aus, um das Konfigurationsmenü zu öffnen. Navigieren Sie zu **3 Interfacing Options** -> **I3 SPI** -> **YES**, klicken Sie dann auf **OK** und **Finish**, um SPI zu aktivieren. Starten Sie nach der Aktivierung von SPI den Pironman 5 neu.

Wenn das Problem nach Durchführung der oben genannten Schritte weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

9. CPU-Lüfter funktioniert nicht?
----------------------------------

Wenn die CPU-Temperatur nicht den festgelegten Schwellenwert erreicht hat, funktioniert der CPU-Lüfter nicht.

**Lüfterdrehzahlregelung basierend auf der Temperatur**  

Der PWM-Lüfter arbeitet dynamisch und passt seine Drehzahl entsprechend der Temperatur des Raspberry Pi 5 an:  

* **Unter 50 °C**: Lüfter bleibt aus (0 % Geschwindigkeit).  
* **Bei 50 °C**: Lüfter arbeitet mit niedriger Geschwindigkeit (30 % Geschwindigkeit).  
* **Bei 60 °C**: Lüfter erhöht auf mittlere Geschwindigkeit (50 % Geschwindigkeit).  
* **Bei 67,5 °C**: Lüfter beschleunigt auf hohe Geschwindigkeit (70 % Geschwindigkeit).  
* **Bei 75 °C und darüber**: Lüfter arbeitet mit voller Geschwindigkeit (100 % Geschwindigkeit).  

Weitere Details finden Sie unter: :ref:`Fans`.

10. Wie kann ich das Web-Dashboard deaktivieren?
----------------------------------------------------

Sobald Sie die Installation des Moduls ``pironman5`` abgeschlossen haben, können Sie auf das :ref:`view_control_dashboard` zugreifen.

Wenn Sie diese Funktion nicht benötigen und die CPU- und RAM-Nutzung reduzieren möchten, können Sie das Dashboard während der Installation von ``pironman5`` deaktivieren, indem Sie die Option ``--disable-dashboard`` hinzufügen.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Wenn Sie ``pironman5`` bereits installiert haben, können Sie das Modul ``dashboard`` und ``influxdb`` entfernen und anschließend ``pironman5`` neu starten, um die Änderungen anzuwenden:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

11. Wie kann ich Komponenten mit dem Befehl ``pironman5`` steuern?
---------------------------------------------------------------------

Eine Anleitung zur Steuerung der Komponenten des Pironman 5 mit dem Befehl ``pironman5`` finden Sie hier:

* :ref:`view_control_commands`

12. Wie kann ich die Bootreihenfolge des Raspberry Pi mit Befehlen ändern?
-----------------------------------------------------------------------------

Wenn Sie bereits auf Ihrem Raspberry Pi eingeloggt sind, können Sie die Bootreihenfolge mithilfe von Befehlen ändern. Detaillierte Anweisungen finden Sie hier:

* :ref:`configure_boot_ssd`

13. Wie kann ich die Bootreihenfolge mit dem Raspberry Pi Imager ändern?
----------------------------------------------------------------------------

Zusätzlich zur Änderung des ``BOOT_ORDER`` in der EEPROM-Konfiguration können Sie auch den **Raspberry Pi Imager** verwenden, um die Bootreihenfolge Ihres Raspberry Pi zu ändern.

Es wird empfohlen, für diesen Schritt eine Ersatzkarte zu verwenden.

* :ref:`update_bootloader`

14. Wie kopiere ich das System von der SD-Karte auf eine NVMe-SSD?
-------------------------------------------------------------------

Wenn Sie eine NVMe-SSD haben, aber keinen Adapter, um Ihre NVMe mit Ihrem Computer zu verbinden, können Sie das System zuerst auf Ihrer Micro-SD-Karte installieren. Sobald der Pironman 5 erfolgreich hochgefahren ist, können Sie das System von Ihrer Micro-SD-Karte auf Ihre NVMe-SSD kopieren. Detaillierte Anweisungen finden Sie hier:

* :ref:`copy_sd_to_nvme_rpi`

15. Wie entferne ich die Schutzfolie von den Acrylplatten?
-------------------------------------------------------------

Im Lieferumfang sind zwei Acrylplatten enthalten, die auf beiden Seiten mit einer gelben/transparente Schutzfolie überzogen sind, um Kratzer zu vermeiden. Die Schutzfolie lässt sich möglicherweise schwer entfernen. Verwenden Sie einen Schraubendreher, um vorsichtig an den Ecken zu kratzen, und ziehen Sie dann die gesamte Folie vorsichtig ab.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

16. Wie installiert man OpenSSH über PowerShell?
----------------------------------------------------

Wenn Sie den Befehl ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP-Adresse>``) verwenden, um eine Verbindung zu Ihrem Raspberry Pi herzustellen, aber die folgende Fehlermeldung angezeigt wird:

    .. code-block::

        ssh: Der Begriff 'ssh' ist nicht als Name eines Cmdlets, einer Funktion, einer Skriptdatei oder eines ausführbaren Programms erkannt. Überprüfen Sie die Schreibweise des Namens, oder wenn ein Pfad angegeben wurde, stellen Sie sicher, dass der Pfad korrekt ist, und versuchen Sie es erneut.

Bedeutet dies, dass Ihr Computersystem veraltet ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Folgen Sie der untenstehenden Anleitung, um es manuell zu installieren.

#. Geben Sie ``powershell`` in die Suchleiste Ihres Windows-Desktops ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im angezeigten Menü ``Als Administrator ausführen`` aus.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Verwenden Sie den folgenden Befehl, um ``OpenSSH.Client`` zu installieren.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach der Installation wird die folgende Ausgabe angezeigt.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Überprüfen Sie die Installation mit folgendem Befehl.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Es wird angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning::
        Wenn die obige Meldung nicht erscheint, bedeutet dies, dass Ihr Windows-System immer noch zu alt ist. Es wird empfohlen, ein Drittanbieter-SSH-Tool wie |link_putty| zu installieren.

#. Starten Sie PowerShell neu und führen Sie es erneut als Administrator aus. An diesem Punkt können Sie sich mit dem Befehl ``ssh`` bei Ihrem Raspberry Pi anmelden. Sie werden aufgefordert, das zuvor festgelegte Passwort einzugeben.

   .. image:: img/powershell_login.png

17. Wie schaltet man das OLED-Display EIN/AUS?
--------------------------------------------------

Sie können das OLED-Display über das Dashboard oder die Kommandozeile ein- oder ausschalten.

1. OLED-Display über das Dashboard ein-/ausschalten.

   .. note::

    Bevor Sie das Dashboard verwenden, müssen Sie es in Home Assistant einrichten. Weitere Informationen finden Sie unter: :ref:`view_control_dashboard`.

- Nach der Einrichtung können Sie die folgenden Schritte ausführen, um das OLED-Display ein-/auszuschalten oder zu konfigurieren.

   .. image:: img/set_up_on_dashboard.jpg
      :width: 90%

2. OLED-Display über die Kommandozeile ein-/ausschalten.

- Verwenden Sie den folgenden Befehl, um das OLED-Display ein- oder auszuschalten.

.. code-block::

    sudo pironman5 -oe on/off

.. note::

    Möglicherweise müssen Sie den Dienst pironman5 neu starten, damit die Änderungen wirksam werden. Verwenden Sie den folgenden Befehl, um den Dienst neu zu starten:

      .. code-block::

        sudo systemctl restart pironman5.service
