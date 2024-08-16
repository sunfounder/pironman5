.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _install_to_nvme_home_bridge:

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

#. Insert your SD card into your computer or laptop using a Reader.

#. Within the |link_rpi_imager|, click **Raspberry Pi Device** and select the **Raspberry Pi 5** model from the dropdown list.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      

#. Click on the **Operating System** tab.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scroll down to the bottom of the page and select the your operating system.

   .. note::

      * For **Ubuntu** system, you need to click **Other general-purpose OS** -> **Ubuntu**, and select either **Ubuntu Desktop 24.04 LTS (64 bit)** or **Ubuntu Server 24.04 LTS (64 bit)**.
      * For **Kali Linux**, **Home Assistant** and **Homebridge** systems, you need to click **Other specific-purpose OS** and then select the corresponding system.

   .. image:: img/os_other_os.png
      :width: 90%

#. In the **Storage** option, select the appropriate storage device for the installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      

#. Click **NEXT**.

   .. note::

      * For systems that cannot be configured in advance, after clicking **NEXT**, you will be prompted whether to save the data within the device. If you have confirmed that a backup has been made, select **Yes**.

      * For systems where the Hostname, WiFi, and Enable SSH can be configured in advance, a pop-up will appear prompting whether to apply the OS's custom settings. You can choose **Yes** or **No**, or go back to edit further.

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Define a **hostname** for your Raspberry Pi. The hostname is your Raspberry Pi's network identifier. You can access your Pi using ``<hostname>.local`` or ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Create a **Username** and **Password** for the Raspberry Pi's administrator account. Establishing a unique username and password is vital for securing your Raspberry Pi, which lacks a default password.

     .. image:: img/os_set_username.png

   * Configure the wireless LAN by providing your network's **SSID** and **Password**.

     .. note::

       Set the ``Wireless LAN country`` to the two-letter `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corresponding to your location.

     .. image:: img/os_set_wifi.png
         
   * To remotely connect to your Raspberry Pi, enable SSH in the Services tab.

     * For **password authentication**, use the username and password from the General tab.
     * For public-key authentication, choose "Allow public-key authentication only". If you have an RSA key, it will be used. If not, click "Run SSH-keygen" to generate a new key pair.

     .. image:: img/os_enable_ssh.png

   * The **Options** menu lets you configure Imager's behavior during a write, including playing sound when finished, ejecting media when finished, and enabling telemetry.

     .. image:: img/os_options.png

         
    
#. When you've finished entering OS customisation settings, click **Save** to save your customisation. Then, click **Yes** to apply them when writing the image.

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. If the NVMe SSD contains existing data, ensure you back it up to prevent data loss. Proceed by clicking **Yes** if no backup is needed.

   .. image:: img/nvme_erase.png
      :width: 90%
      

#. When you see the "Write Successful" popup, your image has been completely written and verified. You're now ready to boot a Raspberry Pi from the NVMe SSD!
