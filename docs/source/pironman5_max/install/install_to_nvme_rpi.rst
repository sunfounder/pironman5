.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_rpi_max:

Instalar el sistema operativo en un SSD NVMe
======================================================

Si estás utilizando un SSD NVMe y dispones de un adaptador para conectar el SSD NVMe a tu ordenador para la instalación del sistema, puedes seguir el siguiente tutorial para una instalación rápida.

**Componentes necesarios**

* Un ordenador personal
* Un SSD NVMe
* Un adaptador NVMe a USB
* Tarjeta Micro SD y lector


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_max:


2. Actualizar el bootloader
--------------------------------

Primero, actualiza el bootloader de la Raspberry Pi 5 para que intente arrancar primero desde **NVMe**, luego desde **USB** y, por último, desde la **tarjeta SD**.

.. note::

    Se recomienda utilizar una **tarjeta Micro SD de repuesto** para este paso.
    
    - Método 1 (recomendado): Graba el bootloader en una tarjeta Micro SD, insértala en la Raspberry Pi y arranca una vez para aplicar la configuración.
    - Método 2: Graba el bootloader directamente en el SSD NVMe. Después, conecta el NVMe a un ordenador para instalar el sistema operativo y, a continuación, vuelve a colocarlo en la Raspberry Pi.

#. Inserta la **tarjeta Micro SD de repuesto o el SSD NVMe** en tu ordenador usando un lector de tarjetas o un adaptador.

#. Cuando se abra Raspberry Pi Imager, verás la página **Device**. Selecciona tu modelo de **Raspberry Pi 5** de la lista.

   .. image:: img/imager_device.png
      :width: 90%

#. Haz clic en **OS**.

   * Desplázate hacia abajo y selecciona **Misc utility images**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Selecciona **Bootloader (Pi 5 family)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Elige **NVMe/USB Boot** para establecer el orden de arranque y, a continuación, haz clic en **NEXT**.

     .. image:: img/nvme_boot.png
        :width: 90%


#. En **Storage**, selecciona la tarjeta Micro SD o el SSD NVMe correctos y haz clic en **NEXT**.

   .. note::

      Asegúrate de que el dispositivo correcto esté seleccionado. Desconecta otros dispositivos de almacenamiento si es necesario.

   .. image:: img/imager_storage.png
      :width: 90%


#. Revisa la configuración y haz clic en **WRITE** para comenzar.

   .. image:: img/nvme_write.png
      :width: 90%

#. Confirma la advertencia y permite que Raspberry Pi Imager borre y escriba el bootloader.

   .. image:: img/imager_erase.png
      :width: 90%

#. Espera hasta que aparezca **Write complete!** y, a continuación, retira de forma segura el dispositivo de almacenamiento.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Inserta la tarjeta Micro SD en la Raspberry Pi y enciéndela una vez para aplicar la actualización del bootloader.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Espera al menos **10 segundos** después de que la Raspberry Pi termine de arrancar y, a continuación, apágala y retira la tarjeta Micro SD o el SSD NVMe.

La Raspberry Pi 5 ya está lista para arrancar desde **NVMe**.

.. end_update_bootloader

3. Instalar el sistema operativo en el SSD NVMe
--------------------------------------------------------

Ahora puedes instalar el sistema operativo en tu SSD NVMe.

#. Inserta el **SSD NVMe** en tu ordenador utilizando un adaptador.

2. Cuando se abra Raspberry Pi Imager, verás la página **Device**. Selecciona tu modelo de **Raspberry Pi 5** de la lista.

   .. image:: img/imager_device.png
      :width: 90%

3. Ve a la sección **OS** y elige la opción recomendada **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

4. En la sección **Storage**, selecciona tu **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

