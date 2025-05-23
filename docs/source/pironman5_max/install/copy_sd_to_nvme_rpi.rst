.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con el apoyo de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios y novedades de productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_copy_sd_to_nvme_rpi:

Copiar el sistema operativo de la tarjeta Micro SD al SSD NVMe
==================================================================

Si tienes un SSD NVMe pero no cuentas con un adaptador para conectarlo a tu ordenador, puedes optar por este método alternativo: primero instala el sistema en tu tarjeta Micro SD. Una vez que el Pironman 5 haya arrancado correctamente, podrás transferir el sistema desde la tarjeta Micro SD al SSD NVMe.

* Primero, debes seguir los pasos de :ref:`max_install_os_sd_rpi`.
* Luego, inicia sesión en tu Raspberry Pi. Si no sabes cómo hacerlo, puedes visitar el sitio oficial de Raspberry Pi: |link_rpi_get_start|.

Completa estos pasos antes de continuar con las instrucciones siguientes.


1. Habilitar PCIe
--------------------

Por defecto, el conector PCIe no está habilitado.

* Para activarlo, abre el archivo ``/boot/firmware/config.txt``:

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt

* Luego añade la siguiente línea al archivo:

  .. code-block:: shell
  
    # Habilitar el conector PCIe externo.
    dtparam=pciex1

* Existe un alias más fácil de recordar para ``pciex1``, por lo que también puedes añadir ``dtparam=nvme`` al archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell

    dtparam=nvme

* La conexión está certificada para velocidades Gen 2.0 (5 GT/s), pero puedes forzar Gen 3.0 (10 GT/s) añadiendo lo siguiente:

  .. code-block:: shell
  
    # Forzar velocidad Gen 3.0
    dtparam=pciex1_gen=3

  .. warning::

    La Raspberry Pi 5 no está certificada para velocidades Gen 3.0 y las conexiones a esa velocidad podrían ser inestables.

* También debes desactivar la demora de arranque del PCIe para que la Raspberry Pi detecte la unidad NVMe conectada detrás del Switch PCIe. Añade esta línea:

  .. code-block:: shell

      dtparam=pciex1_no_10s=on


* Pulsa ``Ctrl + X``, luego ``Y`` y ``Enter`` para guardar los cambios.


**BOOT_ORDER**

Si tienes dos discos NVMe con sistema operativo instalado y necesitas elegir cuál arrancar, puedes modificar el valor de ``ROOT=PARTUUID=xxxxxxxxx`` en el archivo ``/boot/firmware/cmdline.txt`` con la UUID del disco deseado. Usa este comando para obtener la UUID:

.. code-block:: shell

   ls /dev/disk/by-id/


2. Instalar el sistema operativo en el SSD
-----------------------------------------------

Hay dos formas de instalar un sistema operativo en el SSD:

**Copiar el sistema desde la tarjeta Micro SD al SSD**

#. Conecta una pantalla o accede al escritorio de Raspberry Pi mediante VNC Viewer. Luego haz clic en **Raspberry Pi logo** -> **Accessories** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png


#. Asegúrate de seleccionar correctamente los dispositivos **Copy From** y **Copy To**. No los confundas.

   .. image:: img/ssd_copy_from.png

#. Marca la opción "NEW Partition UUIDs" para evitar conflictos de montaje o errores de arranque.

   .. image:: img/ssd_copy_uuid.png

#. Luego haz clic en **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Se te advertirá que el contenido del SSD será borrado. Haz una copia de seguridad antes de continuar.

   .. image:: img/ssd_copy_erase.png

#. Espera unos minutos hasta que finalice la copia.


**Instalar el sistema usando Raspberry Pi Imager**

Si tu tarjeta Micro SD tiene un sistema con escritorio, puedes usar una herramienta como Raspberry Pi Imager para grabar la imagen en el SSD. En este ejemplo se usa Raspberry Pi OS Bookworm, pero otros sistemas pueden requerir que primero instales la herramienta.

