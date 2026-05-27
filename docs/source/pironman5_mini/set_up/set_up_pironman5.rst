.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_pironman5_mini:

4. Configuración o Instalación de Software
================================================

Una vez que el sistema haya sido escrito en la tarjeta Micro SD o en el SSD NVMe, puedes insertarlo en la ranura correspondiente de la Raspberry Pi. Luego, presiona el botón de encendido para iniciar el dispositivo.

Tras encender, verás que los diferentes LEDs de alimentación se iluminan, pero los LEDs RGB y el ventilador RGB aún no estarán operativos, ya que requieren configuración previa. Si observas distorsión en la pantalla, ignórala por el momento; se solucionará después de la configuración.

Antes de proceder con la configuración, debes arrancar e iniciar sesión en tu Raspberry Pi. Si no estás seguro de cómo iniciar sesión, puedes visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.

A continuación, selecciona el tutorial de configuración según el sistema operativo que estés utilizando.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel
    set_up_batocera

**Sobre el Botón de Encendido**

El botón de encendido corresponde al botón físico de la Raspberry Pi 5 y tiene la misma funcionalidad.

* **Apagar**

    * Si estás utilizando el sistema **Raspberry Pi OS Desktop**, puedes presionar dos veces seguidas el botón de encendido para apagar.
    * Si usas **Raspberry Pi OS Lite**, presiona una sola vez para iniciar el apagado.
    * Para un apagado forzado, mantén presionado el botón de encendido.

* **Encender**

    * Si la Raspberry Pi está apagada pero sigue conectada a la fuente de alimentación, presiona una vez el botón para encenderla.

* Si estás ejecutando un sistema que no admite el botón de apagado, puedes mantenerlo presionado durante 5 segundos para forzar el apagado, y presionar una vez para encender desde el estado apagado.



