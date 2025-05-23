.. note:: 

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede antes que nadie a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de promociones exclusivas en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_install_to_sd_home_bridge:

Instalación del sistema operativo en una tarjeta Micro SD
==============================================================

Si estás utilizando una tarjeta Micro SD, puedes seguir el siguiente tutorial para instalar el sistema en ella.


**Componentes necesarios**

* Un ordenador personal
* Una tarjeta Micro SD y un lector

**Pasos**

#. Inserta tu tarjeta SD en el ordenador o portátil utilizando un lector.

#. Dentro de |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Haz clic en la pestaña **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta el final de la página y selecciona tu sistema operativo.

   .. note::

      * Para el sistema **Ubuntu**, haz clic en **Other general-purpose OS** -> **Ubuntu**, y selecciona **Ubuntu Desktop 24.04 LTS (64 bit)** o **Ubuntu Server 24.04 LTS (64 bit)**.
      * Para sistemas como **Kali Linux**, **Home Assistant** y **Homebridge**, haz clic en **Other specific-purpose OS** y selecciona el sistema correspondiente.

   .. image:: img/os_other_os.png
      :width: 90%

#. En la opción **Storage**, selecciona el dispositivo de almacenamiento adecuado para la instalación.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Haz clic en **NEXT**.

   .. note::

      * Para sistemas que no se pueden configurar previamente, tras hacer clic en **NEXT**, se te preguntará si deseas conservar los datos del dispositivo. Si ya realizaste una copia de seguridad, selecciona **Yes**.

      * Para sistemas donde se pueden configurar previamente el nombre de host, WiFi y habilitar SSH, aparecerá una ventana emergente preguntando si deseas aplicar la configuración personalizada del sistema operativo. Puedes elegir **Yes**, **No**, o regresar para editar.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Define un **hostname** para tu Raspberry Pi. El nombre de host es el identificador en red de tu Raspberry Pi. Puedes acceder a tu Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png  

   * Crea un **Username** y una **Password** para la cuenta de administrador de la Raspberry Pi. Establecer credenciales únicas es vital para proteger tu dispositivo, ya que no cuenta con una contraseña por defecto.

     .. image:: img/os_set_username.png

   * Configura la red inalámbrica ingresando el **SSID** y la **Password** de tu red.

     .. note::

       Establece el valor de ``Wireless LAN country`` según el `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu país.

     .. image:: img/os_set_wifi.png

   * Para conectarte remotamente a tu Raspberry Pi, habilita SSH en la pestaña de Servicios.

     * Para **autenticación por contraseña**, usa el nombre de usuario y la contraseña definidos en la pestaña General.
     * Para autenticación por clave pública, selecciona "Allow public-key authentication only". Si ya tienes una clave RSA, se usará automáticamente. Si no, haz clic en "Run SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png

   * El menú **Options** te permite configurar el comportamiento del Imager durante la escritura, como reproducir un sonido al finalizar, expulsar el medio automáticamente y habilitar la telemetría.

     .. image:: img/os_options.png

#. Una vez completada la personalización del sistema operativo, haz clic en **Save** para guardar los ajustes. Luego, haz clic en **Yes** para aplicarlos durante la escritura de la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si la tarjeta SD contiene datos previos, asegúrate de hacer una copia de seguridad para evitar pérdidas. Si no es necesario, haz clic en **Yes** para continuar.

   .. image:: img/os_continue.png
      :width: 90%


#. Cuando veas la ventana emergente "Write Successful", significa que la imagen se ha escrito y verificado correctamente. ¡Ya estás listo para iniciar tu Raspberry Pi desde la tarjeta Micro SD!
