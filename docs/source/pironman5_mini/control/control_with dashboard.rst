.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo especializado.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _view_control_dashboard_mini:

Visualización y control desde el panel web
===============================================

Una vez instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente tras reiniciar el sistema.

Ahora puedes abrir la página de monitoreo en tu navegador para ver información sobre tu Raspberry Pi, configurar los LEDs RGB, controlar el ventilador, entre otras opciones. El enlace es: ``http://<ip>:34001``.

Esta página incluye **Dashboard**, **Historial**, **Registro** y una sección de **Configuración**.

.. image:: img/dashboard_tab.png
  :width: 90%


Panel
------------------------

Hay varias tarjetas que muestran el estado actual de la Raspberry Pi, entre ellas:

* **Fan**: Muestra la temperatura de la CPU de la Raspberry Pi y la velocidad del ventilador PWM. **GPIO Fan State** indica el estado del ventilador RGB. En la temperatura actual, el ventilador RGB está apagado.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%


* **Storage**: Muestra la capacidad de almacenamiento, con las particiones de disco, espacio usado y disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%


* **Memory**: Muestra el uso actual de la memoria RAM de la Raspberry Pi en porcentaje.

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Network**: Indica el tipo de conexión de red activa, velocidades de subida y bajada.

  .. image:: img/dashboard_network.png
    :width: 90%


* **Processor**: Visualiza el rendimiento de la CPU, incluyendo el estado de los cuatro núcleos, frecuencias de operación y porcentaje de uso.

  .. image:: img/dashboard_processor.png
    :width: 90%


Historial
--------------

En la página de historial puedes consultar datos registrados. Selecciona las métricas desde la barra lateral izquierda, define el rango de tiempo, y también puedes descargar los datos.

.. image:: img/dashboard_history.png
  :width: 90%


Registro
------------

La pestaña Registro permite visualizar los logs del servicio pironman5. Este servicio incluye múltiples subservicios, cada uno con su propio registro. Selecciona el que deseas ver y consulta la información a la derecha. Si está vacío, puede que aún no haya datos.

* Cada archivo de log tiene un tamaño fijo de 10 MB. Al superarse, se genera un nuevo archivo.
* Se almacenan hasta 10 archivos por servicio. Al superar ese número, el más antiguo se elimina.
* Sobre el área de registros encontrarás herramientas para filtrar por nivel, palabras clave y opciones como **Line Wrap**, **Auto Scroll** y **Auto Update**.
* Los registros pueden descargarse localmente.

.. image:: img/dashboard_log.png
  :width: 90%


Configuración
-----------------

Hay un menú de configuración en la parte superior derecha de la página.

.. note::

    Después de realizar cambios, recuerda hacer clic en el botón **SAVE** al final para guardar la configuración.

.. image:: img/dashboard_settings.png
  :width: 90%


* **Dark Mode**: Alterna entre temas claro y oscuro. La preferencia se guarda en la caché del navegador. Cambiar de navegador o borrar la caché restaura el tema por defecto.
* **Temperature Unit**: Define la unidad de temperatura que mostrará el sistema.
* **Fan Mode**: Establece el modo de funcionamiento del ventilador RGB. Cada modo determina a qué temperatura se activa.

    * **Quiet**: El ventilador RGB se activa a 70 °C.
    * **Balanced**: El ventilador RGB se activa a 67.5 °C.
    * **Cool**: El ventilador RGB se activa a 60 °C.
    * **Performance**: El ventilador RGB se activa a 50 °C.
    * **Always On**: El ventilador RGB permanecerá siempre encendido.

    Por ejemplo, si eliges el modo **Performance**, el ventilador se activará al alcanzar 50 °C.

    Una vez guardado, si la temperatura de la CPU supera los 50 °C, en el panel verás el **GPIO Fan State** cambiar a ON y el ventilador comenzará a girar.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300


* **RGB Brightness**: Ajusta el brillo de los LEDs RGB mediante un control deslizante.
* **RGB Color**: Define el color de los LEDs RGB.
* **RGB Style**: Elige el efecto de los LEDs RGB. Las opciones incluyen: **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse** y **Hue Cycle**.

.. note::

  Si seleccionas **Rainbow**, **Rainbow Reverse** o **Hue Cycle**, no será posible definir un color específico.


* **RGB Speed**: Ajusta la velocidad de los efectos de los LEDs RGB.