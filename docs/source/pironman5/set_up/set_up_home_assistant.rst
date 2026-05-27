.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configurazione su Home Assistant
=============================================

Se hai installato il sistema Home Assistant, sarà necessario aggiungere i componenti aggiuntivi necessari e avviarli per far funzionare il Pironman 5.

.. note::

    Il seguente metodo è applicabile solo ai sistemi con Home Assistant installato nativamente. Non si applica ai sistemi Raspberry Pi con Home Assistant installato sopra o alle versioni Docker di Home Assistant.

1. Accedi a Home Assistant
-------------------------------

* Dopo aver avviato Pironman 5, è consigliato collegare direttamente un cavo Ethernet. In questo modo, puoi aprire il browser del tuo computer e digitare: ``homeassistant.local:8123`` per accedere a Home Assistant.

  .. image:: img/home_login.png
   :width: 90%


* Seleziona **CREA LA MIA CASA SMART**, quindi crea il tuo account.

  .. image:: img/home_account.png
   :width: 90%

* Segui le istruzioni per scegliere la tua posizione e altre configurazioni. Una volta completato, entrerai nella dashboard di Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Aggiungi il repository dei componenti aggiuntivi SunFounder
-------------------------------------------------------------------

La funzionalità di Pironman 5 è installata su Home Assistant sotto forma di componenti aggiuntivi. Per prima cosa, devi aggiungere il repository dei componenti aggiuntivi **SunFounder**.

#. Apri **Impostazioni** -> **Componenti aggiuntivi**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Clicca sul segno più in basso a destra per accedere al negozio dei componenti aggiuntivi.

   .. image:: img/home_addon.png
      :width: 90%

#. Nel negozio dei componenti aggiuntivi, clicca sul menu in alto a destra e seleziona **Repository**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Inserisci l'URL del repository dei componenti aggiuntivi **SunFounder**: ``https://github.com/sunfounder/home-assistant-addon`` e clicca su **AGGIUNGI**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Dopo aver aggiunto correttamente, chiudi la finestra pop-up e aggiorna la pagina. Trova l'elenco dei componenti aggiuntivi SunFounder.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Installa il componente aggiuntivo **Pi Config Wizard**
----------------------------------------------------------------

Il **Pi Config Wizard** può aiutarti ad abilitare le configurazioni necessarie per Pironman 5, come I2C e SPI. Se non necessario successivamente, può essere rimosso.

#. Trova **Pi Config Wizard** nell'elenco dei componenti aggiuntivi SunFounder e clicca per accedere.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Nella pagina del **Pi Config Wizard**, clicca su **INSTALLA**. Attendi il completamento dell'installazione.

   .. image:: img/home_config_install.png
      :width: 90%

#. Dopo il completamento dell'installazione, passa alla pagina **Log** per verificare se ci sono errori.

   .. image:: img/home_log.png
      :width: 90%

#. Se non ci sono errori, torna alla pagina **Info** e clicca su **AVVIA** per avviare questo componente aggiuntivo.

   .. image:: img/home_start.png
      :width: 90%

#. Ora apri la WEB UI.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Nella Web UI, vedrai un'opzione per montare la partizione Boot. Clicca su **MONTA** per montare la partizione.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Dopo il montaggio con successo, vedrai le opzioni per impostare I2C, SPI e modificare il file config.txt. Seleziona I2C e SPI per abilitarli. Una volta abilitati, clicca sul pulsante di riavvio in basso per riavviare il Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Dopo il riavvio, aggiorna la pagina. Tornerai di nuovo alla pagina del montaggio della partizione boot. Clicca di nuovo su **MONTA**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Di solito, vedrai che SPI è abilitato, ma I2C no perché richiede due riavvii. Abilita nuovamente I2C, quindi riavvia il Raspberry Pi.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Dopo il riavvio, torna di nuovo alla pagina **MONTA**. Vedrai che sia I2C che SPI sono abilitati.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Se dopo aver aggiornato la pagina, non accedi alla pagina del montaggio della partizione, puoi cliccare su **Impostazioni** -> **Componenti aggiuntivi** -> **Pi Config Wizard** di nuovo.
    * Verifica se questo componente aggiuntivo è avviato. In caso contrario, clicca su **AVVIA**.
    * Dopo l'avvio, clicca su **APRIRE WEB UI**, quindi clicca su **MONTA** per confermare se I2C e SPI sono abilitati.

4. Installa il componente aggiuntivo **Pironman 5**
-------------------------------------------------------

Ora inizia ufficialmente l'installazione del componente aggiuntivo **Pironman 5**.

#. Apri **Impostazioni** -> **Componenti aggiuntivi**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Clicca sul segno più in basso a destra per accedere al negozio dei componenti aggiuntivi.

   .. image:: img/home_addon.png
      :width: 90%

#. Trova **Pironman 5** nell'elenco dei componenti aggiuntivi **SunFounder** e clicca per accedere.

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Ora installa il componente aggiuntivo Pironman 5.

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. Dopo il completamento dell'installazione, clicca su **AVVIA** per avviare questo componente aggiuntivo. Vedrai lo schermo OLED visualizzare la CPU del Raspberry Pi, la temperatura e altre informazioni correlate. Quattro LED RGB WS2812 si illumineranno di blu con una modalità di respirazione.

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. Ora puoi cliccare su **APRIRE WEB UI** per aprire la pagina web di Pironman 5. Puoi anche selezionare l'opzione per mostrare la Web UI nella barra laterale. Questo ti permetterà di vedere l'opzione Pironman 5 nella barra laterale sinistra di Home Assistant e di cliccare per aprire la pagina Pironman 5.

   .. image:: img/home_web_ui.png
      :width: 90%

#. Ora puoi vedere le informazioni sul tuo Raspberry Pi, configurare i LED RGB e controllare la ventola, ecc.

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

   A questo punto, hai completato con successo la configurazione del Pironman 5 ed è pronto per l’uso.
   
   Per un controllo avanzato dei suoi componenti, fai riferimento a :ref:`control_commands_dashboard_5`.
