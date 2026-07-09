.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _copy_sd_to_nvme_promax:

Betriebssystem von Micro-SD auf NVMe-SSD kopieren
==================================================================

Wenn Sie eine NVMe-SSD besitzen, aber keinen Adapter haben, um sie an Ihren Computer anzuschließen, können Sie einen dritten Ansatz wählen: Installieren Sie das System zunächst auf Ihrer Micro-SD-Karte. Nachdem der Pironman 5 Pro MAX erfolgreich hochgefahren ist, können Sie das System dann von Ihrer Micro-SD-Karte auf Ihre NVMe-SSD übertragen.

* Zuerst müssen Sie :ref:`install_os_sd_rpi_promax`.
* Starten Sie dann Ihren Raspberry Pi und melden Sie sich an. Wenn Sie nicht wissen, wie Sie sich anmelden, besuchen Sie die offizielle Raspberry Pi-Website: |link_rpi_get_start|.

Schließen Sie die oben genannten Schritte ab, bevor Sie mit den folgenden Anweisungen fortfahren.


1. PCIe aktivieren
--------------------

Standardmäßig ist der PCIe-Anschluss nicht aktiviert.

* Um ihn zu aktivieren, öffnen Sie die Datei ``/boot/firmware/config.txt``.

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* Fügen Sie dann die folgende Zeile zur Datei hinzu.

  .. code-block:: shell

    # Aktiviert den externen PCIe-Anschluss.
    dtparam=pciex1

* Es gibt einen einprägsameren Alias für ``pciex1``, sodass Sie alternativ ``dtparam=nvme`` zur Datei ``/boot/firmware/config.txt`` hinzufügen können.

  .. code-block:: shell

    dtparam=nvme

.. * Die Verbindung ist für Gen-2.0-Geschwindigkeiten (5 GT/sec) zertifiziert, aber Sie können sie auf Gen 3.0 (10 GT/sec) erzwingen, indem Sie die folgenden Zeilen zu Ihrer ``/boot/firmware/config.txt`` hinzufügen.

..   .. code-block:: shell

..     # Erzwingt Gen-3.0-Geschwindigkeiten
..     dtparam=pciex1_gen=3

..   .. warning::

..     Der Raspberry Pi 5 ist nicht für Gen-3.0-Geschwindigkeiten zertifiziert, und Verbindungen zu PCIe-Geräten mit diesen Geschwindigkeiten können instabil sein.

*  Sie müssen die PCIe-Startverzögerung deaktivieren, damit der Raspberry Pi das NVMe-Laufwerk hinter dem PCIe-Switch beim Start erkennen kann. Fügen Sie die folgende Zeile zur ``/boot/firmware/config.txt`` hinzu:

   .. code-block:: shell

      dtparam=pciex1_no_10s=on


* Drücken Sie ``Strg + X``, ``Y`` und ``Enter``, um die Änderungen zu speichern.


**BOOT_ORDER**

Wenn Sie zwei NVMe-Systemlaufwerke installiert haben und auswählen müssen, von welchem gebootet werden soll,
können Sie den Parameter ``ROOT=PARTUUID=xxxxxxxxx`` in der Datei ``/boot/firmware/cmdline.txt`` auf die UUID des gewünschten Laufwerks ändern. Die Laufwerks-UUID finden Sie mit dem folgenden Befehl:

.. code-block:: shell

   ls /dev/disk/by-id/


.. start_copy_nvme

2. Betriebssystem auf der SSD installieren
---------------------------------------------------------------------

Es gibt zwei Möglichkeiten, ein Betriebssystem auf der SSD zu installieren:

**System von der Micro-SD-Karte auf die SSD kopieren**

#. Schließen Sie ein Display an oder greifen Sie über VNC Viewer auf den Raspberry Pi-Desktop zu. Klicken Sie dann auf **Raspberry Pi-Logo** -> **Zubehör** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png


#. Stellen Sie sicher, dass Sie die korrekten Geräte für **Kopieren von** und **Kopieren nach** auswählen. Achten Sie darauf, sie nicht zu verwechseln.

   .. image:: img/ssd_copy_from.png

#. Denken Sie daran, "NEW Partition UUIDs" auszuwählen, um sicherzustellen, dass das System die Geräte korrekt unterscheiden kann und Einhängekonflikte sowie Startprobleme vermieden werden.

   .. image:: img/ssd_copy_uuid.png

