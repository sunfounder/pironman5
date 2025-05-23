.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo especializado.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para perfeccionar tus habilidades.
    - **Avances exclusivos**: Sé de los primeros en conocer nuestros nuevos lanzamientos y novedades.
    - **Descuentos especiales**: Accede a promociones exclusivas en nuestros productos más recientes.
    - **Sorteos y promociones festivas**: Participa en sorteos y promociones durante celebraciones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_install_os_sd_rpi:

Instalación del sistema operativo en una tarjeta Micro SD
==============================================================
Si estás utilizando una tarjeta Micro SD, puedes seguir el siguiente tutorial para instalar el sistema en ella.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Componentes necesarios**

* Un ordenador personal
* Una tarjeta Micro SD y un lector

**Pasos**

#. Inserta tu tarjeta SD en el ordenador o portátil utilizando un lector.

#. Dentro de |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Selecciona **Operating System** y elige la versión del sistema operativo recomendada.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Haz clic en **Choose Storage** y selecciona el dispositivo de almacenamiento adecuado para la instalación.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Haz clic en **NEXT** y luego en **EDIT SETTINGS** para personalizar la configuración del sistema operativo.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Define un **hostname** para tu Raspberry Pi. Este será el identificador de red de tu dispositivo. Podrás acceder a tu Raspberry Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png


   * Crea un **Username** y una **Password** para la cuenta de administrador. Establecer credenciales únicas es fundamental para la seguridad, ya que el dispositivo no tiene una contraseña predeterminada.

     .. image:: img/os_set_username.png

   * Configura la red inalámbrica ingresando el **SSID** de tu red y la **Password** correspondiente.

     .. note::

       Establece el valor de ``Wireless LAN country`` según el `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

     .. image:: img/os_set_wifi.png


   * Para conectarte remotamente a tu Raspberry Pi, habilita SSH en la pestaña de Servicios.

     * Para **autenticación por contraseña**, utiliza el nombre de usuario y contraseña configurados en la pestaña General.
     * Para autenticación mediante clave pública, selecciona "Allow public-key authentication only". Si ya tienes una clave RSA, se usará. Si no, haz clic en "Run SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png

   * El menú **Options** te permite definir el comportamiento del Imager durante el proceso de escritura, como reproducir un sonido al finalizar, expulsar el medio automáticamente y habilitar la telemetría.

     .. image:: img/os_options.png

#. Una vez que hayas completado la configuración personalizada del sistema operativo, haz clic en **Save** para guardarla. Luego, haz clic en **Yes** para aplicarla durante la escritura de la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si la tarjeta SD contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar pérdidas. Si no es necesario, haz clic en **Yes** para continuar.

   .. image:: img/os_continue.png
      :width: 90%


#. Cuando aparezca el mensaje "Write Successful", la imagen se habrá escrito y verificado correctamente. ¡Ya estás listo para iniciar tu Raspberry Pi desde la tarjeta Micro SD!

   .. image:: img/os_finish.png
      :width: 90%
