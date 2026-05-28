.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Installation von Raspberry Pi OS
================================================================================

Sie können die Installationsmethode je nachdem auswählen, ob Ihnen eine Micro-SD-Karte oder eine NVMe-SSD zur Verfügung steht.

**Verwendung nur einer Micro-SD-Karte**

  Wenn Sie ausschließlich eine Micro-SD-Karte verwenden, können Sie einfach der unten beschriebenen ersten Methode folgen.

**Verwendung einer M.2 NVMe SSD**

  * Wenn Sie über einen **M.2 NVMe SSD Enclosure Adapter** verfügen, können Sie Ihre SSD mit diesem Adapter an Ihren Computer anschließen und der zweiten Methode folgen, um das Betriebssystem zu installieren.  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * Wenn Sie den oben gezeigten Adapter nicht haben, können Sie das Betriebssystem zunächst mit der ersten Methode auf einer Micro-SD-Karte installieren und anschließend mit der dritten Methode das System von der Micro-SD-Karte auf Ihre M.2 NVMe SSD kopieren.  

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi