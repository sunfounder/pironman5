.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _view_control_commands_mini:

Control mediante comandos
========================================

Además de visualizar datos del Pironman 5 Mini y controlar distintos dispositivos desde el panel web, también puedes utilizar comandos para gestionarlos.

.. note::

  * En el sistema **Home Assistant**, solo podrás monitorear y controlar el Pironman 5 Mini desde el panel web, accediendo a ``http://<ip>:34001``.
  * Ten en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio con ``pironman5 restart`` para que surta efecto.

Ver configuraciones básicas
-----------------------------------

El módulo ``pironman5`` ofrece configuraciones básicas del sistema que puedes consultar con el siguiente comando:

.. code-block:: shell

  sudo pironman5 -c

La configuración por defecto es la siguiente:

.. code-block::

  {
      "system": {
          "rgb_color": "feff00",
          "rgb_brightness": 30,
          "rgb_style": "hue_cycle",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 12,
          "temperature_unit": "C",
          "gpio_fan_pin": 5,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "follow",
          "gpio_fan_led_pin": 6
      }
  }

Puedes personalizar estos valores según tus necesidades.

Utiliza ``pironman5`` o ``pironman5 -h`` para ver las instrucciones.

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] 
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


.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, ejecuta este comando para aplicar los cambios:

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verifica el estado del programa ``pironman5`` con ``systemctl``:

  .. code-block:: shell

    sudo systemctl status pironman5.service

* O consulta los archivos de registro generados:

  .. code-block:: shell

    ls /var/log/pironman5/
    cat /var/log/pironman5/main.log

Control de LEDs RGB
----------------------
La placa incluye 4 LEDs RGB WS2812 que pueden personalizarse completamente. Puedes encenderlos o apagarlos, cambiar su color, brillo, modo y velocidad.

.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, ejecuta este comando para aplicar los cambios:

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Encender o apagar los LEDs RGB. ``true`` los enciende, ``false`` los apaga:

.. code-block:: shell

  sudo pironman5 -re true

* Cambiar el color RGB con un valor hexadecimal, por ejemplo: ``fe1a1a``

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Cambiar el brillo (0–100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* Cambiar el estilo de visualización: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``

.. note::

  Si eliges ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, no podrás definir un color específico con ``sudo pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Ajustar la velocidad de cambio (0–100%):

.. code-block:: shell

  sudo pironman5 -rp 80

* Si conectas más de 4 LEDs, ajusta la cantidad con:

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_mini:

Control del ventilador RGB
------------------------------
La placa de expansión IO es compatible con ventiladores de 5 V sin control PWM.

.. note::

  Cada vez que modifiques el estado de ``pironman5.service``, ejecuta este comando para aplicar los cambios:

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Puedes definir el modo de funcionamiento del ventilador RGB con este comando. Cada modo determina a qué temperatura se activará:

Por ejemplo, en modo **1: Performance**, se activará a 50 °C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: Se activa a 70 °C  
* **3: Balanced**: Se activa a 67.5 °C  
* **2: Cool**: Se activa a 60 °C  
* **1: Performance**: Se activa a 50 °C  
* **0: Always On**: El ventilador siempre estará activo

* Si conectaste el ventilador a un pin distinto, cambia el número de pin con:

.. code-block:: shell

  sudo pironman5 -gp 18

**Acerca del ventilador principal**

El ventilador principal se conecta a un puerto dedicado para ventilador PWM de 4 pines en la Raspberry Pi 5. Su estrategia de control predeterminada es un sistema de regulación inteligente de velocidad de varios niveles, gestionado por el firmware, que se basa en la temperatura de la CPU. Esto significa que cuando utilizas un ventilador PWM oficial o compatible y lo conectas correctamente, el sistema ajustará automáticamente la velocidad del ventilador según los cambios en la temperatura de la CPU (comienza a funcionar por encima de los 50°C), sin necesidad de ninguna intervención manual por tu parte.