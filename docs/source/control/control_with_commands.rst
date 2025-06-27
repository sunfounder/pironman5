.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _view_control_commands:

Control con Comandos
========================================
Además de visualizar datos del Pironman 5 y controlar varios dispositivos a través del Panel de Control, también puedes utilizar comandos para controlarlos.

.. note::

  * Para el sistema **Home Assistant**, solo puedes monitorear y controlar el Pironman 5 a través del panel de control abriendo la página web en ``http://<ip>:34001``.
  * Para el sistema **Batocera.linux**, solo puedes monitorear y controlar el Pironman 5 mediante comandos. Es importante tener en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio utilizando ``pironman5 restart`` para que los cambios surtan efecto.


Ver las Configuraciones Básicas
-----------------------------------

El módulo ``pironman5`` ofrece configuraciones básicas para Pironman, las cuales puedes revisar con el siguiente comando.

.. code-block:: shell

  sudo pironman5 -c

Las configuraciones estándar aparecen de la siguiente manera:

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

Personaliza estas configuraciones para adaptarlas a tus necesidades.

Utiliza ``pironman5`` o ``pironman5 -h`` para obtener instrucciones.
 
.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]     
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-od [OLED_DISK]]
                          [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]] [-os [OLED_SLEEP_TIMEOUT]]
                          [{start,restart,stop}]

  Pironman 5 command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                          Debug level
    --background [BACKGROUND]
                          Run in background
    -rd, --remove-dashboard
                          Remove dashboard
    -cp [CONFIG_PATH], --config-path [CONFIG_PATH]
                          Config path
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                          RGB style
    -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                          GPIO fan LED state on/off/follow
    -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                          GPIO fan LED pin
    -oe [OLED_ENABLE], --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -od [OLED_DISK], --oled-disk [OLED_DISK]
                          Set to display which disk on OLED. 'total' or the name of the disk, like mmbclk or nvme
    -oi [OLED_NETWORK_INTERFACE], --oled-network-interface [OLED_NETWORK_INTERFACE]
                          Set to display which ip of network interface on OLED, 'all' or the interface name, like eth0 or      
                          wlan0
    -or [{0,180}], --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -os [OLED_SLEEP_TIMEOUT], --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds



.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, necesitas usar el siguiente comando para que los cambios en la configuración surtan efecto.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verifica el estado del programa ``pironman5`` usando la herramienta ``systemctl``.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternativamente, inspecciona los archivos de registro generados por el programa.

  .. code-block:: shell

    cat /opt/pironman5/log


Control de LEDs RGB
-----------------------
La placa cuenta con 4 LEDs RGB WS2812, ofreciendo un control personalizable. Los usuarios pueden encenderlos o apagarlos, cambiar el color, ajustar el brillo, cambiar los modos de visualización de los LEDs RGB y establecer la velocidad de los cambios.

.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, necesitas usar el siguiente comando para que los cambios en la configuración surtan efecto.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Para modificar el estado de encendido y apagado de los LEDs RGB, usa ``true`` para encenderlos y ``false`` para apagarlos.

.. code-block:: shell

  sudo pironman5 -re true

* Para cambiar su color, introduce los valores hexadecimales del color deseado, como ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Para cambiar el brillo de los LEDs RGB (rango: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* Para cambiar los modos de visualización de los LEDs RGB, elige entre las opciones: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Si configuras el modo de visualización de los LEDs RGB en ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, no podrás configurar el color usando ``pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Para modificar la velocidad de los cambios (rango: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rp 80

* La configuración predeterminada incluye 4 LEDs RGB. Conecta LEDs adicionales y actualiza la cantidad usando:

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan:

Control de Ventiladores RGB
--------------------------------
La placa de expansión IO admite hasta dos ventiladores de 5V sin PWM. Ambos ventiladores se controlan juntos. 

.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, necesitas usar el siguiente comando para que los cambios en la configuración surtan efecto.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Puedes usar comandos para configurar el modo de funcionamiento de los dos ventiladores RGB. Estos modos determinan las condiciones bajo las cuales los ventiladores RGB se activarán. 

Por ejemplo, si está configurado en modo **1: Rendimiento**, los ventiladores RGB se activarán a 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Silencioso**: Los ventiladores RGB se activarán a 70°C.
* **3: Equilibrado**: Los ventiladores RGB se activarán a 67.5°C.
* **2: Fresco**: Los ventiladores RGB se activarán a 60°C.
* **1: Rendimiento**: Los ventiladores RGB se activarán a 50°C.
* **0: Siempre Encendido**: Los ventiladores RGB estarán siempre encendidos.

* Si conectas el pin de control del ventilador RGB a diferentes pines en la Raspberry Pi, puedes usar el siguiente comando para cambiar el número de pin.

.. code-block:: shell

  sudo pironman5 -gp 18


Verificar la Pantalla OLED
-----------------------------------

Cuando hayas instalado la biblioteca ``pironman5``, la pantalla OLED muestra la CPU, RAM, Uso de Disco, Temperatura de la CPU y la Dirección IP de la Raspberry Pi, y lo muestra cada vez que reinicias.

Si tu pantalla OLED no muestra ningún contenido, primero debes verificar si el cable FPC de la OLED está conectado correctamente.

Luego, puedes revisar el registro del programa para ver cuál podría ser el problema usando el siguiente comando.

.. code-block:: shell

  cat /var/log/pironman5/

O verifica si la dirección i2c de la OLED 0x3C es reconocida:

.. code-block:: shell

  i2cdetect -y 1

Verificar el Receptor Infrarrojo
---------------------------------------


* Instala el módulo ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Ahora, prueba el receptor IR ejecutando el siguiente comando.

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Después de ejecutar el comando, presiona un botón en el control remoto y se imprimirá el código de ese botón.

