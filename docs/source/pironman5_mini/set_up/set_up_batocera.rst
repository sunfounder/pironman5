.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

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
   
   .. note::

     El ventilador RGB no girará a menos que la temperatura alcance los 60°C. Para conocer otras temperaturas de activación, consulta :ref:`cc_control_fan_mini`.

Ahora puedes conectar el Pironman 5 a una pantalla, mandos de juego, auriculares y más para sumergirte en tu mundo de juegos.


.. note::

   En este momento, has configurado correctamente todos los componentes del Pironman 5 MAX.  
   La configuración del Pironman 5 MAX está completa.  
   Ahora puedes usar el Pironman 5 MAX para controlar tu Raspberry Pi y otros dispositivos.  
   Para más información y uso de esta página web de Pironman 5 MAX, consulta: :ref:`view_control_dashboard_mini`.
