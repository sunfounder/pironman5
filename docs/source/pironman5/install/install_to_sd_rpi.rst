.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_os_sd_rpi:

Installazione del Sistema Operativo su una Micro SD Card
=============================================================
Se stai utilizzando una scheda Micro SD, puoi seguire il tutorial qui sotto per installare il sistema sulla tua scheda Micro SD.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Componenti necessari**

* Un computer personale
* Una scheda Micro SD e un lettore

**Passaggi**

#. Inserisci la tua scheda SD nel computer o nel laptop utilizzando un lettore.

#. All'interno del |link_rpi_imager|, clicca su **Dispositivo Raspberry Pi** e seleziona il modello **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Seleziona **Sistema Operativo** e scegli la versione raccomandata del sistema operativo.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Clicca su **Scegli Archiviazione** e seleziona il dispositivo di archiviazione appropriato per l'installazione.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Clicca su **NEXT** e poi su **EDIT SETTINGS** per personalizzare le impostazioni del tuo sistema operativo. 

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

   .. image:: img/os_finish.png
      :width: 90%
