.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme agli altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni speciali per le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Configurazione su Raspberry Pi/Ubuntu/Kali/Homebridge OS
=================================================================

Se hai installato Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge sul tuo Raspberry Pi, sarà necessario configurare Pironman 5 utilizzando la riga di comando. I tutorial dettagliati sono disponibili qui sotto:

.. note::

  Prima di configurare, devi avviare e accedere al tuo Raspberry Pi. Se non sei sicuro di come accedere, puoi visitare il sito ufficiale di Raspberry Pi: |link_rpi_get_start|.


Configurazione dello spegnimento per disattivare l'alimentazione GPIO
----------------------------------------------------------------------------
Per evitare che lo schermo OLED e le ventole RGB, alimentate dal GPIO del Raspberry Pi, rimangano attive dopo lo spegnimento, è essenziale configurare il Raspberry Pi per disattivare l'alimentazione del GPIO.

#. Modifica manualmente il file di configurazione ``EEPROM`` con questo comando:

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. Modifica l'impostazione ``POWER_OFF_ON_HALT`` nel file a ``1``. Ad esempio:

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Premi ``Ctrl + X``, ``Y`` e ``Invio`` per salvare le modifiche.


Scaricare e installare il modulo ``pironman5``
-----------------------------------------------------------

#. Per i sistemi lite, installa inizialmente strumenti come ``git``, ``python3``, ``pip3``, ``setuptools``, ecc.
  
   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procedi a scaricare il codice da GitHub e installa il modulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone https://github.com/sunfounder/pironman5.git
      cd ~/pironman5
      sudo python3 install.py


   Dopo una corretta installazione, è necessario un riavvio del sistema per attivare l'installazione. Segui il prompt a schermo per il riavvio.

   Al riavvio, il servizio ``pironman5.service`` si avvierà automaticamente. Ecco le principali configurazioni per Pironman 5:
   
   * Lo schermo OLED mostrerà CPU, RAM, utilizzo del disco, temperatura della CPU e l'indirizzo IP del Raspberry Pi.
   * Quattro LED RGB WS2812 si illumineranno di blu in modalità respiro.
   
   .. note::
   
     I ventilatori RGB non funzioneranno a meno che la temperatura non raggiunga i 60°C. Per temperature di attivazione diverse, consulta :ref:`cc_control_fan`.
   
#. Puoi utilizzare lo strumento ``systemctl`` per ``avviare``, ``fermare``, ``riavviare`` o controllare lo ``stato`` del servizio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Utilizza questo comando per applicare eventuali modifiche apportate alle impostazioni di pironman 5.
   * ``start/stop``: Abilita o disabilita il servizio ``pironman5.service``.
   * ``status``: Verifica lo stato operativo del programma ``pironman5`` utilizzando lo strumento ``systemctl``.

