.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza tus conocimientos sobre Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con el respaldo de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para potenciar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos lanzamientos y adelantos de productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_view_control_commands:

Control mediante comandos
========================================
Además de visualizar datos y controlar diversos dispositivos desde el panel de control, también puedes usar comandos para gestionar el Pironman 5.

.. note::

  * En el sistema **Home Assistant**, solo puedes monitorear y controlar el Pironman 5 a través del panel accediendo a ``http://<ip>:34001``.
  * En el sistema **Batocera.linux**, solo es posible controlar y monitorear el Pironman 5 mediante comandos. Es importante tener en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio con ``pironman5 restart`` para que surta efecto.

Ver configuraciones básicas
-----------------------------------

El módulo ``pironman5`` ofrece configuraciones básicas para Pironman, que puedes consultar con el siguiente comando:

.. code-block:: shell

  pironman5 -c

Las configuraciones por defecto se muestran así:

.. code-block::

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

Personaliza estas configuraciones según tus necesidades.

Utiliza ``pironman5`` o ``pironman5 -h`` para ver las instrucciones.

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc RGB_COLOR] [-rb RGB_BRIGHTNESS] [-rs {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}] [-rp RGB_SPEED] [-re RGB_ENABLE]
                          [-rl RGB_LED_COUNT] [-u {C,F}] [-gm GPIO_FAN_MODE] [-gp GPIO_FAN_PIN]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc RGB_COLOR, --rgb-color RGB_COLOR
                          RGB color
    -rb RGB_BRIGHTNESS, --rgb-brightness RGB_BRIGHTNESS
                          RGB brightness
    -rs {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}, --rgb-style {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}
                          RGB style
    -rp RGB_SPEED, --rgb-speed RGB_SPEED
                          RGB speed
    -re RGB_ENABLE, --rgb-enable RGB_ENABLE
                          RGB enable
    -rl RGB_LED_COUNT, --rgb-led-count RGB_LED_COUNT
                          RGB LED count
    -u {C,F}, --temperature-unit {C,F}
                          Temperature unit
    -gm GPIO_FAN_MODE, --gpio-fan-mode GPIO_FAN_MODE
                          GPIO fan mode, 0-4, ['Always On', 'Performance', 'Cool', 'Balanced', 'Quiet']
    -gp GPIO_FAN_PIN, --gpio-fan-pin GPIO_FAN_PIN
                          GPIO fan pin



.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, debes ejecutar el siguiente comando para aplicar los cambios:

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verifica el estado del programa ``pironman5`` usando la herramienta ``systemctl``:

  .. code-block:: shell

    sudo systemctl status pironman5.service

* También puedes revisar los archivos de registro generados por el programa:

  .. code-block:: shell

    ls /var/log/pironman5/


Control de LEDs RGB
----------------------
La placa incluye 4 LEDs RGB WS2812 con control personalizable. Puedes encenderlos o apagarlos, cambiar el color, ajustar el brillo, elegir el modo de visualización y configurar la velocidad del efecto.

.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, debes ejecutar el siguiente comando para aplicar los cambios:

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Para encender o apagar los LEDs RGB, usa ``true`` para encenderlos, ``false`` para apagarlos:

.. code-block:: shell

  pironman5 -re true

* Para cambiar su color, introduce un valor hexadecimal, por ejemplo ``fe1a1a``:

.. code-block:: shell

  pironman5 -rc fe1a1a

* Para modificar el brillo (rango: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rb 100

* Para cambiar el modo de visualización, elige entre: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Si eliges los modos ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, no podrás cambiar el color con ``pironman5 -rc``.

.. code-block:: shell

  pironman5 -rs breathing

* Para ajustar la velocidad del efecto (rango: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rp 80

* Por defecto se incluyen 4 LEDs RGB. Si conectas más, puedes actualizar el número con:

.. code-block:: shell

  pironman5 -rl 12

.. _max_cc_control_fan:

Control de ventiladores RGB
--------------------------------
La placa de expansión IO admite hasta dos ventiladores de 5V sin PWM. Ambos ventiladores se controlan al mismo tiempo.

.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, debes ejecutar el siguiente comando para aplicar los cambios:

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Puedes configurar el modo de operación de los ventiladores RGB con comandos. Estos modos determinan a qué temperatura se activan:

Por ejemplo, si seleccionas el modo **1: Performance**, los ventiladores RGB se activarán a 50 °C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: Se activan a 70 °C  
* **3: Balanced**: Se activan a 67.5 °C  
* **2: Cool**: Se activan a 60 °C  
* **1: Performance**: Se activan a 50 °C  
* **0: Always On**: Siempre están encendidos  

* Si conectas el pin de control del ventilador RGB a un pin diferente en la Raspberry Pi, puedes cambiarlo con el siguiente comando:

.. code-block:: shell

  sudo pironman5 -gp 18


Verificar pantalla OLED
-----------------------------------

Una vez instalada la biblioteca ``pironman5``, la pantalla OLED muestra la CPU, RAM, uso del disco, temperatura del procesador e IP de la Raspberry Pi cada vez que se reinicia.

Si la pantalla OLED no muestra contenido, primero asegúrate de que el cable FPC esté bien conectado.

Luego, revisa el registro del programa para detectar posibles errores:

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

O verifica si la dirección i2c 0x3C es detectada:

.. code-block:: shell

  i2cdetect -y 1

Probar el receptor infrarrojo
---------------------------------------



* Instala el módulo ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Luego, prueba el receptor IR con el siguiente comando:

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Después de ejecutar el comando, presiona un botón del control remoto y se imprimirá el código correspondiente.

