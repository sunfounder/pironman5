.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _max_omv_5_max:

Configuración de OpenMediaVault
=====================================

.. warning::

   OpenMediaVault **no** admite la instalación en el escritorio de Raspberry Pi OS.

   ⚠️ **Solo se admiten las versiones 11 (Bullseye) y 12 (Bookworm) de Raspberry Pi OS Lite.**

   Asegúrate de haber instalado el sistema operativo correcto y configurado la red.  
   El procedimiento aquí es consistente con :ref:`install_os_sd_rpi_max`, pero al seleccionar una imagen, elige Raspberry Pi OS Lite de Raspberry Pi OS (other).

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (abreviado como OMV) es un sistema operativo de Almacenamiento Conectado en Red (NAS) de código abierto basado en Debian Linux, diseñado para usuarios domésticos y entornos de pequeñas oficinas, con el objetivo de simplificar la gestión del almacenamiento y proporcionar ricas funciones de servicios de red.

Sigue estos pasos para instalar OpenMediaVault en tu Raspberry Pi:

1. Conectarse a tu Raspberry Pi usando SSH
-----------------------------------------------------------

   Introduce el siguiente comando en la terminal:

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Si estás usando Windows, utiliza PuTTY u otro cliente SSH para conectarte a tu Raspberry Pi.

2. Instalar OpenMediaVault
----------------------------

   Introduce el siguiente comando en la terminal:

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   Esto descargará y ejecutará el script de instalación de OpenMediaVault. No reinicies tu Raspberry Pi después de la instalación.

3. Acceder a OpenMediaVault
-----------------------------

   Introduce la siguiente URL en tu navegador para acceder a OpenMediaVault:

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: Si no puedes acceder a la URL anterior, intenta usar la dirección IP en su lugar, por ejemplo, http://192.168.1.100.

   Verás una página de inicio de sesión. Inicia sesión usando el nombre de usuario y contraseña predeterminados. El nombre de usuario por defecto es ``admin`` y la contraseña es ``openmediavault``.

   .. image:: img/omv/omv-login.png

   Después de iniciar sesión, verás la interfaz principal de OpenMediaVault.

   .. image:: img/omv/omv-main.png

   Ahora que has instalado y accedido correctamente a OpenMediaVault, puedes comenzar a configurar y gestionar tu almacenamiento.


4. Configurar RAID (Opcional)
---------------------------------------

   El RAID NVMe es una solución de almacenamiento que combina múltiples SSD NVMe utilizando la tecnología RAID, con el objetivo de maximizar el alto rendimiento del protocolo NVMe y las funciones de redundancia/mejora de rendimiento de RAID. Los modos comunes incluyen RAID 0, 1, 5, 10, etc. Para dos SSD NVMe, los modos más utilizados son RAID 0 y RAID 1.

   * RAID 0 es una tecnología de "striping" que divide los datos en múltiples franjas y las distribuye entre varios discos duros, logrando así mayores velocidades de lectura/escritura. RAID 0 no proporciona protección de redundancia, por lo que si falla uno de los discos, se perderán todos los datos.

   * RAID 1 es una tecnología de duplicación que copia los datos en varios discos duros, proporcionando así protección de redundancia. La velocidad de lectura/escritura de RAID 1 depende de la velocidad de un solo disco, ya que los datos deben leerse desde múltiples discos. Si uno de los discos falla, los demás pueden seguir proporcionando los datos.

   .. note:: Debes montar al menos 2 discos para RAID 0 o RAID 1. En RAID 0, la capacidad del volumen RAID será la suma de las capacidades de todos los discos. En RAID 1, la capacidad del volumen RAID será igual a la capacidad del disco más pequeño. 

   1. En el menú ``System`` haz clic en la opción ``Plugins``, busca el plugin ``openmediavault-md`` e instálalo.

   .. image:: img/omv/omv-raid-1.png

   2. En el menú ``Storage`` haz clic en la opción ``Disks`` y borra dos SSD.
   
   .. image:: img/omv/omv-raid-2.png

   3. Ten en cuenta que esta acción borrará todos los datos de los discos duros, asegúrate de haber hecho una copia de seguridad de todos los datos importantes.

   .. image:: img/omv/omv-raid-3.png

   4. Selecciona el modo de borrado ``QUICK``, que es suficiente.

   .. image:: img/omv/omv-raid-4.png

   5. Entra en la pestaña ``Multiple Device`` y haz clic en ``Create``.

   .. image:: img/omv/omv-raid-5.png

   6. En la opción Level, puedes elegir Stripe (RAID 0) o Mirror (RAID 1). En la opción Devices, selecciona los discos duros que acabas de borrar. Haz clic en ``Save`` y espera a que se complete la configuración RAID.

   .. image:: img/omv/omv-raid-6.png

   .. note:: Si aparece un informe de error (500 - Internal Server Error), intenta reiniciar el sistema OMV.

   7. Aplica la configuración haciendo clic en el botón ``Apply``.

   .. image:: img/omv/omv-raid-7.png

   8. Después de que se complete la configuración RAID, espera a que el estado del RAID llegue al ``100%``.

   .. image:: img/omv/omv-raid-8.png

   9. Una vez completada la configuración RAID, tus discos estarán en una configuración RAID 0 o RAID 1, y podrás utilizarlos como un único dispositivo de almacenamiento.

