.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_home_bridge:

Installation des Betriebssystems auf einer NVMe-SSD
=============================================================

Wenn Sie eine NVMe-SSD verwenden und über einen Adapter verfügen, um die NVMe-SSD für die Systeminstallation mit Ihrem Computer zu verbinden, können Sie die folgende Anleitung für eine schnelle Installation nutzen.

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Erforderliche Komponenten**

* Ein Personal Computer
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Micro-SD-Karte und Kartenleser

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installation des Betriebssystems auf der microSD-Karte
---------------------------------------------------------------------

#. Setzen Sie die **NVMe-SSD** mithilfe eines Adapters in Ihren Computer ein.

2. Wenn der **Raspberry Pi Imager** geöffnet wird, sehen Sie die Seite **Device**.  
   Wählen Sie Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

3. Wechseln Sie zum Abschnitt **OS**, scrollen Sie bis zum Ende der Seite und wählen Sie Ihr Betriebssystem aus.

   .. note::

      * Für **Ubuntu** klicken Sie auf **Other general-purpose OS** → **Ubuntu** und wählen anschließend  
        **Ubuntu Desktop 24.04 LTS (64-bit)** oder **Ubuntu Server 24.04 LTS (64-bit)** aus.
      * Für **Kali Linux**, **Home Assistant** und **Homebridge** klicken Sie auf  
        **Other specific-purpose OS** und wählen dann das entsprechende System aus.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Wählen Sie im Abschnitt **Storage** Ihre **NVMe-SSD** aus. 

   .. image:: img/nvme_storage.png
      :width: 90%

#. Klicken Sie auf **NEXT**.

   .. note::

      * Bei Systemen, die **nicht im Voraus konfiguriert werden können**, überspringt ein Klick auf **NEXT** den Schritt **Customisation** und wechselt direkt zu **Writing**, wobei das Betriebssystem auf die microSD-Karte geschrieben wird.
      * Bei Systemen, die eine **Vorkonfiguration unterstützen**, folgen Sie den **Customisation**-Schritten, um Optionen wie **Hostname**, **WiFi** und **SSH aktivieren** zu konfigurieren.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Wenn das Popup **„Write Successful“** erscheint, wurde das Image vollständig geschrieben und verifiziert. Sie können die microSD-Karte nun sicher entfernen und damit Ihren Raspberry Pi starten.
