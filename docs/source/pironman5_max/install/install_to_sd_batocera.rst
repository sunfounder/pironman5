.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Learn & Share**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato ai nuovi annunci di prodotto e alle anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway speciali.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _max_install_to_sd_ubuntu:

Installazione del sistema operativo su scheda Micro SD
===============================================================

Se stai utilizzando una scheda Micro SD, puoi seguire il tutorial qui sotto per installare il sistema operativo sulla scheda.


**Componenti necessari**

* Un computer personale
* Una scheda Micro SD e un lettore


**Procedura**

#. Vai alla pagina |link_batocera_download|, seleziona **Raspberry Pi 5 B** e clicca per avviare il download.

   .. image:: img/batocera_download.png
      :width: 90%

#. Estrai il file scaricato ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Inserisci la tua scheda SD nel computer tramite un lettore.

#. All’interno di |link_rpi_imager|, clicca sulla scheda **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo alla pagina e seleziona **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. Seleziona il file di sistema appena estratto, ``batocera-xxx-xx-xxxxxxxx.img``, e clicca su **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Clicca su **Choose Storage** e seleziona il dispositivo di archiviazione corretto per l’installazione.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ora clicca su **NEXT**. Se il dispositivo contiene già dei dati, assicurati di eseguire un backup. Se non è necessario, clicca su **Yes** per procedere.

   .. image:: img/os_continue.png
      :width: 90%


#. Quando appare il messaggio "Write Successful", significa che l'immagine è stata scritta e verificata correttamente. Ora sei pronto per avviare il Raspberry Pi dalla scheda Micro SD!