5. Configurar Almacenamiento
-------------------------------

   En la interfaz principal de OpenMediaVault, haz clic en la opción ``Storage`` en el menú lateral izquierdo. En la página ``Storage``, haz clic en la pestaña ``Disks``. En la página ``Disks``, verás todos los discos en tu Raspberry Pi. Asegúrate de que tu NVMe PIP tenga un disco duro conectado.

   .. image:: img/omv/omv-disk.png

   1. En la barra lateral, haz clic en la opción ``File System``. Luego crea y monta un sistema de archivos. Elige ``ext4`` como tipo de sistema de archivos.

   .. image:: img/omv/omv-mount.png

   2. Selecciona el dispositivo y guarda. 
   
   .. note:: Si has configurado el RAID, verás el dispositivo RAID en la lista. Solo selecciónalo y guarda.

   .. image:: img/omv/omv-mount-2.png

   3. Aparecerá una ventana informándote que se está creando el sistema de archivos, espera un momento.

   .. image:: img/omv/omv-mount-3.png

   4. Una vez hecho, entra en la interfaz ``Mount``, selecciona el sistema de archivos que acabas de crear y móntalo en tu Raspberry Pi.

   .. image:: img/omv/omv-mount-4.png

   .. note:: Si estás utilizando dos discos duros (y no RAID), debes repetir los pasos anteriores para montar también el segundo disco duro en tu Raspberry Pi.

   5. Después de montar, haz clic en Apply, y luego podrás ver los datos de tus discos en el sistema de archivos.

   .. image:: img/omv/omv-mount-5.png

   En este punto, has configurado correctamente OpenMediaVault y montado tus discos duros. Ahora puedes usar OpenMediaVault para gestionar tu almacenamiento.


6. Crear una Carpeta Compartida
---------------------------------------

   1. En la página ``Storage``, ve a la pestaña ``Shared Folders``. Y haz clic en el botón ``Create``.

   .. image:: img/omv/omv-share-1.png

   2. En la página ``Create Shared Folder``, introduce el nombre de la carpeta compartida, selecciona el disco duro que deseas compartir, la ruta de la carpeta compartida y establece los permisos. Luego haz clic en el botón ``Save``.

   .. image:: img/omv/omv-share-2.png

   3. Ahora puedes ver la carpeta compartida que acabas de crear. Confirma que es correcta, luego aplica.

   .. image:: img/omv/omv-share-3.png

   Ahora has creado exitosamente una carpeta compartida. 


