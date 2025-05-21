.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Expansor IO
================

LED RGB
------------

.. image:: img/io_board_rgb.png

La placa incluye 4 LEDs RGB WS2812, que ofrecen un control personalizable. Los usuarios pueden encenderlos o apagarlos, cambiar el color, ajustar el brillo, alternar los modos de visualización y establecer la velocidad de los cambios.

* Para modificar el estado de encendido y apagado de los LED RGB, usa ``true`` para encenderlos y ``false`` para apagarlos.

.. code-block:: shell

  pironman5 -re true

* Para cambiar su color, ingresa los valores hexadecimales del color deseado, como ``fe1a1a``.

.. code-block:: shell

  pironman5 -rc fe1a1a

* Para ajustar el brillo de los LED RGB (rango: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rb 100

* Para alternar los modos de visualización de los LED RGB, elige entre las opciones: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Si configuras el modo de visualización de los LED RGB en ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, no podrás establecer el color usando ``pironman5 -rc``.

.. code-block:: shell

  pironman5 -rs breathing

* Para modificar la velocidad de los cambios (rango: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rp 80

Pin de control RGB
-------------------------

Los LED RGB son controlados por SPI y están conectados a GPIO10, que también es el pin SPI MOSI. Los dos pines encima de J9 se utilizan para conectar los LED RGB a GPIO10. Si no se necesitan, se puede quitar el puente.

  .. image:: img/io_board_rgb_pin.png

Pines RGB OUT
-------------------------

.. image:: img/io_board_rgb_out.png

Los LEDs RGB WS2812 admiten conexión en serie, lo que permite conectar una tira LED RGB externa. Conecta el pin **SIG** al pin **DIN** de la tira externa para la expansión.

El ajuste predeterminado incluye 4 LEDs RGB. Conecta LEDs adicionales y actualiza el conteo usando:

.. code-block:: shell

  pironman5 -rl 12


Conector de pantalla OLED
----------------------------

El conector de la pantalla OLED, con una dirección de 0x3C, es una característica clave.

.. image:: img/io_board_oled.png

Si la pantalla OLED no se muestra o se muestra incorrectamente, sigue estos pasos para solucionar el problema:

Verifica si el cable FPC de la pantalla OLED está correctamente conectado.

#. Utiliza el siguiente comando para ver los registros de ejecución del programa y verificar si hay mensajes de error.

    .. code-block:: shell

        cat /opt/pironman5/log

#. Alternativamente, utiliza el siguiente comando para verificar si la dirección i2c de la OLED, 0x3C, es reconocida:
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. Si los dos primeros pasos no revelan ningún problema, intenta reiniciar el servicio pironman5 para ver si eso resuelve el problema.


    .. code-block:: shell

        sudo systemctl restart pironman5.service


Receptor infrarrojo
---------------------------

.. image:: img/io_board_receiver.png

* **Modelo**: IRM-56384, operando a 38KHz.
* **Conexión**: El receptor IR se conecta a **GPIO13**.
* **D1**: Un indicador de recepción infrarroja que parpadea al detectar una señal.
* **J8**: Un pin para habilitar la función infrarroja. Por defecto, un jumper está insertado para su funcionamiento inmediato. Retira el jumper para liberar GPIO13 si el receptor IR no se está utilizando.

Para utilizar el receptor IR, verifica su conexión e instala el módulo necesario:

* Prueba la conexión:

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Instala el módulo ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Ahora, prueba el receptor IR ejecutando el siguiente comando.

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Después de ejecutar el comando, presiona un botón en el control remoto y se imprimirá el código de ese botón.


Pines del ventilador RGB
-----------------------------

La placa de expansión IO admite hasta dos ventiladores de 5V sin PWM. Ambos ventiladores son controlados juntos.

**FAN1** y **FAN2** son dos conjuntos de pines para ventiladores. Debes conectar el cable rojo del ventilador a "+", y el cable negro a "-".

.. image:: img/io_board_fan.png

Los dos pines debajo de J9 son los pines de habilitación para los ventiladores RGB. Por defecto, un jumper está insertado en estos pines, lo que permite controlar el estado de encendido y apagado de los ventiladores mediante GPIO6. Si no se desea que funcionen los ventiladores, se puede retirar el jumper para liberar GPIO6.

.. image:: img/io_board_fan_j9.png

**D2** es un indicador de señal del ventilador que se enciende cuando el ventilador está activo.

.. image:: img/io_board_fan_d2.png

Puedes utilizar un comando para configurar el modo de funcionamiento de los dos ventiladores RGB. Estos modos determinan las condiciones bajo las cuales se activarán los ventiladores RGB.

Por ejemplo, si se configura en **1: Rendimiento**, los ventiladores RGB se activarán a 50°C.

.. code-block:: shell

  pironman5 -gm 3

* **4: Silencioso**: Los ventiladores RGB se activarán a 70°C.
* **3: Equilibrado**: Los ventiladores RGB se activarán a 67.5°C.
* **2: Enfriamiento**: Los ventiladores RGB se activarán a 60°C.
* **1: Rendimiento**: Los ventiladores RGB se activarán a 50°C.
* **0: Siempre encendido**: Los ventiladores RGB estarán siempre encendidos.

Si conectas el pin de control del ventilador RGB a diferentes pines en la Raspberry Pi, puedes utilizar el siguiente comando para cambiar el número de pin.

.. code-block:: shell

  sudo pironman5 -gp 18

Pines de cabecera
----------------------

.. image:: img/io_board_pin_header.png

Dos conectores de cabecera en ángulo recto extienden el GPIO de la Raspberry Pi, pero ten en cuenta que el receptor IR, el LED RGB y el ventilador ocupan algunos pines. Retira los jumpers correspondientes para utilizar estos pines para otras funciones.

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5
    - Raspberry Pi 5
  * - Receptor IR (Opcional)
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - Ventilador (Opcional)
    - GPIO6
  * - RGB (Opcional)
    - GPIO10
  * - RGB (Opcional)
    - GPIO12
  * - RGB (Opcional)
    - GPIO21

