.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configurazione su Home Assistant
============================================

Se hai installato il sistema Home Assistant, dovrai aggiungere i componenti aggiuntivi necessari e avviarli per utilizzare correttamente il Pironman 5 MAX.

.. note::

    Il metodo seguente è valido solo per sistemi con Home Assistant installato in modo nativo. Non è applicabile a sistemi Raspberry Pi con Home Assistant installato sopra altri OS né a versioni Docker di Home Assistant.

1. Accedi a Home Assistant
-----------------------------

* Dopo l'avvio del Pironman 5 MAX, si consiglia di collegare direttamente un cavo Ethernet. In questo modo puoi aprire il browser sul computer e digitare: ``homeassistant.local:8123`` per accedere a Home Assistant.

  .. image:: img/home_login.png
   :width: 90%


* Seleziona **CREATE MY SMART HOME**, quindi crea il tuo account.

  .. image:: img/home_account.png
   :width: 90%

* Segui le istruzioni per configurare posizione e altre impostazioni. Al termine, accederai alla dashboard di Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Aggiungi il repository di componenti SunFounder
----------------------------------------------------

Le funzionalità del Pironman 5 MAX sono fornite sotto forma di componenti aggiuntivi. Per prima cosa, aggiungi il repository **SunFounder**.

#. Apri **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Clicca sul simbolo + in basso a destra per accedere allo store dei componenti.

   .. image:: img/home_addon.png
      :width: 90%

#. Nello store, clicca sul menu in alto a destra e seleziona **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Inserisci l'URL del repository **SunFounder**: ``https://github.com/sunfounder/home-assistant-addon`` e clicca su **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Una volta aggiunto con successo, chiudi la finestra popup e aggiorna la pagina. Trova l’elenco dei componenti SunFounder.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Installa il componente **Pi Config Wizard**
------------------------------------------------------

Il **Pi Config Wizard** aiuta ad abilitare configurazioni essenziali per Pironman 5 MAX come I2C e SPI. Può essere rimosso dopo l’uso.

#. Trova **Pi Config Wizard** nell’elenco dei componenti SunFounder e clicca per accedere.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Nella pagina del componente, clicca su **INSTALL** e attendi il completamento dell’installazione.

   .. image:: img/home_config_install.png
      :width: 90%

#. Al termine, vai alla pagina **Log** per verificare la presenza di eventuali errori.

   .. image:: img/home_log.png
      :width: 90%

#. Se non ci sono errori, torna alla pagina **Info** e clicca su **START** per avviare il componente.

   .. image:: img/home_start.png
      :width: 90%

#. Ora apri la WEB UI.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Nella Web UI, troverai l'opzione per montare la partizione Boot. Clicca su **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Una volta montata correttamente, potrai abilitare I2C e SPI e modificare il file config.txt. Seleziona I2C e SPI, attendi che risultino abilitati, quindi clicca sul pulsante di riavvio in basso.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Dopo il riavvio, aggiorna la pagina. Tornerai alla schermata di montaggio. Clicca di nuovo su **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Di norma, SPI sarà già abilitato, mentre I2C richiederà un secondo riavvio. Abilita nuovamente I2C e riavvia il Raspberry Pi.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Dopo il secondo riavvio, torna alla pagina **MOUNT**: entrambi, I2C e SPI, risulteranno attivi.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Se dopo l’aggiornamento della pagina non accedi alla schermata per montare la partizione, clicca nuovamente su **Settings** -> **Add-ons** -> **Pi Config Wizard**.
    * Verifica se il componente è avviato. In caso contrario, clicca su **START**.
    * Dopo l’avvio, clicca su **OPEN WEB UI**, quindi su **MOUNT** per verificare che I2C e SPI siano abilitati.

4. Installa il componente aggiuntivo **Pironman 5 MAX**
---------------------------------------------------------

Ora puoi procedere all’installazione ufficiale del componente aggiuntivo **Pironman 5 MAX**.

#. Vai su **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Clicca sul simbolo + in basso a destra per aprire lo store dei componenti.

   .. image:: img/home_addon.png
      :width: 90%

#. Trova **Pironman 5 MAX** nell’elenco dei componenti **SunFounder** e clicca per accedere.

   .. image:: img/home_pironman5_max_addon.png
      :width: 90%

#. Installa ora il componente Pironman 5 MAX.

   .. image:: img/home_pironman5_max_addon_install.png
      :width: 90%

#. Dopo aver completato l’installazione, clicca su **START** per avviare il componente. Vedrai sullo schermo OLED le informazioni relative alla CPU del Raspberry Pi, alla temperatura e ad altri dati. Quattro LED RGB WS2812 si illumineranno di blu con effetto respiro.

   .. image:: img/home_pironman5_max_addon_start.png
      :width: 90%

#. Ora puoi cliccare su **OPEN WEB UI** per aprire la pagina web di Pironman 5 MAX. Puoi anche attivare l’opzione per visualizzare la Web UI nella barra laterale. In questo modo, l'opzione Pironman 5 MAX sarà sempre accessibile dalla barra laterale di Home Assistant.

   .. image:: img/home_pironman5_max_webui.png
      :width: 90%

#. Potrai così visualizzare le informazioni sul tuo Raspberry Pi, configurare i LED RGB, controllare la ventola e molto altro.

   .. image:: img/home_web.png
      :width: 90%


.. note::

   A questo punto, hai completato con successo la configurazione del Pironman 5 MAX ed è pronto per l’uso.
   
   Per un controllo avanzato dei suoi componenti, fai riferimento a :ref:`control_commands_dashboard_max`.
