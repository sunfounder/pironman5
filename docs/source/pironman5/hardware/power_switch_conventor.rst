.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Convertitore Interruttore di Alimentazione
================================================

Questo è un modulo che estende l'interruttore di alimentazione del Raspberry Pi 5 all'esterno.

.. image:: img/power_switch_conventor.jpeg

**Aggiunta del Pulsante di Alimentazione**

* Il Raspberry Pi 5 dispone di un jumper **J2**, situato tra il connettore della batteria RTC e il bordo della scheda. Questo breakout consente l'aggiunta di un pulsante di alimentazione personalizzato al Raspberry Pi 5 collegando un interruttore momentaneo Normalmente Aperto (NO) sui due pad. Premere brevemente questo interruttore simula la funzionalità del pulsante di alimentazione integrato.

   .. image:: img/pi5_j2.jpg

* Sul Pironman 5, è presente un **Convertitore Interruttore di Alimentazione** che estende il jumper **J2** a un pulsante di alimentazione esterno utilizzando due pin Pogo.

   .. image:: img/power_switch_convertor.png

* Ora, il Raspberry Pi 5 può essere acceso e spento utilizzando il pulsante di alimentazione.

   .. image:: img/pironman_button.JPG

**Ciclo di alimentazione**

All'accensione iniziale del Raspberry Pi 5, questo si accenderà automaticamente e avvierà il sistema operativo senza bisogno di premere il pulsante.

Se si utilizza il desktop Raspberry Pi, una breve pressione del pulsante di alimentazione avvia un processo di spegnimento pulito. Apparirà un menu che offre opzioni per spegnere, riavviare o disconnettersi. Selezionando un'opzione o premendo nuovamente il pulsante di alimentazione si avvierà uno spegnimento pulito.

.. image:: img/button_shutdown.png

**Spegnimento**

    * Se utilizzi il sistema **Raspberry Pi OS Desktop**, puoi premere due volte rapidamente il pulsante di alimentazione per spegnere.
    * Se utilizzi il sistema **Raspberry Pi OS Lite** senza desktop, premi una volta il pulsante di alimentazione per avviare lo spegnimento.
    * Per forzare uno spegnimento forzato, tieni premuto il pulsante di alimentazione.

**Accensione**

    * Se la scheda Raspberry Pi è spenta, ma ancora alimentata, premi una volta per accendere da uno stato di spegnimento.

.. note::

    Se stai eseguendo un sistema che non supporta il pulsante di spegnimento, puoi tenerlo premuto per 5 secondi per forzare uno spegnimento forzato e premere una volta per accendere da uno stato di spegnimento.
