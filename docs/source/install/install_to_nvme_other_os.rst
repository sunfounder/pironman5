.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_to_nvme_home_bridge:

Installazione del Sistema Operativo su un SSD NVMe
============================================================

Se stai utilizzando un SSD NVMe e hai un adattatore per collegarlo al tuo computer per l'installazione del sistema, puoi seguire il tutorial seguente per un'installazione rapida.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  
        
**Componenti necessari**

* Un computer
* Un SSD NVMe
* Un adattatore NVMe a USB
* Scheda Micro SD e lettore

.. _update_bootloader:

1. Aggiorna il Bootloader
----------------------------------

Per prima cosa, devi aggiornare il bootloader del Raspberry Pi 5 per avviarsi da NVMe prima di provare USB e poi la scheda SD.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    In questo passaggio, si consiglia di utilizzare una scheda Micro SD di riserva. Prima scrivi il bootloader su questa scheda Micro SD e poi inseriscila immediatamente nel Raspberry Pi per abilitare l'avvio da un dispositivo NVMe.
    
    In alternativa, puoi scrivere prima il bootloader direttamente sul tuo dispositivo NVMe, quindi inserirlo nel Raspberry Pi per modificare il metodo di avvio. Successivamente, collega l'SSD NVMe a un computer per installare il sistema operativo e, una volta completata l'installazione, reinseriscilo nel Raspberry Pi.

#. Inserisci la tua scheda Micro SD di riserva o SSD NVMe nel computer o nel laptop utilizzando un lettore.

#. All'interno del |link_rpi_imager|, fai clic su **Dispositivo Raspberry Pi** e seleziona il modello **Raspberry Pi 5** dall'elenco a discesa.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. Nella scheda **Sistema Operativo**, scorri verso il basso e seleziona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Seleziona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Seleziona **NVMe/USB Boot** per consentire al Raspberry Pi 5 di avviarsi da NVMe prima di provare USB e poi la scheda SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      


#. Nella sezione **Storage**, seleziona il dispositivo di archiviazione appropriato per l'installazione.

   .. note::

      Assicurati di selezionare il dispositivo di archiviazione corretto. Per evitare confusione, disconnetti eventuali dispositivi di archiviazione aggiuntivi se ne sono collegati più di uno.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Ora puoi fare clic su **NEXT**. Se il dispositivo di archiviazione contiene dati esistenti, assicurati di eseguire un backup per prevenire la perdita di dati. Procedi facendo clic su **Yes** se non è necessario alcun backup.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Presto, ti verrà comunicato che **NVMe/USB Boot** è stato scritto sul tuo dispositivo di archiviazione.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Ora puoi inserire la tua scheda Micro SD o SSD NVMe nel Raspberry Pi. Dopo aver alimentato il Raspberry Pi con un adattatore di tipo C, il bootloader dalla scheda Micro SD o dall'SSD NVMe verrà scritto sull'EEPROM del Raspberry Pi.

.. note::

   Successivamente, il Raspberry Pi si avvierà da NVMe prima di provare USB e poi la scheda SD. 
    
   Spegni il Raspberry Pi e rimuovi la scheda Micro SD o l'SSD NVMe.


2. Installa il Sistema Operativo su NVMe SSD
---------------------------------------------

Ora puoi installare il sistema operativo sul tuo SSD NVMe.

**Passaggi**

#. Inserisci la tua scheda SD nel tuo computer o laptop utilizzando un lettore.

#. All'interno del |link_rpi_imager|, fai clic su **Dispositivo Raspberry Pi** e seleziona il modello **Raspberry Pi 5** dall'elenco a discesa.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      

#. Fai clic sulla scheda **Sistema Operativo**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo alla pagina e seleziona il tuo sistema operativo.

   .. note::

      * Per il sistema **Ubuntu**, è necessario fare clic su **Other general-purpose OS** -> **Ubuntu**, e selezionare **Ubuntu Desktop 24.04 LTS (64 bit)** oppure **Ubuntu Server 24.04 LTS (64 bit)**.
      * Per i sistemi **Kali Linux**, **Home Assistant** e **Homebridge**, è necessario fare clic su **Other specific-purpose OS** e quindi selezionare il sistema corrispondente.

   .. image:: img/os_other_os.png
      :width: 90%

#. Nella sezione **Storage**, seleziona il dispositivo di archiviazione appropriato per l'installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      

#. Fai clic su **NEXT**.

   .. note::

      * Per i sistemi che non possono essere configurati in anticipo, dopo aver fatto clic su **NEXT**, ti verrà chiesto se salvare i dati all'interno del dispositivo. Se hai confermato di aver eseguito un backup, seleziona **Yes**.

      * Per i sistemi in cui è possibile configurare in anticipo Hostname, WiFi e Abilita SSH, apparirà una finestra che chiederà se applicare le impostazioni personalizzate del sistema operativo. Puoi scegliere **Yes**, **No** o tornare indietro per ulteriori modifiche.

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Definisci un **hostname** per il tuo Raspberry Pi. L'hostname è l'identificativo di rete del tuo Raspberry Pi. Puoi accedere al tuo Pi utilizzando ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea un **Nome Utente** e una **Password** per l'account amministratore del Raspberry Pi. Stabilire un nome utente e una password univoci è fondamentale per proteggere il tuo Raspberry Pi, che non dispone di una password predefinita.

     .. image:: img/os_set_username.png

   * Configura la rete wireless fornendo il **SSID** e la **Password** della tua rete.

     .. note::

       Imposta il ``Paese della LAN wireless`` sul codice `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ a due lettere corrispondente alla tua posizione.

     .. image:: img/os_set_wifi.png
         
   * Per connetterti in remoto al tuo Raspberry Pi, abilita SSH nella scheda Servizi.

     * Per l'**autenticazione tramite password**, utilizza il nome utente e la password dalla scheda Generale.
     * Per l'autenticazione con chiave pubblica, scegli "Consenti solo autenticazione con chiave pubblica". Se disponi di una chiave RSA, verrà utilizzata. In caso contrario, fai clic su "Esegui SSH-keygen" per generare una nuova coppia di chiavi.

     .. image:: img/os_enable_ssh.png

   * Il menu **Opzioni** ti consente di configurare il comportamento di Imager durante la scrittura, inclusa la riproduzione di un suono al termine, l'espulsione del supporto al termine e l'abilitazione della telemetria.

     .. image:: img/os_options.png

         
    
#. Quando hai terminato di inserire le impostazioni di personalizzazione del sistema operativo, fai clic su **Salva** per salvare la tua personalizzazione. Quindi, fai clic su **Yes** per applicarle durante la scrittura dell'immagine.

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. Se l'SSD NVMe contiene dati esistenti, assicurati di eseguire un backup per prevenire la perdita di dati. Procedi facendo clic su **Yes** se non è necessario alcun backup.

   .. image:: img/nvme_erase.png
      :width: 90%
      

#. Quando visualizzi il popup "Scrittura riuscita", l'immagine è stata completamente scritta e verificata. Ora sei pronto per avviare un Raspberry Pi dall'SSD NVMe!
