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

4. Set Up or Install Software
================================================

After installing the operating system onto your Micro SD card or NVMe SSD, insert it into your Pironman 5. Press the power button to turn on the device.

At this stage, you will notice that the power LEDs are lit, but certain features of the Pironman 5, such as the OLED display, RGB LEDs, and side-mounted RGB fan(s), will not be operational yet. This is because they require configuration through the ``pironman5.service``, which identifies and enables the specific features of your Pironman series product.

If you encounter screen garbling issues, you can ignore them for now, as they will be resolved after completing the configuration process.

To begin the configuration, you first need to boot and log into your Raspberry Pi. If you're unsure how to log in, visit the official Raspberry Pi website: |link_rpi_get_start|.

Once logged in, follow the configuration tutorial for your chosen system:


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


    
    