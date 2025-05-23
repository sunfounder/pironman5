.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más a fondo en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo especializado.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

5. Control mediante comandos o desde el panel web
=======================================================

Una vez que hayas instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente tras reiniciar el sistema.

Puedes supervisar y controlar el Pironman 5 Mini mediante comandos o accediendo al panel web desde la dirección ``http://<ip>:34001``.

.. note::

    * En el sistema **Home Assistant**, solo podrás monitorear y controlar el Pironman 5 Mini a través del panel web, accediendo a ``http://<ip>:34001``.

    .. * En el sistema **Batocera.linux**, solo es posible controlar y monitorear el Pironman 5 Mini mediante comandos. Es importante tener en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio con ``pironman5 restart`` para que tenga efecto.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands