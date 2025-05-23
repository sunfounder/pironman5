.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza tus conocimientos sobre Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con el respaldo de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para desarrollar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

5. Control con comandos o panel de control
=======================================================

Una vez que hayas instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente al reiniciar el sistema.

Puedes monitorear y controlar el Pironman 5 mediante comandos o accediendo al panel de control desde la página web en ``http://<ip>:34001``.

.. note::

    * En el sistema **Home Assistant**, solo puedes monitorear y controlar el Pironman 5 a través del panel de control accediendo a la página web en ``http://<ip>:34001``.
    * En el sistema **Batocera.linux**, solo puedes monitorear y controlar el Pironman 5 mediante comandos. Es importante tener en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio usando ``pironman5 restart`` para que los cambios surtan efecto.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands