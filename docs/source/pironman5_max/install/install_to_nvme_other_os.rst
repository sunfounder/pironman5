.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza tus conocimientos sobre Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Soluciona problemas técnicos y postventa con el apoyo de nuestra comunidad y equipo especializado.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede antes que nadie a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_install_to_nvme_home_bridge:

Instalación del sistema operativo en un SSD NVMe
======================================================

Si dispones de un SSD NVMe y un adaptador para conectarlo a tu ordenador, puedes seguir este tutorial para realizar una instalación rápida.

**Componentes necesarios**

* Un ordenador personal
* Un SSD NVMe
* Un adaptador NVMe a USB
* Una tarjeta Micro SD y lector

.. _update_bootloader_max:

1. Actualizar el Bootloader
----------------------------------

Primero necesitas actualizar el bootloader de la Raspberry Pi 5 para que arranque desde NVMe antes de intentar desde USB y luego desde la tarjeta SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    En este paso se recomienda utilizar una tarjeta Micro SD de repuesto. Primero graba el bootloader en esta tarjeta y luego insértala en la Raspberry Pi para activar el arranque desde un dispositivo NVMe.
    
    Como alternativa, puedes escribir el bootloader directamente en tu dispositivo NVMe, insertarlo en la Raspberry Pi para cambiar su método de arranque, y luego conectarlo a tu ordenador para instalar el sistema operativo. Una vez completada la instalación, vuelve a insertar el SSD en la Raspberry Pi.

#. Inserta tu tarjeta Micro SD de repuesto o SSD NVMe en tu ordenador mediante un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. En la pestaña **Operating System**, desplázate hacia abajo y selecciona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Selecciona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Selecciona **NVMe/USB Boot** para que la Raspberry Pi 5 arranque primero desde NVMe, luego USB y por último desde la tarjeta SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. En la opción **Storage**, selecciona el dispositivo de almacenamiento adecuado.

   .. note::

      Asegúrate de elegir correctamente el dispositivo. Para evitar confusiones, desconecta otros dispositivos si tienes varios conectados.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Haz clic en **NEXT**. Si el dispositivo contiene datos importantes, haz una copia de seguridad antes de continuar. Haz clic en **Yes** si no necesitas respaldo.

   .. image:: img/os_continue.png
      :width: 90%


#. Pronto recibirás una notificación indicando que **NVMe/USB Boot** se ha escrito correctamente en el dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Ahora puedes insertar la tarjeta Micro SD o el SSD NVMe en tu Raspberry Pi. Al encenderla con un adaptador USB tipo C, el bootloader se grabará en la EEPROM de la Raspberry Pi.

.. note::

    A partir de ahora, la Raspberry Pi arrancará desde NVMe, luego USB y finalmente desde la tarjeta SD. 
    
    Apaga la Raspberry Pi y retira la tarjeta Micro SD o el SSD NVMe.


2. Instalar el sistema operativo en el SSD NVMe
------------------------------------------------------

Ahora puedes instalar el sistema operativo en tu SSD NVMe.

**Pasos**

#. Inserta tu tarjeta SD en el ordenador utilizando un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Haz clic en la pestaña **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta el final y selecciona tu sistema operativo.

   .. note::

      * Para **Ubuntu**, haz clic en **Other general-purpose OS** -> **Ubuntu**, y selecciona **Ubuntu Desktop 24.04 LTS (64 bit)** o **Ubuntu Server 24.04 LTS (64 bit)**.
      * Para **Kali Linux**, **Home Assistant** y **Homebridge**, haz clic en **Other specific-purpose OS** y selecciona el sistema correspondiente.

   .. image:: img/os_other_os.png
      :width: 90%

#. En la opción **Storage**, selecciona el dispositivo de almacenamiento correspondiente.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Haz clic en **NEXT**.

   .. note::

      * Para sistemas que no se pueden configurar de antemano, aparecerá un mensaje preguntando si deseas borrar los datos del dispositivo. Si ya hiciste copia de seguridad, selecciona **Yes**.

      * Para sistemas que permiten configurar Hostname, WiFi y habilitar SSH por adelantado, aparecerá una ventana emergente donde puedes aplicar la configuración personalizada del sistema. Puedes hacer clic en **Yes**, **No** o volver para editar.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Define un **hostname** para tu Raspberry Pi. Este será su identificador de red y podrás acceder a él con ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Nombre de usuario** y **Contraseña** para la cuenta de administrador. Establecer credenciales únicas es importante para la seguridad del sistema, ya que no hay una contraseña por defecto.

     .. image:: img/os_set_username.png

   * Configura la red Wi-Fi introduciendo el **SSID** y la **Contraseña**.

     .. note::

       Establece el ``Wireless LAN country`` utilizando el código de dos letras `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu país.

     .. image:: img/os_set_wifi.png

   * Para conectarte remotamente, habilita SSH en la pestaña de **Services**.

     * Para autenticación por contraseña, utiliza el nombre de usuario y contraseña definidos en la pestaña **General**.
     * Para autenticación con clave pública, selecciona "Allow public-key authentication only". Si ya tienes una clave RSA, se usará automáticamente. Si no, haz clic en "Run SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png

   * En el menú **Options** puedes configurar el comportamiento de Imager al finalizar la escritura, como reproducir un sonido, expulsar el medio o habilitar la telemetría.

     .. image:: img/os_options.png



#. Una vez que completes la personalización del sistema operativo, haz clic en **Save** para guardar los cambios. Luego, haz clic en **Yes** para aplicarlos durante la escritura de la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si el SSD NVMe contiene datos existentes, asegúrate de respaldarlos antes de continuar. Haz clic en **Yes** si no necesitas conservar los datos.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Cuando aparezca el mensaje "Write Successful", la imagen se habrá escrito y verificado correctamente. ¡Ya puedes arrancar tu Raspberry Pi desde el SSD NVMe!
