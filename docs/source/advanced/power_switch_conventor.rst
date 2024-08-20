.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Power Switch Converter
==============================

Este es un módulo que expande el interruptor de encendido del Raspberry Pi 5 hacia el exterior.

.. image:: img/power_switch_conventor.jpeg

**Añadiendo el Botón de Encendido**

* El Raspberry Pi 5 cuenta con un jumper **J2**, ubicado entre el conector de la batería RTC y el borde de la placa. Este punto de conexión permite añadir un botón de encendido personalizado al Raspberry Pi 5 conectando un interruptor momentáneo de Tipo Normalmente Abierto (NO) a las dos almohadillas. Al pulsar brevemente este interruptor, se emula la funcionalidad del botón de encendido integrado.

   .. image:: img/pi5_j2.jpg

* En el Pironman 5, hay un **Convertidor de Interruptor de Encendido** que extiende el jumper **J2** a un botón de encendido externo usando dos pines Pogo.

   .. image:: img/power_switch_convertor.png

* Ahora, el Raspberry Pi 5 puede encenderse y apagarse usando el botón de encendido.

   .. image:: img/pironman_button.JPG

**Ciclo de Encendido**

Al encender inicialmente tu Raspberry Pi 5, este se activará automáticamente y arrancará el sistema operativo sin necesidad de pulsar el botón.

Si estás ejecutando Raspberry Pi Desktop, una breve pulsación del botón de encendido iniciará un proceso de apagado seguro. Aparecerá un menú que ofrecerá opciones para apagar, reiniciar o cerrar sesión. Seleccionar una opción o pulsar nuevamente el botón de encendido iniciará un apagado seguro.

.. image:: img/button_shutdown.png

**Apagado**

    * Si estás ejecutando el sistema **Bookworm Desktop** de Raspberry Pi, puedes pulsar dos veces rápidamente el botón de encendido para apagar.
    * Si estás ejecutando el sistema **Bookworm Lite** de Raspberry Pi sin escritorio, presiona el botón de encendido una sola vez para iniciar un apagado.
    * Para forzar un apagado brusco, mantén presionado el botón de encendido.


**Encendido**

    * Si la placa Raspberry Pi está apagada pero aún con alimentación, pulsa una sola vez para encenderla desde el estado de apagado.

.. note::

    Si estás ejecutando un sistema que no admite el botón de apagado, puedes mantenerlo presionado durante 5 segundos para forzar un apagado brusco, y pulsarlo una vez para encenderlo desde el estado de apagado.

