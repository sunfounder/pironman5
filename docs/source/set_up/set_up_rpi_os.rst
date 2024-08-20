.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _set_up_pironman5:

Configuración en Raspberry Pi/Ubuntu/Kali/Homebridge OS
==========================================================

Si has instalado Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge en tu Raspberry Pi, necesitarás configurar el Pironman 5 usando la línea de comandos. Puedes encontrar tutoriales detallados a continuación:

.. note::

  Antes de configurar, debes encender e iniciar sesión en tu Raspberry Pi. Si no estás seguro de cómo hacerlo, puedes visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.


Configurar el apagado para desactivar la alimentación GPIO
-------------------------------------------------------------
Para evitar que la pantalla OLED y los ventiladores RGB, alimentados por el GPIO de Raspberry Pi, sigan activos después del apagado, es fundamental configurar Raspberry Pi para desactivar la alimentación del GPIO.

#. Edita manualmente el archivo de configuración del ``EEPROM`` con este comando:

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. Modifica la configuración ``POWER_OFF_ON_HALT`` en el archivo a ``1``. Por ejemplo:

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Presiona ``Ctrl + X``, ``Y`` y ``Enter`` para guardar los cambios.


Descargar e instalar el módulo ``pironman5``
-----------------------------------------------

#. Para sistemas lite, primero instala herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

   .. code-block:: shell
   
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procede a descargar el código desde GitHub e instalar el módulo ``pironman5``.

   .. code-block:: shell

     cd ~
     git clone https://github.com/sunfounder/pironman5.git
     cd ~/pironman5
     sudo python3 install.py

   .. note::
    
      Una vez que hayas completado la instalación del módulo ``pironman5``, podrás acceder al :ref:`view_control_dashboard`.
      
      Si no necesitas esta función y quieres reducir el uso de CPU y RAM, puedes deshabilitar el tablero durante la instalación de ``pironman5`` añadiendo la opción ``--disable-dashboard``.

      .. code-block:: shell
      
        sudo python3 install.py --disable-dashboard
      
      Si ya has instalado ``pironman5``, puedes eliminar el módulo ``dashboard`` y ``influxdb``, luego reinicia ``pironman5`` para aplicar los cambios:

      .. code-block:: shell
      
        /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
        sudo apt purge influxdb
        sudo systemctl restart pironman5

   Tras la instalación exitosa, se requiere un reinicio del sistema para activar la instalación. Sigue el aviso de reinicio en pantalla.

   Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente. Aquí están las configuraciones principales para Pironman 5:
   
     * La pantalla OLED muestra el uso de CPU, RAM, disco, temperatura de la CPU y la dirección IP de Raspberry Pi.
     * Cuatro LEDs RGB WS2812 se encenderán en azul con un modo de respiración.
     * Los ventiladores RGB se activarán a 60°C.

#. Puedes usar la herramienta ``systemctl`` para ``iniciar``, ``detener``, ``reiniciar`` o verificar el ``estado`` del servicio ``pironman5.service``.

   .. code-block:: shell
   
      sudo systemctl restart pironman5.service

   * ``restart``: Usa este comando para aplicar cualquier cambio realizado en la configuración de ``pironman5``.
   * ``start/stop``: Habilita o deshabilita el servicio ``pironman5.service``.
   * ``status``: Verifica el estado operativo del programa ``pironman5`` usando la herramienta ``systemctl``.

