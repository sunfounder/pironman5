.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Soluciona problemas técnicos y postventa con el apoyo de nuestro equipo y comunidad.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede antes que nadie a nuevos lanzamientos y adelantos de productos.
    - **Descuentos especiales**: Aprovecha ofertas exclusivas en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para descubrir y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Instalar Raspberry Pi OS
================================================================================

Puedes elegir el método de instalación según tengas a mano una tarjeta Micro SD o un SSD NVMe.

* La instalación directa en un SSD NVMe implica un paso adicional en comparación con la instalación en una tarjeta Micro SD: es necesario actualizar el bootloader de la Raspberry Pi, ya que por defecto está configurado para arrancar desde la tarjeta Micro SD. Actualiza el bootloader para que priorice el arranque desde el SSD NVMe.
* Si tienes un SSD NVMe pero no cuentas con un adaptador para conectarlo a tu ordenador, considera una tercera opción: primero instala el sistema en la tarjeta Micro SD. Una vez que el Pironman 5 haya iniciado correctamente, podrás copiar el sistema desde la Micro SD al SSD NVMe.


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi