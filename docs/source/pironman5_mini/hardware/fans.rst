.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _fan_mini:

Ventole
============

Sistema di Raffreddamento Attivo
-------------------------------------------

Il sistema di raffreddamento attivo del Pironman 5 Mini è gestito direttamente dal sistema operativo del Raspberry Pi.

.. image:: img/active_cooler.png

Per quanto riguarda le soluzioni di raffreddamento per Raspberry Pi 5, 
specialmente durante carichi di lavoro intensi, il design del Pironman 5 Mini integra un sistema di raffreddamento intelligente. 
Include una ventola principale Active Cooler e una ventola RGB supplementare. 
La strategia di raffreddamento è strettamente collegata al sistema di gestione termica del Raspberry Pi 5.

Il funzionamento dell’Active Cooler è basato sulla temperatura rilevata dal Raspberry Pi 5:

* Sotto i 50°C, l’Active Cooler rimane spento (velocità 0%).
* A 50°C, la ventola si avvia a bassa velocità (30%).
* Al raggiungimento dei 60°C, aumenta a velocità media (50%).
* A 67.5°C, accelera ulteriormente a velocità alta (70%).
* A 75°C o più, la ventola lavora alla massima velocità (100%).

Questo rapporto tra temperatura e velocità viene mantenuto anche durante il raffreddamento, grazie a un'isteresi di 5°C. La velocità della ventola si riduce quando la temperatura scende di 5°C rispetto a ciascuna soglia.

* Comandi per monitorare l’Active Cooler. Per controllare lo stato dell’Active Cooler:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Per visualizzare la velocità della ventola Active Cooler:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Nel Pironman 5 Mini, l’Active Cooler è un componente essenziale per mantenere temperature operative ottimali, soprattutto durante attività intensive, garantendo prestazioni stabili ed efficienti al Raspberry Pi 5.

Ventola RGB
-------------------

.. image:: img/size_fan.png

* **Dimensioni esterne**: 40×40×10 mm  
* **Peso**: 13,5±5 g/cad  
* **Durata**: 40.000 ore (a temperatura ambiente 25°C)  
* **Portata d'aria massima**: 2,46 CFM  
* **Pressione dell’aria massima**: 0,62 mm-H2O  
* **Rumorosità acustica**: 22,31 dBA  
* **Potenza nominale in ingresso**: 5V/0,1A  
* **Velocità nominale**: 3500±10% RPM  
* **Temperatura operativa**: da -10°C a +70°C  
* **Temperatura di stoccaggio**: da -30°C a +85°C  
