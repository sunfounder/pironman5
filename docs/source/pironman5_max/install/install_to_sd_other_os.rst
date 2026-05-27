.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_sd_other_max:

Instalar el sistema operativo en una tarjeta Micro SD
================================================================

Si estás utilizando una tarjeta Micro SD, puedes seguir el siguiente tutorial para instalar el sistema en tu tarjeta Micro SD.


**Componentes necesarios**

* Un ordenador personal
* Una tarjeta Micro SD y un lector

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Instalar el sistema operativo en la tarjeta microSD
------------------------------------------------------------------

1. Inserta tu tarjeta microSD en el ordenador utilizando un lector de tarjetas.  
   Antes de continuar, haz una copia de seguridad de cualquier dato importante de la tarjeta, ya que se borrará.

   .. image:: img/insert_sd.png
      :width: 90%

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

4. En la sección **Storage**, selecciona tu tarjeta microSD.  
   Por seguridad, se recomienda desconectar otros dispositivos de almacenamiento USB para que solo la tarjeta microSD aparezca en la lista.

   .. image:: img/imager_storage.png
      :width: 90%

#. Haz clic en **NEXT**.

   .. note::

      * Para los sistemas que **no se pueden configurar previamente**, al hacer clic en **NEXT** se omitirá el paso de **Customisation** y se pasará directamente a **Writing**, donde el sistema operativo se escribirá en la tarjeta microSD.
      * Para los sistemas que **admiten configuración previa**, sigue los pasos de **Customisation** para configurar opciones como **Hostname**, **WiFi** y **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Cuando aparezca la ventana emergente **“Write Successful”**, la imagen se habrá escrito y verificado por completo. Ahora puedes retirar de forma segura la tarjeta microSD y usarla para arrancar tu Raspberry Pi.
