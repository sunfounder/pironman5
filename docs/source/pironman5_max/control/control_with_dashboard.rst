.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_dashboard:

Visualizzazione e Controllo dalla Dashboard
=============================================

Una volta installato correttamente il modulo ``pironman5``, il servizio ``pironman5.service`` si avvierà automaticamente al riavvio.

Ora puoi aprire la pagina di monitoraggio nel browser per vedere le informazioni sul tuo Raspberry Pi, configurare gli RGB e controllare la ventola. Il link della pagina è: ``http://<ip>:34001``.

Questa pagina include le sezioni **Dashboard**, **Cronologia**, **Log** e **Impostazioni**.

.. image:: img/dashboard_home.png


Dashboard
-----------------------

Sono disponibili diverse schede per visualizzare lo stato del Raspberry Pi, tra cui:

* **Temperatura**: Visualizza la temperatura CPU/GPU del Raspberry Pi e la velocità della ventola CPU. Lo **Stato ventole GPIO** mostra lo stato delle due ventole GPIO laterali.

  .. image:: img/dashboard_tem.png
    :width: 90%

* **Archiviazione**: Mostra la capacità di archiviazione del Raspberry Pi, visualizzando le partizioni del disco con lo spazio utilizzato e disponibile.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Memoria**: Mostra l'utilizzo della RAM del Raspberry Pi e la sua percentuale.

  .. image:: img/dashboard_memory.png
    :width: 90%

* **Rete**: Visualizza il tipo di connessione di rete attuale, velocità di upload e download.

  .. image:: img/dashboard_network.png
    :width: 90%

* **Processore**: Illustra le prestazioni della CPU del Raspberry Pi, incluso lo stato dei quattro core, le frequenze operative e la percentuale di utilizzo della CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%


Cronologia
--------------

La pagina Cronologia ti permette di visualizzare i dati storici. Seleziona i dati che vuoi vedere nella barra laterale sinistra, poi scegli l'intervallo di tempo per visualizzare i dati di quel periodo. Puoi anche scaricarli.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Log
------------

La pagina Log mostra il log di esecuzione del servizio Pironman5.

* Le voci di log possono essere filtrate per livello (Debug, Info, Warning, Error o Critical).
* Il file di log può anche essere scaricato localmente.

.. image:: img/dashboard_log.png
  :width: 90%

Impostazioni
------------

La pagina Impostazioni ti permette di personalizzare l'aspetto della Dashboard, le preferenze di sistema, lo schermo OLED, l'illuminazione RGB e il comportamento delle ventole. Mostra anche informazioni di rete di base come l'indirizzo MAC e l'indirizzo IP.

.. image:: img/dashboard_setting.png
    :width: 600


* **Interfaccia**

  Configura l'aspetto della Dashboard e il comportamento di visualizzazione.

  .. image:: img/dashboard_setting_interface.png
      :width: 600

  * **Modalità scura**: Attiva o disattiva il tema scuro.
  * **Mostra dischi non montati**: Visualizza i dispositivi di archiviazione non montati nella scheda Archiviazione.
  * **Mostra tutti i core**: Visualizza tutti i core della CPU nella scheda Processore.
  * **Layout schede**: Personalizza il layout delle schede della Dashboard.
  * **Unità di temperatura**: Passa tra Celsius e Fahrenheit.
  * **Versione interfaccia web**: Mostra la versione attuale della Dashboard.


* **OLED**

  Configura la visualizzazione e il comportamento dello schermo OLED.

  .. image:: img/dashboard_setting_oled.png
      :width: 600

  * **Abilita OLED**: Attiva o disattiva lo schermo OLED.
  * **Rotazione OLED**: Ruota il display OLED tra ``0°`` e ``180°``.
  * **Timeout sospensione OLED**: Imposta per quanto tempo lo schermo OLED rimane acceso prima di spegnersi automaticamente.
  * **Pagine OLED**: Configura quali pagine vengono visualizzate sullo schermo OLED e regola il loro ordine.

    Pagine disponibili:

    * **Indirizzi IP**: Mostra gli indirizzi IP di tutte le interfacce di rete fisiche.
    * **Utilizzo disco**: Mostra le informazioni di utilizzo del disco per tutti i dischi.
    * **Metriche di prestazione**: Mostra l'utilizzo della CPU, la temperatura della CPU, l'utilizzo della RAM e la velocità della ventola.
    * **Mix di sistema**: Mostra l'utilizzo della CPU, la temperatura della CPU e l'indirizzo IP.


* **RGB**

  Configura gli effetti di illuminazione e il comportamento dei LED RGB.

  .. image:: img/dashboard_setting_rgb.png
      :width: 600

  * **Abilita RGB**: Attiva o disattiva i LED RGB.
  * **Colore RGB**: Imposta il colore dei LED RGB.
  * **Luminosità RGB**: Regola la luminosità dei LED RGB.
  * **Stile RGB**: Seleziona l'effetto di illuminazione RGB, tra ``Nessuno``, ``Fisso``, ``Respirazione``, ``Flusso``, ``Flusso inverso``, ``Arcobaleno``, ``Arcobaleno inverso`` e ``Ciclo tonalità``.
  * **Velocità RGB**: Regola la velocità di animazione dell'effetto RGB selezionato.
  * **LED RGB**: Imposta il numero di LED RGB attivi.


* **Ventole GPIO**

  Configura la modalità operativa delle due ventole GPIO.

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  La modalità selezionata determina quando le ventole GPIO si attiveranno.

  * **Silenzioso**: Le ventole GPIO si attiveranno a 70°C.
  * **Bilanciato**: Le ventole GPIO si attiveranno a 67,5°C.
  * **Fresco**: Le ventole GPIO si attiveranno a 60°C.
  * **Prestazioni**: Le ventole GPIO si attiveranno a 50°C.
  * **Sempre attive**: Le ventole GPIO rimarranno sempre attive.


* **Sistema**

  Configura il comportamento del sistema e visualizza le informazioni del dispositivo.

  .. image:: img/dashboard_setting_system.png
      :width: 600

  * **Livello di debug**: Imposta il livello di registrazione del servizio Pironman 5.
  * **Indirizzo MAC**: Mostra gli indirizzi MAC delle interfacce di rete del Raspberry Pi.
  * **Indirizzo IP**: Mostra gli indirizzi IP delle interfacce di rete del Raspberry Pi.
  * **Conservazione cronologia**: Imposta per quanti giorni i dati storici saranno conservati.
  * **Cancella tutti i dati**: Cancella tutti i dati storici registrati.
  * **Riavvia**: Riavvia il Raspberry Pi da remoto dalla Dashboard.
  * **Spegni**: Spegni in sicurezza il Raspberry Pi da remoto dalla Dashboard.
