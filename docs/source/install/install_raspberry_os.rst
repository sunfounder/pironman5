.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Installa Raspberry Pi OS
================================================================================

Puoi scegliere il metodo di installazione in base al fatto che tu disponga di una Micro SD o di un SSD NVMe.

* L'installazione diretta sull'SSD NVMe comporta un passaggio aggiuntivo rispetto all'installazione su Micro SD: è necessario aggiornare il bootloader del Raspberry Pi perché, per impostazione predefinita, avvia il sistema dalla Micro SD. Aggiorna il bootloader per dare priorità all'avvio dall'SSD NVMe.
* Se hai un SSD NVMe ma non hai un adattatore per collegare il tuo NVMe al computer, considera la terza opzione di installare prima il sistema sulla tua scheda Micro SD. Una volta che il Pironman 5 si avvia correttamente, puoi copiare il sistema dalla tua Micro SD al tuo SSD NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi