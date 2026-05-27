.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _max_set_up_batocera:

Configuración en Batocera.linux
=========================================================

Si ya has instalado el sistema operativo Batocera.linux, puedes iniciar sesión de forma remota mediante SSH y seguir los pasos a continuación para completar la configuración.

#. Una vez que el sistema haya iniciado, usa ssh para conectarte remotamente a Pironman5. En Windows, puedes abrir **Powershell**, y en Mac OS X o Linux, abre directamente el **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. El nombre de host predeterminado del sistema Batocera es ``batocera``, con el nombre de usuario ``root`` y la contraseña ``linux``. Por lo tanto, puedes iniciar sesión escribiendo ``ssh root@batocera.local`` y luego ingresando la contraseña ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Ejecuta el siguiente comando: ``/etc/init.d/S92switch setup`` para acceder al menú de configuración.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Usa la flecha hacia abajo para desplazarte al final del menú, selecciona y activa los servicios **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Después de activar el servicio Pironman5, selecciona **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Ejecuta el comando ``reboot`` para reiniciar Pironman5.

   .. code-block:: shell

      reboot

#. Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente. Estas son las configuraciones principales de Pironman 5 MAX:

   * La pantalla OLED mostrará el uso de CPU, RAM, disco, temperatura de la CPU y la dirección IP de la Raspberry Pi.
   * Cuatro LEDs RGB WS2812 se encenderán en color azul con efecto de respiración.
   * Los ventiladores GPIO están configurados por defecto en el modo **Balanced**. Para cambiar la temperatura de activación, consulta :ref:`cc_control_fan_max`.

Ahora puedes conectar el Pironman 5 MAX a una pantalla, controles de juego, auriculares y más, y sumergirte en tu mundo de juegos.


.. note::

   En este punto, ha configurado correctamente el Pironman 5 MAX y está listo para usar.
   
   Para un control avanzado de sus componentes, consulte :ref:`max_view_control_commands`.
