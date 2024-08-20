.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_os_sd_rpi:

Instalación del Sistema Operativo en una Tarjeta Micro SD
==============================================================
Si estás utilizando una tarjeta Micro SD, puedes seguir el siguiente tutorial para instalar el sistema en tu tarjeta Micro SD.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Componentes Requeridos**

* Una computadora personal
* Una tarjeta Micro SD y lector

**Pasos**

#. Inserta tu tarjeta SD en tu computadora o laptop utilizando un lector.

#. Dentro del |link_rpi_imager|, haz clic en **Dispositivo Raspberry Pi** y selecciona el modelo **Raspberry Pi 5** de la lista desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Selecciona **Sistema Operativo** y elige la versión recomendada del sistema operativo.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Haz clic en **Elegir Almacenamiento** y selecciona el dispositivo de almacenamiento apropiado para la instalación.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Haz clic en **SIGUIENTE** y luego en **EDITAR CONFIGURACIÓN** para personalizar tu sistema operativo. 

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Define un **nombre de host** para tu Raspberry Pi. El nombre de host es el identificador de red de tu Raspberry Pi. Puedes acceder a tu Pi utilizando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png
   

   * Crea un **Nombre de Usuario** y una **Contraseña** para la cuenta de administrador del Raspberry Pi. Establecer un nombre de usuario y contraseña únicos es vital para asegurar tu Raspberry Pi, que carece de una contraseña predeterminada.

     .. image:: img/os_set_username.png      

   * Configura la red inalámbrica LAN proporcionando el **SSID** y la **Contraseña** de tu red.

     .. note::

       Establece el ``país de la LAN inalámbrica`` al código de dos letras  `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

     .. image:: img/os_set_wifi.png


   * Para conectarte de forma remota a tu Raspberry Pi, habilita SSH en la pestaña Servicios.

     * Para **autenticación con contraseña**, utiliza el nombre de usuario y la contraseña de la pestaña General.
     * Para autenticación con clave pública, elige "Permitir solo autenticación con clave pública". Si tienes una clave RSA, se usará. Si no, haz clic en "Ejecutar SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png

   * El menú **Opciones** te permite configurar el comportamiento de Imager durante la escritura, incluyendo reproducir sonido cuando termine, expulsar el medio cuando finalice y habilitar la telemetría.

     .. image:: img/os_options.png

#. Cuando hayas terminado de ingresar la personalización del sistema operativo, haz clic en **Guardar** para guardar tu personalización. Luego, haz clic en **Sí** para aplicarlas al escribir la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. Si la tarjeta SD contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar la pérdida de datos. Procede haciendo clic en **Sí** si no se necesita una copia de seguridad.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Cuando veas el mensaje emergente "Escritura Exitosa", tu imagen ha sido completamente escrita y verificada. ¡Ahora estás listo para iniciar un Raspberry Pi desde la tarjeta Micro SD!

   .. image:: img/os_finish.png
      :width: 90%
      
