.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue capacità.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci dei nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway dedicati.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _max_install_to_nvme_ubuntu:

Installazione del sistema operativo su SSD NVMe
======================================================

Se stai utilizzando un SSD NVMe e disponi di un adattatore per collegarlo al computer, puoi seguire il tutorial qui sotto per un'installazione rapida.

**Componenti necessari**

* Un computer personale
* Un SSD NVMe
* Un adattatore NVMe-USB
* Una scheda Micro SD e un lettore

1. Aggiornare il Bootloader
----------------------------------

Per prima cosa è necessario aggiornare il bootloader del Raspberry Pi 5 per consentire l’avvio da NVMe, prima che da USB e poi da scheda SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    In questa fase si consiglia di utilizzare una scheda Micro SD di riserva. Scrivi il bootloader su questa scheda e inseriscila subito nel Raspberry Pi per abilitare l'avvio da NVMe.

    In alternativa, puoi scrivere direttamente il bootloader sul tuo dispositivo NVMe, inserirlo nel Raspberry Pi per aggiornare la modalità di avvio, quindi collegare l'SSD NVMe a un computer per installare il sistema operativo. Una volta completata l'installazione, reinseriscilo nel Raspberry Pi.

#. Inserisci la tua scheda Micro SD o SSD NVMe nel computer tramite un lettore.

#. All'interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a discesa.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Nella scheda **Operating System**, scorri verso il basso e seleziona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Seleziona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Seleziona **NVMe/USB Boot** per abilitare l’avvio del Raspberry Pi 5 da NVMe, seguito da USB e infine da SD Card.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Nell'opzione **Storage**, seleziona il dispositivo di archiviazione corretto per l'installazione.

   .. note::

      Assicurati di selezionare il dispositivo giusto. Per evitare errori, scollega eventuali altri dispositivi di archiviazione collegati.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ora puoi cliccare su **NEXT**. Se il dispositivo contiene dati importanti, esegui un backup prima di proseguire. In caso contrario, clicca su **Yes** per continuare.

   .. image:: img/os_continue.png
      :width: 90%


#. Riceverai una notifica che indica che la configurazione **NVMe/USB Boot** è stata scritta con successo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Ora puoi inserire la scheda Micro SD o l'SSD NVMe nel Raspberry Pi. Dopo averlo alimentato tramite adattatore Type C, il bootloader verrà scritto sulla EEPROM del Raspberry Pi.

.. note::

    Da questo momento in poi, il Raspberry Pi si avvierà da NVMe, poi da USB e infine da SD Card.
    
    Spegni il Raspberry Pi e rimuovi la scheda Micro SD o l’SSD NVMe.


2. Installare il sistema operativo su SSD NVMe
---------------------------------------------------

Ora puoi procedere con l'installazione del sistema operativo su SSD NVMe.

**Passaggi**

#. Accedi alla pagina |link_batocera_download|, seleziona **Raspberry Pi 5 B** e clicca per scaricare.

   .. image:: img/batocera_download.png
      :width: 90%


#. Estrai il file scaricato ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Inserisci la tua scheda SD nel computer tramite un lettore.

#. All'interno di |link_rpi_imager|, clicca sulla scheda **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo alla pagina e seleziona **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. Seleziona il file di sistema appena estratto, ``batocera-xxx-xx-xxxxxxxx.img``, e clicca su **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Nella sezione **Storage**, seleziona il dispositivo di archiviazione corretto.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. Ora puoi cliccare su **NEXT**. Se il dispositivo contiene dati, esegui un backup per evitarne la perdita. In assenza di backup, conferma cliccando su **Yes**.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Quando visualizzi il messaggio "Write Successful", l'immagine è stata scritta e verificata correttamente. Ora sei pronto per avviare il Raspberry Pi da SSD NVMe!
