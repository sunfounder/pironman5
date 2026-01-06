.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie zusammen mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

FAQ
============

1. Über kompatible Systeme
-------------------------------

Die auf dem Raspberry Pi 5 getesteten Systeme:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Über die Einschalttaste
----------------------------

Die Einschalttaste des Pironman 5 entspricht der Einschalttaste des Raspberry Pi 5 und funktioniert auf die gleiche Weise.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Herunterfahren**

  * Bei Verwendung des **Raspberry Pi OS Desktop**-Systems können Sie die Einschalttaste zweimal schnell hintereinander drücken, um das Gerät herunterzufahren.
  * Bei Verwendung des **Raspberry Pi OS Lite**-Systems reicht ein einmaliges Drücken der Einschalttaste aus, um das Herunterfahren zu starten.
  * Für ein erzwungenes Herunterfahren halten Sie die Einschalttaste gedrückt.

* **Einschalten**

  * Wenn das Raspberry Pi-Board heruntergefahren, aber noch mit Strom versorgt ist, können Sie durch einmaliges Drücken die Stromversorgung wieder aktivieren.

* Bei Systemen, die keine Herunterfahrfunktion unterstützen, können Sie die Taste 5 Sekunden lang gedrückt halten, um ein erzwungenes Herunterfahren durchzuführen, und durch einmaliges Drücken das Gerät wieder einschalten.

3. Über die Luftstromrichtung
--------------------------------

Der Luftstrom im Pironman 5-Gehäuse ist sorgfältig gestaltet, um die Kühleffizienz zu maximieren. Kühle Luft tritt hauptsächlich durch die GPIO-Schnittstelle und andere kleine Öffnungen in das Gehäuse ein, um einen gleichmäßigen Lufteinlass zu gewährleisten. Anschließend durchströmt die Luft den Tower Cooler mit einem Hochleistungslüfter zur Temperaturregulierung und wird schließlich durch die beiden RGB-Lüfter an der Seitenwand abgeführt.

Eine detaillierte Demonstration finden Sie im folgenden Video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

4. Über den Tower-Kühler
----------------------------------------------------------

#. Die U-förmigen Heatpipes an der Oberseite des Tower-Kühlers sind gepresst, um das Durchführen der Kupferrohre durch die Aluminiumlamellen zu erleichtern. Dies ist ein normaler Bestandteil des Herstellungsprozesses für Kupferrohre.

   .. image::  img/tower_cooler1.png

#. Wichtige Hinweise zur Installation eines Tower-Kühlers:

**Pads anbringen**: Vor der Installation des Tower-Kühlers sollten Pads auf dem Raspberry Pi angebracht werden, um Schäden oder Kratzer zu vermeiden.

 .. image::  img/tower_cooler_thermal.png

**Richtige Ausrichtung**: Achte auf die korrekte Platzierung des Tower-Kühlers. Richte ihn an den Positionierungslöchern des Raspberry Pi aus, bevor du die Federschrauben festziehst.

 .. image::  img/tower_cooler_place.jpg

**Vorsicht beim Entfernen**: Falls der Tower-Kühler falsch ausgerichtet installiert wurde oder die Pads nicht angebracht wurden, darf er nicht mit Gewalt entfernt werden.

- Um den Tower-Kühler sicher zu entfernen, folge diesen Schritten:

  Greife die Spitze der Feder-Mutter mit einer Pinzette oder Zange und drücke sie vorsichtig nach oben, um sie zu lösen.

     .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/remove_tower_cooler.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

5. Über den Raspberry Pi AI HAT+
----------------------------------------------------------

Der Raspberry Pi AI HAT+ ist nicht mit dem Pironman 5 kompatibel.

   .. image::  img/output3.png
        :width: 400

Das Raspberry Pi AI Kit kombiniert den Raspberry Pi M.2 HAT+ und das Hailo AI-Beschleunigermodul.

   .. image::  img/output2.jpg
        :width: 400

Sie können das Hailo AI-Beschleunigermodul vom Raspberry Pi AI Kit abnehmen und direkt in das NVMe PIP-Modul des Pironman 5 einsetzen.

   .. image::  img/output4.png
        :width: 800

6. PI5 startet nicht (rote LED)?
-------------------------------------------

Dieses Problem kann durch ein Systemupdate, Änderungen der Bootreihenfolge oder einen beschädigten Bootloader verursacht werden. Sie können die folgenden Schritte ausprobieren, um das Problem zu lösen:

