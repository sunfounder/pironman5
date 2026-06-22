.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_os_max:

Configuración en Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
==================================================================

.. image:: ../img/pironman5_max.jpg
    :width: 400
    :align: center


Si has instalado Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge en tu Raspberry Pi, deberás configurar el Pironman 5 MAX utilizando la línea de comandos.

.. note::

  Antes de proceder con la configuración, debes iniciar y acceder a tu Raspberry Pi. Si no estás seguro de cómo iniciar sesión, puedes visitar el sitio oficial de Raspberry Pi: |link_rpi_get_start|.


.. _safe_shutdown_max:

1. Configurar el apagado para desactivar la alimentación GPIO
---------------------------------------------------------------

Para evitar que la pantalla OLED y los ventiladores GPIO, alimentados por el GPIO de la Raspberry Pi, permanezcan activos después del apagado, es fundamental configurar la Raspberry Pi para desactivar la alimentación GPIO.

#. Abre la herramienta de configuración EEPROM:

   .. code-block::

      sudo raspi-config

#. Navega a **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Selecciona **B1 Full Power Off...**.

   .. image:: img/run_power_off.png

#. Guarda los cambios. Se te pedirá reiniciar para que la nueva configuración surta efecto.


.. _install_pironman5_module_max:

2. Instalando el módulo ``pironman5``
-----------------------------------------------------------

.. note::

   Para sistemas Raspberry Pi OS Lite, primero instala las herramientas necesarias como ``git`` y ``python3``.

   .. code-block:: shell

      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Descarga e instala el módulo ``pironman5`` desde GitHub.

   .. tip::

      Si estás usando **Ubuntu**, instala ``curl`` primero:

      .. code-block:: shell

         sudo apt install curl -y

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

   .. note::

      Si usas la serie Pironman 5 junto con PiPower 5, ejecuta el siguiente comando en su lugar:

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

#. Una vez completada la instalación, reinicia la Raspberry Pi cuando se te solicite. El primer inicio puede tardar hasta 30 segundos mientras se inicializan los servicios.

#. Después de que el Pironman 5 MAX se inicie correctamente, verifica que los siguientes componentes funcionen correctamente.

   * **Pantalla OLED**

     * Muestra el uso de CPU, uso de RAM, temperatura de CPU y dirección IP.
     * Se apaga automáticamente después de 10 segundos.
     * Presiona brevemente el botón de encendido para activar la pantalla o cambiar de página.

   * **Botón de encendido**

     * Pulsación breve: Encender / activar OLED / cambiar página OLED.
     * Mantener 2 segundos: Apagado seguro (requiere :ref:`safe_shutdown_max`).
     * Mantener 5 segundos: Apagado forzado.

   * **LEDs RGB WS2812**

     * Se iluminan en azul con efecto de respiración.

   * **Dos ventiladores GPIO**

     * Configurados en modo **Always On** de forma predeterminada.
     * El modo de funcionamiento se puede cambiar mediante comandos o el Panel de Control.

   * **Ventilador de la CPU (Ventilador del disipador en torre)**

     * Ajusta automáticamente la velocidad según la temperatura de la CPU.
     * Curva de ventilación predeterminada:

       * < 50°C: Apagado (0%)
       * 50°C+: Baja (30%)
       * 60°C+: Media (50%)
       * 67.5°C+: Alta (70%)
       * 75°C+: Máxima velocidad (100%)

      * :ref:`faq_pwm_fan_max`

#. Usa ``systemctl`` para gestionar el servicio ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Reemplaza ``restart`` con ``start``, ``stop`` o ``status`` según sea necesario para gestionar el servicio.

.. note::

   El Pironman 5 está listo para usar.

   Para controles avanzados y funciones del panel, consulta :ref:`control_commands_dashboard_max`.
