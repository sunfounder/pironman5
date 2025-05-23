.. _max_omv_5_max:


(Opcional) Configuración de OpenMediaVault
==============================================

.. warning::

   OpenMediaVault **no** es compatible con la instalación en Raspberry Pi OS con escritorio.

   Asegúrate de haber instalado el sistema operativo correcto y haber configurado la red.  
   Este procedimiento es similar al descrito en :ref:`max_install_os_sd_rpi`, pero al seleccionar la imagen, elige Raspberry Pi OS Lite desde la opción Raspberry Pi OS (other).

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (OMV) es un sistema operativo de almacenamiento en red (NAS) de código abierto basado en Debian Linux. Está diseñado para usuarios domésticos y pequeñas oficinas, y tiene como objetivo simplificar la gestión del almacenamiento y ofrecer funciones avanzadas de servicios de red.

Sigue estos pasos para instalar OpenMediaVault en tu Raspberry Pi:

1. Conéctate a tu Raspberry Pi mediante SSH
-------------------------------------------------------------

   Ingresa el siguiente comando en la terminal:

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Si usas Windows, emplea PuTTY u otro cliente SSH para conectarte a tu Raspberry Pi.

2. Instala OpenMediaVault
----------------------------

   Ingresa los siguientes comandos en la terminal:

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   Esto descargará y ejecutará el script de instalación de OpenMediaVault. No reinicies tu Raspberry Pi después de la instalación.

3. Accede a OpenMediaVault
-----------------------------

   Abre tu navegador e ingresa la siguiente URL:

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: Si no puedes acceder mediante esa URL, intenta con la dirección IP directamente, por ejemplo, http://192.168.1.100.

   Verás una página de inicio de sesión. Ingresa con el nombre de usuario y contraseña predeterminados:  
   Usuario: ``admin``  
   Contraseña: ``openmediavault``

   .. image:: img/omv/omv-login.png

   Una vez dentro, verás la interfaz principal de OpenMediaVault.

   .. image:: img/omv/omv-main.png

   Ahora que has accedido correctamente, puedes comenzar a configurar y administrar tu almacenamiento.



6. Configura RAID (Opcional)
---------------------------------------

   RAID NVMe es una solución que combina múltiples SSD NVMe usando tecnología RAID, diseñada para maximizar el rendimiento del protocolo NVMe y ofrecer redundancia y mayor rendimiento. Los modos más comunes incluyen RAID 0, 1, 5, 10. Para dos unidades NVMe, los más utilizados son RAID 0 y RAID 1.

   * RAID 0 divide los datos en bloques y los distribuye entre varios discos para lograr mayor velocidad. No ofrece redundancia, y si falla un disco, se pierde toda la información.

   * RAID 1 crea una copia exacta de los datos en ambos discos, ofreciendo protección contra fallos. La velocidad depende de un solo disco. Si uno falla, el otro puede seguir operando.

   .. note:: Se requieren al menos 2 discos montados para usar RAID 0 o RAID 1. En RAID 0, la capacidad total será la suma de ambos discos. En RAID 1, la capacidad será igual a la del disco más pequeño.

   1. En el menú ``System``, haz clic en ``Plugins``, busca ``openmediavault-md`` y haz clic para instalarlo.

   .. image:: img/omv/omv-raid-1.png

   2. En el menú ``Storage``, selecciona ``Disks`` y borra dos SSD.

   .. image:: img/omv/omv-raid-2.png

   3. Esta acción eliminará todos los datos. Asegúrate de hacer una copia de seguridad antes.

   .. image:: img/omv/omv-raid-3.png

   4. Selecciona ``QUICK`` como modo de borrado.

   .. image:: img/omv/omv-raid-4.png

   5. Ve a la pestaña ``Multiple Device`` y haz clic en ``Create``.

   .. image:: img/omv/omv-raid-5.png

   6. Elige ``Stripe (RAID 0)`` o ``Mirror (RAID 1)``, selecciona los discos, haz clic en ``Save`` y espera a que se configure.

   .. image:: img/omv/omv-raid-6.png

   .. note:: Si aparece un error 500 - Internal Server Error, intenta reiniciar OMV.

   7. Haz clic en ``Apply`` para aplicar los cambios.

   .. image:: img/omv/omv-raid-7.png

   8. Espera a que el estado del RAID alcance ``100%``.

   .. image:: img/omv/omv-raid-8.png

   9. Una vez completado, tus discos estarán en RAID 0 o RAID 1 y listos para usarse como una única unidad.

5. Configura el Almacenamiento
----------------------------------

   En la interfaz principal, ve a ``Storage`` > ``Disks`` para verificar que tus discos estén conectados.

   .. image:: img/omv/omv-disk.png

   1. En el menú lateral, selecciona ``File System``. Crea y monta un nuevo sistema de archivos usando ``ext4``.

   .. image:: img/omv/omv-mount.png

   2. Selecciona el dispositivo y haz clic en Save.

   .. note:: Si ya creaste RAID, aparecerá en la lista como un dispositivo. Selecciónalo y guarda.

   .. image:: img/omv/omv-mount-2.png

   3. Aparecerá una ventana indicando que se está creando el sistema de archivos.

   .. image:: img/omv/omv-mount-3.png

   4. Cuando finalice, ve a la pestaña ``Mount``, selecciona el sistema de archivos recién creado y móntalo.

   .. image:: img/omv/omv-mount-4.png

   .. note:: Si usas dos discos sin RAID, repite los pasos para montar el segundo.

   5. Luego de montar, haz clic en Apply. Ya podrás ver los datos de tus discos en el sistema de archivos.

   .. image:: img/omv/omv-mount-5.png

   Ya has configurado correctamente OpenMediaVault y montado tus discos.


6. Crear una Carpeta Compartida
---------------------------------------

   1. En ``Storage``, ve a la pestaña ``Shared Folders`` y haz clic en ``Create``.

   .. image:: img/omv/omv-share-1.png

   2. Ingresa el nombre, selecciona el disco, la ruta y los permisos. Luego haz clic en ``Save``.

   .. image:: img/omv/omv-share-2.png

   3. Verifica que se haya creado correctamente y haz clic en Apply.

   .. image:: img/omv/omv-share-3.png

   Has creado una carpeta compartida con éxito.


7. Crear un Nuevo Usuario
-------------------------------

   Para acceder a la carpeta, es necesario crear un nuevo usuario. Por favor, sigue estos pasos:

   1. En la sección ``User``, haz clic en ``Create``.

   .. image:: img/omv/omv-user-1.png

   2. En la página ``Create User``, introduce el nombre de usuario y la contraseña del nuevo usuario, luego haz clic en el botón ``Save``.

   .. image:: img/omv/omv-user-2.png

   Has creado un nuevo usuario correctamente.


8. Asignar Permisos al Usuario
---------------------------------------

   1. En ``Shared Folders``, selecciona la carpeta creada y haz clic en ``Permissions``.

   .. image:: img/omv/omv-user-3.png

   2. En la página ``Permissions``, configura los permisos correspondientes. Luego haz clic en el botón ``Save``.

   .. image:: img/omv/omv-user-4.png

   3. Finalmente, haz clic en ``Apply``.

   .. image:: img/omv/omv-user-5.png

   Ahora puedes acceder a la carpeta compartida con el nuevo usuario.


9. Configurar el Servicio SMB
----------------------------------

   1. Ve a ``Services`` > ``SMB/CIFS`` > pestaña ``Setting``. Marca ``Enable`` y haz clic en ``Save``.

   .. image:: img/omv/omv-smb-1.png

   2. Haz clic en ``Apply`` para aplicar los cambios.

   .. image:: img/omv/omv-smb-2.png

   3. En la pestaña ``Shares``, haz clic en ``Create``.

   .. image:: img/omv/omv-smb-3.png

   4. Selecciona la ruta de la carpeta compartida, configura las opciones necesarias y haz clic en ``Save``.

   .. image:: img/omv/omv-smb-4.png

   5. Haz clic en ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   Has configurado SMB exitosamente y ya puedes acceder a la carpeta compartida.


10. Acceder a la Carpeta Compartida en Windows
-----------------------------------------------

   1. Abre ``This PC`` y haz clic en ``Map network drive``.

   .. image:: img/omv/omv-network-location-1.png

   2. Ingresa la IP del Raspberry Pi, por ejemplo ``\\192.168.1.100\`` o ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Haz clic en el botón explorar y selecciona la carpeta compartida. Ingresa el usuario y contraseña.

   .. image:: img/omv/omv-network-location-3.png

   4. Marca “Conectar al iniciar sesión” y haz clic en ``Finish``.

   .. image:: img/omv/omv-network-location-4.png

   5. Ya puedes acceder a tu carpeta compartida NAS.

   .. image:: img/omv/omv-network-location-5.png

10. Acceder a la Carpeta Compartida en Mac
-------------------------------------------

   1. En el menú ``Ir``, selecciona ``Connect to Server``.

   .. image:: img/omv/omv-mac-1.png

   2. Ingresa ``smb://192.168.1.100`` o ``smb://pi.local``.

   .. image:: img/omv/omv-mac-2.png

   3. Haz clic en ``Connect``.

   .. image:: img/omv/omv-mac-3.png

   4. Introduce el usuario y contraseña creados previamente. Haz clic en ``Connect``.

   .. image:: img/omv/omv-mac-4.png

   5. Ya puedes acceder a tu carpeta compartida NAS.

   .. image:: img/omv/omv-mac-5.png
