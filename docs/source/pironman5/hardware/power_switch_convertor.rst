.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


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

  * Si utilizas el sistema **Raspberry Pi OS Desktop**, puedes presionar dos veces rápidamente el botón de encendido para apagarlo.
  * Si utilizas el sistema **Raspberry Pi OS Lite** sin escritorio, presiona una vez el botón de encendido para iniciar el apagado.
  * Para forzar un apagado, mantén presionado el botón de encendido.


**Encendido**

  * Si la placa Raspberry Pi está apagada pero aún con alimentación, pulsa una sola vez para encenderla desde el estado de apagado.

.. note::

    Si estás ejecutando un sistema que no admite el botón de apagado, puedes mantenerlo presionado durante 5 segundos para forzar un apagado brusco, y pulsarlo una vez para encenderlo desde el estado de apagado.

