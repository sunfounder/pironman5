.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _view_control_dashboard:

Ver y controlar desde el panel de control
=============================================

Una vez que hayas instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente al reiniciar.

Ahora puedes abrir la página de monitoreo en tu navegador para ver la información de tu Raspberry Pi, configurar los LEDs RGB y controlar el ventilador, entre otras funciones. El enlace a la página es: ``http://<ip>:34001``.

Esta página incluye las secciones **Panel de control**, **Historial**, **Registro** y **Configuración**.

.. image:: img/dashboard_tab_new.jpg


Panel de control
--------------------

Hay varias tarjetas para ver el estado relevante del Raspberry Pi, incluyendo:

* **Ventilador**: Muestra la temperatura del CPU del Raspberry Pi y la velocidad del ventilador PWM. **Estado del GPIO del ventilador** indica el estado de los dos ventiladores RGB laterales. A la temperatura actual, los ventiladores RGB están apagados.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%

* **Almacenamiento**: Muestra la capacidad de almacenamiento del Raspberry Pi, incluyendo las particiones del disco con su espacio utilizado y disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Memoria**: Indica el uso de la RAM del Raspberry Pi y su porcentaje.

  .. image:: img/dashboard_memory.png
    :width: 90%

* **Red**: Muestra el tipo de conexión de red actual, junto con las velocidades de subida y bajada.

  .. image:: img/dashboard_network.png
    :width: 90%

* **Procesador**: Ilustra el rendimiento del CPU del Raspberry Pi, incluyendo el estado de sus cuatro núcleos, las frecuencias de operación y el porcentaje de uso del CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%


Historial
-----------

La página Historial te permite ver datos históricos. Selecciona los datos que deseas ver en la barra lateral izquierda, luego elige el rango de tiempo para ver los datos de ese período. También puedes hacer clic para descargarlos.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Registro
-----------

La página de Registro se utiliza para ver los registros del servicio Pironman5 en ejecución. El servicio Pironman5 incluye varios subservicios, cada uno con su propio registro. Selecciona el registro que deseas ver y los datos se mostrarán en el lado derecho. Si está vacío, puede significar que no hay contenido de registro.

* Cada registro tiene un tamaño fijo de 10 MB. Cuando se supera este tamaño, se crea un segundo registro.
* El número de registros para un mismo servicio está limitado a 10. Si se supera este límite, el registro más antiguo se elimina automáticamente.
* Hay herramientas de filtro sobre el área de registro en el lado derecho. Puedes seleccionar el nivel de registro, filtrar por palabras clave y usar varias herramientas prácticas como **Ajuste de línea**, **Desplazamiento automático** y **Actualización automática**.
* Los registros también pueden descargarse localmente.

.. image:: img/dashboard_log1.png
  :width: 90%

.. image:: img/dashboard_log2.png
  :width: 90%

Configuración
----------------

En la esquina superior derecha de la página hay un menú de configuración donde puedes personalizar las opciones según tus preferencias. Después de realizar modificaciones, los cambios se guardan automáticamente. Si es necesario, puedes hacer clic en el botón CLEAR en la parte inferior para borrar los datos históricos.

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **Modo oscuro**: Alterna entre los temas claro y oscuro. La opción de tema se guarda en la caché del navegador. Cambiar de navegador o borrar la caché restablecerá el tema predeterminado claro.
* **Unidad de temperatura**: Establece la unidad de temperatura que muestra el sistema.

**Acerca de la pantalla OLED**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **Activar OLED**: Activa o desactiva la pantalla OLED.
* **Disco OLED**: Configura el disco de la pantalla OLED.
* **Interfaz de red OLED**: 

  * **all**: Alterna entre la IP Ethernet y la IP Wi-Fi.
  * **eth0**: Muestra solo la IP Ethernet.
  * **wlan0**: Muestra solo la IP Wi-Fi.

* **Rotación OLED**: Configura el ángulo de rotación de la pantalla OLED.

**Acerca de los LEDs RGB**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **Activar RGB**: Activa o desactiva los LEDs RGB.
* **Color RGB**: Configura el color de los LEDs RGB.
* **Brillo RGB**: Ajusta el brillo de los LEDs RGB con un control deslizante.
* **Estilo RGB**: Elige el modo de visualización de los LEDs RGB. Las opciones incluyen **Estático**, **Respiración**, **Flujo**, **Flujo inverso**, **Arco iris**, **Arco iris inverso** y **Ciclo de tonalidad**.

  .. note::

     Si configuras el **Estilo RGB** en **Arco iris**, **Arco iris inverso** o **Ciclo de tonalidad**, no podrás configurar el color.

* **Velocidad RGB**: Ajusta la velocidad de los cambios de color de los LEDs RGB.

**Acerca de los ventiladores RGB**

.. image:: img/RGB_fans.png
  :width: 600

* **LED del ventilador**: Configura el LED del ventilador en ON, OFF o MODO SEGUIMIENTO.
* **Modo del ventilador**: Configura el modo de funcionamiento de los dos ventiladores RGB. Estos modos determinan las condiciones bajo las cuales los ventiladores RGB se activan.

    * **Silencioso**: Los ventiladores RGB se activan a 70°C.
    * **Equilibrado**: Los ventiladores RGB se activan a 67.5°C.
    * **Fresco**: Los ventiladores RGB se activan a 60°C.
    * **Rendimiento**: Los ventiladores RGB se activan a 50°C.
    * **Siempre encendido**: Los ventiladores RGB están siempre activos.

Por ejemplo, si configuras el modo **Rendimiento**, los ventiladores RGB se activarán a 50°C.

Después de guardar, si la temperatura del CPU supera los 50°C, verás que el **Estado del GPIO del ventilador** cambia a ON en el Panel de control, y los ventiladores RGB laterales comenzarán a girar.

.. image:: img/dashboard_rgbfan_on.png
  :width: 300
