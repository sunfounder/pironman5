.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Schnelle Fehlerbehebung
-------------------------

* Einschalttaste funktioniert nicht → :ref:`faq_power_button_not_work_promax`
* OLED-Bildschirm funktioniert nicht → :ref:`faq_oled_promax`
* RGB-LEDs funktionieren nicht → :ref:`faq_rgb_promax`
* Lüfter funktioniert nicht → :ref:`promax_fan_faq`
* Dashboard zeigt keine Daten an → :ref:`faq_dashboard_promax`
* NVMe-SSD wird nicht erkannt → :ref:`faq_nvme_promax`
* NVMe-SSD erkannt, verursacht aber Systemneustart → :ref:`faq_nvme_link_down_promax`
* PI5 startet nicht → :ref:`faq_pi5_boot_fail_promax`



1. Hardware
-------------


.. _com_os_promax:

Kompatible Systeme
^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_promax`

Einschalttaste
^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_promax:

Einschalttaste funktioniert nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Kupferrohrenden am Tower-Kühler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^

Das Raspberry Pi AI HAT+ ist nicht mit dem Pironman 5 Pro MAX kompatibel.

.. image:: img/output3.png
    :width: 400

Das Raspberry Pi AI Kit kombiniert den Raspberry Pi M.2 HAT+ und das Hailo-KI-Beschleunigermodul.

.. image:: img/output2.jpg
    :width: 400

Sie können das Hailo-KI-Beschleunigermodul vom Raspberry Pi AI Kit abnehmen und direkt in das NVMe PIP-Modul des Pironman 5 Pro MAX einsetzen.


4,3-Zoll-Bildschirm ist schwarz / zeigt nichts an?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der 4,3-Zoll-DSI-Bildschirm ist Plug-and-Play — es ist keine zusätzliche Treiberinstallation erforderlich.

.. note::

   Der **ON/AUTO**-Jumper auf der HDMI-/USB-Platine steuert nur die Lautsprecherausgabe. Er hat **keinen Einfluss** auf die Bildschirmanzeige.

Wenn der Bildschirm schwarz ist oder nichts anzeigt, prüfen Sie Folgendes:

#. Stellen Sie sicher, dass das DSI-Flachbandkabel am richtigen DSI-Port des Raspberry Pi 5 angeschlossen ist.

#. Prüfen Sie, ob das Flachbandkabel vollständig eingesteckt, die Klemme fest gedrückt und die Kontakte in die richtige Richtung weisend sind.

#. Führen Sie den folgenden Befehl aus, um zu prüfen, ob das System den DSI-Bildschirm erkennt:

   .. code-block:: shell

      sudo dmesg | grep -i dsi

   Wenn der Bildschirm erkannt wird, sollte eine Ausgabe ähnlich ``DSI display found`` erscheinen. Wenn keine Ausgabe erscheint, wird der Bildschirm nicht erkannt — prüfen Sie die physische Verbindung erneut.


Externer HDMI-Bildschirm — Taskleiste erscheint nur auf dem 4,3-Zoll-Bildschirm?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn Sie einen externen HDMI-Monitor an den Pironman 5 Pro MAX anschließen, kann die Taskleiste des Desktops auf dem integrierten 4,3-Zoll-DSI-Bildschirm verbleiben, anstatt auf den externen Bildschirm zu wechseln. Das liegt daran, dass das System den DSI-Bildschirm standardmäßig als primären Bildschirm verwendet.

Wenn Sie den HDMI-Monitor beim Start als primären Bildschirm festlegen möchten:

#. Erstellen Sie ein Startskript:

   .. code-block:: shell

      sudo nano /usr/local/bin/fix-primary-screen.sh

#. Fügen Sie folgenden Inhalt in das Skript ein:

   .. code-block:: bash

      #!/bin/bash
      # Check if an external HDMI monitor is connected
      if wlr-randr | grep -q "HDMI-A-1"; then
          # Turn off the DSI screen first
          wlr-randr --output DSI-1 --off
          sleep 2
          # Re-enable DSI and place it to the right of HDMI
          wlr-randr --output DSI-1 --on --right-of HDMI-A-1
      fi

#. Machen Sie das Skript ausführbar:

   .. code-block:: shell

      sudo chmod +x /usr/local/bin/fix-primary-screen.sh

#. Fügen Sie das Skript zum Autostart hinzu. Bearbeiten Sie die labwc-Autostart-Datei:

   .. code-block:: shell

      nano ~/.config/labwc/autostart

   Fügen Sie die folgende Zeile hinzu (das ``&`` führt sie im Hintergrund aus):

   .. code-block:: text

      /usr/local/bin/fix-primary-screen.sh &


2. Kühlung und Lüfter
-----------------------


.. _promax_fan_faq:

Lüfter funktioniert nicht / lässt sich nicht steuern?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan

Dashboard zeigt keine Lüfterdrehzahl an?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der Pro MAX verwendet benutzerdefinierte **5-Pin**-Lüfter mit folgender Pinbelegung: **PWM / 5V / GND / RGB Data In / RGB Data Out**.

Diese Lüfter haben **keinen** Tachometer-Pin (Drehzahlsignal), daher kann das System die tatsächliche Drehzahl nicht auslesen. Dass das Dashboard keine Lüfterdrehzahl anzeigt, ist normal und beabsichtigt.

Die Lüfterdrehzahl wird über die native PWM-Temperaturkurve des Raspberry Pi gesteuert:

* < 50 °C: Aus (0 %)
* 50 °C und mehr: Niedrige Drehzahl (30 %)
* 60 °C und mehr: Mittlere Drehzahl (50 %)
* 67,5 °C und mehr: Hohe Drehzahl (70 %)
* 75 °C und mehr: Volle Drehzahl (100 %)


3. OLED und RGB
-----------------


.. _faq_oled_promax:

OLED-Bildschirm funktioniert nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`promax_set_up_pi_os`
.. |link_compatible_systems| replace:: :ref:`com_os_promax`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled

.. _faq_customize_oled_promax:

Wie passe ich den OLED-Bildschirm an?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled

.. _faq_rgb_promax:

RGB-LEDs funktionieren nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb

Wie wecke ich den OLED-Bildschirm auf?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um Energie zu sparen und die Lebensdauer des Bildschirms zu verlängern, schaltet sich der OLED-Bildschirm nach einer Phase der Inaktivität automatisch aus. Dies gehört zum normalen Design und beeinträchtigt die Produktfunktionalität nicht.

.. note::

   Informationen zur Konfiguration des OLED-Bildschirms (Ein-/Ausschalten, Ruhezeit, Drehung usw.) finden Sie unter :ref:`promax_view_control_dashboard` oder :ref:`promax_view_control_commands`.


4. Dashboard und Software
---------------------------


.. _faq_dashboard_promax:

Dashboard zeigt keine Daten an
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard

.. |link_view_control_dashboard| replace:: :ref:`promax_view_control_dashboard`

Wie deaktiviere ich das Web-Dashboard?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Wie deinstalliere und reinstalliere ich die Pironman 5 Software?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


.. |link_view_control_commands| replace:: :ref:`promax_view_control_commands`

Wie steuere ich Komponenten mit dem ``pironman5``-Befehl?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


.. _faq_piper_tts_32bit_promax:

``pip install piper-tts`` schlägt fehl mit "Could Not Find a Version"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bei der Installation von ``sunfounder-voice-assistant`` auf dem Pironman 5 Pro MAX kann folgender Fehler auftreten:

.. code-block:: text

   ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
   ERROR: No matching distribution found for piper-tts==1.3.0

Dieser Fehler tritt auf, weil ``piper-tts`` 1.3.0 nur **64-Bit**-Wheels (``aarch64``) bereitstellt. Wenn Ihr Raspberry Pi ein **32-Bit**-Betriebssystem ausführt, kann pip kein kompatibles Paket finden.

**Lösung:** Installieren Sie eine 64-Bit-Version von Raspberry Pi OS.

#. Prüfen Sie die aktuelle Systemarchitektur:

   .. code-block:: shell

      uname -m

   * ``aarch64`` → 64-Bit (kein Problem)
   * ``armv7l`` → 32-Bit (Upgrade erforderlich)

#. Verwenden Sie `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`_, um ein **64-Bit**-Image von Raspberry Pi OS auf Ihr Speichermedium zu flashen.

#. Installieren Sie nach der Installation des 64-Bit-OS die Software ``pironman5`` und ``sunfounder-voice-assistant`` erneut.


5. Boot und Speicher
----------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_promax`

