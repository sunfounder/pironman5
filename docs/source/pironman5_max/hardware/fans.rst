.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _fan_max:

Ventole
============

Ventola CPU
---------------

La ventola CPU del Pironman 5 MAX è controllata direttamente dal sistema del Raspberry Pi.

In merito alle soluzioni di raffreddamento per il Raspberry Pi 5, soprattutto sotto carichi elevati, il design del Pironman 5 MAX integra un sistema di raffreddamento intelligente. Include una ventola CPU principale e due ventole GPIO supplementari. La strategia di raffreddamento è strettamente integrata con il sistema di gestione termica del Raspberry Pi 5.

Il funzionamento della ventola CPU si basa sulla temperatura del Raspberry Pi 5:

* Sotto i 50°C, la ventola CPU rimane spenta (velocità 0%).
* A 50°C, la ventola parte a bassa velocità (30%).
* A 60°C, la ventola passa a velocità media (50%).
* A 67,5°C, la ventola aumenta a velocità alta (70%).
* A 75°C e oltre, la ventola funziona alla massima velocità (100%).

Questa relazione temperatura-velocità si applica anche quando la temperatura scende, con una isteresi di 5°C. La velocità della ventola si riduce quando la temperatura scende di 5°C al di sotto di ciascuna soglia.

* Comandi per monitorare la ventola CPU. Per verificare lo stato della ventola CPU:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Per visualizzare la velocità della ventola CPU:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Nel Pironman 5 MAX, la ventola CPU è un componente essenziale per mantenere temperature operative ottimali, soprattutto durante attività intensive, garantendo che il Raspberry Pi 5 operi in modo efficiente e affidabile.

Ventole GPIO
-------------------

.. image:: img/size_fan.png

* **Dimensioni esterne**: 40*40*10MM
* **Peso**: 13,5±5g/cad
* **Durata**: 30.000 ore (temperatura ambiente 25°C)
* **Portata massima d'aria**: 2.46CFM
* **Pressione massima dell'aria**: 0.62mm-H2O
* **Rumorosità acustica**: 22.31dBA
* **Potenza nominale in ingresso**: 5V/0.15A
* **Velocità nominale**: 3500±10%RPM
* **Temperatura operativa**: -10℃~+60℃
* **Temperatura di stoccaggio**: -20℃~+70℃

