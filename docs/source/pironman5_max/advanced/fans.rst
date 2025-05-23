.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza tus conocimientos sobre Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Expert Support**: Soluciona problemas postventa y desafíos técnicos con el apoyo de nuestra comunidad y equipo.
    - **Learn & Share**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Exclusive Previews**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Special Discounts**: Aprovecha descuentos especiales en nuestros productos más recientes.
    - **Festive Promotions and Giveaways**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Fans
============

Ventilador PWM
-----------------

El ventilador PWM del Pironman 5 es controlado por el sistema del Raspberry Pi.

En cuanto a las soluciones de refrigeración para el Raspberry Pi 5, especialmente bajo cargas elevadas, el diseño del Pironman 5 incorpora un sistema de enfriamiento inteligente. Cuenta con un ventilador PWM principal y dos ventiladores RGB complementarios. Esta estrategia de enfriamiento está estrechamente integrada con el sistema de gestión térmica del Raspberry Pi 5.

El funcionamiento del ventilador PWM se basa en la temperatura del Raspberry Pi 5:

* Por debajo de los 50 °C, el ventilador permanece apagado (0 % de velocidad).
* A los 50 °C, el ventilador inicia a baja velocidad (30 %).
* Al alcanzar los 60 °C, aumenta a velocidad media (50 %).
* A los 67.5 °C, sube a alta velocidad (70 %).
* A los 75 °C o más, opera a velocidad máxima (100 %).

Esta relación temperatura/velocidad también se aplica al disminuir la temperatura, con una histéresis de 5 °C. La velocidad del ventilador se reduce cuando la temperatura baja 5 °C respecto a cada uno de estos umbrales.

* Comandos para monitorear el ventilador PWM. Para comprobar su estado:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Para ver la velocidad del ventilador PWM:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

En el Pironman 5, el ventilador PWM es un componente clave para mantener temperaturas óptimas de funcionamiento, especialmente durante tareas intensivas, garantizando que el Raspberry Pi 5 opere de forma eficiente y confiable.

Ventiladores RGB
---------------------

.. image:: img/size_fan.png

* **Dimensión externa**: 40*40*10MM  
* **Peso**: 13.5±5g/unidad  
* **Vida útil**: 40,000 horas (a temperatura ambiente de 25 °C)  
* **Flujo de aire máximo**: 2.46CFM  
* **Presión de aire máxima**: 0.62mm-H2O  
* **Nivel de sonido acústico**: 22.31dBA  
* **Potencia de entrada nominal**: 5V/0.1A  
* **Velocidad nominal**: 3500±10%RPM  
* **Temperatura de funcionamiento**: -10℃~+70℃  
* **Temperatura de almacenamiento**: -30℃~+85℃  

