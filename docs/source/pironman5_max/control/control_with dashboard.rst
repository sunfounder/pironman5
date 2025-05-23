
.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para potenciar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_view_control_dashboard:

Ver y controlar desde el panel
=========================================

Una vez instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente al reiniciar el sistema.

Ahora puedes abrir la página de monitoreo en tu navegador para ver la información de tu Raspberry Pi, configurar los LEDs RGB, controlar el ventilador, entre otras funciones. El enlace de la página es: ``http://<ip>:34001``.

Esta página incluye **Dashboard**, **Historial**, **Registro** y una sección de **Ajustes**.

.. image:: img/dashboard_tab.png
  :width: 90%
  

Dashboard
-----------------------

Hay varias tarjetas que muestran el estado actual del Raspberry Pi, entre ellas:

* **Fan**: Muestra la temperatura del CPU y la velocidad del ventilador PWM. **GPIO Fan State** indica el estado de los dos ventiladores RGB laterales. A la temperatura actual, los ventiladores RGB están apagados.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%


* **Storage**: Muestra la capacidad de almacenamiento del Raspberry Pi, incluyendo las particiones del disco con su espacio usado y disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%


* **Memory**: Indica el uso de RAM del Raspberry Pi y el porcentaje correspondiente.

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Network**: Muestra el tipo de conexión actual, así como las velocidades de subida y bajada.

  .. image:: img/dashboard_network.png
    :width: 90%


* **Processor**: Presenta el rendimiento del CPU del Raspberry Pi, incluyendo el estado de los cuatro núcleos, frecuencias de operación y porcentaje de uso del procesador.

  .. image:: img/dashboard_processor.png
    :width: 90%


History
--------------

La página de historial permite visualizar datos históricos. Selecciona en la barra lateral izquierda los datos que deseas consultar, elige el rango de tiempo y podrás ver la información correspondiente a ese período. También puedes descargarla con un clic.

.. image:: img/dashboard_history1.png
  :width: 90%
  
.. image:: img/dashboard_history2.png
  :width: 90%

Log
------------

La sección de registro permite visualizar los logs del servicio Pironman5 en ejecución. Este servicio cuenta con varios sub-servicios, cada uno con su propio registro. Selecciona el que deseas ver para ver los datos en el panel derecho. Si está en blanco, podría significar que no hay contenido registrado.

* Cada log tiene un tamaño fijo de 10 MB. Al superar ese tamaño, se crea un segundo archivo de log.
* El número de logs por servicio está limitado a 10. Si se excede, se eliminará automáticamente el log más antiguo.
* Sobre el área de logs hay herramientas de filtrado. Puedes seleccionar el nivel de registro, filtrar por palabras clave y usar varias funciones útiles, como **Line Wrap**, **Auto Scroll** y **Auto Update**.
* También es posible descargar los logs localmente.

.. image:: img/dashboard_log1.png
  :width: 90%
  
.. image:: img/dashboard_log2.png
  :width: 90%


Settings
-----------------

En la esquina superior derecha encontrarás el menú de ajustes, donde puedes personalizar la configuración según tus preferencias. Los cambios se guardan automáticamente. Si es necesario, puedes hacer clic en el botón CLEAR al final para borrar los datos históricos.

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **Dark Mode**: Alterna entre el modo claro y el modo oscuro. La preferencia de tema se guarda en la caché del navegador. Si cambias de navegador o borras la caché, volverá al tema claro por defecto.
* **Temperature Unit**: Define la unidad de temperatura que mostrará el sistema.

**Sobre la pantalla OLED**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **OLED Enable**: Activa o desactiva la pantalla OLED.
* **OLED Disk**: Define el disco que se mostrará en la pantalla OLED.
* **OLED Network Interface**:

  * **all**: Alterna entre mostrar la IP de Ethernet y la IP de Wi-Fi.
  * **eth0**: Muestra solo la IP de Ethernet.
  * **wlan0**: Muestra solo la IP de Wi-Fi.

* **OLED Rotation**: Ajusta la rotación de la pantalla OLED.

**Sobre los LEDs RGB**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **RGB Enable**: Activa o desactiva los LEDs RGB.
* **RGB Color**: Define el color de los LEDs RGB.
* **RGB Brightness**: Ajusta el brillo de los LEDs RGB con un control deslizante.
* **RGB Style**: Selecciona el modo de visualización de los LEDs RGB. Las opciones incluyen **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse** y **Hue Cycle**.

  .. note::

     Si eliges un estilo RGB como **Rainbow**, **Rainbow Reverse** o **Hue Cycle**, no podrás seleccionar un color específico.

* **RGB Speed**: Ajusta la velocidad del cambio de efectos de los LEDs RGB.

**Sobre los ventiladores RGB**

.. image:: img/RGB_FAN2.png
  :width: 600

* **GPIO Fan Mode**: Define el modo de funcionamiento de los dos ventiladores RGB. Cada modo establece la temperatura a la que se activan los ventiladores.

    * **Quiet**: Se activan a 70 °C.
    * **Balanced**: Se activan a 67,5 °C.
    * **Cool**: Se activan a 60 °C.
    * **Performance**: Se activan a 50 °C.
    * **Always On**: Siempre están encendidos.

Por ejemplo, si seleccionas el modo **Performance**, los ventiladores RGB se activarán a los 50 °C.

Una vez guardados los cambios, si la temperatura del CPU supera los 50 °C, verás que el **GPIO Fan State** en el panel cambia a ON y los ventiladores RGB laterales comenzarán a girar.

.. image:: img/dashboard_rgbfan_on.png
  :width: 300

