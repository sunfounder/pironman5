.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_pi_os:

Configurazione su Raspberry Pi/Ubuntu/Kali/Homebridge OS
==============================================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Se hai installato Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge sul tuo Raspberry Pi, dovrai configurare Pironman 5 Pro MAX utilizzando la riga di comando. I tutorial dettagliati sono disponibili qui sotto:

.. note::

  Prima di configurare, devi avviare e accedere al tuo Raspberry Pi. Se non sei sicuro di come accedere, puoi visitare il sito web ufficiale di Raspberry Pi: |link_rpi_get_start|.

Configurazione dello Spegnimento per Disattivare l'Alimentazione GPIO
------------------------------------------------------------------------------------

Per evitare che lo schermo OLED e le ventole GPIO, alimentati dal GPIO del Raspberry Pi, rimangano attivi dopo lo spegnimento, è essenziale configurare il Raspberry Pi per la disattivazione dell'alimentazione GPIO.

#. Apri lo strumento di configurazione EEPROM:

   .. code-block::

      sudo raspi-config

#. Naviga a **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Seleziona **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Salva le modifiche. Ti verrà chiesto di riavviare per rendere effettive le nuove impostazioni.

.. _install_pironman5_module_promax:

Scaricare e Installare il Modulo ``pironman5``
-----------------------------------------------------------

.. note::

   Per i sistemi lite, installa inizialmente strumenti come ``git``, ``python3``, ``pip3``, ``setuptools``, ecc.

   .. code-block:: shell

      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procedi a scaricare il codice da GitHub e installare il modulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Dopo l'installazione riuscita, è necessario un riavvio del sistema per attivare l'installazione. Segui il prompt di riavvio sullo schermo.

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