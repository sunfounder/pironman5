.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Scopri di più su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e omaggi festivi**: Partecipa a concorsi e promozioni speciali.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _view_control_dashboard:

Visualizza e controlla dal Dashboard
=========================================

Dopo aver installato correttamente il modulo ``pironman5``, il servizio ``pironman5.service`` verrà avviato automaticamente al riavvio.

Ora puoi aprire la pagina di monitoraggio nel tuo browser per visualizzare le informazioni sul tuo Raspberry Pi, configurare l'RGB, controllare la ventola, ecc. Il link alla pagina è: ``http://<ip>:34001``.

Questa pagina include le sezioni **Dashboard**, **Cronologia**, **Log** e **Impostazioni**.

.. image:: img/dashboard_tab_new.jpg

  
Dashboard
-----------------------

La Dashboard contiene varie schede per visualizzare lo stato rilevante del Raspberry Pi, tra cui:

* **Ventola**: Visualizza la temperatura della CPU del Raspberry Pi e la velocità PWM della ventola. **Stato GPIO Fan** indica lo stato delle due ventole RGB laterali. Alla temperatura attuale, le due ventole RGB sono spente.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Archiviazione**: Mostra la capacità di archiviazione del Raspberry Pi, visualizzando le varie partizioni del disco con lo spazio utilizzato e disponibile.

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Memoria**: Mostra l'uso della RAM del Raspberry Pi e la percentuale di utilizzo.

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Rete**: Visualizza il tipo di connessione di rete corrente, la velocità di upload e download.

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Processore**: Illustra le prestazioni della CPU del Raspberry Pi, inclusi lo stato dei quattro core, le frequenze operative e la percentuale di utilizzo della CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

Cronologia
--------------

La pagina Cronologia consente di visualizzare i dati storici. Seleziona i dati che desideri visualizzare nella barra laterale sinistra, quindi scegli l'intervallo di tempo per vedere i dati di quel periodo. Puoi anche scaricarli cliccando sull'apposita opzione.

.. image:: img/dashboard_history1.png
  :width: 90%
  
.. image:: img/dashboard_history2.png
  :width: 90%

Log
------------

La pagina Log è utilizzata per visualizzare i log del servizio Pironman5 attualmente in esecuzione. Il servizio Pironman5 include diversi sottoservizi, ognuno con il proprio log. Seleziona il log che desideri visualizzare per vedere i dati a destra. Se non ci sono dati, potrebbe significare che non c'è contenuto di log.

* Ogni log ha una dimensione fissa di 10MB. Quando questa dimensione viene superata, verrà creato un secondo log.
* Il numero massimo di log per lo stesso servizio è limitato a 10. Se si supera questo limite, il log più vecchio verrà eliminato automaticamente.
* Sopra l'area dei log a destra sono presenti strumenti di filtro. Puoi selezionare il livello del log, filtrare per parole chiave e utilizzare strumenti pratici come **Line Wrap**, **Auto Scroll** e **Auto Update**.
* I log possono anche essere scaricati localmente.

.. image:: img/dashboard_log1.png
  :width: 90%
  
.. image:: img/dashboard_log2.png
  :width: 90%

Impostazioni
-----------------

Nel menu Impostazioni in alto a destra della pagina, puoi personalizzare le impostazioni secondo le tue preferenze. Dopo aver apportato modifiche, le modifiche verranno salvate automaticamente. Se necessario, puoi cliccare sul pulsante CLEAR in basso per cancellare i dati storici.

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **Modalità Scura**: Passa tra i temi chiaro e scuro. L'opzione del tema viene salvata nella cache del browser. Cambiando browser o cancellando la cache, verrà ripristinato il tema chiaro predefinito.
* **Unità di Temperatura**: Imposta l'unità di temperatura visualizzata dal sistema.

**Informazioni sullo Schermo OLED**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **Abilita OLED**: Abilita o disabilita l'OLED.
* **Disco OLED**: Imposta il disco per l'OLED.
* **Interfaccia di Rete OLED**: 

  * **all**: Alterna la visualizzazione tra l'IP Ethernet e l'IP Wi-Fi in sequenza.
  * **eth0**: Mostra solo l'IP Ethernet.
  * **wlan0**: Mostra solo l'IP Wi-Fi.

* **Rotazione OLED**: Imposta la rotazione dell'OLED.

**Informazioni sui LED RGB**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **Abilita RGB**: Abilita o disabilita i LED RGB.
* **Colore RGB**: Imposta il colore dei LED RGB.
* **Luminosità RGB**: Puoi regolare la luminosità dei LED RGB con uno slider.
* **Stile RGB**: Scegli la modalità di visualizzazione dei LED RGB. Le opzioni includono **Solido**, **Respiro**, **Flusso**, **Flusso Inverso**, **Arcobaleno**, **Arcobaleno Inverso** e **Ciclo Hue**.

  .. note::

     Se imposti lo **Stile RGB** su **Arcobaleno**, **Arcobaleno Inverso** o **Ciclo Hue**, non sarà possibile impostare il colore.

* **Velocità RGB**: Imposta la velocità delle modifiche dei LED RGB.

**Informazioni sulle Ventole RGB**

.. image:: img/RGB_fans.png
  :width: 600

* **LED Ventola**: Puoi impostare il LED della ventola su ON, OFF o FOLLOW.
* **Modalità Ventola**: Imposta la modalità operativa delle due ventole RGB. Queste modalità determinano le condizioni di attivazione delle ventole RGB.

    * **Silenziosa**: Le ventole RGB si attivano a 70°C.
    * **Bilanciata**: Le ventole RGB si attivano a 67,5°C.
    * **Fresca**: Le ventole RGB si attivano a 60°C.
    * **Prestazioni**: Le ventole RGB si attivano a 50°C.
    * **Sempre Accese**: Le ventole RGB sono sempre accese.

Ad esempio, se impostato su **Prestazioni**, le ventole RGB si attiveranno a 50°C.

Dopo aver salvato, se la temperatura della CPU supera i 50°C, vedrai lo **Stato GPIO Fan** cambiare su ON nella Dashboard, e le ventole RGB laterali inizieranno a girare.

.. image:: img/dashboard_rgbfan_on.png
  :width: 300
