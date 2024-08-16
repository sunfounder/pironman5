.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _install_to_nvme_ubuntu:

Installation des Betriebssystems auf einer NVMe-SSD
=========================================================

Wenn Sie eine NVMe-SSD verwenden und über einen Adapter verfügen, um die NVMe-SSD für die Systeminstallation mit Ihrem Computer zu verbinden, können Sie das folgende Tutorial für eine schnelle Installation nutzen.

**Erforderliche Komponenten**

* Ein PC
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Eine Micro-SD-Karte und ein Kartenleser

.. _update_bootloader:

1. Aktualisierung des Bootloaders
---------------------------------------

Zuerst müssen Sie den Bootloader des Raspberry Pi 5 aktualisieren, damit dieser zuerst von der NVMe-SSD bootet, bevor USB und dann die SD-Karte ausprobiert werden.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    In diesem Schritt wird empfohlen, eine Ersatz-Micro-SD-Karte zu verwenden. Schreiben Sie zuerst den Bootloader auf diese Micro-SD-Karte und stecken Sie sie dann sofort in den Raspberry Pi, um das Booten von einem NVMe-Gerät zu ermöglichen.
    
    Alternativ können Sie den Bootloader direkt auf Ihr NVMe-Gerät schreiben, dieses dann in den Raspberry Pi einsetzen, um die Bootmethode zu ändern. Danach verbinden Sie die NVMe-SSD mit einem Computer, um das Betriebssystem zu installieren. Sobald die Installation abgeschlossen ist, setzen Sie es zurück in den Raspberry Pi ein.

#. Setzen Sie Ihre Ersatz-Micro-SD-Karte oder NVMe-SSD über einen Kartenleser in Ihren Computer oder Laptop ein.

#. Klicken Sie im |link_rpi_imager| auf **Raspberry Pi Device** und wählen Sie das Modell **Raspberry Pi 5** aus der Dropdown-Liste.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Scrollen Sie im Tab **Betriebssystem** nach unten und wählen Sie **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. Wählen Sie **Bootloader (Pi 5 Familie)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Wählen Sie **NVMe/USB Boot**, um den Raspberry Pi 5 so einzustellen, dass er zuerst von der NVMe-SSD bootet, bevor er USB und dann die SD-Karte ausprobiert.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      

#. Wählen Sie im Tab **Speicher** das entsprechende Speichermedium für die Installation.

   .. note::

      Stellen Sie sicher, dass Sie das richtige Speichermedium auswählen. Um Verwechslungen zu vermeiden, trennen Sie alle anderen angeschlossenen Speichermedien.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Klicken Sie jetzt auf **Weiter**. Falls sich bereits Daten auf dem Speichermedium befinden, sichern Sie diese, um Datenverlust zu vermeiden. Klicken Sie auf **Ja**, wenn keine Sicherung erforderlich ist.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Sie werden bald darauf hingewiesen, dass **NVMe/USB Boot** auf Ihr Speichermedium geschrieben wurde.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Nun können Sie Ihre Micro-SD-Karte oder NVMe-SSD in den Raspberry Pi einsetzen. Nach dem Einschalten des Raspberry Pi mit einem Type-C-Adapter wird der Bootloader von der Micro-SD-Karte oder NVMe-SSD in das EEPROM des Raspberry Pi geschrieben.
.. note::

    Danach wird der Raspberry Pi zuerst von der NVMe-SSD booten, bevor er USB und dann die SD-Karte ausprobiert.
    
    Schalten Sie den Raspberry Pi aus und entfernen Sie die Micro-SD-Karte oder die NVMe-SSD.


2. Installation des Betriebssystems auf der NVMe-SSD
----------------------------------------------------------

Nun können Sie das Betriebssystem auf Ihrer NVMe-SSD installieren.

**Schritte**

#. Gehen Sie zuerst zur Seite |link_batocera_download|, wählen Sie **Raspberry Pi 5 B** aus und klicken Sie auf Download.

   .. image:: img/batocera_download.png
      :width: 90%
      

#. Setzen Sie Ihre SD-Karte mit einem Kartenleser in Ihren Computer oder Laptop ein.

#. Klicken Sie im |link_rpi_imager| auf den Tab **Betriebssystem**.

   .. image:: img/os_choose_os.png
      :width: 90%
      
#. Scrollen Sie bis zum unteren Ende der Seite und wählen Sie **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%
      

#. Wählen Sie die soeben heruntergeladene Systemdatei ``batocera-xxx-xx-xxxxxxxx.img.gz`` und klicken Sie auf **Öffnen**.

   .. image:: img/batocera_os_choose.png
      :width: 90%
      

#. Wählen Sie im Tab **Speicher** das entsprechende Speichermedium für die Installation aus.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      


#. Klicken Sie jetzt auf **Weiter**. Falls sich bereits Daten auf dem Speichermedium befinden, sichern Sie diese, um Datenverlust zu vermeiden. Klicken Sie auf **Ja**, wenn keine Sicherung erforderlich ist.

   .. image:: img/nvme_erase.png
      :width: 90%
      

#. Wenn Sie das Popup "Schreiben erfolgreich" sehen, wurde Ihr Image vollständig geschrieben und überprüft. Sie sind nun bereit, den Raspberry Pi von der NVMe-SSD zu booten!

