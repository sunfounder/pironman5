.. note::

    Ciao, benvenuto nella Community SunFounder dedicata agli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni stagionali e giveaway.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _install_os_sd_rpi_mini:

Installazione del Sistema Operativo su una Scheda Micro SD
===============================================================
.. If you are using a Micro SD card, you can follow the tutorial below to install the system onto your Micro SD card.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Componenti Necessari**

* Un computer
* Una scheda Micro SD e un lettore

**Procedura**

#. Inserisci la scheda SD nel computer o portatile tramite un lettore.

#. All'interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a discesa.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Seleziona **Operating System** e scegli la versione raccomandata del sistema operativo.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Clicca su **Choose Storage** e seleziona il dispositivo di archiviazione corretto per l’installazione.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Clicca su **NEXT** e poi su **EDIT SETTINGS** per personalizzare le impostazioni del sistema operativo.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Definisci un **hostname** per il tuo Raspberry Pi. Questo sarà l’identificativo della rete. Puoi accedere al tuo Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png


   * Crea un **Username** e una **Password** per l’account amministratore del Raspberry Pi. È fondamentale per la sicurezza, dato che non c’è una password predefinita.

     .. image:: img/os_set_username.png

   * Configura la rete wireless inserendo **SSID** e **Password** del tuo Wi-Fi.

     .. note::

       Imposta il ``Wireless LAN country`` utilizzando il codice a due lettere `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua nazione.

     .. image:: img/os_set_wifi.png


   * Per connetterti da remoto al tuo Raspberry Pi, abilita SSH nella scheda Servizi.

     * Per **l’autenticazione con password**, utilizza le credenziali dalla scheda Generale.
     * Per l’**autenticazione con chiave pubblica**, seleziona "Allow public-key authentication only". Se disponi di una chiave RSA, verrà utilizzata; altrimenti clicca su "Run SSH-keygen" per generare una nuova coppia di chiavi.

     .. image:: img/os_enable_ssh.png

   * Il menu **Options** consente di configurare il comportamento dell’Imager durante la scrittura, incluso il suono a fine processo, l’espulsione del supporto e la telemetria.

     .. image:: img/os_options.png

#. Dopo aver completato la personalizzazione del sistema operativo, clicca su **Save** per salvare le impostazioni, poi su **Yes** per applicarle durante la scrittura dell'immagine.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Se la scheda SD contiene già dei dati, esegui un backup per evitarne la perdita. Prosegui cliccando su **Yes** se non è necessario il backup.

   .. image:: img/os_continue.png
      :width: 90%


#. Quando appare il messaggio "Write Successful", significa che l'immagine è stata scritta e verificata con successo. Ora sei pronto per avviare il tuo Raspberry Pi dalla scheda Micro SD!

   .. image:: img/os_finish.png
      :width: 90%
