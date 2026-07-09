.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _copy_sd_to_nvme_promax:

Copiar el SO de la Micro SD al SSD NVMe
==================================================================

Si tiene un SSD NVMe pero carece de un adaptador para conectarlo a su ordenador, puede optar por un tercer enfoque: instalar inicialmente el sistema en su tarjeta Micro SD. Después de que el Pironman 5 Pro MAX arranque correctamente, puede transferir el sistema de su tarjeta Micro SD a su SSD NVMe.

* Primero, necesita :ref:`install_os_sd_rpi_promax`.
* Luego, arranque e inicie sesión en su Raspberry Pi. Si no está seguro de cómo iniciar sesión, puede visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.

Complete los pasos anteriores antes de continuar con las instrucciones a continuación.

1. Habilitar PCIe
--------------------

Por defecto, el conector PCIe no está habilitado.

* Para habilitarlo, debe abrir el archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* Luego agregue la siguiente línea al archivo.

  .. code-block:: shell

    # Enable the PCIe External connector.
    dtparam=pciex1

* Existe un alias más fácil de recordar para ``pciex1``, por lo que también puede agregar ``dtparam=nvme`` al archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell

    dtparam=nvme

* Necesitará deshabilitar el retraso de arranque de PCIe para que la Raspberry Pi pueda detectar la unidad NVMe detrás del conmutador PCIe al inicio. Agregue la siguiente línea a ``/boot/firmware/config.txt``:

   .. code-block:: shell

      dtparam=pciex1_no_10s=on

* Presione ``Ctrl + X``, ``Y`` y ``Enter`` para guardar los cambios.

**BOOT_ORDER**

Si ha instalado dos unidades de sistema NVMe y necesita elegir una para arrancar,
puede modificar el ``ROOT=PARTUUID=xxxxxxxxx`` en el archivo ``/boot/firmware/cmdline.txt`` al UUID del disco desde el que desea arrancar. Puede encontrar el UUID del disco con el siguiente comando:

.. code-block:: shell

   ls /dev/disk/by-id/

.. start_copy_nvme

2. Instalar el SO en el SSD
----------------------------------------

Hay dos formas de instalar un sistema operativo en el SSD:

**Copiar el Sistema de la Tarjeta Micro SD al SSD**

#. Conecte una pantalla o acceda al escritorio de Raspberry Pi a través de VNC Viewer. Luego haga clic en **Raspberry Pi logo** -> **Accessories** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png

#. Asegúrese de seleccionar los dispositivos correctos **Copy From** y **Copy To**. Tenga cuidado de no confundirlos.

   .. image:: img/ssd_copy_from.png

#. Recuerde seleccionar "NEW Partition UUIDs" para asegurar que el sistema pueda distinguir correctamente los dispositivos, evitando conflictos de montaje y problemas de arranque.

   .. image:: img/ssd_copy_uuid.png

#. Después de la selección, haga clic en **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Se le advertirá que el contenido del SSD será borrado. Asegúrese de respaldar sus datos antes de hacer clic en Yes. Espere un momento y la copia se completará.

**Instalar el Sistema con Raspberry Pi Imager**

Si su tarjeta Micro SD tiene instalada la versión de escritorio del sistema, puede usar una herramienta de imagen (como Raspberry Pi Imager) para grabar el sistema en el SSD. Este ejemplo usa Raspberry Pi OS bookworm, pero otros sistemas podrían requerir instalar primero la herramienta de imagen.

#. Conecte una pantalla o acceda al escritorio de Raspberry Pi a través de VNC Viewer. Luego haga clic en **Raspberry Pi logo** -> **Accessories** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Inserte su tarjeta microSD en su ordenador usando un lector de tarjetas. Respalde cualquier dato importante antes de continuar.

   .. image:: img/insert_sd.png
      :width: 90%

#. Cuando se abra Raspberry Pi Imager, verá la página **Device**. Seleccione su modelo de Raspberry Pi 5 de la lista.

   .. image:: img/imager_device.png
      :width: 90%

#. Vaya a la sección **OS** y elija la opción recomendada **Raspberry Pi OS (64-bit)**.

   .. warning::

      Asegúrate de elegir una versión de **64 bits**. Si instalas un sistema de **32 bits**, algunos paquetes solo están disponibles para ``aarch64`` (64 bits) y es posible que ciertas funciones no se instalen o no funcionen correctamente.

   .. image:: img/imager_os.png
      :width: 90%

#. En la sección **Storage**, seleccione su **NVMe SSD**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_promax:

3. Configurar el arranque desde el SSD
---------------------------------------

En esta sección, configuraremos su Raspberry Pi para que arranque directamente desde un SSD NVMe, proporcionando tiempos de arranque más rápidos y un rendimiento mejorado en comparación con una tarjeta SD. Siga estos pasos cuidadosamente:

#. Primero, abra una terminal en su Raspberry Pi y ejecute el siguiente comando para acceder a la interfaz de configuración:

   .. code-block:: shell

      sudo raspi-config

#. En el menú de ``raspi-config``, use las teclas de flecha para navegar y seleccione **Advanced Options**. Presione ``Enter`` para acceder a la configuración avanzada.

   .. image:: img/nvme_open_config.png

#. Dentro de **Advanced Options**, seleccione **Boot Order**. Esta configuración le permite especificar el orden en que su Raspberry Pi busca dispositivos de arranque.

   .. image:: img/nvme_boot_order.png

#. Luego, elija **NVMe/USB boot**. Esto le dice a la Raspberry Pi que priorice el arranque desde SSD conectados por USB o unidades NVMe sobre otras opciones, como la tarjeta SD.

   .. image:: img/nvme_boot_nvme.png

#. Después de seleccionar el orden de arranque, presione **Finish** para salir de raspi-config. También puede usar la tecla **Escape** para cerrar la herramienta de configuración.

   .. image:: img/nvme_boot_ok.png

#. Para aplicar la nueva configuración de arranque, reinicie su Raspberry Pi ejecutando ``sudo reboot``.

   .. code-block:: shell

      sudo reboot

   .. image:: img/nvme_boot_reboot.png

Después de reiniciar, la Raspberry Pi debería intentar arrancar desde su SSD NVMe conectado, proporcionándole un rendimiento mejorado y mayor durabilidad para su sistema.

.. end_copy_nvme