.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuración en Home Assistant
============================================

Si has instalado el sistema Home Assistant, necesitarás agregar los complementos necesarios y activarlos para que el Pironman 5 funcione correctamente.

.. note::

    El siguiente método solo es aplicable a sistemas con Home Assistant instalado de manera nativa. No se aplica a sistemas Raspberry Pi con Home Assistant instalado encima o a versiones de Home Assistant en Docker.

1. Iniciar sesión en Home Assistant
----------------------------------------

* Después de encender el Pironman 5, se recomienda conectar directamente un cable Ethernet. De esta manera, puedes abrir el navegador de tu computadora e ingresar: ``homeassistant.local:8123`` para acceder a Home Assistant.

  .. image:: img/home_login.png
   :width: 90%


* Selecciona **CREAR MI HOGAR INTELIGENTE**, y luego crea tu cuenta.

  .. image:: img/home_account.png
   :width: 90%

* Sigue las indicaciones para elegir tu ubicación y otras configuraciones. Una vez completado, ingresarás al panel de control de Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Agregar el repositorio de complementos de SunFounder
-------------------------------------------------------------

La funcionalidad del Pironman 5 se instala en Home Assistant en forma de complementos. Primero, necesitas agregar el repositorio de complementos de **SunFounder**.

#. Abre **Configuración** -> **Complementos**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Haz clic en el signo de más en la esquina inferior derecha para ingresar a la tienda de complementos.

   .. image:: img/home_addon.png
      :width: 90%

#. En la tienda de complementos, haz clic en el menú en la esquina superior derecha y selecciona **Repositorios**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Ingresa la URL del repositorio de complementos de **SunFounder**: ``https://github.com/sunfounder/home-assistant-addon``, y haz clic en **AGREGAR**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Después de agregarlo exitosamente, cierra la ventana emergente y actualiza la página. Busca la lista de complementos de SunFounder.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Instalar el complemento **Pi Config Wizard**
------------------------------------------------------

El **Pi Config Wizard** puede ayudar a habilitar las configuraciones necesarias para el Pironman 5, como I2C y SPI. Si no se necesitan después, se puede eliminar.

#. Encuentra **Pi Config Wizard** en la lista de complementos de SunFounder y haz clic para ingresar.

   .. image:: img/home_pi_config.png
      :width: 90%

#. En la página de **Pi Config Wizard**, haz clic en **INSTALAR**. Espera a que se complete la instalación.

   .. image:: img/home_config_install.png
      :width: 90%

#. Después de que la instalación se complete, cambia a la página de **Registro** para confirmar si hay algún error.

   .. image:: img/home_log.png
      :width: 90%

#. Si no hay errores, regresa a la página de **Información** y haz clic en **INICIAR** para comenzar con este complemento.

   .. image:: img/home_start.png
      :width: 90%

#. Ahora abre la INTERFAZ WEB.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. En la interfaz web, verás una opción para montar la partición Boot. Haz clic en **MONTAR** para montarla.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Después de montar con éxito, verás opciones para configurar I2C, SPI y editar el archivo config.txt. Marca I2C y SPI para habilitarlos. Una vez que estén habilitados, haz clic en el botón de reinicio en la parte inferior para reiniciar la Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Después del reinicio, actualiza la página. Volverás a la página de montaje de la partición Boot nuevamente. Haz clic en **MONTAR** otra vez.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Normalmente, verás que SPI está habilitado, pero I2C no, ya que I2C requiere dos reinicios. Habilita I2C nuevamente, luego reinicia la Raspberry Pi.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Después del reinicio, vuelve a la página de **MONTAR** nuevamente. Verás que tanto I2C como SPI están habilitados.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Si después de actualizar la página, no ingresas a la página de montaje de la partición, puedes hacer clic en **Configuración** -> **Complementos** -> **Pi Config Wizard** nuevamente.
    * Verifica si este complemento está iniciado. Si no lo está, haz clic en **INICIAR**.
    * Después de iniciarlo, haz clic en **ABRIR INTERFAZ WEB**, luego haz clic en **MONTAR** para confirmar si I2C y SPI están habilitados.

4. Instalar el complemento **Pironman 5**
---------------------------------------------

Ahora comienza la instalación oficial del complemento **Pironman 5**.

#. Abre **Configuración** -> **Complementos**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Haz clic en el signo de más en la esquina inferior derecha para ingresar a la tienda de complementos.

   .. image:: img/home_addon.png
      :width: 90%

#. Encuentra **Pironman 5** en la lista de complementos de **SunFounder** y haz clic para ingresar.

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Ahora instala el complemento Pironman 5.

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. Después de que la instalación esté completa, haz clic en **INICIAR** para comenzar con este complemento. Verás que la pantalla OLED muestra la CPU de la Raspberry Pi, la temperatura y otra información relacionada. Cuatro LEDs RGB WS2812 se encenderán en azul en modo de respiración.

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. Ahora puedes hacer clic en **ABRIR INTERFAZ WEB** para abrir la página web de Pironman 5. También puedes marcar la opción para mostrar la interfaz web en la barra lateral. Esto te permitirá ver la opción de Pironman 5 en la barra lateral izquierda de Home Assistant y hacer clic para abrir la página de Pironman 5.

   .. image:: img/home_web_ui.png
      :width: 90%

#. Ahora puedes ver la información sobre tu Raspberry Pi, configurar los LEDs RGB y controlar el ventilador, etc.

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

   En este punto, ha configurado correctamente el Pironman 5 y está listo para usar.
   
   Para un control avanzado de sus componentes, consulte :ref:`control_commands_dashboard_5`.
