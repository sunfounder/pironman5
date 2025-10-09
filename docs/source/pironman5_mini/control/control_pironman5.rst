.. note::

    Ciao, benvenuto nella community Facebook degli appassionati di SunFounder Raspberry Pi, Arduino ed ESP32! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto del nostro team e della community.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni speciali.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _control_commands_dashboard_mini:

5. Controllo tramite Comandi o Dashboard
=======================================================

Dopo aver installato con successo il modulo ``pironman5``, il servizio ``pironman5.service`` si avvierà automaticamente al riavvio del sistema.

Puoi monitorare e controllare il Pironman 5 Mini tramite comandi, oppure accedendo alla dashboard tramite la pagina web all’indirizzo ``http://<ip>:34001``.

.. note::

    * Per il sistema **Home Assistant**, è possibile monitorare e controllare il Pironman 5 Mini solo attraverso la dashboard, accedendo alla pagina web ``http://<ip>:34001``.

    .. * Per il sistema **Batocera.linux**, il controllo e il monitoraggio del Pironman 5 Mini sono disponibili solo tramite comandi. È importante ricordare che ogni modifica alla configurazione richiede un riavvio del servizio tramite ``pironman5 restart`` per essere applicata.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands