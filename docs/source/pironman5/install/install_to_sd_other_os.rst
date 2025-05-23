.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_to_sd_home_bridge:

Installazione del Sistema Operativo su una Micro SD
========================================================

Se stai utilizzando una scheda Micro SD, puoi seguire il tutorial qui sotto per installare il sistema sulla tua scheda.


**Componenti necessari**

* Un computer
* Una scheda Micro SD e un lettore

**Passaggi**

#. Inserisci la tua scheda SD nel computer o nel laptop utilizzando un lettore.

#. All'interno del |link_rpi_imager|, clicca su **Dispositivo Raspberry Pi** e seleziona il modello **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      

#. Clicca sulla scheda **Sistema Operativo**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo alla pagina e seleziona il tuo sistema operativo.

   .. note::

      * Per il sistema **Ubuntu**, clicca su **Altri sistemi operativi generici** -> **Ubuntu**, e seleziona **Ubuntu Desktop 24.04 LTS (64 bit)** o **Ubuntu Server 24.04 LTS (64 bit)**.
      * Per i sistemi **Kali Linux**, **Home Assistant** e **Homebridge**, clicca su **Altri sistemi operativi specifici** e seleziona il sistema corrispondente.

   .. image:: img/os_other_os.png
      :width: 90%

#. Nella sezione **Archiviazione**, seleziona il dispositivo di archiviazione appropriato per l'installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      

#. Clicca su **NEXT**.

   .. note::

      * Per i sistemi che non possono essere configurati in anticipo, dopo aver cliccato su **NEXT**, ti verrà chiesto se vuoi salvare i dati all'interno del dispositivo. Se hai confermato di aver fatto un backup, seleziona **Yes**.

      * Per i sistemi in cui il nome host, il WiFi e l'abilitazione SSH possono essere configurati in anticipo, apparirà una finestra di dialogo che chiederà se applicare le impostazioni personalizzate del sistema operativo. Puoi scegliere **Yes**, **No** o tornare indietro per modificare ulteriormente.

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Definisci un **hostname** per il tuo Raspberry Pi. L'hostname è l'identificativo di rete del tuo Raspberry Pi. Puoi accedere al tuo Pi utilizzando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png  

   * Crea un **Nome Utente** e una **Password** per l'account amministratore del Raspberry Pi. Stabilire un nome utente e una password unici è fondamentale per proteggere il tuo Raspberry Pi, che non ha una password predefinita.

     .. image:: img/os_set_username.png
         
   * Configura la LAN wireless fornendo l'**SSID** e la **Password** della tua rete.

     .. note::

       Imposta il ``Paese della LAN wireless`` sul codice ISO/IEC alpha2 corrispondente alla tua posizione.

     .. image:: img/os_set_wifi.png
         
   * Per connetterti da remoto al tuo Raspberry Pi, abilita SSH nella scheda Servizi.

     * Per l'autenticazione con **password**, utilizza il nome utente e la password della scheda Generale.
     * Per l'autenticazione con chiave pubblica, scegli "Consenti solo l'autenticazione con chiave pubblica". Se possiedi una chiave RSA, verrà utilizzata. In caso contrario, clicca su "Esegui SSH-keygen" per generare una nuova coppia di chiavi.

     .. image:: img/os_enable_ssh.png
         
   * Il menu **Opzioni** ti consente di configurare il comportamento di Imager durante la scrittura, inclusa la riproduzione di suoni al termine, l'espulsione del supporto al termine e l'attivazione della telemetria.

     .. image:: img/os_options.png
           
#. Quando hai terminato di inserire le impostazioni di personalizzazione del sistema operativo, clicca su **Salva** per salvare la tua personalizzazione. Poi clicca su **Yes** per applicarle durante la scrittura dell'immagine.

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. Se la scheda SD contiene dati esistenti, assicurati di eseguire un backup per evitare la perdita di dati. Procedi cliccando su **Yes** se non è necessario alcun backup.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Quando visualizzi il popup "Scrittura completata", l'immagine è stata completamente scritta e verificata. Ora sei pronto per avviare un Raspberry Pi dalla scheda Micro SD!

