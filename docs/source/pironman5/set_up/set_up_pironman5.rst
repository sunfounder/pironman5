.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme agli altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni speciali per le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _set_up_pironman5:

4. Configurazione o installazione del software
====================================================

Ora che il sistema è stato scritto sulla Micro SD o sull'SSD NVMe, puoi inserirli nello slot di Pironman 5. Successivamente, premi il pulsante di accensione per accendere il dispositivo.

Dopo l'accensione, vedrai che i vari LED di alimentazione si illuminano, ma lo schermo OLED, i LED RGB e le ventole RGB (le due ventole laterali) non saranno ancora operativi, poiché necessitano di essere configurati. Se ci sono problemi di distorsione sullo schermo, ignora temporaneamente il problema; verrà risolto dopo la configurazione.

Prima di procedere con la configurazione, devi avviare e accedere al tuo Raspberry Pi. Se non sei sicuro di come accedere, puoi visitare il sito ufficiale di Raspberry Pi: |link_rpi_get_start|.

Puoi quindi procedere selezionando il tutorial di configurazione in base al tuo sistema.

.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel




**Informazioni sul pulsante di accensione**

Il pulsante di accensione riproduce la funzione del pulsante di accensione del Raspberry Pi 5 e si comporta esattamente come il pulsante di accensione del Raspberry Pi 5.

* **Spegnimento**

  * Se utilizzi il sistema **Raspberry Pi OS Desktop**, puoi premere il pulsante di accensione due volte in rapida successione per spegnere.  
  * Se utilizzi il sistema **Raspberry Pi OS Lite**, premi il pulsante di accensione una sola volta per avviare lo spegnimento.
  * Per forzare uno spegnimento immediato, tieni premuto il pulsante di accensione.

* **Accensione**

  * Se la scheda Raspberry Pi è spenta ma ancora alimentata, premi una sola volta per riaccendere da uno stato di spegnimento.

* Se utilizzi un sistema che non supporta il pulsante di spegnimento, puoi tenerlo premuto per 5 secondi per forzare uno spegnimento immediato e poi premerlo una volta per riaccendere da uno stato di spegnimento.