#. Überprüfen Sie die USB-HDMI-Adapter-Verbindung

   * Bitte überprüfen Sie sorgfältig, ob der USB-HDMI-Adapter korrekt mit dem PI5 verbunden ist.
   * Versuchen Sie, den USB-HDMI-Adapter zu entfernen und erneut anzuschließen.
   * Schließen Sie dann die Stromversorgung wieder an und prüfen Sie, ob der PI5 erfolgreich startet.

#. Testen Sie den PI5 außerhalb des Gehäuses

   * Wenn das erneute Anschließen des Adapters das Problem nicht löst:
   * Entfernen Sie den PI5 aus dem Pironman 5 Gehäuse.
   * Versorgen Sie den PI5 direkt mit dem Netzteil (ohne das Gehäuse).
   * Überprüfen Sie, ob er normal starten kann.

#. Bootloader wiederherstellen

   * Wenn der PI5 immer noch nicht startet, ist möglicherweise der Bootloader beschädigt. Sie können dieser Anleitung folgen: :ref:`update_bootloader_5` und wählen, ob vom SD-Karte oder NVMe/USB gebootet werden soll.
   * Legen Sie die vorbereitete SD-Karte in den PI5 ein, schalten Sie ihn ein und warten Sie mindestens 10 Sekunden. Sobald die Wiederherstellung abgeschlossen ist, entfernen und formatieren Sie die SD-Karte erneut. 
   * Verwenden Sie dann Raspberry Pi Imager, um das neueste Raspberry Pi OS auf die SD-Karte zu flashen, setzen Sie die Karte wieder ein und versuchen Sie erneut zu starten.

.. 6. Unterstützt der Pironman 5 Retro-Gaming-Systeme?
.. ------------------------------------------------------

.. Ja, er ist kompatibel. Allerdings sind die meisten Retro-Gaming-Systeme abgespeckte Versionen, die keine zusätzlichen Softwarepakete installieren und ausführen können. Dies kann dazu führen, dass einige Komponenten des Pironman 5, wie das OLED-Display, die beiden RGB-Lüfter und die 4 RGB-LEDs, nicht ordnungsgemäß funktionieren, da sie die Installation der Softwarepakete des Pironman 5 erfordern.

.. .. note::

..    Das Batocera.linux-System ist jetzt vollständig kompatibel mit dem Pironman 5. Batocera.linux ist eine Open-Source- und vollständig kostenlose Retro-Gaming-Distribution.

..    * :ref:`install_batocera`
..    * :ref:`set_up_batocera`

7. OLED-Bildschirm funktioniert nicht?
--------------------------------------------

Wenn der OLED-Bildschirm nichts anzeigt oder fehlerhaft angezeigt wird, führen Sie die folgenden Schritte zur Fehlerbehebung aus:

#. Vergewissern Sie sich, dass das FPC-Kabel des OLED-Bildschirms sicher angeschlossen ist. Es wird empfohlen, den OLED-Bildschirm erneut anzuschließen und das Gerät anschließend einzuschalten.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Bestätigen Sie, dass das Raspberry Pi ein kompatibles Betriebssystem verwendet. Der Pironman 5 unterstützt nur die folgenden Systeme:  

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Wenn Sie ein nicht unterstütztes System installiert haben, folgen Sie der Anleitung zur Installation eines kompatiblen Betriebssystems: :ref:`install_the_os_5`.

#. Beim ersten Einschalten des OLED-Bildschirms werden möglicherweise nur Pixelblöcke angezeigt. Folgen Sie den Anweisungen in :ref:`set_up_pironman5`, um die Konfiguration abzuschließen, damit der Bildschirm die korrekten Informationen anzeigt.

#. Verwenden Sie den folgenden Befehl, um zu überprüfen, ob die I2C-Adresse ``0x3C`` des OLED-Bildschirms erkannt wird:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Wenn die I2C-Adresse ``0x3C`` erkannt wird, starten Sie den Pironman 5-Dienst mit folgendem Befehl neu:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Aktivieren Sie I2C, wenn die Adresse nicht erkannt wird:

     * Bearbeiten Sie die Konfigurationsdatei mit folgendem Befehl:

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Fügen Sie am Ende der Datei die folgende Zeile hinzu:

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Speichern Sie die Datei mit ``Ctrl+X``, bestätigen Sie mit ``Y`` und beenden Sie. Starten Sie den Pironman 5 neu und überprüfen Sie, ob das Problem behoben ist.

Falls das Problem nach Durchführung der oben genannten Schritte weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden uns so schnell wie möglich bei Ihnen melden.

8. NVMe PIP-Modul funktioniert nicht? 
---------------------------------------

