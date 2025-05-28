.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche grazie al supporto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e iniziative promozionali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

.. _install_to_nvme_ubuntu_mini:

Installazione del sistema operativo su SSD NVMe
==========================================================

Se stai utilizzando un SSD NVMe e disponi di un adattatore per collegarlo al computer, puoi seguire il tutorial seguente per una rapida installazione del sistema operativo.

**Componenti necessari**

* Un computer personale
* Un SSD NVMe
* Un adattatore da NVMe a USB
* Una scheda Micro SD e un lettore

.. _update_bootloader_mini:

1. Aggiornare il Bootloader
----------------------------------

Per prima cosa, è necessario aggiornare il bootloader del Raspberry Pi 5 per consentire l’avvio da NVMe prima di tentare USB e poi SD Card.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Per questo passaggio, si consiglia di utilizzare una scheda Micro SD di riserva. Scrivi prima il bootloader su questa scheda, poi inseriscila subito nel Raspberry Pi per abilitare l’avvio da dispositivo NVMe.

    In alternativa, puoi scrivere il bootloader direttamente sul tuo dispositivo NVMe, poi inserirlo nel Raspberry Pi per modificare il metodo di avvio. Successivamente, collega l’SSD NVMe al computer per installare il sistema operativo. Una volta completata l’installazione, reinseriscilo nel Raspberry Pi.

#. Inserisci la tua scheda Micro SD di riserva o l’SSD NVMe nel computer utilizzando un lettore.

#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Nella scheda **Operating System**, scorri verso il basso e seleziona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Seleziona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Seleziona **NVMe/USB Boot** per abilitare l’avvio da NVMe prima di USB e SD Card.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Nella sezione **Storage**, seleziona il dispositivo di archiviazione corretto.

   .. note::

      Assicurati di selezionare il dispositivo corretto. Per evitare errori, scollega eventuali dispositivi di archiviazione aggiuntivi.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ora puoi cliccare su **NEXT**. Se il dispositivo contiene dati, esegui un backup prima di continuare. Clicca su **Yes** per procedere se non necessario.

   .. image:: img/os_continue.png
      :width: 90%


#. Riceverai una conferma che **NVMe/USB Boot** è stato scritto correttamente sul dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Ora puoi inserire la scheda Micro SD o l’SSD NVMe nel Raspberry Pi. Dopo averlo alimentato con un adattatore Type C, il bootloader sarà scritto nella EEPROM del Raspberry Pi.

.. note::

    Dopo questa operazione, il Raspberry Pi si avvierà da NVMe prima di USB e SD Card.
    
    Spegni il Raspberry Pi e rimuovi la scheda Micro SD o l’SSD NVMe.


2. Installare il sistema operativo su SSD NVMe
--------------------------------------------------

Ora puoi installare il sistema operativo sul tuo SSD NVMe.

**Procedura**

#. Vai alla pagina |link_batocera_download|, seleziona **Raspberry Pi 5 B** e clicca per scaricare.

   .. image:: img/batocera_download.png
      :width: 90%


#. Estrai il file scaricato ``batocera-xxx-xx-xxxxxxxx.img.gz``.


#. Inserisci la tua SD card o SSD nel computer tramite un lettore.

#. All’interno di |link_rpi_imager|, clicca sulla scheda **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo alla pagina e seleziona **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. Scegli il file appena estratto ``batocera-xxx-xx-xxxxxxxx.img``, poi clicca su **Open**.


   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Nella sezione **Storage**, seleziona il dispositivo corretto per l’installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. Ora puoi cliccare su **NEXT**. Se il dispositivo contiene dati, effettua un backup. Clicca su **Yes** per procedere se non necessario.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Alla comparsa del messaggio "Write Successful", l’immagine è stata scritta e verificata correttamente. Ora sei pronto ad avviare il Raspberry Pi da SSD NVMe!
