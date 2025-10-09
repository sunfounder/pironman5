.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con el respaldo de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede antes que nadie a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_install_to_nvme_ubuntu:

Instalación del sistema operativo en un SSD NVMe
=====================================================

Si cuentas con un SSD NVMe y un adaptador para conectarlo a tu ordenador, puedes seguir este tutorial para realizar una instalación rápida.

**Componentes necesarios**

* Un ordenador personal
* Un SSD NVMe
* Un adaptador de NVMe a USB
* Una tarjeta Micro SD y su lector

.. _update_bootloader_max:

1. Actualizar el bootloader
----------------------------------

Primero debes actualizar el bootloader de la Raspberry Pi 5 para que arranque desde NVMe antes de intentar desde USB y luego desde la tarjeta SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    En este paso, se recomienda usar una tarjeta Micro SD de repuesto. Primero escribe el bootloader en esta tarjeta y luego insértala en la Raspberry Pi para habilitar el arranque desde un dispositivo NVMe.
    
    Como alternativa, puedes escribir el bootloader directamente en el NVMe, insertarlo en la Raspberry Pi para cambiar el método de arranque, y luego conectarlo al ordenador para instalar el sistema operativo. Una vez instalado, vuelve a insertar el SSD en la Raspberry Pi.

#. Inserta tu tarjeta Micro SD o SSD NVMe en tu ordenador mediante un lector.

#. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. En la pestaña **Operating System**, desplázate hacia abajo y selecciona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. Selecciona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Selecciona **NVMe/USB Boot** para que la Raspberry Pi 5 arranque desde NVMe antes de intentar desde USB y luego SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. En la opción **Storage**, selecciona el dispositivo de almacenamiento correcto.

   .. note::

      Asegúrate de elegir el dispositivo correcto. Para evitar errores, desconecta otras unidades si hay varias conectadas.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ahora haz clic en **NEXT**. Si el dispositivo contiene datos, haz una copia de seguridad antes de continuar. Haz clic en **Yes** si no necesitas conservar esos datos.

   .. image:: img/os_continue.png
      :width: 90%


#. Pronto verás una notificación indicando que **NVMe/USB Boot** ha sido escrito en tu dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Inserta tu tarjeta Micro SD o SSD NVMe en la Raspberry Pi. Al encenderla con un adaptador USB-C, el bootloader será escrito en la EEPROM de la Raspberry Pi.

.. note::

    A partir de ahora, la Raspberry Pi arrancará primero desde NVMe, luego desde USB, y por último desde la tarjeta SD.
    
    Apaga la Raspberry Pi y retira la tarjeta Micro SD o el SSD NVMe.


2. Instalar el sistema operativo en el SSD NVMe
--------------------------------------------------

Ahora puedes instalar el sistema operativo en tu SSD NVMe.

**Pasos**

#. Dirígete a la página |link_batocera_download|, selecciona **Raspberry Pi 5 B** y haz clic en descargar.

   .. image:: img/batocera_download.png
      :width: 90%


#. Descomprime el archivo descargado ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Inserta tu tarjeta SD en el ordenador mediante un lector.

#. Abre |link_rpi_imager| y haz clic en la pestaña **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta el final y selecciona **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. Selecciona el archivo descomprimido ``batocera-xxx-xx-xxxxxxxx.img`` y haz clic en **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. En la opción **Storage**, selecciona el dispositivo adecuado para la instalación.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. Ahora haz clic en **NEXT**. Si el dispositivo tiene datos, respáldalos antes de continuar. Haz clic en **Yes** si estás listo para continuar.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Cuando veas el mensaje "Write Successful", significa que la imagen se ha escrito y verificado correctamente. ¡Ya puedes arrancar tu Raspberry Pi desde el SSD NVMe!
