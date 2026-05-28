.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _copy_sd_to_nvme_max:

Betriebssystem von der Micro-SD-Karte auf eine NVMe-SSD kopieren
==================================================================

Wenn Sie eine NVMe-SSD besitzen, aber keinen Adapter haben, um sie mit Ihrem Computer zu verbinden, können Sie einen dritten Ansatz wählen: Installieren Sie das System zunächst auf Ihrer Micro-SD-Karte. Nachdem der Pironman 5 MAX erfolgreich gestartet ist, können Sie das System von der Micro-SD-Karte auf Ihre NVMe-SSD übertragen.

* Zuerst müssen Sie :ref:`install_os_sd_rpi_max` abschließen.
* Starten Sie anschließend Ihren Raspberry Pi und melden Sie sich an. Wenn Sie nicht sicher sind, wie Sie sich anmelden, können Sie die offizielle Raspberry-Pi-Website besuchen: |link_rpi_get_start|.

Führen Sie die oben genannten Schritte vollständig aus, bevor Sie mit den folgenden Anweisungen fortfahren.


1. PCIe aktivieren
--------------------

Standardmäßig ist der PCIe-Anschluss nicht aktiviert.

* Um ihn zu aktivieren, öffnen Sie die Datei ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Fügen Sie anschließend die folgende Zeile zur Datei hinzu.

  .. code-block:: shell
  
    # Externen PCIe-Anschluss aktivieren
    dtparam=pciex1
  
* Für ``pciex1`` existiert ein leichter zu merkender Alias. Alternativ können Sie daher auch ``dtparam=nvme`` zur Datei ``/boot/firmware/config.txt`` hinzufügen.

  .. code-block:: shell
  
    dtparam=nvme

.. * Die Verbindung ist für Gen-2.0-Geschwindigkeiten (5 GT/s) zertifiziert, Sie können sie jedoch auf Gen 3.0 (10 GT/s) erzwingen, indem Sie die folgenden Zeilen zur Datei ``/boot/firmware/config.txt`` hinzufügen.

..   .. code-block:: shell
  
..     # Gen-3.0-Geschwindigkeit erzwingen
..     dtparam=pciex1_gen=3
  
..   .. warning::
  
..     Der Raspberry Pi 5 ist nicht für Gen-3.0-Geschwindigkeiten zertifiziert, und Verbindungen zu PCIe-Geräten mit diesen Geschwindigkeiten können instabil sein.

*  Sie müssen die PCIe-Boot-Verzögerung deaktivieren, damit der Raspberry Pi das NVMe-Laufwerk hinter dem PCIe-Switch beim Start erkennen kann. Fügen Sie dazu die folgende Zeile zur Datei ``/boot/firmware/config.txt`` hinzu:

   .. code-block:: shell

      dtparam=pciex1_no_10s=on


* Drücken Sie ``Strg + X``, anschließend ``Y`` und dann ``Enter``, um die Änderungen zu speichern.


**BOOT_ORDER**

Wenn Sie zwei NVMe-Systemlaufwerke installiert haben und auswählen möchten, von welchem gebootet werden soll, 
können Sie den Eintrag ``ROOT=PARTUUID=xxxxxxxxx`` in der Datei ``/boot/firmware/cmdline.txt`` auf die UUID des gewünschten Laufwerks ändern. Die UUID des Laufwerks können Sie mit folgendem Befehl ermitteln:

.. code-block:: shell

   ls /dev/disk/by-id/

.. start_copy_nvme

2. Betriebssystem auf der SSD installieren
----------------------------------------------------

Es gibt zwei Möglichkeiten, ein Betriebssystem auf der SSD zu installieren:

**Kopieren des Systems von der Micro-SD-Karte auf die SSD**

#. Schließen Sie einen Bildschirm an oder greifen Sie über den VNC Viewer auf den Raspberry-Pi-Desktop zu. Klicken Sie dann auf **Raspberry-Pi-Logo** -> **Zubehör** -> **SD-Card-Copier**.

   .. image:: img/ssd_copy.png
      
    
#. Stellen Sie sicher, dass Sie die richtigen Geräte für **Copy From** und **Copy To** auswählen. Achten Sie darauf, diese nicht zu verwechseln.

   .. image:: img/ssd_copy_from.png
      
#. Denken Sie daran, **„NEW Partition UUIDs“** auszuwählen, damit das System die Geräte korrekt unterscheiden kann und Mount-Konflikte sowie Boot-Probleme vermieden werden.

   .. image:: img/ssd_copy_uuid.png
    
#. Klicken Sie nach der Auswahl auf **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Sie werden darauf hingewiesen, dass der Inhalt der SSD gelöscht wird. Sichern Sie Ihre Daten, bevor Sie auf **Yes** klicken. Warten Sie einige Zeit, bis der Kopiervorgang abgeschlossen ist.

**Installation des Systems mit Raspberry Pi Imager**

Wenn auf Ihrer Micro-SD-Karte eine Desktop-Version des Systems installiert ist, können Sie ein Imaging-Tool (z. B. Raspberry Pi Imager) verwenden, um das System auf die SSD zu schreiben. In diesem Beispiel wird Raspberry Pi OS Bookworm verwendet, andere Systeme erfordern möglicherweise zunächst die Installation des Imaging-Tools.

#. Schließen Sie einen Bildschirm an oder greifen Sie über den VNC Viewer auf den Raspberry-Pi-Desktop zu. Klicken Sie dann auf **Raspberry-Pi-Logo** -> **Zubehör** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Stecken Sie Ihre Micro-SD-Karte mithilfe eines Kartenlesers in Ihren Computer. Sichern Sie vor dem Fortfahren alle wichtigen Daten.

   .. image:: img/insert_sd.png
      :width: 90%

#. Nach dem Start des Raspberry Pi Imager sehen Sie die Seite **Device**. Wählen Sie dort Ihr Raspberry-Pi-5-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

#. Wechseln Sie zum Abschnitt **OS** und wählen Sie die empfohlene Option **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

#. Wählen Sie im Abschnitt **Storage** Ihre **NVMe-SSD** aus.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_max:

3. Start von der SSD konfigurieren
---------------------------------------

In diesem Abschnitt konfigurieren wir Ihren Raspberry Pi so, dass er direkt von einer NVMe-SSD startet. Dies sorgt für schnellere Startzeiten und eine bessere Leistung im Vergleich zu einer SD-Karte. Befolgen Sie diese Schritte sorgfältig:

#. Öffnen Sie zunächst ein Terminal auf Ihrem Raspberry Pi und führen Sie den folgenden Befehl aus, um die Konfigurationsoberfläche zu öffnen:

   .. code-block:: shell

      sudo raspi-config

#. Navigieren Sie im Menü ``raspi-config`` mit den Pfeiltasten und wählen Sie **Advanced Options**. Drücken Sie ``Enter``, um auf die erweiterten Einstellungen zuzugreifen.

   .. image:: img/nvme_open_config.png

#. Wählen Sie innerhalb von **Advanced Options** den Punkt **Boot Order** aus. Mit dieser Einstellung legen Sie fest, in welcher Reihenfolge Ihr Raspberry Pi nach startfähigen Geräten sucht.

   .. image:: img/nvme_boot_order.png

#. Wählen Sie anschließend **NVMe/USB boot**. Dadurch wird festgelegt, dass der Raspberry Pi den Start von über USB angeschlossenen SSDs oder NVMe-Laufwerken gegenüber anderen Optionen, wie z. B. der SD-Karte, priorisiert.

   .. image:: img/nvme_boot_nvme.png

#. Nachdem Sie die Boot-Reihenfolge ausgewählt haben, drücken Sie **Finish**, um raspi-config zu beenden. Alternativ können Sie auch die **Escape**-Taste verwenden, um das Konfigurationstool zu schließen.

   .. image:: img/nvme_boot_ok.png

#. Um die neuen Boot-Einstellungen anzuwenden, starten Sie Ihren Raspberry Pi neu, indem Sie ``sudo reboot`` ausführen.

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

Nach dem Neustart sollte der Raspberry Pi nun versuchen, von der angeschlossenen NVMe-SSD zu booten, wodurch Sie eine verbesserte Leistung und höhere Zuverlässigkeit für Ihr System erhalten.

.. end_copy_nvme
