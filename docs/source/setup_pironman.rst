.. _set_up_pironman:

5. Setting Up the Pironman
===================================

.. note::
    * The Pironman 5 functions similarly to a PC and requires the power button for powering on/off.


Configuring Shutdown to Deactivate GPIO Power
------------------------------------------------------------
To prevent the OLED screen and RGB fans, powered by the Raspberry Pi GPIO, from remaining active post-shutdown, it's essential to configure the Raspberry Pi for GPIO power deactivation.

* Manually edit the ``EEPROM`` configuration file with this command:

  .. code-block:: shell

    sudo rpi-eeprom-config -e

* Modify the ``POWER_OFF_ON_HALT`` setting in the file to ``1``. For instance:

  .. code-block:: shell

    BOOT_UART=1
    POWER_OFF_ON_HALT=1
    BOOT_ORDER=0xf416

Downloading and Installing the Software
-----------------------------------------

.. note::

  For lite systems, initially install tools like ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
  
  .. code-block:: shell
  
    sudo apt-get update
    sudo apt-get install git -y
    sudo apt-get install python3 python3-pip python3-setuptools -y

Proceed to download and install the source code from GitHub.

.. code-block:: shell

  cd ~
  git clone https://github.com/sunfounder/pironman5.git
  cd ~/pironman5
  sudo python3 install.py

A system reboot is required to activate the installation. Follow the on-screen reboot prompt.

Here are the primary configurations for Pironman:

  * The OLED screen displays CPU, RAM, Disk Usage, CPU Temperature, and the Raspberry Pi's IP Address.
  * You can execute a double press for a safe shutdown or hold for 5 seconds for a forced shutdown.
  

Modifying the Configuration
-----------------------------

The ``pironman5`` module offers basic configurations for Pironman, which you can review with the following command.

.. code-block:: shell

    sudo pironman5 -c

The standard configurations appear as follows:

.. code-block:: 

  config file:/opt/pironman5/config.txt
  
  temp_unit = C
  rgb_enable = True
  rgb_num = 4
  rgb_style = breath
  rgb_color = 0a1aff
  rgb_blink_speed = 50
  rgb_freq = 1000
  rgb_pin = 10

Customize these configurations to fit your needs.

Use ``sudo pironman5``, ``sudo pironman5 -h``, or ``sudo pironman5 --help`` for instructions.

.. code-block:: shell

    config file:/opt/pironman5/config.txt

    Usage:
    pironman5 <OPTION> <input>

    Options:
    start                start pironman5 service
    stop                 stop pironman5 service
    restart              restart pironman5 service
    -h,--help            help, show this help
    -c,--check           show all configurations
    -a,--auto            [ on ],enable auto-start at boot
                        [ off ], disable auto-start at boot
    -u,--unit            [ C/F ], set the unit of temperature,
                        C or F (Celsius/Fahrenheit)
    -re|--rgb_enable     [on/true/off/false], whether enable rgb strip,
    -rn|--rgb_num        the number of rgb lamp beads, default 4
    -rs,--rgb_style      rgb strip display style, default: breath,
                        in [breath / leap / flow / colorful / colorful_leap]
    -rc,--rgb_color      [(HEX)color], set the color of rgb strip,
                        default: 0a1aff
    -rb,--rgb_speed      [speed], rgb blink speed (0 ~ 100, default 50)
    -fq,--rgb_freq       [frequency], rgb signal frequency (400 ~ 1600, default 1000 kHz)
    -rp,--rgb_pin        [pin], rgb signal pin, could be [10 / spi/ SPI / 12 / pwm/ PWM] or
                        [21 / pcm / PCM], default 10
    -F,--foreground      run in foreground

.. note::

    The ``-rp`` command is currently unavailable, please disregard it for now.


* Verify the ``pironman5`` program status using the ``systemctl`` tool.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternatively, inspect the program-generated log files.

  .. code-block:: shell

    cat /opt/pironman5/log

* To deactivate automatic program execution at boot:

  .. code-block:: shell

    sudo pironman5 -a off

* To reset the RGB LEDs' color:

  .. code-block:: shell

    sudo pironman5 -rc ff8a40


* You can directly modify configurations in ``/opt/pironman5/config.txt``.

  .. code-block:: shell

    sudo nano /opt/pironman5/config.txt

  Press ``Ctrl+X`` -> ``Y`` -> ``Enter`` to save and exit.

.. note::
  For a detailed introduction and configuration of Pironman 5 components, refer to: :ref:`about_hardware`.
