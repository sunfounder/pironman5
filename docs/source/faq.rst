.. note:: 

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios de nuevos productos y contenido exclusivo.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

FAQ
============

1. Sobre sistemas compatibles
--------------------------------

Sistemas que pasaron la prueba en Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Sobre el botón de encendido
------------------------------------

El botón de encendido activa el botón del Raspberry Pi 5 y funciona de la misma manera que el botón original del dispositivo.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Apagar**

  * Si utilizas el sistema **Bookworm Desktop** de Raspberry Pi, puedes presionar el botón de encendido dos veces rápidamente para apagarlo.
  * Si utilizas el sistema **Bookworm Lite** de Raspberry Pi, presiona el botón de encendido una vez para iniciar el apagado.
  * Para forzar un apagado completo, mantén presionado el botón de encendido.

* **Encender**

  * Si la placa Raspberry Pi está apagada pero aún conectada a la corriente, presiona el botón una vez para encenderla.

* Si usas un sistema que no admite un botón de apagado, mantén el botón presionado durante 5 segundos para forzar un apagado completo y presiónalo una vez para encenderlo nuevamente.

3. Sobre la dirección del flujo de aire
----------------------------------------------

El flujo de aire en el chasis del Pironman 5 está diseñado cuidadosamente para maximizar la eficiencia de enfriamiento. El aire fresco entra al chasis principalmente a través de la interfaz GPIO y otras pequeñas aberturas, asegurando una entrada uniforme. Luego pasa a través del Tool Cooler, equipado con un ventilador de alto rendimiento para regular la temperatura interna, y finalmente es expulsado por los dos ventiladores RGB en el panel lateral.

Para una demostración detallada, consulta el video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Tu navegador no admite la etiqueta de video.
        </video>
    </div>

4. Sobre los extremos de los tubos de cobre del Tower Cooler
-----------------------------------------------------------------

Los tubos de calor en forma de U en la parte superior del Tower Cooler están comprimidos para facilitar el paso de los tubos de cobre a través de las aletas de aluminio, lo cual forma parte del proceso normal de fabricación.

   .. image::  img/tower_cooler1.png

5. Sobre el Raspberry Pi AI HAT+
------------------------------------------------------------

El Raspberry Pi AI HAT+ no es compatible con el Pironman 5.

   .. image::  img/output3.png
        :width: 400

El kit de inteligencia artificial de Raspberry Pi combina el M.2 HAT+ de Raspberry Pi y el módulo acelerador de inteligencia artificial Hailo.

   .. image::  img/output2.jpg
        :width: 400

Puedes desconectar el módulo acelerador de IA Hailo del kit de IA de Raspberry Pi e insertarlo directamente en el módulo NVMe PIP del Pironman 5.

   .. image::  img/output4.png
        :width: 800

6. ¿El Pironman 5 es compatible con sistemas de juegos retro?
-------------------------------------------------------------------
Sí, es compatible. Sin embargo, la mayoría de los sistemas de juegos retro son versiones simplificadas que no pueden instalar ni ejecutar software adicional. Esta limitación puede hacer que algunos componentes del Pironman 5, como la pantalla OLED, los dos ventiladores RGB y los 4 LEDs RGB, no funcionen correctamente, ya que requieren la instalación de paquetes de software del Pironman 5.

.. note::

   El sistema Batocera.linux ahora es totalmente compatible con el Pironman 5. Batocera.linux es una distribución de juegos retro de código abierto completamente gratuita.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

7. ¿Pantalla OLED no funciona?
-----------------------------------

Si la pantalla OLED no muestra nada o lo hace de manera incorrecta, sigue estos pasos de solución de problemas:

#. Asegúrate de que el cable FPC de la pantalla OLED esté conectado de forma segura. Se recomienda reconectar la pantalla OLED y luego encender el dispositivo.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

#. Confirma que el Raspberry Pi esté ejecutando un sistema operativo compatible. El Pironman 5 solo admite los siguientes sistemas:

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Si instalaste un sistema no compatible, sigue la guía para instalar un sistema operativo compatible: :ref:`install_the_os`.

#. Al encender la pantalla OLED por primera vez, es posible que solo muestre bloques de píxeles. Sigue las instrucciones en :ref:`set_up_pironman5` para completar la configuración y que pueda mostrar información correctamente.

