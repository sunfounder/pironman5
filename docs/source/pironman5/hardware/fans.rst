.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _fan:

Fans
============

PWM Fan
-----------------

The PWM fan in the Pironman 5 is managed by the Raspberry Pi system and forms the cornerstone of its smart cooling solution, especially under heavy loads. This system combines a primary PWM fan with two supplementary RGB fans for enhanced cooling performance, closely integrated with the Raspberry Pi 5's thermal management system.  

.. image:: img/fan_tower_cooler.png  
  :width: 600  
  :align: center  

**Electrical Characteristics**

* **Rated Voltage**: 5 VDC  
* **Starting Voltage**: 4.0 V (at 25°C Power ON/OFF)  
* **Operating Voltage Range**: 4.0 ~ 5.5 VDC  
* **Rated Current**: 0.05 A / MAX. 0.08 A  
* **Rated Power**: 0.25 W / MAX. 0.40 W  
* **Rated Speed**: 3500±10% RPM (at 25°C, tested after 3 minutes of operation)  
* **Maximum Airflow**: 2.46 (MIN. 2.21) CFM (at zero static pressure)  
* **Maximum Static Pressure**: 0.62 (MIN. 0.496) mmH2O (at zero airflow)  
* **Acoustical Noise**: 22.31 dB(A) MAX. 25.31 dB(A)  
* **Life Expectancy**: 40,000 hours (at 25°C, 65% humidity, normal room conditions)  

**Mechanical Characteristics**

* **Dimensions**: 40x10.4x40 mm (LxWxH)  
* **Frame Material**: PBT Plastic  
* **Impeller Material**: PBT Plastic  
* **Bearing Type**: Hydraulic Bearing  

**Environmental Parameters**

* **Operating Temperature**: -10°C ~ 70°C  
* **Storage Temperature**: -40°C ~ 75°C  
* **Operating Humidity**: 5% ~ 90% RH  
* **Storage Humidity**: 5% ~ 95% RH  

**Fan Speed Control Based on Temperature**  

The PWM fan operates dynamically, adjusting its speed according to the Raspberry Pi 5's temperature:  

* **Below 50°C**: Fan remains off (0% speed).  
* **At 50°C**: Fan operates at low speed (30% speed).  
* **At 60°C**: Fan increases to medium speed (50% speed).  
* **At 67.5°C**: Fan ramps up to high speed (70% speed).  
* **At 75°C and above**: Fan operates at full speed (100% speed).  

This temperature-to-speed control includes a 5°C hysteresis to prevent frequent speed changes. For instance, the fan will reduce its speed only after the temperature drops 5°C below each threshold.  

The following commands allow users to monitor the PWM fan's operation:  

To check the fan's current state:  

.. code-block:: shell

  cat /sys/class/thermal/cooling_device0/cur_state

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

