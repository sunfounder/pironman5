.. _install_batocera:


Installing and Configuring Batocera.linux on Pironman 5
=========================================================

Batocera.linux is an open-source and completely free retro-gaming distribution that can be copied to a USB stick or an SD card with the aim of turning any computer or nano computer into a gaming console, whether temporarily during a game session or permanently. No modifications are needed on your computer to use Batocera.linux.

Install Batocera.linux OS
----------------------------------
Now, let's explore how to install the Batocera.linux system on Pironman 5 and configure it to ensure that the OLED display, the two RGB fans, and the 4 RGB LEDs function correctly under the Batocera.linux system.

#. First, navigate to the |link_batocera_download| page, select **Raspberry Pi 5 B**, and click to download.

   .. image:: img/batocera_download.png
       :width: 600
       :align: center

#. Next, open the `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_ to begin writing the system to an SD card or SSD.

   .. image:: img/batocera_os_open.png
       :width: 600
       :align: center

#. Then, click on **CHOOSE OS** and scroll down to the end to select **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
       :width: 600
       :align: center

#. Choose the system file you have just downloaded, ``batocera-xxx-xx-xxxxxxxx.img.gz``, and then click **Open**.

   .. image:: img/batocera_os_choose.png
       :width: 600
       :align: center

#. Wait for the success notification indicating that the writing process is complete. You can now insert the SD card with the batocera system into Pironman5 and press the power button to start the device.

#. Once the system boots up, use ssh to remotely connect to Pironman5. For Windows, you can open **Powershell**, and for Mac OS X and Linux, you can directly open **Terminal**.

   .. image:: img/batocera_powershell.png
       :width: 600
       :align: center

#. The default hostname for the batocera system is ``batocera``, with the default username as ``root`` and the password as ``linux``. Therefore, you can log in by typing ``ssh root@batocera.local`` and entering the password ``linux``.

   .. image:: img/batocera_login.png
       :width: 600
       :align: center

#. Execute the command: ``/etc/init.d/S92switch`` setup to enter the menu settings page.

   .. image:: img/batocera_configure.png
       :width: 600
       :align: center

#. Use the down arrow key to navigate to the end, select and activate the **Pironman5** services.

   .. image:: img/batocera_configure_pironman5.png
       :width: 600
       :align: center

#. After activating the pironman5 service, select **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
       :width: 600
       :align: center

#. Execute the command ``reboot`` to restart Pironman5.

   .. code-block:: shell

      reboot

#. Upon reboot, the ``pironman5.service`` will start automatically. Here are the primary configurations for Pironman 5:

  * The OLED screen displays CPU, RAM, Disk Usage, CPU Temperature, and the Raspberry Pi's IP Address.
  * Four WS2812 RGB LEDs will light up in blue with a breathing mode.
  * The RGB fans will activate at 60°C.


Now, you can connect the Pironman 5 to a screen, game controllers, headphones, and more to immerse yourself in your gaming world.

.. note::

    The next steps involve further configurations such as modifying the color effects of the RGB strips, adjusting the activation temperature of the RGB fans, and checking the OLED Screen, among others. You can set these aside for now and refer back when needed.

View the Basic Configurations
-----------------------------------

The ``pironman5`` module offers basic configurations for Pironman 5, which you can review with the following command.

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

    usage: pironman5-service [-h] [-c] [-rc [RGB_COLOR]]
                            [-rb [RGB_BRIGHTNESS]]
                            [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]]
                            [-rp [RGB_SPEED]] [-re [RGB_ENABLE]]
                            [-rl [RGB_LED_COUNT]] [-u [{C,F}]]
                            [-gm [GPIO_FAN_MODE]]
                            [-gp [GPIO_FAN_PIN]]
                            [--background [BACKGROUND]]
                            [{start,restart,stop}]

    Pironman5

    positional arguments:
    {start,restart,stop}  Command

    options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                            RGB color in hex format without # (e.g.
                            00aabb)
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
                            GPIO fan mode, 0: Always On, 1:
                            Performance, 2: Cool, 3: Balanced, 4:
                            Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                            GPIO fan pin
    --background [BACKGROUND]
                            Run in background


.. note::

    For any changes in settings to take effect, use the following command:

    .. code-block:: shell

        pironman5 restart

Control RGB LEDs
----------------------
The board features 4 WS2812 RGB LEDs, offering customizable control. Users can turn them on or off, change the color, adjust the brightness, switch RGB LED display modes, and set the speed of changes.

.. note::

    For any changes in settings to take effect, use the following command:

    .. code-block:: shell

        pironman5 restart

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

Control RGB Fans
---------------------
The IO expansion board supports up to two 5V non-PWM fans. Both fans are controlled together. 

.. note::

  For any changes in settings to take effect, use the following command:

  .. code-block:: shell

    pironman5 restart

* You can use command to configure the operating mode of the two RGB fans. These modes determine the conditions under which the RGB fans will activate. 

For instance, if set to **1: Performance** mode, the RGB fans will activate at 50°C.


.. code-block:: shell

    sudo pironman5 -gm 3

* **4: Quiet**: The RGB fans will activate at 70°C.
* **3: Balanced**: The RGB fans will activate at 67.5°C.
* **2: Cool**: The RGB fans will activate at 60°C.
* **1: Performance**: The RGB fans will activate at 50°C.
* **0: Always On**: The RGB fans will always on.

If you connect the control pin of the RGB fan to different pins on the Raspberry Pi, you can use the following command to change the pin number.

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
