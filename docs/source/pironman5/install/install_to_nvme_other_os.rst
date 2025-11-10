.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_to_nvme_home_bridge:

Instalación del Sistema Operativo en un NVMe SSD
=====================================================

Si estás utilizando un NVMe SSD y tienes un adaptador para conectarlo a tu computadora para la instalación del sistema, puedes seguir el siguiente tutorial para una instalación rápida.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center 

**Componentes Requeridos**

* Una computadora personal
* Un NVMe SSD
* Un adaptador de NVMe a USB
* Tarjeta Micro SD y lector



1. Actualizar el Bootloader
----------------------------------

Primero, debes actualizar el bootloader del Raspberry Pi 5 para que arranque desde NVMe antes de intentar USB y luego la tarjeta SD.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="Reproductor de video de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    En este paso, se recomienda utilizar una tarjeta Micro SD de repuesto. Primero, escribe el bootloader en esta tarjeta Micro SD y luego insértala inmediatamente en el Raspberry Pi para habilitar el arranque desde un dispositivo NVMe.
    
    Alternativamente, puedes escribir el bootloader directamente en tu dispositivo NVMe primero, luego insertarlo en el Raspberry Pi para cambiar su método de arranque. Posteriormente, conecta el NVMe SSD a una computadora para instalar el sistema operativo y, una vez que la instalación esté completa, vuelve a insertarlo en el Raspberry Pi.

#. Inserta tu tarjeta Micro SD de repuesto o NVMe SSD en tu computadora o laptop utilizando un lector.

#. Dentro del |link_rpi_imager|, haz clic en **Dispositivo Raspberry Pi** y selecciona el modelo **Raspberry Pi 5** de la lista desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. En la pestaña **Sistema Operativo**, desplázate hacia abajo y selecciona **Imágenes de utilidad diversas**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Selecciona **Bootloader (familia Pi 5)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Selecciona **Arranque NVMe/USB** para habilitar que Raspberry Pi 5 arranque desde NVMe antes de intentar USB y luego la tarjeta SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      


#. En la opción **Almacenamiento**, selecciona el dispositivo de almacenamiento apropiado para la instalación.

   .. note::

      Asegúrate de seleccionar el dispositivo de almacenamiento correcto. Para evitar confusión, desconecta cualquier dispositivo de almacenamiento adicional si hay varios conectados.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Ahora puedes hacer clic en **SIGUIENTE**. Si el dispositivo de almacenamiento contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar la pérdida de datos. Procede haciendo clic en **Sí** si no se necesita una copia de seguridad.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Pronto se te indicará que **Arranque NVMe/USB** se ha escrito en tu dispositivo de almacenamiento.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Ahora, puedes insertar tu tarjeta Micro SD o NVMe SSD en el Raspberry Pi. Después de alimentar el Raspberry Pi con un adaptador Tipo C, el bootloader de la tarjeta Micro SD o NVMe SSD se escribirá en la EEPROM del Raspberry Pi.

.. note::

   Después de esto, el Raspberry Pi arrancará desde NVMe antes de intentar USB y luego la tarjeta SD. 
    
   Apaga el Raspberry Pi y retira la tarjeta Micro SD o NVMe SSD.


2. Instalar el Sistema Operativo en el NVMe SSD
----------------------------------------------------

Ahora puedes instalar el sistema operativo en tu NVMe SSD.

**Pasos**

#. Inserta tu tarjeta SD en tu computadora o laptop utilizando un lector.

#. Dentro del |link_rpi_imager|, haz clic en **Dispositivo Raspberry Pi** y selecciona el modelo **Raspberry Pi 5** de la lista desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      

#. Haz clic en la pestaña **Sistema Operativo**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta la parte inferior de la página y selecciona tu sistema operativo.

   .. note::

      * Para el sistema **Ubuntu**, debes hacer clic en **Otro sistema operativo de propósito general** -> **Ubuntu**, y seleccionar ya sea **Ubuntu Desktop 24.04 LTS (64 bit)** o **Ubuntu Server 24.04 LTS (64 bit)**.
      * Para los sistemas **Kali Linux**, **Home Assistant** y **Homebridge**, debes hacer clic en **Otros sistemas operativos específicos** y luego seleccionar el sistema correspondiente.

   .. image:: img/os_other_os.png
      :width: 90%

#. En la opción **Almacenamiento**, selecciona el dispositivo de almacenamiento apropiado para la instalación.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      

#. Haz clic en **SIGUIENTE**.

   .. note::

      * Para sistemas que no pueden configurarse por adelantado, después de hacer clic en **SIGUIENTE**, se te preguntará si deseas guardar los datos dentro del dispositivo. Si has confirmado que se ha realizado una copia de seguridad, selecciona **Sí**.

      * Para sistemas donde se puede configurar el Nombre del Host, WiFi y habilitar SSH por adelantado, aparecerá una ventana emergente preguntando si deseas aplicar la configuración personalizada del sistema operativo. Puedes elegir **Sí** o **No**, o volver atrás para editar más.

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Define un **nombre de host** para tu Raspberry Pi. El nombre de host es el identificador de red de tu Raspberry Pi. Puedes acceder a tu Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Nombre de Usuario** y **Contraseña** para la cuenta de administrador de Raspberry Pi. Establecer un nombre de usuario y contraseña únicos es fundamental para proteger tu Raspberry Pi, que carece de una contraseña predeterminada.

     .. image:: img/os_set_username.png

   * Configura la red LAN inalámbrica proporcionando el **SSID** y la **Contraseña** de tu red.

     .. note::

       Establece el ``país de la LAN inalámbrica`` al código de dos letras `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

     .. image:: img/os_set_wifi.png
         
   * Para conectarte de forma remota a tu Raspberry Pi, habilita SSH en la pestaña Servicios.

     * Para **autenticación con contraseña**, utiliza el nombre de usuario y la contraseña de la pestaña General.
     * Para autenticación con clave pública, elige "Permitir solo autenticación con clave pública". Si tienes una clave RSA, se usará. Si no, haz clic en "Ejecutar SSH-keygen" para generar un nuevo par de claves.

     .. image:: img/os_enable_ssh.png

   * El menú **Opciones** te permite configurar el comportamiento de Imager durante una escritura, incluyendo reproducir sonido cuando termine, expulsar el medio cuando termine y habilitar la telemetría.

     .. image:: img/os_options.png

         
    
#. Cuando hayas terminado de ingresar la personalización del sistema operativo, haz clic en **Guardar** para guardar tu personalización. Luego, haz clic en **Sí** para aplicarlas al escribir la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. Si el NVMe SSD contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar la pérdida de datos. Procede haciendo clic en **Sí** si no se necesita una copia de seguridad.

   .. image:: img/nvme_erase.png
      :width: 90%
      

#. Cuando veas el mensaje emergente "Escritura Exitosa", tu imagen ha sido completamente escrita y verificada. ¡Ahora estás listo para iniciar un Raspberry Pi desde el NVMe SSD!

