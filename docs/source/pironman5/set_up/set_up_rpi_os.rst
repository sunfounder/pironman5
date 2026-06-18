.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




Configurazione su Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
==================================================================

.. image:: ../img/pironman5_pic.jpg
    :width: 400
    :align: center


Se hai installato Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge sul tuo Raspberry Pi, dovrai configurare il Pironman 5 usando la riga di comando.

.. note::

  Prima della configurazione, devi avviare e accedere al tuo Raspberry Pi. Se non sei sicuro di come accedere, visita il sito ufficiale di Raspberry Pi: |link_rpi_get_start|.


.. _safe_shutdown_5:

1. Configurazione dell'arresto per disattivare l'alimentazione GPIO
-------------------------------------------------------------------

Per evitare che lo schermo OLED e le ventole GPIO, alimentate dal GPIO del Raspberry Pi, rimangano attive dopo l'arresto, è essenziale configurare il Raspberry Pi per disattivare l'alimentazione GPIO.

#. Apri lo strumento di configurazione EEPROM:

   .. code-block::

      sudo raspi-config

#. Vai a **Opzioni avanzate → A12 Comportamento all'arresto**.

   .. image:: img/shutdown_behaviour.png

#. Seleziona **B1 Spegnimento completo...**.

   .. image:: img/run_power_off.png

#. Salva le modifiche. Ti verrà chiesto di riavviare per applicare le nuove impostazioni.


.. _install_pironman5_module_5:

2. Installazione del modulo ``pironman5``
-----------------------------------------------------------

.. note::

   Per i sistemi Raspberry Pi OS Lite, installa prima gli strumenti necessari come ``git`` e ``python3``.

   .. code-block:: shell

      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Scarica e installa il modulo ``pironman5`` da GitHub.

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

   .. note::

      Se usi la serie Pironman 5 insieme a PiPower 5, esegui invece il seguente comando:

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --pipower5

#. Dopo aver eseguito il programma di installazione, seleziona il tuo modello Pironman 5 (1~4).

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. Una volta completata l'installazione, riavvia il Raspberry Pi come richiesto. Il primo avvio potrebbe richiedere fino a 30 secondi mentre i servizi si inizializzano.

#. Dopo che il Pironman 5 si è avviato correttamente, verifica che i seguenti componenti funzionino correttamente.

   * **Schermo OLED**

     * Visualizza l'utilizzo della CPU, della RAM, la temperatura della CPU e l'indirizzo IP.
     * Si spegne automaticamente dopo 10 secondi.
     * Premi brevemente il pulsante di accensione per riattivare lo schermo o cambiare pagina.

   * **Pulsante di accensione**

     * Pressione breve: Accensione / riattivazione OLED / cambio pagina OLED.
     * Tieni premuto 2 secondi: Arresto sicuro (richiede :ref:`safe_shutdown_5`).
     * Tieni premuto 5 secondi: Arresto forzato.

   * **LED RGB WS2812**

     * Si illuminano in blu con un effetto di respirazione.

   * **Due ventole GPIO**

     * Impostate in modalità **Sempre attive** per impostazione predefinita.
     * La modalità di funzionamento può essere modificata tramite comandi o la Dashboard.


   * **Ventola CPU (ventola del dissipatore a torre)**

     * Regola automaticamente la velocità in base alla temperatura della CPU.
     * Curva predefinita della ventola:

       * < 50°C: Spenta (0%)
       * 50°C+: Bassa (30%)
       * 60°C+: Media (50%)
       * 67,5°C+: Alta (70%)
       * 75°C+: Massima velocità (100%)

#. Usa ``systemctl`` per gestire ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   Sostituisci ``restart`` con ``start``, ``stop`` o ``status`` secondo necessità per gestire il servizio.

.. note::

   Pironman 5 è ora pronto all'uso.

   Per controlli avanzati e funzionalità della dashboard, vedi :ref:`control_commands_dashboard_5`.
