.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _view_control_dashboard:

Ver y Controlar desde el Panel
=========================================

Una vez que hayas instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente al reiniciar.

Ahora puedes abrir la página de monitoreo en tu navegador para ver la información de tu Raspberry Pi, configurar los RGB y controlar los ventiladores, etc. El enlace de la página es: ``http://<ip>:34001``.

Esta página tiene páginas de **Dashboard**, **History**, **Log** y **Settings**.

.. image:: img/dashboard_home.png


Dashboard
-----------------------

Hay múltiples tarjetas para ver el estado relevante de la Raspberry Pi, incluyendo:

* **Temperature**: Muestra la temperatura de la CPU/GPU de la Raspberry Pi y la velocidad del ventilador de la CPU. **GPIO Fan State** muestra el estado de los dos ventiladores GPIO laterales.

  .. image:: img/dashboard_tem.png
    :width: 90%

* **Storage**: Muestra la capacidad de almacenamiento de la Raspberry Pi, mostrando varias particiones de disco con su espacio utilizado y disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Memory**: Muestra el uso de RAM de la Raspberry Pi y su porcentaje.

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Network**: Muestra el tipo de conexión de red actual, velocidades de subida y bajada.

  .. image:: img/dashboard_network.png
    :width: 90%


* **Processor**: Ilustra el rendimiento de la CPU de la Raspberry Pi, incluyendo el estado de sus cuatro núcleos, frecuencias de operación y porcentaje de uso de CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%


History
--------------

La página History te permite ver datos históricos. Marca los datos que deseas ver en la barra lateral izquierda, luego selecciona el rango de tiempo para ver los datos de ese período; también puedes hacer clic para descargarlos.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Log
------------

La página Log muestra el registro de ejecución del servicio Pironman5.

* Las entradas de registro se pueden filtrar por nivel (Debug, Info, Warning, Error o Critical).
* El archivo de registro también se puede descargar localmente.

.. image:: img/dashboard_log.png
  :width: 90%

Settings
------------

La página Settings te permite personalizar la visualización del Panel, las preferencias del sistema, la pantalla OLED, la iluminación RGB y el comportamiento de los ventiladores. También muestra información básica de red, como la dirección MAC y la dirección IP.

.. image:: img/dashboard_setting.png
    :width: 600


* **Interface**

  Configura la apariencia y el comportamiento de visualización del Panel.

  .. image:: img/dashboard_setting_interface.png
      :width: 600

  * **Dark mode**: Activa o desactiva el tema oscuro.
  * **Show unmounted disk**: Muestra dispositivos de almacenamiento no montados en la tarjeta Storage.
  * **Show all cores**: Muestra todos los núcleos de CPU en la tarjeta Processor.
  * **Card layout**: Personaliza el diseño de las tarjetas del Panel.
  * **Temperature Unit**: Cambia entre Celsius y Fahrenheit.
  * **Web UI Version**: Muestra la versión actual del Panel.


* **OLED**

  Configura la pantalla OLED y su comportamiento.

  .. image:: img/dashboard_setting_oled.png
      :width: 600

  * **OLED Enable**: Activa o desactiva la pantalla OLED.
  * **OLED Rotation**: Rota la pantalla OLED entre ``0°`` y ``180°``.
  * **OLED Sleep Timeout**: Establece cuánto tiempo permanece encendida la pantalla OLED antes de apagarse automáticamente.
  * **OLED Pages**: Configura qué páginas se muestran en la pantalla OLED y ajusta su orden de visualización.

    Las páginas disponibles incluyen:

    * **IP Addresses**: Muestra las direcciones IP de todas las interfaces de red físicas.
    * **Disk Usage**: Muestra información de uso de disco para todos los discos.
    * **Performance Metrics**: Muestra el uso de CPU, temperatura de CPU, uso de RAM y velocidad del ventilador.
    * **System Mix**: Muestra el uso de CPU, temperatura de CPU y dirección IP.


* **RGB**

  Configura los efectos de iluminación LED RGB y su comportamiento.

  .. image:: img/dashboard_setting_rgb.png
      :width: 600

  * **RGB Enable**: Activa o desactiva los LEDs RGB.
  * **RGB Color**: Establece el color de los LEDs RGB.
  * **RGB Brightness**: Ajusta el brillo de los LEDs RGB.
  * **RGB Style**: Selecciona el efecto de iluminación RGB, incluyendo ``None``, ``Solid``, ``Breathing``, ``Flow``, ``Flow Reverse``, ``Rainbow``, ``Rainbow Reverse`` y ``Hue Cycle``.
  * **RGB Speed**: Ajusta la velocidad de animación del efecto RGB seleccionado.
  * **RGB Led**: Establece el número de LEDs RGB activos.


* **GPIO Fans**

  Configura el modo de funcionamiento y el comportamiento de los LEDs de los dos ventiladores GPIO.

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  * **Fan LED**

    Controla el comportamiento de la iluminación RGB de los ventiladores GPIO.

    * **ON**: Los LEDs de los ventiladores permanecen siempre encendidos.
    * **OFF**: Los LEDs de los ventiladores permanecen apagados.
    * **FOLLOW**: Los LEDs de los ventiladores siguen los efectos de iluminación RGB del sistema.

  * **GPIO Fan Mode**

    El modo seleccionado determina cuándo se activarán los ventiladores GPIO.

    * **Quiet**: Los ventiladores GPIO se activan a 70°C.
    * **Balanced**: Los ventiladores GPIO se activan a 67.5°C.
    * **Cool**: Los ventiladores GPIO se activan a 60°C.
    * **Performance**: Los ventiladores GPIO se activan a 50°C.
    * **Always On**: Los ventiladores GPIO permanecen siempre activos.


* **System**

  Configura el comportamiento del sistema y ve la información del dispositivo.

  .. image:: img/dashboard_setting_system.png
      :width: 600

  * **Debug Level**: Establece el nivel de registro del servicio Pironman 5.
  * **Mac Address**: Muestra las direcciones MAC de las interfaces de red de la Raspberry Pi.
  * **IP Address**: Muestra las direcciones IP de las interfaces de red de la Raspberry Pi.
  * **History Retention**: Establece cuántos días se almacenarán los datos históricos.
  * **Clear All Data**: Borra todos los datos históricos registrados.
  * **Reboot**: Reinicia la Raspberry Pi de forma remota desde el Panel.
  * **Shutdown**: Apaga la Raspberry Pi de forma segura y remota desde el Panel.
