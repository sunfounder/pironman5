.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más a fondo en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

FAQ
============

¿Cómo desactivar el panel web?
------------------------------------------------------

Una vez completada la instalación del módulo ``pironman5``, podrás acceder al :ref:`max_view_control_dashboard`.
      
Si no necesitas esta función y deseas reducir el uso de CPU y RAM, puedes desactivar el panel añadiendo el parámetro ``--disable-dashboard`` durante la instalación de ``pironman5``.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Si ya instalaste ``pironman 5``, puedes eliminar el módulo ``dashboard`` y ``influxdb``, luego reiniciar pironman5 para aplicar los cambios:
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. ¿Pironman 5 MAX es compatible con sistemas retro?
.. ------------------------------------------------------
.. Sí, es compatible. Sin embargo, la mayoría de los sistemas retro son versiones ligeras que no permiten instalar software adicional. Esta limitación puede hacer que ciertos componentes de Pironman 5 MAX, como la pantalla OLED, los dos ventiladores RGB y los 4 LEDs RGB, no funcionen correctamente, ya que requieren los paquetes de software de Pironman 5 MAX.


.. .. note::

..     El sistema Batocera.linux ahora es totalmente compatible con Pironman 5 MAX. Batocera.linux es una distribución de retro gaming de código abierto y completamente gratuita.

..     * :ref:`max_install_batocera`
..     * :ref:`max_set_up_batocera`

¿Cómo controlar los componentes con el comando ``pironman5``?
----------------------------------------------------------------------

Consulta el siguiente tutorial para controlar los componentes de Pironman 5 MAX utilizando el comando ``pironman5``.

* :ref:`max_view_control_commands`

¿Cómo cambiar el orden de arranque de Raspberry Pi usando comandos?
--------------------------------------------------------------------------

Si ya iniciaste sesión en tu Raspberry Pi, puedes cambiar el orden de arranque usando comandos. Consulta las instrucciones detalladas en:

* :ref:`max_configure_boot_ssd`


¿Cómo modificar el orden de arranque con Raspberry Pi Imager?
-------------------------------------------------------------------

Además de editar el parámetro ``BOOT_ORDER`` en la configuración de EEPROM, también puedes usar **Raspberry Pi Imager** para cambiar el orden de arranque de tu Raspberry Pi.

Se recomienda utilizar una tarjeta de repuesto para este paso.

* :ref:`max_update_bootloader`

¿Cómo copiar el sistema de la tarjeta SD a un SSD NVMe?
-------------------------------------------------------------

Si tienes un SSD NVMe pero no cuentas con un adaptador para conectarlo a tu ordenador, puedes instalar primero el sistema en una tarjeta Micro SD. Una vez que Pironman 5 MAX haya iniciado correctamente, podrás copiar el sistema de la tarjeta SD al SSD NVMe. Consulta las instrucciones detalladas:


* :ref:`max_copy_sd_to_nvme_rpi`

¿Módulo NVMe PIP no funciona?
---------------------------------------

1. Asegúrese de que el cable FPC que conecta el módulo NVMe PIP con la Raspberry Pi 5 esté bien conectado.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

2. Confirme que su SSD esté correctamente instalado en el módulo NVMe PIP.

3. Verifique el estado de los LEDs del módulo NVMe PIP:

   Después de confirmar todas las conexiones, encienda el Pironman 5 MAX y observe los dos indicadores en el módulo NVMe PIP:

   * **LED PWR**: Debe estar encendido.  
   * **LED STA**: Debe parpadear para indicar un funcionamiento normal.

   .. image:: img/dual_nvme_pip_leds.png

   * Si el **LED PWR** está encendido pero el **LED STA** no parpadea, indica que la Raspberry Pi no reconoce el SSD NVMe.  
   * Si el **LED PWR** está apagado, puentee los pines "Force Enable" en el módulo. Si el **LED PWR** se enciende, podría indicar un cable FPC flojo o una configuración del sistema no compatible con NVMe.

   .. image:: img/dual_nvme_pip_j4.png


