.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche grazie al supporto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e iniziative promozionali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

.. _copy_sd_to_nvme_rpi_mini:

Copia del sistema operativo da Micro SD a SSD NVMe
==================================================================

Se possiedi un SSD NVMe ma non hai un adattatore per collegarlo al computer, puoi seguire una terza opzione: installa prima il sistema sulla scheda Micro SD. Una volta avviato correttamente il Pironman 5 Mini, potrai trasferire il sistema dalla Micro SD all’SSD NVMe.

* Per prima cosa, devi :ref:`install_os_sd_rpi_mini`.
* Poi avvia e accedi al tuo Raspberry Pi. Se non sai come accedere, visita il sito ufficiale Raspberry Pi: |link_rpi_get_start|.

Completa questi passaggi prima di procedere con le istruzioni seguenti.


1. Abilitare il PCIe
-------------------------

Per impostazione predefinita, il connettore PCIe non è attivo.

* Per abilitarlo, apri il file ``/boot/firmware/config.txt``.

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* Aggiungi la riga seguente al file:

  .. code-block:: shell

    # Abilita il connettore PCIe esterno
    dtparam=pciex1

* Esiste un alias più facile da ricordare per ``pciex1``, quindi in alternativa puoi aggiungere ``dtparam=nvme`` al file ``/boot/firmware/config.txt``.

  .. code-block:: shell

    dtparam=nvme

* La connessione è certificata per velocità Gen 2.0 (5 GT/sec), ma puoi forzarla a Gen 3.0 (10 GT/sec) aggiungendo le seguenti righe al file ``/boot/firmware/config.txt``.

  .. code-block:: shell

    # Forza velocità Gen 3.0
    dtparam=pciex1_gen=3

  .. warning::

    Il Raspberry Pi 5 non è certificato per le velocità Gen 3.0, e l’uso di dispositivi PCIe a questa velocità può causare instabilità.

* Premi ``Ctrl + X``, poi ``Y`` e ``Enter`` per salvare le modifiche.


2. Installare il sistema operativo sull’SSD
----------------------------------------------

Ci sono due metodi per installare il sistema operativo su SSD:

**Copia del sistema dalla Micro SD all’SSD**

#. Collega un monitor o accedi al desktop del Raspberry Pi tramite VNC Viewer. Quindi clicca su **logo Raspberry Pi** -> **Accessori** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png


#. Assicurati di selezionare correttamente i dispositivi **Copy From** e **Copy To**. Presta attenzione a non invertirli.

   .. image:: img/ssd_copy_from.png

#. Seleziona "NEW Partition UUIDs" per evitare conflitti di montaggio o problemi di avvio.

   .. image:: img/ssd_copy_uuid.png

#. Dopo la selezione, clicca su **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Ti verrà chiesto conferma per la cancellazione del contenuto sull’SSD. Effettua un backup prima di procedere.

   .. image:: img/ssd_copy_erase.png

#. Attendi il completamento del processo.

**Installazione del sistema con Raspberry Pi Imager**

Se la Micro SD utilizza una versione desktop, puoi utilizzare un tool come Raspberry Pi Imager per scrivere l’immagine sull’SSD.

#. Collega un monitor o accedi al desktop via VNC Viewer. Quindi clicca su **logo Raspberry Pi** -> **Accessori** -> **Imager**.

   .. image:: img/ssd_imager.png


#. All’interno di |link_rpi_imager| seleziona **Raspberry Pi Device**, scegli il modello **Raspberry Pi 5**.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Seleziona **Operating System** e scegli la versione consigliata.

   .. image:: img/ssd_os.png
      :width: 90%

#. In **Storage**, seleziona l’SSD NVMe rilevato.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Clicca su **NEXT**, poi su **EDIT SETTINGS** per personalizzare le impostazioni del sistema operativo.

   .. note::

      Se disponi di un monitor per il Raspberry Pi, puoi saltare i passaggi successivi e cliccare 'Yes' per avviare l'installazione.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Definisci un **hostname** per il tuo Raspberry Pi.

   .. note::

      L’hostname identifica il dispositivo in rete. Puoi accedervi tramite ``<hostname>.local`` o ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png


#. Crea un **Username** e una **Password** per l’account amministratore del Raspberry Pi.

   .. note::

      È fondamentale creare credenziali sicure, poiché il sistema non ha password predefinita.

   .. image:: img/os_set_username.png


#. Configura la rete Wi-Fi inserendo **SSID** e **Password**.

   .. note::

     Imposta il ``Wireless LAN country`` con il codice a due lettere `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua posizione geografica.

   .. image:: img/os_set_wifi.png

#. Per connetterti da remoto, **enable SSH** nella scheda **Services**.

   * Per **l’autenticazione tramite password**, usa le credenziali definite in precedenza.
   * Per autenticazione con chiave pubblica, scegli "Allow public-key authentication only" e genera una chiave se necessario.

   .. image:: img/os_enable_ssh.png



#. Nel menu **Options**, puoi configurare il comportamento di Imager, ad esempio l’espulsione del supporto e la notifica sonora.

   .. image:: img/os_options.png

#. Dopo aver completato la personalizzazione, clicca su **Save**, poi su **Yes** per applicarla durante la scrittura.

   .. image:: img/os_click_yes.png
      :width: 90%

#. Se l’SSD contiene dati, esegui un backup. Se non necessario, clicca su **Yes** per continuare.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Alla comparsa del messaggio "Write Successful", l’immagine è stata scritta e verificata. Ora puoi avviare il Raspberry Pi da SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _configure_boot_ssd_mini:

3. Configurare l’avvio da SSD
---------------------------------------

In questa sezione configurerai il Raspberry Pi per l’avvio diretto da SSD NVMe, ottenendo tempi di avvio più rapidi e migliori prestazioni.

#. Apri il terminale sul tuo Raspberry Pi e accedi al tool di configurazione:

   .. code-block:: shell

      sudo raspi-config

#. Nel menu ``raspi-config``, seleziona **Advanced Options** e premi ``Enter``.

   .. image:: img/nvme_open_config.png

#. Seleziona **Boot Order** per definire l’ordine dei dispositivi da cui effettuare l’avvio.

   .. image:: img/nvme_boot_order.png

#. Scegli **NVMe/USB boot** per dare priorità all’avvio da SSD NVMe o USB.

   .. image:: img/nvme_boot_nvme.png

#. Dopo la selezione, premi **Finish** oppure usa **Escape** per uscire.

   .. image:: img/nvme_boot_ok.png

#. Per applicare le nuove impostazioni di avvio, riavvia il tuo Raspberry Pi eseguendo il comando ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

Dopo il riavvio, il Raspberry Pi tenterà di avviarsi dal tuo SSD NVMe, garantendo prestazioni più elevate e una maggiore affidabilità.
