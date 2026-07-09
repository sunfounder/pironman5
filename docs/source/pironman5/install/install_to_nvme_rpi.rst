.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_5:

Installazione del sistema operativo su un SSD NVMe
==============================================================

Se utilizzi un SSD NVMe e disponi di un adattatore per collegare l’SSD NVMe al computer per l’installazione del sistema, puoi seguire il tutorial seguente per un’installazione rapida.

**Componenti richiesti**

* Un computer personale
* Un SSD NVMe
* Un adattatore NVMe a USB
* Scheda Micro SD e lettore


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_5:


2. Aggiornare il bootloader
--------------------------------

Per prima cosa, aggiorna il bootloader del Raspberry Pi 5 in modo che tenti l’avvio prima da **NVMe**, poi da **USB** e infine dalla **scheda SD**.

.. note::

    Si consiglia di utilizzare una **scheda Micro SD di riserva** per questo passaggio.
    
    - Metodo 1 (consigliato): scrivi il bootloader su una scheda Micro SD, inseriscila nel Raspberry Pi ed esegui un avvio per applicare l’impostazione.
    - Metodo 2: scrivi il bootloader direttamente sull’SSD NVMe. Successivamente, collega l’NVMe a un computer per installare il sistema operativo, quindi reinseriscilo nel Raspberry Pi.

#. Inserisci la **scheda Micro SD di riserva o l’SSD NVMe** nel computer utilizzando un lettore di schede o un adattatore.

#. Quando si apre Raspberry Pi Imager, vedrai la pagina **Device**. Seleziona il tuo modello di **Raspberry Pi 5** dall’elenco.

   .. image:: img/imager_device.png
      :width: 90%

#. Fai clic su **OS**.

   * Scorri verso il basso e seleziona **Misc utility images**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Seleziona **Bootloader (Pi 5 family)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Scegli **NVMe/USB Boot** per impostare l’ordine di avvio, quindi fai clic su **NEXT**.

     .. image:: img/nvme_boot.png
        :width: 90%


#. In **Storage**, seleziona la scheda Micro SD o l’SSD NVMe corretto, quindi fai clic su **NEXT**.

   .. note::

      Assicurati che sia selezionato il dispositivo corretto. Se necessario, scollega altri dispositivi di archiviazione.

   .. image:: img/imager_storage.png
      :width: 90%


#. Rivedi le impostazioni e fai clic su **WRITE** per avviare il processo.

   .. image:: img/nvme_write.png
      :width: 90%

#. Conferma l’avviso e consenti a Raspberry Pi Imager di cancellare e scrivere il bootloader.

   .. image:: img/imager_erase.png
      :width: 90%

#. Attendi la comparsa di **Write complete!**, quindi rimuovi in sicurezza il dispositivo di archiviazione.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Inserisci la scheda Micro SD nel Raspberry Pi e accendilo una volta per applicare l’aggiornamento del bootloader.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Attendi almeno **10 secondi** dopo che il Raspberry Pi ha completato l’avvio, quindi spegnilo e rimuovi la scheda Micro SD o l’SSD NVMe.

Il Raspberry Pi 5 è ora pronto per l’avvio da **NVMe**.

.. end_update_bootloader

3. Installare il sistema operativo sull’SSD NVMe
----------------------------------------------------------

Ora puoi installare il sistema operativo sul tuo SSD NVMe.

#. Inserisci l’**SSD NVMe** nel computer utilizzando un adattatore.

2. Quando si apre Raspberry Pi Imager, vedrai la pagina **Device**. Seleziona il tuo modello di **Raspberry Pi 5** dall’elenco.

   .. image:: img/imager_device.png
      :width: 90%

3. Vai alla sezione **OS** e scegli l’opzione consigliata **Raspberry Pi OS (64-bit)**.

   .. warning::

      Assicurati di scegliere una versione a **64 bit**. Se installi un sistema a **32 bit**, alcuni pacchetti sono disponibili solo per ``aarch64`` (64 bit) e alcune funzionalità potrebbero non installarsi o non funzionare correttamente.

   .. image:: img/imager_os.png
      :width: 90%

4. Nella sezione **Storage**, seleziona il tuo **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

