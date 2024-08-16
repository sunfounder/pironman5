.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _install_to_nvme_ubuntu:

Installing the OS on an NVMe SSD
============================================

If you are using an NVMe SSD and have an adapter to connect the NVMe SSD to your computer for system installation, you can use the following tutorial for a quick installation.

**Required Components**

* A Personal Computer
* A NVMe SSD
* A NVMe to USB Adapter
* Micro SD Card and Reader

.. _update_bootloader:

1. Update the Bootloader
----------------------------------

First, you need to update the Raspberry Pi 5 bootloader to boot from NVMe before trying USB and then SD Card.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    At this step, it is recommended to use a spare Micro SD card. First, write the bootloader to this Micro SD card and then immediately insert it into the Raspberry Pi to enable booting from an NVMe device.
    
    Alternatively, you can write the bootloader directly to your NVMe device first, then insert it into the Raspberry Pi to change its boot method. Afterwards, connect the NVMe SSD to a computer to install the operating system, and once the installation is complete, reinsert it back into the Raspberry Pi.

#. Insert your spare Micro SD card or NVMe SSD into your computer or laptop using a Reader.

#. Within the |link_rpi_imager|, click **Raspberry Pi Device** and select the **Raspberry Pi 5** model from the dropdown list.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. On the **Operating System** tab, scroll down and select **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. Select **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Select **NVMe/USB Boot** to enable Raspberry Pi 5 to boot from NVMe before trying USB and then SD Card.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      


#. In the **Storage** option, select the appropriate storage device for the installation.

   .. note::

      Ensure you select the correct storage device. To avoid confusion, disconnect any additional storage devices if multiple ones are connected.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Now you can click **NEXT**. If the storage device contains existing data, ensure you back it up to prevent data loss. Proceed by clicking **Yes** if no backup is needed.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Soon, you will be prompted that **NVMe/USB Boot** has been written to your storage device.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Now, you can insert your Micro SD card or NVMe SSD into the Raspberry Pi. After powering the Raspberry Pi with a Type C adapter, the bootloader from the Micro SD card or NVMe SSD will be written to the Raspberry Pi's EEPROM.

.. note::

    Afterward, the Raspberry Pi will boot from NVMe before trying USB and then the SD Card. 
    
    Power off the Raspberry Pi and remove the Micro SD card or NVMe SSD.


2. Install OS to NVMe SSD
---------------------------------

Now you can install the operating system on your NVMe SSD.

**Steps**

#. First, navigate to the |link_batocera_download| page, select **Raspberry Pi 5 B**, and click to download.

   .. image:: img/batocera_download.png
      :width: 90%
      

#. Insert your SD card into your computer or laptop using a Reader.

#. Within the |link_rpi_imager|, click on the **Operating System** tab.

   .. image:: img/os_choose_os.png
      :width: 90%
      
#. Scroll down to the bottom of the page and select **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%
      

#. Choose the system file you have just downloaded, ``batocera-xxx-xx-xxxxxxxx.img.gz``, and then click **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%
      

#. In the **Storage** option, select the appropriate storage device for the installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      


#. Now you can click **NEXT**. If the storage device contains existing data, ensure you back it up to prevent data loss. Proceed by clicking **Yes** if no backup is needed.

   .. image:: img/nvme_erase.png
      :width: 90%
      

#. When you see the "Write Successful" popup, your image has been completely written and verified. You're now ready to boot a Raspberry Pi from the NVMe SSD!
