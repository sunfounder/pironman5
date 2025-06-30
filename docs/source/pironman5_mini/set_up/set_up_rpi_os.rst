.. note:: 

    Ciao, benvenuto nella Community di SunFounder dedicata agli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e difficoltà tecniche con l’aiuto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni speciali e omaggi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _set_up_pironman5_mini:

Configurazione su Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

Se hai installato Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge sul tuo Raspberry Pi, sarà necessario configurare il Pironman 5 Mini tramite riga di comando. Di seguito trovi i tutorial dettagliati:

.. note::

  Prima della configurazione, è necessario avviare e accedere al Raspberry Pi. Se non sai come farlo, visita il sito ufficiale Raspberry Pi: |link_rpi_get_start|.


Configurazione dello spegnimento per disattivare l'alimentazione GPIO
-----------------------------------------------------------------------------
Per evitare che la ventola RGB alimentata dai GPIO del Raspberry Pi resti attiva dopo lo spegnimento, è importante configurare lo spegnimento dell'alimentazione GPIO.

#. Modifica manualmente il file di configurazione ``EEPROM`` con questo comando:

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. Modifica l'impostazione ``POWER_OFF_ON_HALT`` impostandola a ``1``. Esempio:

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Premi ``Ctrl + X``, poi ``Y`` e ``Enter`` per salvare le modifiche.


Download e installazione del modulo ``pironman5``
-----------------------------------------------------------

#. Nei sistemi "lite", installa prima strumenti come ``git``, ``python3``, ``pip3``, ``setuptools``, ecc.
  
   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procedi al download del codice da GitHub e all’installazione del modulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Dopo l’installazione, è necessario riavviare il sistema per rendere attiva l’installazione. Segui il messaggio a schermo per il riavvio.

   Al riavvio, il servizio ``pironman5.service`` verrà avviato automaticamente. Ecco le principali configurazioni di Pironman 5:
   
   * I quattro LED WS2812 RGB si accenderanno in blu con effetto respiro.
     
   .. note::
    
     La ventola RGB non si attiverà finché la temperatura non raggiungerà i 60°C. Per impostare temperature diverse, vedi :ref:`cc_control_fan_mini`.

#. Puoi usare lo strumento ``systemctl`` per ``start``, ``stop``, ``restart`` o controllare lo ``status`` di ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Applica le modifiche effettuate alla configurazione del Pironman 5 Mini.
   * ``start/stop``: Avvia o interrompe il servizio ``pironman5.service``.
   * ``status``: Controlla lo stato di esecuzione del programma ``pironman5`` con lo strumento ``systemctl``.
