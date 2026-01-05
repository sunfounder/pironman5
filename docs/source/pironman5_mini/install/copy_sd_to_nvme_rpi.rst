.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _copy_sd_to_nvme_mini:

Copying the OS from a Micro SD Card to an NVMe SSD
==================================================================

If you do not have an NVMe adapter, you can first install the OS on a **Micro SD card**, then copy it to the **NVMe SSD** after the Pironman 5 boots successfully.

* First, complete :ref:`install_os_sd_rpi_mini`.
* Then, boot and log in to your Raspberry Pi. For login help, see: |link_rpi_get_start|.

Complete the steps above before continuing.


1. Enabling PCIe
--------------------

By default the PCIe connector is not enabled. 

* To enable it you should open the ``/boot/firmware/config.txt`` file.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Then add the following line to the file. 

  .. code-block:: shell
  
    # Enable the PCIe External connector.
    dtparam=pciex1
  
* A more memorable alias for ``pciex1`` exists, so you can alternatively add ``dtparam=nvme`` to the ``/boot/firmware/config.txt`` file.

  .. code-block:: shell
  
    dtparam=nvme

* The connection is certified for Gen 2.0 speeds (5 GT/sec), but you can force it to Gen 3.0 (10 GT/sec) if you add the following lines to your ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    # Force Gen 3.0 speeds
    dtparam=pciex1_gen=3
  
  .. warning::
  
    The Raspberry Pi 5 is not certified for Gen 3.0 speeds, and connections to PCIe devices at these speeds may be unstable.

* Press ``Ctrl + X``, ``Y`` and ``Enter`` to save the changes.

.. start_copy_nvme

2. Install the OS on the SSD
----------------------------------------

There are two ways to install an operating system on the SSD:

**Copying the System from the Micro SD Card to the SSD**

#. Connect a display or access the Raspberry Pi desktop through VNC Viewer. Then click **Raspberry Pi logo** -> **Accessories** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png
      
    
#. Make sure to select the correct **Copy From** and **Copy To** devices. Be careful not to mix them up.

   .. image:: img/ssd_copy_from.png
      
#. Remember to select "NEW Partition UUIDs" to ensure the system can correctly distinguish devices, avoiding mounting conflicts and boot issues.

   .. image:: img/ssd_copy_uuid.png
    
#. After selection, click **Start**.

   .. image:: img/ssd_copy_click_start.png

#. You will be prompted that the content on the SSD will be erased. Make sure to back up your data before clicking Yes. Wait for some time, and the copying will be completed.

**Installing the System with Raspberry Pi Imager**

If your Micro SD card has a desktop version of the system installed, you can use an imaging tool (like Raspberry Pi Imager) to burn the system to the SSD. This example uses Raspberry Pi OS bookworm, but other systems might require installing the imaging tool first.

#. Connect a display or access the Raspberry Pi desktop through VNC Viewer. Then click **Raspberry Pi logo** -> **Accessories** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Insert your microSD card into your computer using a card reader. Back up any important data before proceeding.

   .. image:: img/insert_sd.png
      :width: 90%

#. When Raspberry Pi Imager opens, you will see the **Device** page. Select your Raspberry Pi 5 model from the list.

   .. image:: img/imager_device.png
      :width: 90%

#. Go to the **OS** section and choose the recommended **Raspberry Pi OS (64-bit)** option.

   .. image:: img/imager_os.png
      :width: 90%

#. In the **Storage** section, select your **NVMe SSD**. 

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_mini:

3. Configure boot from the SSD
---------------------------------------

In this section, we'll configure your Raspberry Pi to boot directly from an NVMe SSD, providing faster boot times and improved performance over an SD card. Follow these steps carefully:

#. First, open a terminal on your Raspberry Pi and run the following command to access the configuration interface:.

   .. code-block:: shell

      sudo raspi-config

#. In the ``raspi-config`` menu, use the arrow keys to navigate and select **Advanced Options**. Press ``Enter`` to access the advanced settings.

   .. image:: img/nvme_open_config.png

#. Inside **Advanced Options**, select **Boot Order**. This setting allows you to specify the order in which your Raspberry Pi looks for bootable devices.

   .. image:: img/nvme_boot_order.png

#. Then, choose **NVMe/USB boot**. This tells the Raspberry Pi to prioritize booting from USB-connected SSDs or NVMe drives over other options, such as the SD card.

   .. image:: img/nvme_boot_nvme.png

#. After selecting the boot order, press **Finish** to exit raspi-config. You may also use the **Escape** key to close the configuration tool.

   .. image:: img/nvme_boot_ok.png

#. To apply the new boot settings, reboot your Raspberry Pi by running ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

After rebooting, the Raspberry Pi should now attempt to boot from your connected NVMe SSD, providing you with enhanced performance and durability for your system.

.. end_copy_nvme
