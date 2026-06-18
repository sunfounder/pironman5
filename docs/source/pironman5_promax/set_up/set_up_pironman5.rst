.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_pironman5:

4. Configurare o Installare il Software
================================================

Ora che il sistema è stato scritto sulla Micro SD o sull'SSD NVMe, puoi inserirli nello slot del Pironman 5 Pro MAX. Quindi premi il pulsante di accensione per accendere il dispositivo.

Dopo l'accensione, vedrai i vari LED di alimentazione accendersi, ma lo schermo OLED, i LED RGB e le ventole GPIO (le due ventole laterali) non saranno ancora operativi, poiché necessitano di configurazione. Se c'è un problema di distorsione dello schermo, ignorarlo per ora; verrà risolto dopo la configurazione.

Prima di configurare, devi avviare e accedere al tuo Raspberry Pi. Se non sei sicuro di come accedere, puoi visitare il sito web ufficiale di Raspberry Pi: |link_rpi_get_start|.

Puoi quindi procedere a selezionare il tutorial di configurazione in base al tuo sistema.

.. toctree::
    :maxdepth: 1

    set_up_rpi_os
    set_up_umbrel

.. set_up_batocera

.. set_up_home_assistant

**Informazioni sul Pulsante di Accensione**

Il pulsante di accensione richiama il pulsante di accensione del Raspberry Pi 5 e funziona esattamente come il pulsante di accensione del Raspberry Pi 5.

* **Spegnimento**

    * Se esegui il sistema **Raspberry Pi OS Desktop**, puoi premere il pulsante di accensione due volte rapidamente per spegnere.
    * Se esegui il sistema **Raspberry Pi OS Lite**, premi il pulsante di accensione una volta per avviare lo spegnimento.
    * Per forzare uno spegnimento brusco, tieni premuto il pulsante di accensione.

* **Accensione**

    * Se la scheda Raspberry Pi è spenta, ma ancora alimentata, premi una volta per accendere da uno stato di spegnimento.

* Se stai eseguendo un sistema che non supporta un pulsante di spegnimento, puoi tenerlo premuto per 5 secondi per forzare uno spegnimento brusco, e premerlo una volta per accendere da uno stato di spegnimento.