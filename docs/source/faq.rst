.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

FAQ
====

1. Sistemas compatibles
------------------------

Sistemas que han pasado las pruebas en el Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Sobre el botón de encendido
------------------------------

El botón de encendido es una extensión del botón del Raspberry Pi 5 y funciona de la misma manera.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Apagar**

  * Si utilizas el sistema **Raspberry Pi Bookworm Desktop**, puedes presionar el botón de encendido dos veces rápidamente para apagarlo.
  * Si utilizas el sistema **Raspberry Pi Bookworm Lite**, presiona el botón de encendido una sola vez para iniciar el apagado.
  * Para forzar un apagado completo, mantén presionado el botón de encendido.

* **Encender**

  * Si la placa del Raspberry Pi está apagada pero aún tiene alimentación, presiona una sola vez el botón para encenderla.

* Si estás utilizando un sistema que no admite un botón de apagado, puedes mantenerlo presionado durante 5 segundos para forzar un apagado completo y presionar una sola vez para encenderla.

3. Dirección del flujo de aire
------------------------------

El flujo de aire en el chasis del Pironman 5 está diseñado cuidadosamente para maximizar la eficiencia del enfriamiento. El aire frío entra principalmente a través de la interfaz GPIO y otras pequeñas aberturas, garantizando una entrada uniforme. Luego, pasa a través del Tool Cooler, equipado con un ventilador de alto rendimiento para regular las temperaturas internas, y finalmente se expulsa a través de los dos ventiladores RGB en el panel lateral.

Para una demostración detallada, consulta el siguiente video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Tu navegador no admite la etiqueta de video.
        </video>
    </div>


4. Sobre los extremos de los tubos de cobre del Tower Cooler
------------------------------------------------------------

Los tubos de calor en forma de U situados en la parte superior del Tower Cooler están comprimidos para facilitar el paso de los tubos de cobre a través de las aletas de aluminio, lo cual es parte del proceso normal de fabricación.

   .. image:: img/tower_cooler1.png

5. ¿El Pironman 5 es compatible con sistemas de juegos retro?
-------------------------------------------------------------

Sí, es compatible. Sin embargo, la mayoría de los sistemas de juegos retro son versiones simplificadas que no permiten instalar y ejecutar software adicional. Esta limitación puede hacer que algunos componentes del Pironman 5, como la pantalla OLED, los dos ventiladores RGB y los 4 LEDs RGB, no funcionen correctamente, ya que requieren la instalación de los paquetes de software del Pironman 5.

.. note::

   El sistema Batocera.linux es ahora totalmente compatible con el Pironman 5. Batocera.linux es una distribución de juegos retro de código abierto y completamente gratuita.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

6. ¿La pantalla OLED no funciona?
----------------------------------

Si la pantalla OLED no muestra nada o muestra incorrectamente, sigue estos pasos de solución de problemas:

#. Asegúrate de que el cable FPC de la pantalla OLED esté conectado de forma segura. Se recomienda reconectar la pantalla OLED y luego encender el dispositivo.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

#. Confirma que el Raspberry Pi está ejecutando un sistema operativo compatible. El Pironman 5 solo es compatible con los siguientes sistemas:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si has instalado un sistema no compatible, sigue la guía para instalar un sistema operativo compatible: :ref:`install_the_os`.

#. Cuando la pantalla OLED se enciende por primera vez, puede mostrar solo bloques de píxeles. Debes seguir las instrucciones en :ref:`set_up_pironman5` para completar la configuración antes de que pueda mostrar información correctamente.

#. Usa el siguiente comando para verificar si se detecta la dirección I2C ``0x3C`` de la OLED:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Si se detecta la dirección I2C ``0x3C``, reinicia el servicio Pironman 5 usando este comando:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Activa I2C si la dirección no se detecta:

     * Edita el archivo de configuración ejecutando:

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Agrega la siguiente línea al final del archivo:

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Guarda el archivo presionando ``Ctrl+X``, luego ``Y`` y sal. Reinicia el Pironman 5 y verifica si el problema se resuelve.

Si el problema persiste después de realizar los pasos anteriores, envía un correo a service@sunfounder.com. Responderemos lo antes posible.

