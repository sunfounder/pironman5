.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


USB-HDMI-Adapter
==========================================

.. image:: img/hdmi_adapter.jpeg

Dieses USB-HDMI-Adapterboard wurde speziell für den Raspberry Pi 5 entwickelt. Seine Hauptfunktion besteht darin, die USB- und HDMI-Anschlüsse neu zu positionieren, um sie auf die Seite mit der USB-Schnittstelle des Raspberry Pi auszurichten, was die Zugänglichkeit und das Kabelmanagement verbessert.

Zusätzlich wird der HDMI-Anschluss in eine Standard-HDMI-Typ-A-Schnittstelle umgewandelt, was eine breitere Kompatibilität bietet.

**Zusätzliche NVMe-Stromversorgung**

Das Board verfügt über einen 5V-Stromanschluss, der speziell für die NVMe PIP-Stromversorgung vorgesehen ist. Zusammen mit einem Erweiterungsheader kann es an die zusätzliche Stromschnittstelle des NVMe angeschlossen werden, um zusätzliche Leistung bereitzustellen.

**1220RTC-Batteriehalter**

Ein 1220RTC-Batteriehalter ist integriert, um die Installation einer RTC-Batterie zu erleichtern. Er wird über ein umgekehrtes SH1.0-2P-Kabel mit der RTC-Schnittstelle des Raspberry Pi verbunden.

Der Batteriehalter ist sowohl mit CR1220- als auch mit ML1220-Batterien kompatibel. Wenn eine ML1220 (Lithium-Mangandioxid-Batterie) verwendet wird, kann das Laden direkt auf dem Raspberry Pi konfiguriert werden. Beachten Sie, dass die CR1220 nicht wiederaufladbar ist.

**Aktivierung des Erhaltungsladens**

.. warning::

  Wenn Sie eine CR1220-Batterie verwenden, aktivieren Sie das Erhaltungsladen nicht, da dies die Batterie irreparabel beschädigen und die Platine gefährden kann.

Standardmäßig ist das Erhaltungsladen für die Batterie deaktiviert. Die ``sysfs``-Dateien zeigen die aktuelle Erhaltungsladespannung und die Grenzwerte an:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Um das Erhaltungsladen zu aktivieren, fügen Sie ``rtc_bbat_vchg`` in ``/boot/firmware/config.txt`` hinzu:

  * Öffnen Sie die Datei ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
  * Fügen Sie ``rtc_bbat_vchg`` in ``/boot/firmware/config.txt`` hinzu.
  
    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
Nach dem Neustart wird das System folgendes anzeigen:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Dies bestätigt, dass die Batterie nun im Erhaltungsladen ist. Um diese Funktion zu deaktivieren, entfernen Sie einfach die ``dtparam``-Zeile aus der ``config.txt``.
