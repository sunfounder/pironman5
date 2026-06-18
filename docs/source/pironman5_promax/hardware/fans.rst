
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Ventole
============

Ventola CPU
------------------------------

Ci sono 3 Ventole CPU sul Pironman 5 Pro MAX.

La ventola CPU sul Pironman 5 Pro MAX è controllata dal sistema Raspberry Pi.

Per quanto riguarda le soluzioni di raffreddamento per il Raspberry Pi 5, specialmente sotto carico elevato, il design del Pironman 5 Pro MAX incorpora un sistema di raffreddamento intelligente. Dispone di una ventola CPU principale e due ventole GPIO supplementari. La strategia di raffreddamento è strettamente integrata con il sistema di gestione termica del Raspberry Pi 5.

Il funzionamento della ventola CPU si basa sulla temperatura del Raspberry Pi 5:

* Sotto i 50°C, la ventola CPU rimane spenta (velocità 0%).
* A 50°C, la ventola si avvia a bassa velocità (velocità 30%).
* Raggiungendo i 60°C, la ventola aumenta a velocità media (velocità 50%).
* A 67,5°C, la ventola accelera ad alta velocità (velocità 70%).
* A 75°C e oltre, la ventola opera a piena velocità (velocità 100%).

Questa relazione temperatura-velocità si applica anche quando la temperatura diminuisce, con un'isteresi di 5°C. La velocità della ventola si riduce quando la temperatura scende di 5°C al di sotto di ciascuna di queste soglie.

* Comandi per monitorare la ventola CPU. Per controllare lo stato della ventola CPU:

  .. code-block:: shell

    cat /sys/class/thermal/cooling_device0/cur_state

* Per visualizzare la velocità della ventola CPU:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Nel Pironman 5 Pro MAX, la ventola CPU è un componente critico per mantenere temperature operative ottimali, specialmente durante attività intensive, garantendo che il Raspberry Pi 5 funzioni in modo efficiente e affidabile.

**Specifiche della Ventola**

.. image:: img/size_fan.png

* **Dimensioni esterne**: 40*40*10MM
* **Potenza nominale in ingresso**: 5V/0.106A
* **Velocità nominale**: 4000 RPM
* **Peso**: 13,5±5g/pcs
* **Durata**: 30.000 ore (temperatura ambiente 25°C)
* **Rumore acustico**: 22,31 dBA
* **Flusso d'aria massimo**: 2,46 CFM
* **Pressione aria massima**: 0,62 mm-H₂O
* **Temperatura di funzionamento**: -10°C ~ +60°C
* **Temperatura di conservazione**: -20°C ~ +70°C

**Definizioni dei Pin**

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Pin
     - Colore
     - Descrizione
   * - 1
     - Blu
     - Segnale PWM per il controllo della velocità della ventola
   * - 2
     - Rosso
     - Alimentazione 5V
   * - 3
     - Nero
     - Terra
   * - 4
     - Giallo
     - Dati in ingresso del LED RGB interno
   * - 5 
     - Verde
     - Dati in uscita del LED RGB interno

Dissipatore a Torre
----------------------------

Nel Pro MAX, il dissipatore a torre è una soluzione di raffreddamento ad alte prestazioni progettata per mantenere il tuo Raspberry Pi 5 a temperature ottimali durante attività impegnative. Presenta un grande dissipatore in alluminio e una ventola che può essere controllata tramite PWM per regolare le prestazioni di raffreddamento secondo necessità. Il dissipatore a torre è compatibile con il Raspberry Pi 5 e può essere facilmente installato utilizzando le viti e la staffa di montaggio incluse.

.. image:: img/size_tower_cooler.png

**Avvertenza**

Non toccare le pale, né lasciare che i cavi di alimentazione si avvolgano attorno alla ventola, né tirare i cavi di alimentazione con forza per evitare di danneggiare la ventola.

Non utilizzare in ambienti con gas infiammabili o qualsiasi pericolo.

Quando la ventola è in funzione, non cercare di bloccarla per lunghi periodi. In caso contrario, la ventola si brucerà a causa dell'elevato calore generato dall'arresto continuo.

Durante l'assemblaggio della ventola, prestare particolare attenzione al rumore generato da risonanza o vibrazioni.

Non far cadere il Icecube Tower Cooler da altezze elevate, poiché ciò potrebbe influenzare l'equilibrio delle pale della ventola.
