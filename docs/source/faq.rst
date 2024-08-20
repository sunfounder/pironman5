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

¿Es compatible el Pironman 5 con sistemas retro de juegos?
-----------------------------------------------------------
Sí, es compatible. Sin embargo, la mayoría de los sistemas retro de juegos son versiones simplificadas que no pueden instalar ni ejecutar software adicional. Esta limitación puede hacer que algunos componentes del Pironman 5, como la pantalla OLED, los dos ventiladores RGB y los 4 LEDs RGB, no funcionen correctamente, ya que estos componentes requieren la instalación de los paquetes de software de Pironman 5.

.. note::

    El sistema Batocera.linux ahora es completamente compatible con Pironman 5. Batocera.linux es una distribución retro de juegos de código abierto y completamente gratuita.

    * :ref:`install_batocera`
    * :ref:`set_up_batocera`

¿Cómo controlar los componentes usando el comando ``pironman5``?
------------------------------------------------------------------
Puedes consultar el siguiente tutorial para controlar los componentes del Pironman 5 utilizando el comando ``pironman5``.

* :ref:`view_control_commands`

¿Cómo cambiar el orden de arranque de la Raspberry Pi usando comandos?
------------------------------------------------------------------------
Si ya has iniciado sesión en tu Raspberry Pi, puedes cambiar el orden de arranque usando comandos. Las instrucciones detalladas son las siguientes:

* :ref:`configure_boot_ssd`

¿Cómo modificar el orden de arranque con Raspberry Pi Imager?
---------------------------------------------------------------
Además de modificar el ``BOOT_ORDER`` en la configuración del EEPROM, también puedes utilizar el **Raspberry Pi Imager** para cambiar el orden de arranque de tu Raspberry Pi.

Se recomienda usar una tarjeta de repuesto para este paso.

* :ref:`update_bootloader`

¿Cómo copiar el sistema de la tarjeta SD a un SSD NVMe?
---------------------------------------------------------
Si tienes un SSD NVMe pero no tienes un adaptador para conectarlo a tu computadora, puedes instalar primero el sistema en tu tarjeta Micro SD. Una vez que el Pironman 5 se haya iniciado correctamente, puedes copiar el sistema de tu tarjeta Micro SD a tu SSD NVMe. Las instrucciones detalladas son las siguientes:

* :ref:`copy_sd_to_nvme_rpi`

¿La pantalla OLED no funciona?
--------------------------------
Si la pantalla OLED no muestra nada o muestra incorrectamente, puedes seguir estos pasos para solucionar el problema:

Verifica si el cable FPC de la pantalla OLED está correctamente conectado.

#. Utiliza el siguiente comando para ver los registros del programa y comprobar si hay mensajes de error.

   .. code-block:: shell

      cat /opt/pironman5/log

#. Alternativamente, utiliza el siguiente comando para verificar si la dirección i2c 0x3C de la OLED es reconocida:

   .. code-block:: shell

      sudo i2cdetect -y 1

#. Si los primeros dos pasos no revelan ningún problema, intenta reiniciar el servicio pironman5 para ver si se resuelve el problema.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

.. _openssh_powershell:

Instalar OpenSSH a través de Powershell
-------------------------------------------
Cuando utilizas ``ssh <usuario>@<nombrehost>.local`` (o ``ssh <usuario>@<dirección IP>``) para conectarte a tu Raspberry Pi, pero aparece el siguiente mensaje de error.

    .. code-block::

        ssh: El término 'ssh' no se reconoce como el nombre de un cmdlet, función, archivo de script o programa ejecutable. Verifica la ortografía del nombre o, si se incluyó una ruta, asegúrate de que la ruta sea correcta e inténtalo de nuevo.

Significa que tu sistema es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado, por lo que necesitas seguir el tutorial a continuación para instalarlo manualmente.

#. Escribe ``powershell`` en el cuadro de búsqueda de tu escritorio de Windows, haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador`` en el menú que aparece.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Utiliza el siguiente comando para instalar ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Después de la instalación, se devolverá el siguiente resultado.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación utilizando el siguiente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora te indicará que ``OpenSSH.Client`` se ha instalado correctamente.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 
        Si no aparece el mensaje anterior, significa que tu sistema Windows sigue siendo demasiado antiguo y se te recomienda instalar una herramienta SSH de terceros, como |link_putty|.

#. Ahora reinicia PowerShell y ejecútalo nuevamente como administrador. En este punto, podrás iniciar sesión en tu Raspberry Pi utilizando el comando ``ssh``, donde se te pedirá que ingreses la contraseña que configuraste anteriormente.

   .. image:: img/powershell_login.png
