.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Ventiladores
===============

Ventilador PWM
----------------

El ventilador PWM del Pironman 5 está controlado por el sistema de Raspberry Pi.

En cuanto a las soluciones de refrigeración para la Raspberry Pi 5, especialmente bajo cargas intensas, el diseño del Pironman 5 incorpora un sistema de enfriamiento inteligente. Cuenta con un ventilador PWM principal y dos ventiladores RGB adicionales. La estrategia de refrigeración está estrechamente integrada con el sistema de gestión térmica de la Raspberry Pi 5.

El funcionamiento del ventilador PWM se basa en la temperatura de la Raspberry Pi 5:

* Por debajo de 50°C, el ventilador PWM permanece apagado (velocidad del 0%).
* A 50°C, el ventilador comienza a baja velocidad (30% de velocidad).
* Al llegar a 60°C, el ventilador aumenta a una velocidad media (50% de velocidad).
* A 67.5°C, el ventilador se eleva a alta velocidad (70% de velocidad).
* A 75°C o más, el ventilador funciona a máxima velocidad (100% de velocidad).

Esta relación temperatura-velocidad también se aplica cuando la temperatura disminuye, con una histéresis de 5°C. La velocidad del ventilador se reduce cuando la temperatura cae 5°C por debajo de cada uno de estos umbrales.

* Comandos para monitorear el estado del ventilador PWM. Para comprobar el estado del ventilador PWM:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Para ver la velocidad del ventilador PWM:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

En el Pironman 5, el ventilador PWM es un componente crítico para mantener temperaturas óptimas de funcionamiento, especialmente durante tareas intensivas, asegurando que la Raspberry Pi 5 funcione de manera eficiente y confiable.

Ventiladores RGB
----------------------

.. image:: img/size_fan.png

* **Dimensiones externas**: 40*40*10MM
* **Peso**: 13.5±5g/pcs
* **Duración**: 40,000 horas (temperatura ambiente 25°C)
* **Flujo de aire máximo**: 2.46CFM
* **Presión de aire máxima**: 0.62mm-H2O
* **Sonido acústico**: 22.31dBA
* **Potencia de entrada nominal**: 5V/0.1A
* **Velocidad nominal**: 3500±10%RPM
* **Temperatura de funcionamiento**: -10℃~+70℃
* **Temperatura de almacenamiento**: -30℃~+85℃

