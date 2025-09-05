.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Explora a fondo el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus conocimientos.
    - **Avances exclusivos**: Sé el primero en conocer los nuevos productos y obtener adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

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

   .. note::

     Los ventiladores RGB no girarán hasta que la temperatura alcance los 60°C. Para cambiar la temperatura de activación, consulta :ref:`max_cc_control_fan`.

Ahora puedes conectar el Pironman 5 MAX a una pantalla, controles de juego, auriculares y más, y sumergirte en tu mundo de juegos.


.. note::

   En este momento, has configurado correctamente todos los componentes del Pironman 5 MAX.  
   La configuración del Pironman 5 MAX está completa.  
   Ahora puedes usar el Pironman 5 MAX para controlar tu Raspberry Pi y otros dispositivos.  
   Para más información y uso de esta página web de Pironman 5 MAX, consulta: :ref:`max_view_control_dashboard`.
