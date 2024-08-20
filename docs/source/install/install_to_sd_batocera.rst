.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_to_sd_ubuntu:

Instalación del Sistema Operativo en una Tarjeta Micro SD
================================================================

Si estás utilizando una tarjeta Micro SD, puedes seguir el siguiente tutorial para instalar el sistema en tu tarjeta Micro SD.


**Componentes Requeridos**

* Una computadora personal
* Una tarjeta Micro SD y lector

**Pasos**

#. Primero, navega a la página de |link_batocera_download|, selecciona **Raspberry Pi 5 B** y haz clic para descargar.

   .. image:: img/batocera_download.png
      :width: 90%
      

#. Inserta tu tarjeta SD en tu computadora o laptop utilizando un lector.

#. Dentro del |link_rpi_imager|, haz clic en la pestaña **Sistema Operativo**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Desplázate hasta la parte inferior de la página y selecciona **Usar Personalizado**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%
      

#. Elige el archivo del sistema que acabas de descargar, ``batocera-xxx-xx-xxxxxxxx.img.gz``, y luego haz clic en **Abrir**.

   .. image:: img/batocera_os_choose.png
      :width: 90%
      

#. Haz clic en **Elegir Almacenamiento** y selecciona el dispositivo de almacenamiento apropiado para la instalación.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Ahora puedes hacer clic en **SIGUIENTE**. Si el dispositivo de almacenamiento contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar la pérdida de datos. Procede haciendo clic en **Sí** si no se necesita una copia de seguridad.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Cuando veas el mensaje emergente "Escritura Exitosa", tu imagen ha sido completamente escrita y verificada. ¡Ahora estás listo para iniciar un Raspberry Pi desde la tarjeta Micro SD!

