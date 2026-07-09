.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Schnelle Fehlerbehebung
-------------------------------

* OLED-Bildschirm funktioniert nicht -> :ref:`faq_oled_5`
* RGB-LEDs funktionieren nicht -> :ref:`faq_rgb_5`
* GPIO-Lüfter funktionieren nicht -> :ref:`faq_gpio_fans_5`
* CPU-Lüfter dreht sich nicht -> :ref:`faq_pwm_fan_5`
* Dashboard zeigt keine Daten an -> :ref:`faq_dashboard_5`
* NVMe-SSD wird nicht erkannt -> :ref:`faq_nvme_5`



1. Hardware
-----------


.. _compatible_systems_5:

Kompatible Systeme
------------------

.. start_faq_com_os

Systeme, die auf dem Raspberry Pi 5 getestet wurden:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

.. end_faq_com_os

Einschalttaste
--------------

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_5`

.. start_faq_power_button

Die Einschalttaste erweitert die ursprungliche Einschalttaste des Raspberry Pi 5 und verhalt sich ahnlich.

* Kurz drucken: Einschalten / OLED aufwecken / OLED-Seiten wechseln.
* 2 Sekunden gedruckt halten: Sicheres Herunterfahren (erfordert |link_safe_shutdown|).
* 5 Sekunden gedruckt halten: Erzwungenes Herunterfahren.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

.. end_faq_power_button


Luftstromrichtung
-----------------

.. start_faq_airflow_direction

Der Luftstrom im Pironman 5 ist so ausgelegt, dass die Kuhleffizienz maximiert wird. Kuhle Luft tritt durch die GPIO-Offnung und andere Lufteinlasse ein, passiert den Tower-Kuhler und wird durch die beiden seitlichen GPIO-Lufter abgefuhrt.

Eine detaillierte Demonstration finden Sie im folgenden Video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

.. end_faq_airflow_direction


Kupferrohrenden am Tower-Kuhler
-------------------------------

.. start_faq_copper_pipe_ends

Die abgeflachten Enden der U-formigen Kupfer-Heatpipes sind Teil des normalen Herstellungsprozesses und ermoglichen den Heatpipes, durch die Aluminiumlamellen zu verlaufen.

.. image:: img/tower_cooler1.png

.. end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
--------------------

.. start_faq_ai_hat

Der Raspberry Pi AI HAT+ ist nicht mit dem Pironman 5 kompatibel.

.. image:: img/output3.png
    :width: 400

Das Raspberry Pi AI Kit kombiniert den Raspberry Pi M.2 HAT+ und das Hailo AI-Beschleunigermodul.

.. image:: img/output2.jpg
    :width: 400

Sie konnen das Hailo AI-Beschleunigermodul vom Raspberry Pi AI Kit abnehmen und direkt in das NVMe PIP-Modul des Pironman 5 einsetzen.

.. image:: img/output4.png
    :width: 800

.. end_faq_ai_hat



2. Kuhlung und Lufter
---------------------


.. _faq_pwm_fan_5:

CPU-Lufter funktioniert nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_pwm_fan

Der CPU-Lufter des Pironman 5 wird vom Raspberry-Pi-System gesteuert. Die Drehzahl des CPU-Lufters hangt von der CPU-Temperatur des Raspberry Pi 5 ab.

Standard-Lufterkennlinie des CPU-Lufters:

* < 50 °C: Aus (0 %)
* 50 °C+: Niedrige Drehzahl (30 %)
* 60 °C+: Mittlere Drehzahl (50 %)
* 67,5 °C+: Hohe Drehzahl (70 %)
* 75 °C+: Volle Drehzahl (100 %)

Aktuelle CPU-Temperatur uberprufen (Beispielausgabe: ``temp=48.7'C``):

.. code-block:: shell

   vcgencmd measure_temp

Sie konnen den CPU-Lufter mit den folgenden Befehlen manuell steuern:

.. code-block:: shell

   pinctrl FAN_PWM op dl   # Lufter einschalten (low active)
   pinctrl FAN_PWM op dh   # Lufter ausschalten (high active)
   pinctrl FAN_PWM a0      # Automatikmodus

Sie konnen die CPU-Lufter-Temperaturschwellen auch durch Bearbeiten der folgenden Datei anpassen:

.. code-block:: shell

   nano /boot/firmware/config.txt

Fugen Sie hinzu:

.. code-block:: text

   dtparam=cooling_fan=on
   dtparam=fan_temp0=40000
   dtparam=fan_temp0_hyst=10000
   dtparam=fan_temp0_speed=125

Diese Konfiguration startet den CPU-Lufter bei 40 °C mit PWM-Drehzahlstufe 125.

Starten Sie nach dem Speichern der Datei den Raspberry Pi neu, damit die Anderungen wirksam werden.

.. end_faq_pwm_fan


.. _faq_gpio_fans_5:

GPIO-Lufter funktionieren nicht?
--------------------------------

.. start_faq_gpio_fans

Uberprufen Sie zunachst, ob die FAN-Jumperkappe auf dem IO-Erweiterungsboard korrekt installiert ist.

.. image:: hardware/img/io_board_fan_j9.png

Stellen Sie dann die GPIO-Lufter auf den Modus ``Always On`` und prufen Sie, ob die Lufter zu laufen beginnen.

.. code-block:: shell

   sudo pironman5 -gm 0

Sie konnen die GPIO-Lufter auch direkt an die ``5V``- und ``GND``-Pins des Raspberry Pi anschlieen, um sie zu testen.

Wenn die Lufter bei direktem Anschluss normal laufen, liegt das Problem moglicherweise am IO-Erweiterungsboard. Bitte kontaktieren Sie uns fur weitere Unterstutzung.

Wenn das Problem weiterhin besteht, offnen Sie die **Log**-Seite des Dashboards und prufen Sie auf Fehlermeldungen. Sie konnen uns auch die folgende Protokolldatei senden:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

.. end_faq_gpio_fans

3. OLED und RGB
---------------


.. _faq_oled_5:

OLED-Bildschirm funktioniert nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_5`
.. |link_compatible_systems| replace:: :ref:`compatible_systems_5`

