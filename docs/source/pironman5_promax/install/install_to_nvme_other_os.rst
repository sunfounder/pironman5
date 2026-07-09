.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_to_nvme_other_promax:

Betriebssystem auf einer NVMe-SSD installieren
=====================================================================

Wenn Sie eine NVMe-SSD verwenden und einen Adapter besitzen, um die NVMe-SSD zur Systeminstallation mit Ihrem Computer zu verbinden, können Sie das folgende Tutorial für eine schnelle Installation nutzen.

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center

**Benötigte Komponenten**

* Ein Personal Computer
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Micro-SD-Karte und Kartenleser

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Betriebssystem auf der NVMe-SSD installieren
---------------------------------------------------

#. Schließen Sie die **NVMe-SSD** mit einem Adapter an Ihren Computer an.

2. Wenn **Raspberry Pi Imager** geöffnet wird, sehen Sie die Seite **Gerät**.
   Wählen Sie Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

3. Gehen Sie zum Bereich **Betriebssystem**, scrollen Sie nach unten zum Ende der Seite und wählen Sie Ihr Betriebssystem aus.

   .. note::

      * Für **Ubuntu** klicken Sie auf **Andere Allzweck-Betriebssysteme** → **Ubuntu** und wählen Sie dann
        **Ubuntu Desktop 24.04 LTS (64-bit)** oder **Ubuntu Server 24.04 LTS (64-bit)**.
      * Für **Kali Linux** und **Homebridge** klicken Sie auf
        **Andere spezielle Betriebssysteme** und wählen Sie dann das entsprechende System aus.

   .. warning::

      Welches System Sie auch wählen, achten Sie darauf, eine **64-Bit**-Version auszuwählen. Auf einem **32-Bit**-System sind einige Pakete nur für ``aarch64`` (64 Bit) verfügbar, und bestimmte Funktionen lassen sich möglicherweise nicht installieren oder funktionieren nicht richtig.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Wählen Sie im Bereich **Speicher** Ihre **NVMe-SSD** aus.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Klicken Sie auf **WEITER**.

   .. note::

      * Bei Systemen, die **nicht im Voraus konfiguriert werden können**, überspringt das Klicken auf **WEITER** den Schritt **Anpassung** und geht direkt zum **Schreiben**, wo das Betriebssystem auf die NVMe-SSD geschrieben wird.
      * Bei Systemen, die **eine Vorkonfiguration unterstützen**, folgen Sie den Schritten unter **Anpassung**, um Optionen wie **Hostname**, **WLAN** und **SSH aktivieren** zu konfigurieren.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Wenn das Popup **“Schreiben erfolgreich”** erscheint, wurde das Image vollständig geschrieben und verifiziert. Sie können die NVMe-SSD jetzt sicher entfernen und verwenden, um Ihren Raspberry Pi zu starten.