1. Stellen Sie sicher, dass das FPC-Kabel, das das NVMe PIP-Modul mit dem Raspberry Pi 5 verbindet, sicher angeschlossen ist.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

2. Vergewissern Sie sich, dass Ihre SSD korrekt am NVMe PIP-Modul befestigt ist.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

3. Überprüfen Sie den Status der LEDs des NVMe PIP-Moduls:

   Nachdem alle Verbindungen überprüft wurden, schalten Sie den Pironman 5 ein und beobachten Sie die beiden Anzeigen auf dem NVMe PIP-Modul:  

   * **PWR-LED**: Sollte leuchten.  
   * **STA-LED**: Sollte blinken, um den normalen Betrieb anzuzeigen.  

   .. image:: img/nvme_pip_leds.png  

   * Wenn die **PWR-LED** leuchtet, die **STA-LED** jedoch nicht blinkt, wird die NVMe-SSD nicht vom Raspberry Pi erkannt.  
   * Wenn die **PWR-LED** nicht leuchtet, überbrücken Sie die "Force Enable"-Pins (J4) auf dem Modul. Wenn die **PWR-LED** aufleuchtet, könnte dies auf ein loses FPC-Kabel oder eine nicht unterstützte Systemkonfiguration für NVMe hinweisen.

     .. image:: img/nvme_pip_j4.png  

4. Stellen Sie sicher, dass Ihr NVMe-SSD ein korrekt installiertes Betriebssystem hat. Siehe: :ref:`install_the_os_5`.

5. Wenn die Verkabelung korrekt ist und das Betriebssystem installiert wurde, die NVMe-SSD jedoch weiterhin nicht bootet, versuchen Sie, von einer Micro-SD-Karte zu booten, um die Funktionalität anderer Komponenten zu überprüfen. Sobald bestätigt, fahren Sie fort mit: :ref:`configure_boot_ssd_5`.

Falls das Problem nach Durchführung der oben genannten Schritte weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

9. RGB-LEDs funktionieren nicht?
------------------------------------

#. Die beiden Pins am IO-Expander über J9 verbinden die RGB-LEDs mit GPIO10. Stellen Sie sicher, dass die Jumperkappe auf diesen beiden Pins korrekt angebracht ist.

   .. image:: img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Überprüfen Sie, ob das Raspberry Pi ein kompatibles Betriebssystem ausführt. Der Pironman 5 unterstützt nur die folgenden Betriebssystemversionen:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Falls ein nicht unterstütztes Betriebssystem installiert ist, folgen Sie der Anleitung zur Installation eines kompatiblen Betriebssystems: :ref:`install_the_os_5`.

#. Führen Sie den Befehl ``sudo raspi-config`` aus, um das Konfigurationsmenü zu öffnen. Navigieren Sie zu **3 Interfacing Options** -> **I3 SPI** -> **YES**, klicken Sie dann auf **OK** und **Finish**, um SPI zu aktivieren. Starten Sie anschließend den Pironman 5 neu.

Falls das Problem nach Durchführung der oben genannten Schritte weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

10. CPU-Lüfter funktioniert nicht?
----------------------------------------------

Wenn die CPU-Temperatur den festgelegten Schwellenwert nicht erreicht hat, bleibt der CPU-Lüfter ausgeschaltet.

**Lüfterdrehzahlregelung basierend auf der Temperatur**  

Der PWM-Lüfter arbeitet dynamisch und passt seine Drehzahl entsprechend der Temperatur des Raspberry Pi 5 an:  

* **Unter 50°C**: Lüfter bleibt aus (0% Drehzahl).  
* **Bei 50°C**: Lüfter läuft mit niedriger Drehzahl (30% Drehzahl).  
* **Bei 60°C**: Lüfter erhöht auf mittlere Drehzahl (50% Drehzahl).  
* **Bei 67,5°C**: Lüfter beschleunigt auf hohe Drehzahl (70% Drehzahl).  
* **Bei 75°C und höher**: Lüfter läuft mit maximaler Drehzahl (100% Drehzahl).  

Weitere Details finden Sie unter: :ref:`Fans`.

11. Wie deaktiviert man das Web-Dashboard?
------------------------------------------------------

Nach der Installation des Moduls ``pironman5`` können Sie auf das :ref:`view_control_dashboard` zugreifen.
      
Falls Sie diese Funktion nicht benötigen und die Nutzung von CPU und RAM reduzieren möchten, können Sie das Dashboard während der Installation von ``pironman5`` mit dem Flag ``--disable-dashboard`` deaktivieren.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Falls Sie ``pironman5`` bereits installiert haben, können Sie das ``dashboard``-Modul und ``influxdb`` entfernen und anschließend den Pironman 5 neu starten, um die Änderungen anzuwenden:
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