.. start_faq_oled

Wenn der OLED-Bildschirm nichts anzeigt oder fehlerhaft anzeigt, fuhren Sie die folgenden Schritte zur Fehlerbehebung aus:

#. Stellen Sie sicher, dass das FPC-Kabel des OLED-Bildschirms sicher angeschlossen ist. Es wird empfohlen, den OLED-Bildschirm erneut anzuschlieen und das Gerat dann einzuschalten.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Bestatigen Sie, dass der Raspberry Pi ein unterstutztes Betriebssystem ausfuhrt.

   Siehe |link_compatible_systems|.

#. Beim ersten Einschalten des OLED-Bildschirms werden moglicherweise nur Pixelblocke angezeigt. Sie mussen den Anweisungen in |link_set_up_pironman5| folgen, um die Konfiguration abzuschlieen, bevor der Bildschirm korrekte Informationen anzeigen kann.

#. Verwenden Sie den folgenden Befehl, um zu uberprufen, ob die OLED-I2C-Adresse ``0x3C`` erkannt wird:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Wenn die I2C-Adresse ``0x3C`` erkannt wird, starten Sie den Pironman-5-Dienst neu:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Wenn die Adresse nicht erkannt wird, aktivieren Sie I2C:

     .. code-block:: shell

        sudo nano /boot/firmware/config.txt

     Fugen Sie hinzu:

     .. code-block:: shell

        dtparam=i2c_arm=on

     Speichern Sie die Datei und starten Sie den Raspberry Pi neu.

#. Wenn das Problem weiterhin besteht, senden Sie uns bitte die folgende Protokolldatei:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_oled


.. _faq_rgb_5:

RGB-LEDs funktionieren nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. start_faq_rgb

