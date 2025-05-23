.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos lanzamientos y primicias de productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales en fechas señaladas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _install_to_sd_ubuntu_mini:

Instalación del sistema operativo en una tarjeta Micro SD
==============================================================

Si vas a utilizar una tarjeta Micro SD, puedes seguir el siguiente tutorial para instalar el sistema en ella.


**Componentes necesarios**

* Una computadora personal
* Una tarjeta Micro SD y un lector

**Pasos**

#. Primero, accede a la página |link_batocera_download|, selecciona **Raspberry Pi 5 B** y haz clic para descargar.

   .. image:: img/batocera_download.png
      :width: 90%
      

#. Descomprime el archivo descargado ``batocera-xxx-xx-xxxxxxxx.img.gz``.



#. Inserta la tarjeta SD en tu computadora o portátil mediante un lector.

#. En |link_rpi_imager|, haz clic en la pestaña **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta el final de la página y selecciona **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. Selecciona el archivo del sistema que acabas de descomprimir, ``batocera-xxx-xx-xxxxxxxx.img``, y luego haz clic en **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Haz clic en **Choose Storage** y selecciona el dispositivo de almacenamiento adecuado para la instalación.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ahora puedes hacer clic en **NEXT**. Si el dispositivo de almacenamiento contiene datos, asegúrate de hacer una copia de seguridad para evitar pérdidas. Si no necesitas respaldo, haz clic en **Yes** para continuar.

   .. image:: img/os_continue.png
      :width: 90%


#. Cuando aparezca el mensaje "Write Successful", la imagen se habrá escrito y verificado correctamente. ¡Ya estás listo para arrancar tu Raspberry Pi desde la tarjeta Micro SD!
