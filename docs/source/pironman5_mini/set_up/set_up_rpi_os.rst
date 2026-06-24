.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configurazione su Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================


.. image:: ../img/pironman5_mini_pic.jpg
    :width: 400
    :align: center


Se hai installato Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge sul tuo Raspberry Pi, dovrai configurare il Pironman 5 Mini utilizzando la riga di comando. Di seguito puoi trovare tutorial dettagliati.

.. note::

  Prima di procedere con la configurazione, devi avviare e accedere al tuo Raspberry Pi.  
  Se non sei sicuro di come effettuare l’accesso, puoi visitare il sito ufficiale di Raspberry Pi: |link_rpi_get_start|.


Configurazione dello spegnimento per disattivare l’alimentazione GPIO
------------------------------------------------------------------------------

Per evitare che la ventola GPIO, alimentata dal GPIO del Raspberry Pi, rimanga attiva dopo lo spegnimento, è fondamentale configurare il Raspberry Pi per disattivare l’alimentazione GPIO.

#. Apri lo strumento di configurazione EEPROM:

   .. code-block::

      sudo raspi-config

#. Vai su **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Seleziona **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Salva le modifiche. Ti verrà chiesto di riavviare affinché le nuove impostazioni abbiano effetto.


.. _install_pironman5_module_mini:

Download e installazione del modulo ``pironman5``
-----------------------------------------------------------

.. .. note::

..    Per i sistemi Raspberry Pi OS Lite, installa prima gli strumenti necessari come ``git`` e ``python3``.

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. Scarica e installa il modulo ``pironman5`` da GitHub.



   .. code-block:: shell

      curl -sSL “https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh” | sudo bash



   .. note::

      1. Se stai usando **Ubuntu**, installa ``curl`` prima: ``sudo apt install curl -y``

      2. Se stai usando la serie Pironman 5 insieme a **PiPower 5**, esegui invece il seguente comando:

      .. code-block:: shell

         curl -sSL “https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh” | sudo bash -s -- --pipower5

#. Dopo aver eseguito l’installer, seleziona il tuo modello di Pironman 5 (1~4).

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. Una volta completata l’installazione, riavvia il Raspberry Pi come richiesto. Il primo avvio potrebbe richiedere fino a 30 secondi mentre i servizi si inizializzano.

   #. Dopo che Pironman 5 Mini si è avviato correttamente, verifica che i seguenti componenti funzionino correttamente.

   * **Pulsante di accensione**

     * Pressione breve: Accensione.
     * Tieni premuto 2 secondi: Arresto sicuro (richiede :ref:`safe_shutdown_mini`).
     * Tieni premuto 5 secondi: Arresto forzato.

   * **LED RGB WS2812**

     * Si illuminano in blu con un effetto di respirazione.

   * **Ventola RGB**

     * Impostata in modalità **Always On** per impostazione predefinita.
     * La modalità di funzionamento può essere modificata tramite comandi o la Dashboard. Vedi :ref:`cc_control_fan_mini`.

   * **Ventola CPU (Ventola del dissipatore attivo)**

     * Regola automaticamente la velocità in base alla temperatura della CPU.
     * Curva predefinita della ventola:

       * < 50°C: Spenta (0%)
       * 50°C+: Bassa (30%)
       * 60°C+: Media (50%)
       * 67,5°C+: Alta (70%)
       * 75°C+: Massima velocità (100%)

#. Puoi utilizzare lo strumento ``systemctl`` per ``start``, ``stop``, ``restart`` o controllare lo ``status`` del servizio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa questo comando per applicare eventuali modifiche alle impostazioni di Pironman 5 Mini.  
   * ``start/stop``: Abilita o disabilita il servizio ``pironman5.service``.  
   * ``status``: Controlla lo stato operativo del programma ``pironman5`` utilizzando lo strumento ``systemctl``.

.. note::

   A questo punto hai configurato con successo il Pironman 5 Mini ed è pronto per l’uso.  
   Per il controllo avanzato dei suoi componenti, consulta :ref:`control_commands_dashboard_mini`.
