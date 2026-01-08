.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_to_sd_home_bridge:

Installazione del sistema operativo su una scheda Micro SD
====================================================================

Se utilizzi una scheda Micro SD, puoi seguire il tutorial seguente per installare il sistema sulla tua scheda Micro SD.


**Componenti richiesti**

* Un computer personale
* Una scheda Micro SD e un lettore

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installare il sistema operativo sulla scheda microSD
--------------------------------------------------------------------------

1. Inserisci la scheda microSD nel computer utilizzando un lettore di schede.  
   Prima di procedere, esegui il backup di eventuali dati importanti presenti sulla scheda, poiché verranno cancellati.

   .. image:: img/insert_sd.png
      :width: 90%

2. Quando si apre **Raspberry Pi Imager**, vedrai la pagina **Device**.  
   Seleziona il tuo modello di **Raspberry Pi 5** dall’elenco.

   .. image:: img/imager_device.png
      :width: 90%

3. Vai alla sezione **OS**, scorri fino in fondo alla pagina e seleziona il tuo sistema operativo.

   .. note::

      * Per **Ubuntu**, fai clic su **Other general-purpose OS** → **Ubuntu**, quindi seleziona  
        **Ubuntu Desktop 24.04 LTS (64-bit)** oppure **Ubuntu Server 24.04 LTS (64-bit)**.
      * Per **Kali Linux**, **Home Assistant** e **Homebridge**, fai clic su  
        **Other specific-purpose OS**, quindi seleziona il sistema corrispondente.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Nella sezione **Storage**, seleziona la tua scheda microSD.  
   Per sicurezza, si consiglia di scollegare altri dispositivi di archiviazione USB in modo che nell’elenco compaia solo la scheda microSD.

   .. image:: img/imager_storage.png
      :width: 90%

#. Fai clic su **NEXT**.

   .. note::

      * Per i sistemi che **non possono essere preconfigurati**, facendo clic su **NEXT** verrà saltato il passaggio di **Customisation** e si passerà direttamente a **Writing**, dove il sistema operativo viene scritto sulla scheda microSD.
      * Per i sistemi che **supportano la preconfigurazione**, segui i passaggi di **Customisation** per configurare opzioni come **Hostname**, **WiFi** e **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Quando appare il popup **“Write Successful”**, l’immagine è stata completamente scritta e verificata. Ora puoi rimuovere in sicurezza la scheda microSD e utilizzarla per avviare il tuo Raspberry Pi.
