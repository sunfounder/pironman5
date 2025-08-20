.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto della nostra community e del nostro team.
    - **Learn & Share**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Accedi in anteprima ai nuovi annunci e alle anticipazioni sui prodotti.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway riservati.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _max_set_up_pi_os:

Configurazione su Raspberry Pi/Ubuntu/Kali/Homebridge OS
=============================================================

Se hai installato Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge sul tuo Raspberry Pi, dovrai configurare il Pironman 5 MAX utilizzando la riga di comando. Di seguito trovi i tutorial dettagliati:

.. note::

  Prima di configurare, è necessario avviare e accedere al tuo Raspberry Pi. Se non sai come farlo, puoi visitare il sito ufficiale Raspberry Pi: |link_rpi_get_start|.


Configurazione dello spegnimento per disattivare l’alimentazione GPIO
----------------------------------------------------------------------------

Per evitare che lo schermo OLED e le ventole RGB alimentate dal GPIO del Raspberry Pi rimangano attivi dopo lo spegnimento, è importante configurare la disattivazione dell’alimentazione GPIO.

#. Modifica manualmente il file di configurazione ``EEPROM`` con il comando:

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. Modifica il parametro ``POWER_OFF_ON_HALT`` impostandolo su ``1``. Ad esempio:

   .. code-block:: shell

     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Premi ``Ctrl + X``, poi ``Y`` e infine ``Enter`` per salvare le modifiche.


Download e installazione del modulo ``pironman5``
-----------------------------------------------------------

#. Nei sistemi lite, installa inizialmente strumenti come ``git``, ``python3``, ``pip3``, ``setuptools``, ecc.

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procedi con il download del codice da GitHub e installa il modulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Dopo un’installazione completata con successo, sarà necessario riavviare il sistema per attivare il modulo. Segui il messaggio a schermo per eseguire il riavvio.

   Al riavvio, il servizio ``pironman5.service`` si avvierà automaticamente. Ecco le principali funzionalità di Pironman 5 MAX:

   * Il display OLED mostra utilizzo di CPU, RAM, disco, temperatura della CPU e indirizzo IP del Raspberry Pi.

   .. note:: Lo schermo OLED può spegnersi automaticamente dopo un periodo di inattività per risparmiare energia. Puoi toccare delicatamente il case per attivare il sensore di vibrazione e riaccendere lo schermo.


   * Quattro LED RGB WS2812 si illumineranno di blu con effetto respiro.

   .. note::

     Le ventole RGB non si attivano finché la temperatura non raggiunge i 60 °C. Per modificare la soglia di attivazione, vedi :ref:`max_cc_control_fan`.

#. Puoi utilizzare lo strumento ``systemctl`` per ``start``, ``stop``, ``restart`` o controllare lo ``status`` di ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``: Usa questo comando per applicare eventuali modifiche alla configurazione di Pironman 5 MAX.
   * ``start/stop``: Avvia o interrompi il servizio ``pironman5.service``.
   * ``status``: Controlla lo stato operativo del programma ``pironman5`` con il comando ``systemctl``.
