IO Expander
================

RGB LEDs
------------

.. image:: img/io_board_rgb.png

The board features 4 WS2812 RGB LEDs, offering customizable control. Users can turn them on or off, change their color (default set to blue), adjust display modes, and modify the change rate.

* To turn on the RGB LEDs:

  .. code-block:: shell

    sudo pironman5 -re on

* To turn them off:

  .. code-block:: shell

    sudo pironman5 -re off

* To change their color, input the desired hexadecimal color values:

  .. code-block:: shell

    sudo pironman5 -rc fe1a1a

* To switch display modes, choose from 5 options: ``breath / leap / flow / colorful / colorful_leap``:

  .. code-block:: shell

    sudo pironman5 -rs leap

* To adjust the RGB signal frequency (range: 400 ~ 1600, default 1000 kHz):

  .. code-block:: shell

    sudo pironman5 -fq 1600

* To modify the speed of change (range: 0 ~ 100%):

  .. code-block:: shell

    sudo pironman5 -rb 80

* For custom RGB LED effects, modify and run the script ``/opt/pironman5/ws2812_RGB.py``:

  * Edit the script:

    .. code-block:: shell

      sudo nano /opt/pironman5/ws2812_RGB.py

  * Save and exit with ``Ctrl+X``, ``Y``, then ``Enter``.

  * Execute the script:

    .. code-block:: shell

      sudo python3 /opt/pironman5/ws2812_RGB.py

RGB Select Pins
-------------------------

.. warning::

  As of now, only **SPI (IO10)** can drive the RGB LEDs. Other pins are not operational.

* The Raspberry Pi supports three high-speed signal driving modes for RGB LEDs: SPI (IO10), PWM (IO12), and PCM (IO21). Note that using these for RGB LEDs will disable their primary functions.

  .. image:: img/io_board_rgb_pin.png

  * SPI (IO10) is generally used for the SPI interface.
  * PWM (IO12) is typically for analog audio.
  * PCM (IO21) is often for digital audio.

* By default, **SPI (IO10)** is selected for RGB LED control. If you opt for a different pin during assembly, adjust the configuration accordingly:

  .. code-block:: shell

    sudo pironman5 -rp 21


RGB OUT Pins
-------------------------

.. image:: img/io_board_rgb_out.png

The WS2812 RGB LEDs support serial connection, allowing for the attachment of an external RGB LED strip. Connect the **SIG** pin to the external strip's **DIN** pin for expansion.

The default setup includes 4 RGB LEDs. Connect additional LEDs and update the count using:

.. code-block:: shell

  sudo pironman5 -rn 8



OLED Screen Connector
----------------------------

The OLED screen connector, with an address of 0x3C, is a key feature.

.. image:: img/io_board_oled.png


Infrared Receiver
---------------------------

.. image:: img/io_board_receiver.png

* **Model**: IRM-56384, operating at 38KHz.
* **Connection**: The IR receiver connects to **GPIO13**.
* **D1**: An infrared reception indicator that blinks upon signal detection.
* **J8**: A pin for enabling the infrared function. By default, a jumper cap is inserted for immediate functionality. Remove the cap to free GPIO13 if the IR receiver is not in use.

To utilize the IR receiver, verify its connection and install the necessary module:

* Test the connection:

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Install the ``lirc`` module:

  .. code-block:: shell

    sudo apt-get install lirc -y

* To test remote controller functionality, execute:

  .. code-block:: shell

    mode2 -d /dev/lirc0

Fans Pins
-----------

.. image:: img/io_board_fan.png

* **FAN1 and FAN 2**: Two sets of fan pins, directly connected to 5V and GND.
* **FAN**: The enable pin for fans, with **GPIO6** monitoring Raspberry Pi 5's PWM fan status. Connect a jumper cap for GPIO6 control; remove it to free up GPIO6 if not in use.
* **D3**: A fan signal indicator that lights up when the fan is active.

Pin Headers
------------

.. image:: img/io_board_pin_header.png

Two right-angle header connectors extend the Raspberry Pi's GPIO, but note that the IR receiver, RGB LED, and fan occupy some pins. Remove the corresponding jumper caps to utilize these pins for other functions.

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5
    - Raspberry Pi 5
  * - IR Receiver(Optional)
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - FAN(Optional)
    - GPIO6
  * - RGB(Optional)
    - GPIO10
  * - RGB(Optional)
    - GPIO12
  * - RGB(Optional)
    - GPIO21
