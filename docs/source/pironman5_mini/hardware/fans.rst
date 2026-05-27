.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _fan_mini:

Ventiladores
===============

Refrigeración activa
-------------------------

El sistema de refrigeración activa del Pironman 5 Mini está controlado por el sistema operativo de la Raspberry Pi.

.. image:: img/active_cooler.png

En cuanto a soluciones térmicas para la Raspberry Pi 5, especialmente bajo cargas elevadas, el diseño del Pironman 5 Mini incorpora un sistema de enfriamiento inteligente. Este incluye un ventilador principal de refrigeración activa (Active Cooler) y un ventilador RGB auxiliar. La estrategia de enfriamiento está estrechamente integrada con el sistema de gestión térmica de la Raspberry Pi 5.

El funcionamiento del refrigerador activo se basa en la temperatura del sistema:

* Por debajo de 50 °C, el ventilador permanece apagado (velocidad 0%).
* A 50 °C, el ventilador se enciende a baja velocidad (30%).
* Al alcanzar los 60 °C, el ventilador aumenta a velocidad media (50%).
* A 67.5 °C, sube a velocidad alta (70%).
* A 75 °C o más, opera a velocidad máxima (100%).

Esta relación temperatura/velocidad también se aplica al enfriamiento, con una histéresis de 5 °C. Es decir, la velocidad del ventilador disminuye cuando la temperatura desciende 5 °C por debajo de cada umbral.

* Comandos para monitorear el estado del ventilador activo. Para verificar su estado:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Para ver la velocidad actual del ventilador:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

En el Pironman 5 Mini, el ventilador activo es un componente clave para mantener temperaturas de operación óptimas, especialmente durante tareas exigentes, garantizando un funcionamiento eficiente y confiable de la Raspberry Pi 5.

Ventilador RGB
-------------------

.. image:: img/size_fan.png

* **Dimensiones externas**: 40 × 40 × 10 mm  
* **Peso**: 13.5 ± 5 g/unidad  
* **Vida útil**: 40,000 horas (a 25 °C)  
* **Flujo de aire máximo**: 2.46 CFM  
* **Presión de aire máxima**: 0.62 mm-H2O  
* **Ruido acústico**: 22.31 dBA  
* **Potencia nominal de entrada**: 5 V / 0.1 A  
* **Velocidad nominal**: 3500 ± 10 % RPM  
* **Temperatura de operación**: -10 °C ~ +70 °C  
* **Temperatura de almacenamiento**: -30 °C ~ +85 °C  
