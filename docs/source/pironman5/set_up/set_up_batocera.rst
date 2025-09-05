.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

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
   
   .. note::
    
     Los ventiladores RGB no girarán a menos que la temperatura alcance los 60°C. Para diferentes temperaturas de activación, consulta :ref:`cc_control_fan`.

Ahora, puedes conectar el Pironman 5 a una pantalla, controladores de juego, auriculares y más para sumergirte en tu mundo de videojuegos.

.. note::

   En este momento, has configurado correctamente todos los componentes del Pironman 5.  
   La configuración del Pironman 5 está completa.  
   Ahora puedes usar el Pironman 5 para controlar tu Raspberry Pi y otros dispositivos.  
   Para más información y uso de esta página web de Pironman 5, consulta: :ref:`view_control_dashboard`.
