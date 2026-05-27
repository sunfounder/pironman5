.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configurazione di Plex
=======================================

Plex è una potente piattaforma server multimediale che ti permette di organizzare, trasmettere in streaming e accedere ai tuoi film, serie TV, musica e foto su più dispositivi.  
Configurando Plex sulla serie Pironman5 alimentata da Raspberry Pi, puoi creare un centro multimediale domestico accessibile, a basso consumo energetico, funzionante 24 ore su 24, 7 giorni su 7.  
Le dimensioni compatte, il basso consumo energetico e la flessibilità del Raspberry Pi lo rendono una scelta eccellente per ospitare Plex, trasformando il tuo Pi in un hub di intrattenimento personale accessibile dalla tua rete domestica o persino da remoto.


**Preparazione**

* Scheda MicroSD (16 GB+, classe 10 consigliata)  
* Sistema ufficiale Raspberry Pi OS (o Raspberry Pi OS Lite)  
* Connessione di rete stabile (rete cablata Ethernet consigliata)  
* Disco rigido esterno o chiavetta USB (per espandere lo spazio di archiviazione)  


**Installare Portainer**

Apri il terminale e inserisci i seguenti comandi:

1. Installa Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installa Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Riavvia il tuo Raspberry Pi. (Poi procedi immediatamente con i passi seguenti.)

4. Dopo l'avvio del tuo Raspberry Pi, apri un browser web e visita il tuo indirizzo Portainer: ``http://<indirizzo-ip-del-tuo-rpi>:9443`` .

5. Di default, potresti vedere un avviso che indica che il sito utilizza un certificato SSL/TLS autofirmato non emesso da un'Autorità di Certificazione (CA) riconosciuta. La maggior parte dei browser mostrerà questo avviso. In questo caso, puoi tranquillamente ignorarlo, accettare il rischio e procedere.

   .. image:: img/home_server_app/private_save.png

#. Al primo accesso, ti verrà richiesto di impostare una password per l'amministratore.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Dopo aver creato l'account amministratore, accederai all'interfaccia di Portainer. Dalla barra di navigazione a sinistra, vai in **Settings (Impostazioni) -> General (Generale)**, trova **App Templates (Modelli Applicazione)**, e inserisci il seguente URL nel campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Clicca su **Save Application Settings (Salva impostazioni applicazione)**. La configurazione richiederà circa 10 secondi.


**Installare Plex**

1. Nella barra di navigazione a sinistra, clicca su **Home (Home) -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2. Vai in **Templates (Modelli) -> Application (Applicazione)**. Nella barra di ricerca in alto a destra, digita *plex* e cliccaci sopra.

   .. image:: img/home_server_app/ptn_temp_plex.png

#. Imposta la modalità di rete su **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

#. Espandi **Show advanced options (Mostra opzioni avanzate)**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#. Nella sezione **volume mapping (mappatura volumi)**, configura i percorsi di archiviazione per i tuoi file multimediali e concedi a Plex i permessi di lettura/scrittura. I percorsi predefiniti sono ``/portainer/TV`` e ``/portainer/Movies``, entrambi con accesso in lettura/scrittura abilitato.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#. Clicca su **Deploy (Distribuisci)** e attendi il completamento dell'installazione di Plex.


**Configurare il Server Plex**

1. Apri il tuo browser e inserisci: ``http://<tua_ip>:32400/web`` . Dovresti ora vedere l'interfaccia di Plex.

   .. image:: img/home_server_app/plex_visit.png

2. Ignora l'offerta di abbonamento premium.

3. Successivamente, vedrai la schermata di **Configurazione del server (Server Setup)**. Puoi spuntare *Consenti l'accesso ai miei media fuori casa (Allow me to access my media outside my home)*. Per ora, si consiglia di lasciare questa opzione deselezionata e configurarla in seguito se necessario.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Ti verrà quindi chiesto di organizzare i tuoi media. Puoi scegliere *Salta (Skip)* e aggiungere i media in seguito tramite le impostazioni. Tuttavia, si consiglia di aggiungere direttamente i percorsi di archiviazione che hai configurato nella mappatura dei volumi di Portainer, in modo che Plex possa scannerizzare e importare automaticamente i tuoi media.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Seleziona il tipo della tua libreria multimediale, dai un nome alla tua libreria e scegli la lingua.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Aggiungi cartelle. Individua i percorsi di archiviazione dei media che hai definito in precedenza e clicca su **Aggiungi libreria (Add Library)**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Clicca su **Termina (Finish)**. Il tuo server Plex su Raspberry Pi è ora completamente configurato.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Dovresti ora vedere i tuoi file multimediali visualizzati nella home page del server Plex.

   .. image:: img/home_server_app/plex_index.png