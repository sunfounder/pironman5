.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


USB HDMI Adapter
==========================================

.. image:: img/hdmi_adapter.jpeg

Esta placa adaptadora USB HDMI está diseñada específicamente para el Raspberry Pi 5. Su función principal es reubicar las conexiones USB y HDMI para alinearlas con el lateral del Raspberry Pi donde se encuentran los puertos USB, mejorando así la accesibilidad y la gestión de cables.

Además, el puerto HDMI se convierte en una interfaz HDMI Tipo A estándar, lo que ofrece una mayor compatibilidad.

**Alimentación adicional para NVMe**

La placa incluye un conector de alimentación de 5 V destinado específicamente a suministrar energía al NVMe PIP. Combinado con un conector de extensión, permite conectar la interfaz de alimentación adicional del NVMe para proporcionar energía extra.

**Portabatería 1220RTC**

Se incorpora un portabatería 1220RTC para facilitar la instalación de una batería RTC. Este se conecta a la interfaz RTC del Raspberry Pi mediante un cable inverso SH1.0 de 2 pines.

El portabatería es compatible con baterías CR1220 y ML1220. Si se utiliza una ML1220 (batería de dióxido de manganeso-litio), la carga puede configurarse directamente en el Raspberry Pi. Ten en cuenta que la batería CR1220 no es recargable.

**Activación de la carga por goteo**

.. warning::

  Si utilizas una batería CR1220, **no** actives la carga por goteo, ya que podría causar daños irreversibles a la batería y poner en riesgo la placa.

Por defecto, la función de carga por goteo está desactivada. Los archivos de ``sysfs`` muestran el voltaje y los límites actuales para esta función:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Para habilitar la carga por goteo, añade ``rtc_bbat_vchg`` al archivo ``/boot/firmware/config.txt``:

  * Abre ``/boot/firmware/config.txt``.

    .. code-block:: shell

      sudo nano /boot/firmware/config.txt

  * Añade ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``.

    .. code-block:: shell

      dtparam=rtc_bbat_vchg=3000000

Después de reiniciar, el sistema mostrará:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Esto confirma que la batería ahora está bajo carga por goteo. Para desactivar esta función, simplemente elimina la línea ``dtparam`` del archivo ``config.txt``.

