.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_copy_sd_to_nvme_rpi:

Betriebssystem von der Micro SD auf die NVMe SSD kopieren
==================================================================

Wenn du eine NVMe SSD hast, aber keinen Adapter, um sie an deinen Computer anzuschließen, kannst du eine dritte Methode verwenden: Installiere zunächst das System auf deiner Micro SD-Karte. Nachdem der Pironman 5 MAX erfolgreich hochgefahren ist, kannst du das System von der Micro SD auf die NVMe SSD übertragen.

* Zuerst musst du :ref:`max_install_os_sd_rpi` durchführen.
* Starte dann deinen Raspberry Pi und melde dich an. Falls du unsicher bist, wie du dich einloggst, besuche die offizielle Raspberry Pi-Website: |link_rpi_get_start|.

Schließe die obigen Schritte ab, bevor du mit den folgenden Anweisungen fortfährst.


1. PCIe aktivieren
--------------------

Standardmäßig ist der PCIe-Anschluss deaktiviert.

* Um ihn zu aktivieren, öffne die Datei ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Füge dann folgende Zeile in die Datei ein.

  .. code-block:: shell
  
    # PCIe externen Anschluss aktivieren.
    dtparam=pciex1
  
* Es gibt auch einen leichter zu merkenden Alias für ``pciex1``, du kannst alternativ ``dtparam=nvme`` in die Datei ``/boot/firmware/config.txt`` einfügen.

  .. code-block:: shell
  
    dtparam=nvme

.. * Die Verbindung ist für Gen 2.0 Geschwindigkeiten (5 GT/sec) zertifiziert, aber du kannst sie auf Gen 3.0 (10 GT/sec) erzwingen, indem du folgende Zeilen in deine ``/boot/firmware/config.txt`` hinzufügst.

..   .. code-block:: shell
  
..     # Erzwinge Gen 3.0 Geschwindigkeiten
..     dtparam=pciex1_gen=3
  
..   .. warning::
  
..     Der Raspberry Pi 5 ist nicht für Gen 3.0 Geschwindigkeiten zertifiziert, und Verbindungen zu PCIe-Geräten bei diesen Geschwindigkeiten könnten instabil sein.

* Du musst die PCIe-Startverzögerung deaktivieren, damit der Raspberry Pi das NVMe-Laufwerk hinter dem PCIe-Switch beim Start erkennen kann. Füge folgende Zeile zu ``/boot/firmware/config.txt`` hinzu:

   .. code-block:: shell

      dtparam=pciex1_no_10s=on


* Drücke ``Ctrl + X``, ``Y`` und ``Enter``, um die Änderungen zu speichern.


**BOOT_ORDER**

Wenn du zwei NVMe-Systemlaufwerke installiert hast und eines auswählen musst, 
von dem du booten möchtest, kannst du ``ROOT=PARTUUID=xxxxxxxxx`` in der Datei ``/boot/firmware/cmdline.txt`` auf die UUID des Laufwerks ändern, von dem du booten möchtest. Du kannst die UUID des Laufwerks mit folgendem Befehl finden:

.. code-block:: shell

   ls /dev/disk/by-id/


2. Betriebssystem auf der SSD installieren
---------------------------------------------

Es gibt zwei Möglichkeiten, ein Betriebssystem auf der SSD zu installieren:

**System von der Micro SD-Karte auf die SSD kopieren**

#. Schließe ein Display an oder greife über VNC Viewer auf den Raspberry Pi-Desktop zu. Klicke dann auf **Raspberry Pi-Logo** -> **Zubehör** -> **SD-Kartenkopierer**.

   .. image:: img/ssd_copy.png
      

#. Stelle sicher, dass du die richtigen Geräte für **Kopie von** und **Kopie auf** auswählst. Sei vorsichtig, damit du sie nicht vertauschst.

   .. image:: img/ssd_copy_from.png

#. Denke daran, "NEUE Partition UUIDs" auszuwählen, um sicherzustellen, dass das System die Geräte korrekt unterscheiden kann und keine Konflikte beim Mounten oder Booten auftreten.

   .. image:: img/ssd_copy_uuid.png
    
#. Nach der Auswahl klicke auf **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Es wird eine Warnung angezeigt, dass der Inhalt auf der SSD gelöscht wird. Stelle sicher, dass du deine Daten gesichert hast, bevor du auf Ja klickst.

   .. image:: img/ssd_copy_erase.png

#. Warte eine Weile, und der Kopiervorgang wird abgeschlossen.


**System mit Raspberry Pi Imager installieren**

Wenn auf deiner Micro SD-Karte eine Desktop-Version des Systems installiert ist, kannst du ein Imaging-Tool (wie den Raspberry Pi Imager) verwenden, um das System auf die SSD zu brennen. In diesem Beispiel wird Raspberry Pi OS Bookworm verwendet, aber andere Systeme erfordern möglicherweise zuerst die Installation des Imaging-Tools.

#. Schließe ein Display an oder greife über VNC Viewer auf den Raspberry Pi-Desktop zu. Klicke dann auf **Raspberry Pi-Logo** -> **Accessories** -> **Imager**.

   .. image:: img/ssd_imager.png
      

