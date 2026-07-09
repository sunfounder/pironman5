.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _copy_sd_to_nvme_promax:

Copiare il Sistema Operativo dalla Micro SD all'NVMe SSD
==================================================================

Se disponi di un SSD NVMe ma non hai un adattatore per collegarlo al tuo computer, puoi optare per un terzo approccio: installare inizialmente il sistema sulla tua scheda Micro SD. Dopo che il Pironman 5 Pro MAX si è avviato con successo, puoi quindi trasferire il sistema dalla tua scheda Micro SD al tuo SSD NVMe.

* Per prima cosa, devi :ref:`install_os_sd_rpi_promax`.
* Successivamente, avvia e accedi al tuo Raspberry Pi. Se non sei sicuro di come accedere, puoi visitare il sito web ufficiale di Raspberry Pi: |link_rpi_get_start|.

Completa i passaggi sopra prima di procedere con le istruzioni seguenti.

1. Abilitare PCIe
--------------------

Per impostazione predefinita il connettore PCIe non è abilitato.

* Per abilitarlo devi aprire il file ``/boot/firmware/config.txt``.

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* Quindi aggiungi la seguente riga al file.

  .. code-block:: shell

    # Enable the PCIe External connector.
    dtparam=pciex1

* Esiste un alias più facile da ricordare per ``pciex1``, quindi puoi anche aggiungere ``dtparam=nvme`` al file ``/boot/firmware/config.txt``.

  .. code-block:: shell

    dtparam=nvme

* Dovrai disabilitare il ritardo di avvio PCIe in modo che il Raspberry Pi possa rilevare l'unità NVMe dietro lo switch PCIe all'avvio. Aggiungi la seguente riga a ``/boot/firmware/config.txt``:

   .. code-block:: shell

      dtparam=pciex1_no_10s=on

* Premi ``Ctrl + X``, ``Y`` e ``Enter`` per salvare le modifiche.

**BOOT_ORDER**

Se hai installato due unità di sistema NVMe e devi scegliere da quale avviare,
puoi modificare ``ROOT=PARTUUID=xxxxxxxxx`` nel file ``/boot/firmware/cmdline.txt`` con l'UUID del disco da cui desideri avviare. Puoi trovare l'UUID del disco con il seguente comando:

.. code-block:: shell

   ls /dev/disk/by-id/

.. start_copy_nvme

2. Installare il Sistema Operativo sull'SSD
-----------------------------------------------------------------------

Ci sono due modi per installare un sistema operativo sull'SSD:

**Copiare il Sistema dalla Scheda Micro SD all'SSD**

#. Collega un display o accedi al desktop del Raspberry Pi tramite VNC Viewer. Quindi clicca su **Raspberry Pi logo** -> **Accessori** -> **SD Card Copier**.

   .. image:: img/ssd_copy.png

#. Assicurati di selezionare i dispositivi **Copia da** e **Copia a** corretti. Fai attenzione a non confonderli.

   .. image:: img/ssd_copy_from.png

#. Ricordati di selezionare "NEW Partition UUIDs" per assicurarti che il sistema possa distinguere correttamente i dispositivi, evitando conflitti di montaggio e problemi di avvio.

   .. image:: img/ssd_copy_uuid.png

#. Dopo la selezione, clicca su **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Ti verrà chiesto che il contenuto sull'SSD verrà cancellato. Assicurati di eseguire il backup dei tuoi dati prima di cliccare su Sì. Attendi per un po' di tempo, e la copia sarà completata.

**Installare il Sistema con Raspberry Pi Imager**

Se la tua scheda Micro SD ha installata una versione desktop del sistema, puoi utilizzare uno strumento di imaging (come Raspberry Pi Imager) per scrivere il sistema sull'SSD. Questo esempio utilizza Raspberry Pi OS bookworm, ma altri sistemi potrebbero richiedere l'installazione preliminare dello strumento di imaging.

#. Collega un display o accedi al desktop del Raspberry Pi tramite VNC Viewer. Quindi clicca su **Raspberry Pi logo** -> **Accessori** -> **Raspberry Pi Imager**.

   .. image:: img/ssd_imager.png

#. Inserisci la tua scheda microSD nel tuo computer usando un lettore di schede. Esegui il backup di tutti i dati importanti prima di procedere.

   .. image:: img/insert_sd.png
      :width: 90%

#. Quando Raspberry Pi Imager si apre, vedrai la pagina **Device**. Seleziona il tuo modello Raspberry Pi 5 dall'elenco.

   .. image:: img/imager_device.png
      :width: 90%

#. Vai alla sezione **OS** e scegli l'opzione consigliata **Raspberry Pi OS (64-bit)**.

   .. warning::

      Assicurati di scegliere una versione a **64 bit**. Se installi un sistema a **32 bit**, alcuni pacchetti sono disponibili solo per ``aarch64`` (64 bit) e alcune funzionalità potrebbero non installarsi o non funzionare correttamente.

   .. image:: img/imager_os.png
      :width: 90%

#. Nella sezione **Storage**, seleziona il tuo **NVMe SSD**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_promax:

3. Configurare l'avvio dall'SSD
---------------------------------------

In questa sezione, configureremo il tuo Raspberry Pi per avviarsi direttamente da un SSD NVMe, fornendo tempi di avvio più rapidi e prestazioni migliori rispetto a una scheda SD. Segui attentamente questi passaggi:

#. Per prima cosa, apri un terminale sul tuo Raspberry Pi ed esegui il seguente comando per accedere all'interfaccia di configurazione:

   .. code-block:: shell

      sudo raspi-config

#. Nel menu ``raspi-config``, usa i tasti freccia per navigare e seleziona **Advanced Options**. Premi ``Enter`` per accedere alle impostazioni avanzate.

   .. image:: img/nvme_open_config.png

#. All'interno di **Advanced Options**, seleziona **Boot Order**. Questa impostazione ti permette di specificare l'ordine in cui il tuo Raspberry Pi cerca i dispositivi avviabili.

   .. image:: img/nvme_boot_order.png

#. Quindi, scegli **NVMe/USB boot**. Questo dice al Raspberry Pi di dare priorità all'avvio da SSD collegati via USB o unità NVMe rispetto ad altre opzioni, come la scheda SD.

   .. image:: img/nvme_boot_nvme.png

#. Dopo aver selezionato l'ordine di avvio, premi **Finish** per uscire da raspi-config. Puoi anche usare il tasto **Escape** per chiudere lo strumento di configurazione.

   .. image:: img/nvme_boot_ok.png

#. Per applicare le nuove impostazioni di avvio, riavvia il tuo Raspberry Pi eseguendo ``sudo reboot``.

   .. code-block:: shell

      sudo reboot

   .. image:: img/nvme_boot_reboot.png

Dopo il riavvio, il Raspberry Pi dovrebbe ora tentare di avviarsi dal tuo SSD NVMe collegato, offrendoti prestazioni e durata migliorate per il tuo sistema.

.. end_copy_nvme