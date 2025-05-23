.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el universo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados de la tecnología.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y posventa con la ayuda de nuestro equipo y comunidad.
    - **Aprende y comparte**: Intercambia consejos, experiencias y tutoriales que potenciarán tus conocimientos.
    - **Avances exclusivos**: Accede antes que nadie a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros últimos lanzamientos.
    - **Promociones festivas y sorteos**: Participa en promociones especiales y sorteos durante todo el año.

    👉 ¿Listo para descubrir y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_install_batocera:

Instalar Batocera Linux
======================================================

|link_batocera| es una distribución de retro-gaming completamente gratuita y de código abierto, diseñada para ser copiada en una memoria USB o tarjeta SD con el objetivo de convertir cualquier ordenador o nanoordenador en una consola de videojuegos —ya sea de forma temporal o permanente— con una experiencia optimizada para emulación.

Puedes elegir el método de instalación en función del soporte de almacenamiento disponible: una tarjeta Micro SD o un SSD NVMe.

La instalación directa en un SSD NVMe requiere un paso adicional en comparación con la instalación en Micro SD: debes actualizar el bootloader de la Raspberry Pi, ya que por defecto está configurada para arrancar desde la tarjeta Micro SD. Es fundamental actualizar el bootloader para que priorice el arranque desde el SSD NVMe y garantice una correcta inicialización del sistema.

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

