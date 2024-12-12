.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Preguntas Frecuentes
========================

1. Sobre sistemas compatibles
-----------------------------

Sistemas que pasaron la prueba en el Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Sobre el botón de encendido
------------------------------

El botón de encendido del Pironman 5 refleja la funcionalidad del botón de encendido del Raspberry Pi 5 y funciona de la misma manera.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Apagado**

  * Si utiliza el sistema **Bookworm Desktop** de Raspberry Pi, puede presionar el botón de encendido dos veces rápidamente para apagarlo.
  * Si utiliza el sistema **Bookworm Lite** de Raspberry Pi, presione el botón de encendido una sola vez para iniciar el apagado.
  * Para un apagado forzado, mantenga presionado el botón de encendido.

* **Encendido**

  * Si la placa Raspberry Pi está apagada pero aún tiene energía, presione una sola vez para encender desde un estado apagado.

* Si está ejecutando un sistema que no admite el botón de apagado, manténgalo presionado durante 5 segundos para forzar un apagado y presione una sola vez para encender desde un estado apagado.

3. Sobre la dirección del flujo de aire
---------------------------------------

El flujo de aire en el chasis del Pironman 5 está cuidadosamente diseñado para maximizar la eficiencia de enfriamiento. El aire fresco entra al chasis principalmente a través de la interfaz GPIO y otras pequeñas aberturas, asegurando una entrada uniforme. Luego pasa a través del Tool Cooler, equipado con un ventilador de alto rendimiento para regular las temperaturas internas, y finalmente es expulsado a través de los dos ventiladores RGB en el panel lateral.

Para una demostración detallada, consulte el video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Su navegador no soporta la etiqueta de video.
        </video>
    </div>

4. ¿El Pironman 5 es compatible con sistemas de retro gaming?
-------------------------------------------------------------

Sí, es compatible. Sin embargo, la mayoría de los sistemas de retro gaming son versiones optimizadas que no pueden instalar ni ejecutar software adicional. Esta limitación puede causar que algunos componentes del Pironman 5, como la pantalla OLED, los dos ventiladores RGB y los 4 LED RGB, no funcionen correctamente, ya que estos componentes requieren la instalación de los paquetes de software del Pironman 5.

.. note::

   El sistema Batocera.linux ahora es completamente compatible con el Pironman 5. Batocera.linux es una distribución de retro gaming de código abierto y completamente gratuita.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

5. ¿La pantalla OLED no funciona?
----------------------------------

Si la pantalla OLED no muestra nada o muestra información incorrecta, siga estos pasos de solución de problemas:

#. Asegúrese de que el cable FPC de la pantalla OLED esté conectado de manera segura. Se recomienda volver a conectar la pantalla OLED y luego encender el dispositivo.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Su navegador no soporta la etiqueta de video.
           </video>
       </div>

#. Confirme que el Raspberry Pi esté ejecutando un sistema operativo compatible. El Pironman 5 solo admite los siguientes sistemas:

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Si ha instalado un sistema no compatible, siga la guía para instalar un sistema operativo compatible: :ref:`install_the_os`.

#. Cuando se enciende la pantalla OLED por primera vez, puede que solo muestre bloques de píxeles. Debe seguir las instrucciones en :ref:`set_up_pironman5` para completar la configuración antes de que pueda mostrar información adecuada.

#. Use el siguiente comando para verificar si se detecta la dirección I2C ``0x3C`` de la pantalla OLED:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Si se detecta la dirección I2C ``0x3C``, reinicie el servicio Pironman 5 con este comando:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Habilite I2C si no se detecta la dirección:

     * Edite el archivo de configuración ejecutando:

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Agregue la siguiente línea al final del archivo:

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Guarde el archivo presionando ``Ctrl+X``, luego ``Y`` y salga. Reinicie el Pironman 5 y verifique si el problema se resuelve.

Si el problema persiste después de realizar los pasos anteriores, envíe un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.

6. ¿El módulo NVMe PIP no funciona?
------------------------------------

1. Asegúrese de que el cable FPC que conecta el módulo NVMe PIP al Raspberry Pi 5 esté conectado de manera segura.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Su navegador no soporta la etiqueta de video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Su navegador no soporta la etiqueta de video.
           </video>
       </div>

2. Confirme que su SSD esté correctamente asegurado al módulo NVMe PIP.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Su navegador no soporta la etiqueta de video.
           </video>
       </div>

3. Verifique el estado de los LED del módulo NVMe PIP:

   Después de confirmar todas las conexiones, encienda el Pironman 5 y observe los dos indicadores en el módulo NVMe PIP:

   * **LED PWR**: Debería estar encendido.
   * **LED STA**: Debería parpadear para indicar un funcionamiento normal.

   .. image:: img/nvme_pip_leds.png  

   * Si el **LED PWR** está encendido pero el **LED STA** no parpadea, indica que el SSD NVMe no es reconocido por el Raspberry Pi.
   * Si el **LED PWR** está apagado, haga un puente en los pines "Force Enable" (J4) del módulo. Si el **LED PWR** se enciende, podría indicar un cable FPC suelto o una configuración de sistema no compatible para NVMe.

     .. image:: img/nvme_pip_j4.png  

