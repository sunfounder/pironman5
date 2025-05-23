.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a nuevos anuncios y vistas previas de productos.
    - **Descuentos especiales**: Disfruta de promociones exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Para usuarios de Mac OS X
==============================

Para los usuarios de Mac OS X, SSH (Secure Shell) ofrece un método seguro y práctico para acceder y controlar remotamente una Raspberry Pi. Esto resulta especialmente útil cuando trabajas con la Raspberry Pi de forma remota o sin un monitor conectado. Utilizando la aplicación Terminal en Mac, puedes establecer esta conexión segura. El proceso implica un comando SSH que incluye el nombre de usuario y el hostname de la Raspberry Pi. Durante la primera conexión, se mostrará un aviso de seguridad que solicitará confirmar la autenticidad del dispositivo.

#. Para conectarte a la Raspberry Pi, escribe el siguiente comando SSH:

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. Aparecerá un mensaje de seguridad en tu primer inicio de sesión. Responde con **yes** para continuar.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Introduce la contraseña de tu Raspberry Pi. Ten en cuenta que no se mostrará en la pantalla mientras escribes, lo cual es una característica estándar de seguridad.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $

