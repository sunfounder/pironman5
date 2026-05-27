.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_commands_5:

Control con Comandos
========================================
Además de visualizar datos del Pironman 5 y controlar varios dispositivos a través del Panel de Control, también puedes utilizar comandos para controlarlos.

.. note::

  * Para el sistema **Home Assistant**, solo puedes monitorear y controlar el Pironman 5 a través del panel de control abriendo la página web en ``http://<ip>:34001``.

.. * Para el sistema **Batocera.linux**, solo puedes monitorear y controlar el Pironman 5 mediante comandos. Es importante tener en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio utilizando ``pironman5 restart`` para que los cambios surtan efecto.

Ver las Configuraciones Básicas
-----------------------------------

El módulo ``pironman5`` ofrece configuraciones básicas para Pironman, las cuales puedes revisar con el siguiente comando.

.. code-block:: shell

  sudo pironman5 -c

Las configuraciones estándar aparecen de la siguiente manera:

.. code-block::

  {
      "system": {
          "data_interval": 1,
          "database_retention_days": 30,
          "temperature_unit": "C",
          "enable_history": true,
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "rgb_enable": true,
          "rgb_color": "#0a1aff",
          "rgb_brightness": 100,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_led_count": 4,
          "rgb_led_count_min": 4,
          "gpio_fan_pin": 6,
          "gpio_fan_mode": 0,
          "debug_level": "INFO"
      }
  }

Personaliza estas configuraciones para adaptarlas a tus necesidades.

Usa ``pironman5`` o ``pironman5 -h`` para ver las instrucciones.

.. code-block::


  usage: pironman5-service [-h] [-v] [-c] [-dl [{debug,info,warning,error,critical}]] [--background [BACKGROUND]] [-rd] [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-oe [OLED_ENABLE]]
                          [-od [OLED_DISK]] [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]]
                          [{start,restart,stop}]

  Pironman 5 command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Database retention days
    -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                          Debug level
    -rd, --remove-dashboard
                          Remove dashboard
    -cp, --config-path [CONFIG_PATH]
                          Config path
    -eh, --enable-history [ENABLE_HISTORY]
                          Enable history, True/true/on/On/1 or False/false/off/Off/0
    -re, --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rs, --rgb-style [RGB_STYLE]
                          RGB style: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
    -rc, --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u, --temperature-unit [{C,F}]
                          Temperature unit
    -gm, --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp, --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -oe, --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          OLED pages, split by ',': mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds

  Subcommands:
    {start,stop,launch-browser}
      start               Start Pironman5
      stop                Stop Pironman5
      launch-browser      Launch browser

.. note::

   Cada vez que modifiques el estado de ``pironman5.service``, debes reiniciar el servicio para que los cambios de configuración surtan efecto.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Verifica el estado del programa ``pironman5`` usando la herramienta ``systemctl``.

  .. code-block:: shell

     sudo systemctl status pironman5.service

* Alternativamente, inspecciona los archivos de registro generados por el programa.

  .. code-block:: shell

     cat /var/log/pironman5/pironman5.log


Control de LEDs RGB
----------------------

La placa cuenta con 4 LEDs RGB WS2812, que ofrecen un control personalizable. Los usuarios pueden encenderlos o apagarlos, cambiar el color, ajustar el brillo, cambiar los modos de visualización de los LEDs RGB y configurar la velocidad de los cambios.

.. note::

   Cada vez que modifiques el estado de ``pironman5.service``, debes reiniciar el servicio para que los cambios de configuración surtan efecto.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Para modificar el estado de encendido/apagado de los LEDs RGB, usa ``true`` para encenderlos o ``false`` para apagarlos.

  .. code-block:: shell

     sudo pironman5 -re true

* Para cambiar el color de los LEDs RGB, introduce el valor de color hexadecimal deseado, como ``fe1a1a``.

  .. code-block:: shell

     sudo pironman5 -rc fe1a1a

* Para cambiar el brillo de los LEDs RGB (rango: ``0 ~ 100``):

  .. code-block:: shell

     sudo pironman5 -rb 100

* Para cambiar los modos de visualización de los LEDs RGB, elige entre:

  ``solid`` / ``breathing`` / ``flow`` / ``flow_reverse`` / ``rainbow`` / ``rainbow_reverse`` / ``hue_cycle``

  .. note::

     Si el modo de visualización de los LEDs RGB está configurado en ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, la configuración de color usando ``pironman5 -rc`` no tendrá efecto.

  .. code-block:: shell

     sudo pironman5 -rs breathing

* Para modificar la velocidad de animación de los LEDs RGB (rango: ``0 ~ 100``):

  .. code-block:: shell

     sudo pironman5 -rp 80

* La configuración predeterminada incluye 4 LEDs RGB. Si conectas LEDs adicionales, actualiza el número de LEDs usando:

  .. code-block:: shell

     sudo pironman5 -rl 12


.. _cc_control_fan:

Control de Ventiladores GPIO
----------------------------

La placa de expansión IO admite hasta dos ventiladores de 5V (no CPU). Ambos ventiladores se controlan conjuntamente.

.. note::

   Cada vez que modifiques el estado de ``pironman5.service``, debes reiniciar el servicio para que los cambios de configuración surtan efecto.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Puedes configurar el modo de funcionamiento de los dos ventiladores GPIO mediante comandos. Estos modos determinan el umbral de temperatura al que se activarán los ventiladores GPIO.

  Por ejemplo, si se configura en modo **1: Performance**, los ventiladores GPIO se activarán a ``50°C``.

  .. code-block:: shell

     sudo pironman5 -gm 3

* **4: Quiet**: Los ventiladores GPIO se activarán a ``70°C``.
* **3: Balanced**: Los ventiladores GPIO se activarán a ``67.5°C``.
* **2: Cool**: Los ventiladores GPIO se activarán a ``60°C``.
* **1: Performance**: Los ventiladores GPIO se activarán a ``50°C``.
* **0: Always On**: Los ventiladores GPIO permanecerán siempre encendidos.

* Si conectas el pin de control del ventilador RGB a un pin GPIO diferente en la Raspberry Pi, puedes cambiar el número de pin usando:

  .. code-block:: shell

     sudo pironman5 -gp 18


Acerca del Ventilador de la CPU
--------------------------------

El ventilador de la CPU se conecta a un puerto dedicado de 4 pines para ventilador de CPU en la Raspberry Pi 5.

Su estrategia de control predeterminada es un esquema de ajuste de velocidad inteligente de múltiples niveles gestionado por firmware, basado en la temperatura de la CPU. Cuando uses un ventilador de CPU oficial o compatible y lo conectes correctamente, el sistema ajustará automáticamente la velocidad del ventilador según los cambios en la temperatura de la CPU (comenzando por encima de ``50°C``) sin necesidad de intervención manual.


Verificar la Pantalla OLED
-----------------------------------

Cuando la biblioteca ``pironman5`` está instalada, la pantalla OLED muestra el uso de CPU, uso de RAM, uso de disco, temperatura de CPU y la dirección IP de la Raspberry Pi automáticamente después de cada reinicio.

Si la pantalla OLED no muestra ningún contenido, primero verifica si el cable FPC de la OLED está conectado correctamente.

Luego inspecciona el registro del programa usando el siguiente comando:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

También puedes verificar si se detecta la dirección I2C ``0x3C`` de la OLED:

.. code-block:: shell

   i2cdetect -y 1


Verificar el Receptor Infrarrojo
---------------------------------------

* Instala el módulo ``lirc``:

  .. code-block:: shell

     sudo apt-get install lirc -y

* Prueba el receptor IR usando el siguiente comando:

  .. code-block:: shell

     mode2 -d /dev/lirc0

* Después de ejecutar el comando, presiona un botón en el control remoto. El código IR correspondiente se imprimirá en la terminal.
