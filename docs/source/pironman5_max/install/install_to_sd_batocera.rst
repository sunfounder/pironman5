.. note:: 

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede antes que nadie a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de promociones exclusivas en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_install_to_sd_ubuntu:

Instalación del sistema operativo en una tarjeta Micro SD
=============================================================

Si estás utilizando una tarjeta Micro SD, puedes seguir el siguiente tutorial para instalar el sistema en tu tarjeta.


**Componentes necesarios**

* Un ordenador personal
* Una tarjeta Micro SD y un lector

**Pasos**

#. Primero, accede a la página |link_batocera_download|, selecciona **Raspberry Pi 5 B** y haz clic para descargar.

   .. image:: img/batocera_download.png
      :width: 90%
      
#. Descomprime el archivo descargado ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Inserta tu tarjeta SD en el ordenador o portátil utilizando un lector.

#. Dentro de |link_rpi_imager|, haz clic en la pestaña **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta el final de la página y selecciona **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%
      

#. Elige el archivo del sistema que acabas de descomprimir, ``batocera-xxx-xx-xxxxxxxx.img``, y luego haz clic en **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%
      

#. Haz clic en **Choose Storage** y selecciona el dispositivo de almacenamiento adecuado para la instalación.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Ahora puedes hacer clic en **NEXT**. Si el dispositivo de almacenamiento contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar pérdidas. Si no necesitas respaldo, haz clic en **Yes** para continuar.

   .. image:: img/os_continue.png
      :width: 90%
      
      
#. Cuando veas la ventana emergente "Write Successful", significa que la imagen se ha escrito y verificado correctamente. ¡Ahora estás listo para arrancar tu Raspberry Pi desde la tarjeta Micro SD!
