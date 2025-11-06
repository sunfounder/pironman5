.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _set_up_pironman5_mini:

Setting Up on Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

If you have installed Raspberry Pi OS, Ubuntu, Kali Linux or Homebridge on your Raspberry Pi, you will need to configure the Pironman 5 Mini using the command line. Detailed tutorials can be found below:

.. note::

  Before configuring, you need to boot up and log into your Raspberry Pi. If you're unsure how to log in, you can visit the official Raspberry Pi website: |link_rpi_get_start|.


Configuring Shutdown to Deactivate GPIO Power
------------------------------------------------------------
To prevent the RGB fan, powered by the Raspberry Pi GPIO, from remaining active post-shutdown, it's essential to configure the Raspberry Pi for GPIO power deactivation.

#. Open the EEPROM configuration tool:

   .. code-block::

      sudo raspi-config

#. Navigate to **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Select **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Save the changes. You will be prompted to reboot for the new settings to take effect.



Downloading and Installing the ``pironman5`` Module
-----------------------------------------------------------

.. note::

   For lite systems, initially install tools like ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Proceed to download code from GitHub and install the ``pironman5`` module .

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   After successful installation, a system reboot is required to activate the installation. Follow the on-screen reboot prompt.

   Upon reboot, the ``pironman5.service`` will start automatically. Here are the primary configurations for Pironman 5:
   
   * Four WS2812 RGB LEDs will light up in blue with a breathing mode.
     
   .. note::
    
     * The RGB fans are set to **Always On** mode by default. For different activation temperatures, see :ref:`cc_control_fan_mini`.

#. You can use the ``systemctl`` tool to ``start``, ``stop``, ``restart``, or check the ``status`` of ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Use this command to apply any changes made to the settings of pironman 5 Mini.
   * ``start/stop``: Enable or disable the ``pironman5.service``.
   * ``status``: Check the operational status of the ``pironman5`` program using the ``systemctl`` tool.

.. note::

   At this point, you have successfully set up the Pironman 5 Mini, and it is ready to use.
   
   For advanced control of its components, please refer to :ref:`control_commands_dashboard_mini`.