12. Wie steuert man Komponenten mit dem Befehl ``pironman5``?
----------------------------------------------------------------------

Sie können die folgende Anleitung verwenden, um die Komponenten des Pironman 5 mit dem Befehl ``pironman5`` zu steuern.

* :ref:`view_control_commands`

13. Wie ändert man die Boot-Reihenfolge des Raspberry Pi mit Befehlen?
--------------------------------------------------------------------------

Wenn Sie bereits beim Raspberry Pi angemeldet sind, können Sie die Boot-Reihenfolge mit Befehlen ändern. Detaillierte Anweisungen finden Sie unter:

* :ref:`configure_boot_ssd_5`

14. Wie ändert man die Boot-Reihenfolge mit dem Raspberry Pi Imager?
---------------------------------------------------------------------------

Zusätzlich zur Änderung der ``BOOT_ORDER`` in der EEPROM-Konfiguration können Sie auch den **Raspberry Pi Imager** verwenden, um die Boot-Reihenfolge Ihres Raspberry Pi zu ändern.

Es wird empfohlen, für diesen Schritt eine Ersatzkarte zu verwenden.

* :ref:`update_bootloader_5`

15. Wie kopiert man das System von der SD-Karte auf eine NVMe-SSD? 
-----------------------------------------------------------------------

Wenn Sie eine NVMe-SSD besitzen, jedoch keinen Adapter haben, um die NVMe mit Ihrem Computer zu verbinden, können Sie das System zunächst auf Ihrer Micro-SD-Karte installieren. Sobald der Pironman 5 erfolgreich gestartet ist, können Sie das System von der Micro-SD-Karte auf die NVMe-SSD kopieren. Detaillierte Anweisungen finden Sie hier:

* :ref:`copy_sd_to_nvme_5`

16. Wie entfernt man die Schutzfolie von den Acrylplatten?
------------------------------------------------------------------

Im Lieferumfang sind zwei Acrylplatten enthalten, die auf beiden Seiten mit einer gelblichen/transparenten Schutzfolie überzogen sind, um Kratzer zu vermeiden. Die Schutzfolie kann etwas schwer zu entfernen sein. Verwenden Sie einen Schraubendreher, um vorsichtig an den Ecken zu kratzen, und ziehen Sie dann die gesamte Folie sorgfältig ab.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

17. Wie installiert man OpenSSH über PowerShell?
--------------------------------------------------------------

Wenn Sie ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) verwenden, um sich mit Ihrem Raspberry Pi zu verbinden, aber die folgende Fehlermeldung erhalten:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Das bedeutet, dass Ihr Betriebssystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Sie müssen es manuell installieren, indem Sie der folgenden Anleitung folgen.

#. Geben Sie ``powershell`` in das Suchfeld Ihres Windows-Desktops ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im erscheinenden Menü ``Als Administrator ausführen`` aus.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Verwenden Sie den folgenden Befehl, um ``OpenSSH.Client`` zu installieren.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach der Installation wird folgende Ausgabe angezeigt:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Überprüfen Sie die Installation mit dem folgenden Befehl:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Es wird angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

  .. warning:: 

    Wenn die obige Ausgabe nicht erscheint, bedeutet dies, dass Ihr Windows-System weiterhin zu alt ist. In diesem Fall wird empfohlen, ein Drittanbieter-SSH-Tool wie |link_putty| zu verwenden.

6. Starten Sie PowerShell neu und führen Sie es weiterhin als Administrator aus. Ab diesem Punkt können Sie sich mit dem Befehl ``ssh`` in Ihren Raspberry Pi einloggen. Sie werden aufgefordert, das zuvor festgelegte Passwort einzugeben.

   .. image:: img/powershell_login.png

.. 18. Warum schaltet sich der OLED-Bildschirm automatisch aus?
.. ---------------------------------------------------------------------------------

.. Um Energie zu sparen und die Lebensdauer des Bildschirms zu verlängern, schaltet sich der OLED-Bildschirm nach einer gewissen Inaktivität automatisch aus. Dies ist Teil des normalen Designs und beeinträchtigt die Funktionalität des Produkts nicht.

.. Drücke einfach einmal die Taste am Gerät, um den OLED-Bildschirm aufzuwecken und die Anzeige fortzusetzen.

.. .. note::

..    Für die Konfiguration des OLED-Bildschirms (z. B. Ein-/Ausschalten, Ruhezeit, Drehung usw.) siehe: :ref:`view_control_dashboard` oder :ref:`view_control_commands`.
