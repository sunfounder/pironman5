.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




Setting Up on Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
==================================================================

.. image:: ../img/pironman5_pic.jpg
    :width: 400
    :align: center


If you have installed Raspberry Pi OS, Ubuntu, Kali Linux or Homebridge on your Raspberry Pi, you will need to configure the Pironman 5 using the command line.

.. note::

  Before configuring, you need to boot up and log into your Raspberry Pi. If you're unsure how to log in, you can visit the official Raspberry Pi website: |link_rpi_get_start|.


.. _safe_shutdown_5:

1. Configuring Shutdown to Deactivate GPIO Power
------------------------------------------------------------

To prevent the OLED screen and GPIO Fans, powered by the Raspberry Pi GPIO, from remaining active post-shutdown, it's essential to configure the Raspberry Pi for GPIO power deactivation.

#. Open the EEPROM configuration tool:

   .. code-block::

      sudo raspi-config

#. Navigate to **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Select **B1 Full Power Off...**.

   .. image:: img/run_power_off.png

#. Save the changes. You will be prompted to reboot for the new settings to take effect.


.. _install_pironman5_module_5:

2. Installing the ``pironman5`` Module
-----------------------------------------------------------

.. note::

   For Raspberry Pi OS Lite systems, first install the required tools such as ``git`` and ``python3``.

   .. code-block:: shell

      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Download and install the ``pironman5`` module from GitHub.

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

#. After Pironman 5 starts successfully, check whether the following components are working properly.

   * **OLED Screen**

     * Displays CPU usage, RAM usage, CPU temperature, and IP address.
     * Turns off automatically after 10 seconds.
     * Briefly press the power button to wake the screen or switch pages.

   * **Power Button**

     * Briefly press: Power on / wake up OLED / switch OLED page.
     * Hold for 2 seconds: Safe shutdown (requires :ref:`safe_shutdown_5`).
     * Hold for 5 seconds: Force shutdown.

   * **WS2812 RGB LEDs**

     * Light up in blue with a breathing effect.

   * **Two GPIO Fans**

     * Set to **Always On** mode by default.
     * The working mode can be changed via commands or the Dashboard.


   * **CPU Fan (Tower Cooler Fan)**

     * Automatically adjusts speed based on CPU temperature.
     * Default fan curve:
     
       * < 50°C: Off (0%)
       * 50°C+: Low (30%)
       * 60°C+: Medium (50%)
       * 67.5°C+: High (70%)
       * 75°C+: Full speed (100%)

#. Use ``systemctl`` to manage the ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Replace ``restart`` with ``start``, ``stop``, or ``status`` as needed to manage the service.

.. note::

   Pironman 5 is now ready to use.

   For advanced controls and dashboard features, see :ref:`control_commands_dashboard_5`.

