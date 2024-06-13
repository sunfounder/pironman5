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

4. Set Up Pironman5
================================================

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

Software Configuration
--------------------------

1. If you have installed Raspberry Pi OS, Ubuntu, or Kali on your Raspberry Pi, you will need to configure the Pironman 5 using the command line. Detailed tutorials can be found below:


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 

2. If you have installed the Home Assistant system, you will need to add the necessary add-ons to Home Assistant and start them to get the Pironman 5 working.

.. note::

    The following method is only applicable to systems with Home Assistant installed natively. It does not apply to Raspberry Pi systems with Home Assistant installed on top or to Docker versions of Home Assistant.


.. toctree::
    :maxdepth: 1  

    set_up_home_assistant