.. _faq_pi5_boot_fail_promax:

PI5 startet nicht (rote LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail

.. _faq_nvme_promax:

NVMe PIP-Modul funktioniert nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_dual| replace:: :ref:`install_the_os_promax`

.. include:: ../pironman5_max/faq.rst
   :start-after: start_faq_nvme_pip_dual
   :end-before: end_faq_nvme_pip_dual

#. Wenn die Verkabelung korrekt und das Betriebssystem installiert ist, die NVMe-SSD aber trotzdem nicht startet, versuchen Sie von einer Micro-SD-Karte zu booten, um die Funktion der anderen Komponenten zu prüfen. Fahren Sie anschließend mit :ref:`configure_boot_ssd_promax` fort.

#. Wenn das Problem nach den oben genannten Schritten weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir antworten so schnell wie möglich.


.. _faq_nvme_link_down_promax:

NVMe-SSD erkannt, verursacht aber Neustart beim Lesen/Schreiben?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_promax`

Wie ändere ich die Boot-Reihenfolge des Raspberry Pi mit Befehlen?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Wie ändere ich die Boot-Reihenfolge mit Raspberry Pi Imager?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_promax`

Wie kopiere ich das System von der SD-Karte auf eine NVMe-SSD?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme


6. Erweiterte Nutzung
-----------------------


Wie entferne ich die Schutzfolie?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film


.. _promax_openssh_powershell:

Wie installiere ich OpenSSH über PowerShell?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


Wenn ich OMV einrichte, kann ich dann trotzdem die Funktionen des Pironman5 nutzen?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ja, OpenMediaVault wird auf dem Raspberry-Pi-System eingerichtet. Bitte folgen Sie den Schritten von :ref:`promax_set_up_pi_os`, um die Konfiguration fortzusetzen.


Kamera des Raspberry Pi funktioniert nicht?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn die Kamera nicht funktioniert, stehen 90 % der Probleme mit der Flachbandkabelverbindung oder der Kamera-Hardware selbst in Zusammenhang.

Prüfen Sie zunächst mit ``rpicam-hello --list-cameras``, ob die Kamera erkannt wird. Wenn sie erfolgreich erkannt wird, sollten Sie eine Meldung ähnlich der folgenden sehen:

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

Wenn die Kamera nicht erkannt wird, prüfen Sie, ob das Flachbandkabel verkehrt herum oder nicht vollständig eingesteckt ist. Wenn das Problem weiterhin besteht, versuchen Sie, das Flachbandkabel oder das Kameramodul gegen ein anderes zu tauschen (Gegenprobe).


Kann ich Home Assistant OS auf dem Pironman 5 Pro MAX installieren?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der Pironman 5 Pro MAX besitzt kein eigenes dediziertes Home-Assistant-Add-on. Sie können jedoch stattdessen das **Pironman 5 MAX**-Add-on verwenden — folgen Sie der `Anleitung zum SunFounder-Add-ons-Repository <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5_max/set_up/set_up_home_assistant.html#add-the-sunfounder-add-ons-repository>`_.

Beachten Sie folgende Einschränkungen:

* **4,3-Zoll-Bildschirm**: Home Assistant OS ist ein **Lite**-System ohne Desktop-Umgebung. Der im Pro MAX integrierte 4,3-Zoll-Bildschirm zeigt nichts an.

* **Zwei NVMe-SSDs des NVMe PIP-Moduls**: Home Assistant OS kann nicht beide NVMe-SSDs des dualen NVMe PIP-Moduls des Pro MAX lesen.

* **OLED-Bildschirm und RGB-LEDs**: Diese Komponenten funktionieren nach der Installation des Add-ons normal — es ist keine zusätzliche Konfiguration erforderlich.

* **CPU-Lüfter**: Der CPU-Lüfter erfordert eine manuelle Konfiguration, um unter Home Assistant OS zu funktionieren. Fügen Sie Folgendes in ``/boot/firmware/config.txt`` ein:

  .. code-block:: text

     dtparam=cooling_fan=on
     dtparam=fan_temp0=40000
     dtparam=fan_temp0_hyst=10000
     dtparam=fan_temp0_speed=125

  Nach dem Speichern und Neustart wird der CPU-Lüfter vom Raspberry Pi je nach CPU-Temperatur gesteuert. Sie können ihn auch manuell über ``pinctrl``-Befehle steuern — siehe :ref:`promax_fan_faq`.