7. Crear un Nuevo Usuario
---------------------------------------

   Para acceder a la carpeta, necesitamos crear un nuevo usuario. Sigue estos pasos:

   1. En la página ``User``, haz clic en el botón ``Create``.

   .. image:: img/omv/omv-user-1.png

   2. En la página ``Create User``, introduce el nombre de usuario y la contraseña del nuevo usuario, luego haz clic en el botón ``Save``.

   .. image:: img/omv/omv-user-2.png

   Ahora has creado exitosamente un nuevo usuario.


8. Configurar Permisos para el Nuevo Usuario
----------------------------------------------

   1. En la página ``Shared Folders``, haz clic en la carpeta compartida que acabas de crear. Luego haz clic en el botón ``Permissions``.

   .. image:: img/omv/omv-user-3.png

   2. En la página ``Permissions``, establece los permisos. Luego haz clic en el botón ``Save``.

   .. image:: img/omv/omv-user-4.png

   3. Una vez completado, haz clic en el botón ``Apply``.

   .. image:: img/omv/omv-user-5.png

   Ahora puedes usar este nuevo usuario para acceder a tu carpeta compartida.


9. Configurar el Servicio SMB
---------------------------------------

   1. En la página ``Services``, busca la pestaña ``SMB/CIFS`` > ``Setting``. Marca la opción ``Enable``. Luego haz clic en el botón ``Save``.

   .. image:: img/omv/omv-smb-1.png

   2. Aplica los cambios haciendo clic en el botón ``Apply``.

   .. image:: img/omv/omv-smb-2.png

   3. Entra en la página ``Shares`` y haz clic en el botón ``Create``.

   .. image:: img/omv/omv-smb-3.png

   4. En la página ``Create Share``, selecciona la ruta de la carpeta compartida. Luego haz clic en el botón ``Save``. Además, hay muchas opciones en esta página que puedes configurar según sea necesario.

   .. image:: img/omv/omv-smb-4.png

   5. Haz clic en ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   Ahora has configurado exitosamente el servicio SMB. Ahora puedes usar el protocolo SMB para acceder a tu carpeta compartida.


10. Acceder a la Carpeta Compartida en Windows
-----------------------------------------------

   1. Abre ``Este equipo`` y luego haz clic en ``Conectar a unidad de red``.

   .. image:: img/omv/omv-network-location-1.png

   2. En el cuadro de diálogo emergente, introduce la IP de la Raspberry Pi en el campo ``Folder``, por ejemplo, ``\\192.168.1.100\``, o el nombre de host de la Raspberry Pi, por ejemplo, ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Haz clic en el botón examinar y selecciona la carpeta compartida a la que deseas acceder. Durante este proceso, deberás introducir el nombre de usuario y la contraseña que creaste anteriormente.

   .. image:: img/omv/omv-network-location-3.png

   4. Marca "Reconnect at sign-in" y haz clic en el botón ``Finish``.

   .. image:: img/omv/omv-network-location-4.png
   

   5. Ahora puedes acceder a la carpeta compartida NAS.

   .. image:: img/omv/omv-network-location-5.png

10. Acceder a la Carpeta Compartida en Mac
-------------------------------------------

   1. En el menú ``Go``, haz clic en ``Connect to Server``.

   .. image:: img/omv/omv-mac-1.png

   2. En el cuadro de diálogo emergente, introduce la IP de la Raspberry Pi, por ejemplo, ``smb://192.168.1.100``, o el nombre de host de la Raspberry Pi, por ejemplo, ``smb://pi.local``.

   .. image:: img/omv/omv-mac-2.png

   3. Haz clic en el botón ``Connect``.

   .. image:: img/omv/omv-mac-3.png

   4. En el cuadro de diálogo emergente, introduce el nombre de usuario y la contraseña que creaste anteriormente. Haz clic en el botón ``Connect``.

   .. image:: img/omv/omv-mac-4.png

   5. Ahora puedes acceder a la carpeta compartida NAS.

   .. image:: img/omv/omv-mac-5.png
