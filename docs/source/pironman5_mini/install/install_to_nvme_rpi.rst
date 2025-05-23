.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _install_to_nvme_rpi_mini:

Instalación del sistema operativo en un SSD NVMe
==========================================================
Si dispones de un SSD NVMe y un adaptador para conectarlo a tu computadora, puedes seguir este tutorial para realizar una instalación rápida.

**Componentes necesarios**

* Una computadora personal
* Un SSD NVMe
* Un adaptador NVMe a USB
* Tarjeta Micro SD y lector

.. _update_bootloader_mini:

1. Actualizar el gestor de arranque
-----------------------------------

Primero, necesitas actualizar el gestor de arranque de la Raspberry Pi 5 para que inicie desde NVMe antes que desde USB o tarjeta SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    En este paso se recomienda utilizar una tarjeta Micro SD adicional. Primero, graba el gestor de arranque en esta tarjeta y luego insértala de inmediato en la Raspberry Pi para habilitar el arranque desde un dispositivo NVMe.
    
    Como alternativa, puedes grabar el gestor de arranque directamente en tu dispositivo NVMe, insertarlo en la Raspberry Pi para cambiar el método de arranque y luego conectarlo a una computadora para instalar el sistema operativo. Una vez completada la instalación, vuelve a insertarlo en la Raspberry Pi.

#. Inserta tu tarjeta Micro SD de repuesto o SSD NVMe en tu computadora mediante un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. En la pestaña **Operating System**, desplázate y selecciona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Selecciona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Selecciona **NVMe/USB Boot** para habilitar el arranque desde NVMe antes de probar USB y luego tarjeta SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. En la opción **Storage**, selecciona el dispositivo adecuado para la instalación.

   .. note::

      Asegúrate de seleccionar el dispositivo correcto. Para evitar confusiones, desconecta cualquier otro dispositivo de almacenamiento que esté conectado.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Haz clic en **NEXT**. Si el dispositivo contiene datos, asegúrate de realizar una copia de seguridad antes de continuar. Haz clic en **Yes** si no es necesario hacer copia.

   .. image:: img/os_continue.png
      :width: 90%


#. Pronto aparecerá una notificación indicando que **NVMe/USB Boot** se ha escrito correctamente en tu dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Ahora puedes insertar tu tarjeta Micro SD o SSD NVMe en la Raspberry Pi. Al alimentarla con un adaptador tipo C, el gestor de arranque se escribirá en la EEPROM de la Raspberry Pi.

.. note::

    Luego de esto, la Raspberry Pi arrancará desde NVMe antes de intentar desde USB y tarjeta SD.
    
    Apaga la Raspberry Pi y retira la tarjeta Micro SD o el SSD NVMe.


2. Instalar el sistema operativo en el SSD NVMe
-------------------------------------------------------

Ahora puedes instalar el sistema operativo en tu SSD NVMe.


#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Selecciona **Operating System** y elige la versión recomendada del sistema operativo.

   .. image:: img/os_choose_os.png
      :width: 90%


#. En la opción **Storage**, selecciona el dispositivo de almacenamiento apropiado.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Haz clic en **NEXT** y luego en **EDIT SETTINGS** para personalizar la configuración del sistema operativo.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Define un **hostname** para tu Raspberry Pi. Este será el identificador de red del dispositivo. Puedes acceder a tu Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Username** y **Password** para la cuenta de administrador. Establecer credenciales únicas es fundamental para proteger tu Raspberry Pi, ya que no tiene contraseña por defecto.

     .. image:: img/os_set_username.png

   * Configura la red inalámbrica ingresando el **SSID** y la **Password** de tu red.

     .. note::

       Define el parámetro ``Wireless LAN country`` utilizando el código alfa-2 de dos letras `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu país.

     .. image:: img/os_set_wifi.png

   * Para conectarte de forma remota a tu Raspberry Pi, habilita SSH en la pestaña Services.

     * Para autenticación por contraseña, utiliza el nombre de usuario y la contraseña definidos en la pestaña **General**.
     * Para autenticación por clave pública, selecciona "Allow public-key authentication only". Si ya tienes una clave RSA se utilizará. Si no, haz clic en "Run SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png

   * El menú **Options** permite configurar el comportamiento de Imager al finalizar la escritura, incluyendo reproducir un sonido, expulsar el medio y activar la telemetría.

     .. image:: img/os_options.png

#. Cuando termines de ingresar la configuración personalizada del sistema operativo, haz clic en **Save** para guardarla y luego en **Yes** para aplicarla al escribir la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si el SSD NVMe contiene datos existentes, asegúrate de respaldarlos para evitar pérdidas. Si no necesitas respaldo, haz clic en **Yes** para continuar.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Cuando aparezca la ventana emergente "Write Successful", la imagen se habrá escrito y verificado correctamente. ¡Ya estás listo para arrancar tu Raspberry Pi desde el SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%