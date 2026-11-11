.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _rgb_module_ultra:

RGB Module
================

The RGB module is located on the top of the case. It is an integrated module that provides the following functions:

* **RGB light strip**: the light strip on the top of the case, using WS2812 addressable RGB LEDs.
* **Fan adapter connector**: provides the connection for the front RGB fans.
* **OLED connector**: connects the OLED screen.
* **I2C microcontroller**: an onboard microcontroller communicates with the Raspberry Pi over I2C and drives the LED effects.

The Raspberry Pi communicates with the microcontroller on the RGB module over I2C. The microcontroller drives the WS2812 RGB LEDs to produce full-color effects. The RGB light strip and the two front RGB fans are controlled by the same module, so their lighting effects are synchronized.

**Control Method**

* The Raspberry Pi talks to the microcontroller on the RGB module over I2C.
* The microcontroller drives the WS2812 RGB LEDs to produce full-color effects.
* The RGB light strip and the RGB fans are controlled together for synchronized lighting.
* The style, color, brightness and animation speed can be set on the Dashboard or with the CLI.

.. note::

   The microcontroller runs a default breathing effect by itself. The RGB light strip and the front RGB fans
   therefore light up as soon as the device is powered on, **even if the** ``pironman5`` **software is not installed**.
   The software is only needed to change the style, color, brightness or speed.

RGB LEDs
-------------

The module drives the top RGB light strip and the two front RGB fans. Users can turn them on or off, change the color, adjust the brightness, switch display modes, and set the speed of changes.

* To modify the on and off state of the RGB LEDs, use ``true`` to turn them on, or ``false`` to turn them off.

.. code-block:: shell

  sudo pironman5 -re true

* To change the color, input the desired hexadecimal color value, such as ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* To change the brightness of the RGB LEDs (range: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* To switch display modes, choose from: ``solid`` / ``breathing`` / ``flow`` / ``flow_reverse`` / ``rainbow`` / ``rainbow_reverse`` / ``hue_cycle``:

.. note::

  If you set the display mode to ``rainbow``, ``rainbow_reverse``, or ``hue_cycle``, you will not be able to set the color using ``sudo pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* To modify the speed of change (range: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rp 80

Front RGB Fan Pin Definition
---------------------------------

Each front RGB fan uses a 5-pin connector:

.. csv-table:: Front RGB Fan Pins
   :header: "Pin color", "Function"
   :widths: 25, 50

   "Blue", "PWM signal (speed control)"
   "Red", "5V power"
   "Black", "GND"
   "Yellow", "RGB_DIN (RGB data input)"
   "Green", "RGB_DATA_OUT (RGB data output, for daisy-chaining)"

The fan has a built-in WS2812 RGB LED. The yellow and green pins carry the RGB lighting data, so several fans can be daisy-chained and controlled together by the RGB module.

OLED Screen Connector
----------------------------

The OLED screen connector, with an I2C address of ``0x3C``, is located on the RGB module.

If the OLED screen is not displaying or displaying incorrectly, you can follow these steps to troubleshoot the issue:

Check if the FPC cable of the OLED screen is properly connected.

#. Use the following command to view the program's run logs and check for error messages.

    .. code-block:: shell

        cat /var/log/pironman5/pironman5.log

#. Alternatively, use the following command to check if the OLED's I2C address ``0x3C`` is recognized:
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. If the first two steps don't reveal any issues, try restarting the ``pironman5`` service.

    .. code-block:: shell

        sudo systemctl restart pironman5.service
