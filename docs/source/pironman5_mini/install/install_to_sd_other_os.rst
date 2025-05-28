.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotto e anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi a premi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

.. _install_to_sd_home_bridge_mini:

Installazione del sistema operativo su scheda Micro SD
======================================================

Se stai utilizzando una scheda Micro SD, puoi seguire il tutorial qui sotto per installare il sistema sulla tua scheda.

**Componenti necessari**

* Un computer personale
* Una scheda Micro SD e un lettore

**Procedura**

#. Inserisci la scheda SD nel tuo computer o laptop utilizzando un lettore.

#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Clicca sulla scheda **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo alla pagina e seleziona il tuo sistema operativo.

   .. note::

      * Per il sistema **Ubuntu**, clicca su **Other general-purpose OS** -> **Ubuntu**, e seleziona **Ubuntu Desktop 24.04 LTS (64 bit)** o **Ubuntu Server 24.04 LTS (64 bit)**.
      * Per **Kali Linux**, **Home Assistant** e **Homebridge**, clicca su **Other specific-purpose OS** e seleziona il sistema corrispondente.

   .. image:: img/os_other_os.png
      :width: 90%

#. Nella sezione **Storage**, seleziona il dispositivo di archiviazione appropriato per l’installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Clicca su **NEXT**.

   .. note::

      * Per i sistemi che non possono essere configurati in anticipo, dopo aver cliccato su **NEXT**, ti verrà chiesto se desideri sovrascrivere i dati presenti sul dispositivo. Se hai già eseguito un backup, seleziona **Yes**.

      * Per i sistemi in cui è possibile configurare in anticipo Hostname, Wi-Fi e SSH, apparirà una finestra di dialogo per applicare le impostazioni personalizzate del sistema operativo. Puoi scegliere **Yes**, **No** oppure tornare indietro per ulteriori modifiche.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Definisci un **hostname** per il tuo Raspberry Pi. Il nome host identifica il tuo Raspberry Pi in rete. Puoi accedervi tramite ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png  

   * Crea un **Username** e una **Password** per l’account amministratore del Raspberry Pi. Impostare credenziali univoche è fondamentale per garantire la sicurezza del dispositivo.

     .. image:: img/os_set_username.png

   * Configura la rete wireless LAN inserendo il **SSID** e la **Password** della tua rete.

     .. note::

         Imposta il ``Wireless LAN country`` utilizzando il codice a due lettere `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua posizione geografica.

     .. image:: img/os_set_wifi.png

   * Per connetterti in remoto al tuo Raspberry Pi, abilita SSH nella scheda Servizi.

     * Per **l’autenticazione tramite password**, utilizza nome utente e password impostati nella scheda Generale.
     * Per l’autenticazione a chiave pubblica, seleziona "Allow public-key authentication only". Se disponi già di una chiave RSA, verrà utilizzata. In caso contrario, clicca su "Run SSH-keygen" per generare una nuova coppia di chiavi.

     .. image:: img/os_enable_ssh.png

   * Il menu **Options** consente di configurare il comportamento di Imager durante la scrittura, come l’emissione di un suono al termine, l’espulsione del supporto o l’attivazione della telemetria.

     .. image:: img/os_options.png

#. Una volta completata la personalizzazione del sistema operativo, clicca su **Save** per salvare le impostazioni. Successivamente, clicca su **Yes** per applicarle durante la scrittura dell’immagine.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Se la scheda SD contiene dati, assicurati di eseguire un backup per evitare perdite. Procedi cliccando su **Yes** se non è necessario alcun backup.

   .. image:: img/os_continue.png
      :width: 90%


#. Quando visualizzi il messaggio "Write Successful", l’immagine è stata scritta e verificata correttamente. Ora sei pronto ad avviare il Raspberry Pi dalla tua scheda Micro SD!