4. Confirme que su SSD NVMe tenga un sistema operativo correctamente instalado. Consulte: :ref:`max_install_the_os`.

5. Si el cableado es correcto y el sistema operativo está instalado pero el SSD NVMe aún no arranca, intente arrancar desde una tarjeta Micro SD para verificar el funcionamiento de otros componentes. Una vez confirmado, continúe con: :ref:`max_configure_boot_ssd`.

Si el problema persiste después de realizar los pasos anteriores, envíe un correo electrónico a service@sunfounder.com. Le responderemos lo antes posible.


¿Pantalla OLED no funciona?
----------------------------

.. note:: La pantalla OLED puede apagarse automáticamente después de un período de inactividad para ahorrar energía. Puede tocar suavemente la carcasa para activar el sensor de vibración y encender la pantalla.

Si la pantalla OLED no muestra nada o muestra información incorrecta, siga estos pasos para solucionar el problema:

1. **Verifique la conexión de la pantalla OLED**

   Asegúrese de que el cable FPC de la pantalla OLED esté correctamente conectado.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Oled-11.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

2. **Verifique la compatibilidad del sistema operativo**

   Asegúrese de estar utilizando un sistema operativo compatible en su Raspberry Pi.

3. **Verifique la dirección I2C**

   Ejecute el siguiente comando para comprobar si se detecta la dirección I2C (0x3C) de la OLED:

   .. code-block:: shell

      sudo i2cdetect -y 1

   Si no se detecta la dirección, habilite I2C con el siguiente comando:

   .. code-block:: shell

      sudo raspi-config

4. **Reinicie el servicio pironman5**

   Reinicie el servicio `pironman5` para ver si se resuelve el problema:

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **Verifique el archivo de registro**

   Si el problema persiste, revise el archivo de registro para obtener mensajes de error y proporcione la información al soporte técnico para un análisis más detallado:

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log


¿Por qué se apaga automáticamente la pantalla OLED?
---------------------------------------------------------------------------------

Para ahorrar energía y prolongar la vida útil de la pantalla, la pantalla OLED se apagará automáticamente después de un período de inactividad.  
Esto forma parte del diseño normal y no afecta la funcionalidad del producto.

Simplemente presiona una vez el botón del dispositivo para reactivar la pantalla OLED y reanudar la visualización.

.. note::

   Para la configuración de la pantalla OLED (como encendido/apagado, tiempo de suspensión, rotación, etc.), consulta: :ref:`view_control_dashboard` o :ref:`view_control_commands`.


.. _max_openssh_powershell:

Instalar OpenSSH desde PowerShell
-------------------------------------

Si al usar ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) para conectarte a tu Raspberry Pi aparece el siguiente mensaje de error:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Significa que tu sistema Windows es demasiado antiguo y no trae `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado. Deberás instalarlo manualmente siguiendo este tutorial:

#. Escribe ``powershell`` en el buscador de Windows, haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Usa el siguiente comando para instalar ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Tras la instalación, verás una salida similar a esta:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación con el siguiente comando:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora verás que ``OpenSSH.Client`` está correctamente instalado.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 

        Si no aparece el mensaje anterior, significa que tu sistema es aún demasiado antiguo. En ese caso, te recomendamos usar una herramienta SSH de terceros como |link_putty|.

#. Ahora reinicia PowerShell y vuelve a ejecutarlo como administrador. Ya deberías poder iniciar sesión en tu Raspberry Pi con el comando ``ssh``, donde se te pedirá la contraseña configurada previamente.

   .. image:: img/powershell_login.png



¿Puedo seguir usando las funciones de Pironman5 si configuro OMV?
--------------------------------------------------------------------------------------------------------

Sí, OpenMediaVault se ejecuta sobre el sistema Raspberry Pi. Solo debes seguir los pasos de :ref:`max_set_up_pi_os` para continuar con la configuración.