.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Fans
============

CPU Fan
-----------

The CPU Fan on the Pironman 5 MAX is controlled by the Raspberry Pi system.

Regarding cooling solutions for the Raspberry Pi 5, especially under heavy load, the design of the Pironman 5 MAX incorporates a smart cooling system. It features a primary CPU Fan and two supplementary GPIO Fans. The cooling strategy is closely integrated with the Raspberry Pi 5's thermal management system.

The CPU Fan's operation is based on the Raspberry Pi 5's temperature:

* Below 50°C, the CPU Fan remains off (0% speed).
* At 50°C, the fan starts at a low speed (30% speed).
* Reaching 60°C, the fan increases to a medium speed (50% speed).
* At 67.5°C, the fan ramps up to a high speed (70% speed).
* At 75°C and above, the fan operates at full speed (100% speed).

This temperature-to-speed relationship also applies when the temperature decreases, with a 5°C hysteresis. The fan speed reduces when the temperature falls 5°C below each of these thresholds.

* Commands to monitor the CPU Fan. To check the CPU Fan's status:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* To view the CPU Fan's speed:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

In the Pironman 5 MAX, the CPU Fan is a critical component for maintaining optimal operating temperatures, particularly during intensive tasks, ensuring the Raspberry Pi 5 runs efficiently and reliably.

GPIO Fans
-------------------

.. image:: img/size_fan.png

* **Extermal dimension**: 40*40*10MM
* **Weight**: 13.5±5g/pcs
* **Life**: 30,000 hours (room temperature 25°C)
* **Maximum Air Flow**: 2.46CFM
* **Max.Air Pressure**: 0.62mm-H2O
* **Accoustic Sound**: 22.31dBA
* **Rated Input power**: 5V/0.15A
* **Rated Speed**: 3500±10%RPM
* **Operating Temperature**: -10℃~+60℃
* **Storage Temperature**: -20℃~+70℃

