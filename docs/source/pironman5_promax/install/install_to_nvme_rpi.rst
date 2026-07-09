.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_to_nvme_rpi_promax:

Instalación del SO en un SSD NVMe
===================================

Si está usando un SSD NVMe y tiene un adaptador para conectar el SSD NVMe a su ordenador para la instalación del sistema, puede usar el siguiente tutorial para una instalación rápida.

**Componentes Requeridos**

* Una Computadora Personal
* Un SSD NVMe
* Un adaptador de NVMe a USB
* Tarjeta Micro SD y Lector

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_promax:

2. Actualizar el Bootloader
--------------------------------

Primero, actualice el bootloader de la Raspberry Pi 5 para que intente arrancar desde **NVMe primero**, luego **USB**, y finalmente la **tarjeta SD**.

.. note::

    Se recomienda usar una **tarjeta Micro SD de repuesto** para este paso.

    - Método 1 (Recomendado): Escriba el bootloader en una tarjeta Micro SD, insértela en la Raspberry Pi y arranque una vez para aplicar la configuración.
    - Método 2: Escriba el bootloader directamente en el SSD NVMe. Luego, conecte el NVMe a un ordenador para instalar el SO, y vuelva a colocarlo en la Raspberry Pi.

#. Inserte la **tarjeta Micro SD de repuesto o el SSD NVMe** en su ordenador usando un lector de tarjetas o adaptador.

#. Cuando se abra Raspberry Pi Imager, verá la página **Device**. Seleccione su modelo de Raspberry Pi 5 de la lista.

   .. image:: img/imager_device.png
      :width: 90%

#. Haga clic en **OS**.

   * Desplácese hacia abajo y seleccione **Misc utility images**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Seleccione **Bootloader (Pi 5 family)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Elija **NVMe/USB Boot** para establecer el orden de arranque, luego haga clic en **NEXT**.

     .. image:: img/nvme_boot.png
        :width: 90%

#. En **Storage**, seleccione la tarjeta Micro SD o el SSD NVMe correcto, luego haga clic en **NEXT**.

   .. note::

      Asegúrese de que el dispositivo correcto esté seleccionado. Desconecte otros dispositivos de almacenamiento si es necesario.

   .. image:: img/imager_storage.png
      :width: 90%

#. Revise la configuración y haga clic en **WRITE** para comenzar.

   .. image:: img/nvme_write.png
      :width: 90%

#. Confirme la advertencia y permita que Raspberry Pi Imager borre y escriba el bootloader.

   .. image:: img/imager_erase.png
      :width: 90%

#. Espere hasta que aparezca **Write complete!**, luego retire de forma segura el dispositivo de almacenamiento.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Inserte la tarjeta Micro SD en la Raspberry Pi y enciéndala una vez para aplicar la actualización del bootloader.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Espere al menos **10 segundos** después de que la Raspberry Pi termine de arrancar, luego apáguela y retire la tarjeta Micro SD o el SSD NVMe.

La Raspberry Pi 5 ahora está lista para arrancar desde **NVMe**.

.. end_update_bootloader

3. Instalar el SO en el SSD NVMe
-----------------------------------

Ahora puede instalar el sistema operativo en su SSD NVMe.

#. Inserte el **SSD NVMe** en su ordenador usando un adaptador.

2. Cuando se abra Raspberry Pi Imager, verá la página **Device**. Seleccione su modelo de Raspberry Pi 5 de la lista.

   .. image:: img/imager_device.png
      :width: 90%

3. Vaya a la sección **OS** y elija la opción recomendada **Raspberry Pi OS (64-bit)**.

   .. warning::

      Asegúrate de elegir una versión de **64 bits**. Si instalas un sistema de **32 bits**, algunos paquetes solo están disponibles para ``aarch64`` (64 bits) y es posible que ciertas funciones no se instalen o no funcionen correctamente.

   .. image:: img/imager_os.png
      :width: 90%

4. En la sección **Storage**, seleccione su **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os