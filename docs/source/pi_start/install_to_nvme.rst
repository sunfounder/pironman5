.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Installing the OS on an NVMe SSD
===================================

**Required Components**

* A Personal Computer
* A NVMe SSD
* A NVMe to USB Adapter
* Micro SD Card and Reader

1. Install Raspberry Pi Imager
----------------------------------

#. Visit the Raspberry Pi software download page at `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Choose the Imager version compatible with your operating system. Download and open the file to initiate installation.

    .. image:: img/os_install_imager.png
        :align: center

#. A security prompt may appear during installation, depending on your operating system. For example, Windows might display a warning message. In such cases, select **More info** and then **Run anyway**. Follow the on-screen guidance to complete the installation of the Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Launch the Raspberry Pi Imager application by clicking its icon or typing ``rpi-imager`` in your terminal.

    .. image:: img/os_open_imager.png
        :align: center

.. _update_bootloader:

2. Update the Bootloader
---------------------------

First, you need to update the Raspberry Pi 5 bootloader to boot from NVMe before trying USB and then SD Card.

.. note::

    At this step, it is recommended to use a spare Micro SD card. First, write the bootloader to this Micro SD card and then immediately insert it into the Raspberry Pi to enable booting from an NVMe device.
    
    Alternatively, you can write the bootloader directly to your NVMe device first, then insert it into the Raspberry Pi to change its boot method. Afterwards, connect the NVMe SSD to a computer to install the operating system, and once the installation is complete, reinsert it back into the Raspberry Pi.

#. Insert your spare Micro SD card or NVMe SSD into your computer or laptop using a Reader.

#. Within the Imager, click **Raspberry Pi Device** and select the **Raspberry Pi 5** model from the dropdown list.

    .. image:: img/os_choose_device_pi5.png
        :align: center

#.  On the **Operating System** tab, scroll down and select **Misc utility images**.

    .. image:: img/nvme_misc.png
        :align: center

#. Select **Bootloader (Pi 5 family)**.

    .. image:: img/nvme_bootloader.png
        :align: center

#. Select **NVMe/USB Boot** to enable Raspberry Pi 5 to boot from NVMe before trying USB and then SD Card.

    .. image:: img/nvme_nvme_boot.png
        :align: center


#. In the **Storage** option, select your inserted NVMe SSD.

    .. note::

        Ensure you select the correct storage device. To avoid confusion, disconnect any additional storage devices if multiple ones are connected.

    .. image:: img/nvme_ssd_storage.png
        :align: center

#. Now you can click **NEXT**. If the storage device contains existing data, ensure you back it up to prevent data loss. Proceed by clicking **Yes** if no backup is needed.

    .. image:: img/nvme_erase.png
        :align: center

#. Soon, you will be prompted that **NVMe/USB Boot** has been written to your storage device.

    .. image:: img/nvme_boot_finish.png
        :align: center

#. Now, you can insert your Micro SD card or NVMe SSD into the |link_pironman5|. After powering the |link_pironman5| with a Type C adapter, the bootloader from the Micro SD card or NVMe SSD will be written to the Raspberry Pi's EEPROM.

.. note::

    Afterward, the Raspberry Pi will boot from NVMe before trying USB and then the SD Card. 
    
    Power off the |link_pironman5| and remove the Micro SD card or NVMe SSD.


3. Install OS to NVMe SSD
--------------------------------

Now you can install the operating system on your NVMe SSD.

#. Within the Imager, click **Raspberry Pi Device** and select the **Raspberry Pi 5** model from the dropdown list.

    .. image:: img/os_choose_device_pi5.png
        :align: center

#. Select **Operating System** and opt for the recommended operating system version.

    .. image:: img/os_choose_os.png
        :align: center

#. In the **Storage** option, select your inserted NVMe SSD.

    .. note::

        Ensure you select the correct storage device. To avoid confusion, disconnect any additional storage devices if multiple ones are connected.

    .. image:: img/nvme_ssd_storage.png
        :align: center

#. Click **NEXT** and then **EDIT SETTINGS** to tailor your OS settings. 

    .. note::

        If you have a monitor for your Raspberry Pi, you can skip the next steps and click 'Yes' to begin the installation. Adjust other settings later on the monitor.

    .. image:: img/os_enter_setting.png
        :align: center

#. Define a **hostname** for your Raspberry Pi.

    .. note::

        The hostname is your Raspberry Pi's network identifier. You can access your Pi using ``<hostname>.local`` or ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Create a **Username** and **Password** for the Raspberry Pi's administrator account.

    .. note::

        Establishing a unique username and password is vital for securing your Raspberry Pi, which lacks a default password.

    .. image:: img/os_set_username.png
        :align: center

#. Configure the wireless LAN by providing your network's **SSID** and **Password**.

    .. note::

        Set the ``Wireless LAN country`` to the two-letter `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corresponding to your location.

    .. image:: img/os_set_wifi.png
        :align: center


#. To remotely connect to your Raspberry Pi, **enable SSH** in the **Services** tab.

    * For **password authentication**, use the username and password from the **General** tab.
    * For public-key authentication, choose "Allow public-key authentication only". If you have an RSA key, it will be used. If not, click "Run SSH-keygen" to generate a new key pair.

    .. image:: img/os_enable_ssh.png
        :align: center

#. The **Options** menu lets you configure Imager's behavior during a write, including playing sound when finished, ejecting media when finished, and enabling telemetry.

    .. image:: img/os_options.png
        :align: center

    
#. When you've finished entering OS customisation settings, click **Save** to save your customisation. Then, click **Yes** to apply them when writing the image.

    .. image:: img/os_click_yes.png
        :align: center

#. If the NVMe SSD contains existing data, ensure you back it up to prevent data loss. Proceed by clicking **Yes** if no backup is needed.

    .. image:: img/nvme_erase.png
        :align: center

#. When you see the "Write Successful" popup, your image has been completely written and verified. You're now ready to boot a Raspberry Pi from the NVMe SSD!

    .. image:: img/nvme_install_finish.png
        :align: center


#. Now, insert the NVMe SSD into the NVMe PiP board of the |link_pironman5|.

    .. image:: img/nvme_assemble.png
        :width: 500
        :align: center


