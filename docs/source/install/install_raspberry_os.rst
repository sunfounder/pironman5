.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Instalar el Raspberry Pi OS
================================================================================

Puedes elegir el método de instalación según si tienes a mano una tarjeta Micro SD o un NVMe SSD.

* Instalar directamente en el NVMe SSD implica un paso adicional en comparación con la instalación en la tarjeta Micro SD: debes actualizar el bootloader del Raspberry Pi, ya que por defecto arranca desde la tarjeta Micro SD. Actualiza el bootloader para priorizar el arranque desde el NVMe SSD.
* Si tienes un NVMe SSD pero no dispones de un adaptador para conectarlo a tu computadora, considera la tercera opción: instalar primero el sistema en tu tarjeta Micro SD. Una vez que el Pironman 5 arranque con éxito, podrás copiar el sistema desde tu tarjeta Micro SD a tu NVMe SSD.


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi