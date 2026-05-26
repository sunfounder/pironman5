.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _max_view_control_commands:

Control with Commands
========================================
In addition to viewing data from the Pironman 5 MAX and controlling various devices through the Dashboard, you can also use commands to control them.

.. note::

  * For the **Home Assistant** system, you can only monitor and control the Pironman 5 MAX through the dashboard by opening the webpage at ``http://<ip>:34001``.

View the Basic Configurations
-----------------------------------

The ``pironman5`` module offers basic configurations for Pironman, which you can review with the following command.

.. code-block:: shell

  sudo pironman5 -c

The standard configurations appear as follows:

.. code-block:: 

  {
      "system": {
          "data_interval": 1,
          "database_retention_days": 30,
          "temperature_unit": "C",
          "enable_history": true,
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "rgb_enable": true,
          "rgb_color": "#0a1aff",
          "rgb_brightness": 100,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_led_count": 4,
          "rgb_led_count_min": 4,
          "gpio_fan_pin": 6,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "on",
          "gpio_fan_led_pin": 5,
          "debug_level": "INFO"
      }
  }

Customize these configurations to fit your needs.

Use ``pironman5`` or ``pironman5 -h`` for instructions.

.. code-block::

    usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]] [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]]
                    [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-or [{0,180}]]
                    [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                    {start,stop,launch-browser} ...

    Pironman 5 Max command line interface

    options:
      -h, --help            show this help message and exit
      -v, --version         Show version
      -c, --config          Show config
      -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                            Database retention days
      -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                            Debug level
      -rd, --remove-dashboard
                            Remove dashboard
      -cp, --config-path [CONFIG_PATH]
                            Config path
      -eh, --enable-history [ENABLE_HISTORY]
                            Enable history, True/true/on/On/1 or False/false/off/Off/0
      -re, --rgb-enable [RGB_ENABLE]
                            RGB enable True/False
      -rs, --rgb-style [RGB_STYLE]
                            RGB style: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
      -rc, --rgb-color [RGB_COLOR]
                            RGB color in hex format without # (e.g. 00aabb)
      -rb, --rgb-brightness [RGB_BRIGHTNESS]
                            RGB brightness 0-100
      -rp, --rgb-speed [RGB_SPEED]
                            RGB speed 0-100
      -rl, --rgb-led-count [RGB_LED_COUNT]
                            RGB LED count int
      -u, --temperature-unit [{C,F}]
                            Temperature unit
      -gm, --gpio-fan-mode [GPIO_FAN_MODE]
                            GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
      -gp, --gpio-fan-pin [GPIO_FAN_PIN]
                            GPIO fan pin
      -fl, --gpio-fan-led [GPIO_FAN_LED]
                            GPIO fan LED state on/off/follow
      -fp, --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                            GPIO fan LED pin
      -oe, --oled-enable [OLED_ENABLE]
                            OLED enable True/true/on/On/1 or False/false/off/Off/0
      -or, --oled-rotation [{0,180}]
                            Set to rotate OLED display, 0, 180
      -op, --oled-pages [OLED_PAGES]
                            OLED pages, split by ',': mix,performance,ips,disk
      -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                            OLED sleep timeout in seconds

    Subcommands:
      {start,stop,launch-browser}
        start               Start Pironman5
        stop                Stop Pironman5
        launch-browser      Launch browser

.. note::

  Each time you modify the status of ``pironman5.service``, you need to use the following command to make the configuration changes take effect.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verify the ``pironman5`` program status using the ``systemctl`` tool.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternatively, inspect the program-generated log.

  .. code-block:: shell

      cat /var/log/pironman5/pironman5.log


Control RGB LEDs
----------------------
The board features 4 WS2812 RGB LEDs, offering customizable control. Users can turn them on or off, change the color, adjust the brightness, switch RGB LED display modes, and set the speed of changes.

.. note::

  Each time you modify the status of ``pironman5.service``, you need to use the following command to make the configuration changes take effect.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* To modify the on and off state of the RGB LEDs, ``true`` to turn on the RGB LEDs, ``false`` to turn them off.

.. code-block:: shell

  sudo pironman5 -re true

* To change their color, input the desired hexadecimal color values, such as ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* To change the brightness of the RGB LED (range: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* To switch RGB LED display modes, choose from options: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  If you set the RGB LED display mode to ``rainbow``, ``rainbow_reverse``, or ``hue_cycle``, you will not be able to set the color using ``pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* To modify the speed of change (range: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rp 80

* The default setup includes 4 RGB LEDs. Connect additional LEDs and update the count using:

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_max:

Control GPIO Fans
---------------------
The IO expansion board supports up to two 5V non-CPU Fans. Both fans are controlled together. 

.. note::

  Each time you modify the status of ``pironman5.service``, you need to use the following command to make the configuration changes take effect.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* You can use command to configure the operating mode of the two GPIO Fans. These modes determine the conditions under which the GPIO Fans will activate. 

For instance, if set to **1: Performance** mode, the GPIO Fans will activate at 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: The GPIO Fans will activate at 70°C.
* **3: Balanced**: The GPIO Fans will activate at 67.5°C.
* **2: Cool**: The GPIO Fans will activate at 60°C.
* **1: Performance**: The GPIO Fans will activate at 50°C.
* **0: Always On**: The GPIO Fans will always on.

* If you connect the control pin of the RGB fan to different pins on the Raspberry Pi, you can use the following command to change the pin number.

.. code-block:: shell

  sudo pironman5 -gp 18


**About Core Fan**

The core fan connects to a dedicated 4-pin CPU Fan port on the Raspberry Pi 5. Its default control strategy is a firmware-managed, multi-level intelligent speed adjustment scheme based on CPU temperature. This means that when you use an official or compatible CPU Fan and connect it correctly, the system will automatically adjust the fan speed according to changes in CPU temperature (starting to operate above 50°C) without any manual intervention from you.


Check the OLED Screen
-----------------------------------

When you have installed the ``pironman5`` library, the OLED screen displays CPU, RAM, Disk Usage, CPU Temperature, and the Raspberry Pi's IP Address, and it shows this every time you reboot.

If your OLED screen does not display any content, you need to first check if the OLED's FPC cable is connected properly.

Then you can check the program log to see what might be the problem through the following command.

.. code-block:: shell

  cat /var/log/pironman5/pironman5.log

Or check if the OLED's i2c address 0x3C is recognized:

.. code-block:: shell

  i2cdetect -y 1

Checkout the Infrared Receiver
---------------------------------------

* Install the ``lirc`` module:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Now, test the IR Receiver by running the following command. 

  .. code-block:: shell

    mode2 -d /dev/lirc0

* After running the command, press a button on the remote control, and the code of that button will be printed.