#. Die beiden Pins am IO-Erweiterungsboard uber J9 verbinden die RGB-LEDs mit GPIO10. Stellen Sie sicher, dass die Jumperkappe auf diesen beiden Pins korrekt installiert ist.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Bestatigen Sie, dass der Raspberry Pi ein unterstutztes Betriebssystem ausfuhrt.

   Siehe |link_compatible_systems|.

#. Fuhren Sie den folgenden Befehl aus, um SPI zu aktivieren:

   .. code-block:: shell

      sudo raspi-config

   Navigieren Sie zu:

   ``3 Interfacing Options`` -> ``I3 SPI`` -> ``YES``

   Starten Sie dann den Raspberry Pi neu.

#. Wenn das Problem weiterhin besteht, senden Sie uns bitte die folgende Protokolldatei:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_rgb

.. _faq_customize_oled_5:

Wie kann ich die OLED-Anzeige anpassen?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_customize_oled

Wenn Sie die OLED-Anzeige anpassen mochten, z. B. benutzerdefinierte 2-4-stellige Bildanzeigen hinzufugen, konnen Sie die OLED-Seitendateien auf eine der folgenden Arten andern.

* **Methode 1: Direkte Anderung der installierten Dateien**

  #. Listen Sie die OLED-Seitendateien auf:

     .. code-block:: shell

        ls /opt/pironman5/venv/lib/python3.13/site-packages/pm_auto/addons/oled/pages/

  #. Andern Sie die gewunschten Python-Dateien.

  #. Starten Sie den Dienst neu, um die Anderungen zu ubernehmen:

     .. code-block:: shell

        sudo systemctl restart pironman5.service


* **Methode 2: ``pm_auto`` klonen und neu installieren**

  #. Klonen Sie das ``pm_auto``-Repository:

     .. code-block:: shell

        git clone -b 1.4.x https://github.com/sunfounder/pm_auto/

  #. Nehmen Sie Ihre Anderungen vor und installieren Sie das geanderte Paket neu:

     .. code-block:: shell

        sudo /opt/pironman5/venv/bin/pip3 uninstall pm_auto -y && \
        sudo /opt/pironman5/venv/bin/pip3 install ~/pm_auto --no-build-isolation && \
        sudo chown -R pironman5:pironman5 /opt/pironman5

  #. Starten Sie den Dienst neu:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

* **Testen und Debuggen**

  So zeigen Sie Laufzeitprotokolle an:

  .. code-block:: shell

     journalctl -xefu pironman5.service

  Sie konnen den Dienst auch anhalten und manuell ausfuhren, um schneller zu testen:

  .. code-block:: shell

     sudo systemctl stop pironman5.service
     sudo systemctl restart pironman5.service

.. end_faq_customize_oled

4. Dashboard und Software
-------------------------


.. _faq_dashboard_5:

Dashboard zeigt keine Daten an
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_dashboard

Wenn das Dashboard keine Daten anzeigt, offnen Sie zunachst die **Log**-Seite des Dashboards und prufen Sie, ob Fehlermeldungen im Zusammenhang mit ``influxdb`` angezeigt werden.

Haufige Fehler sind:

* ``database not found``
* ``failed to connect to influxdb``
* ``connection refused``
* ``timeout``

Sie konnen die folgenden Schritte zur Behebung des Problems versuchen.

#. Leeren Sie den Browser-Cache oder offnen Sie die Dashboard-Seite im **Inkognito-/Privatmodus**.

#. Uberprufen Sie, ob die folgenden Dienste ordnungsgema ausgefuhrt werden:

   .. code-block:: shell

      sudo systemctl status pironman5 --no-pager
      sudo systemctl status influxdb --no-pager

   Beide Dienste sollten Folgendes anzeigen:

   .. code-block:: text

      active (running)

#. Wenn einer der Dienste nicht ordnungsgema lauft, starten Sie ihn neu:

   .. code-block:: shell

      sudo systemctl restart influxdb
      sudo systemctl restart pironman5

   Warten Sie dann etwa 30 Sekunden und aktualisieren Sie die Dashboard-Seite.

