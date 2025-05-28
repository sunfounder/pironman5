.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e difficoltà tecniche con l’aiuto della nostra community e del nostro team.
    - **Learn & Share**: Scambia consigli e tutorial per migliorare le tue capacità.
    - **Exclusive Previews**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni stagionali e giveaway esclusivi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _max_install_to_sd_home_bridge:

Installazione del sistema operativo su scheda Micro SD
==============================================================

Se stai utilizzando una scheda Micro SD, segui il tutorial qui sotto per installare il sistema operativo sulla scheda.


**Componenti necessari**

* Un computer personale
* Una scheda Micro SD e un lettore

**Procedura**

#. Inserisci la scheda SD nel tuo computer o laptop utilizzando un lettore.

#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Clicca sulla scheda **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo alla pagina e seleziona il sistema operativo desiderato.

   .. note::

      * Per il sistema **Ubuntu**, clicca su **Other general-purpose OS** -> **Ubuntu**, e seleziona **Ubuntu Desktop 24.04 LTS (64 bit)** oppure **Ubuntu Server 24.04 LTS (64 bit)**.
      * Per **Kali Linux**, **Home Assistant** e **Homebridge**, clicca su **Other specific-purpose OS** e seleziona il sistema corrispondente.

   .. image:: img/os_other_os.png
      :width: 90%

#. Nella sezione **Storage**, seleziona il dispositivo di archiviazione corretto per l’installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Clicca su **NEXT**.

   .. note::

      * Per i sistemi che non possono essere configurati in anticipo, dopo aver cliccato su **NEXT**, ti verrà chiesto se desideri salvare i dati presenti nel dispositivo. Se hai già eseguito un backup, seleziona **Yes**.

      * Per i sistemi che permettono di configurare Hostname, Wi-Fi e SSH in anticipo, apparirà una finestra che chiederà se vuoi applicare le impostazioni personalizzate del sistema operativo. Puoi scegliere **Yes**, **No** o tornare indietro per modificarle.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Definisci un **hostname** per il tuo Raspberry Pi. L'hostname è l’identificatore del dispositivo nella rete. Puoi accedere al Raspberry Pi tramite ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png  

   * Crea uno **Username** e una **Password** per l’account amministratore del Raspberry Pi. Impostare credenziali univoche è fondamentale per la sicurezza del dispositivo, che non dispone di una password predefinita.

     .. image:: img/os_set_username.png

   * Configura la rete Wi-Fi inserendo l’**SSID** e la **Password** della tua rete.

     .. note::

       Imposta il ``Wireless LAN country`` con il codice a due lettere `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua località.

     .. image:: img/os_set_wifi.png

   * Per connetterti da remoto al tuo Raspberry Pi, abilita SSH nella scheda Servizi.

     * Per l’autenticazione con **password**, utilizza le credenziali definite nella scheda Generale.
     * Per l’autenticazione con chiave pubblica, seleziona "Allow public-key authentication only". Se disponi di una chiave RSA, verrà utilizzata. In caso contrario, clicca su "Run SSH-keygen" per generare una nuova coppia di chiavi.

     .. image:: img/os_enable_ssh.png

   * Il menu **Options** ti consente di configurare il comportamento dell’Imager durante la scrittura, come la riproduzione di un suono al termine, l’espulsione automatica del supporto e l’abilitazione della telemetria.

     .. image:: img/os_options.png

#. Quando hai completato la configurazione del sistema operativo, clicca su **Save** per salvare le personalizzazioni. Poi clicca su **Yes** per applicarle durante la scrittura dell’immagine.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Se la scheda SD contiene dati esistenti, esegui un backup per evitare la perdita di informazioni. Se non è necessario, clicca su **Yes** per proseguire.

   .. image:: img/os_continue.png
      :width: 90%


#. Quando visualizzi il messaggio "Write Successful", l’immagine è stata scritta e verificata con successo. Ora sei pronto per avviare il Raspberry Pi dalla scheda Micro SD!
