.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri membri appassionati.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e difficoltà tecniche grazie al supporto del nostro team e della community.
    - **Learn & Share**: Condividi suggerimenti e tutorial per sviluppare ulteriormente le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti riservati sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway esclusivi.

    👉 Pronto a esplorare e creare insieme a noi? Clicca su [|link_sf_facebook|] e unisciti subito!

Installazione del sistema operativo Raspberry Pi
================================================================================

Puoi scegliere il metodo di installazione in base al tipo di supporto disponibile: Micro SD o SSD NVMe.

* L’installazione diretta su SSD NVMe richiede un passaggio aggiuntivo rispetto alla Micro SD: è necessario aggiornare il bootloader del Raspberry Pi, che per impostazione predefinita avvia il sistema dalla Micro SD. Aggiorna il bootloader per dare priorità all’avvio da SSD NVMe.
* Se possiedi un SSD NVMe ma non hai un adattatore per collegarlo al computer, puoi optare per la terza opzione: installa prima il sistema su una Micro SD. Una volta che il Pironman 5 si avvia correttamente, potrai copiare il sistema dalla Micro SD all’SSD NVMe.


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi