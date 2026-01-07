.. note:: 

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios de nuevos productos y contenido exclusivo.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_to_nvme_other_5:

Instalar el sistema operativo en un SSD NVMe
============================================

Si estás utilizando un SSD NVMe y dispones de un adaptador para conectar el SSD NVMe a tu ordenador para la instalación del sistema, puedes seguir el siguiente tutorial para una instalación rápida.

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Componentes necesarios**

* Un ordenador personal
* Un SSD NVMe
* Un adaptador NVMe a USB
* Tarjeta Micro SD y lector

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Instalar el sistema operativo en la tarjeta microSD
-------------------------------------------------------------

#. Inserta el **SSD NVMe** en tu ordenador utilizando un adaptador.

2. Cuando se abra **Raspberry Pi Imager**, verás la página **Device**.  
   Selecciona tu modelo de **Raspberry Pi 5** de la lista.

   .. image:: img/imager_device.png
      :width: 90%

3. Ve a la sección **OS**, desplázate hasta la parte inferior de la página y selecciona tu sistema operativo.

   .. note::

      * Para **Ubuntu**, haz clic en **Other general-purpose OS** → **Ubuntu**, y luego selecciona  
        **Ubuntu Desktop 24.04 LTS (64-bit)** o **Ubuntu Server 24.04 LTS (64-bit)**.
      * Para **Kali Linux**, **Home Assistant** y **Homebridge**, haz clic en  
        **Other specific-purpose OS** y luego selecciona el sistema correspondiente.

   .. image:: img/imager_other_os.png
      :width: 90%

4. En la sección **Storage**, selecciona tu **SSD NVMe**. 

   .. image:: img/nvme_storage.png
      :width: 90%

#. Haz clic en **NEXT**.

   .. note::

      * Para los sistemas que **no se pueden configurar previamente**, al hacer clic en **NEXT** se omitirá el paso de **Customisation** y se pasará directamente a **Writing**, donde el sistema operativo se escribirá en la tarjeta microSD.
      * Para los sistemas que **admiten configuración previa**, sigue los pasos de **Customisation** para configurar opciones como **Hostname**, **WiFi** y **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Cuando aparezca la ventana emergente **“Write Successful”**, la imagen se habrá escrito y verificado por completo. Ahora puedes retirar de forma segura la tarjeta microSD y usarla para arrancar tu Raspberry Pi.