#. Utiliza el siguiente comando para verificar si se detecta la dirección I2C ``0x3C`` de la OLED:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Si se detecta la dirección I2C ``0x3C``, reinicia el servicio Pironman 5 usando este comando:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Habilita I2C si no se detecta la dirección:

     * Edita el archivo de configuración ejecutando:

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Agrega la siguiente línea al final del archivo:

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Guarda el archivo presionando ``Ctrl+X``, luego ``Y`` y sal. Reinicia el Pironman 5 y verifica si el problema se ha resuelto.

Si el problema persiste después de realizar los pasos anteriores, envía un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.

8. ¿El módulo NVMe PIP no funciona? 
---------------------------------------

1. Asegúrate de que el cable FPC que conecta el módulo NVMe PIP al Raspberry Pi 5 esté conectado de forma segura.

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

2. Confirma que tu SSD esté correctamente asegurado al módulo NVMe PIP.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

3. Verifica el estado de los LEDs del módulo NVMe PIP:

   Después de confirmar todas las conexiones, enciende el Pironman 5 y observa los dos indicadores en el módulo NVMe PIP:

   * **PWR LED**: Debería estar encendido.
   * **STA LED**: Debería parpadear para indicar un funcionamiento normal.

   .. image:: img/nvme_pip_leds.png  

   * Si el **PWR LED** está encendido pero el **STA LED** no parpadea, indica que el NVMe SSD no es reconocido por el Raspberry Pi.  
   * Si el **PWR LED** está apagado, conecta los pines de "Force Enable" (J4) en el módulo. Si el **PWR LED** se enciende, podría indicar un cable FPC suelto o una configuración del sistema no compatible con NVMe.

     .. image:: img/nvme_pip_j4.png  

4. Confirma que tu NVMe SSD tenga un sistema operativo instalado correctamente. Consulta: :ref:`install_the_os`.

5. Si el cableado es correcto y el sistema operativo está instalado, pero el NVMe SSD aún no arranca, intenta iniciar desde una tarjeta Micro SD para verificar la funcionalidad de otros componentes. Una vez confirmado, procede a: :ref:`configure_boot_ssd`.

Si el problema persiste después de realizar los pasos anteriores, envía un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.

9. ¿Las luces RGB no funcionan?
-----------------------------------

#. Los dos pines del expansor de E/S sobre el conector J9 se utilizan para conectar las luces RGB al GPIO10. Asegúrate de que el puente en estos dos pines esté colocado correctamente.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifica que el Raspberry Pi esté ejecutando un sistema operativo compatible. El Pironman 5 solo admite las siguientes versiones de sistemas operativos:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si instalaste un sistema no compatible, sigue la guía para instalar un sistema operativo compatible: :ref:`install_the_os`.

#. Ejecuta el comando ``sudo raspi-config`` para abrir el menú de configuración. Navega a **3 Interfacing Options** -> **I3 SPI** -> **YES**, luego haz clic en **OK** y **Finish** para habilitar SPI. Después de habilitar SPI, reinicia el Pironman 5.

Si el problema persiste después de realizar los pasos anteriores, envía un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.

10. ¿El ventilador de la CPU no funciona?
----------------------------------------------

Cuando la temperatura de la CPU no ha alcanzado el umbral establecido, el ventilador de la CPU no se activa.

**Control de velocidad del ventilador basado en la temperatura**  

El ventilador PWM opera dinámicamente, ajustando su velocidad según la temperatura del Raspberry Pi 5:

* **Por debajo de 50°C**: El ventilador permanece apagado (0% de velocidad).
* **A 50°C**: El ventilador opera a baja velocidad (30% de velocidad).
* **A 60°C**: El ventilador aumenta a velocidad media (50% de velocidad).
* **A 67.5°C**: El ventilador incrementa a alta velocidad (70% de velocidad).
* **A 75°C y más**: El ventilador opera a velocidad máxima (100% de velocidad).

Para más detalles, consulta: :ref:`Fans`.

11. ¿Cómo deshabilitar el panel web?
------------------------------------------------------

Una vez que hayas completado la instalación del módulo ``pironman5``, podrás acceder al :ref:`view_control_dashboard`.

Si no necesitas esta función y deseas reducir el uso de CPU y RAM, puedes deshabilitar el panel durante la instalación del ``pironman5`` agregando el indicador ``--disable-dashboard``.

