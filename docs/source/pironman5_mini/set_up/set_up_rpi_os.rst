.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas posventa y retos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede antes que nadie a los anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante celebraciones.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _set_up_pironman5_mini:

Configuración en Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

Si has instalado Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge en tu Raspberry Pi, deberás configurar el Pironman 5 Mini desde la línea de comandos. A continuación encontrarás tutoriales detallados:

.. note::

  Antes de comenzar la configuración, asegúrate de haber iniciado y accedido a tu Raspberry Pi. Si no sabes cómo hacerlo, puedes consultar el sitio oficial de Raspberry Pi: |link_rpi_get_start|.


Configuración para apagar la alimentación del GPIO al apagar el sistema
----------------------------------------------------------------------------
Para evitar que el ventilador RGB, alimentado por los pines GPIO de la Raspberry Pi, permanezca encendido después de apagar el sistema, es necesario configurar la desactivación de energía del GPIO.

#. Edita manualmente el archivo de configuración de la ``EEPROM`` con el siguiente comando:

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. Cambia el parámetro ``POWER_OFF_ON_HALT`` a ``1``. Por ejemplo:

   .. code-block:: shell

     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Pulsa ``Ctrl + X``, ``Y`` y luego ``Enter`` para guardar los cambios.


Descargar e instalar el módulo ``pironman5``
-----------------------------------------------------------

#. En sistemas Lite, instala primero herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Luego descarga el código desde GitHub e instala el módulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Después de una instalación exitosa, se requiere reiniciar el sistema para activar la instalación. Sigue la indicación en pantalla para reiniciar.

   Tras el reinicio, el ``pironman5.service`` se iniciará automáticamente. Estas son las configuraciones principales para el Pironman 5:

   * Los cuatro LEDs RGB WS2812 se encenderán en azul con un efecto de respiración.

   .. note::

     El ventilador RGB no girará a menos que la temperatura alcance los 60°C. Para conocer otros umbrales de activación, consulta :ref:`cc_control_fan_mini`.

#. Puedes usar la herramienta ``systemctl`` para ``start``, ``stop``, ``restart`` o verificar el ``status`` del servicio ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``: Usa este comando para aplicar cualquier cambio realizado en la configuración del Pironman 5 Mini.
   * ``start/stop``: Activa o detiene el servicio ``pironman5.service``.
   * ``status``: Verifica el estado operativo del programa ``pironman5`` con la herramienta ``systemctl``.


.. note::

   En este punto, ha configurado correctamente el Pironman 5 Mini y está listo para usar.
   
   Para un control avanzado de sus componentes, consulte :ref:`control_commands_dashboard_mini`.
