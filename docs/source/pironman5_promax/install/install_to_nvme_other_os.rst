.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_to_nvme_other_promax:

Instalación del SO en un SSD NVMe
============================================

Si está usando un SSD NVMe y tiene un adaptador para conectar el SSD NVMe a su ordenador para la instalación del sistema, puede usar el siguiente tutorial para una instalación rápida.

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center

**Componentes Requeridos**

* Una Computadora Personal
* Un SSD NVMe
* Un adaptador de NVMe a USB
* Tarjeta Micro SD y Lector

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Instalar el SO en la tarjeta microSD
------------------------------------------------

#. Inserte el **SSD NVMe** en su ordenador usando un adaptador.

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

4. En la sección **Storage**, seleccione su **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Haga clic en **NEXT**.

   .. note::

      * Para sistemas que **no se pueden configurar por adelantado**, hacer clic en **NEXT** omitirá el paso de **Customisation** e irá directamente a **Writing**, donde el SO se escribe en la tarjeta microSD.
      * Para sistemas que **soportan preconfiguración**, siga los pasos de **Customisation** para configurar opciones como **Hostname**, **WiFi** y **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Cuando aparezca la ventana emergente **“Write Successful”**, la imagen ha sido completamente escrita y verificada. Ahora puede retirar la tarjeta microSD de forma segura y usarla para arrancar su Raspberry Pi.