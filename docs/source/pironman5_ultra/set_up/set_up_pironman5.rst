.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _set_up_pironman5_ultra:

4. Setting Up or Installing Software
================================================

Now that the system has been written to either the Micro SD or NVMe SSD, you can insert it into the Pironman 5 Ultra slot. Then press the power button to turn on the device — **no external power supply is required**, because the built-in PiPower 5 module runs on the battery.

.. note::

   PiPower 5 is set to **Default On** by default, so the device also powers on automatically as soon as external power is connected. Whether the **Default On** jumper is at ON or OFF, you can always turn the device on by pressing the power button.

After powering on, you will see the various power LEDs lit up, but the OLED screen and the RGB lighting will not be operational yet, as they need to be configured. If there is a screen garbling issue, please ignore it for now; it will be resolved after configuration.

Before configuring, you need to boot up and log into your Raspberry Pi. If you're unsure how to log in, you can visit the official Raspberry Pi website: |link_rpi_get_start|.

You can then proceed to select the configuration tutorial based on your system.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os

**About the Power Button**

The power button on Pironman 5 Ultra is the PiPower 5 button. It controls the power of the whole device, including the battery.

* **Short press**

    * When the device is off, single-press to power on. No external power supply is required — the built-in battery supplies the power.
    * When the Raspberry Pi is running, single-press wakes the OLED screen and switches to the next OLED page.

* **Long press for 2 seconds**

    * Sends a safe shutdown request to the Raspberry Pi. After the Raspberry Pi shuts down, PiPower 5 cuts the power automatically (requires the shutdown configuration described in :ref:`safe_shutdown_ultra`).

* **Keep holding to 5 seconds**

    * Cuts the power immediately (hard shutdown).

.. note::

   You can also shut down the Raspberry Pi from the desktop menu or with ``sudo shutdown now``. PiPower 5 detects the shutdown state and cuts the power afterwards.
