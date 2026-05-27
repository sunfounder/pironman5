.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Adattatore USB HDMI
==========================================

.. image:: img/hdmi_adapter.jpeg

Questo adattatore USB HDMI è progettato specificamente per il Raspberry Pi 5. La sua funzione principale è riposizionare le connessioni USB e HDMI in modo che siano allineate con il lato dell'interfaccia USB del Raspberry Pi, migliorando l'accessibilità e la gestione dei cavi.

Inoltre, la porta HDMI viene convertita in un'interfaccia HDMI standard di tipo A, offrendo una compatibilità più ampia.

**Alimentazione aggiuntiva per NVMe**

La scheda è dotata di un connettore di alimentazione a 5V specificamente per l'alimentazione NVMe PIP. Insieme a un connettore di estensione, può essere collegata all'interfaccia di alimentazione aggiuntiva dell'NVMe per fornire ulteriore potenza.

**Portabatteria 1220RTC**

Un portabatteria 1220RTC è incorporato per l'installazione comoda di una batteria RTC. Si collega all'interfaccia RTC del Raspberry Pi tramite un cavo SH1.0 2P inverso.

Il portabatteria è compatibile con le batterie CR1220 e ML1220. Se si utilizza una ML1220 (batteria al biossido di manganese al litio), la ricarica può essere configurata direttamente sul Raspberry Pi. Nota che la CR1220 non è ricaricabile.

**Abilitazione della ricarica lenta**

.. warning::

  Se stai usando una batteria CR1220, non abilitare la ricarica lenta poiché potrebbe causare danni irreparabili alla batteria e mettere a rischio la scheda.

Per impostazione predefinita, la funzione di ricarica lenta per la batteria è disabilitata. I file ``sysfs`` indicano la tensione e i limiti di ricarica lenta attuali:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Per abilitare la ricarica lenta, aggiungi ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``:

  * Apri ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
  * Aggiungi ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
Dopo il riavvio, il sistema visualizzerà:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Questo conferma che la batteria è ora sotto ricarica lenta. Per disabilitare questa funzione, basta rimuovere la riga ``dtparam`` da ``config.txt``.

