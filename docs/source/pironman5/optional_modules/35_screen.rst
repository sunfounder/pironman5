.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Schermo Touch da 3,5 pollici
=============================

.. note::

    La serie Pironman 5 non include uno schermo touch da 3,5 pollici.  
    Dovrai procurartene uno oppure acquistarlo dal nostro sito ufficiale:

   * `Schermo Touch da 3,5 pollici <https://www.sunfounder.com/products/touchscreen-02>`_

Lo schermo touch da 3,5 pollici si collega direttamente al connettore GPIO del Raspberry Pi,  
fornendo sia la visualizzazione che il controllo touch per il Pironman 5.  
Segui attentamente i passaggi per garantire una corretta installazione ed evitare danni hardware.

Maggiori dettagli sono disponibili qui:  
`Documentazione Schermo Touch da 3,5 pollici <https://docs.sunfounder.com/projects/35-ips-screen/en/latest/get_started/get_started.html>`_.


**Assemblaggio**

.. image:: img/lcd_to_pironman5.png
    :width: 340

.. image:: img/lcd_to_pironman5.jpg
    :width: 340


.. warning:: 
   
   Quando installi lo schermo touch da 3,5 pollici sul Pironman 5, assicurati che i pin siano perfettamente allineati.  
   L’header deve combaciare con l’interfaccia GPIO del Raspberry Pi senza alcuno spostamento.  
   Un disallineamento potrebbe danneggiare lo schermo o persino il Raspberry Pi.  
   Ricontrolla i collegamenti prima di accendere l’alimentazione!

**Rimozione del Jumper RGB**

Quando utilizzi il Pironman 5 con lo schermo touch da 3,5 pollici,  
nota che i LED RGB sull’IO Expander condividono lo stesso pin SPI MOSI (GPIO10) con lo schermo.  
Per evitare conflitti e garantire il corretto funzionamento:

1. Sull’IO Expander, rimuovi il cappuccio jumper dai **pin dei LED RGB** (sopra J9).

   .. image:: img/lcd_to_max0.jpg
      :width: 600
      :align: center

2. Disattiva il servizio di controllo dei LED RGB:

   .. code-block:: bash

      sudo pironman5 -re false
      sudo systemctl restart pironman5.service

Questo libera l’interfaccia SPI per lo schermo touch da 3,5 pollici ed evita problemi di visualizzazione.


**Installazione Driver**

Per istruzioni dettagliate, fare riferimento a |link_3.5_screen|, che descrive l'installazione del driver per i diversi sistemi.