.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_pi_os:

Configuración en Raspberry Pi/Ubuntu/Kali/Homebridge OS
==========================================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Si ha instalado Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge en su Raspberry Pi, necesitará configurar el Pironman 5 Pro MAX usando la línea de comandos. Los tutoriales detallados se pueden encontrar a continuación:

.. note::

  Antes de configurar, necesita arrancar e iniciar sesión en su Raspberry Pi. Si no está seguro de cómo iniciar sesión, puede visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.

.. _safe_shutdown_promax:

1. Configuración del Apagado para Desactivar la Alimentación GPIO
-------------------------------------------------------------------------

Para evitar que la pantalla OLED y los ventiladores RGB, alimentados por el GPIO de la Raspberry Pi, permanezcan activos después del apagado, es esencial configurar la Raspberry Pi para la desactivación de la alimentación GPIO.

#. Abra la herramienta de configuración EEPROM:

   .. code-block::

      sudo raspi-config

#. Navegue a **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Seleccione **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Guarde los cambios. Se le pedirá que reinicie para que los nuevos ajustes tomen efecto.

.. _install_pironman5_module_promax:

2. Instalación del módulo ``pironman5``
----------------------------------------------

.. .. note::

..    Para sistemas lite, instala inicialmente herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

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

   #. Después de que el Pironman 5 Pro MAX se inicie correctamente, verifica que los siguientes componentes funcionen correctamente.

   * **Pantalla OLED**

     * Muestra el uso de CPU, RAM, temperatura de la CPU y dirección IP.
     * Se apaga automáticamente después de 10 segundos.
     * Presiona brevemente el botón de encendido para activar la pantalla o cambiar de página.

   * **Botón de encendido**

     * Pulsación breve: Encender / activar la pantalla OLED / cambiar página OLED.
     * Mantener pulsado 2 segundos: Apagado seguro (requiere :ref:`safe_shutdown_promax`).
     * Mantener pulsado 5 segundos: Apagado forzado.

   * **LEDs RGB WS2812**

     * Se iluminan en azul con un efecto de respiración.

   * **Ventiladores PWM**

     * Configurados por defecto en modo **Always On**.
     * El modo de funcionamiento se puede configurar mediante comandos o el panel de control.

   * **Ventilador de la CPU (Ventilador del cooler de torre)**

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

   El Pironman 5 Pro MAX ya está listo para usar.

   Para funciones avanzadas de control y panel, consulta :ref:`control_commands_dashboard_promax`.