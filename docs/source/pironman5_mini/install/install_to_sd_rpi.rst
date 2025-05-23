.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros aficionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _install_os_sd_rpi_mini:

Instalación del sistema operativo en una tarjeta Micro SD
==============================================================
.. If you are using a Micro SD card, you can follow the tutorial below to install the system onto your Micro SD card.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Componentes necesarios**

* Una computadora personal
* Una tarjeta Micro SD y un lector

**Pasos**

#. Inserta tu tarjeta SD en la computadora o portátil usando un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Selecciona **Operating System** y elige la versión recomendada del sistema operativo.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Haz clic en **Choose Storage** y selecciona el dispositivo de almacenamiento adecuado para la instalación.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Haz clic en **NEXT** y luego en **EDIT SETTINGS** para personalizar la configuración del sistema operativo.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Define un **hostname** para tu Raspberry Pi. Este nombre es el identificador de red del dispositivo. Puedes acceder a tu Raspberry Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png


   * Crea un **Username** y una **Password** para la cuenta de administrador. Establecer un nombre de usuario y contraseña únicos es fundamental para proteger tu Raspberry Pi, que no tiene contraseña predeterminada.

     .. image:: img/os_set_username.png

   * Configura la red inalámbrica introduciendo el **SSID** y la **Password** de tu red.

     .. note::

       Establece el valor de ``Wireless LAN country`` con el código de dos letras según la norma `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

     .. image:: img/os_set_wifi.png


   * Para conectarte remotamente a tu Raspberry Pi, activa SSH en la pestaña de Servicios.

     * Para **autenticación con contraseña**, usa el nombre de usuario y la contraseña definidos en la pestaña General.
     * Para autenticación con clave pública, selecciona "Allow public-key authentication only". Si ya tienes una clave RSA, se usará. Si no, haz clic en "Run SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png

   * El menú **Options** te permite configurar el comportamiento de Imager durante la escritura, como reproducir sonido al finalizar, expulsar el medio automáticamente y activar la telemetría.

     .. image:: img/os_options.png

#. Cuando termines de personalizar la configuración del sistema operativo, haz clic en **Save** para guardar los ajustes. Luego haz clic en **Yes** para aplicarlos al escribir la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si la tarjeta SD contiene datos anteriores, asegúrate de hacer una copia de seguridad. Haz clic en **Yes** si no necesitas conservar los datos.

   .. image:: img/os_continue.png
      :width: 90%


#. Cuando veas el mensaje "Write Successful", la imagen habrá sido escrita y verificada con éxito. ¡Ya puedes arrancar tu Raspberry Pi desde la tarjeta Micro SD!

   .. image:: img/os_finish.png
      :width: 90%
