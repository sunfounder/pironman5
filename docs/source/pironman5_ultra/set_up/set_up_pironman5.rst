.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _set_up_pironman5_ultra:

4. Setting Up or Installing Software
================================================

Insert the Micro SD card or NVMe SSD with the system into Pironman 5 Ultra, then press the power button. **No external power supply is required** — the built-in PiPower 5 module runs on the battery.

.. note::

   PiPower 5 is set to **Default On**, so it also powers on automatically when external power is connected. The power button works either way.

The power LEDs light up right away, and the RGB light strip and front RGB fans start their breathing effect. Both are driven by the microcontroller on the RGB module, so they work **even before the** ``pironman5`` **software is installed**. The OLED screen stays blank until it is configured.

Log in to your Raspberry Pi (see |link_rpi_get_start|), then follow the tutorial for your system:

.. toctree::
    :maxdepth: 1

    set_up_rpi_os

**About the Power Button**

* **Short press**: power on when the device is off, or wake the OLED and switch to the next page when it is running.
* **Long press 2 seconds**: safe shutdown. PiPower 5 cuts the power afterwards (requires :ref:`safe_shutdown_ultra`).
* **Hold 5 seconds**: cut the power immediately.

.. note::

   You can also shut down from the desktop menu or with ``sudo shutdown now``; PiPower 5 cuts the power afterwards.
