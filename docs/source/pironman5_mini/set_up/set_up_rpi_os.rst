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


.. _safe_shutdown_mini:

1. Configurar el Apagado para Desactivar la Alimentación de los GPIO
-------------------------------------------------------------------------
Para evitar que el ventilador RGB, alimentado por los GPIO de la Raspberry Pi, permanezca activo después del apagado, es esencial configurar la Raspberry Pi para desactivar la alimentación de los GPIO.

#. Abre la herramienta de configuración de la EEPROM:

   .. code-block::

      sudo raspi-config

#. Navega a **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Selecciona **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Guarda los cambios. Se te pedirá que reinicies para que la nueva configuración surta efecto.

.. _install_pironman5_module_mini:

2. Instalación del módulo ``pironman5``
----------------------------------------------

.. .. note::

..    Para los sistemas “lite”, instala primero herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. Descarga e instala el módulo ``pironman5`` desde GitHub.

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash



   .. note::

      1. Si usas **Ubuntu**, instala ``curl`` primero: ``sudo apt install curl -y``

      2. Si usas la serie Pironman 5 junto con **PiPower 5**, ejecuta el siguiente comando en su lugar:

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --pipower5

#. Después de ejecutar el instalador, selecciona tu modelo de Pironman 5 (1~4).

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. Una vez completada la instalación, reinicia la Raspberry Pi cuando se te indique. El primer inicio puede tardar hasta 30 segundos mientras los servicios se inicializan.

   #. Después de que el Pironman 5 Mini se inicie correctamente, verifica que los siguientes componentes funcionen correctamente.

   * **Botón de encendido**

     * Pulsación breve: Encender.
     * Mantener pulsado 2 segundos: Apagado seguro (requiere :ref:`safe_shutdown_mini`).
     * Mantener pulsado 5 segundos: Apagado forzado.

   * **LEDs RGB WS2812**

     * Se iluminan en azul con un efecto de respiración.

   * **Ventilador RGB**

     * Configurado por defecto en modo **Always On**.
     * El modo de funcionamiento se puede cambiar mediante comandos o el Panel de control. Consulta :ref:`cc_control_fan_mini`.

   * **Ventilador de la CPU (Ventilador del cooler activo)**

     * Ajusta automáticamente la velocidad según la temperatura de la CPU.
     * Curva de ventilador predeterminada:

       * < 50 °C: Apagado (0 %)
       * 50 °C+: Bajo (30 %)
       * 60 °C+: Medio (50 %)
       * 67.5 °C+: Alto (70 %)
       * 75 °C+: Velocidad máxima (100 %)

#. Usa ``systemctl`` para gestionar el ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Reemplaza ``restart`` con ``start``, ``stop`` o ``status`` según sea necesario para gestionar el servicio.

.. note::

   El Pironman 5 Mini ya está listo para usar.

   Para funciones avanzadas de control y panel, consulta :ref:`control_commands_dashboard_mini`.
