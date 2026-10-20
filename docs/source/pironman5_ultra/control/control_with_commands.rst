.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_commands_ultra:

Control with Commands
========================================
In addition to viewing data from Pironman 5 Ultra and controlling various devices through the Dashboard, you can also use commands to control them.

View the Basic Configurations
-----------------------------------

The ``pironman5`` module offers basic configurations for Pironman 5 Ultra, which you can review with the following command.

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
              "battery",
              "input",
              "rpi_power"
          ],
          "rgb_enable": true,
          "rgb_color": "#0a1aff",
          "rgb_brightness": 100,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "shutdown_percentage": 10,
          "pipower5_buzzer_volume": 5,
          "pipower5_buzz_on": [],
          "debug_level": "INFO"
      }
  }

Customize these configurations to fit your needs.

Use ``pironman5`` or ``pironman5 -h`` for instructions.

.. code-block:: text

  usage: pironman5-service [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]]
                          [-dl [{debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]]
                          [-eh [ENABLE_HISTORY]] [-u [{C,F}]] [-re [RGB_ENABLE]]
                          [-rs [RGB_STYLE]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-oe [OLED_ENABLE]]
                          [-or [{0,180}]] [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                          [{start,restart,stop,launch-browser}]

  Pironman 5 command line interface

  positional arguments:
    {start,restart,stop,launch-browser}
                        Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Database retention days
    -dl, --debug-level [{debug,info,warning,error,critical}]
                          Debug level
    -rd, --remove-dashboard
                          Remove dashboard
    -cp, --config-path [CONFIG_PATH]
                          Config path
    -eh, --enable-history [ENABLE_HISTORY]
                          Enable history, True/true/on/On/1 or False/false/off/Off/0
    -u, --temperature-unit [{C,F}]
                          Temperature unit
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
    -oe, --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          OLED pages, split by ',': mix,performance,ips,disk,battery,input,rpi_power
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds

.. note::

   Each time you modify the status of ``pironman5.service``, you need to restart the service to make the configuration changes take effect.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Verify the ``pironman5`` program status using the ``systemctl`` tool.

  .. code-block:: shell

     sudo systemctl status pironman5.service

* Alternatively, inspect the program-generated log files.

  .. code-block:: shell

     cat /var/log/pironman5/pironman5.log


Control the RGB Lighting
----------------------------

The RGB module drives the top RGB light strip and the two front RGB fans. Users can turn them on or off, change the color, adjust the brightness, switch the display mode, and set the speed of changes.

* To modify the on and off state of the RGB lighting, use ``true`` to turn it on, or ``false`` to turn it off.

  .. code-block:: shell

     sudo pironman5 -re true

* To change the color, input the desired hexadecimal color value, such as ``fe1a1a``.

  .. code-block:: shell

     sudo pironman5 -rc fe1a1a

* To change the brightness (range: ``0 ~ 100``):

  .. code-block:: shell

     sudo pironman5 -rb 100

* To switch the display mode, choose from:

  ``solid`` / ``breathing`` / ``flow`` / ``flow_reverse`` / ``rainbow`` / ``rainbow_reverse`` / ``hue_cycle``

  .. code-block:: shell

     sudo pironman5 -rs breathing

* To modify the animation speed (range: ``0 ~ 100``):

  .. code-block:: shell

     sudo pironman5 -rp 80


Control the PWM Fans
-------------------------

Pironman 5 Ultra has three PWM fans: one CPU turbo fan and two front RGB fans. They are driven by the Raspberry Pi system and follow the standard Raspberry Pi 5 temperature curve. The fans only have a control signal and no tachometer signal, so the speed cannot be read back.

* The CPU turbo fan is managed automatically by the Raspberry Pi firmware. No manual configuration is required.
* To check the current fan state:

  .. code-block:: shell

     cat /sys/class/thermal/cooling_device0/cur_state


Check the OLED Screen
-----------------------------------

When the ``pironman5`` library is installed, the OLED screen displays information automatically after each reboot. OLED has several pages, including ``mix``, ``performance``, ``ips``, ``disk``, ``battery``, ``input`` and ``rpi_power``.

A single click on the power button wakes the OLED screen and switches to the next page. A double click returns to the previous page.

To adjust which pages are shown and their order:

.. code-block:: shell

   sudo pironman5 -op battery,mix,rpi_power

Because OLED screens can suffer from burn-in if one image is displayed for a long time, the screen turns off automatically after a period. To set how long the OLED screen stays on:

.. code-block:: shell

   sudo pironman5 -os 20

If the OLED screen does not display any content, first check whether the OLED FPC cable is connected properly.

Then inspect the program log using the following command:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

You can also check whether the OLED I2C address ``0x3C`` is detected:

.. code-block:: shell

   i2cdetect -y 1


Audio Output Mode
-----------------------

Pironman 5 Ultra has built-in stereo speakers and a 3.5mm headphone jack. The output mode can be set on the Dashboard (Settings → Speaker Mode) or with the ``pironman5`` command:

* **Auto** (default): when a monitor is plugged into HDMI0 or headphones are inserted, the speaker output is turned off and audio is played through the external device.
* **ON**: the speakers stay on regardless of external devices.


PiPower 5 and Battery
---------------------------

PiPower 5 is installed together with the ``pironman5`` module on Pironman 5 Ultra, so there is no separate installation step.

Show all PiPower 5 status information:

.. code-block:: shell

   pipower5 -a

Example output:

.. code-block:: text

   Input:
      voltage: 0 mV
      current: 0 mA
      power: 0.000 W
      plugged in: False
   Output:
      voltage: 5296 mV
      current: 452 mA
      power: 2.394 W
   Battery:
      voltage: 8028 mV
      current: -315 mA
      power: -2.529 W
      percentage: 91 %
      source: 1 - Battery
      charging: False

   Internal:
      shutdown request: 0 - NONE
      power button: 0 - RELEASED
      max charging current: 0 mA
      default on: on
      shutdown percentage: 10 %

Useful commands:

* Show the battery percentage: ``pipower5 -bp``
* Show the charging status: ``pipower5 -ichg``
* Show the input voltage: ``pipower5 -iv``
* Read the shutdown percentage: ``pipower5 -sp``
* Set the shutdown percentage to 30%: ``pipower5 -sp 30``
* Check the default-on setting: ``pipower5 -do``
* Show the full command list: ``pipower5 --help``

.. note::

   After changing a PiPower 5 setting, restart the service to apply it:

   .. code-block:: shell

      sudo systemctl restart pironman5.service

**Power Failure Simulation**

Back up your data and close affected software first. Make sure the battery level is above 80% and external power is connected.

.. code-block:: shell

   pipower5 -pfs

**Notifications**

PiPower 5 can notify you through the buzzer and email. Configure the events on the Dashboard or with the CLI.

* Set which events trigger the buzzer: ``pipower5 -bzo power_disconnected low_battery``
* Set the buzzer volume: ``pipower5 -bzv 5``
* Test the buzzer: ``pipower5 -bzt power_disconnected``
* Set which events send an email: ``pipower5 -seo low_battery power_disconnected``
* Set the recipient email address: ``pipower5 -set you@example.com``
* Configure the SMTP server, port, account, password and security: ``pipower5 -ss smtp.gmail.com -smp 465 -se you@gmail.com -spw <APP_PASSWORD> -ssc ssl``


View the Runtime Log
-------------------------

Check the ``pironman5`` service status with ``systemctl``:

.. code-block:: shell

   sudo systemctl status pironman5.service

Or view the log files generated by the program:

.. code-block:: shell

   ls /var/log/pironman5/