7. ¿El módulo NVMe PIP no funciona?
--------------------------------------

1. Asegúrate de que el cable FPC que conecta el módulo NVMe PIP al Raspberry Pi 5 esté conectado de manera segura.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

2. Confirma que tu SSD está correctamente asegurado al módulo NVMe PIP.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

3. Verifica el estado de los LEDs del módulo NVMe PIP:

   Después de confirmar todas las conexiones, enciende el Pironman 5 y observa los dos indicadores en el módulo NVMe PIP:

   * **LED de alimentación (PWR)**: Debe estar encendido.
   * **LED de estado (STA)**: Debe parpadear para indicar un funcionamiento normal.

   .. image:: img/nvme_pip_leds.png

   * Si el **LED PWR** está encendido pero el **LED STA** no parpadea, indica que el SSD NVMe no es reconocido por el Raspberry Pi.
   * Si el **LED PWR** está apagado, une los pines "Force Enable" (J4) en el módulo. Si el **LED PWR** se enciende, podría indicar un cable FPC flojo o una configuración de sistema no compatible para NVMe.

     .. image:: img/nvme_pip_j4.png

4. Confirma que tu SSD NVMe tiene un sistema operativo correctamente instalado. Consulta: :ref:`install_the_os`.

5. Si el cableado es correcto y el sistema operativo está instalado, pero el SSD NVMe aún no arranca, intenta arrancar desde una tarjeta Micro SD para verificar la funcionalidad de otros componentes. Una vez confirmado, procede a: :ref:`configure_boot_ssd`.

Si el problema persiste después de realizar los pasos anteriores, envía un correo a service@sunfounder.com. Responderemos lo antes posible.

8. ¿Los LEDs RGB no funcionan?
---------------------------------

#. Los dos pines en el IO Expander encima de J9 se utilizan para conectar los LEDs RGB al GPIO10. Asegúrate de que el puente (jumper) en estos dos pines esté colocado correctamente.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifica que el Raspberry Pi esté ejecutando un sistema operativo compatible. El Pironman 5 solo es compatible con las siguientes versiones de sistemas operativos:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si has instalado un sistema operativo no compatible, sigue la guía para instalar un sistema operativo compatible: :ref:`install_the_os`.

#. Ejecuta el comando ``sudo raspi-config`` para abrir el menú de configuración. Navega a **3 Interfacing Options** -> **I3 SPI** -> **YES**, luego haz clic en **OK** y **Finish** para habilitar SPI. Después de habilitar SPI, reinicia el Pironman 5.

Si el problema persiste después de realizar los pasos anteriores, envía un correo a service@sunfounder.com. Responderemos lo antes posible.

9. ¿El ventilador del CPU no funciona?
-----------------------------------------

Cuando la temperatura del CPU no ha alcanzado el umbral establecido, el ventilador del CPU no se activará.

**Control de velocidad del ventilador basado en la temperatura**

El ventilador PWM opera de manera dinámica, ajustando su velocidad según la temperatura del Raspberry Pi 5:

* **Por debajo de 50°C**: El ventilador permanece apagado (0% de velocidad).  
* **A 50°C**: El ventilador opera a baja velocidad (30% de velocidad).  
* **A 60°C**: El ventilador aumenta a velocidad media (50% de velocidad).  
* **A 67.5°C**: El ventilador se acelera a alta velocidad (70% de velocidad).  
* **A 75°C y más**: El ventilador opera a velocidad máxima (100% de velocidad).  

Para más detalles, consulta: :ref:`Fans`.

10. ¿Cómo deshabilitar el panel de control web?
--------------------------------------------------

Una vez que hayas completado la instalación del módulo ``pironman5``, podrás acceder a :ref:`view_control_dashboard`.

Si no necesitas esta función y deseas reducir el uso de CPU y RAM, puedes deshabilitar el panel de control durante la instalación de ``pironman5`` añadiendo la opción ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si ya has instalado ``pironman5``, puedes eliminar el módulo ``dashboard`` y ``influxdb``, luego reiniciar ``pironman5`` para aplicar los cambios:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

11. ¿Cómo controlar los componentes usando el comando ``pironman5``?
-----------------------------------------------------------------------

Puedes consultar el siguiente tutorial para controlar los componentes del Pironman 5 utilizando el comando ``pironman5``:

* :ref:`view_control_commands`

12. ¿Cómo cambiar el orden de arranque del Raspberry Pi usando comandos?
----------------------------------------------------------------------------

Si ya has iniciado sesión en tu Raspberry Pi, puedes cambiar el orden de arranque utilizando comandos. Las instrucciones detalladas son las siguientes:

* :ref:`configure_boot_ssd`

13. ¿Cómo modificar el orden de arranque con Raspberry Pi Imager?
---------------------------------------------------------------------

Además de modificar el ``BOOT_ORDER`` en la configuración EEPROM, también puedes usar **Raspberry Pi Imager** para cambiar el orden de arranque de tu Raspberry Pi.

Se recomienda usar una tarjeta de repuesto para este paso.

* :ref:`update_bootloader`

14. ¿Cómo copiar el sistema de la tarjeta SD a un SSD NVMe?
--------------------------------------------------------------

Si tienes un SSD NVMe pero no tienes un adaptador para conectarlo a tu computadora, puedes primero instalar el sistema en tu tarjeta Micro SD. Una vez que el Pironman 5 se inicie correctamente, puedes copiar el sistema desde tu tarjeta Micro SD al SSD NVMe. Las instrucciones detalladas son las siguientes:

* :ref:`copy_sd_to_nvme_rpi`

15. ¿Cómo quitar la película protectora de las placas de acrílico?
----------------------------------------------------------------------

En el paquete se incluyen dos placas de acrílico, ambas cubiertas con una película protectora amarilla/transparente en ambos lados para evitar arañazos. La película protectora puede ser un poco difícil de quitar. Usa un destornillador para raspar suavemente las esquinas, luego retira cuidadosamente toda la película.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

16. ¿Cómo instalar OpenSSH a través de PowerShell?
------------------------------------------------------

Cuando intentas usar ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) para conectarte a tu Raspberry Pi, puede aparecer el siguiente mensaje de error:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Esto indica que tu sistema operativo es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado. Sigue los pasos a continuación para instalarlo manualmente.

#. Escribe ``powershell`` en el cuadro de búsqueda de tu escritorio de Windows, haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador`` en el menú que aparece.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Usa el siguiente comando para instalar ``OpenSSH.Client``:

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Una vez completada la instalación, aparecerá la siguiente salida:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación ejecutando el siguiente comando:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. El resultado debería indicar que ``OpenSSH.Client`` se ha instalado correctamente:

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning::
        Si no aparece la información anterior, significa que tu sistema Windows es demasiado antiguo. Se recomienda usar una herramienta SSH de terceros, como |link_putty|.

#. Reinicia PowerShell y ejecútalo nuevamente como administrador. Ahora podrás iniciar sesión en tu Raspberry Pi usando el comando ``ssh``, donde se te pedirá que ingreses la contraseña configurada previamente.

   .. image:: img/powershell_login.png


17. ¿Cómo encender/apagar la pantalla OLED?
---------------------------------------------

Puedes encender o apagar la pantalla OLED utilizando el panel de control o la línea de comandos.

1. Encender/apagar la pantalla OLED desde el panel de control.

   .. note::

    Antes de usar el panel de control, necesitas configurarlo en Home Assistant. Consulta: :ref:`view_control_dashboard`.

- Después de completar la configuración, sigue estos pasos para encender, apagar o configurar tu pantalla OLED.

   .. image:: img/set_up_on_dashboard.jpg
      :width: 90%

2. Encender/apagar la pantalla OLED desde la línea de comandos.

- Usa el siguiente comando para encender o apagar la pantalla OLED:

.. code-block::

    sudo pironman5 -oe on/off

.. note::

    Es posible que necesites reiniciar el servicio pironman5 para que los cambios surtan efecto. Usa el siguiente comando para reiniciar el servicio:

      .. code-block::

        sudo systemctl restart pironman5.service
