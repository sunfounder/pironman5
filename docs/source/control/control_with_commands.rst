.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _view_control_commands:

Control with Commands
========================================
In addition to viewing data from the Pironman 5 and controlling various devices through the Dashboard, you can also use commands to control them.

.. note::

  * For the **Home Assistant** system, you can only monitor and control the Pironman 5 through the dashboard by opening the webpage at ``http://<ip>:34001``.
  * For the **Batocera.linux** system, you can only monitor and control the Pironman 5 via commands. It is important to note that any changes to the configuration require a restart of the service using ``pironman5 restart`` to take effect.

View the Basic Configurations
-----------------------------------

The ``pironman5`` module offers basic configurations for Pironman, which you can review with the following command.

.. code-block:: shell

  pironman5 -c

The standard configurations appear as follows:

.. code-block:: 

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

Customize these configurations to fit your needs.

Use ``pironman5`` or ``pironman5 -h`` for instructions.

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format with or without # (e.g. #FF0000 or 00aabb)
    -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                          RGB style
    -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin

.. note::

  Each time you modify the status of ``pironman5.service``, you need to use the following command to make the configuration changes take effect.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verify the ``pironman5`` program status using the ``systemctl`` tool.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternatively, inspect the program-generated log files.

  .. code-block:: shell

    cat /opt/pironman5/log


Control RGB LEDs
----------------------
The board features 4 WS2812 RGB LEDs, offering customizable control. Users can turn them on or off, change the color, adjust the brightness, switch RGB LED display modes, and set the speed of changes.

.. note::

  Each time you modify the status of ``pironman5.service``, you need to use the following command to make the configuration changes take effect.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* To modify the on and off state of the RGB LEDs, ``true`` to turn on the RGB LEDs, ``false`` to turn them off.

.. code-block:: shell

  pironman5 -re true

* To change their color, input the desired hexadecimal color values, such as ``fe1a1a``.

.. code-block:: shell

  pironman5 -rc fe1a1a

* To change the brightness of the RGB LED (range: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rb 100

* To switch RGB LED display modes, choose from options: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  If you set the RGB LED display mode to ``rainbow``, ``rainbow_reverse``, or ``hue_cycle``, you will not be able to set the color using ``pironman5 -rc``.

.. code-block:: shell

  pironman5 -rs breathing

* To modify the speed of change (range: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rp 80

* The default setup includes 4 RGB LEDs. Connect additional LEDs and update the count using:

.. code-block:: shell

  pironman5 -rl 12

.. _cc_control_fan:

Control RGB Fans
---------------------
The IO expansion board supports up to two 5V non-PWM fans. Both fans are controlled together. 

.. note::

  Each time you modify the status of ``pironman5.service``, you need to use the following command to make the configuration changes take effect.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* You can use command to configure the operating mode of the two RGB fans. These modes determine the conditions under which the RGB fans will activate. 

For instance, if set to **1: Performance** mode, the RGB fans will activate at 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: The RGB fans will activate at 70°C.
* **3: Balanced**: The RGB fans will activate at 67.5°C.
* **2: Cool**: The RGB fans will activate at 60°C.
* **1: Performance**: The RGB fans will activate at 50°C.
* **0: Always On**: The RGB fans will always on.

* If you connect the control pin of the RGB fan to different pins on the Raspberry Pi, you can use the following command to change the pin number.

.. code-block:: shell

  sudo pironman5 -gp 18


Check the OLED Screen
-----------------------------------

When you have installed the ``pironman5`` library, the OLED screen displays CPU, RAM, Disk Usage, CPU Temperature, and the Raspberry Pi's IP Address, and it shows this every time you reboot.

If your OLED screen does not display any content, you need to first check if the OLED's FPC cable is connected properly.

Then you can check the program log to see what might be the problem through the following command.

.. code-block:: shell

  cat /var/log/pironman5/

Or check if the OLED's i2c address 0x3C is recognized:

.. code-block:: shell

  i2cdetect -y 1

Checkout the Infrared Receiver
---------------------------------------

To utilize the IR receiver, verify its connection and install the necessary module:

* Test the connection:

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Install the ``lirc`` module:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Now, test the IR Receiver by running the following command. 

  .. code-block:: shell

    mode2 -d /dev/lirc0

* After running the command, press a button on the remote control, and the code of that button will be printed.

