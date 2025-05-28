.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto del nostro team e della community.
    - **Learn & Share**: Scambia consigli e tutorial per potenziare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato ai nuovi annunci di prodotto e alle anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway dedicati.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _max_install_to_nvme_home_bridge:

Installazione del sistema operativo su SSD NVMe
===========================================================

Se utilizzi un SSD NVMe e possiedi un adattatore per collegarlo al computer, puoi seguire il tutorial seguente per un’installazione rapida.

**Componenti richiesti**

* Un computer personale
* Un SSD NVMe
* Un adattatore NVMe-USB
* Una scheda Micro SD e un lettore

.. _max_update_bootloader:

1. Aggiornare il Bootloader
----------------------------------

Per prima cosa è necessario aggiornare il bootloader del Raspberry Pi 5 in modo che si avvii da NVMe, prima di tentare con USB e poi con la scheda SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    In questa fase, si consiglia di utilizzare una scheda Micro SD di riserva. Scrivi il bootloader su questa scheda e inseriscila immediatamente nel Raspberry Pi per abilitare l’avvio da un dispositivo NVMe.

    In alternativa, puoi scrivere il bootloader direttamente sul tuo SSD NVMe, inserirlo nel Raspberry Pi per aggiornare la modalità di avvio, poi collegare l’SSD al computer per installare il sistema operativo. Una volta completata l’installazione, reinseriscilo nel Raspberry Pi.

#. Inserisci la scheda Micro SD o l’SSD NVMe nel tuo computer tramite un lettore.

#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Nella scheda **Operating System**, scorri verso il basso e seleziona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Seleziona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Seleziona **NVMe/USB Boot** per abilitare l’avvio da NVMe, prima che da USB e poi da SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Nella sezione **Storage**, seleziona il dispositivo di destinazione corretto.

   .. note::

      Assicurati di scegliere il dispositivo giusto. Per evitare errori, scollega eventuali altri dispositivi di archiviazione.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ora puoi cliccare su **NEXT**. Se il dispositivo contiene dati, effettua un backup per evitarne la perdita. In caso contrario, clicca su **Yes** per proseguire.

   .. image:: img/os_continue.png
      :width: 90%


#. Apparirà una notifica che conferma che **NVMe/USB Boot** è stato scritto correttamente sul dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Inserisci ora la scheda Micro SD o l’SSD NVMe nel Raspberry Pi. Dopo aver alimentato il Raspberry Pi con un adattatore Type C, il bootloader verrà scritto nella EEPROM.

.. note::

    A questo punto, il Raspberry Pi si avvierà da NVMe prima di tentare con USB e poi con la SD Card.
    
    Spegni il Raspberry Pi e rimuovi la Micro SD o l’SSD NVMe.


2. Installare il sistema operativo su SSD NVMe
-----------------------------------------------------

Ora puoi procedere con l’installazione del sistema operativo sull’SSD NVMe.

**Passaggi**

#. Inserisci la tua scheda SD nel computer tramite lettore.

#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Clicca sulla scheda **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri in fondo alla pagina e seleziona il sistema operativo desiderato.

   .. note::

      * Per **Ubuntu**, clicca su **Other general-purpose OS** -> **Ubuntu**, e seleziona **Ubuntu Desktop 24.04 LTS (64 bit)** oppure **Ubuntu Server 24.04 LTS (64 bit)**.
      * Per **Kali Linux**, **Home Assistant** e **Homebridge**, clicca su **Other specific-purpose OS** e seleziona il sistema corrispondente.

   .. image:: img/os_other_os.png
      :width: 90%

#. Nella sezione **Storage**, seleziona il dispositivo corretto per l’installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Clicca su **NEXT**.

   .. note::

      * Per i sistemi che non consentono la configurazione anticipata, dopo **NEXT** ti verrà chiesto se desideri cancellare i dati. Se hai già eseguito un backup, seleziona **Yes**.

      * Per i sistemi che supportano impostazioni personalizzate come Hostname, WiFi e abilitazione SSH, apparirà una finestra che chiede se applicare le personalizzazioni. Puoi scegliere **Yes**, **No** o tornare indietro per modificarle.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Imposta un **hostname** per il tuo Raspberry Pi. L’hostname è il nome con cui il dispositivo sarà visibile in rete. Puoi accedervi tramite ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Username** e una **Password** per l’account amministratore. L’uso di credenziali univoche protegge il dispositivo, che non ha una password predefinita.

     .. image:: img/os_set_username.png

   * Configura la rete Wi-Fi inserendo **SSID** e **Password** del tuo Wi-Fi.

     .. note::

       Imposta il ``Wireless LAN country`` utilizzando il codice a due lettere `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua posizione geografica.

     .. image:: img/os_set_wifi.png
         
   * Per connetterti da remoto al tuo Raspberry Pi, abilita SSH nella scheda Servizi.

     * Per l’autenticazione tramite **password**, utilizza il nome utente e la password definiti nella scheda Generale.
     * Per l’autenticazione con chiave pubblica, seleziona "Allow public-key authentication only". Se possiedi una chiave RSA, verrà utilizzata. In caso contrario, clicca su "Run SSH-keygen" per generare una nuova coppia di chiavi.

     .. image:: img/os_enable_ssh.png

   * Il menu **Options** consente di configurare il comportamento dell’Imager durante la scrittura, ad esempio riprodurre un suono al termine, espellere il supporto automaticamente e abilitare la telemetria.

     .. image:: img/os_options.png



#. Una volta completata la personalizzazione del sistema operativo, clicca su **Save** per salvare le impostazioni. Poi clicca su **Yes** per applicarle durante la scrittura dell’immagine.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Se l’SSD NVMe contiene già dei dati, assicurati di eseguire un backup per evitarne la perdita. In caso contrario, clicca su **Yes** per proseguire.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Quando visualizzi il messaggio "Write Successful", significa che l’immagine è stata scritta e verificata correttamente. Ora sei pronto per avviare il tuo Raspberry Pi dall’SSD NVMe!