#. Uberprufen Sie, ob die Datenbank ``pironman5`` existiert:

   .. code-block:: shell

      influx

   Fuhren Sie dann Folgendes aus:

   .. code-block:: text

      SHOW DATABASES;

   Sie sollten Folgendes sehen:

   .. code-block:: text

      pironman5
      _internal

#. Wenn die Datenbank fehlt oder beschadigt ist, konnen Sie versuchen, die historischen Daten uber das Dashboard zu loschen:

   ``Settings -> Clear All Data``

#. Wenn das Problem nach allen oben genannten Schritten weiterhin besteht, empfehlen wir eine Neuinstallation des Raspberry Pi OS und der Pironman-5-Software.

.. end_faq_dashboard


Wie deaktiviere ich das Web-Dashboard?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_5`

.. start_faq_disable_dashboard

Nach Abschluss der Installation des Moduls ``pironman5`` kannst du auf das |link_view_control_dashboard| zugreifen.

Wenn du diese Funktion nicht benotigst und die CPU- und RAM-Auslastung reduzieren mochtest, kannst du das Dashboard wahrend der Installation mit dem Flag ``--disable-dashboard`` deaktivieren.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Wenn du ``pironman5`` bereits installiert hast, kannst du das Dashboard-Modul und ``influxdb`` entfernen:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. end_faq_disable_dashboard


Wie deinstalliere und installiere ich die Pironman-5-Software neu?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_reinstall_pironman5

#. Deinstalliere die aktuelle ``pironman5``-Software:

   .. code-block:: shell

      cd ~/pironman5
      sudo python3 install.py --uninstall

#. Starte den Raspberry Pi wie aufgefordert neu und entferne dann das Verzeichnis ``pironman5``:

   .. code-block:: shell

      cd ~/
      sudo rm -rf pironman5

#. Fuhre den folgenden Befehl aus, um die Software fur dein Pironman-5-Modell neu zu installieren:

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash

.. end_faq_reinstall_pironman5


Wie steuere ich Komponenten mit dem Befehl ``pironman5``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`view_control_commands_5`

.. start_faq_pironman5_command

Sie konnen auf das folgende Tutorial verweisen, um die Komponenten der Pironman-5-Serie mit dem Befehl ``pironman5`` zu steuern.

* |link_view_control_commands|

.. end_faq_pironman5_command



5. Booten und Speicher
----------------------


PI5 startet nicht (rote LED)?
-----------------------------

.. |link_update_bootloader| replace:: :ref:`update_bootloader_5`

.. start_faq_pi5_boot_fail

Dieses Problem kann durch ein Systemupdate, Anderungen der Boot-Reihenfolge oder einen beschadigten Bootloader verursacht werden. Sie konnen die folgenden Schritte zur Behebung des Problems versuchen:

#. USB-HDMI-Adapter-Verbindung prufen

   * Bitte prufen Sie sorgfaltig, ob der USB-HDMI-Adapter korrekt mit dem PI5 verbunden ist.
   * Versuchen Sie, den USB-HDMI-Adapter zu entfernen und wieder anzuschlieen.
   * Schlieen Sie dann die Stromversorgung wieder an und prufen Sie, ob der PI5 erfolgreich startet.

#. PI5 auerhalb des Gehauses testen

   * Wenn das erneute Anschlieen des Adapters das Problem nicht lost:
   * Entfernen Sie den PI5 aus dem Pironman-5-Gehause.
   * Versorgen Sie den PI5 direkt mit dem Netzteil (ohne Gehause).
   * Prufen Sie, ob er normal starten kann.

#. Bootloader wiederherstellen

   * Wenn der PI5 immer noch nicht startet, ist moglicherweise der Bootloader beschaftigt. Sie konnen dieser Anleitung folgen: |link_update_bootloader| und wahlen, ob von SD-Karte oder NVMe/USB gebootet werden soll.
   * Legen Sie die vorbereitete SD-Karte in den PI5 ein, schalten Sie ihn ein und warten Sie mindestens 10 Sekunden. Sobald die Wiederherstellung abgeschlossen ist, entfernen und formatieren Sie die SD-Karte erneut.
   * Verwenden Sie dann Raspberry Pi Imager, um das neueste Raspberry Pi OS zu flashen und versuchen Sie erneut zu starten.

.. end_faq_pi5_boot_fail


.. _faq_nvme_5:

NVMe PIP-Modul funktioniert nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os| replace:: :ref:`install_the_os_5`
.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_5`

