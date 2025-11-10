.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros aficionados para profundizar tus conocimientos en Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede antes que nadie a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Aprovecha descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _install_to_nvme_ubuntu_mini:

Instalación del sistema operativo en un SSD NVMe
====================================================

Si estás utilizando un SSD NVMe y tienes un adaptador para conectarlo a tu computadora, puedes seguir este tutorial para una instalación rápida.

**Componentes necesarios**

* Una computadora personal
* Un SSD NVMe
* Un adaptador NVMe a USB
* Tarjeta Micro SD y lector


1. Actualizar el gestor de arranque
--------------------------------------

Primero, debes actualizar el gestor de arranque de la Raspberry Pi 5 para permitir el arranque desde NVMe antes de intentar USB y luego la tarjeta SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    En este paso, se recomienda usar una tarjeta Micro SD adicional. Primero escribe el gestor de arranque en esta tarjeta Micro SD e insértala de inmediato en la Raspberry Pi para habilitar el arranque desde un dispositivo NVMe.

    Alternativamente, puedes escribir el gestor de arranque directamente en tu NVMe, insertarlo en la Raspberry Pi para cambiar el método de arranque, luego conectarlo a una computadora para instalar el sistema operativo, y finalmente volver a insertarlo en la Raspberry Pi.

#. Inserta tu tarjeta Micro SD adicional o SSD NVMe en tu computadora mediante un lector.

#. Dentro de |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. En la pestaña **Operating System**, desplázate hacia abajo y selecciona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Selecciona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Selecciona **NVMe/USB Boot** para habilitar el arranque desde NVMe antes de intentar con USB y luego la tarjeta SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. En la opción **Storage**, selecciona el dispositivo de almacenamiento correcto para la instalación.

   .. note::

      Asegúrate de seleccionar el dispositivo adecuado. Para evitar confusiones, desconecta cualquier otro dispositivo de almacenamiento conectado.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Haz clic en **NEXT**. Si el dispositivo contiene datos existentes, asegúrate de hacer una copia de seguridad. Haz clic en **Yes** si no necesitas respaldar nada.

   .. image:: img/os_continue.png
      :width: 90%


#. Aparecerá un mensaje indicando que **NVMe/USB Boot** se ha escrito correctamente en tu dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Ahora puedes insertar tu tarjeta Micro SD o SSD NVMe en la Raspberry Pi. Después de encenderla con un adaptador USB-C, el gestor de arranque será grabado en el EEPROM de la Raspberry Pi.

.. note::

    A partir de este momento, la Raspberry Pi intentará arrancar desde NVMe, luego USB, y por último desde la tarjeta SD.

    Apaga la Raspberry Pi y retira la tarjeta Micro SD o el SSD NVMe.


2. Instalar el sistema operativo en el SSD NVMe
--------------------------------------------------

Ahora puedes instalar el sistema operativo en tu SSD NVMe.

**Pasos**

#. Primero, ve a la página |link_batocera_download|, selecciona **Raspberry Pi 5 B** y haz clic para descargar.

   .. image:: img/batocera_download.png
      :width: 90%


#. Descomprime el archivo descargado ``batocera-xxx-xx-xxxxxxxx.img.gz``.


#. Inserta tu tarjeta SD en la computadora mediante un lector.

#. En |link_rpi_imager|, haz clic en la pestaña **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta abajo y selecciona **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. Elige el archivo del sistema que acabas de descomprimir, ``batocera-xxx-xx-xxxxxxxx.img``, y haz clic en **Open**.


   .. image:: img/batocera_os_choose.png
      :width: 90%


#. En la opción **Storage**, selecciona el dispositivo correcto para la instalación.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. Haz clic en **NEXT**. Si el SSD contiene datos, haz una copia de seguridad antes de continuar. Si no es necesario, haz clic en **Yes**.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Cuando veas el mensaje "Write Successful", significa que la imagen se ha grabado y verificado correctamente. ¡Ya puedes arrancar tu Raspberry Pi desde el SSD NVMe!
