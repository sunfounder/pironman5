.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza tus conocimientos sobre Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo especializado.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de promociones exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y actividades especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_install_to_nvme_rpi:

Instalación del sistema operativo en un SSD NVMe
=======================================================
Si estás utilizando un SSD NVMe y cuentas con un adaptador para conectarlo a tu ordenador, puedes seguir este tutorial para realizar una instalación rápida.

**Componentes necesarios**

* Un ordenador personal
* Un SSD NVMe
* Un adaptador de NVMe a USB
* Tarjeta Micro SD y lector

.. _update_bootloader_max:

1. Actualizar el Bootloader
--------------------------------

Primero debes actualizar el bootloader de la Raspberry Pi 5 para que arranque desde NVMe antes de intentar desde USB y luego desde la tarjeta SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    En este paso se recomienda usar una tarjeta Micro SD de repuesto. Primero graba el bootloader en esta tarjeta y luego insértala en la Raspberry Pi para habilitar el arranque desde NVMe.
    
    Como alternativa, puedes grabar el bootloader directamente en tu dispositivo NVMe, insertarlo en la Raspberry Pi para cambiar el método de arranque y luego conectarlo al ordenador para instalar el sistema operativo. Una vez completada la instalación, vuelve a insertarlo en la Raspberry Pi.

#. Inserta tu tarjeta Micro SD o SSD NVMe en tu ordenador utilizando un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. En la pestaña **Operating System**, desplázate hacia abajo y selecciona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Selecciona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Selecciona **NVMe/USB Boot** para habilitar el arranque desde NVMe antes que desde USB y luego SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. En la opción **Storage**, selecciona el dispositivo de almacenamiento correspondiente.

   .. note::

      Asegúrate de seleccionar el dispositivo correcto. Para evitar confusión, desconecta cualquier otro dispositivo de almacenamiento adicional.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ahora haz clic en **NEXT**. Si el dispositivo contiene datos, asegúrate de hacer una copia de seguridad antes de continuar. Si no necesitas respaldo, haz clic en **Yes**.

   .. image:: img/os_continue.png
      :width: 90%


#. En breve verás un mensaje indicando que **NVMe/USB Boot** ha sido escrito correctamente en tu dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Ahora puedes insertar tu tarjeta Micro SD o SSD NVMe en la Raspberry Pi. Al encenderla con un adaptador Tipo C, el bootloader se grabará en la EEPROM de la Raspberry Pi.

.. note::

    Después de esto, la Raspberry Pi arrancará desde NVMe antes de intentar desde USB y luego desde la tarjeta SD. 
    
    Apaga la Raspberry Pi y retira la tarjeta Micro SD o el SSD NVMe.


2. Instalar el sistema operativo en el SSD NVMe
------------------------------------------------------

Ahora puedes instalar el sistema operativo en tu SSD NVMe.


#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Selecciona **Operating System** y elige la versión recomendada del sistema.

   .. image:: img/os_choose_os.png
      :width: 90%


#. En la opción **Storage**, selecciona el dispositivo de almacenamiento correspondiente.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Haz clic en **NEXT** y luego en **EDIT SETTINGS** para personalizar la configuración del sistema operativo.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Define un **hostname** para tu Raspberry Pi. El hostname es el identificador de red del dispositivo y puedes acceder a él usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png
         
   * Crea un **Username** y una **Password** para la cuenta de administrador. Establecer credenciales únicas es fundamental para la seguridad, ya que la Raspberry Pi no tiene una contraseña predeterminada.

     .. image:: img/os_set_username.png
         
   * Configura la red inalámbrica proporcionando el **SSID** y la **Password** de tu red.

     .. note::

       Establece el valor de ``Wireless LAN country`` utilizando el código de dos letras `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

     .. image:: img/os_set_wifi.png
         
   * Para conectarte de forma remota, habilita el acceso SSH desde la pestaña **Services**.

     * Para **autenticación por contraseña**, utiliza el nombre de usuario y contraseña definidos en la pestaña **General**.
     * Para autenticación por clave pública, selecciona "Allow public-key authentication only". Si ya tienes una clave RSA, se usará automáticamente. Si no, haz clic en "Run SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png
         
   * El menú **Options** te permite configurar el comportamiento del Imager tras finalizar la escritura, como reproducir un sonido, expulsar el dispositivo o habilitar la telemetría.

     .. image:: img/os_options.png

#. Cuando termines de configurar los ajustes personalizados, haz clic en **Save** para guardarlos. Luego haz clic en **Yes** para aplicarlos al escribir la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si el SSD NVMe contiene datos, asegúrate de hacer una copia de seguridad antes de continuar. Haz clic en **Yes** si no se requiere respaldo.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Cuando aparezca el mensaje "Write Successful", la imagen se habrá grabado y verificado correctamente. ¡Tu Raspberry Pi ya está lista para arrancar desde el SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%

