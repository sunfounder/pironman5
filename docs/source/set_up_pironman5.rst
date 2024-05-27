.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _set_up_pironman5:

5. Set up Pironman 5
===================================

Before Configuration
-----------------------
After powering on, you will only see the various power LEDs lit up, but the OLED screen (if there is a screen garbling issue, please ignore it as it will resolve after configuration), RGB LEDs, and RGB fans (the two fans on the side) are not yet functional because they have not been configured.

The power button brings out the power button of the Raspberry Pi 5, and it functions just like the power button of the Raspberry Pi 5.

**Shutdown**

    * If you run Raspberry Pi **Bookworm Desktop** system, you can press the power button twice in quick succession to shutdown. 
    * If you run Raspberry Pi **Bookworm Lite** system, press the power button a single time to initiate a shutdown.
    * To force a hard shutdown, press and hold the power button.

**Power on**

    * If the Raspberry Pi board is shut down, but still powered, single-press to power on from a shutdown state.

.. note::

    If you are running a system that does not support a shutdown button, you can hold it for 5 seconds to force a hard shutdown, and single-press to power on from a shutdown state.


Configuring Shutdown to Deactivate GPIO Power
------------------------------------------------------------
To prevent the OLED screen and RGB fans, powered by the Raspberry Pi GPIO, from remaining active post-shutdown, it's essential to configure the Raspberry Pi for GPIO power deactivation.

* Manually edit the ``EEPROM`` configuration file with this command:

  .. code-block:: shell

    sudo rpi-eeprom-config -e

* Modify the ``POWER_OFF_ON_HALT`` setting in the file to ``1``. For instance:

  .. code-block:: shell

    BOOT_UART=1
    POWER_OFF_ON_HALT=1
    BOOT_ORDER=0xf41


Downloading and Installing the ``pironman5`` Module
-----------------------------------------------------------

.. note::

  For lite systems, initially install tools like ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
  
  .. code-block:: shell
  
    sudo apt-get update
    sudo apt-get install git -y
    sudo apt-get install python3 python3-pip python3-setuptools -y

Proceed to download code from GitHub and install the ``pironman5`` module .

.. code-block:: shell

  cd ~
  git clone https://github.com/sunfounder/pironman5.git
  cd ~/pironman5
  sudo python3 install.py

After successful installation, a system reboot is required to activate the installation. Follow the on-screen reboot prompt.

Upon reboot, the ``pironman5.service`` will start automatically. Here are the primary configurations for |link_pironman5|:

  * The OLED screen displays CPU, RAM, Disk Usage, CPU Temperature, and the Raspberry Pi's IP Address.
  * Four WS2812 RGB LEDs will light up in blue with a breathing mode.
  * 

You can use the ``systemctl`` tool to ``start``, ``stop``, ``restart``, or check the ``status`` of ``pironman5.service``.

.. code-block:: shell

  sudo systemctl restart pironman5.service

* ``restart``: Use this command to apply any changes made to the settings of pironman 5.
* ``start/stop``: Enable or disable the ``pironman5.service``.
* ``status``: Check the operational status of the ``pironman5`` program using the ``systemctl`` tool.

.. note::

  * Next, you can view and control the components of |link_pironman5| from dashboard, please refer to :ref:`view_control_dashboard`.
  * If you wish to use commands, please see :ref:`view_control_commands`.


