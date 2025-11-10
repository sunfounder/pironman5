.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Soluciona problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Sé el primero en conocer nuevos lanzamientos y vistas previas de productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _install_to_nvme_home_bridge_mini:

Instalación del sistema operativo en un SSD NVMe
=====================================================

Si cuentas con un SSD NVMe y un adaptador para conectarlo a tu computadora, puedes seguir el siguiente tutorial para realizar una instalación rápida.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Componentes necesarios**

* Una computadora personal
* Un SSD NVMe
* Un adaptador NVMe a USB
* Tarjeta Micro SD y lector

1. Actualizar el gestor de arranque
------------------------------------

Primero, necesitas actualizar el gestor de arranque de la Raspberry Pi 5 para que arranque desde NVMe antes de intentar USB y luego la tarjeta SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    En este paso se recomienda usar una tarjeta Micro SD adicional. Primero escribe el gestor de arranque en esta tarjeta e insértala inmediatamente en la Raspberry Pi para habilitar el arranque desde un dispositivo NVMe.
    
    Alternativamente, puedes escribir el gestor de arranque directamente en tu SSD NVMe, insertarlo en la Raspberry Pi para cambiar el método de arranque, y luego conectarlo a una computadora para instalar el sistema operativo. Una vez completado, vuelve a insertar el SSD en la Raspberry Pi.

#. Inserta tu tarjeta Micro SD adicional o SSD NVMe en la computadora mediante un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. En la pestaña **Operating System**, desplázate y selecciona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Selecciona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Selecciona **NVMe/USB Boot** para habilitar el arranque desde NVMe antes que USB y tarjeta SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. En la opción **Storage**, elige el dispositivo de almacenamiento adecuado.

   .. note::

      Asegúrate de seleccionar el dispositivo correcto. Para evitar confusiones, desconecta otros dispositivos de almacenamiento si los hay.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Haz clic en **NEXT**. Si el dispositivo contiene datos, asegúrate de respaldarlos antes de continuar. Haz clic en **Yes** si no necesitas respaldo.

   .. image:: img/os_continue.png
      :width: 90%


#. Aparecerá una notificación indicando que el arranque **NVMe/USB Boot** se ha escrito correctamente.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Ahora puedes insertar tu tarjeta Micro SD o SSD NVMe en la Raspberry Pi. Al alimentarla con un adaptador tipo C, el gestor de arranque será escrito en la EEPROM.

.. note::

   Después de esto, la Raspberry Pi arrancará desde NVMe antes de probar USB y SD.
    
   Apaga la Raspberry Pi y retira la tarjeta Micro SD o el SSD NVMe.


2. Instalar el sistema operativo en el SSD NVMe
---------------------------------------------------

Ahora puedes instalar el sistema operativo en tu SSD NVMe.

**Pasos**

#. Inserta tu tarjeta SD en la computadora mediante un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Haz clic en la pestaña **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta el final de la página y selecciona el sistema operativo correspondiente.

   .. note::

      * Para **Ubuntu**, haz clic en **Other general-purpose OS** -> **Ubuntu**, y selecciona **Ubuntu Desktop 24.04 LTS (64 bit)** o **Ubuntu Server 24.04 LTS (64 bit)**.
      * Para **Kali Linux**, **Home Assistant** y **Homebridge**, haz clic en **Other specific-purpose OS** y selecciona el sistema deseado.

   .. image:: img/os_other_os.png
      :width: 90%

#. En la opción **Storage**, selecciona el dispositivo de almacenamiento adecuado.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Haz clic en **NEXT**.

   .. note::

      * Para sistemas que no permiten configuración anticipada, al hacer clic en **NEXT** se te preguntará si deseas guardar los datos del dispositivo. Si ya hiciste respaldo, selecciona **Yes**.

      * Para sistemas con configuración anticipada de Hostname, WiFi y SSH, aparecerá un mensaje preguntando si deseas aplicar las personalizaciones del sistema operativo. Puedes seleccionar **Yes**, **No**, o regresar para editar.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Define un **hostname** para tu Raspberry Pi. Este será el identificador de red. Podrás acceder con ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Username** y **Password** para la cuenta de administrador. Establecer credenciales seguras es fundamental, ya que no hay contraseña por defecto.

     .. image:: img/os_set_username.png

   * Configura la red inalámbrica ingresando el **SSID** y la **contraseña**.

     .. note::

       Define el valor de ``Wireless LAN country`` usando el código de dos letras `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

     .. image:: img/os_set_wifi.png
         
   * Para conectarte remotamente a tu Raspberry Pi, habilita SSH en la pestaña Services.

     * Para autenticación por contraseña, usa las credenciales de la pestaña General.
     * Para autenticación por clave pública, selecciona "Allow public-key authentication only". Si no tienes una clave RSA, haz clic en "Run SSH-keygen".

     .. image:: img/os_enable_ssh.png

   * El menú **Options** permite configurar el comportamiento del Imager al finalizar: reproducir sonido, expulsar medios y habilitar telemetría.

     .. image:: img/os_options.png



#. Una vez ingresadas todas las configuraciones, haz clic en **Save** para guardarlas, y luego en **Yes** para aplicarlas al escribir la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si el SSD NVMe contiene datos previos, asegúrate de hacer una copia de seguridad. De lo contrario, haz clic en **Yes** para continuar.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Cuando aparezca el mensaje "Write Successful", la imagen se habrá escrito y verificado correctamente. ¡Ya puedes arrancar tu Raspberry Pi desde el SSD NVMe!
