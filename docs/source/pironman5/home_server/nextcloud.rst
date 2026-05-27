.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configurazione di NextCloudPi
=======================================

NextCloud è una soluzione open-source di cloud storage privato, simile a Google Drive o Dropbox.  
Può essere utilizzato per archiviare file, condividere documenti, sincronizzare foto e gestire calendari e contatti.  
A differenza dei servizi cloud pubblici, NextCloud offre agli utenti il pieno controllo sui propri dati, rendendolo una soluzione ideale per individui e piccoli team che danno priorità alla privacy e alla sicurezza dei dati.

La serie Pironman5, alimentata da Raspberry Pi, offre basso consumo energetico, dimensioni compatte e prestazioni affidabili, rendendola una scelta eccellente per un server cloud privato domestico. In combinazione con NextCloud, può fungere da sistema NAS economico.


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

4. Dopo l'avvio del tuo Raspberry Pi, apri un browser web e visita il tuo indirizzo Portainer: ``https://<indirizzo-ip-del-tuo-rpi>:9443`` .

5. Di default, vedrai un avviso che indica che il sito utilizza un certificato SSL/TLS autofirmato non emesso da un'Autorità di Certificazione (CA) riconosciuta. La maggior parte dei browser mostrerà questo avviso. In questo caso, puoi tranquillamente ignorare l'avviso, accettare il rischio e procedere.

   .. image:: img/home_server_app/private_save.png

#. Al primo accesso, dovrai impostare una password per l'amministratore.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Dopo la registrazione dell'account amministratore, accederai all'interfaccia di Portainer. Dalla barra di navigazione a sinistra, clicca su **Settings (Impostazioni) -> General (Generale)**, trova **App Templates (Modelli Applicazione)**, e inserisci il seguente URL nel campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Clicca su **Save Application Settings (Salva impostazioni applicazione)**. La configurazione richiederà circa 10 secondi.


**Installare NextCloud**

1. Nella barra di navigazione a sinistra, clicca su **Home (Home) -> local**

   .. image:: img/home_server_app/ptn_home_local.png

2. Vai in **Templates (Modelli) -> Application (Applicazione)**. Nella barra di ricerca in alto a destra, digita *nextcloud* e cliccaci sopra.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. Clicca su **Deploy the stack (Distribuisci lo stack)**, e attendi il completamento della distribuzione. Solitamente richiede circa due minuti.

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. Una volta completato, NextCloud sarà installato.

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png


**Utilizzare NextCloud**

1. Apri il tuo browser e visita il tuo indirizzo NextCloud: ``https://<indirizzo-ip-del-tuo-rpi>:32768`` .

.. note::

   Allo stesso modo, vedrai un avviso che indica che il sito utilizza un certificato SSL/TLS autofirmato non emesso da un'Autorità di Certificazione (CA) riconosciuta. La maggior parte dei browser mostrerà questo avviso.  
   In questo caso, puoi tranquillamente ignorare l'avviso, accettare il rischio e procedere.

   .. image:: img/home_server_app/private_save.png

2. Al primo accesso, dovrai impostare una password per l'amministratore.

   .. image:: img/home_server_app/nc_admin_install.png

3. Dopo la registrazione, puoi iniziare a utilizzare NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png