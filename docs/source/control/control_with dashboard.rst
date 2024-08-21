
.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _view_control_dashboard:

Visualizzazione e Controllo dalla Dashboard
====================================================

Una volta installato correttamente il modulo ``pironman5``, il servizio ``pironman5.service`` si avvierà automaticamente al riavvio.

Ora puoi aprire la pagina di monitoraggio nel browser per visualizzare le informazioni sul tuo Raspberry Pi, configurare i LED RGB e controllare la ventola, ecc. Il link della pagina è: ``http://<ip>:34001``.

Questa pagina include **Dashboard**, **Cronologia**, **Log** e una pagina di **Impostazioni**.

.. image:: img/dashboard_tab.png
  :width: 90%
  
  
Dashboard
-----------------------

Ci sono diverse schede per visualizzare lo stato del Raspberry Pi, tra cui:

* **Ventola**: Visualizza la temperatura della CPU del Raspberry Pi e la velocità della ventola PWM. **Stato Ventola GPIO** indica lo stato delle due ventole RGB laterali. Alla temperatura attuale, le due ventole RGB sono spente.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Archiviazione**: Mostra la capacità di archiviazione di un Raspberry Pi, visualizzando le varie partizioni del disco con lo spazio utilizzato e disponibile.

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Memoria**: Mostra l'utilizzo e la percentuale di RAM del Raspberry Pi.

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Rete**: Mostra il tipo di connessione di rete corrente, la velocità di upload e download.

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Processore**: Illustra le prestazioni della CPU del Raspberry Pi, incluso lo stato dei suoi quattro core, le frequenze operative e la percentuale di utilizzo della CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

Cronologia
----------------

La pagina Cronologia ti consente di visualizzare i dati storici. Seleziona i dati che desideri visualizzare nella barra laterale sinistra, quindi seleziona l'intervallo di tempo per vedere i dati di quel periodo e puoi anche cliccare per scaricarli.

.. image:: img/dashboard_history.png
  :width: 90%
  

Log
------------

La pagina Log è utilizzata per visualizzare i log del servizio Pironman5 attualmente in esecuzione. Il servizio Pironman5 include più sottoservizi, ciascuno con il proprio log. Seleziona il log che desideri visualizzare e potrai vedere i dati del log a destra. Se è vuoto, potrebbe significare che non ci sono contenuti di log.

* Ogni log ha una dimensione fissa di 10MB. Quando si supera questa dimensione, verrà creato un secondo log.
* Il numero di log per lo stesso servizio è limitato a 10. Se il numero supera questo limite, il log più vecchio verrà automaticamente eliminato.
* Ci sono strumenti di filtro sopra l'area del log a destra. Puoi selezionare il livello del log, filtrare per parole chiave e utilizzare diversi strumenti pratici, tra cui **Line Wrap**, **Auto Scroll** e **Auto Update**.
* I log possono anche essere scaricati localmente.

.. image:: img/dashboard_log.png
  :width: 90%
  

Impostazioni
-----------------

C'è un menu di impostazioni nell'angolo in alto a destra della pagina. 

.. note::
    
    Dopo aver modificato le impostazioni, è necessario cliccare sul pulsante **SALVA** in basso per salvare le impostazioni.

.. image:: img/dashboard_settings.png
  :width: 90%
  

* **Modalità Scura**: Passa tra i temi modalità chiara e scura. L'opzione tema è salvata nella cache del browser. Cambiare browser o cancellare la cache riporterà il tema predefinito alla modalità chiara.
* **Unità di Temperatura**: Imposta l'unità di temperatura visualizzata dal sistema.
* **Modalità Ventola**: Puoi impostare la modalità operativa delle due ventole RGB. Queste modalità determinano le condizioni in cui le ventole RGB si attiveranno.

    * **Silenziosa**: Le ventole RGB si attiveranno a 70°C.
    * **Bilanciata**: Le ventole RGB si attiveranno a 67,5°C.
    * **Fresca**: Le ventole RGB si attiveranno a 60°C.
    * **Performance**: Le ventole RGB si attiveranno a 50°C.
    * **Sempre Accese**: Le ventole RGB saranno sempre accese.

    Ad esempio, se impostata su modalità **Performance**, le ventole RGB si attiveranno a 50°C.

    Dopo aver salvato, se la temperatura della CPU supera i 50°C, vedrai lo **Stato Ventola GPIO** passare a ON nella Dashboard e le ventole RGB laterali inizieranno a girare.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300
    

* **Luminosità RGB**: Puoi regolare la luminosità dei LED RGB con un cursore.
* **Colore RGB**: Imposta il colore dei LED RGB.
* **Stile RGB**: Scegli la modalità di visualizzazione dei LED RGB. Le opzioni includono **Solido**, **Respiro**, **Flusso**, **Flusso_inverso**, **Arcobaleno**, **Arcobaleno Inverso** e **Ciclo di Tonalità**.

.. note::

  Se imposti lo **Stile RGB** su **Arcobaleno**, **Arcobaleno Inverso** o **Ciclo di Tonalità**, non sarà possibile impostare il colore.


* **Velocità RGB**: Imposta la velocità dei cambiamenti dei LED RGB.
