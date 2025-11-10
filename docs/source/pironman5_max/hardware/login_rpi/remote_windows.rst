.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las fiestas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Para usuarios de Windows
=========================

Para usuarios de Windows 10 o superior, el acceso remoto a una Raspberry Pi se puede lograr siguiendo estos pasos:

#. Escribe ``powershell`` en el cuadro de búsqueda de Windows. Haz clic derecho sobre ``Windows PowerShell`` y selecciona ``Ejecutar como administrador``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Determina la dirección IP de tu Raspberry Pi escribiendo ``ping -4 <hostname>.local`` en PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%


   La dirección IP de la Raspberry Pi aparecerá una vez esté conectada a la red.

   * Si la terminal muestra el mensaje ``Ping request could not find host pi.local. Please check the name and try again.``, verifica que el nombre del host sea correcto.
   * Si aún no puedes obtener la dirección IP, revisa la configuración de red o WiFi de tu Raspberry Pi.

#. Una vez confirmada la dirección IP, accede a tu Raspberry Pi usando ``ssh <username>@<hostname>.local`` o ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si aparece un error como ``The term 'ssh' is not recognized as the name of a cmdlet...``, es posible que tu sistema no tenga herramientas SSH preinstaladas. En ese caso, instala OpenSSH manualmente siguiendo :ref:`max_openssh_powershell`, o utiliza una herramienta externa como |link_putty|.

#. En tu primer inicio de sesión, aparecerá un mensaje de seguridad. Escribe ``yes`` para continuar.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Introduce la contraseña que configuraste anteriormente. Ten en cuenta que, por motivos de seguridad, los caracteres no se mostrarán mientras escribes.

    .. note::
        Es normal que la contraseña no se visualice al escribirla. Asegúrate de introducirla correctamente.

#. Una vez conectado, tu Raspberry Pi estará lista para operar de forma remota.

   .. image:: img/sp221221_140628.png
      :width: 90%

