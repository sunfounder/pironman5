.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e difficoltà tecniche grazie all’aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ricevi in anticipo annunci e anticipazioni sui nuovi prodotti.
    - **Sconti speciali**: Approfitta di offerte esclusive sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e iniziative promozionali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

.. _install_to_sd_ubuntu_mini:

Installazione del sistema operativo su scheda Micro SD
=============================================================

Se stai utilizzando una scheda Micro SD, puoi seguire il tutorial qui sotto per installare il sistema direttamente sulla scheda.


**Componenti necessari**

* Un computer personale
* Una scheda Micro SD e lettore


**Passaggi**

#. Per prima cosa, vai alla pagina |link_batocera_download|, seleziona **Raspberry Pi 5 B** e clicca per scaricare.

   .. image:: img/batocera_download.png
      :width: 90%


#. Estrai il file scaricato ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Inserisci la scheda SD nel tuo computer o laptop tramite lettore.


#. All’interno di |link_rpi_imager|, clicca sulla scheda **Operating System**.


   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo alla pagina e seleziona **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. Seleziona il file di sistema appena estratto, ``batocera-xxx-xx-xxxxxxxx.img``, e poi clicca su **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Clicca su **Choose Storage** e seleziona il dispositivo di archiviazione corretto per l’installazione.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ora clicca su **NEXT**. Se il dispositivo contiene dati, assicurati di eseguire un backup per evitarne la perdita. Se non è necessario, clicca su **Yes** per continuare.

   .. image:: img/os_continue.png
      :width: 90%


#. Quando compare il messaggio "Write Successful", l’immagine è stata scritta e verificata correttamente. Ora sei pronto ad avviare il Raspberry Pi dalla scheda Micro SD!
