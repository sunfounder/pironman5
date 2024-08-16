.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _copy_sd_to_nvme_rpi:

Betriebssystem von Micro-SD auf NVMe-SSD kopieren
==================================================================

Falls Sie über eine NVMe-SSD verfügen, aber keinen Adapter besitzen, um diese an Ihren Computer anzuschließen, können Sie eine alternative Methode wählen: Installieren Sie das System zunächst auf Ihrer Micro-SD-Karte. Nachdem der Pironman 5 erfolgreich hochgefahren ist, können Sie das System von Ihrer Micro-SD-Karte auf die NVMe-SSD übertragen.

* Zuerst müssen Sie :ref:`install_os_sd_rpi` installieren.
* Starten Sie dann den Raspberry Pi und melden Sie sich an. Falls Sie nicht wissen, wie Sie sich anmelden, besuchen Sie die offizielle Raspberry Pi Webseite: |link_rpi_get_start|.

Führen Sie die obigen Schritte durch, bevor Sie mit den nachfolgenden Anweisungen fortfahren.


1. PCIe aktivieren
----------------------

Standardmäßig ist der PCIe-Anschluss nicht aktiviert. 

* Um ihn zu aktivieren, öffnen Sie die Datei ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Fügen Sie dann die folgende Zeile in die Datei ein.

  .. code-block:: shell
  
    # Externen PCIe-Anschluss aktivieren.
    dtparam=pciex1
  
* Es gibt einen einfacheren Alias für ``pciex1``, daher können Sie alternativ ``dtparam=nvme`` in die Datei ``/boot/firmware/config.txt`` hinzufügen.

  .. code-block:: shell
  
    dtparam=nvme

* Die Verbindung ist für Gen 2.0 Geschwindigkeiten (5 GT/sec) zertifiziert, Sie können sie jedoch auf Gen 3.0 (10 GT/sec) erzwingen, indem Sie die folgenden Zeilen in die Datei ``/boot/firmware/config.txt`` einfügen.

  .. code-block:: shell
  
    # Gen 3.0 Geschwindigkeiten erzwingen
    dtparam=pciex1_gen=3
  
  .. warning::
  
    Der Raspberry Pi 5 ist nicht für Gen 3.0 Geschwindigkeiten zertifiziert, und Verbindungen zu PCIe-Geräten bei diesen Geschwindigkeiten könnten instabil sein.

* Drücken Sie ``Ctrl + X``, ``Y`` und ``Enter``, um die Änderungen zu speichern.


2. Betriebssystem auf der SSD installieren
----------------------------------------------

Es gibt zwei Möglichkeiten, ein Betriebssystem auf der SSD zu installieren:

**System von der Micro-SD-Karte auf die SSD kopieren**

#. Schließen Sie einen Bildschirm an oder greifen Sie über VNC Viewer auf den Raspberry Pi Desktop zu. Klicken Sie dann auf **Raspberry Pi Logo** -> **Zubehör** -> **SD-Karten-Kopierer**.

   .. image:: img/ssd_copy.png
      
    
#. Stellen Sie sicher, dass Sie die richtigen Geräte für **Von kopieren** und **Nach kopieren** auswählen. Achten Sie darauf, sie nicht zu verwechseln.

   .. image:: img/ssd_copy_from.png
      
#. Klicken Sie nach der Auswahl auf **Starten**.

   .. image:: img/ssd_copy_start.png

#. Sie werden aufgefordert, dass der Inhalt auf der SSD gelöscht wird. Sichern Sie Ihre Daten, bevor Sie auf Ja klicken.

   .. image:: img/ssd_copy_erase.png

#. Warten Sie eine Weile, und der Kopiervorgang wird abgeschlossen.


**System mit Raspberry Pi Imager installieren**

Wenn auf Ihrer Micro-SD-Karte eine Desktop-Version des Systems installiert ist, können Sie ein Imaging-Tool (wie Raspberry Pi Imager) verwenden, um das System auf die SSD zu schreiben. Dieses Beispiel verwendet Raspberry Pi OS Bookworm, andere Systeme erfordern möglicherweise eine vorherige Installation des Imaging-Tools.

#. Schließen Sie einen Bildschirm an oder greifen Sie über VNC Viewer auf den Raspberry Pi Desktop zu. Klicken Sie dann auf **Raspberry Pi Logo** -> **Zubehör** -> **Imager**.

   .. image:: img/ssd_imager.png

      
#. Wählen Sie im |link_rpi_imager| die Option **Raspberry Pi Gerät** und wählen Sie das Modell **Raspberry Pi 5** aus dem Dropdown-Menü aus.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Wählen Sie **Betriebssystem** und entscheiden Sie sich für die empfohlene Betriebssystemversion.

   .. image:: img/ssd_os.png
      :width: 90%
    
#. Wählen Sie im Menü **Speicher** Ihre eingesetzte NVMe-SSD aus.

   .. image:: img/nvme_storage.png
      :width: 90%
    
#. Klicken Sie auf **Weiter** und dann auf **Einstellungen bearbeiten**, um Ihre Betriebssystemeinstellungen anzupassen.

   .. note::

      Wenn Sie einen Monitor für Ihren Raspberry Pi haben, können Sie die nächsten Schritte überspringen und 'Ja' auswählen, um mit der Installation zu beginnen. Passen Sie die anderen Einstellungen später am Monitor an.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Definieren Sie einen **Hostnamen** für Ihren Raspberry Pi.

   .. note::

      Der Hostname ist die Netzwerkkennung Ihres Raspberry Pi. Sie können auf Ihren Pi über ``<hostname>.local`` oder ``<hostname>.lan`` zugreifen.

   .. image:: img/os_set_hostname.png
      

#. Erstellen Sie einen **Benutzernamen** und ein **Passwort** für das Administratorkonto des Raspberry Pi.

   .. note::

      Die Einrichtung eines eindeutigen Benutzernamens und Passworts ist entscheidend, um Ihren Raspberry Pi zu sichern, der kein Standardpasswort besitzt.

   .. image:: img/os_set_username.png
      

#. Konfigurieren Sie das drahtlose LAN, indem Sie die **SSID** und das **Passwort** Ihres Netzwerks eingeben.

   .. note::

      Stellen Sie das ``WLAN-Land`` auf den entsprechenden `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_  für Ihren Standort ein.

   .. image:: img/os_set_wifi.png

#. Aktivieren Sie **SSH** im Tab **Dienste**, um sich aus der Ferne mit Ihrem Raspberry Pi zu verbinden.

   * Für **Passwort-Authentifizierung** verwenden Sie den Benutzernamen und das Passwort aus dem Tab **Allgemein**.
   * Für die Authentifizierung mit öffentlichen Schlüsseln wählen Sie "Nur öffentliche Schlüssel zulassen". Falls Sie keinen RSA-Schlüssel haben, wird einer generiert. Falls nicht, klicken Sie auf "SSH-Schlüssel erzeugen", um ein neues Schlüsselpaar zu erstellen.

   .. image:: img/os_enable_ssh.png

      

#. Im Menü **Optionen** können Sie das Verhalten von Imager während des Schreibvorgangs konfigurieren, einschließlich akustischer Benachrichtigung bei Abschluss, Auswerfen des Mediums bei Abschluss und Aktivieren der Telemetrie.

   .. image:: img/os_options.png
    
#. Nachdem Sie die Einstellungen angepasst haben, klicken Sie auf **Speichern**, um Ihre Anpassungen zu sichern. Klicken Sie anschließend auf **Ja**, um sie beim Schreiben des Abbilds zu übernehmen.

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. Falls die NVMe-SSD bereits Daten enthält, sichern Sie diese, um Datenverlust zu vermeiden. Klicken Sie auf **Ja**, falls keine Sicherung benötigt wird.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Wenn die Meldung "Schreiben erfolgreich" erscheint, wurde Ihr Abbild vollständig geschrieben und überprüft. Jetzt können Sie einen Raspberry Pi von der NVMe-SSD starten!

   .. image:: img/nvme_install_finish.png
      :width: 90%
      

.. _configure_boot_ssd:

3. Boot von der SSD konfigurieren
---------------------------------------

* Um die Firmware Ihres Raspberry Pi auf die neueste Version zu aktualisieren, verwenden Sie ``rpi-update``.

  .. code-block:: shell

    sudo rpi-update

* Um den Boot-Support zu aktivieren, müssen Sie die ``BOOT_ORDER`` in der Bootloader-Konfiguration ändern. Bearbeiten Sie die EEPROM-Konfiguration durch:

  .. code-block:: shell
  
    sudo rpi-eeprom-config --edit
  
* Ändern Sie dann die Zeile ``BOOT_ORDER`` wie unten angegeben. ``0xf416``: Versuchen Sie zuerst die NVMe-SSD, gefolgt von der SD-Karte und dann USB.

  .. code-block:: shell
  
    BOOT_ORDER=0xf416

  .. note::
    
    Ändern Sie nur die Reihenfolge, in der der Raspberry Pi startet, aber entfernen Sie keine anderen Startoptionen. Dies stellt sicher, dass er immer richtig startet.


Die Einstellung ``BOOT_ORDER`` ermöglicht eine flexible Konfiguration der Priorität für verschiedene Boot-Modi. Sie wird als 32-Bit-Ganzzahl dargestellt, wobei jedes Nibble einen Boot-Modus repräsentiert. Die Boot-Modi werden in der Reihenfolge vom niedrigstwertigen zum höchstwertigen Nibble ausgeführt.
Die Eigenschaft ``BOOT_ORDER`` definiert die Reihenfolge der verschiedenen Boot-Modi. Sie wird von rechts nach links gelesen, und es können bis zu acht Stellen definiert werden.

.. image:: img/boot_order.png
      :width: 90%
      

* ``0xf41``: Versuchen Sie zuerst die SD-Karte, gefolgt von USB-MSD, dann wiederholen (Standard, falls ``BOOT_ORDER`` leer ist).
* ``0xf14``: Versuchen Sie zuerst USB, gefolgt von der SD-Karte, dann wiederholen.

* Sobald das Update abgeschlossen ist, starten Sie Ihren Raspberry Pi neu, damit die Änderungen wirksam werden.

.. code-block:: shell

    sudo reboot



