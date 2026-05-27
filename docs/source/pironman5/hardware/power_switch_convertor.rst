.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


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
