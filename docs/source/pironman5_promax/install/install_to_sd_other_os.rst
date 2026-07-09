.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_to_sd_other_promax:

Instalación del SO en una Tarjeta Micro SD
=============================================

Si está usando una tarjeta Micro SD, puede seguir el tutorial a continuación para instalar el sistema en su tarjeta Micro SD.

**Componentes Requeridos**

* Una Computadora Personal
* Una tarjeta Micro SD y un Lector

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Instalar el SO en la tarjeta microSD
------------------------------------------------

1. Inserte su tarjeta microSD en su ordenador usando un lector de tarjetas.
   Antes de continuar, respalde cualquier dato importante en la tarjeta, ya que será borrada.

   .. image:: img/insert_sd.png
      :width: 90%

2. Cuando se abra **Raspberry Pi Imager**, verá la página **Device**.
   Seleccione su modelo de **Raspberry Pi 5** de la lista.

   .. image:: img/imager_device.png
      :width: 90%

3. Vaya a la sección **OS**, desplácese hacia abajo hasta el final de la página y seleccione su sistema operativo.

   .. note::

      * Para **Ubuntu**, haga clic en **Other general-purpose OS** → **Ubuntu**, luego seleccione
        **Ubuntu Desktop 24.04 LTS (64-bit)** o **Ubuntu Server 24.04 LTS (64-bit)**.
      * Para **Kali Linux** y **Homebridge**, haga clic en
        **Other specific-purpose OS**, luego seleccione el sistema correspondiente.

   .. warning::

      Sea cual sea el sistema que elijas, asegúrate de seleccionar una versión de **64 bits**. En un sistema de **32 bits**, algunos paquetes solo están disponibles para ``aarch64`` (64 bits) y es posible que ciertas funciones no se instalen o no funcionen correctamente.

   .. image:: img/imager_other_os.png
      :width: 90%

4. En la sección **Storage**, seleccione su tarjeta microSD.
   Por seguridad, se recomienda desconectar otros dispositivos de almacenamiento USB para que solo aparezca la tarjeta microSD en la lista.

   .. image:: img/imager_storage.png
      :width: 90%

#. Haga clic en **NEXT**.

   .. note::

      * Para sistemas que **no se pueden configurar por adelantado**, hacer clic en **NEXT** omitirá el paso de **Customisation** e irá directamente a **Writing**, donde el SO se escribe en la tarjeta microSD.
      * Para sistemas que **soportan preconfiguración**, siga los pasos de **Customisation** para configurar opciones como **Hostname**, **WiFi** y **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Cuando aparezca la ventana emergente **“Write Successful”**, la imagen ha sido completamente escrita y verificada. Ahora puede retirar la tarjeta microSD de forma segura y usarla para arrancar su Raspberry Pi.