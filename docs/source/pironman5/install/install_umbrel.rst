Installing Umbrel OS
============================================

Umbrel is an open-source, self-hosted home-server platform/OS that lets you run your own Bitcoin node, install a variety of one-click self-hosted apps — and turn your hardware into your personal home cloud. It’s an excellent way to start with self-custody and privacy.

**Required Components**

* A Personal Computer
* A NVMe SSD
* A NVMe to USB Adapter
* Micro SD Card and Reader


1. Update the Bootloader
--------------------------------

First, you need to update the Raspberry Pi 5 bootloader to boot from NVMe before trying USB and then SD Card.

.. note::

    * At this step, it is recommended to use a spare Micro SD card. First, write the bootloader to this Micro SD card and then immediately insert it into the Raspberry Pi to enable booting from an NVMe device.
    * Alternatively, you can write the bootloader directly to your NVMe device first, then insert it into the Raspberry Pi to change its boot method. Afterwards, connect the NVMe SSD to a computer to install the operating system, and once the installation is complete, reinsert it back into the Raspberry Pi.

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
      

#. Insert your Micro SD card or NVMe SSD into the Raspberry Pi. After connecting the Type-C power adapter, the bootloader from the Micro SD card or NVMe SSD will be written to the Raspberry Pi’s EEPROM.

   .. note::

      * After the update, the Raspberry Pi will boot from the NVMe drive first, followed by USB, and then the Micro SD card.
      * Wait for one to two minutes, then power off the Raspberry Pi and remove the Micro SD card or NVMe SSD.


2. Install the OS on the NVMe SSD
-----------------------------------

**Steps**

1. Download the latest Umbrel OS image and extract it. You can also visit the `Umbrel Release Page <https://github.com/getumbrel/umbrel/releases>`_ to choose a specific version.

   * :download:`Latest Umbrel OS Image <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. In |link_rpi_imager|, click **Raspberry Pi Device** and select **Raspberry Pi 5** from the dropdown list.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. Launch the **Raspberry Pi Imager** and click **CHOOSE OS**.

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. Scroll to the bottom and select **Use custom**.

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. Choose the Umbrel OS image file you downloaded earlier and click **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. Under the **Storage** option, select the NVMe SSD as the installation target.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. Click **NEXT**, then select **NO**. Umbrel OS will automatically initialize its own system and user configuration during the first boot, and does not use the username or password set in Raspberry Pi Imager.

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. If the NVMe SSD contains existing data, back it up before proceeding to avoid data loss. Click **Yes** to continue if no backup is needed.

   .. image:: img/nvme_erase.png
      :width: 90%

9. When the “Write Successful” message appears, the image has been fully written and verified. Your NVMe SSD is now ready to boot your Raspberry Pi!

   .. image:: img/umbrel_finish.png
      :width: 90%