#. Wähle im |link_rpi_imager| die **Raspberry Pi Device**-Option und wähle das Modell **Raspberry Pi 5** aus der Dropdown-Liste.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Wähle das **Operating System** und die empfohlene Version des Betriebssystems aus.

   .. image:: img/ssd_os.png
      :width: 90%
    
#. Wähle unter **Storage** deine eingesteckte NVMe SSD aus.

   .. image:: img/nvme_storage.png
      :width: 90%
    
#. Klicke auf **NEXT** und dann auf **EDIT SETTINGS**, um deine OS-Einstellungen anzupassen.

   .. note::

      Wenn du ein Monitor für deinen Raspberry Pi hast, kannst du die nächsten Schritte überspringen und auf „Ja“ klicken, um mit der Installation zu beginnen. Passe andere Einstellungen später am Monitor an.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Lege einen **hostname** für deinen Raspberry Pi fest.

   .. note::

      Der Hostname ist der Netzwerkbezeichner deines Raspberry Pi. Du kannst auf deinen Pi zugreifen, indem du ``<hostname>.local`` oder ``<hostname>.lan`` verwendest.

   .. image:: img/os_set_hostname.png
      

#. Erstelle einen **Username** und ein **Password** für das Administrator-Konto des Raspberry Pi.

   .. note::

      Ein einzigartiger Benutzername und ein Passwort sind wichtig, um deinen Raspberry Pi zu sichern, da er kein Standardpasswort hat.

   .. image:: img/os_set_username.png
      

#. Konfiguriere das drahtlose LAN, indem du den **SSID** und das **Passwort** deines Netzwerks angibst.

   .. note::

      Setze das ``Wireless LAN country`` auf den zweibuchstabigen `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ für deinen Standort.

   .. image:: img/os_set_wifi.png

#. Um remote auf deinen Raspberry Pi zuzugreifen, **enable SSH** im **Services**-Tab.

   * Für **password authentication** verwende den Benutzernamen und das Passwort aus dem **General**-Tab.
   * Für die öffentliche Schlüssel-Authentifizierung wähle „Nur öffentliche Schlüssel-Authentifizierung zulassen“. Wenn du einen RSA-Schlüssel hast, wird dieser verwendet. Andernfalls klicke auf „SSH-Schlüssel generieren“, um ein neues Schlüsselpaar zu erstellen.

   .. image:: img/os_enable_ssh.png
      


#. Das Menü **Options** ermöglicht es dir, das Verhalten von Imager während des Schreibvorgangs zu konfigurieren, einschließlich des Abspielens von Sound, dem Auswerfen von Medien nach Abschluss und dem Aktivieren von Telemetrie.

   .. image:: img/os_options.png
    
#. Wenn du mit den Anpassungen des Betriebssystems fertig bist, klicke auf **Save**, um deine Anpassungen zu speichern. Klicke dann auf **Yes**, um sie beim Schreiben des Abbilds anzuwenden.

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. Wenn die NVMe SSD bereits Daten enthält, stelle sicher, dass du diese sicherst, um Datenverlust zu vermeiden. Klicke auf **Yes**, wenn kein Backup erforderlich ist.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Wenn du die „Schreibvorgang erfolgreich“-Meldung siehst, wurde dein Abbild erfolgreich geschrieben und überprüft. Dein Raspberry Pi ist nun bereit, von der NVMe SSD zu starten!

   .. image:: img/nvme_install_finish.png
      :width: 90%
      

.. _max_configure_boot_ssd:

3. Booten von der SSD konfigurieren
---------------------------------------

In diesem Abschnitt konfigurieren wir deinen Raspberry Pi so, dass er direkt von einer NVMe SSD bootet, was schnellere Bootzeiten und verbesserte Leistung im Vergleich zur SD-Karte bietet. Folge diesen Schritten sorgfältig:

#. Öffne zunächst ein Terminal auf deinem Raspberry Pi und führe den folgenden Befehl aus, um das Konfigurationsmenü zu öffnen:.

   .. code-block:: shell

      sudo raspi-config

#. Wähle im ``raspi-config``-Menü mit den Pfeiltasten **Advanced Options** und drücke ``Enter``, um die erweiterten Einstellungen aufzurufen.

   .. image:: img/nvme_open_config.png

#. Wähle unter **Advanced Options** die **Boot Order**. Diese Einstellung ermöglicht es dir, die Reihenfolge festzulegen, in der der Raspberry Pi nach bootfähigen Geräten sucht.

   .. image:: img/nvme_boot_order.png

#. Wähle dann **NVMe/USB boot**. Damit wird dem Raspberry Pi mitgeteilt, dass beim Start von USB-verbundenen SSDs oder NVMe-Laufwerken gebootet werden soll, anstatt von der SD-Karte.

   .. image:: img/nvme_boot_nvme.png

#. Nachdem du die Boot-Reihenfolge ausgewählt hast, drücke **Fertig**, um raspi-config zu verlassen. Du kannst auch die **Escape**-Taste verwenden, um das Konfigurationstool zu schließen.

   .. image:: img/nvme_boot_ok.png

#. Um die neuen Boot-Einstellungen anzuwenden, starte deinen Raspberry Pi neu, indem du ``sudo reboot`` ausführst.

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

Nach dem Neustart sollte der Raspberry Pi nun versuchen, von der angeschlossenen NVMe SSD zu booten, was dir verbesserte Leistung und Haltbarkeit für dein System bietet.


