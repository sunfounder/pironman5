.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _copy_sd_to_nvme_rpi:

Copia del Sistema Operativo da Micro SD a NVMe SSD
==================================================================

Se hai un NVMe SSD ma non hai un adattatore per collegarlo al tuo computer, puoi optare per un terzo approccio: inizialmente installa il sistema sulla tua Micro SD. Dopo che il Pironman 5 si avvia correttamente, puoi trasferire il sistema dalla Micro SD al tuo NVMe SSD.

* Prima di tutto, devi :ref:`install_os_sd_rpi`.
* Successivamente, avvia e accedi al tuo Raspberry Pi. Se non sai come accedere, puoi visitare il sito ufficiale di Raspberry Pi: |link_rpi_get_start|.

Completa i passaggi sopra indicati prima di procedere con le istruzioni seguenti.


1. Abilitare PCIe
----------------------

Per impostazione predefinita, il connettore PCIe non è abilitato. 

* Per abilitarlo, devi aprire il file ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Quindi, aggiungi la seguente riga al file.

  .. code-block:: shell
  
    # Abilita il connettore PCIe esterno.
    dtparam=pciex1
  
* Esiste un alias più intuitivo per ``pciex1``, quindi puoi alternativamente aggiungere ``dtparam=nvme`` al file ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    dtparam=nvme

* La connessione è certificata per velocità Gen 2.0 (5 GT/sec), ma puoi forzarla a velocità Gen 3.0 (10 GT/sec) aggiungendo le seguenti righe al tuo ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    # Forza velocità Gen 3.0
    dtparam=pciex1_gen=3
  
  .. warning::
  
    Il Raspberry Pi 5 non è certificato per velocità Gen 3.0, e le connessioni ai dispositivi PCIe a queste velocità potrebbero risultare instabili.

* Premi ``Ctrl + X``, ``Y`` e ``Invio`` per salvare le modifiche.


2. Installa il Sistema Operativo sull'SSD
-------------------------------------------------

Ci sono due modi per installare un sistema operativo sull'SSD:

**Copia del Sistema dalla Micro SD all'SSD**

#. Collega un display o accedi al desktop del Raspberry Pi tramite VNC Viewer. Quindi fai clic su **Logo Raspberry Pi** -> **Accessori** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png
      
    
#. Assicurati di selezionare i dispositivi corretti in **Copia Da** e **Copia A**. Fai attenzione a non confonderli.

   .. image:: img/ssd_copy_from.png
      
#. Ricordati di selezionare "NUOVI UUID di Partizione" per garantire che il sistema possa distinguere correttamente i dispositivi, evitando conflitti di montaggio e problemi di avvio.

   .. image:: img/ssd_copy_uuid.png
    
#. Dopo aver effettuato la selezione, fai clic su **Avvia**.

   .. image:: img/ssd_copy_click_start.png

#. Verrà visualizzato un avviso che il contenuto dell'SSD verrà cancellato. Assicurati di eseguire il backup dei tuoi dati prima di fare clic su Sì.

   .. image:: img/ssd_copy_erase.png

#. Attendi un po', e la copia sarà completata.


**Installazione del Sistema con Raspberry Pi Imager**

Se la tua Micro SD contiene una versione desktop del sistema, puoi utilizzare uno strumento di imaging (come Raspberry Pi Imager) per masterizzare il sistema sull'SSD. Questo esempio utilizza Raspberry Pi OS Bookworm, ma altri sistemi potrebbero richiedere prima l'installazione dello strumento di imaging.

#. Collega un display o accedi al desktop del Raspberry Pi tramite VNC Viewer. Quindi fai clic su **Logo Raspberry Pi** -> **Accessori** -> **Imager**.

   .. image:: img/ssd_imager.png

      
#. All'interno del |link_rpi_imager|, fai clic su **Dispositivo Raspberry Pi** e seleziona il modello **Raspberry Pi 5** dall'elenco a discesa.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Seleziona **Sistema Operativo** e scegli la versione del sistema operativo consigliata.

   .. image:: img/ssd_os.png
      :width: 90%
    
#. Nell'opzione **Archiviazione**, seleziona il tuo SSD NVMe inserito.

   .. image:: img/nvme_storage.png
      :width: 90%
    
#. Fai clic su **NEXT** e poi su **MODIFICA IMPOSTAZIONI** per personalizzare le impostazioni del tuo sistema operativo.

   .. note::

      Se hai un monitor per il tuo Raspberry Pi, puoi saltare i prossimi passaggi e fare clic su 'Sì' per iniziare l'installazione. Modifica altre impostazioni successivamente sul monitor.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Definisci un **hostname** per il tuo Raspberry Pi.

   .. note::

      L'hostname è l'identificativo di rete del tuo Raspberry Pi. Puoi accedere al tuo Pi utilizzando ``<hostname>.local`` o ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png
      

#. Crea un **Nome utente** e una **Password** per l'account amministratore del Raspberry Pi.

   .. note::

      Stabilire un nome utente e una password unici è fondamentale per proteggere il tuo Raspberry Pi, che non ha una password predefinita.

   .. image:: img/os_set_username.png
      

#. Configura la rete LAN wireless fornendo **SSID** e **Password** della tua rete.

   .. note::

      Imposta il ``Paese LAN wireless`` sul codice `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ a due lettere corrispondente alla tua posizione.

   .. image:: img/os_set_wifi.png

#. Per connetterti in remoto al tuo Raspberry Pi, **abilita SSH** nella scheda **Servizi**.

   * Per l'autenticazione tramite password, utilizza il nome utente e la password dalla scheda **Generale**.
   * Per l'autenticazione tramite chiave pubblica, scegli "Consenti solo autenticazione con chiave pubblica". Se hai una chiave RSA, verrà utilizzata. In caso contrario, fai clic su "Esegui SSH-keygen" per generare una nuova coppia di chiavi.

   .. image:: img/os_enable_ssh.png

      

#. Il menu **Opzioni** ti consente di configurare il comportamento di Imager durante la scrittura, inclusa la riproduzione del suono al termine, l'espulsione del supporto una volta terminato e l'abilitazione della telemetria.

   .. image:: img/os_options.png
    
#. Quando hai terminato di inserire le impostazioni di personalizzazione del sistema operativo, fai clic su **Salva** per salvarle. Quindi, fai clic su **Sì** per applicarle durante la scrittura dell'immagine.

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. Se l'SSD NVMe contiene dati esistenti, assicurati di eseguirne il backup per evitare la perdita di dati. Procedi facendo clic su **Sì** se non è necessario un backup.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Quando vedi il popup "Scrittura Completata", la tua immagine è stata completamente scritta e verificata. Ora sei pronto per avviare un Raspberry Pi dall'SSD NVMe!

   .. image:: img/nvme_install_finish.png
      :width: 90%
      

.. _configure_boot_ssd:

3. Configurazione dell'avvio dalla SSD
---------------------------------------

In questa sezione configureremo il Raspberry Pi per avviarsi direttamente da un SSD NVMe, ottenendo tempi di avvio più rapidi e prestazioni migliori rispetto a una scheda SD. Segui attentamente questi passaggi:

#. Prima di tutto, apri un terminale sul tuo Raspberry Pi ed esegui il seguente comando per accedere all'interfaccia di configurazione:

   .. code-block:: shell

      sudo raspi-config

#. Nel menu ``raspi-config``, utilizza i tasti freccia per selezionare **Advanced Options**. Premi ``Enter`` per accedere alle impostazioni avanzate.

   .. image:: img/nvme_open_config.png

#. All'interno di **Advanced Options**, seleziona **Boot Order**. Questa impostazione consente di specificare l'ordine in cui il Raspberry Pi cerca dispositivi di avvio.

   .. image:: img/nvme_boot_order.png

#. Quindi, scegli **NVMe/USB boot**. Questo indica al Raspberry Pi di dare priorità all'avvio da SSD connessi tramite USB o da unità NVMe rispetto ad altre opzioni, come la scheda SD.

   .. image:: img/nvme_boot_nvme.png

#. Dopo aver selezionato l'ordine di avvio, premi **Finish** per uscire da ``raspi-config``. Puoi anche utilizzare il tasto **Escape** per chiudere lo strumento di configurazione.

   .. image:: img/nvme_boot_ok.png

#. Per applicare le nuove impostazioni di avvio, riavvia il Raspberry Pi eseguendo:

   .. code-block:: shell

      sudo reboot

   .. image:: img/nvme_boot_reboot.png

Dopo il riavvio, il Raspberry Pi dovrebbe tentare di avviarsi dall'SSD NVMe collegato, fornendoti prestazioni e durata migliorate per il tuo sistema.
