.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_os_sd_rpi_promax:

Instalación del Sistema Operativo
===================================

Antes de usar su Raspberry Pi, necesita instalar **Raspberry Pi OS** en una tarjeta microSD.
Esta guía explica cómo hacerlo usando **Raspberry Pi Imager** de una manera simple y amigable para principiantes.

**Componentes Requeridos**

* Una computadora (Windows, macOS o Linux)
* Una tarjeta microSD (16GB o más; marcas recomendadas: SanDisk, Samsung)
* Un lector de tarjetas microSD

-------------------

.. start_install_imager

1. Instalar Raspberry Pi Imager
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>

#. Visite la página oficial de descarga de Raspberry Pi Imager: |shared_link_rpi_imager|. Descargue el instalador correcto para su sistema operativo.

   .. image:: img/imager_download.png
      :width: 70%

#. Siga las instrucciones de instalación (idioma, ruta de instalación, confirmación). Después de la instalación, ejecute **Raspberry Pi Imager** desde su escritorio o menú de aplicaciones.

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. Instalar el SO en la tarjeta microSD
------------------------------------------------

1. Inserte su tarjeta microSD en su computadora usando un lector de tarjetas. Respalde cualquier dato importante antes de continuar.

   .. image:: img/insert_sd.png
      :width: 90%

2. Cuando se abra Raspberry Pi Imager, verá la página **Device**. Seleccione su modelo de Raspberry Pi 5 de la lista.

   .. image:: img/imager_device.png
      :width: 90%

3. Vaya a la sección **OS** y elija la opción recomendada **Raspberry Pi OS (64-bit)**.

   .. warning::

      Asegúrate de elegir una versión de **64 bits**. Si instalas un sistema de **32 bits**, algunos paquetes solo están disponibles para ``aarch64`` (64 bits) y es posible que ciertas funciones no se instalen o no funcionen correctamente.

   .. image:: img/imager_os.png
      :width: 90%

4. En la sección **Storage**, seleccione su tarjeta microSD.

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. Haga clic en **Next** para continuar al paso de personalización.

   .. note::

      * Si va a conectar un monitor, teclado y mouse directamente a su Raspberry Pi, puede hacer clic en **SKIP CUSTOMISATION**.
      * Si planea configurar la Raspberry Pi de forma *headless* (acceso remoto por Wi-Fi), debe completar la configuración de personalización.

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **Establecer Hostname**

   * Asigne un nombre de host único a su Raspberry Pi.
   * Puede conectarse más tarde usando ``hostname.local``.

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **Establecer Localización**

   * Elija su ciudad capital.
   * Imager completará automáticamente la zona horaria y la distribución del teclado según su selección, aunque puede ajustarlas si es necesario. Seleccione Next.

   .. image:: img/imager_custom_local.png
      :width: 90%

#. **Establecer Nombre de Usuario y Contraseña**

   Cree una cuenta de usuario para su Raspberry Pi.

   .. image:: img/imager_custom_user.png
      :width: 90%

#. **Configurar Wi-Fi**

   * Ingrese su **SSID** (nombre de la red) y **contraseña** de Wi-Fi.
   * Su Raspberry Pi se conectará automáticamente en el primer arranque.

   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **Habilitar SSH (Opcional pero Recomendado)**

   * Habilitar SSH le permite iniciar sesión de forma remota desde su computadora.
   * Puede iniciar sesión usando su nombre de usuario/contraseña o configurar claves SSH.

   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **Habilitar Raspberry Pi Connect (Opcional)**

   Raspberry Pi Connect le permite acceder al escritorio de su Raspberry Pi desde un navegador web.

   * Active **Raspberry Pi Connect**, luego haga clic en **OPEN RASPBERRY PI CONNECT**.

     .. image:: img/imager_custom_connect.png
        :width: 90%

   * El sitio web de Raspberry Pi Connect se abrirá en su navegador predeterminado. Inicie sesión en su cuenta de Raspberry Pi ID, o regístrese si aún no tiene una.

     .. image:: img/imager_custom_open.png
        :width: 90%

   * En la página **New auth key**, cree su clave de autenticación de un solo uso.

      * Si su cuenta de Raspberry Pi ID no pertenece a ninguna organización, seleccione **Create auth key and launch Raspberry Pi Imager**.
      * Si pertenece a una o más organizaciones, elija una, luego cree la clave y ejecute Imager.
      * Asegúrese de encender su Raspberry Pi y conectarla a internet antes de que expire la clave.

     .. image:: img/imager_custom_authkey.png
        :width: 90%

   * Su navegador puede pedirle que abra Raspberry Pi Imager — permítalo.

     * Imager se abrirá en la pestaña de Raspberry Pi Connect, mostrando el token de autenticación.
     * Si el token no se transfiere automáticamente, abra la sección **Having trouble?** en la página de Raspberry Pi Connect, copie el token y péguelo manualmente en Imager.

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. Revise todas las configuraciones y haga clic en **WRITE**.

   .. image:: img/imager_writing.png
      :width: 90%

#. Si la tarjeta ya contiene datos, Raspberry Pi Imager mostrará una advertencia de que todos los datos en el dispositivo serán borrados. Verifique que seleccionó la unidad correcta, luego haga clic en **I UNDERSTAND, ERASE AND WRITE** para continuar.

   .. image:: img/imager_erase.png
      :width: 90%

#. Espere a que finalicen la escritura y la verificación. Cuando termine, Raspberry Pi Imager mostrará **Write complete!** y un resumen de sus opciones. El dispositivo de almacenamiento se expulsará automáticamente para que pueda retirarlo de forma segura.

   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. Retire la tarjeta microSD e insértela en la ranura en la parte inferior de su Raspberry Pi. ¡Su Raspberry Pi ya está lista para arrancar con el nuevo SO!

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%