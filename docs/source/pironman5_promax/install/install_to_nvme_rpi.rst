.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_to_nvme_rpi_promax:

Betriebssystem auf einer NVMe-SSD installieren
================================================================

Wenn Sie eine NVMe-SSD verwenden und einen Adapter besitzen, um die NVMe-SSD zur Systeminstallation mit Ihrem Computer zu verbinden, können Sie das folgende Tutorial für eine schnelle Installation nutzen.

**Benötigte Komponenten**

* Ein Personal Computer
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Micro-SD-Karte und Kartenleser


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_promax:


2. Bootloader aktualisieren
--------------------------------

Aktualisieren Sie zuerst den Bootloader des Raspberry Pi 5, sodass er zuerst versucht, von **NVMe** zu booten, dann von **USB** und schließlich von der **SD-Karte**.

.. note::

    Es wird empfohlen, für diesen Schritt eine **zusätzliche Micro-SD-Karte** zu verwenden.

    - Methode 1 (Empfohlen): Schreiben Sie den Bootloader auf eine Micro-SD-Karte, legen Sie sie in den Raspberry Pi ein und booten Sie einmal, um die Einstellung zu übernehmen.
    - Methode 2: Schreiben Sie den Bootloader direkt auf die NVMe-SSD. Verbinden Sie danach die NVMe mit einem Computer, um das Betriebssystem zu installieren, und setzen Sie sie dann wieder in den Raspberry Pi ein.

#. Legen Sie die zusätzliche **Micro-SD-Karte oder NVMe-SSD** mit einem Kartenleser oder Adapter in Ihren Computer ein.

#. Wenn Raspberry Pi Imager geöffnet wird, sehen Sie die Seite **Gerät**. Wählen Sie Ihr Raspberry Pi 5-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

#. Klicken Sie auf **Betriebssystem**.

   * Scrollen Sie nach unten und wählen Sie **Dienstprogramm-Images**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Wählen Sie **Bootloader (Pi 5 Familie)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Wählen Sie **NVMe/USB-Start**, um die Startreihenfolge festzulegen, und klicken Sie dann auf **WEITER**.

     .. image:: img/nvme_boot.png
        :width: 90%


#. Wählen Sie unter **Speicher** die richtige Micro-SD-Karte oder NVMe-SSD aus und klicken Sie dann auf **WEITER**.

   .. note::

      Stellen Sie sicher, dass das richtige Gerät ausgewählt ist. Trennen Sie bei Bedarf andere Speichergeräte.

   .. image:: img/imager_storage.png
      :width: 90%

#. Überprüfen Sie die Einstellungen und klicken Sie auf **SCHREIBEN**, um zu starten.

   .. image:: img/nvme_write.png
      :width: 90%

#. Bestätigen Sie die Warnung und erlauben Sie dem Raspberry Pi Imager, den Bootloader zu löschen und zu schreiben.

   .. image:: img/imager_erase.png
      :width: 90%

#. Warten Sie, bis **Schreiben abgeschlossen!** erscheint, und entfernen Sie dann sicher das Speichergerät.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Legen Sie die Micro-SD-Karte in den Raspberry Pi ein und schalten Sie ihn einmal ein, um das Bootloader-Update zu übernehmen.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Warten Sie nach dem Hochfahren des Raspberry Pi mindestens **10 Sekunden**, schalten Sie ihn dann aus und entfernen Sie die Micro-SD-Karte oder NVMe-SSD.

Der Raspberry Pi 5 ist jetzt bereit, von **NVMe** zu booten.

.. end_update_bootloader

3. Betriebssystem auf NVMe-SSD installieren
----------------------------------------------------------------------------------

Jetzt können Sie das Betriebssystem auf Ihrer NVMe-SSD installieren.

#. Schließen Sie die **NVMe-SSD** mit einem Adapter an Ihren Computer an.

2. Wenn Raspberry Pi Imager geöffnet wird, sehen Sie die Seite **Gerät**. Wählen Sie Ihr Raspberry Pi 5-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

3. Gehen Sie zum Bereich **Betriebssystem** und wählen Sie die empfohlene Option **Raspberry Pi OS (64-bit)**.

   .. warning::

      Achten Sie darauf, eine **64-Bit**-Version zu wählen. Wenn Sie ein **32-Bit**-System installieren, sind einige Pakete nur für ``aarch64`` (64 Bit) verfügbar, und bestimmte Funktionen lassen sich möglicherweise nicht installieren oder funktionieren nicht richtig.

   .. image:: img/imager_os.png
      :width: 90%

4. Wählen Sie im Bereich **Speicher** Ihre **NVMe-SSD** aus.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os