#. Conecta una pantalla o accede al escritorio con VNC Viewer. Luego ve a **Raspberry Pi logo** -> **Accessories** -> **Imager**.

   .. image:: img/ssd_imager.png


#. Dentro de |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5**.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Selecciona **Operating System** y escoge la versión recomendada.

   .. image:: img/ssd_os.png
      :width: 90%

#. En la opción **Storage**, selecciona tu SSD NVMe conectado.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Haz clic en **NEXT** y luego en **EDIT SETTINGS** para personalizar tu sistema.

   .. note::

      Si tienes una pantalla conectada a tu Raspberry Pi, puedes omitir los siguientes pasos y hacer clic en 'Yes' para iniciar la instalación. Podrás ajustar la configuración más adelante.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Asigna un **hostname** a tu Raspberry Pi.

   .. note::

      El nombre del host es el identificador de red de tu Raspberry Pi. Puedes acceder con ``<hostname>.local`` o ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png


#. Crea un **Nombre de usuario** y una **Contraseña** para la cuenta de administrador.

   .. note::

      Es importante establecer un usuario y contraseña únicos para proteger tu sistema, ya que no hay una contraseña predeterminada.

   .. image:: img/os_set_username.png


#. Configura tu red Wi-Fi ingresando el **SSID** y la **Contraseña**.

   .. note::

      Establece el ``Wireless LAN country`` con el código de dos letras `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

   .. image:: img/os_set_wifi.png

#. Para conectarte de forma remota, **activa SSH** desde la pestaña **Services**.

   * Para **autenticación por contraseña**, usa los datos del apartado **General**.
   * Para autenticación con clave pública, selecciona "Allow public-key authentication only". Si no tienes una clave RSA, puedes generar una con "Run SSH-keygen".

   .. image:: img/os_enable_ssh.png



#. En el menú **Options**, puedes configurar el comportamiento del Imager: reproducir sonido al terminar, expulsar la unidad o enviar telemetría.

   .. image:: img/os_options.png

#. Una vez que hayas personalizado tu sistema, haz clic en **Save** y luego en **Yes** para aplicar los cambios.

   .. image:: img/os_click_yes.png
      :width: 90%

#. Si tu SSD NVMe contiene datos, respáldalos antes de continuar. Haz clic en **Yes** para continuar sin copia de seguridad.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Cuando veas el mensaje "Write Successful", significa que la imagen fue escrita y verificada. ¡Tu Raspberry Pi ya está lista para arrancar desde el SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _max_configure_boot_ssd:

3. Configurar el arranque desde SSD
---------------------------------------

En esta sección configurarás tu Raspberry Pi para que arranque directamente desde un SSD NVMe, mejorando los tiempos de inicio y el rendimiento general. Sigue estos pasos:

#. Abre una terminal y ejecuta el siguiente comando para acceder al menú de configuración:

   .. code-block:: shell

      sudo raspi-config

#. En el menú ``raspi-config``, usa las teclas de dirección para seleccionar **Advanced Options** y pulsa ``Enter``.

   .. image:: img/nvme_open_config.png

#. Dentro de **Advanced Options**, selecciona **Boot Order** para definir el orden de arranque de los dispositivos.

   .. image:: img/nvme_boot_order.png

#. Selecciona **NVMe/USB boot** para priorizar el arranque desde SSDs conectados por USB o NVMe.

   .. image:: img/nvme_boot_nvme.png

#. Después de elegir el orden de arranque, selecciona **Finish** para salir del menú, o pulsa **Escape** para cerrar la herramienta.

   .. image:: img/nvme_boot_ok.png

#. Para aplicar la nueva configuración de arranque, reinicia tu Raspberry Pi ejecutando ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

Después del reinicio, tu Raspberry Pi intentará arrancar desde el SSD NVMe conectado, brindando mayor velocidad y durabilidad al sistema.


