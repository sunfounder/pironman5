.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Installing Raspberry Pi OS
================================================================================

You can choose an installation method based on whether you have a Micro SD card or an NVMe SSD available.

**Using a Micro SD Card Only**

  If you are only using a Micro SD card, you can simply follow the first method below.

**Using an M.2 NVMe SSD**

  * If you have an **M.2 NVMe SSD Enclosure Adapter**, you can connect your SSD to your computer using the adapter and follow the second method to install the OS.  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * If you do not have the adapter shown above, you can first install the OS on a Micro SD card using the first method, then use the third method to copy the system from the Micro SD card to your M.2 NVMe SSD.  

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi