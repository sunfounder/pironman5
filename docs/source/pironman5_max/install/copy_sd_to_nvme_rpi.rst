.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della community e del nostro team.
    - **Impara e condividi**: Condividi suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotto e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra nella community oggi stesso!

.. _max_copy_sd_to_nvme_rpi:

Copiare il Sistema Operativo da Micro SD a SSD NVMe
==================================================================

Se disponi di un SSD NVMe ma non di un adattatore per collegarlo al computer, puoi adottare una terza soluzione: installare inizialmente il sistema sulla scheda Micro SD. Dopo l’avvio corretto del Pironman 5 MAX, puoi trasferire il sistema dalla Micro SD all’SSD NVMe.

* Per prima cosa, devi seguire i passaggi in :ref:`max_install_os_sd_rpi`.
* Poi avvia e accedi al tuo Raspberry Pi. Se non sai come fare, visita il sito ufficiale Raspberry Pi: |link_rpi_get_start|.

Completa i passaggi sopra prima di procedere con le istruzioni seguenti.


1. Abilitare il PCIe
------------------------

Per impostazione predefinita, il connettore PCIe non è abilitato.

* Per abilitarlo, apri il file ``/boot/firmware/config.txt``:

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Aggiungi la seguente riga:

  .. code-block:: shell
  
    # Abilita il connettore PCIe esterno.
    dtparam=pciex1
  
* È disponibile un alias più intuitivo per ``pciex1``, quindi puoi anche usare:

  .. code-block:: shell
  
    dtparam=nvme

.. * La connessione è certificata per la velocità Gen 2.0 (5 GT/sec), ma puoi forzarla a Gen 3.0 (10 GT/sec) aggiungendo:

..   .. code-block:: shell
  
..     # Forza la velocità Gen 3.0
..     dtparam=pciex1_gen=3

..   .. warning::

..     Il Raspberry Pi 5 non è certificato per la velocità Gen 3.0, quindi potrebbero verificarsi instabilità con alcuni dispositivi PCIe.

* Disabilita il ritardo di avvio PCIe per permettere il rilevamento dell’SSD NVMe:

  .. code-block:: shell

      dtparam=pciex1_no_10s=on


* Premi ``Ctrl + X``, poi ``Y`` e ``Invio`` per salvare.


**BOOT_ORDER**

Se hai installato due SSD NVMe e vuoi scegliere da quale avviare, modifica ``ROOT=PARTUUID=xxxxxxxxx`` nel file ``/boot/firmware/cmdline.txt`` con l’UUID del disco di avvio. Puoi trovare l’UUID con:

.. code-block:: shell

   ls /dev/disk/by-id/


2. Installare il Sistema Operativo sull’SSD 
----------------------------------------------------

Esistono due modalità per installare un sistema operativo su un SSD:

**Copia del Sistema dalla Scheda Micro SD all’SSD**

#. Collega un display oppure accedi al desktop del Raspberry Pi tramite VNC Viewer. Poi clicca su **Logo Raspberry Pi** -> **Accessori** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png
      

#. Assicurati di selezionare correttamente i dispositivi **Copia Da** e **Copia A**. Presta attenzione a non invertirli.

   .. image:: img/ssd_copy_from.png
      
#. Ricorda di selezionare "NEW Partition UUIDs" per permettere al sistema di distinguere correttamente i dispositivi ed evitare conflitti di montaggio o errori di avvio.

   .. image:: img/ssd_copy_uuid.png
    
#. Dopo la selezione, clicca su **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Apparirà un messaggio che avvisa che il contenuto dell’SSD verrà cancellato. Assicurati di eseguire un backup prima di cliccare su Sì.

   .. image:: img/ssd_copy_erase.png

#. Attendi il termine della procedura di copia.


**Installazione del Sistema tramite Raspberry Pi Imager**

Se la tua scheda Micro SD ha già installata una versione desktop del sistema, puoi utilizzare un tool di imaging (come Raspberry Pi Imager) per scrivere il sistema sull’SSD. In questo esempio si usa Raspberry Pi OS Bookworm, ma per altri sistemi potrebbe essere necessario installare il tool.

#. Collega un display o accedi al desktop tramite VNC Viewer. Poi clicca su **Logo Raspberry Pi** -> **Accessori** -> **Imager**.

   .. image:: img/ssd_imager.png


#. All’interno di |link_rpi_imager|, clicca su **Dispositivo Raspberry Pi** e seleziona **Raspberry Pi 5** dal menu a tendina.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Seleziona **Sistema Operativo** e scegli la versione consigliata.

   .. image:: img/ssd_os.png
      :width: 90%
    
#. Nella sezione **Storage**, seleziona il tuo SSD NVMe.

   .. image:: img/nvme_storage.png
      :width: 90%
    
#. Clicca su **NEXT** e poi su **EDIT SETTINGS** per personalizzare le impostazioni.

   .. note::

      Se disponi di un monitor per il Raspberry Pi, puoi saltare i passaggi successivi e cliccare su "Yes" per iniziare l’installazione. Potrai modificare le impostazioni in seguito.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Definisci un **hostname** per il tuo Raspberry Pi.

   .. note::

      L’hostname è l’identificativo di rete del Raspberry Pi. Puoi accedere al tuo dispositivo con ``<hostname>.local`` oppure ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png
      

#. Crea un **Nome utente** e una **Password** per l’account amministratore del Raspberry Pi.

   .. note::

      È fondamentale impostare un nome utente e una password sicuri, poiché il sistema non ha credenziali predefinite.

   .. image:: img/os_set_username.png
      

#. Configura la rete wireless inserendo l’**SSID** e la **Password** del tuo Wi-Fi.

   .. note::

      Imposta il valore ``Wireless LAN country`` secondo il codice a due lettere `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ del tuo paese.

   .. image:: img/os_set_wifi.png

#. Per collegarti in remoto al Raspberry Pi, **abilita SSH** nella scheda **Services**.

   * Per l'autenticazione con password, usa le credenziali definite nella scheda **General**.
   * Per autenticazione tramite chiave pubblica, seleziona "Allow public-key authentication only". Se hai una chiave RSA, verrà usata; altrimenti clicca su "Run SSH-keygen" per generare una nuova coppia di chiavi.

   .. image:: img/os_enable_ssh.png



#. Il menu **Options** consente di impostare comportamenti del tool, come suono a scrittura completata, espulsione automatica e invio dati di telemetria.

   .. image:: img/os_options.png
    
#. Quando hai finito di personalizzare il sistema operativo, clicca su **Save**, poi su **Yes** per applicare le modifiche.

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. Se l’SSD NVMe contiene dati, esegui un backup per evitare perdite. Se non necessario, clicca su **Yes** per procedere.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Quando compare il messaggio "Write Successful", il sistema è stato scritto e verificato correttamente. Ora sei pronto per avviare il Raspberry Pi dall’SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _max_configure_boot_ssd:

3. Configurare l’Avvio da SSD
---------------------------------------

In questa sezione configureremo il Raspberry Pi per eseguire l’avvio direttamente da un SSD NVMe, migliorando tempi di avvio e prestazioni rispetto alla scheda SD.

#. Apri un terminale sul Raspberry Pi ed esegui:

   .. code-block:: shell

      sudo raspi-config

#. All’interno del menu ``raspi-config``, usa le frecce per navigare e seleziona **Advanced Options**. Premi ``Enter``.

   .. image:: img/nvme_open_config.png

#. In **Advanced Options**, scegli **Boot Order** per impostare l’ordine dei dispositivi di avvio.

   .. image:: img/nvme_boot_order.png

#. Seleziona **NVMe/USB boot** per dare priorità a SSD collegati via USB o NVMe.

   .. image:: img/nvme_boot_nvme.png

#. Dopo aver scelto l’ordine di avvio, premi **Finish** per uscire, oppure usa **Esc**.

   .. image:: img/nvme_boot_ok.png

#. Per applicare le nuove impostazioni, riavvia il Raspberry Pi con: ``sudo reboot``

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

Dopo il riavvio, il Raspberry Pi tenterà di avviarsi dal tuo SSD NVMe, garantendo prestazioni superiori e maggiore durata del sistema.


