.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche grazie al supporto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e iniziative promozionali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

.. _install_to_nvme_home_bridge_mini:

Installazione del sistema operativo su SSD NVMe
========================================================

Se stai utilizzando un SSD NVMe e disponi di un adattatore per collegarlo al computer per l’installazione del sistema, puoi seguire il tutorial seguente per completare l’installazione in modo rapido.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Componenti necessari**

* Un computer personale
* Un SSD NVMe
* Un adattatore da NVMe a USB
* Una scheda Micro SD e lettore

.. _update_bootloader_mini:

1. Aggiornare il Bootloader
----------------------------------

Per prima cosa, devi aggiornare il bootloader del Raspberry Pi 5 affinché possa avviarsi da NVMe prima di tentare da USB e poi dalla scheda SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    In questo passaggio si consiglia di usare una scheda Micro SD di riserva. Scrivi prima il bootloader su questa scheda e inseriscila subito nel Raspberry Pi per abilitare l'avvio da dispositivo NVMe.

    In alternativa, puoi scrivere il bootloader direttamente sul tuo dispositivo NVMe, inserirlo nel Raspberry Pi per modificarne il metodo di avvio. Dopo l’installazione del sistema operativo tramite computer, reinserisci l’SSD nel Raspberry Pi.

#. Inserisci la scheda Micro SD o l’SSD NVMe nel computer tramite lettore.

#. All’interno di |link_rpi_imager| clicca su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. Nella scheda **Operating System**, scorri verso il basso e seleziona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Seleziona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Seleziona **NVMe/USB Boot** per permettere l’avvio da NVMe prima di USB e SD Card.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Nella sezione **Storage**, seleziona il dispositivo corretto.

   .. note::

      Assicurati di selezionare il dispositivo giusto. Per evitare confusione, scollega eventuali altri dispositivi di archiviazione.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Ora clicca su **NEXT**. Se il dispositivo contiene dati, effettua un backup. Procedi cliccando su **Yes** se non necessario.

   .. image:: img/os_continue.png
      :width: 90%


#. Apparirà una conferma che **NVMe/USB Boot** è stato scritto sul dispositivo di archiviazione.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Inserisci ora la scheda Micro SD o l’SSD NVMe nel Raspberry Pi. Dopo averlo alimentato con un adattatore Type-C, il bootloader sarà scritto nella EEPROM del Raspberry Pi.

.. note::

    Dopo questa operazione, il Raspberry Pi tenterà l’avvio da NVMe prima di USB e poi da SD Card. 
    
    Spegni il Raspberry Pi e rimuovi la Micro SD o l’SSD NVMe.


2. Installare il sistema operativo su SSD NVMe
------------------------------------------------------

Ora puoi installare il sistema operativo sull’SSD NVMe.

**Procedura**

#. Inserisci la scheda SD o l’SSD nel computer tramite un lettore.

#. All’interno di |link_rpi_imager|, clicca su **Raspberry Pi Device** e seleziona **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Clicca sulla scheda **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scorri fino in fondo e seleziona il sistema operativo desiderato.

   .. note::

      * Per il sistema **Ubuntu**, clicca su **Other general-purpose OS** -> **Ubuntu** e seleziona **Ubuntu Desktop 24.04 LTS (64 bit)** o **Ubuntu Server 24.04 LTS (64 bit)**.
      * Per **Kali Linux**, **Home Assistant** e **Homebridge**, clicca su **Other specific-purpose OS** e seleziona il sistema corrispondente.

   .. image:: img/os_other_os.png
      :width: 90%

#. In **Storage**, seleziona il dispositivo NVMe corretto.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Clicca su **NEXT**.

   .. note::

      * Per i sistemi non configurabili in anticipo, dopo **NEXT**, ti verrà chiesto se vuoi mantenere i dati esistenti. Se hai già fatto un backup, seleziona **Yes**.
      * Per sistemi configurabili (Hostname, WiFi, SSH), apparirà un prompt per applicare le personalizzazioni. Puoi scegliere **Yes**, **No** o tornare indietro per modificare.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Definisci un **hostname** per il tuo Raspberry Pi. Sarà l’identificativo in rete accessibile via ``<hostname>.local`` o ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Crea uno **Username** e una **Password** per l’account amministratore. È importante per la sicurezza, poiché non esiste una password predefinita.

     .. image:: img/os_set_username.png

   * Configura la rete wireless inserendo **SSID** e **Password** della tua rete.

     .. note::

        Imposta il campo ``Wireless LAN country`` con il codice a due lettere secondo lo standard `ISO/IEC alpha2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_.

     .. image:: img/os_set_wifi.png

   * Per la connessione remota, abilita SSH nella scheda Services.

     * Per **autenticazione via password**, usa le credenziali definite sopra.
     * Per autenticazione tramite chiave pubblica, seleziona “Allow public-key authentication only”. Se non hai una chiave RSA, clicca su “Run SSH-keygen” per generarne una.

     .. image:: img/os_enable_ssh.png

   * Dal menu **Options** puoi configurare il comportamento di Imager, come espulsione automatica e notifica sonora.

     .. image:: img/os_options.png



#. Dopo aver completato la configurazione del sistema operativo, clicca su **Save**, poi su **Yes** per applicarla durante la scrittura dell’immagine.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Se l’SSD NVMe contiene dati, esegui un backup. In caso contrario, clicca su **Yes** per procedere.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Quando appare il messaggio "Write Successful", l’immagine è stata scritta e verificata correttamente. Ora sei pronto per avviare il Raspberry Pi da SSD NVMe!
