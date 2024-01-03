Power Button
=====================

This is a power button that leads from the Raspberry Pi 5 to power off the Raspberry Pi directly.

.. image:: img/pironman_button.JPG

**Adding the Power Button**

The Raspberry Pi 5 features a **J2** jumper, situated between the RTC battery connector and the board edge. This breakout enables the addition of a custom power button to the Raspberry Pi 5 by connecting a Normally Open (NO) momentary switch across the two pads. Briefly engaging this switch mimics the onboard power button's functionality.

.. image:: img/pi5_j2.jpg

On the Pironman 5, there's a **Power Switch Converter** that extends the **J2** jumper to an external power button using two Pogo pins.

.. image:: img/power_switch_convertor.png

**Power Cycling**

Upon initially powering your Raspberry Pi, it will automatically turn on and boot into the operating system without the need to press the button.

If running the Raspberry Pi Desktop, a brief press of the power button initiates a clean shutdown process. A menu will appear, offering options to shutdown, reboot, or logout. Selecting an option or pressing the power button again will start a clean shutdown.

.. image:: img/button_shutdown.png

**Shutdown Operations**

* For the **bookworm Desktop** system: Double-click to safely shut down, hold for 5 seconds to force a shutdown, and single-click to power on from a shutdown state.
* For the **bookworm lite** system: Single-click to safely shut down when powered on, hold for 5 seconds to force a shutdown, and single-click to power on from a shutdown state.
* For other systems: Hold for 5 seconds to force a shutdown, and single-click to power on from a shutdown state.