#. Klicken Sie nach der Auswahl auf **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Sie werden darauf hingewiesen, dass der Inhalt auf der SSD gelöscht wird. Stellen Sie sicher, dass Sie Ihre Daten gesichert haben, bevor Sie auf Ja klicken. Warten Sie einige Zeit, bis der Kopiervorgang abgeschlossen ist.

**System mit Raspberry Pi Imager installieren**

Wenn auf Ihrer Micro-SD-Karte eine Desktop-Version des Systems installiert ist, können Sie ein Abbildungstool (wie Raspberry Pi Imager) verwenden, um das System auf die SSD zu übertragen. Dieses Beispiel verwendet Raspberry Pi OS Bookworm, bei anderen Systemen muss möglicherweise zuerst das Abbildungstool installiert werden.

#. Schließen Sie ein Display an oder greifen Sie über VNC Viewer auf den Raspberry Pi-Desktop zu. Klicken Sie dann auf **Raspberry Pi-Logo** -> **Zubehör** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Legen Sie Ihre microSD-Karte mit einem Kartenleser in Ihren Computer ein. Sichern Sie vor dem Fortfahren alle wichtigen Daten.

   .. image:: img/insert_sd.png
      :width: 90%

#. Wenn Raspberry Pi Imager geöffnet wird, sehen Sie die Seite **Gerät**. Wählen Sie Ihr Raspberry Pi 5-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

#. Gehen Sie zum Bereich **Betriebssystem** und wählen Sie die empfohlene Option **Raspberry Pi OS (64-bit)**.

   .. warning::

      Achten Sie darauf, eine **64-Bit**-Version zu wählen. Wenn Sie ein **32-Bit**-System installieren, sind einige Pakete nur für ``aarch64`` (64 Bit) verfügbar, und bestimmte Funktionen lassen sich möglicherweise nicht installieren oder funktionieren nicht richtig.

   .. image:: img/imager_os.png
      :width: 90%

#. Wählen Sie im Bereich **Speicher** Ihre **NVMe-SSD** aus.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_promax:

3. Booten von der SSD konfigurieren
---------------------------------------

In diesem Abschnitt konfigurieren wir Ihren Raspberry Pi so, dass er direkt von einer NVMe-SSD bootet, was schnellere Bootzeiten und eine verbesserte Leistung im Vergleich zu einer SD-Karte bietet. Befolgen Sie diese Schritte sorgfältig:

#. Öffnen Sie zunächst ein Terminal auf Ihrem Raspberry Pi und führen Sie den folgenden Befehl aus, um auf die Konfigurationsoberfläche zuzugreifen:

   .. code-block:: shell

      sudo raspi-config

#. Navigieren Sie im Menü ``raspi-config`` mit den Pfeiltasten und wählen Sie **Erweiterte Optionen**. Drücken Sie ``Enter``, um auf die erweiterten Einstellungen zuzugreifen.

   .. image:: img/nvme_open_config.png

#. Wählen Sie in den **Erweiterten Optionen** die Option **Startreihenfolge**. Diese Einstellung ermöglicht es Ihnen, die Reihenfolge festzulegen, in der Ihr Raspberry Pi nach bootfähigen Geräten sucht.

   .. image:: img/nvme_boot_order.png

#. Wählen Sie dann **NVMe/USB-Start**. Dies teilt dem Raspberry Pi mit, das Booten von USB-SSDs oder NVMe-Laufwerken gegenüber anderen Optionen wie der SD-Karte zu priorisieren.

   .. image:: img/nvme_boot_nvme.png

#. Wählen Sie nach der Festlegung der Startreihenfolge **Fertigstellen**, um raspi-config zu beenden. Sie können auch die **Escape**-Taste verwenden, um das Konfigurationstool zu schließen.

   .. image:: img/nvme_boot_ok.png

#. Um die neuen Boot-Einstellungen zu übernehmen, starten Sie Ihren Raspberry Pi mit ``sudo reboot`` neu.

   .. code-block:: shell

      sudo reboot

   .. image:: img/nvme_boot_reboot.png

Nach dem Neustart sollte der Raspberry Pi nun versuchen, von Ihrer angeschlossenen NVMe-SSD zu booten, was Ihnen eine verbesserte Leistung und Haltbarkeit für Ihr System bietet.

.. end_copy_nvme