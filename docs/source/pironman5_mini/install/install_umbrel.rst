.. note:: 

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios de nuevos productos y contenido exclusivo.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


Instalar Umbrel OS
============================================

Umbrel es una plataforma/sistema operativo de servidor doméstico autoalojado y de código abierto que te permite ejecutar tu propio nodo de Bitcoin, instalar una variedad de aplicaciones autoalojadas con un solo clic y convertir tu hardware en tu nube doméstica personal. Es una excelente forma de comenzar con la autocustodia y la privacidad.

**Componentes necesarios**

* Un ordenador personal
* Un SSD NVMe
* Un adaptador NVMe a USB
* Tarjeta Micro SD y lector

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Instalar el sistema operativo en el SSD NVMe
--------------------------------------------------

Ahora estás listo para instalar el sistema operativo en tu **SSD NVMe**.  
Solo sigue cuidadosamente los pasos a continuación: esta guía está pensada para principiantes y es fácil de seguir.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Versiones de Umbrel OS</a>

#. Descarga la última imagen de **Umbrel OS** y extrae el archivo. Si deseas usar una versión específica, también puedes visitar la página de |link_umbrel_release|.

   * :download:`Última imagen de Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Inserta el **SSD NVMe** en tu ordenador usando un **adaptador NVMe a USB**.

#. Abre **Raspberry Pi Imager**. En la pantalla **Device**, selecciona tu modelo de **Raspberry Pi 5** de la lista.

   .. image:: img/imager_device.png
      :width: 90%

#. Ve a la sección **OS**, desplázate hasta la parte inferior y selecciona **Use custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Selecciona el **archivo de imagen de Umbrel OS** que descargaste y extrajiste anteriormente, luego haz clic en **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Haz clic en **Next** para continuar.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. En la sección **Storage**, selecciona tu **SSD NVMe**. Asegúrate de elegir el SSD NVMe y no otra unidad de tu ordenador.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Revisa cuidadosamente todos los ajustes y luego haz clic en **WRITE**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. Si el SSD NVMe ya contiene datos, Raspberry Pi Imager mostrará una advertencia indicando que todos los datos se borrarán. Verifica de nuevo que la unidad correcta esté seleccionada y luego haz clic en **I UNDERSTAND, ERASE AND WRITE**.

   .. image:: img/imager_erase.png
      :width: 90%

#. Cuando aparezca el mensaje **“Write Complete”**, la imagen se habrá escrito y verificado correctamente.

   .. image:: img/imager_umbrel_finish.png
      :width: 90%

