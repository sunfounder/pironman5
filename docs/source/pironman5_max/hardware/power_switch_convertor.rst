.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Convertidor de Interruptor de Encendido
==============================================

Este es un módulo que extiende el interruptor de encendido de la Raspberry Pi 5 hacia el exterior.

.. image:: img/power_switch_conventor.jpeg

**Añadiendo el Botón de Encendido**

* La Raspberry Pi 5 cuenta con un puente **J2**, situado entre el conector de la batería RTC y el borde de la placa. Esta expansión permite añadir un botón de encendido personalizado a la Raspberry Pi 5 conectando un interruptor momentáneo Normalmente Abierto (NO) a través de los dos pines. Presionar brevemente este interruptor simula la funcionalidad del botón de encendido integrado.

   .. image:: img/pi5_j2.jpg

* En el Pironman 5, hay un **Convertidor de Interruptor de Encendido** que extiende el puente **J2** a un botón de encendido externo usando dos pines Pogo.

   .. image:: img/power_switch_convertor.png

* Ahora, la Raspberry Pi 5 puede encenderse y apagarse usando el Botón de Encendido.

   .. image:: img/pironman_button.JPG

**Ciclo de Encendido**

Al encender inicialmente tu Raspberry Pi 5, se encenderá automáticamente e iniciará el sistema operativo sin necesidad de presionar el botón.

Si estás ejecutando el Escritorio de Raspberry Pi, una breve pulsación del botón de encendido inicia un proceso de apagado limpio. Aparecerá un menú ofreciendo opciones para apagar, reiniciar o cerrar sesión. Seleccionar una opción o presionar el botón de encendido nuevamente iniciará un apagado limpio.

.. image:: img/button_shutdown.png

**Apagado**

    * Si ejecutas el sistema **Raspberry Pi OS Desktop**, puedes presionar el botón de encendido dos veces en rápida sucesión para apagar.
    * Si ejecutas el sistema **Raspberry Pi OS Lite** sin escritorio, presiona el botón de encendido una sola vez para iniciar el apagado.
    * Para forzar un apagado brusco, mantén presionado el botón de encendido.

**Encendido**

    * Si la placa Raspberry Pi está apagada pero aún recibe alimentación, presiona una vez para encender desde el estado de apagado.

.. note::

    Si estás ejecutando un sistema que no soporta un botón de apagado, puedes mantenerlo presionado durante 5 segundos para forzar un apagado brusco, y presionar una vez para encender desde el estado de apagado.
