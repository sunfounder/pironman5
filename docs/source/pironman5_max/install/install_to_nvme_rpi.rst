.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_rpi_max:

Installation des Betriebssystems auf einer NVMe-SSD
=============================================================

Wenn Sie eine NVMe-SSD verwenden und über einen Adapter verfügen, um die NVMe-SSD für die Systeminstallation mit Ihrem Computer zu verbinden, können Sie die folgende Anleitung für eine schnelle Installation nutzen.

**Erforderliche Komponenten**

* Ein Personal Computer
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Micro-SD-Karte und Kartenleser


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_max:


2. Bootloader aktualisieren
--------------------------------

Aktualisieren Sie zunächst den Bootloader des Raspberry Pi 5 so, dass er zuerst von **NVMe**, dann von **USB** und zuletzt von der **SD-Karte** zu booten versucht.

.. note::

    Für diesen Schritt wird empfohlen, eine **zusätzliche Micro-SD-Karte** zu verwenden.
    
    - Methode 1 (empfohlen): Schreiben Sie den Bootloader auf eine Micro-SD-Karte, setzen Sie sie in den Raspberry Pi ein und starten Sie ihn einmal, um die Einstellung zu übernehmen.
    - Methode 2: Schreiben Sie den Bootloader direkt auf die NVMe-SSD. Schließen Sie die NVMe anschließend an einen Computer an, um das Betriebssystem zu installieren, und setzen Sie sie danach wieder in den Raspberry Pi ein.

#. Setzen Sie die zusätzliche **Micro-SD-Karte oder NVMe-SSD** mithilfe eines Kartenlesers oder Adapters in Ihren Computer ein.

#. Wenn der Raspberry Pi Imager geöffnet wird, sehen Sie die Seite **Device**. Wählen Sie Ihr Raspberry-Pi-5-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

#. Klicken Sie auf **OS**.

   * Scrollen Sie nach unten und wählen Sie **Misc utility images**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Wählen Sie **Bootloader (Pi 5 family)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Wählen Sie **NVMe/USB Boot**, um die Boot-Reihenfolge festzulegen, und klicken Sie anschließend auf **NEXT**.

     .. image:: img/nvme_boot.png
        :width: 90%


#. Wählen Sie im Abschnitt **Storage** die richtige Micro-SD-Karte oder NVMe-SSD aus und klicken Sie auf **NEXT**.

   .. note::

      Stellen Sie sicher, dass das richtige Laufwerk ausgewählt ist. Trennen Sie bei Bedarf andere Speichermedien.

   .. image:: img/imager_storage.png
      :width: 90%


#. Überprüfen Sie die Einstellungen und klicken Sie auf **WRITE**, um zu starten.

   .. image:: img/nvme_write.png
      :width: 90%

#. Bestätigen Sie die Warnmeldung und erlauben Sie dem Raspberry Pi Imager, den Bootloader zu löschen und zu schreiben.

   .. image:: img/imager_erase.png
      :width: 90%

#. Warten Sie, bis **Write complete!** angezeigt wird, und entfernen Sie anschließend das Speichermedium sicher.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Setzen Sie die Micro-SD-Karte in den Raspberry Pi ein und schalten Sie ihn einmal ein, um das Bootloader-Update anzuwenden.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Warten Sie mindestens **10 Sekunden**, nachdem der Raspberry Pi den Startvorgang abgeschlossen hat, schalten Sie ihn dann aus und entfernen Sie die Micro-SD-Karte oder NVMe-SSD.

Der Raspberry Pi 5 ist nun bereit, von **NVMe** zu booten.

.. end_update_bootloader

3. Betriebssystem auf der NVMe-SSD installieren
----------------------------------------------------------

Nun können Sie das Betriebssystem auf Ihrer NVMe-SSD installieren.

#. Setzen Sie die **NVMe-SSD** mithilfe eines Adapters in Ihren Computer ein.

2. Wenn der Raspberry Pi Imager geöffnet wird, sehen Sie die Seite **Device**.  
   Wählen Sie Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

3. Wechseln Sie zum Abschnitt **OS** und wählen Sie die empfohlene Option **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

4. Wählen Sie im Abschnitt **Storage** Ihre **NVMe-SSD** aus.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

