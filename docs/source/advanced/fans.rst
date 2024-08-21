.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Ventole
============

Ventola PWM
--------------

La ventola PWM nel Pironman 5 è controllata dal sistema Raspberry Pi.

Per quanto riguarda le soluzioni di raffreddamento per il Raspberry Pi 5, specialmente sotto carichi pesanti, il design del Pironman 5 incorpora un sistema di raffreddamento intelligente. Esso include una ventola PWM principale e due ventole RGB supplementari. La strategia di raffreddamento è strettamente integrata con il sistema di gestione termica del Raspberry Pi 5.

Il funzionamento della ventola PWM è basato sulla temperatura del Raspberry Pi 5:

* Sotto i 50°C, la ventola PWM rimane spenta (velocità 0%).
* A 50°C, la ventola si avvia a bassa velocità (velocità 30%).
* Al raggiungimento di 60°C, la ventola aumenta a velocità media (velocità 50%).
* A 67,5°C, la ventola accelera ad alta velocità (velocità 70%).
* A 75°C e oltre, la ventola funziona alla massima velocità (velocità 100%).

Questo rapporto temperatura-velocità si applica anche quando la temperatura diminuisce, con una isteresi di 5°C. La velocità della ventola si riduce quando la temperatura scende di 5°C al di sotto di ciascuna di queste soglie.

* Comandi per monitorare la ventola PWM. Per controllare lo stato della ventola PWM:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Per visualizzare la velocità della ventola PWM:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Nel Pironman 5, la ventola PWM è un componente critico per mantenere temperature operative ottimali, specialmente durante compiti intensivi, garantendo che il Raspberry Pi 5 funzioni in modo efficiente e affidabile.

Ventole RGB
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
