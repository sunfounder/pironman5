.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

5. Control con Comandos o Panel de Control
=======================================================

Una vez que hayas instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente al reiniciar el sistema.

Puedes monitorear y controlar el Pironman 5 mediante comandos o accediendo al panel de control a través de la página web en ``http://<ip>:34001``.

.. note::

    * Para el sistema **Home Assistant**, solo puedes monitorear y controlar el Pironman 5 a través del panel de control abriendo la página web en ``http://<ip>:34001``.

.. * Para el sistema **Batocera.linux**, solo puedes monitorear y controlar el Pironman 5 mediante comandos. Es importante tener en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio utilizando ``pironman5 restart`` para que los cambios surtan efecto.

.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands