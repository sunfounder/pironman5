.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_standard:

.. start_using_openclaw

Utilizzo di OpenClaw
========================================

**Cos'è OpenClaw?**

Immaginalo come una versione potenziata di ChatGPT. Mentre i chatbot tradizionali possono solo parlare (generare testo), OpenClaw può agire. Comprende le tue istruzioni in linguaggio naturale e può effettivamente eseguire operazioni sul tuo computer, come lanciare comandi, gestire file e richiamare vari strumenti.

Ecco alcuni fantastici scenari applicativi:

* **Assistente Personale Tuttofare:** Lascia che ti aiuti a gestire il tuo programma, impostare promemoria e tenere traccia delle attività. Devi solo dirglielo in un'app di chat (come Telegram, WhatsApp) e lui lo ricorderà ed eseguirà.
* "Collante" per l'Automazione:** Può fungere da legante per i tuoi vari servizi. Ad esempio, puoi fargli monitorare un sito web per rilevare variazioni di prezzo. Una volta rilevato un calo di prezzo, può attivare automaticamente un flusso di lavoro di automazione n8n per inviarti una notifica email.
* **Assistente di Sviluppo Dedicato:** Fatti aiutare a gestire server, eseguire script e controllare i log. Puoi semplicemente dire "Controlla il carico di sistema per me", e lui può connettersi in SSH al tuo server, eseguire il comando e restituire i risultati.
* **"Compagno di Giochi" Hardware:** Questo è un caso d'uso molto interessante. Puoi far sì che OpenClaw controlli l'hardware collegato a un Raspberry Pi. Ad esempio, uno sviluppatore lo ha usato per controllare un aspirapolvere robotico con un braccio meccanico, o addirittura per analizzare i dati di un simulatore di guida e visualizzarli su uno schermo LED. Il team ufficiale di Raspberry Pi lo ha persino usato per costruire un photobooth automatico per un matrimonio, semplicemente tramite conversazione, senza scrivere una sola riga di codice!

**Perché installare OpenClaw su un Raspberry Pi?**

Installarlo su un Raspberry Pi ha due vantaggi principali:

* **Isolamento di Sicurezza:** OpenClaw richiede permessi di sistema elevati, il che rappresenta un rischio su un computer principale. Usare un Raspberry Pi come dispositivo dedicato è come metterlo in una "sandbox"; anche se qualcosa va storto, non influenzerà il tuo sistema principale.
* **Sempre Acceso 24/7:** Il Raspberry Pi ha un consumo energetico estremamente basso, permettendogli di rimanere acceso tutto il tempo, pronto per eseguire compiti in qualsiasi momento.

----------------------------------------------------------------

Avvio Rapido di OpenClaw
------------------------------

Se vuoi sperimentare la potenza di OpenClaw il più rapidamente possibile, usa questo metodo. Installerà automaticamente e lancerà una procedura guidata interattiva.

1.  Apri il terminale sul tuo Raspberry Pi ed esegui direttamente il seguente comando. Questo comando scarica lo script di installazione dal sito ufficiale e lo esegue:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: Poiché le nuove versioni vengono aggiornate rapidamente, è normale che i tuoi passaggi di installazione differiscano leggermente.

2.  Lo script scaricherà e installerà automaticamente OpenClaw.

    .. image:: /pironman5/home_server/img/openclaw/install_open_claw.png


3.  Vedrai quindi un messaggio di sicurezza che ti chiede se ti fidi di OpenClaw. Una volta che sei sicuro che sia sicuro e affidabile, usa i tasti freccia per navigare su "Yes" e premi Invio.

    .. image:: /pironman5/home_server/img/openclaw/security_open_claw.png


4.  Seleziona "Quick Start", quindi premi Invio.

    .. image:: /pironman5/home_server/img/openclaw/quickstart_open_claw.png

5.  Seleziona il tuo Modello (Model), quindi premi Invio. Qui usiamo OpenAI come esempio.

    .. image:: /pironman5/home_server/img/openclaw/model_provider_open_claw.png

6.  Seleziona "OpenAI API Key".

    .. image:: /pironman5/home_server/img/openclaw/api_key_open_claw.png

7.  Incolla ora la chiave API.

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_open_claw.png

8.  Vai su |link_openai_platform| e accedi. Nella pagina **API keys**, clicca su **Create new secret key**.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create.png

9.  Compila i dettagli (Proprietario, Nome, Progetto e permessi se necessario), quindi clicca su **Create secret key**.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create_confirm.png

10. Una volta creata la chiave, copiala immediatamente — non potrai più vederla. Se la perdi, dovrai generararne una nuova.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_copy.png

11. Incolla la chiave nella configurazione di OpenClaw.

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_enter_open_claw.png

12. Seleziona il Modello (Model) che desideri utilizzare. In questo esempio, useremo **Keep current** (Mantieni corrente).

    .. image:: /pironman5/home_server/img/openclaw/model_config_open_claw.png

13. Successivamente c'è la selezione del canale (Channel). I canali si riferiscono ai servizi di comunicazione supportati da OpenClaw, come Telegram, WhatsApp, Discord e altri. Usa il tasto freccia giù per selezionare l'opzione "Skip for now" (Salta per ora), quindi premi Invio.

    .. image:: /pironman5/home_server/img/openclaw/channel_open_claw.png

14. Successivamente, ti verrà chiesto se configurare le abilità (skills) immediatamente. Seleziona "Yes" e premi Invio.

    .. image:: /pironman5/home_server/img/openclaw/config_skill_open_claw.png

15. Installa le abilità di cui hai bisogno. Nell'esempio seguente, selezioniamo l'opzione "Skip for now" (premi la barra spaziatrice per selezionare), quindi premi Invio.

    .. image:: /pironman5/home_server/img/openclaw/install_skill_open_claw.png


16. Successivamente ci sono gli Hook; selezioneremo "command-logger" e "session-memory".

    .. image:: /pironman5/home_server/img/openclaw/hooks2_open_claw.png


17. L'installazione è ora completa. Puoi avviare OpenClaw selezionando "Hatch in TUI" e premendo Invio.

   .. image:: /pironman5/home_server/img/openclaw/hatch_open_claw.png


.. note:: 
   
   Puoi avviare OpenClaw inserendo il seguente comando:

    .. code-block:: bash

       openclaw tui

   E puoi premere ctrl+c due volte per uscire dall'interfaccia TUI.




-----------------------------------------------------

.. end_using_openclaw

Abilitare OpenClaw a Operare il Pironman5
----------------------------------------------

Per consentire a OpenClaw di operare il Pironman5, dobbiamo installare l'abilità (skill) Pironman5.

1.  Assicurati di aver già installato Pironman5. In caso contrario, consulta :ref:`install_pironman5_module_5`.

2.  Esegui il seguente comando nel terminale:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-skill/ ~/.openclaw/skills/pironman5-skill/

3.  Ora puoi operare il Pironman5 in ``openclaw tui``. Prova a inviare comandi nella TUI, ad esempio provando ad accendere le luci LED sulla scocca, cambiarne il colore o far scattare una foto alla fotocamera. Puoi anche dirgli che hai un modulo DHT11 collegato al GPIO17 e lasciare che ti dica la temperatura.

   .. note:: Se OpenClaw non riesce ancora a riconoscere l'abilità importata, ricordagli di fare rsync.

---------------------------------------

.. start_using_openclaw_telegram

Opera il Tuo Sistema con Telegram
---------------------------------------


**Panoramica**

Tramite OpenClaw, puoi utilizzare le popolari app di messaggistica per operare il tuo sistema (qui usiamo Telegram come esempio). Puoi persino lasciare che OpenClaw ti aiuti a completare questa configurazione.

Chiedi semplicemente in ``openclaw tui``: *"Voglio connetterti a Telegram, cosa devo fare?"*

Ti guiderà passo dopo passo attraverso il processo e potrai seguire le sue istruzioni per completare la configurazione.


**Prerequisiti**

Prima di iniziare, assicurati di avere:

- Un **account Telegram**
- Accesso alla rete a Telegram
- OpenClaw in esecuzione con successo (verifica con ``openclaw status``)

**Passo 1: Creare un Bot Telegram**

1. **Trova @BotFather su Telegram** (il creatore ufficiale di bot)
2. **Crea un nuovo bot**: Invia il comando ``/newbot``
3. **Segui le istruzioni**:

   - Dai un nome al tuo bot (es., ``Il mio Assistente OpenClaw``)
   - Imposta un nome utente per il tuo bot (deve terminare con ``bot``, es., ``mio_openclaw_bot``)

4. **In caso di successo, riceverai un messaggio** contenente il tuo **Token del Bot**, simile a:

   .. code-block:: text

      1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

   .. warning:: Proteggi questo token come una password!

**Passo 2: Configurare Telegram in OpenClaw**

In ``openclaw tui``, di' direttamente:

> *"Voglio connettere il mio bot Telegram a OpenClaw. Ecco il mio Token del Bot: <tuo-token-qui>. Per favore, aiutami a completare la configurazione."*

OpenClaw automaticamente:

- Installerà le dipendenze necessarie (come ``node-telegram-bot-api``)
- Creerà il file di configurazione del gateway Telegram
- Testerà se la connessione ha successo


**Passo 3: Testare la Connessione**

1. Trova il tuo bot appena creato su Telegram
2. Invia il comando ``/start``
3. Il bot dovrebbe rispondere con un codice di associazione (pairing code), invia questo codice alla TUI di OpenClaw (es. ``Pairing code: ZAN4XI34``)
4. Attendi che sia configurato correttamente
5. Prova a inviare comandi semplici come "ciao"
6. Se tutto è configurato correttamente, dovresti vedere la risposta dal tuo bot

**Passo 4: Goditelo!**

Dopo aver completato questa configurazione, sarai in grado di:

* Controllare il tuo Raspberry Pi sempre e ovunque tramite Telegram
* Eseguire comandi in remoto e controllare lo stato del sistema
* Controllare dispositivi fisici integrando GPIO (come accendere LED)
* Godere di un'esperienza interattiva intelligente con il tuo assistente AI


**Configurazione di Sicurezza (Fondamentale!)**

Per impedire a sconosciuti di controllare il tuo sistema, assicurati di implementare le seguenti misure di sicurezza:

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Misura di Sicurezza
     - Metodo di Configurazione
     - Descrizione
   * - Limitare gli Utenti
     - Imposta ``allowedUsers`` nella configurazione
     - Consenti solo a specifici utenti Telegram
   * - Impostare una Password
     - Aggiungi ``"password": "tua-password"`` nella configurazione
     - Richiede la verifica della password prima dei comandi
   * - Limitare i Comandi
     - Crea una whitelist di comandi
     - Consenti solo specifici comandi predefiniti
   * - Log di Audit
     - Abilita l'hook ``command-logger``
     - Registra tutti i comandi eseguiti tramite Telegram


**Ricorda: prima la sicurezza!** Limita sempre gli utenti e l'ambito dei comandi in modo appropriato. Se incontri problemi specifici durante la configurazione, non esitare a chiedere aiuto.

-------------------------------------

.. end_using_openclaw_telegram

.. start_using_openclaw_faq

Risoluzione dei Problemi di OpenClaw
-------------------------------------

D. Durante l'installazione, ottengo l'errore ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. Cosa devo fare?

   Puoi ignorarlo per ora, ma potresti incontrare problemi nei passaggi successivi. Ti preghiamo di affrontarli uno per uno in quel momento.


D. Quando eseguo ``openclaw tui``, ottengo l'errore ``-bash: openclaw: command not found``. Cosa devo fare?

   Esegui il seguente comando:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Ora dovresti essere in grado di avviare l'interfaccia TUI con ``openclaw tui``.



D. In ``openclaw tui``, incontro l'errore ``not connected to gateway — message not sent`` o il messaggio ``gateway disconnected: closed``.

   Questo accade perché il servizio OpenClaw Gateway non è avviato. Apri un altro terminale ed esegui il seguente comando per avviare OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway

   Quindi riavvia ``openclaw tui`` e potrai usarlo direttamente.


D. Voglio impostare il servizio OpenClaw Gateway per farlo funzionare in background / avviarlo automaticamente all'avvio. Come faccio?

   Normalmente, il tuo servizio OpenClaw Gateway dovrebbe avviarsi automaticamente all'avvio. In caso contrario, puoi avviarlo manualmente con il seguente comando.

   1. Crea la directory ``~/.config/systemd/user``:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Crea il file ``openclaw-gateway.service``:

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. Quindi ricarica la configurazione di systemd:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Avvia il servizio:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   A questo punto, riavvia ``openclaw tui`` e potrai usarlo direttamente.

   5. Abilitalo all'avvio automatico:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


D. Il mio OpenClaw non può operare il sistema, cosa devo fare?

   Un'installazione nuova di OpenClaw potrebbe non avere il permesso di operare il tuo sistema Raspberry Pi per impostazione predefinita; può solo chattare. Dobbiamo configurare manualmente i permessi.

   1.  Apri il file di configurazione di OpenClaw:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Trova le opzioni ``tools`` e modifica ``profile`` e ``exec`` come segue.

      .. code-block:: json

         "tools": {
            "profile": "coding",
            "exec": {
               "secrity": "full"
            }
         },

   3.  Salva ed esci.

   4.  Inserisci il seguente comando nel terminale per riavviare OpenClaw Gateway:

      .. code-block:: bash

         openclaw gateway restart

   Ora OpenClaw dovrebbe avere i permessi di lettura e scrittura ed essere in grado di operare il tuo sistema Raspberry Pi.

.. end_using_openclaw_faq