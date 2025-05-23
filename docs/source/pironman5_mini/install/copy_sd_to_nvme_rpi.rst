.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete más a fondo en Raspberry Pi, Arduino y ESP32 junto a otros apasionados!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios de nuevos productos y avances especiales.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en promociones de temporada y sorteos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _copy_sd_to_nvme_rpi_mini:

Copiar el sistema operativo de la Micro SD al SSD NVMe
==================================================================

Si tienes un SSD NVMe pero no cuentas con un adaptador para conectarlo a tu ordenador, puedes optar por este método: primero instala el sistema en tu tarjeta Micro SD. Una vez que el Pironman 5 Mini haya arrancado correctamente, podrás transferir el sistema desde la Micro SD al SSD NVMe.

* Primero, necesitas :ref:`install_os_sd_rpi_mini`.
* Luego, inicia y accede a tu Raspberry Pi. Si no sabes cómo iniciar sesión, puedes visitar el sitio oficial de Raspberry Pi: |link_rpi_get_start|.

Completa los pasos anteriores antes de continuar con las siguientes instrucciones.


1. Activar PCIe
--------------------

Por defecto, el conector PCIe no está habilitado.

* Para activarlo, abre el archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Luego, añade la siguiente línea al archivo:

  .. code-block:: shell
  
    # Activar el conector PCIe externo.
    dtparam=pciex1
  
* Existe un alias más fácil de recordar para ``pciex1``, por lo que también puedes añadir ``dtparam=nvme`` al archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    dtparam=nvme

* La conexión está certificada para velocidades Gen 2.0 (5 GT/s), pero puedes forzarla a Gen 3.0 (10 GT/s) añadiendo las siguientes líneas:

  .. code-block:: shell
  
    # Forzar velocidad Gen 3.0
    dtparam=pciex1_gen=3
  
  .. warning::
  
    La Raspberry Pi 5 no está certificada para velocidades Gen 3.0, y la conexión con dispositivos PCIe a estas velocidades puede ser inestable.

* Presiona ``Ctrl + X``, luego ``Y`` y ``Enter`` para guardar los cambios.


2. Instalar el sistema operativo en el SSD
--------------------------------------------------

Hay dos maneras de instalar un sistema operativo en el SSD:

**Copiando el sistema desde la Micro SD al SSD**

#. Conecta una pantalla o accede al escritorio de Raspberry Pi mediante VNC Viewer. Luego haz clic en **Logo de Raspberry Pi** -> **Accesorios** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png


#. Asegúrate de seleccionar correctamente los dispositivos en **Copy From** y **Copy To**.

   .. image:: img/ssd_copy_from.png

#. Recuerda seleccionar "NEW Partition UUIDs" para evitar conflictos de montaje o errores de arranque.

   .. image:: img/ssd_copy_uuid.png

#. Tras realizar la selección, haz clic en **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Se te advertirá que el contenido del SSD se borrará. Haz una copia de seguridad si es necesario y luego confirma.

   .. image:: img/ssd_copy_erase.png

#. Espera un momento hasta que se complete la copia.

**Instalar el sistema con Raspberry Pi Imager**

Si tu Micro SD tiene una versión con escritorio del sistema, puedes usar una herramienta de grabación (como Raspberry Pi Imager) para instalar el sistema en el SSD.

#. Conecta una pantalla o accede al escritorio de Raspberry Pi con VNC Viewer. Luego haz clic en **Logo de Raspberry Pi** -> **Accesorios** -> **Imager**.

   .. image:: img/ssd_imager.png


#. Dentro de |link_rpi_imager|, haz clic en **Dispositivo Raspberry Pi** y selecciona **Raspberry Pi 5**.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Selecciona **Sistema Operativo** y elige la versión recomendada.

   .. image:: img/ssd_os.png
      :width: 90%
    
#. En **Almacenamiento**, selecciona tu SSD NVMe conectado.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Haz clic en **NEXT** y luego en **EDIT SETTINGS** para personalizar tu sistema.

   .. note::

      Si usas un monitor con tu Raspberry Pi, puedes omitir los pasos siguientes y hacer clic en 'Yes' para comenzar la instalación.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Define un **hostname** para tu Raspberry Pi.

   .. note::

      Puedes acceder a tu Raspberry Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png


#. Crea un **Nombre de usuario** y **Contraseña** para el administrador.

   .. note::

      Es importante definir credenciales únicas para proteger tu dispositivo.

   .. image:: img/os_set_username.png


#. Configura tu red inalámbrica introduciendo el **SSID** y **Contraseña**.

   .. note::

      Establece el ``Wireless LAN country`` con el código de dos letras `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

   .. image:: img/os_set_wifi.png

#. Para conectarte remotamente, **enable SSH** en la pestaña **Servicios**.

   * Usa tu usuario y contraseña definidos en la pestaña **General**.
   * O bien configura autenticación por clave pública.

   .. image:: img/os_enable_ssh.png



#. El menú **Options** permite configurar el comportamiento del Imager durante la escritura.

   .. image:: img/os_options.png

#. Tras completar la personalización del sistema, haz clic en **Save** y luego en **Yes**.

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. Si el SSD ya contiene datos, respáldalos antes de continuar. Si no es necesario, haz clic en **Yes**.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Cuando aparezca el mensaje "Write Successful", el sistema ha sido grabado y verificado correctamente. ¡Tu Raspberry Pi está lista para arrancar desde el SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _configure_boot_ssd_mini:

3. Configurar arranque desde SSD
---------------------------------------

En esta sección configurarás tu Raspberry Pi para que arranque directamente desde el SSD NVMe:

#. Abre un terminal y ejecuta el siguiente comando:

   .. code-block:: shell

      sudo raspi-config

#. En el menú de ``raspi-config``, ve a **Advanced Options** y presiona ``Enter``.

   .. image:: img/nvme_open_config.png

#. Dentro de **Advanced Options**, selecciona **Boot Order**.

   .. image:: img/nvme_boot_order.png

#. Luego selecciona **NVMe/USB boot** para priorizar el arranque desde SSD NVMe.

   .. image:: img/nvme_boot_nvme.png

#. Presiona **Finish** para salir de raspi-config o utiliza la tecla **Escape**.

   .. image:: img/nvme_boot_ok.png

#. Aplica los cambios reiniciando con ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

Después del reinicio, la Raspberry Pi debería arrancar desde tu SSD NVMe conectado, proporcionando un mejor rendimiento y mayor durabilidad.
