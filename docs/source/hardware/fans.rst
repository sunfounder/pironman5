Fans
============

PWM Fan
-----------

The PWM fan on the Pironman 5 is controlled by the Raspberry Pi system, and its operation influences the two additional RGB fans. These RGB fans activate and deactivate in sync with the PWM fan.

Regarding cooling solutions for the Raspberry Pi 5, especially under heavy load, the design of the Pironman 5 incorporates a smart cooling system. It features a primary PWM fan and two supplementary RGB fans. The cooling strategy is closely integrated with the Raspberry Pi 5's thermal management system.

The PWM fan's operation is based on the Raspberry Pi 5's temperature:

* Below 50°C, the PWM fan remains off (0% speed).
* At 50°C, the fan starts at a low speed (30% speed).
* Reaching 60°C, the fan increases to a medium speed (50% speed).
* At 67.5°C, the fan ramps up to a high speed (70% speed).
* At 75°C and above, the fan operates at full speed (100% speed).

This temperature-to-speed relationship also applies when the temperature decreases, with a 5°C hysteresis. The fan speed reduces when the temperature falls 5°C below each of these thresholds.

* Commands to monitor the PWM fan. To check the PWM fan's status:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* To view the PWM fan's speed:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

In the Pironman 5, the PWM fan is a critical component for maintaining optimal operating temperatures, particularly during intensive tasks, ensuring the Raspberry Pi 5 runs efficiently and reliably.

RGB Fans
-------------------

.. image:: img/size_fan.png

* **Extermal dimension**: 40*40*10MM
* **Weight**: 13.5±5g/pcs
* **Life**: 40,000 hours (room temperature 25°C)
* **Maximum Air Flow**: 2.46CFM
* **Max.Air Pressure**: 0.62mm-H2O
* **Accoustic Sound**: 22.31dBA
* **Rated Input power**: 5V/0.1A
* **Rated Speed**: 3500±10%RPM
* **Operating Temperature**: -10℃~+70℃
* **Storage Temperature**: -30℃~+85℃