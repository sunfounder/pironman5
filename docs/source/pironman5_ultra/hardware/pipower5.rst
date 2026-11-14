.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _pipower5_ultra:

PiPower 5 and Battery
=========================

Pironman 5 Ultra integrates the **PiPower 5** module, which provides uninterruptible power for the Raspberry Pi 5. For the complete hardware description of the PiPower 5 module itself, please refer to the `PiPower 5 documentation <https://docs.sunfounder.com/projects/pipower5/en/latest/>`_.

.. note::

   Pironman 5 Ultra and the PiPower 5 module are only supported on **64-bit operating systems**.

Power Input
----------------

* **Input**: 5-15V, 45W Max, USB Type-C PD or screw terminal
* **Output for Raspberry Pi**: 5V/5A
* **Charging power**: 5 / 10 / 15 / 20W (selectable)

It is recommended to use a **45W or higher USB Type-C PD power supply**. With the official 27W power supply the Raspberry Pi can still be powered at up to 5V/5A, but the charging power is limited to 5W.

Battery
----------------

* **Model**: Power Pack SFB20003C2S
* **Capacity**: 7.4V 2000mAh
* **Type**: 2-cell Li-ion
* **Connector**: VH3.96-2P

The battery is installed on the side acrylic panel. When external power is disconnected, the battery keeps the Raspberry Pi running and PiPower 5 can shut it down safely.

.. warning::

   Make sure the battery connector is inserted with the correct polarity. Do not reverse it, do not short-circuit the battery, and do not pierce or crush the battery pack.

Charge Select
-------------------

Charging power is configured with the **Charge SEL** DIP switch (switches 1 and 2). Both switches are OFF by default, which means 5W.

.. csv-table:: Charging Power Settings
   :header: "Switch 1", "Switch 2", "Charging Power"
   :widths: 20, 20, 20

   "OFF", "OFF", "5W"
   "ON", "OFF", "10W"
   "OFF", "ON", "15W"
   "ON", "ON", "20W"

**How to choose the charging power**

.. code-block:: text

   Power supply = Power needed by the Raspberry Pi + Charging power

We recommend calculating the power needed by the Raspberry Pi as 20W, or even 25W. So if you use a 30W power supply, set the charging power to 10W or 5W. If you use a 45W power supply, you can safely set the charging power to 20W.

.. note::

   If the charging power is set too high, the Raspberry Pi may shut down because of insufficient power.

Default On
---------------

PiPower 5 is set to **Default On** by default, which means the device powers on automatically as soon as external power is connected. This setting only controls the automatic power-on: because Pironman 5 Ultra has a built-in battery, you can always turn the device on by pressing the power button, with or without an external power supply. If you do not want the automatic power-on behavior, move the **Default On** jumper cap from ON to OFF.

Power Button
-----------------

* **Short press**: Power on, or wake the OLED screen.
* **Hold for 2 seconds**: Shut down the Raspberry Pi safely.
* **Keep holding to 5 seconds**: Cut the power immediately (hard shutdown).

Shutdown Behaviour
-----------------------

PiPower 5 relies on the Raspberry Pi shutdown state to control the power output. Configure the Raspberry Pi as described in :ref:`safe_shutdown_ultra` so that PiPower 5 can cut the power automatically after the Raspberry Pi shuts down.

PiPower 5 supports these shutdown methods:

* Hold the PiPower button for 2 seconds
* Shut down from the Raspberry Pi desktop menu, or run ``sudo shutdown now``
* Automatic shutdown when the battery level falls below the configured **shutdown percentage**

Shutdown Percentage
-------------------------

The **shutdown percentage** is the battery level at which PiPower 5 notifies the Raspberry Pi to shut down. When the battery falls below this value and there is no external power, PiPower 5 sends a ``LOW BATTERY`` shutdown request over I2C; after the Raspberry Pi shuts down, PiPower 5 cuts the power.

.. tip::

   On the Raspberry Pi 5, if the power consumption is high (more than 3A), the battery cannot supply power for a long time. In this case set the shutdown percentage to ``100%``, so that the Raspberry Pi shuts down immediately when the external power is disconnected, protecting the system and your data.

You can change the shutdown percentage from the Dashboard or with the ``pipower5`` command. See :ref:`view_control_dashboard_ultra` and :ref:`view_control_commands_ultra`.

Power Failure Simulation
-----------------------------

The power failure simulation tests whether the device keeps running when external power is cut, and how the battery behaves afterwards.

Before running the test, back up your data and close software or services that may be affected. Make sure the battery level is above **80%** and that external power is connected.

Run the test from **Settings → Power Failure Simulation** on the Dashboard, or with:

.. code-block:: shell

   sudo pipower5 -pfs

The test uses the onboard MOSFET to simulate disconnecting the external input. After disconnecting, the battery status is monitored for **1 minute**. The test then ends automatically, restores external power, and prints a short report about the battery status during that minute and the estimated remaining runtime.

Desktop Battery Icon
--------------------------

After the PiPower 5 service is installed and running, it registers itself as a system battery device, so a small battery icon appears in the desktop status bar showing the battery level and whether it is charging. The device path is ``/dev/pipower5``.

Notifications
------------------

The PiPower 5 board has a buzzer, and the software can also send email notifications for important power events.

See :ref:`notifications_ultra` for the list of events and how to configure the buzzer and the email notifications.
