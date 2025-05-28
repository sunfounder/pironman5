.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto del nostro team e della community.
    - **Learn & Share**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni stagionali e giveaway esclusivi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _max_install_to_nvme_rpi:

Installazione del sistema operativo su SSD NVMe
========================================================
Se stai utilizzando un SSD NVMe e disponi di un adattatore per collegarlo al computer, puoi seguire questo tutorial per un’installazione rapida.

**Componenti necessari**

* Un computer personale
* Un SSD NVMe
* Un adattatore da NVMe a USB
* Una scheda Micro SD e un lettore

.. _max_update_bootloader:

1. Aggiornare il Bootloader
--------------------------------

Per prima cosa, è necessario aggiornare il bootloader del Raspberry Pi 5 per abilitare l’avvio da NVMe, seguito da USB e poi da scheda SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    In questa fase, si consiglia di utilizzare una scheda Micro SD di riserva. Scrivi il bootloader su questa scheda e inseriscila subito nel Raspberry Pi per abilitare l’avvio da dispositivo NVMe.

    In alternativa, puoi scrivere il bootloader direttamente sul tuo SSD NVMe, inserirlo nel Raspberry Pi per modificarne la modalità di avvio, collegarlo successivamente al computer per installare il sistema operativo e, infine, reinserirlo nel Raspberry Pi.

#. Inserisci la scheda Micro SD o l’SSD NVMe nel computer tramite lettore.

#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona **Raspberry Pi 5** dal menu a discesa.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Nella scheda **Operating System**, scorri verso il basso e seleziona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Seleziona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Seleziona **NVMe/USB Boot** per abilitare l’avvio del Raspberry Pi 5 da NVMe, poi USB e infine SD Card.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Nella sezione **Storage**, seleziona il dispositivo corretto per l’installazione.

   .. note::

      Verifica di selezionare il dispositivo giusto. Per evitare confusione, scollega eventuali dispositivi di archiviazione non necessari.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ora clicca su **NEXT**. Se il dispositivo contiene dati importanti, esegui un backup. In caso contrario, clicca su **Yes** per proseguire.

   .. image:: img/os_continue.png
      :width: 90%


#. A breve riceverai una notifica che conferma che la configurazione **NVMe/USB Boot** è stata scritta sul tuo dispositivo.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Inserisci ora la scheda Micro SD o l’SSD NVMe nel Raspberry Pi. Dopo averlo alimentato con un adattatore Type C, il bootloader verrà scritto nella EEPROM del dispositivo.

.. note::

    Dopo questo passaggio, il Raspberry Pi eseguirà l’avvio da NVMe, poi da USB e infine da SD Card.

    Spegni il Raspberry Pi e rimuovi la scheda Micro SD o l’SSD NVMe.


2. Installare il sistema operativo su SSD NVMe
-------------------------------------------------------

Ora puoi procedere all’installazione del sistema operativo sull’SSD NVMe.


#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Seleziona **Operating System** e scegli la versione del sistema operativo consigliata.

   .. image:: img/os_choose_os.png
      :width: 90%


#. Nella sezione **Storage**, seleziona il dispositivo di archiviazione corretto.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Clicca su **NEXT**, quindi su **EDIT SETTINGS** per personalizzare le impostazioni del sistema operativo.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Imposta un **hostname** per il Raspberry Pi. Si tratta dell’identificativo di rete del dispositivo. Puoi accedere al Pi usando ``<hostname>.local`` oppure ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Username** e una **Password** per l’account amministratore del Raspberry Pi. È importante impostare credenziali univoche poiché il sistema non prevede password predefinite.

     .. image:: img/os_set_username.png

   * Configura la rete wireless inserendo **SSID** e **Password** del tuo Wi-Fi.

     .. note::

       Imposta il ``Wireless LAN country`` utilizzando il codice ISO a due lettere `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua posizione.

     .. image:: img/os_set_wifi.png

   * Per connetterti da remoto al Raspberry Pi, abilita SSH nella scheda Servizi.

     * Per l’autenticazione tramite **password**, usa le credenziali dalla scheda Generale.
     * Per l’autenticazione tramite chiave pubblica, seleziona "Allow public-key authentication only". Se hai una chiave RSA, verrà utilizzata. Altrimenti clicca su "Run SSH-keygen" per generarne una nuova.

     .. image:: img/os_enable_ssh.png

   * Il menu **Options** consente di personalizzare il comportamento di Imager durante la scrittura, come la riproduzione di un suono al termine, l’espulsione del supporto e l’abilitazione della telemetria.

     .. image:: img/os_options.png

#. Una volta completata la personalizzazione, clicca su **Save** per salvare le impostazioni e poi su **Yes** per applicarle durante la scrittura dell’immagine.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Se l’SSD NVMe contiene dati, esegui un backup per evitare perdite. In caso contrario, clicca su **Yes** per procedere.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Quando visualizzi il messaggio "Write Successful", significa che l’immagine è stata scritta e verificata correttamente. Ora sei pronto per avviare il Raspberry Pi direttamente da SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%

