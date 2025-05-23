.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Para usuarios de Windows
=============================

Si utilizas Windows 10 o superior, puedes iniciar sesión de forma remota en una Raspberry Pi siguiendo estos pasos:

#. Escribe ``powershell`` en el cuadro de búsqueda de Windows. Haz clic derecho sobre ``Windows PowerShell`` y selecciona ``Ejecutar como administrador``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Determina la dirección IP de tu Raspberry Pi escribiendo ``ping -4 <hostname>.local`` en PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%


   La dirección IP de la Raspberry Pi se mostrará una vez esté conectada a la red.

   * Si la terminal muestra ``Ping request could not find host pi.local. Please check the name and try again.``, verifica que el nombre del host sea correcto.
   * Si aún no se puede obtener la dirección IP, revisa la configuración de red o Wi-Fi en la Raspberry Pi.

#. Una vez confirmada la dirección IP, inicia sesión en tu Raspberry Pi con ``ssh <username>@<hostname>.local`` o ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si aparece un error indicando ``The term 'ssh' is not recognized as the name of a cmdlet...``, es posible que tu sistema no tenga herramientas SSH preinstaladas. En ese caso, deberás instalar OpenSSH manualmente siguiendo :ref:`openssh_powershell_mini`, o usar una herramienta de terceros como |link_putty|.

#. En tu primer inicio de sesión, verás un mensaje de seguridad. Escribe ``yes`` para continuar.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Introduce la contraseña que configuraste previamente. Ten en cuenta que, por razones de seguridad, no se mostrarán caracteres al escribirla.

    .. note::
        Es completamente normal que no se muestren caracteres al introducir la contraseña. Asegúrate de ingresarla correctamente.

#. Una vez conectado, tu Raspberry Pi estará lista para ser utilizada de forma remota.

   .. image:: img/sp221221_140628.png
      :width: 90%

