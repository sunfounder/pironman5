.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_pironman5_5:

4. Configurar o Instalar Software
================================================

Una vez que el sistema se haya escrito en la Micro SD o el NVMe SSD, puedes insertarlos en la ranura del Pironman 5. Luego, presiona el botón de encendido para encender el dispositivo.

Después de encenderlo, verás que se iluminan varios LEDs de encendido, pero la pantalla OLED, los LEDs RGB y los ventiladores RGB (los dos ventiladores en el lateral) aún no estarán operativos, ya que necesitan ser configurados. Si experimentas un problema de distorsión en la pantalla, ignóralo por ahora; se resolverá después de la configuración.

Antes de configurar, necesitas iniciar sesión en tu Raspberry Pi. Si no estás seguro de cómo iniciar sesión, puedes visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.

Luego, puedes proceder a seleccionar el tutorial de configuración según tu sistema.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel
    set_up_batocera


**Acerca del botón de encendido**

El botón de encendido replica la función del botón de encendido del Raspberry Pi 5, y su funcionalidad es similar al del Raspberry Pi 5.

* **Apagado**

  * Si utilizas el sistema **Raspberry Pi OS Desktop**, puedes presionar dos veces rápidamente el botón de encendido para apagarlo.
  * Si utilizas el sistema **Raspberry Pi OS Lite** sin escritorio, presiona una vez el botón de encendido para iniciar el apagado.
  * Para forzar un apagado, mantén presionado el botón de encendido.

* **Encendido**

  * Si la placa Raspberry Pi está apagada pero sigue recibiendo energía, presiona el botón una sola vez para encenderla desde un estado de apagado.

* Si estás ejecutando un sistema que no admite un botón de apagado, puedes mantener presionado el botón durante 5 segundos para forzar un apagado forzoso y presionar una vez para encender desde un estado de apagado.

