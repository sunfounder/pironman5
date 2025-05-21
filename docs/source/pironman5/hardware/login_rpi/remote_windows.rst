.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Para usuarios de Windows
============================

Para los usuarios de Windows 10 o superior, el inicio de sesión remoto en una Raspberry Pi se puede lograr a través de los siguientes pasos:

#. Busca ``powershell`` en la barra de búsqueda de Windows. Haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Determina la dirección IP de tu Raspberry Pi escribiendo ``ping -4 <nombre_de_host>.local`` en PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   La dirección IP de la Raspberry Pi se mostrará una vez que esté conectada a la red.

   * Si la terminal muestra ``Ping request could not find host pi.local. Please check the name and try again.``, verifica que el nombre de host ingresado sea correcto.
   * Si aún no se puede obtener la dirección IP, revisa la configuración de red o WiFi en la Raspberry Pi.

#. Una vez confirmada la dirección IP, inicia sesión en tu Raspberry Pi usando ``ssh <nombre_de_usuario>@<nombre_de_host>.local`` o ``ssh <nombre_de_usuario>@<dirección_IP>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si aparece un error que dice ``The term 'ssh' is not recognized as the name of a cmdlet...``, es posible que tu sistema no tenga las herramientas SSH preinstaladas. En este caso, deberás instalar OpenSSH manualmente siguiendo :ref:`openssh_powershell` , o usar una herramienta de terceros como |link_putty|.

#. Aparecerá un mensaje de seguridad en tu primer inicio de sesión. Escribe ``yes`` para continuar.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Ingresa la contraseña que configuraste previamente. Ten en cuenta que los caracteres de la contraseña no se mostrarán en la pantalla, lo cual es una característica de seguridad estándar.

    .. note::
        La ausencia de caracteres visibles al escribir la contraseña es normal. Asegúrate de ingresar la contraseña correcta.

#. Una vez conectado, tu Raspberry Pi estará lista para operaciones remotas.

   .. image:: img/sp221221_140628.png
      :width: 90%
      
