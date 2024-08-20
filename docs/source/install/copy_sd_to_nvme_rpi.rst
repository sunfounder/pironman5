.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _copy_sd_to_nvme_rpi:

Copiar el Sistema Operativo de Micro SD a NVMe SSD
==================================================================

Si tienes un NVMe SSD pero no cuentas con un adaptador para conectarlo a tu computadora, puedes optar por un enfoque alternativo: instala el sistema inicialmente en tu tarjeta Micro SD. Después de que el Pironman 5 haya iniciado con éxito, puedes transferir el sistema desde tu tarjeta Micro SD a tu NVMe SSD.

* Primero, necesitas :ref:`install_os_sd_rpi`.
* Luego, inicia sesión en tu Raspberry Pi. Si no sabes cómo iniciar sesión, puedes visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.

Completa los pasos anteriores antes de continuar con las siguientes instrucciones.


1. Habilitar PCIe
-----------------------

Por defecto, el conector PCIe no está habilitado.

* Para habilitarlo, debes abrir el archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Luego, añade la siguiente línea al archivo. 

  .. code-block:: shell
  
    # Habilitar el conector PCIe externo.
    dtparam=pciex1
  
* Existe un alias más fácil de recordar para ``pciex1``, por lo que también puedes añadir ``dtparam=nvme`` al archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    dtparam=nvme

* La conexión está certificada para velocidades Gen 2.0 (5 GT/seg), pero puedes forzarla a Gen 3.0 (10 GT/seg) si añades las siguientes líneas a tu archivo ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    # Forzar velocidades Gen 3.0
    dtparam=pciex1_gen=3
  
  .. warning::
  
    El Raspberry Pi 5 no está certificado para velocidades Gen 3.0, y las conexiones a dispositivos PCIe a estas velocidades pueden ser inestables.

* Presiona ``Ctrl + X``, ``Y`` y ``Enter`` para guardar los cambios.


2. Instalar el Sistema Operativo en el SSD
------------------------------------------------

Existen dos maneras de instalar un sistema operativo en el SSD:

**Copiando el Sistema desde la Tarjeta Micro SD al SSD**

#. Conecta una pantalla o accede al escritorio de Raspberry Pi a través de VNC Viewer. Luego, haz clic en **Logotipo de Raspberry Pi** -> **Accesorios** -> **Copiador de Tarjetas SD**.

   .. image:: img/ssd_copy.png
      
    
#. Asegúrate de seleccionar los dispositivos correctos en **Copiar Desde** y **Copiar A**. Ten cuidado de no confundirlos.

   .. image:: img/ssd_copy_from.png
      
#. Después de la selección, haz clic en **Iniciar**.

   .. image:: img/ssd_copy_start.png

#. Se te advertirá que el contenido del SSD será borrado. Asegúrate de hacer una copia de seguridad de tus datos antes de hacer clic en Sí.

   .. image:: img/ssd_copy_erase.png

#. Espera un tiempo, y la copia se completará.


**Instalar el Sistema con Raspberry Pi Imager**

Si tu tarjeta Micro SD tiene una versión de escritorio del sistema instalado, puedes utilizar una herramienta de imágenes (como Raspberry Pi Imager) para grabar el sistema en el SSD. Este ejemplo utiliza Raspberry Pi OS bookworm, pero otros sistemas pueden requerir la instalación de la herramienta de imágenes primero.

#. Conecta una pantalla o accede al escritorio de Raspberry Pi a través de VNC Viewer. Luego, haz clic en **Logotipo de Raspberry Pi** -> **Accesorios** -> **Imager**.

   .. image:: img/ssd_imager.png

      
#. Dentro del |link_rpi_imager|, haz clic en **Dispositivo Raspberry Pi** y selecciona el modelo **Raspberry Pi 5** de la lista desplegable.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Selecciona **Sistema Operativo** y opta por la versión recomendada del sistema operativo.

   .. image:: img/ssd_os.png
      :width: 90%
    
#. En la opción **Almacenamiento**, selecciona tu NVMe SSD insertado.

   .. image:: img/nvme_storage.png
      :width: 90%
    
#. Haz clic en **SIGUIENTE** y luego en **EDITAR CONFIGURACIÓN** para personalizar la configuración de tu sistema operativo. 

   .. note::

      Si tienes un monitor para tu Raspberry Pi, puedes omitir los próximos pasos y hacer clic en 'Sí' para comenzar la instalación. Ajusta otras configuraciones más adelante en el monitor.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Define un **nombre de host** para tu Raspberry Pi.

   .. note::

      El nombre de host es el identificador de red de tu Raspberry Pi. Puedes acceder a tu Pi usando ``<nombre_host>.local`` o ``<nombre_host>.lan``.

   .. image:: img/os_set_hostname.png
      

#. Crea un **Nombre de Usuario** y **Contraseña** para la cuenta de administrador de Raspberry Pi.

   .. note::

      Establecer un nombre de usuario y contraseña únicos es fundamental para proteger tu Raspberry Pi, que carece de una contraseña predeterminada.

   .. image:: img/os_set_username.png
      

#. Configura la red LAN inalámbrica proporcionando el **SSID** y la **Contraseña** de tu red.

   .. note::

      Establece el ``país de la LAN inalámbrica`` al código de dos letras  `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

   .. image:: img/os_set_wifi.png

#. Para conectarte de forma remota a tu Raspberry Pi, **habilita SSH** en la pestaña **Servicios**.

   * Para **autenticación con contraseña**, usa el nombre de usuario y contraseña de la pestaña **General**.
   * Para autenticación con clave pública, elige "Permitir solo autenticación con clave pública". Si tienes una clave RSA, se usará. Si no, haz clic en "Ejecutar SSH-keygen" para generar un nuevo par de claves.

   .. image:: img/os_enable_ssh.png

      

#. El menú **Opciones** te permite configurar el comportamiento de Imager durante una escritura, incluyendo reproducir sonido cuando termine, expulsar el medio cuando termine y habilitar la telemetría.

   .. image:: img/os_options.png
    
#. Cuando hayas terminado de ingresar la personalización del sistema operativo, haz clic en **Guardar** para guardar tu personalización. Luego, haz clic en **Sí** para aplicarlos al escribir la imagen.

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. Si el NVMe SSD contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar la pérdida de datos. Procede haciendo clic en **Sí** si no se necesita una copia de seguridad.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Cuando veas el mensaje emergente "Escritura Exitosa", tu imagen ha sido completamente escrita y verificada. ¡Ahora estás listo para iniciar una Raspberry Pi desde el NVMe SSD!

   .. image:: img/nvme_install_finish.png
      :width: 90%
      

.. _configure_boot_ssd:

3. Configurar el inicio desde el SSD
---------------------------------------

* Para actualizar el firmware de tu Raspberry Pi a la versión más reciente, utiliza ``rpi-update``.

  .. code-block:: shell

    sudo rpi-update

* Para habilitar el soporte de inicio, necesitas cambiar el ``BOOT_ORDER`` en la configuración del bootloader. Edita la configuración de la EEPROM mediante:

  .. code-block:: shell
  
    sudo rpi-eeprom-config --edit
  
* Luego, cambia la línea ``BOOT_ORDER`` de la siguiente manera. ``0xf416``: Intentar primero el NVMe SSD, seguido por la tarjeta SD y luego USB.

  .. code-block:: shell
  
    BOOT_ORDER=0xf416

  .. note::
    
    Simplemente cambia el orden en que arranca el Raspberry Pi, pero no elimines otras formas de iniciar. Esto asegura que siempre arranque correctamente.


La configuración ``BOOT_ORDER`` permite una configuración flexible de la prioridad de los diferentes modos de inicio. Se representa como un entero sin signo de 32 bits donde cada nibble representa un modo de inicio. Los modos de inicio se intentan en el orden del nibble menos significativo al más significativo.
La propiedad ``BOOT_ORDER`` define la secuencia de los diferentes modos de inicio. Se lee de derecha a izquierda y se pueden definir hasta ocho dígitos.

.. image:: img/boot_order.png
      :width: 90%
      

* ``0xf41``: Intentar primero SD, seguido por USB-MSD y luego repetir (predeterminado si ``BOOT_ORDER`` está vacío).
* ``0xf14``: Intentar primero USB, seguido por SD y luego repetir.

* Una vez que la actualización esté completa, reinicia tu Raspberry Pi para que estos cambios surtan efecto.

.. code-block:: shell

    sudo reboot

