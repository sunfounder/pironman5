.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e difficoltà tecniche grazie al supporto del nostro team e della nostra community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per sviluppare ulteriormente le tue abilità.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e ad anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway riservati alla community.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _max_install_os_sd_rpi:

Installazione del sistema operativo su scheda Micro SD
============================================================
Se stai utilizzando una scheda Micro SD, puoi seguire il tutorial qui sotto per installare il sistema operativo.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Componenti necessari**

* Un computer personale
* Una scheda Micro SD e un lettore

**Procedura**

#. Inserisci la scheda SD nel computer o nel laptop tramite un lettore.

#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Seleziona **Operating System** e scegli la versione consigliata del sistema operativo.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Clicca su **Choose Storage** e seleziona il dispositivo di archiviazione corretto per l’installazione.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Clicca su **NEXT** e poi su **EDIT SETTINGS** per personalizzare la configurazione del sistema operativo.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Definisci un **hostname** per il tuo Raspberry Pi. L'hostname identifica il dispositivo all'interno della rete. Puoi accedere al tuo Raspberry Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png


   * Crea uno **Username** e una **Password** per l’account amministratore. L’uso di credenziali univoche è fondamentale per proteggere il Raspberry Pi, che non ha una password predefinita.

     .. image:: img/os_set_username.png

   * Configura la rete Wi-Fi inserendo **SSID** e **Password** della tua connessione.

     .. note::

       Imposta il valore di ``Wireless LAN country`` utilizzando il codice a due lettere `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua area geografica.

     .. image:: img/os_set_wifi.png


   * Per accedere al Raspberry Pi da remoto, abilita SSH nella scheda Servizi.

     * Per l’autenticazione tramite **password**, utilizza le credenziali impostate nella scheda Generale.
     * Per l’autenticazione con chiave pubblica, seleziona "Allow public-key authentication only". Se possiedi una chiave RSA, verrà utilizzata. Altrimenti, clicca su "Run SSH-keygen" per generarne una nuova.

     .. image:: img/os_enable_ssh.png

   * Il menu **Options** consente di configurare il comportamento di Imager durante la scrittura, ad esempio riprodurre un suono al termine, espellere il supporto o abilitare la telemetria.

     .. image:: img/os_options.png

#. Una volta completata la personalizzazione, clicca su **Save** per salvare le impostazioni, poi clicca su **Yes** per applicarle durante la scrittura dell'immagine.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Se la scheda SD contiene dati esistenti, assicurati di eseguire un backup per evitare perdite. In caso contrario, clicca su **Yes** per continuare.

   .. image:: img/os_continue.png
      :width: 90%


#. Quando compare il messaggio "Write Successful", significa che l'immagine è stata scritta e verificata correttamente. Ora sei pronto per avviare il Raspberry Pi dalla scheda Micro SD!

   .. image:: img/os_finish.png
      :width: 90%
