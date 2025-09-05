.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche con il supporto della nostra community e del nostro team.
    - **Learn & Share**: Condividi suggerimenti e tutorial per migliorare le tue abilità.
    - **Exclusive Previews**: Accedi in anteprima ai nuovi annunci e alle anticipazioni sui prodotti.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway esclusivi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!


Configurazione di Plex
=======================================

Plex è una potente piattaforma di server multimediale che ti permette di organizzare, trasmettere in streaming e accedere ai tuoi film, programmi TV, musica e foto su più dispositivi.  
Configurando Plex sulla serie Pironman5 alimentata da Raspberry Pi, puoi creare un centro multimediale domestico economico ed efficiente dal punto di vista energetico che funziona 24/7.  
Le dimensioni compatte, il basso consumo energetico e la flessibilità del Raspberry Pi lo rendono una scelta eccellente per ospitare Plex, trasformando il tuo Pi in un hub di intrattenimento personale accessibile dalla tua rete domestica o persino da remoto.


**Preparazione**

* Scheda MicroSD (16GB+, Classe 10 consigliata)  
* Sistema ufficiale Raspberry Pi OS (o Raspberry Pi OS Lite)  
* Connessione di rete stabile (Ethernet cablata consigliata)  
* Disco rigido esterno o chiavetta USB (per espansione della memoria)  


**Installare Portainer**

Apri il terminale e inserisci i seguenti comandi:

1. Installare Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installare Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Apri il browser e visita il tuo indirizzo Portainer: ``http://<your-rpi-ip-address>:9443`` .

.. note::

   Per impostazione predefinita, potresti vedere un avviso che il sito utilizza un certificato SSL/TLS autofirmato non emesso da un’Autorità di Certificazione (CA) riconosciuta.  
   La maggior parte dei browser web mostrerà tale avviso.  
   In questo caso, puoi ignorarlo in sicurezza, accettare il rischio e procedere.

   .. image:: img/home_server_app/private_save.png


4. Al primo accesso, ti verrà chiesto di impostare una password di amministratore.

   .. image:: img/home_server_app/ptn_new_admin.png

5. Dopo aver creato l’account amministratore, entrerai nell’interfaccia di Portainer. Dal menu di navigazione a sinistra, vai su **Setting -> General**, trova **App Templates** e inserisci il seguente URL nel campo:  
   ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Fai clic su **Save Application Settings**. La configurazione richiederà circa 10 secondi.


**Installare Plex**

1. Dal menu di navigazione a sinistra, fai clic su **Home -> local -> Templates -> Application**. Nella barra di ricerca in alto a destra, digita *plex* e selezionalo.

   .. image:: img/home_server_app/ptn_temp_plex.png

2. Imposta la modalità di rete su **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

3. Espandi **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

4. Nella sezione **volume mapping**, configura i percorsi di archiviazione per i tuoi file multimediali e concedi a Plex i permessi di lettura/scrittura.  
   I percorsi predefiniti sono ``/portainer/TV`` e ``/portainer/Movies``, entrambi con accesso in lettura/scrittura abilitato.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

5. Fai clic su **Deploy** e attendi che l’installazione di Plex sia completata.


**Configurare il server Plex**

1. Apri il browser e inserisci: ``http://<your_ip>:32400/`` . Ora dovresti vedere l’interfaccia di Plex.

   .. image:: img/home_server_app/plex_visit.png

2. Salta l’offerta di abbonamento premium.

3. Successivamente, vedrai la schermata **Server Setup**. Puoi selezionare *Allow me to access my media outside my home*.  
   Per ora, si consiglia di lasciarla deselezionata e configurarla in seguito se necessario.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Ti verrà quindi chiesto di organizzare i tuoi contenuti multimediali. Puoi scegliere *Skip* e aggiungere i contenuti più tardi dalle impostazioni.  
   Tuttavia, si consiglia di aggiungere direttamente i percorsi di archiviazione che hai configurato nel mapping dei volumi di Portainer, in modo che Plex possa scansionare e importare automaticamente i tuoi media.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Seleziona il tipo di libreria multimediale, assegna un nome alla libreria e scegli la lingua.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Aggiungi cartelle. Individua i percorsi di archiviazione dei media che hai configurato in precedenza e fai clic su **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Fai clic su **Finish**. Il tuo server Plex su Raspberry Pi è ora completamente configurato.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Ora dovresti vedere i tuoi file multimediali visualizzati sulla homepage del server Plex.

   .. image:: img/home_server_app/plex_index.png
