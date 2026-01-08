.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _copy_sd_to_nvme_max:

Copiare il sistema operativo da Micro SD a SSD NVMe
==================================================================

Se disponi di un SSD NVMe ma non hai un adattatore per collegarlo al computer, puoi utilizzare un terzo metodo: installare inizialmente il sistema sulla scheda Micro SD. Dopo che il Pironman 5 MAX si è avviato correttamente, potrai quindi trasferire il sistema dalla scheda Micro SD all’SSD NVMe.

* Per prima cosa, devi completare :ref:`install_os_sd_max`.
* Quindi, avvia e accedi al tuo Raspberry Pi. Se non sei sicuro di come effettuare l’accesso, puoi visitare il sito ufficiale di Raspberry Pi: |link_rpi_get_start|.

Completa i passaggi sopra indicati prima di procedere con le istruzioni seguenti.


1. Abilitare PCIe
--------------------

Per impostazione predefinita, il connettore PCIe non è abilitato. 

* Per abilitarlo, apri il file ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Quindi aggiungi la seguente riga al file. 

  .. code-block:: shell
  
    # Abilita il connettore PCIe esterno.
    dtparam=pciex1
  
* Esiste anche un alias più facile da ricordare per ``pciex1``, quindi in alternativa puoi aggiungere ``dtparam=nvme`` al file ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    dtparam=nvme

.. * La connessione è certificata per velocità Gen 2.0 (5 GT/sec), ma puoi forzarla a Gen 3.0 (10 GT/sec) aggiungendo le seguenti righe al file ``/boot/firmware/config.txt``.

..   .. code-block:: shell
  
..     # Forza la velocità Gen 3.0
..     dtparam=pciex1_gen=3
  
..   .. warning::
  
..     Il Raspberry Pi 5 non è certificato per velocità Gen 3.0 e le connessioni ai dispositivi PCIe a queste velocità potrebbero essere instabili.

*  Dovrai disabilitare il ritardo di avvio PCIe affinché il Raspberry Pi possa rilevare l’unità NVMe dietro lo switch PCIe all’avvio. Aggiungi la seguente riga a ``/boot/firmware/config.txt``：

   .. code-block:: shell

      dtparam=pciex1_no_10s=on


* Premi ``Ctrl + X``, ``Y`` e ``Enter`` per salvare le modifiche.


**BOOT_ORDER**

Se hai installato due unità di sistema NVMe e devi scegliere da quale avviare, 
puoi modificare ``ROOT=PARTUUID=xxxxxxxxx`` nel file ``/boot/firmware/cmdline.txt`` impostandolo sull’UUID del disco da cui desideri avviare il sistema. Puoi trovare l’UUID del disco con il seguente comando:

.. code-block:: shell

   ls /dev/disk/by-id/

.. start_copy_nvme

2. Installare il sistema operativo sull’SSD
-----------------------------------------------

Esistono due modi per installare un sistema operativo sull’SSD:

**Copiare il sistema dalla scheda Micro SD all’SSD**

#. Collega un display oppure accedi al desktop del Raspberry Pi tramite VNC Viewer. Quindi fai clic su **logo Raspberry Pi** -> **Accessori** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png
      
    
#. Assicurati di selezionare correttamente i dispositivi **Copia da** e **Copia a**. Fai attenzione a non confonderli.

   .. image:: img/ssd_copy_from.png
      
#. Ricorda di selezionare “NEW Partition UUIDs” per garantire che il sistema possa distinguere correttamente i dispositivi, evitando conflitti di montaggio e problemi di avvio.

   .. image:: img/ssd_copy_uuid.png
    
#. Dopo la selezione, fai clic su **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Ti verrà richiesto di confermare che il contenuto dell’SSD verrà cancellato. Assicurati di eseguire il backup dei tuoi dati prima di fare clic su Yes. Attendi qualche istante e la copia verrà completata.

**Installare il sistema con Raspberry Pi Imager**

Se sulla tua scheda Micro SD è installata una versione desktop del sistema, puoi utilizzare uno strumento di imaging (come Raspberry Pi Imager) per scrivere il sistema sull’SSD. In questo esempio viene utilizzato Raspberry Pi OS Bookworm, ma altri sistemi potrebbero richiedere l’installazione preventiva dello strumento di imaging.

#. Collega un display oppure accedi al desktop del Raspberry Pi tramite VNC Viewer. Quindi fai clic su **logo Raspberry Pi** -> **Accessori** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Inserisci la tua scheda microSD nel computer utilizzando un lettore di schede. Esegui il backup di eventuali dati importanti prima di procedere.

   .. image:: img/insert_sd.png
      :width: 90%

#. Quando si apre Raspberry Pi Imager, verrà visualizzata la pagina **Device**. Seleziona il modello del tuo Raspberry Pi 5 dall’elenco.

   .. image:: img/imager_device.png
      :width: 90%

#. Vai alla sezione **OS** e scegli l’opzione consigliata **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

#. Nella sezione **Storage**, seleziona il tuo **SSD NVMe**. 

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_max:

3. Configurare l’avvio dall’SSD
---------------------------------------

In questa sezione configureremo il tuo Raspberry Pi affinché si avvii direttamente da un SSD NVMe, garantendo tempi di avvio più rapidi e prestazioni migliori rispetto a una scheda SD. Segui attentamente questi passaggi:

#. Per prima cosa, apri un terminale sul tuo Raspberry Pi ed esegui il seguente comando per accedere all’interfaccia di configurazione:.

   .. code-block:: shell

      sudo raspi-config

#. Nel menu ``raspi-config``, utilizza i tasti freccia per navigare e seleziona **Advanced Options**. Premi ``Enter`` per accedere alle impostazioni avanzate.

   .. image:: img/nvme_open_config.png

#. All’interno di **Advanced Options**, seleziona **Boot Order**. Questa impostazione consente di specificare l’ordine con cui il Raspberry Pi cerca i dispositivi avviabili.

   .. image:: img/nvme_boot_order.png

#. Quindi, scegli **NVMe/USB boot**. Questo indica al Raspberry Pi di dare priorità all’avvio da SSD collegati tramite USB o unità NVMe rispetto ad altre opzioni, come la scheda SD.

   .. image:: img/nvme_boot_nvme.png

#. Dopo aver selezionato l’ordine di avvio, premi **Finish** per uscire da raspi-config. Puoi anche utilizzare il tasto **Escape** per chiudere lo strumento di configurazione.

   .. image:: img/nvme_boot_ok.png

#. Per applicare le nuove impostazioni di avvio, riavvia il tuo Raspberry Pi eseguendo ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

Dopo il riavvio, il Raspberry Pi dovrebbe ora tentare di avviarsi dall’SSD NVMe collegato, offrendo prestazioni e affidabilità migliorate per il tuo sistema.

.. end_copy_nvme
