.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!


Installation von Umbrel OS
============================================

Umbrel ist ein Open-Source-Betriebssystem (OS) für Heimserver, mit dem du deinen eigenen Bitcoin-Node betreiben, eine Vielzahl von selbstgehosteten Apps mit einem Klick installieren und deine Hardware in deine persönliche Cloud verwandeln kannst. Es ist ein hervorragender Weg, um mit Selbstverwahrung und Datenschutz zu beginnen.

**Erforderliche Komponenten**

* Ein Personal Computer  
* Eine NVMe-SSD  
* Ein NVMe-zu-USB-Adapter  
* Eine Micro-SD-Karte und ein Kartenleser


1. Bootloader aktualisieren
--------------------------------

Zuerst muss der Bootloader des Raspberry Pi 5 aktualisiert werden, damit er zuerst von NVMe startet, bevor er versucht, von USB oder der SD-Karte zu booten.

.. note::

    * In diesem Schritt wird empfohlen, eine Ersatz-Micro-SD-Karte zu verwenden. Schreibe den Bootloader zunächst auf diese Micro-SD-Karte und stecke sie dann sofort in den Raspberry Pi, um das Booten von einem NVMe-Gerät zu aktivieren.  
    * Alternativ kannst du den Bootloader direkt auf dein NVMe-Gerät schreiben, es dann in den Raspberry Pi einsetzen, um die Bootmethode zu ändern. Anschließend schließe die NVMe-SSD an einen Computer an, um das Betriebssystem zu installieren, und stecke sie nach Abschluss der Installation wieder in den Raspberry Pi.

#. Stecke deine Micro-SD-Karte oder NVMe-SSD mithilfe eines Kartenlesers in den Computer oder Laptop.

#. In |link_rpi_imager| klicke auf **Raspberry Pi Device** und wähle das Modell **Raspberry Pi 5** aus dem Dropdown-Menü.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Im Reiter **Operating System** scrolle nach unten und wähle **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Wähle **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Wähle **NVMe/USB Boot**, um dem Raspberry Pi 5 zu erlauben, zuerst von NVMe, dann von USB und schließlich von der SD-Karte zu starten.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      
#. Unter **Storage** wähle das passende Speichermedium für die Installation aus.

   .. note::

      Stelle sicher, dass du das richtige Speichermedium auswählst. Um Verwechslungen zu vermeiden, trenne zusätzliche Speichermedien, falls mehrere angeschlossen sind.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Nun kannst du auf **NEXT** klicken. Wenn das Speichermedium bereits Daten enthält, sichere diese, um Datenverlust zu vermeiden. Klicke auf **Yes**, wenn kein Backup erforderlich ist.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Nach kurzer Zeit wird dir mitgeteilt, dass **NVMe/USB Boot** auf dein Speichermedium geschrieben wurde.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Stecke deine Micro-SD-Karte oder NVMe-SSD in den Raspberry Pi. Sobald das USB-C-Netzteil angeschlossen ist, wird der Bootloader von der Micro-SD-Karte oder NVMe-SSD in den EEPROM des Raspberry Pi geschrieben.

   .. note::

      * Nach der Aktualisierung startet der Raspberry Pi zuerst von der NVMe-SSD, dann von USB und zuletzt von der Micro-SD-Karte.  
      * Warte ein bis zwei Minuten, schalte dann den Raspberry Pi aus und entferne die Micro-SD-Karte oder die NVMe-SSD.

2. Installation des Betriebssystems auf der NVMe-SSD
------------------------------------------------------------

**Schritte**

1. Lade das neueste Umbrel-OS-Image herunter und entpacke es. Du kannst auch die `Umbrel-Release-Seite <https://github.com/getumbrel/umbrel/releases>`_ besuchen, um eine bestimmte Version auszuwählen.

   * :download:`Neueste Umbrel-OS-Image-Datei <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. Öffne |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle **Raspberry Pi 5** aus dem Dropdown-Menü.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. Starte den **Raspberry Pi Imager** und klicke auf **CHOOSE OS**.

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. Scrolle bis zum Ende und wähle **Use custom**.

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. Wähle die zuvor heruntergeladene Umbrel-OS-Image-Datei aus und klicke auf **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. Wähle unter **Storage** die NVMe-SSD als Ziel für die Installation aus.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. Klicke auf **NEXT** und dann auf **NO**. Umbrel OS initialisiert automatisch sein eigenes System und die Benutzereinrichtung beim ersten Start und verwendet keine im Raspberry Pi Imager gesetzten Benutzer- oder Passwortdaten.

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. Wenn sich auf der NVMe-SSD bereits Daten befinden, erstelle vor dem Fortfahren ein Backup, um Datenverlust zu vermeiden. Klicke auf **Yes**, um fortzufahren, wenn kein Backup erforderlich ist.

   .. image:: img/nvme_erase.png
      :width: 90%

9. Wenn die Meldung „Write Successful“ erscheint, bedeutet das, dass das Image vollständig geschrieben und überprüft wurde. Deine NVMe-SSD ist nun bereit, den Raspberry Pi zu starten!

   .. image:: img/umbrel_finish.png
      :width: 90%

