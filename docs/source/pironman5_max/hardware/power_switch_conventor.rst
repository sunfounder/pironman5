.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Power Switch Conventor
==============================

Este es un módulo que expande el interruptor de encendido del Raspberry Pi 5 hacia el exterior.

.. image:: img/power_switch_conventor.jpeg

**Añadir el botón de encendido**

* El Raspberry Pi 5 cuenta con un jumper **J2**, ubicado entre el conector de batería RTC y el borde de la placa. Esta extensión permite añadir un botón de encendido personalizado al Raspberry Pi 5 conectando un interruptor momentáneo de tipo Normalmente Abierto (NO) entre las dos almohadillas. Al presionar brevemente este interruptor, se simula la funcionalidad del botón de encendido incorporado.

   .. image:: img/pi5_j2.jpg

* En el Pironman 5, hay un **Power Switch Converter** que extiende el jumper **J2** hacia un botón de encendido externo mediante dos pines Pogo.

   .. image:: img/power_switch_convertor.png

* Ahora, el Raspberry Pi 5 se puede encender y apagar usando el botón de encendido externo.

   .. image:: img/pironman_button.JPG

**Ciclo de encendido**

Al conectar por primera vez la alimentación al Raspberry Pi 5, este se encenderá automáticamente e iniciará el sistema operativo sin necesidad de presionar el botón.

Si estás usando Raspberry Pi Desktop, una breve pulsación del botón de encendido iniciará un proceso de apagado limpio. Aparecerá un menú con opciones para apagar, reiniciar o cerrar sesión. Seleccionar una opción o presionar nuevamente el botón iniciará el apagado limpio.

.. image:: img/button_shutdown.png

**Apagado**

  * Si utilizas el sistema **Raspberry Pi OS Desktop**, puedes presionar dos veces rápidamente el botón de encendido para apagarlo.
  * Si utilizas el sistema **Raspberry Pi OS Lite** sin escritorio, presiona una vez el botón de encendido para iniciar el apagado.
  * Para forzar un apagado, mantén presionado el botón de encendido.


**Encendido**

  * Si la placa Raspberry Pi está apagada pero aún recibe energía, basta con una sola pulsación para encenderla desde el estado de apagado.

.. note::

    Si estás utilizando un sistema que no admite el botón de apagado, puedes mantenerlo presionado durante 5 segundos para forzar un apagado completo, y luego presionarlo una vez para encenderlo desde el estado apagado.

