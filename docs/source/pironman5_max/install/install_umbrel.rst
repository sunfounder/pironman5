.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Installation von Umbrel OS
============================================

Umbrel ist eine Open-Source-, selbstgehostete Home-Server-Plattform bzw. ein Betriebssystem, mit dem Sie Ihren eigenen Bitcoin-Node betreiben, eine Vielzahl von selbstgehosteten Apps mit nur einem Klick installieren und Ihre Hardware in Ihre persönliche Home-Cloud verwandeln können. Es ist ein hervorragender Einstieg in Selbstverwahrung und Datenschutz.

**Erforderliche Komponenten**

* Ein Personal Computer
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Micro-SD-Karte und Kartenleser

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installation des Betriebssystems auf der NVMe-SSD
---------------------------------------------------------------

Nun sind Sie bereit, das Betriebssystem auf Ihrer **NVMe-SSD** zu installieren.  
Befolgen Sie einfach die folgenden Schritte sorgfältig — diese Anleitung ist einsteigerfreundlich und leicht nachzuvollziehen.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Umbrel-OS-Releases</a>

#. Laden Sie das neueste **Umbrel OS**-Image herunter und entpacken Sie die Datei. Wenn Sie eine bestimmte Version verwenden möchten, können Sie auch die Seite |link_umbrel_release| besuchen.

   * :download:`Neuestes Umbrel-OS-Image <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Setzen Sie die **NVMe-SSD** mithilfe eines **NVMe-zu-USB-Adapters** in Ihren Computer ein.

#. Öffnen Sie den **Raspberry Pi Imager**. Wählen Sie auf dem Bildschirm **Device** Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

#. Wechseln Sie zum Abschnitt **OS**, scrollen Sie nach unten und wählen Sie **Use custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Wählen Sie die zuvor heruntergeladene und entpackte **Umbrel-OS-Image-Datei** aus und klicken Sie anschließend auf **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Klicken Sie auf **Next**, um fortzufahren.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. Wählen Sie im Abschnitt **Storage** Ihre **NVMe-SSD** aus. Stellen Sie sicher, dass Sie die NVMe-SSD auswählen und kein anderes Laufwerk Ihres Computers.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Überprüfen Sie alle Einstellungen sorgfältig und klicken Sie anschließend auf **WRITE**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. Falls die NVMe-SSD bereits Daten enthält, warnt der Raspberry Pi Imager, dass alle Daten gelöscht werden. Vergewissern Sie sich, dass das richtige Laufwerk ausgewählt ist, und klicken Sie dann auf **I UNDERSTAND, ERASE AND WRITE**.

   .. image:: img/imager_erase.png
      :width: 90%

#. Wenn die Meldung **„Write Complete“** erscheint, wurde das Image erfolgreich geschrieben und verifiziert.

   .. image:: img/imager_umbrel_finish.png
      :width: 90%

