.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configurazione con Home Assistant
============================================

Se hai installato il sistema Home Assistant, dovrai aggiungere i componenti aggiuntivi necessari e avviarli per utilizzare Pironman 5 Mini.

.. note::

    Il seguente metodo è valido solo per sistemi con Home Assistant installato nativamente. Non si applica a versioni installate sopra Raspberry Pi OS né a versioni Docker di Home Assistant.

1. Accesso a Home Assistant
---------------------------------

* Dopo l’avvio di Pironman 5 Mini, si consiglia di collegare direttamente un cavo Ethernet. In questo modo puoi aprire il browser del tuo computer e inserire: ``homeassistant.local:8123`` per accedere a Home Assistant.

  .. image:: img/home_login.png
   :width: 90%


* Seleziona **CREATE MY SMART HOME** e crea il tuo account.

  .. image:: img/home_account.png
   :width: 90%

* Segui le istruzioni per scegliere la tua posizione e altre configurazioni. Una volta completato, accederai alla dashboard di Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Aggiungi il repository di componenti SunFounder
--------------------------------------------------------

La funzionalità di Pironman 5 Mini è fornita sotto forma di componenti aggiuntivi su Home Assistant. Prima di tutto, devi aggiungere il repository **SunFounder**.

#. Vai su **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Clicca sul simbolo **+** in basso a destra per entrare nello store dei componenti aggiuntivi.

   .. image:: img/home_addon.png
      :width: 90%

#. Nel negozio, clicca sul menu in alto a destra e seleziona **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Inserisci l'URL del repository di SunFounder: ``https://github.com/sunfounder/home-assistant-addon`` e clicca su **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Una volta aggiunto con successo, chiudi la finestra pop-up e aggiorna la pagina. Trova l’elenco dei componenti aggiuntivi SunFounder.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Installa il componente **Pi Config Wizard**
------------------------------------------------------

Il **Pi Config Wizard** ti aiuta ad abilitare le configurazioni necessarie per Pironman 5 Mini, come I2C e SPI. Può essere rimosso in seguito se non serve più.

#. Trova **Pi Config Wizard** nell’elenco SunFounder e clicca per entrare.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Nella pagina **Pi Config Wizard**, fai clic su **INSTALL**. Attendi il completamento dell'installazione.

   .. image:: img/home_config_install.png
      :width: 90%

#. Dopo l’installazione, passa alla scheda **Log** per verificare che non ci siano errori.

   .. image:: img/home_log.png
      :width: 90%

#. Se non ci sono errori, torna su **Info** e clicca su **START** per avviare il componente.

   .. image:: img/home_start.png
      :width: 90%

#. Ora clicca su **OPEN WEB UI**.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Nell’interfaccia Web, seleziona **MOUNT** per montare la partizione di avvio.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Dopo il mount, abilita I2C e SPI. Una volta attivati, clicca sul pulsante di riavvio in basso per riavviare Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Dopo il riavvio, aggiorna la pagina. Tornerai alla schermata **MOUNT**, clicca di nuovo su **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Di solito SPI sarà attivo, mentre I2C no. Abilita nuovamente I2C e riavvia.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Dopo il riavvio, torna nuovamente alla pagina **MOUNT**. Vedrai che sia I2C che SPI sono abilitati.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Se la pagina non si aggiorna alla partizione di mount, torna su **Settings** -> **Add-ons** -> **Pi Config Wizard**.
    * Assicurati che il componente sia in esecuzione. In caso contrario, clicca su **START**.
    * Dopo l'avvio, clicca su **OPEN WEB UI** e poi su **MOUNT** per verificare I2C e SPI.



4. Installa il componente **Pironman 5 Mini**
---------------------------------------------------

Ora puoi procedere con l’installazione del componente **Pironman 5 Mini**.

#. Vai su **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Clicca sul simbolo **+** per accedere allo store.

   .. image:: img/home_addon.png
      :width: 90%

#. Trova **Pironman 5 Mini** nell’elenco SunFounder e clicca per entrare.

   .. image:: img/home_pironman5_mini_addon.png
      :width: 90%

#. Procedi all’installazione del componente.

   .. image:: img/home_pironman5_mini_addon_install.png
      :width: 90%

#. Al termine, clicca su **START**. Vedrai quattro LED WS2812 RGB accendersi di blu in modalità respiro.

   .. image:: img/home_pironman5_mini_addon_start.png
      :width: 90%

#. Clicca su **OPEN WEB UI** per accedere alla pagina web di Pironman 5 Mini. Puoi anche spuntare l’opzione per mostrare il Web UI nella sidebar.

   .. image:: img/home_pironman5_mini_webui.png
      :width: 90%

#. Ora puoi visualizzare le informazioni del tuo Raspberry Pi, configurare gli RGB, controllare la ventola e molto altro.

   .. image:: img/home_web.png
      :width: 90%

.. note::

   A questo punto, hai completato con successo la configurazione del Pironman 5 Mini ed è pronto per l’uso.
   
   Per un controllo avanzato dei suoi componenti, fai riferimento a :ref:`control_commands_dashboard_mini`.
