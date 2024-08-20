.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _view_control_dashboard:

Ver y Controlar desde el Panel de Control
============================================

Una vez que hayas instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente al reiniciar el sistema.

Ahora puedes abrir la página de monitoreo en tu navegador para ver la información sobre tu Raspberry Pi, configurar los LEDs RGB, controlar el ventilador, etc. El enlace de la página es: ``http://<ip>:34001``.

Esta página tiene las pestañas **Panel de Control**, **Historial**, **Registro** y una página de **Configuración**.

.. image:: img/dashboard_tab.png
  :width: 90%
  
  
Panel de Control
-----------------------

Hay varias tarjetas para ver el estado relevante de la Raspberry Pi, incluyendo:

* **Ventilador**: Muestra la temperatura de la CPU de la Raspberry Pi y la velocidad del ventilador PWM. El **Estado del Ventilador GPIO** indica el estado de los dos ventiladores RGB laterales. A la temperatura actual, los dos ventiladores RGB están apagados.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Almacenamiento**: Muestra la capacidad de almacenamiento de la Raspberry Pi, mostrando varias particiones de disco con su espacio utilizado y disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Memoria**: Muestra el uso de la RAM de la Raspberry Pi y su porcentaje.

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Red**: Muestra el tipo de conexión de red actual, así como las velocidades de carga y descarga.

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Procesador**: Ilustra el rendimiento de la CPU de la Raspberry Pi, incluyendo el estado de sus cuatro núcleos, frecuencias de operación y porcentaje de uso de la CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

Historial
--------------

La página de Historial te permite ver datos históricos. Marca los datos que deseas ver en la barra lateral izquierda, luego selecciona el rango de tiempo para ver los datos de ese período, y también puedes hacer clic para descargarlos.

.. image:: img/dashboard_history.png
  :width: 90%
  

Registro
------------

La página de Registro se utiliza para ver los registros del servicio Pironman5 que se está ejecutando actualmente. El servicio Pironman5 incluye varios subservicios, cada uno con su propio registro. Selecciona el registro que deseas ver, y podrás ver los datos del registro en el lado derecho. Si está en blanco, puede significar que no hay contenido de registro.

* Cada registro tiene un tamaño fijo de 10MB. Cuando excede este tamaño, se creará un segundo registro.
* El número de registros para el mismo servicio está limitado a 10. Si se excede este límite, el registro más antiguo se eliminará automáticamente.
* Hay herramientas de filtro en la parte superior del área de registro en el lado derecho. Puedes seleccionar el nivel del registro, filtrar por palabras clave y usar varias herramientas convenientes, como **Ajuste de Línea**, **Desplazamiento Automático** y **Actualización Automática**.
* Los registros también se pueden descargar localmente.

.. image:: img/dashboard_log.png
  :width: 90%
  

Configuración
-----------------

Hay un menú de configuración en la esquina superior derecha de la página. 

.. note::
    
    Después de modificar, debes hacer clic en el botón **GUARDAR** en la parte inferior para guardar los cambios.

.. image:: img/dashboard_settings.png
  :width: 90%
  

* **Modo Oscuro**: Alterna entre temas de modo claro y oscuro. La opción del tema se guarda en la caché del navegador. Cambiar de navegador o limpiar la caché restaurará el tema claro predeterminado.
* **Unidad de Temperatura**: Configura la unidad de temperatura que mostrará el sistema.
* **Modo del Ventilador**: Puedes configurar el modo de funcionamiento de los dos ventiladores RGB. Estos modos determinan las condiciones bajo las cuales se activarán los ventiladores RGB.

    * **Silencioso**: Los ventiladores RGB se activarán a 70°C.
    * **Equilibrado**: Los ventiladores RGB se activarán a 67.5°C.
    * **Fresco**: Los ventiladores RGB se activarán a 60°C.
    * **Rendimiento**: Los ventiladores RGB se activarán a 50°C.
    * **Siempre Encendido**: Los ventiladores RGB estarán siempre encendidos.

    Por ejemplo, si se configura en modo **Rendimiento**, los ventiladores RGB se activarán a 50°C.

    Después de guardar, si la temperatura de la CPU supera los 50°C, verás que el **Estado del Ventilador GPIO** cambia a ENCENDIDO en el Panel de Control, y los ventiladores RGB laterales comenzarán a girar.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300
    

* **Brillo RGB**: Puedes ajustar el brillo de los LEDs RGB con un control deslizante.
* **Color RGB**: Configura el color de los LEDs RGB.
* **Estilo RGB**: Elige el modo de visualización de los LEDs RGB. Las opciones incluyen **Sólido**, **Respiración**, **Flujo**, **Flujo Inverso**, **Arcoíris**, **Arcoíris Inverso** y **Ciclo de Matiz**.

.. note::

  Si configuras el **Estilo RGB** en **Arcoíris**, **Arcoíris Inverso** o **Ciclo de Matiz**, no podrás configurar el color.


* **Velocidad RGB**: Configura la velocidad de los cambios en los LEDs RGB.
