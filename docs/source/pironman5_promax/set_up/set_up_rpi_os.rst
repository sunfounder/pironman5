.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_set_up_pi_os:

Configurazione su Raspberry Pi/Ubuntu/Kali/Homebridge OS
==========================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Se hai installato Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge sul tuo Raspberry Pi, dovrai configurare Pironman 5 Pro MAX utilizzando la riga di comando. I tutorial dettagliati sono disponibili qui sotto:

.. note::

  Prima di configurare, devi avviare e accedere al tuo Raspberry Pi. Se non sei sicuro di come accedere, puoi visitare il sito web ufficiale di Raspberry Pi: |link_rpi_get_start|.


.. _safe_shutdown_promax:

Configurazione dello Spegnimento per Disattivare l'Alimentazione GPIO
-----------------------------------------------------------------------------

Per evitare che lo schermo OLED e le ventole RGB, alimentati dal GPIO del Raspberry Pi, rimangano attivi dopo lo spegnimento, è essenziale configurare il Raspberry Pi per la disattivazione dell'alimentazione GPIO.

#. Apri lo strumento di configurazione EEPROM:

   .. code-block::

      sudo raspi-config

#. Naviga a **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Seleziona **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Salva le modifiche. Ti verrà chiesto di riavviare per rendere effettive le nuove impostazioni.


.. _promax_download_pironman5_module:

Scaricare e Installare il Modulo ``pironman5``
-----------------------------------------------------------

.. .. note::

..    Per i sistemi Raspberry Pi OS Lite, installa prima gli strumenti necessari come ``git`` e ``python3``.

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. Scarica e installa il modulo ``pironman5`` da GitHub.



   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash



   .. note::

      1. Se stai usando **Ubuntu**, installa ``curl`` prima: ``sudo apt install curl -y``

      2. Se stai usando la serie Pironman 5 insieme a **PiPower 5**, esegui invece il seguente comando:

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --pipower5

#. Dopo aver eseguito l'installer, seleziona il tuo modello di Pironman 5 (1~4).

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supporta: 5 | 5 Mini | 5 Max | 5 Pro Max

      Seleziona il modello del tuo prodotto:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Inserisci il numero [1-4]:

#. Una volta completata l'installazione, riavvia il Raspberry Pi come richiesto. Il primo avvio potrebbe richiedere fino a 30 secondi mentre i servizi si inizializzano.

   Al riavvio, il ``pironman5.service`` si avvierà automaticamente. Ecco le configurazioni principali per Pironman 5 Pro MAX:

   * Lo schermo OLED visualizza CPU, RAM, utilizzo del disco, temperatura della CPU e l'indirizzo IP del Raspberry Pi.
   * Quattro LED RGB WS2812 si accenderanno in blu con modalità respiro.

#. Puoi utilizzare lo strumento ``systemctl`` per ``start``, ``stop``, ``restart`` o controllare lo ``status`` di ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``: Usa questo comando per applicare eventuali modifiche apportate alle impostazioni di Pironman 5 Pro MAX.
   * ``start/stop``: Abilita o disabilita il ``pironman5.service``.
   * ``status``: Controlla lo stato operativo del programma ``pironman5`` usando lo strumento ``systemctl``.

.. note::

   A questo punto, hai configurato con successo Pironman 5 Pro MAX ed è pronto per l'uso.

   Per il controllo avanzato dei suoi componenti, fare riferimento a :ref:`control_commands_dashboard_promax`.
