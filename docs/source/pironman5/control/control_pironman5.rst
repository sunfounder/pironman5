.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

5. Controllo tramite Comandi o Dashboard
=======================================================

Una volta installato con successo il modulo ``pironman5``, il servizio ``pironman5.service`` si avvierà automaticamente al riavvio.

Puoi monitorare e controllare il Pironman 5 tramite comandi oppure accedendo alla dashboard tramite la pagina web all'indirizzo ``http://<ip>:34001``.

.. note::

    * Per il sistema **Home Assistant**, puoi monitorare e controllare il Pironman 5 solo tramite la dashboard aprendo la pagina web all'indirizzo ``http://<ip>:34001``.
    * Per il sistema **Batocera.linux**, puoi monitorare e controllare il Pironman 5 solo tramite comandi. È importante notare che qualsiasi modifica alla configurazione richiede il riavvio del servizio utilizzando ``pironman5 restart`` affinché abbia effetto.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands