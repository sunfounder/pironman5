.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _copy_sd_to_nvme_rpi:

Copy OS from Micro SD to NVMe SSD
==================================================================

If you have an NVMe SSD but lack an adapter to connect it to your computer, you can opt for a third approach: initially install the system on your Micro SD card. After the Pironman 5 successfully boots up, you can then transfer the system from your Micro SD card to your NVMe SSD.

* First, you need to :ref:`install_os_sd_rpi`.
* Then, boot up and log into your Raspberry Pi. If you're unsure how to log in, you can visit the official Raspberry Pi website: |link_rpi_get_start|.

Complete the above steps before proceeding with the instructions below.


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

#. You will be prompted that the content on the SSD will be erased. Make sure to back up your data before clicking Yes.

   .. image:: img/ssd_copy_erase.png

#. Wait for some time, and the copying will be completed.


**Installing the System with Raspberry Pi Imager**

If your Micro SD card has a desktop version of the system installed, you can use an imaging tool (like Raspberry Pi Imager) to burn the system to the SSD. This example uses Raspberry Pi OS bookworm, but other systems might require installing the imaging tool first.

#. Connect a display or access the Raspberry Pi desktop through VNC Viewer. Then click **Raspberry Pi logo** -> **Accessories** -> **Imager**.

   .. image:: img/ssd_imager.png

      
#. Within the |link_rpi_imager|, click **Raspberry Pi Device** and select the **Raspberry Pi 5** model from the dropdown list.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Select **Operating System** and opt for the recommended operating system version.

   .. image:: img/ssd_os.png
      :width: 90%
    
#. In the **Storage** option, select your inserted NVMe SSD.

   .. image:: img/nvme_storage.png
      :width: 90%
    
#. Click **NEXT** and then **EDIT SETTINGS** to tailor your OS settings. 

   .. note::

      If you have a monitor for your Raspberry Pi, you can skip the next steps and click 'Yes' to begin the installation. Adjust other settings later on the monitor.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Define a **hostname** for your Raspberry Pi.

   .. note::

      The hostname is your Raspberry Pi's network identifier. You can access your Pi using ``<hostname>.local`` or ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png
      

#. Create a **Username** and **Password** for the Raspberry Pi's administrator account.

   .. note::

      Establishing a unique username and password is vital for securing your Raspberry Pi, which lacks a default password.

   .. image:: img/os_set_username.png
      

#. Configure the wireless LAN by providing your network's **SSID** and **Password**.

   .. note::

      Set the ``Wireless LAN country`` to the two-letter `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corresponding to your location.

   .. image:: img/os_set_wifi.png

#. To remotely connect to your Raspberry Pi, **enable SSH** in the **Services** tab.

   * For **password authentication**, use the username and password from the **General** tab.
   * For public-key authentication, choose "Allow public-key authentication only". If you have an RSA key, it will be used. If not, click "Run SSH-keygen" to generate a new key pair.

   .. image:: img/os_enable_ssh.png

      

#. The **Options** menu lets you configure Imager's behavior during a write, including playing sound when finished, ejecting media when finished, and enabling telemetry.

   .. image:: img/os_options.png
    
#. When you've finished entering OS customisation settings, click **Save** to save your customisation. Then, click **Yes** to apply them when writing the image.

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. If the NVMe SSD contains existing data, ensure you back it up to prevent data loss. Proceed by clicking **Yes** if no backup is needed.

   .. image:: img/nvme_erase.png
      :width: 90%

#. When you see the "Write Successful" popup, your image has been completely written and verified. You're now ready to boot a Raspberry Pi from the NVMe SSD!

   .. image:: img/nvme_install_finish.png
      :width: 90%
      

.. _configure_boot_ssd:

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


