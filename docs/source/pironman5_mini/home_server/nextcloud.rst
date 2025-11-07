.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e condividi**: Condividi suggerimenti e tutorial per migliorare le tue abilità.
    - **Anteprime esclusive**: Accedi in anteprima ai nuovi annunci e alle anticipazioni sui prodotti.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway esclusivi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!



Configurazione di NextCloudPi
=======================================

NextCloud è una soluzione open-source di cloud storage privato, simile a Google Drive o Dropbox.  
Può essere utilizzato per archiviare file, condividere documenti, sincronizzare foto e gestire calendari e contatti.  
A differenza dei servizi cloud pubblici, NextCloud offre agli utenti il pieno controllo sui propri dati, rendendolo ideale per individui e piccoli team che valorizzano la privacy e la sicurezza dei dati.

La serie Pironman5 alimentata da Raspberry Pi offre un basso consumo energetico, dimensioni compatte e prestazioni affidabili, il che la rende una scelta eccellente per un server cloud privato domestico. Combinato con NextCloud, può fungere da sistema NAS economico.


**Preparazione**

* Scheda MicroSD (16GB+, Classe 10 consigliata)  
* Sistema ufficiale Raspberry Pi OS (o Raspberry Pi OS Lite)  
* Connessione di rete stabile (Ethernet cablata consigliata)  
* Disco rigido esterno o chiavetta USB (per espandere lo spazio di archiviazione)  


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

   Per impostazione predefinita, vedrai un avviso che il sito utilizza un certificato SSL/TLS autofirmato non rilasciato da un’Autorità di Certificazione (CA) riconosciuta.  
   La maggior parte dei browser web mostrerà un avviso su tali certificati.  
   In questo caso, puoi tranquillamente ignorare l’avviso, accettare il rischio e continuare.

   .. image:: img/home_server_app/private_save.png


4. Al primo accesso, sarà necessario impostare una password di amministratore.

   .. image:: img/home_server_app/ptn_new_admin.png

5. Dopo aver registrato l’account amministratore, entrerai nell’interfaccia di Portainer. Dal menu di navigazione a sinistra, fai clic su **Setting -> General**, trova **App Templates** e inserisci il seguente URL nel campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Fai clic su **Save Application Settings**. La configurazione richiederà circa 10 secondi per essere completata.


**Installare NextCloud**

1. Dal menu di navigazione a sinistra, fai clic su **Home -> local -> Templates -> Application**. Nella barra di ricerca in alto a destra, digita *nextcloud* e fai clic su di esso.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

2. Fai clic su **Deploy the stack** e attendi il completamento della distribuzione. Di solito richiede circa due minuti.

   .. image:: img/home_server_app/ptn_temp_deploy.png

Una volta completato, NextCloud sarà installato.


**Utilizzare NextCloud**

1. Apri il browser e visita il tuo indirizzo NextCloud: ``http://<your-rpi-ip-address>:32768`` .

.. note::

   Allo stesso modo, vedrai un avviso che il sito utilizza un certificato SSL/TLS autofirmato non rilasciato da un’Autorità di Certificazione (CA) riconosciuta.  
   La maggior parte dei browser web mostrerà un avviso su tali certificati.  
   In questo caso, puoi tranquillamente ignorare l’avviso, accettare il rischio e continuare.

   .. image:: img/home_server_app/private_save.png

2. Al primo accesso, sarà necessario impostare una password di amministratore.

   .. image:: img/home_server_app/nc_admin_install.png

3. Dopo la registrazione, puoi iniziare a utilizzare NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png
