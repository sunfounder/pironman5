.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!
.. _install_batocera:

Instalar Batocera Linux
======================================================

|link_batocera| es una distribución de retro-gaming de código abierto y completamente gratuita que se puede copiar en una memoria USB o una tarjeta SD con el objetivo de convertir cualquier computadora/nano computadora en una consola de juegos, ya sea temporalmente durante un juego o de forma permanente.

Puedes elegir el método de instalación según si tienes a mano una tarjeta Micro SD o un NVMe SSD.

Instalar directamente en el NVMe SSD implica un paso adicional en comparación con la instalación en la tarjeta Micro SD: debes actualizar el bootloader del Raspberry Pi, ya que, de forma predeterminada, arranca desde la tarjeta Micro SD. Actualiza el bootloader para priorizar el arranque desde el NVMe SSD.

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

