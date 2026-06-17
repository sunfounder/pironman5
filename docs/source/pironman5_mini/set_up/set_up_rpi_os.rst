.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Setting Up on Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

.. image:: ../img/pironman5_mini_pic.jpg
    :width: 400
    :align: center

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


.. _mini_download_pironman5_module:

Downloading and Installing the ``pironman5`` Module
-----------------------------------------------------------

.. note::

   For lite systems, initially install tools like ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Download and install the ``pironman5`` module from GitHub.

   .. tip::

      If you are using **Ubuntu**, install ``curl`` first:

      .. code-block:: shell

         sudo apt install curl -y

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

   .. note::

      If you are using Pironman 5 series together with PiPower 5, run the following command instead:

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --pipower5

#. After running the installer, select your Pironman 5 model (1~4).

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. Once the installation is complete, reboot the Raspberry Pi as prompted. The first startup may take up to 30 seconds while the services initialize.

   Upon reboot, the ``pironman5.service`` will start automatically. Here are the primary configurations for Pironman 5 Mini:

   * Four WS2812 RGB LEDs will light up in blue with a breathing mode.
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

