.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _install_to_nvme_rpi_mini:

Installing the OS on an NVMe SSD
===================================

If you are using an NVMe SSD and have an adapter to connect the NVMe SSD to your computer for system installation, you can use the following tutorial for a quick installation.

**Required Components**

* A Personal Computer
* A NVMe SSD
* A NVMe to USB Adapter
* Micro SD Card and Reader


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_mini:


2. Update the Bootloader
--------------------------------

First, update the Raspberry Pi 5 bootloader so it tries to boot from **NVMe first**, then **USB**, and finally the **SD card**.

.. note::

    It is recommended to use a **spare Micro SD card** for this step.
    
    - Method 1 (Recommended): Write the bootloader to a Micro SD card, insert it into the Raspberry Pi, and boot once to apply the setting.
    - Method 2: Write the bootloader directly to the NVMe SSD. Afterward, connect the NVMe to a computer to install the OS, then put it back into the Raspberry Pi.

#. Insert the spare **Micro SD card or NVMe SSD** into your computer using a card reader or adapter.

#. When Raspberry Pi Imager opens, you will see the **Device** page. Select your Raspberry Pi 5 model from the list.

   .. image:: img/imager_device.png
      :width: 90%

#. Click **OS**.

   * Scroll down and select **Misc utility images**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Select **Bootloader (Pi 5 family)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Choose **NVMe/USB Boot** to set the boot order, then click **NEXT**.

     .. image:: img/nvme_boot.png
        :width: 90%


#. In **Storage**, select the correct Micro SD card or NVMe SSD, then click **NEXT**.

   .. note::

      Make sure the correct device is selected. Disconnect other storage devices if needed.

   .. image:: img/imager_storage.png
      :width: 90%


#. Review the settings and click **WRITE** to start.

   .. image:: img/nvme_write.png
      :width: 90%

#. Confirm the warning and allow Raspberry Pi Imager to erase and write the bootloader.

   .. image:: img/imager_erase.png
      :width: 90%

#. Wait until **Write complete!** appears, then safely remove the storage device.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Insert the Micro SD card into the Raspberry Pi and power it on once to apply the bootloader update.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Wait at least **10 seconds** after the Raspberry Pi finishes booting, then power it off and remove the Micro SD card or NVMe SSD.

The Raspberry Pi 5 is now ready to boot from **NVMe**.

.. end_update_bootloader

3. Install OS to NVMe SSD
-----------------------------------

Now you can install the operating system on your NVMe SSD.

#. Insert the **NVMe SSD** into your computer using an adapter.

2. When Raspberry Pi Imager opens, you will see the **Device** page. Select your Raspberry Pi 5 model from the list.

   .. image:: img/imager_device.png
      :width: 90%

3. Go to the **OS** section and choose the recommended **Raspberry Pi OS (64-bit)** option.

   .. image:: img/imager_os.png
      :width: 90%

4. In the **Storage** section, select your **NVMe SSD**. 

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

