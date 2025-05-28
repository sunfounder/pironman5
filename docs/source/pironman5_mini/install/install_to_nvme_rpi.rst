.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ricevi in anteprima annunci e anticipazioni sui nuovi prodotti.
    - **Sconti esclusivi**: Approfitta di offerte riservate sui nostri prodotti più recenti.
    - **Promozioni e giveaway festivi**: Partecipa a concorsi e iniziative speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

.. _install_to_nvme_rpi_mini:

Installazione del sistema operativo su SSD NVMe
======================================================
Se stai utilizzando un SSD NVMe e hai un adattatore per collegarlo al computer per l’installazione del sistema, puoi seguire il tutorial seguente per un’installazione rapida.

**Componenti necessari**

* Un computer personale
* Un SSD NVMe
* Un adattatore da NVMe a USB
* Scheda Micro SD e lettore

.. _update_bootloader_mini:

1. Aggiornare il Bootloader
--------------------------------

Per prima cosa, devi aggiornare il bootloader del Raspberry Pi 5 per avviare il sistema da NVMe prima di tentare USB e poi SD Card.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    In questo passaggio, è consigliato utilizzare una scheda Micro SD di riserva. Scrivi prima il bootloader su questa scheda e poi inseriscila subito nel Raspberry Pi per abilitare l’avvio da un dispositivo NVMe.
    
    In alternativa, puoi scrivere il bootloader direttamente sul tuo dispositivo NVMe, poi inserirlo nel Raspberry Pi per modificarne il metodo di avvio. Successivamente collega l’SSD NVMe al computer per installare il sistema operativo e, una volta completata l’installazione, reinseriscilo nel Raspberry Pi.

#. Inserisci la scheda Micro SD o l’SSD NVMe nel tuo computer o laptop tramite lettore.

#. All’interno di |link_rpi_imager| clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Nella scheda **Operating System**, scorri e seleziona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Seleziona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Seleziona **NVMe/USB Boot** per abilitare l’avvio da NVMe prima di USB e SD Card.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Nella sezione **Storage**, seleziona il dispositivo corretto per l’installazione.

   .. note::

      Assicurati di selezionare il dispositivo giusto. Per evitare confusione, scollega eventuali altri dispositivi di archiviazione se presenti.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ora puoi cliccare su **NEXT**. Se il dispositivo contiene dati, esegui un backup per evitarne la perdita. Procedi cliccando su **Yes** se non è necessario il backup.

   .. image:: img/os_continue.png
      :width: 90%


#. Riceverai una conferma che **NVMe/USB Boot** è stato scritto correttamente sul tuo dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Ora inserisci la scheda Micro SD o l’SSD NVMe nel Raspberry Pi. Dopo averlo alimentato con un adattatore Type C, il bootloader verrà scritto nella EEPROM del Raspberry Pi.

.. note::

    Da questo momento, il Raspberry Pi tenterà l’avvio da NVMe prima di USB e poi da SD Card. 
    
    Spegni il Raspberry Pi e rimuovi la scheda Micro SD o l’SSD NVMe.


2. Installare il sistema operativo su SSD NVMe
-----------------------------------------------------

Ora puoi installare il sistema operativo sul tuo SSD NVMe.


#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Seleziona **Operating System** e scegli la versione consigliata del sistema operativo.

   .. image:: img/os_choose_os.png
      :width: 90%


#. Nella sezione **Storage**, seleziona il dispositivo corretto per l’installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Clicca su **NEXT** e poi su **EDIT SETTINGS** per personalizzare le impostazioni del sistema operativo.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Definisci un **hostname** per il tuo Raspberry Pi. Questo nome identifica il tuo Raspberry Pi nella rete locale. Puoi accedere al tuo Pi con ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Username** e una **Password** per l’account amministratore del Raspberry Pi. La scelta di credenziali univoche è fondamentale per la sicurezza del dispositivo.

     .. image:: img/os_set_username.png

   * Configura la rete wireless inserendo **SSID** e **Password** della tua rete.

     .. note::

       Imposta il ``Wireless LAN country`` con il codice a due lettere secondo lo standard `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ relativo alla tua nazione.

     .. image:: img/os_set_wifi.png

   * Per accedere da remoto al tuo Raspberry Pi, abilita SSH nella scheda Services.

     * Per **l’autenticazione con password**, usa le credenziali definite nella scheda General.
     * Per autenticazione con chiave pubblica, scegli “Allow public-key authentication only”. Se non hai una chiave RSA, clicca su “Run SSH-keygen” per generarne una nuova.

     .. image:: img/os_enable_ssh.png

   * Il menu **Options** consente di configurare il comportamento di Imager durante la scrittura, come riproduzione suono a completamento, espulsione automatica e telemetria.

     .. image:: img/os_options.png

#. Una volta terminate le personalizzazioni, clicca su **Save** per salvare le impostazioni. Poi clicca su **Yes** per applicarle durante la scrittura dell’immagine.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Se l’SSD NVMe contiene dati, assicurati di eseguire un backup. Se non necessario, clicca su **Yes** per continuare.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Quando visualizzi il messaggio "Write Successful", l’immagine è stata scritta e verificata con successo. Ora sei pronto ad avviare il tuo Raspberry Pi da SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%