.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si ya instalaste ``pironman 5``, puedes eliminar el módulo ``dashboard`` e ``influxdb``, y luego reiniciar pironman5 para aplicar los cambios:

.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

12. ¿Cómo controlar los componentes usando el comando ``pironman5``?
-----------------------------------------------------------------------

Puedes consultar el siguiente tutorial para controlar los componentes del Pironman 5 usando el comando ``pironman5``.

* :ref:`view_control_commands`

13. ¿Cómo cambiar el orden de arranque del Raspberry Pi usando comandos?
----------------------------------------------------------------------------

Si ya iniciaste sesión en tu Raspberry Pi, puedes cambiar el orden de arranque usando comandos. Las instrucciones detalladas son las siguientes:

* :ref:`configure_boot_ssd`

14. ¿Cómo modificar el orden de arranque con Raspberry Pi Imager?
--------------------------------------------------------------------

Además de modificar el ``BOOT_ORDER`` en la configuración de EEPROM, también puedes usar **Raspberry Pi Imager** para cambiar el orden de arranque de tu Raspberry Pi.

Se recomienda usar una tarjeta de repuesto para este paso.

* :ref:`update_bootloader`

15. ¿Cómo copiar el sistema de la tarjeta SD a un NVMe SSD?
---------------------------------------------------------------

Si tienes un NVMe SSD pero no dispones de un adaptador para conectarlo a tu computadora, puedes instalar primero el sistema en tu tarjeta Micro SD. Una vez que el Pironman 5 inicie correctamente, puedes copiar el sistema de la tarjeta Micro SD a tu NVMe SSD. Las instrucciones detalladas son las siguientes:

* :ref:`copy_sd_to_nvme_rpi`

16. ¿Cómo retirar la película protectora de las placas acrílicas?
---------------------------------------------------------------------

En el paquete se incluyen dos paneles acrílicos, ambos cubiertos con una película protectora amarilla/transparente en ambos lados para evitar rayones. Puede resultar un poco difícil retirar la película protectora. Usa un destornillador para raspar suavemente las esquinas y luego despega cuidadosamente toda la película.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

17. ¿Cómo instalar OpenSSH a través de PowerShell?
-------------------------------------------------------

Cuando intentas conectarte a tu Raspberry Pi usando ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) y aparece el siguiente mensaje de error:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Esto significa que tu sistema operativo es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado. Debes seguir el siguiente tutorial para instalarlo manualmente.

#. Escribe ``powershell`` en el cuadro de búsqueda del escritorio de Windows, haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador`` en el menú que aparece.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Usa el siguiente comando para instalar ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Después de la instalación, se mostrará la siguiente salida.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación usando el siguiente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora se te indicará que ``OpenSSH.Client`` se ha instalado correctamente.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 
        Si no aparece el aviso anterior, significa que tu sistema Windows sigue siendo demasiado antiguo. Se recomienda instalar una herramienta SSH de terceros como |link_putty|.

6. Ahora reinicia PowerShell y continúa ejecutándolo como administrador. En este punto, podrás iniciar sesión en tu Raspberry Pi usando el comando ``ssh``, donde se te pedirá ingresar la contraseña que configuraste previamente.

   .. image:: img/powershell_login.png


18. ¿Cómo encender/apagar la pantalla OLED?
---------------------------------------------------

Puedes elegir encender o apagar la pantalla OLED mediante el panel de control o la línea de comandos.

1. Encender/apagar la pantalla OLED desde el panel de control.

   .. note::

    Antes de usar el panel de control, necesitas configurarlo en Home Assistant. Consulta: :ref:`view_control_dashboard`.

- Una vez completada la configuración, puedes seguir estos pasos para encender, apagar o configurar tu pantalla OLED.

   .. image:: img/set_up_on_dashboard.jpg
      :width: 90%

2. Encender/apagar la pantalla OLED desde la línea de comandos.

- Usa cualquiera de los siguientes cinco comandos para encender la pantalla OLED.

.. code-block::

    sudo pironman5 -oe True/true/on/On/1

- Usa cualquiera de los siguientes cinco comandos para apagar la pantalla OLED.

.. code-block::

    sudo pironman5 -oe False/false/off/Off/0

.. note::

    Es posible que necesites reiniciar el servicio pironman5 para que los cambios surtan efecto. Usa el siguiente comando para reiniciar el servicio:

      .. code-block::

        sudo systemctl restart pironman5.service
