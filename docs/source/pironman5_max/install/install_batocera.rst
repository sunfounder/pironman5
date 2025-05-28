.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche grazie al supporto del nostro team e della community.
    - **Learn & Share**: Condividi suggerimenti e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Accedi in anteprima a nuovi annunci di prodotto e anticipazioni esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni stagionali e giveaway speciali.

    👉 Pronto a esplorare e creare insieme a noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _max_install_batocera:

Installazione di Batocera Linux
======================================================

|link_batocera| è una distribuzione open-source e completamente gratuita per il retrogaming, che può essere copiata su una chiavetta USB o una scheda SD per trasformare qualsiasi computer o nano computer in una console da gioco, sia temporaneamente che in modo permanente.

Puoi scegliere il metodo di installazione in base al tipo di supporto che hai a disposizione: Micro SD o SSD NVMe.

L’installazione diretta su SSD NVMe richiede un passaggio aggiuntivo rispetto all’installazione su Micro SD: è necessario aggiornare il bootloader del Raspberry Pi, poiché per impostazione predefinita il sistema si avvia dalla Micro SD. Aggiorna quindi il bootloader per dare priorità all’avvio da SSD NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

