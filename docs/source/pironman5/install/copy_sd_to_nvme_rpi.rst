.. note:: 

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios de nuevos productos y contenido exclusivo.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _copy_sd_to_nvme_5:

Copiar el sistema operativo desde una tarjeta Micro SD a un SSD NVMe
===========================================================================

Si no dispones de un adaptador NVMe, primero puedes instalar el sistema operativo en una **tarjeta Micro SD** y, una vez que el Pironman 5 haya iniciado correctamente, copiarlo al **SSD NVMe**.

* Primero, completa :ref:`install_os_sd_rpi_5`.
* Luego, inicia y accede a tu Raspberry Pi. Para obtener ayuda sobre el inicio de sesión, consulta: |link_rpi_get_start|.

Completa los pasos anteriores antes de continuar.


1. Habilitar PCIe
--------------------

De forma predeterminada, el conector PCIe no está habilitado.

* Para habilitarlo, abre el archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Luego, añade la siguiente línea al archivo.

  .. code-block:: shell
  
    # Habilitar el conector externo PCIe.
    dtparam=pciex1
  
* Existe un alias más fácil de recordar para ``pciex1``, por lo que también puedes añadir ``dtparam=nvme`` al archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    dtparam=nvme

* La conexión está certificada para velocidades Gen 2.0 (5 GT/seg), pero puedes forzarla a Gen 3.0 (10 GT/seg) si añades las siguientes líneas a tu ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    # Forzar velocidades Gen 3.0
    dtparam=pciex1_gen=3
  
  .. warning::
  
    La Raspberry Pi 5 no está certificada para velocidades Gen 3.0, y las conexiones a dispositivos PCIe a estas velocidades pueden ser inestables.

* Pulsa ``Ctrl + X``, ``Y`` y ``Enter`` para guardar los cambios.

.. start_copy_nvme

2. Instalar el sistema operativo en el SSD
---------------------------------------------------

Hay dos formas de instalar un sistema operativo en el SSD:

**Copiar el sistema desde la tarjeta Micro SD al SSD**

#. Conecta una pantalla o accede al escritorio de la Raspberry Pi mediante VNC Viewer. Luego haz clic en **logotipo de Raspberry Pi** -> **Accessories** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png
      
    
#. Asegúrate de seleccionar correctamente los dispositivos **Copy From** y **Copy To**. Ten cuidado de no confundirlos.

   .. image:: img/ssd_copy_from.png
      
#. Recuerda seleccionar "NEW Partition UUIDs" para garantizar que el sistema pueda distinguir correctamente los dispositivos y evitar conflictos de montaje y problemas de arranque.

   .. image:: img/ssd_copy_uuid.png
    
#. Tras la selección, haz clic en **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Se te advertirá de que el contenido del SSD se borrará. Asegúrate de hacer una copia de seguridad de tus datos antes de hacer clic en Yes. Espera un momento y el proceso de copia se completará.

**Instalar el sistema con Raspberry Pi Imager**

Si tu tarjeta Micro SD tiene instalada una versión de escritorio del sistema, puedes usar una herramienta de grabación (como Raspberry Pi Imager) para instalar el sistema en el SSD. Este ejemplo utiliza Raspberry Pi OS bookworm, pero otros sistemas pueden requerir instalar primero la herramienta de grabación.

#. Conecta una pantalla o accede al escritorio de la Raspberry Pi mediante VNC Viewer. Luego haz clic en **logotipo de Raspberry Pi** -> **Accessories** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Inserta tu tarjeta Micro SD en el ordenador usando un lector de tarjetas. Haz una copia de seguridad de cualquier dato importante antes de continuar.

   .. image:: img/insert_sd.png
      :width: 90%

#. Cuando se abra Raspberry Pi Imager, verás la página **Device**. Selecciona tu modelo de Raspberry Pi 5 de la lista.

   .. image:: img/imager_device.png
      :width: 90%

#. Ve a la sección **OS** y elige la opción recomendada **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

#. En la sección **Storage**, selecciona tu **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_5:

3. Configurar el arranque desde el SSD
---------------------------------------

En esta sección, configuraremos tu Raspberry Pi para que arranque directamente desde un SSD NVMe, lo que proporciona tiempos de arranque más rápidos y un mejor rendimiento en comparación con una tarjeta SD. Sigue estos pasos cuidadosamente:

#. Primero, abre una terminal en tu Raspberry Pi y ejecuta el siguiente comando para acceder a la interfaz de configuración:.

   .. code-block:: shell

      sudo raspi-config

#. En el menú ``raspi-config``, usa las teclas de flecha para navegar y selecciona **Advanced Options**. Pulsa ``Enter`` para acceder a la configuración avanzada.

   .. image:: img/nvme_open_config.png

#. Dentro de **Advanced Options**, selecciona **Boot Order**. Esta opción te permite especificar el orden en el que tu Raspberry Pi busca dispositivos de arranque.

   .. image:: img/nvme_boot_order.png

#. A continuación, elige **NVMe/USB boot**. Esto indica a la Raspberry Pi que priorice el arranque desde SSDs conectados por USB o unidades NVMe sobre otras opciones, como la tarjeta SD.

   .. image:: img/nvme_boot_nvme.png

#. Después de seleccionar el orden de arranque, pulsa **Finish** para salir de raspi-config. También puedes usar la tecla **Escape** para cerrar la herramienta de configuración.

   .. image:: img/nvme_boot_ok.png

#. Para aplicar la nueva configuración de arranque, reinicia tu Raspberry Pi ejecutando ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

Después de reiniciar, la Raspberry Pi debería intentar arrancar desde el SSD NVMe conectado, ofreciéndote un mayor rendimiento y durabilidad para tu sistema.

.. end_copy_nvme