.. start_faq_nvme_pip

#. Stellen Sie sicher, dass das FPC-Kabel, das das NVMe PIP-Modul mit dem Raspberry Pi 5 verbindet, sicher angeschlossen ist.

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

#. Vergewissern Sie sich, dass Ihre SSD korrekt am NVMe PIP-Modul befestigt ist.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Uberprufen Sie den Status der LEDs des NVMe PIP-Moduls:

   * **PWR-LED**: Sollte leuchten.
   * **STA-LED**: Sollte bei normalem Betrieb blinken.

   .. image:: img/nvme_pip_leds.png

   * Wenn die **PWR-LED** leuchtet, aber die **STA-LED** nicht blinkt, wird die NVMe-SSD nicht erkannt.
   * Wenn die **PWR-LED** aus ist, uberbrucken Sie die ``Force Enable``-Pins (J4).

     .. image:: img/nvme_pip_j4.png

#. Bestatigen Sie, dass Ihre NVMe-SSD ein gultiges Betriebssystem enthalt.

   Siehe |link_install_the_os|.

#. Wenn die SSD immer noch nicht bootet, versuchen Sie zunachst, von einer Micro-SD-Karte zu booten, und konfigurieren Sie dann den NVMe-Start:

   * |link_configure_boot_ssd|

#. Wenn das Problem weiterhin besteht, senden Sie uns bitte die folgende Protokolldatei:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_nvme_pip


Wie andert man die Boot-Reihenfolge des Raspberry Pi mit Befehlen?
------------------------------------------------------------------

.. start_faq_boot_order_command

Wenn Sie bereits beim Raspberry Pi angemeldet sind, konnen Sie die Boot-Reihenfolge mit Befehlen andern.

* |link_configure_boot_ssd|

.. end_faq_boot_order_command


Wie andert man die Boot-Reihenfolge mit Raspberry Pi Imager?
------------------------------------------------------------

.. start_faq_boot_order_imager

Zusatzlich zur Anderung der ``BOOT_ORDER`` in der EEPROM-Konfiguration konnen Sie auch Raspberry Pi Imager verwenden, um die Boot-Reihenfolge zu andern.

* |link_update_bootloader|

.. end_faq_boot_order_imager


Wie kopiert man das System von der SD-Karte auf eine NVMe-SSD?
--------------------------------------------------------------

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_5`

.. start_faq_copy_sd_to_nvme

Wenn Sie keinen NVMe-zu-USB-Adapter haben, konnen Sie das System zunachst auf einer Micro-SD-Karte installieren und es nach erfolgreichem Booten auf die NVMe-SSD kopieren.

* |link_copy_sd_to_nvme|

.. end_faq_copy_sd_to_nvme



6. Erweiterte Nutzung
---------------------


Wie entfernt man die Schutzfolie?
---------------------------------

.. start_faq_remove_film

Im Lieferumfang sind zwei Acrylplatten enthalten, die auf beiden Seiten mit einer gelben/transparenten Schutzfolie uberzogen sind, um Kratzer zu vermeiden.

Die Schutzfolie kann schwer zu entfernen sein. Verwenden Sie einen Schraubendreher, um vorsichtig eine Ecke anzuheben, und ziehen Sie dann die gesamte Folie vorsichtig ab.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. end_faq_remove_film