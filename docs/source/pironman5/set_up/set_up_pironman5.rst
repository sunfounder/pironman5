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

4. Set up or Install Software
================================================

Now that the system has been written to either the Micro SD or NVMe SSD, you can insert them into the Pironman 5 slot. Then press the power button to turn on the device.

After powering on, you will see the various power LEDs lit up, but the OLED screen, RGB LEDs, and RGB fans (the two fans on the side) will not be operational yet, as they need to be configured. If there is a screen garbling issue, please ignore it for now; it will be resolved after configuration.

Before configuring, you need to boot up and log into your Raspberry Pi. If you're unsure how to log in, you can visit the official Raspberry Pi website: |link_rpi_get_start|.

You can then proceed to select the configuration tutorial based on your system.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_batocera


**About Power Button**

The power button brings out the power button of the Raspberry Pi 5, and it functions just like the power button of the Raspberry Pi 5.

* **Shutdown**

    * If you run Raspberry Pi **Bookworm Desktop** system, you can press the power button twice in quick succession to shutdown. 
    * If you run Raspberry Pi **Bookworm Lite** system, press the power button a single time to initiate a shutdown.
    * To force a hard shutdown, press and hold the power button.

* **Power on**

    * If the Raspberry Pi board is shut down, but still powered, single-press to power on from a shutdown state.

* If you are running a system that does not support a shutdown button, you can hold it for 5 seconds to force a hard shutdown, and single-press to power on from a shutdown state.


    
    