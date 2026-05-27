.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuración en Home Assistant
============================================

Si ya instalaste el sistema Home Assistant, deberás agregar los complementos necesarios y activarlos para que el Pironman 5 Mini funcione correctamente.

.. note::

    El siguiente método solo es aplicable a sistemas con Home Assistant instalado de forma nativa. No aplica a versiones instaladas sobre Raspberry Pi OS ni a versiones en Docker.

1. Iniciar sesión en Home Assistant
--------------------------------------------

* Después de encender el Pironman 5 Mini, se recomienda conectar un cable Ethernet. Así, podrás acceder desde el navegador de tu computadora ingresando: ``homeassistant.local:8123``.

  .. image:: img/home_login.png
   :width: 90%


* Selecciona **CREATE MY SMART HOME** y crea tu cuenta.

  .. image:: img/home_account.png
   :width: 90%

* Sigue las instrucciones para establecer tu ubicación y demás configuraciones. Una vez finalizado, accederás al panel principal de Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Agregar el repositorio de complementos de SunFounder
------------------------------------------------------------

La funcionalidad del Pironman 5 Mini se instala como complemento en Home Assistant. Primero, debes agregar el repositorio de complementos de **SunFounder**.

#. Abre **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Haz clic en el signo de suma en la esquina inferior derecha para acceder a la tienda de complementos.

   .. image:: img/home_addon.png
      :width: 90%

#. En la tienda de complementos, haz clic en el menú de la esquina superior derecha y selecciona **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Ingresa la URL del repositorio de **SunFounder**: ``https://github.com/sunfounder/home-assistant-addon`` y haz clic en **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Una vez añadido con éxito, cierra la ventana emergente y actualiza la página. Verás la lista de complementos de SunFounder.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Instalar el complemento **Pi Config Wizard**
------------------------------------------------------

El **Pi Config Wizard** permite activar configuraciones necesarias para el Pironman 5 Mini, como I2C y SPI. Se puede eliminar si ya no es necesario.

#. Busca **Pi Config Wizard** en la lista de complementos de SunFounder y haz clic para acceder.

   .. image:: img/home_pi_config.png
      :width: 90%

#. En la página de **Pi Config Wizard**, haz clic en **INSTALL**. Espera a que finalice la instalación.

   .. image:: img/home_config_install.png
      :width: 90%

#. Tras la instalación, cambia a la pestaña **Log** para confirmar que no haya errores.

   .. image:: img/home_log.png
      :width: 90%

#. Si no hay errores, vuelve a la pestaña **Info** y haz clic en **START** para iniciar el complemento.

   .. image:: img/home_start.png
      :width: 90%

#. Ahora abre la interfaz web (WEB UI).

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. En la interfaz web, verás la opción para montar la partición Boot. Haz clic en **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Tras montar exitosamente, podrás activar I2C, SPI y editar el archivo config.txt. Marca I2C y SPI para habilitarlos. Cuando se muestren como habilitados, haz clic en el botón de reinicio para reiniciar la Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Luego del reinicio, actualiza la página y vuelve a montar la partición Boot haciendo clic en **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Usualmente verás que SPI está habilitado, pero I2C no. Esto se debe a que I2C requiere dos reinicios. Vuelve a habilitar I2C y reinicia la Raspberry Pi nuevamente.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Tras el segundo reinicio, vuelve a la página de **MOUNT**. Verás que tanto I2C como SPI están habilitados.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Si al actualizar la página no accedes a la página de montaje, ve a **Settings** -> **Add-ons** -> **Pi Config Wizard**.
    * Verifica que el complemento esté iniciado. Si no lo está, haz clic en **START**.
    * Luego, haz clic en **OPEN WEB UI**, y después en **MOUNT** para confirmar que I2C y SPI están habilitados.





4. Instalar el complemento **Pironman 5 Mini**
----------------------------------------------------

Ahora comenzaremos oficialmente con la instalación del complemento **Pironman 5 Mini**.

#. Abre **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Haz clic en el signo de suma en la esquina inferior derecha para acceder a la tienda de complementos.

   .. image:: img/home_addon.png
      :width: 90%

#. Busca **Pironman 5 Mini** en la lista de complementos de **SunFounder** y haz clic para acceder.

   .. image:: img/home_pironman5_mini_addon.png
      :width: 90%

#. Instala el complemento Pironman 5 Mini.

   .. image:: img/home_pironman5_mini_addon_install.png
      :width: 90%

#. Tras completar la instalación, haz clic en **START** para iniciarlo. Verás que los cuatro LED RGB WS2812 se iluminan en azul con efecto de respiración.

   .. image:: img/home_pironman5_mini_addon_start.png
      :width: 90%

#. Luego haz clic en **OPEN WEB UI** para abrir la página web de Pironman 5 Mini. También puedes marcar la opción para mostrar la interfaz en la barra lateral. Así, podrás acceder a la página desde el menú izquierdo de Home Assistant.

   .. image:: img/home_pironman5_mini_webui.png
      :width: 90%

#. Ahora podrás visualizar información de tu Raspberry Pi, configurar los LED RGB, controlar el ventilador, entre otras opciones.

   .. image:: img/home_web.png
      :width: 90%

.. note::

   En este punto, ha configurado correctamente el Pironman 5 Mini y está listo para usar.
   
   Para un control avanzado de sus componentes, consulte :ref:`control_commands_dashboard_mini`.
