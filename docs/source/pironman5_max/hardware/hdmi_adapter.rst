.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e condividi**: Condividi suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra a far parte della community oggi stesso!

Adattatore USB HDMI
==========================================

.. image:: img/hdmi_adapter.jpeg

Questa scheda adattatore USB HDMI è progettata specificamente per il Raspberry Pi 5. La sua funzione principale è riposizionare le connessioni USB e HDMI sul lato dell'interfaccia USB del Raspberry Pi, migliorando così l’accessibilità e la gestione dei cavi.

Inoltre, la porta HDMI viene convertita in un’interfaccia HDMI Type A standard, offrendo una compatibilità più ampia.

**Alimentazione supplementare per NVMe**

La scheda è dotata di un connettore di alimentazione a 5V dedicato all’alimentazione del modulo NVMe PIP. Insieme a un header di estensione, può essere collegato all’interfaccia di alimentazione supplementare dell’unità NVMe per fornire potenza aggiuntiva.

**Portabatteria 1220RTC**

È incluso un portabatteria 1220RTC per facilitare l’installazione di una batteria RTC. Questo si collega all’interfaccia RTC del Raspberry Pi tramite un cavo invertito SH1.0 a 2 pin.

Il portabatteria è compatibile sia con batterie CR1220 che ML1220. Se si utilizza una ML1220 (batteria al biossido di manganese e litio), è possibile abilitare la ricarica direttamente dal Raspberry Pi. Nota: la CR1220 non è ricaricabile.

**Attivazione della carica di mantenimento (trickle charging)**

.. warning::

  Se stai utilizzando una batteria CR1220, non abilitare la carica di mantenimento: potrebbe causare danni irreparabili alla batteria e alla scheda.

Per impostazione predefinita, la carica di mantenimento è disattivata. I file ``sysfs`` mostrano la tensione di carica corrente e i limiti:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Per abilitare la carica di mantenimento, aggiungi ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``:

  * Apri il file ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
  * Aggiungi ``rtc_bbat_vchg`` al file ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
Dopo il riavvio, il sistema mostrerà:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Questo conferma che la batteria è ora in fase di carica di mantenimento. Per disattivare questa funzione, è sufficiente rimuovere la riga ``dtparam`` da ``config.txt``.

