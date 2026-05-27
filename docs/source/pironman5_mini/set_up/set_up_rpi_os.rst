.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuración en Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

.. image:: ../img/pironman5_mini_pic.jpg
    :width: 400
    :align: center

Si has instalado Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge en tu Raspberry Pi, necesitarás configurar el Pironman 5 Mini usando la línea de comandos. A continuación, puedes encontrar tutoriales detallados:

.. note::

  Antes de configurar, debes encender e iniciar sesión en tu Raspberry Pi. Si no estás seguro de cómo iniciar sesión, puedes visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.


Configurar el Apagado para Desactivar la Alimentación de los GPIO
----------------------------------------------------------------------------------
Para evitar que el ventilador RGB, alimentado por los GPIO de la Raspberry Pi, permanezca activo después del apagado, es esencial configurar la Raspberry Pi para desactivar la alimentación de los GPIO.

#. Abre la herramienta de configuración de la EEPROM:

   .. code-block::

      sudo raspi-config

#. Navega a **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Selecciona **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Guarda los cambios. Se te pedirá que reinicies para que la nueva configuración surta efecto.

.. _mini_download_pironman5_module:

Descarga e instalación del módulo ``pironman5``
-----------------------------------------------------------

.. note::

   Para los sistemas “lite”, instala primero herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procede a descargar el código desde GitHub e instalar el módulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Después de una instalación exitosa, es necesario reiniciar el sistema para activar la instalación. Sigue las indicaciones en pantalla para reiniciar.

   Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente.  
   Estas son las configuraciones principales del Pironman 5 Mini:
   
   * Cuatro LED WS2812 RGB se iluminarán de color azul con un efecto de respiración.
     
   .. note::
    
     * Los ventiladores RGB están configurados por defecto en **Always On**.  
       Para establecer diferentes temperaturas de activación, consulta :ref:`cc_control_fan_mini`.

#. Puedes usar la herramienta ``systemctl`` para ``start``, ``stop``, ``restart`` o verificar el ``status`` del servicio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa este comando para aplicar cualquier cambio en la configuración del Pironman 5 Mini.  
   * ``start/stop``: Habilita o deshabilita el servicio ``pironman5.service``.  
   * ``status``: Verifica el estado operativo del programa ``pironman5`` utilizando la herramienta ``systemctl``.

.. note::

   En este punto, has configurado correctamente el Pironman 5 Mini y está listo para su uso.  
   Para el control avanzado de sus componentes, consulta :ref:`control_commands_dashboard_mini`.
