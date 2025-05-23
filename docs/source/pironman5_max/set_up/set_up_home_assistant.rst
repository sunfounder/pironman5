.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el apasionante mundo de Raspberry Pi, Arduino y ESP32 junto a otros aficionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo especializado.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos especiales.
    - **Descuentos exclusivos**: Disfruta de ofertas únicas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Configuración en Home Assistant
============================================

Si ya tienes instalado el sistema Home Assistant, deberás añadir los complementos necesarios y activarlos para que Pironman 5 funcione correctamente.

.. note::

    El siguiente método solo aplica a sistemas con Home Assistant instalado de forma nativa. No es válido para sistemas donde Home Assistant se ejecuta sobre Raspberry Pi ni para versiones en Docker.

1. Iniciar sesión en Home Assistant
--------------------------------------------

* Después de encender Pironman 5, se recomienda conectar directamente un cable Ethernet. Luego, abre el navegador en tu ordenador e ingresa: ``homeassistant.local:8123`` para acceder a Home Assistant.

  .. image:: img/home_login.png
   :width: 90%


* Selecciona **CREATE MY SMART HOME**, y luego crea tu cuenta.

  .. image:: img/home_account.png
   :width: 90%

* Sigue las instrucciones para establecer tu ubicación y otras configuraciones. Al finalizar, accederás al panel principal de Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Añadir el repositorio de complementos de SunFounder
------------------------------------------------------------

Las funcionalidades de Pironman 5 se integran en Home Assistant mediante complementos. Primero, necesitas añadir el repositorio de complementos de **SunFounder**.

#. Abre **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Haz clic en el ícono de suma en la esquina inferior derecha para acceder a la tienda de complementos.

   .. image:: img/home_addon.png
      :width: 90%

#. En la tienda de complementos, haz clic en el menú superior derecho y selecciona **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Ingresa la URL del repositorio de SunFounder: ``https://github.com/sunfounder/home-assistant-addon``, y haz clic en **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Una vez añadido correctamente, cierra la ventana emergente y actualiza la página. Busca la lista de complementos de SunFounder.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Instalar el complemento **Pi Config Wizard**
------------------------------------------------------

**Pi Config Wizard** permite habilitar configuraciones necesarias para Pironman 5, como I2C y SPI. Si no lo necesitas más adelante, puedes desinstalarlo.

#. Encuentra **Pi Config Wizard** en la lista de complementos de SunFounder y haz clic para ingresar.

   .. image:: img/home_pi_config.png
      :width: 90%

#. En la página de **Pi Config Wizard**, haz clic en **INSTALL** y espera a que termine la instalación.

   .. image:: img/home_config_install.png
      :width: 90%

#. Una vez instalado, cambia a la pestaña **Log** para verificar si hay errores.

   .. image:: img/home_log.png
      :width: 90%

#. Si no hay errores, vuelve a la pestaña **Info** y haz clic en **START** para iniciar el complemento.

   .. image:: img/home_start.png
      :width: 90%

#. Ahora abre la interfaz web (WEB UI).

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. En la interfaz web, verás una opción para montar la partición Boot. Haz clic en **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Tras un montaje exitoso, aparecerán opciones para activar I2C, SPI y editar el archivo config.txt. Marca I2C y SPI para activarlos. Una vez activados, haz clic en el botón de reinicio para reiniciar la Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Después del reinicio, actualiza la página. Volverás a la pantalla de montaje de partición. Haz clic en **MOUNT** nuevamente.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Generalmente verás que SPI está activado, pero I2C no, ya que I2C requiere dos reinicios. Activa I2C nuevamente y reinicia la Raspberry Pi.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Tras el segundo reinicio, vuelve a la página **MOUNT**. Verás que tanto I2C como SPI están activados.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Si al actualizar la página no ingresas a la pantalla de montaje, ve a **Settings** -> **Add-ons** -> **Pi Config Wizard**.
    * Verifica si el complemento está iniciado. Si no lo está, haz clic en **START**.
    * Después de iniciar, haz clic en **OPEN WEB UI**, luego en **MOUNT** para confirmar si I2C y SPI están habilitados.

4. Instalar el complemento **Pironman 5**
---------------------------------------------

Ahora comienza oficialmente la instalación del complemento **Pironman 5**.

#. Abre **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Haz clic en el ícono de suma en la esquina inferior derecha para acceder a la tienda de complementos.

   .. image:: img/home_addon.png
      :width: 90%

#. Encuentra **Pironman 5** en la lista de complementos de **SunFounder** y haz clic para ingresar.

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Instala el complemento Pironman 5.

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. Una vez instalado, haz clic en **START** para iniciar el complemento. Verás en la pantalla OLED información como la CPU de la Raspberry Pi, la temperatura, entre otros datos. Además, cuatro LEDs RGB WS2812 se encenderán en azul con un efecto de respiración.

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. Ahora puedes hacer clic en **OPEN WEB UI** para acceder a la página web de Pironman 5. También puedes activar la opción para mostrar la interfaz en la barra lateral. Así podrás acceder directamente desde el menú lateral de Home Assistant.

   .. image:: img/home_web_ui.png
      :width: 90%

#. En la interfaz web podrás consultar información de tu Raspberry Pi, configurar los LEDs RGB, controlar el ventilador y mucho más.

   .. image:: img/home_web.png
      :width: 90%

.. note::

    Para más información sobre cómo usar la página web de Pironman 5, consulta: :ref:`max_view_control_dashboard`.
