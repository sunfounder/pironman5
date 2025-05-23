.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios y vistas previas de nuevos productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en promociones de temporada y sorteos especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_to_sd_home_bridge_mini:

Instalación del sistema operativo en una tarjeta Micro SD
==============================================================

Si vas a utilizar una tarjeta Micro SD, puedes seguir el siguiente tutorial para instalar el sistema en ella.


**Componentes necesarios**

* Una computadora personal
* Una tarjeta Micro SD y un lector

**Pasos**

#. Inserta tu tarjeta SD en la computadora o portátil mediante un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Haz clic en la pestaña **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta el final de la página y selecciona tu sistema operativo.

   .. note::

      * Para el sistema **Ubuntu**, haz clic en **Other general-purpose OS** -> **Ubuntu**, y selecciona **Ubuntu Desktop 24.04 LTS (64 bit)** o **Ubuntu Server 24.04 LTS (64 bit)**.
      * Para **Kali Linux**, **Home Assistant** y **Homebridge**, haz clic en **Other specific-purpose OS** y selecciona el sistema correspondiente.

   .. image:: img/os_other_os.png
      :width: 90%

#. En la opción **Storage**, selecciona el dispositivo de almacenamiento adecuado para la instalación.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Haz clic en **NEXT**.

   .. note::

      * Para sistemas que no pueden configurarse por adelantado, al hacer clic en **NEXT** se te preguntará si deseas conservar los datos del dispositivo. Si ya realizaste una copia de seguridad, selecciona **Yes**.

      * Para sistemas donde se puede configurar el nombre del host, WiFi y SSH previamente, aparecerá una ventana emergente para aplicar la configuración personalizada del sistema operativo. Puedes seleccionar **Yes**, **No** o volver atrás para editar.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Define un **hostname** para tu Raspberry Pi. Este es el identificador de red del dispositivo. Puedes acceder a tu Raspberry Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Username** y una **Password** para la cuenta de administrador. Establecer credenciales únicas es fundamental para proteger tu Raspberry Pi, ya que no viene con contraseña por defecto.

     .. image:: img/os_set_username.png

   * Configura la red inalámbrica ingresando el **SSID** y la **Password** de tu red.

     .. note::

       Establece el valor de ``Wireless LAN country`` con el código de dos letras según la norma `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu país.

     .. image:: img/os_set_wifi.png

   * Para conectarte remotamente a tu Raspberry Pi, activa SSH en la pestaña de Servicios.

     * Para **autenticación por contraseña**, usa el usuario y contraseña definidos en la pestaña General.
     * Para autenticación por clave pública, selecciona "Allow public-key authentication only". Si ya tienes una clave RSA, se usará automáticamente. Si no, haz clic en "Run SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png

   * El menú **Options** permite configurar el comportamiento de Imager durante la escritura, como reproducir un sonido al finalizar, expulsar el medio y habilitar telemetría.

     .. image:: img/os_options.png

#. Una vez completada la configuración personalizada del sistema operativo, haz clic en **Save** para guardar los cambios y luego en **Yes** para aplicarlos al escribir la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si la tarjeta SD contiene datos previos, asegúrate de hacer una copia de seguridad. Haz clic en **Yes** si no es necesario conservar la información.

   .. image:: img/os_continue.png
      :width: 90%


#. Cuando veas el mensaje "Write Successful", la imagen habrá sido escrita y verificada con éxito. ¡Ya puedes arrancar tu Raspberry Pi desde la tarjeta Micro SD!
