.. note:: 

    Ciao, benvenuto nella Community di SunFounder dedicata agli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e difficoltà tecniche con l’aiuto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni speciali e omaggi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Configurazione su Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

Se hai installato Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge sul tuo Raspberry Pi, dovrai configurare il Pironman 5 Mini utilizzando la riga di comando. Di seguito puoi trovare tutorial dettagliati.

.. note::

  Prima di procedere con la configurazione, devi avviare e accedere al tuo Raspberry Pi.  
  Se non sei sicuro di come effettuare l’accesso, puoi visitare il sito ufficiale di Raspberry Pi: |link_rpi_get_start|.


Configurazione dello spegnimento per disattivare l’alimentazione GPIO
------------------------------------------------------------------------------

Per evitare che la ventola RGB, alimentata dal GPIO del Raspberry Pi, rimanga attiva dopo lo spegnimento, è fondamentale configurare il Raspberry Pi per disattivare l’alimentazione GPIO.

#. Apri lo strumento di configurazione EEPROM:

   .. code-block::

      sudo raspi-config

#. Vai su **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Seleziona **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Salva le modifiche. Ti verrà chiesto di riavviare affinché le nuove impostazioni abbiano effetto.

Download e installazione del modulo ``pironman5``
-----------------------------------------------------------

.. note::

   Per i sistemi “lite”, installa inizialmente strumenti come ``git``, ``python3``, ``pip3``, ``setuptools``, ecc.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procedi a scaricare il codice da GitHub e installare il modulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Dopo un’installazione riuscita, è necessario riavviare il sistema per attivare l’installazione. Segui il prompt a schermo per riavviare.

   Al riavvio, il servizio ``pironman5.service`` verrà avviato automaticamente.  
   Ecco le configurazioni principali di Pironman 5 Mini:
   
   * Quattro LED WS2812 RGB si illumineranno di blu con un effetto di respirazione.
     
   .. note::
    
     * Le ventole RGB sono impostate di default su **Always On**.  
       Per impostare temperature di attivazione differenti, consulta :ref:`cc_control_fan_mini`.

#. Puoi utilizzare lo strumento ``systemctl`` per ``start``, ``stop``, ``restart`` o controllare lo ``status`` del servizio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa questo comando per applicare eventuali modifiche alle impostazioni di Pironman 5 Mini.  
   * ``start/stop``: Abilita o disabilita il servizio ``pironman5.service``.  
   * ``status``: Controlla lo stato operativo del programma ``pironman5`` utilizzando lo strumento ``systemctl``.

.. note::

   A questo punto hai configurato con successo il Pironman 5 Mini ed è pronto per l’uso.  
   Per il controllo avanzato dei suoi componenti, consulta :ref:`control_commands_dashboard_mini`.
