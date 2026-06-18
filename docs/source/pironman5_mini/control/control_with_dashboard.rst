.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_dashboard_mini:

Visualizzazione e Controllo dal Dashboard
===============================================

Una volta installato correttamente il modulo ``pironman5``, il servizio ``pironman5.service`` si avvierà automaticamente al riavvio.

Ora puoi aprire la pagina di monitoraggio nel tuo browser per visualizzare le informazioni sul tuo Raspberry Pi, configurare l’illuminazione RGB, controllare la ventola e altro ancora. Il link della pagina è: ``http://<ip>:34001``.

Questa pagina include le sezioni **Dashboard**, **Cronologia**, **Log** e **Impostazioni**.

.. image:: img/dashboard_tab.png
  :width: 90%
  

Dashboard
-----------------------

Sono presenti diverse schede che mostrano lo stato attuale del Raspberry Pi, tra cui:

* **Ventola**: Visualizza la temperatura della CPU del Raspberry Pi e la velocità della ventola CPU. **Stato ventola GPIO** indica lo stato della ventola GPIO. Alla temperatura attuale, la ventola GPIO è spenta.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Archiviazione**: Mostra la capacità di archiviazione del Raspberry Pi, evidenziando le diverse partizioni del disco con lo spazio utilizzato e disponibile.

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Memoria**: Mostra l’utilizzo e la percentuale di RAM del Raspberry Pi.

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Rete**: Visualizza il tipo di connessione di rete attiva, le velocità di upload e download.

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Processore**: Illustra le prestazioni della CPU del Raspberry Pi, inclusi lo stato dei quattro core, le frequenze operative e la percentuale di utilizzo della CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

Cronologia
--------------

La pagina Cronologia ti consente di visualizzare i dati storici. Seleziona i dati che vuoi analizzare dalla barra laterale sinistra, poi scegli l’intervallo di tempo per visualizzarli, con la possibilità di scaricarli cliccando sull’apposito pulsante.

.. image:: img/dashboard_history.png
  :width: 90%
  

Log
------------

La pagina Log è dedicata alla visualizzazione dei registri del servizio pironman5 attualmente in esecuzione. Il servizio pironman5 comprende diversi sottoservizi, ciascuno con il proprio registro. Seleziona quello che desideri consultare per visualizzarne il contenuto a destra. Se l’area è vuota, potrebbe significare che non ci sono log disponibili.

* Ogni log ha una dimensione massima di 10MB. Una volta superata, verrà creato un nuovo file di log.
* Il numero di log per ogni servizio è limitato a 10. Se viene superato, il log più vecchio verrà eliminato automaticamente.
* Sopra l’area di visualizzazione sono presenti strumenti di filtro: puoi selezionare il livello di log, filtrare per parola chiave e utilizzare strumenti utili come **Line Wrap**, **Auto Scroll** e **Auto Update**.
* I log possono anche essere scaricati localmente.

.. image:: img/dashboard_log.png
  :width: 90%
  

Impostazioni
-----------------

In alto a destra nella pagina è presente un menu delle impostazioni.

.. note::

    Dopo aver effettuato modifiche, è necessario cliccare sul pulsante **SAVE** in fondo alla pagina per salvarle.

.. image:: img/dashboard_settings.png
  :width: 90%
  

* **Dark Mode**: Passa tra il tema chiaro e quello scuro. L’impostazione viene salvata nella cache del browser. Cambiando browser o cancellando la cache si torna al tema chiaro predefinito.
* **Temperature Unit**: Imposta l’unità di misura della temperatura visualizzata dal sistema.
* **Fan Mode**: Imposta la modalità operativa della ventola GPIO. Ogni modalità determina la temperatura a cui la ventola si attiverà.

    * **Quiet**: La ventola GPIO si attiva a 70°C.
    * **Balanced**: La ventola GPIO si attiva a 67,5°C.
    * **Cool**: La ventola GPIO si attiva a 60°C.
    * **Performance**: La ventola GPIO si attiva a 50°C.
    * **Always On**: La ventola GPIO rimane sempre accesa.

    Ad esempio, impostando la modalità **Performance**, la ventola GPIO si attiverà a 50°C.

    Dopo il salvataggio, se la temperatura della CPU supera i 50°C, vedrai lo stato della **Ventola GPIO** passare a ON nel Dashboard e la ventola GPIO inizierà a girare.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300
  

* **Luminosità RGB**: Regola la luminosità dei LED RGB tramite uno slider.
* **Colore RGB**: Imposta il colore dei LED RGB.
* **Stile RGB**: Seleziona la modalità di visualizzazione dei LED RGB. Le opzioni includono **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse**, e **Hue Cycle**.

.. note::

  Se imposti lo **Stile RGB** su **Rainbow**, **Rainbow Reverse** o **Hue Cycle**, non sarà possibile selezionare il colore.


* **Velocità RGB**: Regola la velocità di transizione degli effetti LED RGB.


**Informazioni sulla ventola principale**

La ventola principale si collega a una porta PWM a 4 pin dedicata sul Raspberry Pi 5. La sua strategia di controllo predefinita è uno schema di regolazione intelligente della velocità multilivello gestito dal firmware, basato sulla temperatura della CPU. Ciò significa che quando si utilizza una ventola CPU ufficiale o compatibile e la si collega correttamente, il sistema regolerà automaticamente la velocità della ventola in base alle variazioni di temperatura della CPU (iniziando a funzionare oltre i 50 °C) senza alcun intervento manuale da parte dell'utente.