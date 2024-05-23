.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _install_os_sd:

Installing the OS on a Micro SD Card
============================================================


**Required Components**

* A Personal Computer
* A Micro SD card and Reader

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

2. Install OS to Micro SD Card
--------------------------------

#. Insert your SD card into your computer or laptop using a Reader.

#. Within the Imager, click **Raspberry Pi Device** and select the **Raspberry Pi 5** model from the dropdown list.

    .. image:: img/os_choose_device_pi5.png
        :align: center

#. Select **Operating System** and opt for the recommended operating system version.

    .. image:: img/os_choose_os.png
        :align: center

#. Click **Choose Storage** and select the appropriate storage device for the installation.

    .. note::

        Ensure you select the correct storage device. To avoid confusion, disconnect any additional storage devices if multiple ones are connected.

    .. image:: img/os_choose_sd.png
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


#. To remotely connect to your Raspberry Pi, enable SSH in the Services tab.

    * For **password authentication**, use the username and password from the General tab.
    * For public-key authentication, choose "Allow public-key authentication only". If you have an RSA key, it will be used. If not, click "Run SSH-keygen" to generate a new key pair.

    .. image:: img/os_enable_ssh.png
        :align: center

#. The **Options** menu lets you configure Imager's behavior during a write, including playing sound when finished, ejecting media when finished, and enabling telemetry.

    .. image:: img/os_options.png
        :align: center

    
#. When you've finished entering OS customisation settings, click **Save** to save your customisation. Then, click **Yes** to apply them when writing the image.

    .. image:: img/os_click_yes.png
        :align: center

#. If the SD card contains existing data, ensure you back it up to prevent data loss. Proceed by clicking **Yes** if no backup is needed.

    .. image:: img/os_continue.png
        :align: center

#. When you see the "Write Successful" popup, your image has been completely written and verified. You're now ready to boot a Raspberry Pi from the Micro SD Card!

    .. image:: img/os_finish.png
        :align: center

