.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _set_up_umbrel:

Configuración en Umbrel OS
======================================================================

Si has instalado Umbrel OS en tu Raspberry Pi 5, deberás configurar el Pironman 5 utilizando la línea de comandos. A continuación se proporcionan las instrucciones detalladas:

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
      git clone -b base https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Después de completar la instalación, introduce el siguiente comando para reiniciar tu Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente.  
   Estas son las configuraciones principales del Pironman 5:
   
   * La pantalla OLED muestra CPU, RAM, uso de disco, temperatura de la CPU y dirección IP de la Raspberry Pi.  
   * Cuatro LED WS2812 RGB se iluminarán de color azul con un efecto de respiración.  
   * Los ventiladores RGB están configurados por defecto en el modo **Always On**. Para diferentes temperaturas de activación, consulta :ref:`cc_control_fan`.

#. Puedes utilizar la herramienta ``systemctl`` para ``start``, ``stop``, ``restart`` o verificar el ``status`` del servicio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa este comando para aplicar cualquier cambio en la configuración de Pironman 5.  
   * ``start/stop``: Habilita o deshabilita el servicio ``pironman5.service``.  
   * ``status``: Verifica el estado operativo del programa ``pironman5`` utilizando la herramienta ``systemctl``.

.. note::

   En este punto, has configurado correctamente el Pironman 5 y está listo para su uso.  
   Para el control avanzado de sus componentes, consulta :ref:`control_commands_dashboard_5`.