4. Confirme que su SSD NVMe tenga un sistema operativo instalado correctamente. Consulte: :ref:`install_the_os`.

5. Si el cableado es correcto y el sistema operativo está instalado, pero el SSD NVMe aún no arranca, intente iniciar desde una tarjeta Micro SD para verificar la funcionalidad de otros componentes. Una vez confirmado, proceda a: :ref:`configure_boot_ssd`.

Si el problema persiste después de realizar los pasos anteriores, envíe un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.

7. Los LED RGB no funcionan
-----------------------------

#. Los dos pines en el IO Expander sobre J9 se utilizan para conectar los LED RGB a GPIO10. Asegúrese de que el puente en estos dos pines esté colocado correctamente.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifique que el Raspberry Pi esté ejecutando un sistema operativo compatible. El Pironman 5 solo es compatible con las siguientes versiones de sistema operativo:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si ha instalado un sistema operativo no compatible, siga la guía para instalar un sistema operativo compatible: :ref:`install_the_os`.

#. Ejecute el comando ``sudo raspi-config`` para abrir el menú de configuración. Navegue a **3 Interfacing Options** -> **I3 SPI** -> **YES**, luego haga clic en **OK** y **Finish** para habilitar SPI. Después de habilitar SPI, reinicie el Pironman 5.

Si el problema persiste después de realizar los pasos anteriores, envíe un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.

8. ¿Cómo desactivar el tablero web?
------------------------------------

Una vez que haya completado la instalación del módulo ``pironman5``, podrá acceder al :ref:`view_control_dashboard`.

Si no necesita esta función y desea reducir el uso de CPU y RAM, puede desactivar el tablero durante la instalación de ``pironman5`` agregando el indicador ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si ya ha instalado ``pironman5``, puede eliminar el módulo ``dashboard`` y ``influxdb``, luego reiniciar pironman5 para aplicar los cambios:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

9. ¿Cómo controlar los componentes usando el comando ``pironman5``?
-------------------------------------------------------------------

Puede consultar el siguiente tutorial para controlar los componentes del Pironman 5 usando el comando ``pironman5``.

* :ref:`view_control_commands`

10. ¿Cómo cambiar el orden de arranque del Raspberry Pi usando comandos?
------------------------------------------------------------------------

Si ya ha iniciado sesión en su Raspberry Pi, puede cambiar el orden de arranque usando comandos. Las instrucciones detalladas son las siguientes:

* :ref:`configure_boot_ssd`

11. ¿Cómo modificar el orden de arranque con Raspberry Pi Imager?
------------------------------------------------------------------

Además de modificar el ``BOOT_ORDER`` en la configuración del EEPROM, también puede usar el **Raspberry Pi Imager** para cambiar el orden de arranque de su Raspberry Pi.

Se recomienda usar una tarjeta de repuesto para este paso.

* :ref:`update_bootloader`

12. ¿Cómo copiar el sistema desde la tarjeta SD a un SSD NVMe?
--------------------------------------------------------------

Si tiene un SSD NVMe pero no tiene un adaptador para conectar su NVMe a su computadora, primero puede instalar el sistema en su tarjeta Micro SD. Una vez que el Pironman 5 se inicie con éxito, puede copiar el sistema desde su tarjeta Micro SD a su SSD NVMe. Las instrucciones detalladas son las siguientes:

* :ref:`copy_sd_to_nvme_rpi`

13. ¿Cómo quitar la película protectora de las placas acrílicas?
-----------------------------------------------------------------

El paquete incluye dos paneles acrílicos, ambos cubiertos con una película protectora amarilla/transparente en ambos lados para evitar rayones. La película protectora puede ser algo difícil de quitar. Use un destornillador para raspar suavemente las esquinas y luego retire cuidadosamente toda la película.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

14. ¿Cómo instalar OpenSSH a través de Powershell?
--------------------------------------------------

Cuando usa ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) para conectarse a su Raspberry Pi, pero aparece el siguiente mensaje de error:

    .. code-block::

        ssh: El término 'ssh' no se reconoce como el nombre de un cmdlet, función, archivo de script o programa ejecutable. Verifique la ortografía del nombre o, si se incluyó una ruta, asegúrese de que sea correcta e inténtelo de nuevo.

Esto significa que su sistema operativo es demasiado antiguo y no tiene preinstalado `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_. Debe seguir el tutorial a continuación para instalarlo manualmente.

#. Escriba ``powershell`` en el cuadro de búsqueda de su escritorio de Windows, haga clic derecho en ``Windows PowerShell`` y seleccione ``Ejecutar como administrador`` en el menú que aparece.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Use el siguiente comando para instalar ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Después de la instalación, se devolverá la siguiente salida.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifique la instalación utilizando el siguiente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora le indica que ``OpenSSH.Client`` se ha instalado con éxito.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si no aparece el aviso anterior, significa que su sistema Windows sigue siendo demasiado antiguo y se le recomienda instalar una herramienta SSH de terceros, como |link_putty|.

#. Ahora reinicie PowerShell y continúe ejecutándolo como administrador. En este punto podrá iniciar sesión en su Raspberry Pi utilizando el comando ``ssh``, donde se le pedirá que ingrese la contraseña que configuró anteriormente.

   .. image:: img/powershell_login.png
