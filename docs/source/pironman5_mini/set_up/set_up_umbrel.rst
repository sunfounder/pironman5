.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _set_up_umbrel_mini:

Setting Up on Umbrel OS
======================================================================

If you have installed Umbrel OS on your Raspberry Pi 5, you will need to configure the Pironman 5 Mini using the command line. Detailed instructions are provided below:

#. Connect your Raspberry Pi 5 to your network using an Ethernet cable. This step is essential to ensure that your Raspberry Pi has internet access.

#. In your browser, visit: ``http://umbrel.local``. If the page does not open, check your router for the Umbrel device’s IP address, for example: ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Create your Umbrel account by setting a username and password. This password will be used for future remote access to Umbrel, so make sure to remember it.

   .. image:: img/umbrel_account.png

#. Click **Next** to complete the Umbrel setup and enter the desktop environment.

   .. image:: img/umbrel_desktop.png

#. Open the Terminal. From the desktop, click the **Settings** icon, then select **Advanced Settings** and click **Open**.

   .. image:: img/umbrel_setting.png

#. Click **Open Terminal**.

   .. image:: img/umbrel_open_terminal.png

#. You can choose to open the Terminal in Umbrel OS or within a specific app. Either option will take you to the Terminal interface.

   .. image:: img/umbrel_terminal.png

#. Proceed to download the code from GitHub and install the ``pironman5`` module.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. After the installation is complete, enter the following command to reboot your Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Upon reboot, the ``pironman5.service`` will start automatically. Here are the primary configurations for Pironman 5 Mini:
   
   * Four WS2812 RGB LEDs will light up in blue with a breathing mode.
   * The RGB fans are set to **Always On** mode by default. For information on adjusting activation temperatures, see :ref:`cc_control_fan_mini`.

#. You can use the ``systemctl`` tool to ``start``, ``stop``, ``restart``, or check the ``status`` of ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Use this command to apply any changes made to the settings of pironman 5 Mini.
   * ``start/stop``: Enable or disable the ``pironman5.service``.
   * ``status``: Check the operational status of the ``pironman5`` program using the ``systemctl`` tool.

.. note::

   At this point, you have successfully set up the Pironman 5 Mini, and it is ready to use.
   
   For advanced control of its components, please refer to :ref:`control_commands_dashboard_mini`.



