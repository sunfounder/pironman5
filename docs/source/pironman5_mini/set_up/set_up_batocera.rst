.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_batocera_mini:

Configuración en Batocera.linux
=========================================================

Si ya has instalado el sistema operativo Batocera.linux, puedes iniciar sesión de forma remota a través de SSH y seguir los pasos a continuación para completar la configuración.

#. Una vez que el sistema haya arrancado, utiliza SSH para conectarte remotamente a Pironman5. En Windows, puedes abrir **Powershell**, y en Mac OS X o Linux, abre directamente la **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. El nombre de host predeterminado del sistema Batocera es ``batocera``, con el nombre de usuario ``root`` y la contraseña ``linux``. Por lo tanto, puedes iniciar sesión escribiendo ``ssh root@batocera.local`` e introduciendo la contraseña ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Ejecuta el comando: ``/etc/init.d/S92switch setup`` para acceder al menú de configuración.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Usa la tecla de flecha hacia abajo para ir al final, selecciona y activa los servicios **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Tras activar el servicio pironman5, selecciona **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Ejecuta el comando ``reboot`` para reiniciar Pironman5.

   .. code-block:: shell

      reboot

#. Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente. Aquí están las configuraciones principales para Pironman 5:
   
   * Los cuatro LED RGB WS2812 se encenderán en azul con efecto de respiración.
   * Los ventiladores RGB están configurados por defecto en el modo **Balanced**. Para diferentes temperaturas de activación, consulta :ref:`cc_control_fan_mini`.

Ahora puedes conectar el Pironman 5 a una pantalla, mandos de juego, auriculares y más para sumergirte en tu mundo de juegos.


.. note::

   En este punto, ha configurado correctamente el Pironman 5 Mini y está listo para usar.
   
   Para un control avanzado de sus componentes, consulte :ref:`view_control_commands_mini`.
