.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_batocera:

Configuración en Batocera.linux
=========================================================

Si has instalado el sistema operativo Batocera.linux, puedes iniciar sesión remotamente en este sistema vía SSH y luego seguir los pasos a continuación para completar la configuración.

#. Una vez que el sistema se haya iniciado, utiliza SSH para conectarte remotamente a Pironman5. Para Windows, puedes abrir **Powershell**, y para Mac OS X y Linux, puedes abrir directamente **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%
      

#. El nombre de host predeterminado para el sistema Batocera es ``batocera``, con el nombre de usuario predeterminado ``root`` y la contraseña ``linux``. Por lo tanto, puedes iniciar sesión escribiendo ``ssh root@batocera.local`` y luego introduciendo la contraseña ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Ejecuta el comando: ``/etc/init.d/S92switch setup`` para acceder a la página de configuración del menú.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Usa la tecla de flecha hacia abajo para navegar hasta el final, selecciona y activa los servicios de **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Después de activar el servicio pironman5, selecciona **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Ejecuta el comando ``reboot`` para reiniciar Pironman5.

   .. code-block:: shell

      reboot

#. Tras el reinicio, el ``pironman5.service`` se iniciará automáticamente. Estas son las configuraciones principales para Pironman 5:

   * La pantalla OLED muestra el uso de CPU, RAM, disco, la temperatura de la CPU y la dirección IP de la Raspberry Pi.
   * Cuatro LED RGB WS2812 se encenderán en azul en modo respiración.
   * Los ventiladores GPIO están configurados por defecto en el modo **Balanced**. Para diferentes temperaturas de activación, consulta :ref:`cc_control_fan`.

Ahora, puedes conectar el Pironman 5 a una pantalla, controladores de juego, auriculares y más para sumergirte en tu mundo de videojuegos.

.. note::

   En este punto, ha configurado correctamente el Pironman 5 y está listo para usar.
   
   Para un control avanzado de sus componentes, consulte :ref:`view_control_commands_5`.
