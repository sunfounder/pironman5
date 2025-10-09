.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más a fondo en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Soluciona problemas técnicos y postventa con el apoyo de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a lanzamientos de productos y adelantos especiales.
    - **Descuentos exclusivos**: Aprovecha promociones especiales en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y eventos promocionales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_set_up_pi_os:

Configuración en Raspberry Pi/Ubuntu/Kali/Homebridge OS
==========================================================

Si has instalado Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge en tu Raspberry Pi, deberás configurar el Pironman 5 MAX desde la línea de comandos. A continuación, encontrarás los tutoriales detallados:

.. note::

  Antes de comenzar la configuración, asegúrate de haber iniciado y accedido a tu Raspberry Pi. Si no sabes cómo hacerlo, puedes visitar el sitio oficial de Raspberry Pi: |link_rpi_get_start|.


Configurar el apagado para desactivar la energía del GPIO
---------------------------------------------------------------

Para evitar que la pantalla OLED y los ventiladores RGB —alimentados a través del GPIO de la Raspberry Pi— permanezcan encendidos después del apagado, es necesario configurar la desactivación de energía del GPIO.

#. Edita manualmente el archivo de configuración de ``EEPROM`` con el siguiente comando:

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. Modifica el parámetro ``POWER_OFF_ON_HALT`` en el archivo a ``1``. Por ejemplo:

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Presiona ``Ctrl + X``, luego ``Y`` y ``Enter`` para guardar los cambios.


Descarga e instalación del módulo ``pironman5``
-----------------------------------------------------------

#. En sistemas "lite", primero instala herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
  
   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Luego, descarga el código desde GitHub e instala el módulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Una vez completada la instalación, será necesario reiniciar el sistema para activar los cambios. Sigue las instrucciones en pantalla para reiniciar.

   Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente. Estas son las configuraciones principales de Pironman 5 MAX:
   
   * La pantalla OLED muestra el uso de CPU, RAM, disco, temperatura de la CPU y la dirección IP de la Raspberry Pi.

   .. note:: La pantalla OLED puede apagarse automáticamente después de un período de inactividad para ahorrar energía. Puedes dar un toque suave a la carcasa para activar el sensor de vibración y encender la pantalla.


   * Cuatro LEDs RGB WS2812 se encenderán en azul con efecto de respiración.
     
   .. note::
    
     Los ventiladores RGB no girarán hasta que la temperatura alcance los 60 °C. Para modificar esta temperatura de activación, consulta :ref:`max_cc_control_fan`.

#. Puedes usar la herramienta ``systemctl`` para ``start``, ``stop``, ``restart`` o consultar el ``status`` de ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Aplica los cambios realizados en la configuración de Pironman 5 MAX.
   * ``start/stop``: Activa o desactiva el servicio ``pironman5.service``.
   * ``status``: Verifica el estado de funcionamiento del programa ``pironman5`` mediante la herramienta ``systemctl``.

.. note::

   En este punto, ha configurado correctamente el Pironman 5 MAX y está listo para usar.
   
   Para un control avanzado de sus componentes, consulte :ref:`control_commands_dashboard_max`.
