.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

3. Installing the OS
=======================

**Required Components**

* Raspberry Pi 5B
* A Personal Computer
* A Micro SD card 

**Installation Steps**

#. Visit the Raspberry Pi software download page at `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Choose the Imager version compatible with your operating system. Download and open the file to initiate installation.

    .. image:: img/os_install_imager.png

#. A security prompt may appear during installation, depending on your operating system. For example, Windows might display a warning message. In such cases, select **More info** and then **Run anyway**. Follow the on-screen guidance to complete the installation of the Raspberry Pi Imager.

    .. image:: img/os_info.png

#. Insert your SD card into your computer or laptop's SD card slot.

#. Launch the Raspberry Pi Imager application by clicking its icon or typing ``rpi-imager`` in your terminal.

    .. image:: img/os_open_imager.png

#. Within the Imager, click **CHOOSE DEVICE** and select the **Raspberry Pi 5** model from the dropdown list.

    .. image:: img/os_choose_device_pi5.png

#. Select **CHOOSE OS** and opt for the recommended operating system version.

    .. image:: img/os_choose_os.png

#. Click **Choose Storage** and select the appropriate storage device for the installation.

    .. note::

        Ensure you select the correct storage device. To avoid confusion, disconnect any additional storage devices if multiple ones are connected.

    .. image:: img/os_choose_sd.png

#. Click **NEXT** and then **EDIT SETTINGS** to tailor your OS settings.

    .. image:: img/os_enter_setting.png

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

#. Click **SERVICES** and activate **SSH** for secure, password-based remote access. Remember to save your settings.

    .. image:: img/os_enable_ssh.png

#. Confirm your selected settings by clicking **Yes**.

    .. image:: img/os_click_yes.png

#. If the SD card contains existing data, ensure you back it up to prevent data loss. Proceed by clicking **Yes** if no backup is needed.

    .. image:: img/os_continue.png

#. The OS installation process will commence on the SD card. A confirmation dialog will appear upon completion.

    .. image:: img/os_finish.png
        :align: center
