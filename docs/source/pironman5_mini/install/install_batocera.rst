.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Instalación del Sistema Operativo Batocera
==========================================================

Sigue el siguiente tutorial para instalar el sistema en tu tarjeta microSD.

**Componentes necesarios**

*   Una computadora personal
*   Una tarjeta Micro SD y un lector de tarjetas

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Instalar el sistema operativo en la tarjeta microSD
-------------------------------------------------------------------

1.  Inserta tu tarjeta microSD en tu computadora usando un lector de tarjetas.
    Antes de continuar, haz una copia de seguridad de todos los datos importantes en la tarjeta, ya que serán borrados.

   .. image:: img/insert_sd.png
      :width: 90%

2.  Cuando se abra **Raspberry Pi Imager**, verás la página **Device (Dispositivo)**.
    Selecciona tu modelo de **Raspberry Pi 5** de la lista.

   .. image:: img/imager_device.png
      :width: 90%

3.  Ve a la sección **OS (Sistema Operativo)**, desplázate hasta la parte inferior de la página y selecciona tu sistema operativo.

   .. note::

      *   Para **Ubuntu**, haz clic en **Other general-purpose OS (Otros SO de propósito general)** → **Ubuntu**, y luego selecciona
          **Ubuntu Desktop 24.04 LTS (64-bit)** o **Ubuntu Server 24.04 LTS (64-bit)**.
      *   Para **Kali Linux**, **Home Assistant** y **Homebridge**, haz clic en
          **Other specific-purpose OS (Otros SO de propósito específico)**, y luego selecciona el sistema correspondiente.

   .. image:: img/imager_other_os.png
      :width: 90%

4.  En la sección **Storage (Almacenamiento)**, selecciona tu tarjeta microSD.
    Para mayor seguridad, se recomienda desconectar otros dispositivos de almacenamiento USB para que solo aparezca la tarjeta microSD en la lista.

   .. image:: img/imager_storage.png
      :width: 90%

#.  Haz clic en **NEXT (SIGUIENTE)**.

   .. note::

      *   Para los sistemas que **no se pueden preconfigurar**, hacer clic en **NEXT (SIGUIENTE)** omitirá el paso **Customisation (Personalización)** y pasará directamente a **Writing (Escritura)**, donde el sistema operativo se escribe en la tarjeta microSD.
      *   Para los sistemas que **admiten preconfiguración**, sigue los pasos de **Customisation (Personalización)** para configurar opciones como **Hostname (Nombre de host)**, **WiFi** y la **activación de SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#.  Cuando aparezca la ventana emergente **«Write Successful (Escritura exitosa)»**, la imagen se ha escrito y verificado completamente. Ahora puedes retirar la tarjeta microSD de forma segura y usarla para arrancar tu Raspberry Pi.