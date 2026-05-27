.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_umbrel_mini:

Configuración en Umbrel OS
======================================================================

Si has instalado Umbrel OS en tu Raspberry Pi 5, deberás configurar el Pironman 5 Mini utilizando la línea de comandos. A continuación se proporcionan las instrucciones detalladas:

#. Conecta tu Raspberry Pi 5 a la red mediante un cable Ethernet. Este paso es esencial para garantizar que la Raspberry Pi tenga acceso a Internet.

#. En tu navegador, visita: ``http://umbrel.local``.  
   Si la página no se abre, revisa en el enrutador la dirección IP del dispositivo Umbrel, por ejemplo: ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Crea tu cuenta de Umbrel configurando un nombre de usuario y una contraseña.  
   Esta contraseña se utilizará para futuros accesos remotos a Umbrel, así que asegúrate de recordarla.

   .. image:: img/umbrel_account.png

#. Haz clic en **Next** para completar la configuración de Umbrel y entrar al entorno de escritorio.

   .. image:: img/umbrel_desktop.png

#. Abre el Terminal. Desde el escritorio, haz clic en el ícono **Settings**, luego selecciona **Advanced Settings** y haz clic en **Open**.

   .. image:: img/umbrel_setting.png

#. Haz clic en **Open Terminal**.

   .. image:: img/umbrel_open_terminal.png

#. Puedes optar por abrir el terminal en Umbrel OS o dentro de una aplicación específica. Ambas opciones te llevarán a la interfaz del terminal.

   .. image:: img/umbrel_terminal.png

#. Procede a descargar el código desde GitHub e instalar el módulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Después de completar la instalación, introduce el siguiente comando para reiniciar tu Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente.  
   Estas son las configuraciones principales del Pironman 5 Mini:
   
   * Cuatro LED WS2812 RGB se iluminarán de color azul con un efecto de respiración.  
   * Los ventiladores RGB están configurados por defecto en el modo **Always On**. Para diferentes temperaturas de activación, consulta :ref:`cc_control_fan_mini`.

#. Puedes utilizar la herramienta ``systemctl`` para ``start``, ``stop``, ``restart`` o verificar el ``status`` del servicio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa este comando para aplicar cualquier cambio en la configuración del Pironman 5 Mini.  
   * ``start/stop``: Habilita o deshabilita el servicio ``pironman5.service``.  
   * ``status``: Verifica el estado operativo del programa ``pironman5`` utilizando la herramienta ``systemctl``.

.. note::

   En este punto, has configurado correctamente el Pironman 5 Mini y está listo para su uso.  
   Para el control avanzado de sus componentes, consulta :ref:`control_commands_dashboard_mini`.

