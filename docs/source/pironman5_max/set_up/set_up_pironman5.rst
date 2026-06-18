.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_pironman5_max:

4. Configurazione o Installazione del Software
================================================

Una volta scritto il sistema su Micro SD o SSD NVMe, puoi inserirlo nell’apposito slot del Pironman 5 MAX e premere il pulsante di accensione per avviare il dispositivo.

Dopo l’accensione, vedrai accendersi i vari LED di alimentazione, ma lo schermo OLED, i LED RGB e le ventole GPIO (le due ventole laterali) non saranno ancora attivi, poiché necessitano di essere configurati. Se noti disturbi o glitch grafici sullo schermo, ignorali: verranno risolti dopo la configurazione.

Prima della configurazione, devi avviare e accedere al tuo Raspberry Pi. Se non sai come fare, puoi visitare il sito ufficiale Raspberry Pi: |link_rpi_get_start|.

Successivamente, scegli il tutorial di configurazione in base al sistema operativo in uso.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel


.. set_up_batocera


**Informazioni sul Pulsante di Accensione**

Il pulsante di accensione corrisponde al pulsante fisico del Raspberry Pi 5 e ne replica le funzionalità.

* **Spegnimento**

    * Se utilizzi il sistema **Raspberry Pi OS Desktop**, premi due volte in rapida successione il pulsante per spegnere il dispositivo.
    * Se utilizzi il sistema **Raspberry Pi OS Lite**, premi una sola volta per avviare lo spegnimento.
    * Per forzare lo spegnimento, tieni premuto il pulsante.

* **Accensione**

    * Se la scheda Raspberry Pi è spenta ma alimentata, premi una volta per accenderla dallo stato di spegnimento.

* Se utilizzi un sistema che non supporta il pulsante di spegnimento, tienilo premuto per 5 secondi per forzare lo spegnimento, e premi una sola volta per riaccendere.



