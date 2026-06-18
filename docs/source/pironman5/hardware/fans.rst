.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _fans:

Ventole
============

Ventola CPU
-----------------

La ventola CPU nel Pironman 5 è gestita dal sistema Raspberry Pi e rappresenta il fulcro della soluzione di raffreddamento intelligente, soprattutto sotto carichi pesanti. Questo sistema combina una ventola CPU principale con due ventole GPIO supplementari per migliorare le prestazioni di raffreddamento, strettamente integrate con il sistema di gestione termica del Raspberry Pi 5.

.. image:: img/fan_tower_cooler.png  
  :width: 600  
  :align: center  

**Caratteristiche Elettriche**

* **Tensione Nominale**: 5 VDC  
* **Tensione di Avviamento**: 4.0 V (a 25°C accensione/spegnimento)  
* **Gamma di Tensione Operativa**: 4.0 ~ 5.5 VDC  
* **Corrente Nominale**: 0.05 A / MAX. 0.08 A  
* **Potenza Nominale**: 0.25 W / MAX. 0.40 W  
* **Velocità Nominale**: 3500±10% RPM (a 25°C, test effettuato dopo 3 minuti di funzionamento)  
* **Flusso d'Aria Massimo**: 2.46 (MIN. 2.21) CFM (a pressione statica zero)  
* **Pressione Statica Massima**: 0.62 (MIN. 0.496) mmH2O (a flusso d'aria zero)  
* **Rumore Acustico**: 22.31 dB(A) MAX. 25.31 dB(A)  
* **Durata Prevista**: 40.000 ore (a 25°C, 65% di umidità, condizioni normali di ambiente)  

**Caratteristiche Meccaniche**

* **Dimensioni**: 40x10.4x40 mm (LxPxH)  
* **Materiale del Telaio**: Plastica PBT  
* **Materiale della Girante**: Plastica PBT  
* **Tipo di Cuscinetto**: Cuscinetto Idraulico  

**Parametri Ambientali**

* **Temperatura Operativa**: -10°C ~ 70°C  
* **Temperatura di Conservazione**: -40°C ~ 75°C  
* **Umidità Operativa**: 5% ~ 90% RH  
* **Umidità di Conservazione**: 5% ~ 95% RH  

**Controllo della Velocità della ventola in Base alla Temperatura**  

La ventola CPU opera dinamicamente, regolando la velocità in base alla temperatura del Raspberry Pi 5:  

* **Sotto i 50°C**: La ventola rimane spenta (velocità 0%).  
* **A 50°C**: La ventola opera a bassa velocità (velocità 30%).  
* **A 60°C**: La ventola aumenta a velocità media (velocità 50%).  
* **A 67.5°C**: La ventola accelera a velocità alta (velocità 70%).  
* **A 75°C e oltre**: La ventola opera alla massima velocità (velocità 100%).  

Questo controllo temperatura-velocità include una isteresi di 5°C per evitare cambiamenti di velocità frequenti. Ad esempio, la ventola ridurrà la sua velocità solo dopo che la temperatura scende di 5°C sotto ogni soglia.

I seguenti comandi consentono agli utenti di monitorare il funzionamento della ventola CPU:

Per controllare lo stato corrente della ventola:

.. code-block:: shell

  cat /sys/class/thermal/cooling_device0/cur_state

Ventole GPIO
-------------------

.. image:: img/size_fan.png

* **Dimensioni esterne**: 40*40*10MM
* **Peso**: 13.5±5g/pcs
* **Durata**: 40.000 ore (temperatura ambiente 25°C)
* **Flusso d'aria massimo**: 2.46CFM
* **Massima pressione dell'aria**: 0.62mm-H2O
* **Rumorosità**: 22.31dBA
* **Potenza nominale in ingresso**: 5V/0.1A
* **Velocità nominale**: 3500±10%RPM
* **Temperatura operativa**: -10℃~+70℃
* **Temperatura di stoccaggio**: -30℃~+85℃
