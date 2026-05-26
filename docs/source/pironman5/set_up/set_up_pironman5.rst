.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _set_up_pironman5_5:

4. Setting Up or Installing Software
================================================

Now that the system has been written to either the Micro SD or NVMe SSD, you can insert them into the Pironman 5 slot. Then press the power button to turn on the device.

After powering on, you will see the various power LEDs lit up, but the OLED screen, RGB LEDs, and GPIO Fans (the two fans on the side) will not be operational yet, as they need to be configured. If there is a screen garbling issue, please ignore it for now; it will be resolved after configuration.

Before configuring, you need to boot up and log into your Raspberry Pi. If you're unsure how to log in, you can visit the official Raspberry Pi website: |link_rpi_get_start|.

You can then proceed to select the configuration tutorial based on your system.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel
    set_up_batocera

**About Power Button**

The power button brings out the power button of the Raspberry Pi 5, and it functions just like the power button of the Raspberry Pi 5.

* **Shutdown**

    * If you run **Raspberry Pi OS Desktop** system, you can press the power button twice in quick succession to shutdown. 
    * If you run **Raspberry Pi OS Lite** system, press the power button a single time to initiate a shutdown.
    * To force a hard shutdown, press and hold the power button.

* **Power on**

    * If the Raspberry Pi board is shut down, but still powered, single-press to power on from a shutdown state.

* If you are running a system that does not support a shutdown button, you can hold it for 5 seconds to force a hard shutdown, and single-press to power on from a shutdown state.


    
    