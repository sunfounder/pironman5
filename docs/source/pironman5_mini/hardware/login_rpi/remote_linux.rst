.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a nuevos anuncios y vistas previas de productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Para usuarios de Linux/Unix
=============================

#. Localiza y abre el **Terminal** en tu sistema Linux/Unix.

#. Asegúrate de que tu Raspberry Pi esté conectada a la misma red. Verifícalo escribiendo `ping <hostname>.local`. Por ejemplo:

    .. code-block::

        ping raspberrypi.local

    Deberías ver la dirección IP de la Raspberry Pi si está correctamente conectada a la red.

    * Si el terminal muestra un mensaje como ``Ping request could not find host pi.local. Please check the name and try again.``, revisa cuidadosamente el nombre del host que ingresaste.
    * Si no puedes obtener la dirección IP, revisa la configuración de red o WiFi en la Raspberry Pi.

#. Inicia una conexión SSH escribiendo ``ssh <username>@<hostname>.local`` o ``ssh <username>@<IP address>``. Por ejemplo:

    .. code-block::

        ssh pi@raspberrypi.local

#. En el primer acceso, verás un mensaje de seguridad. Escribe ``yes`` para continuar.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Introduce la contraseña que configuraste previamente. Ten en cuenta que, por motivos de seguridad, no se mostrará ningún carácter mientras la escribes.

    .. note::
        Es normal que los caracteres de la contraseña no se muestren en la terminal. Solo asegúrate de escribirla correctamente.

#. Una vez que hayas iniciado sesión correctamente, tu Raspberry Pi estará conectada y lista para continuar con el siguiente paso.
