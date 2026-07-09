.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_to_nvme_rpi_promax:

Installazione del Sistema Operativo su un SSD NVMe
=============================================================================================

Se stai utilizzando un SSD NVMe e disponi di un adattatore per collegare l'SSD NVMe al tuo computer per l'installazione del sistema, puoi utilizzare il seguente tutorial per un'installazione rapida.

**Componenti Richiesti**

* Un Personal Computer
* Un SSD NVMe
* Un Adattatore NVMe-USB
* Scheda Micro SD e Lettore

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_promax:

2. Aggiornare il Bootloader
--------------------------------------------------------------------

Prima, aggiorna il bootloader del Raspberry Pi 5 in modo che tenti di avviarsi prima da **NVMe**, poi da **USB**, e infine dalla **scheda SD**.

.. note::

    Si consiglia di utilizzare una **scheda Micro SD di riserva** per questo passaggio.

    - Metodo 1 (Consigliato): Scrivi il bootloader su una scheda Micro SD, inseriscila nel Raspberry Pi e avvia una volta per applicare l'impostazione.
    - Metodo 2: Scrivi il bootloader direttamente sull'SSD NVMe. Successivamente, collega l'NVMe a un computer per installare il sistema operativo, poi rimettilo nel Raspberry Pi.

#. Inserisci la **scheda Micro SD o SSD NVMe** di riserva nel tuo computer usando un lettore di schede o un adattatore.

#. Quando Raspberry Pi Imager si apre, vedrai la pagina **Device**. Seleziona il tuo modello Raspberry Pi 5 dall'elenco.

   .. image:: img/imager_device.png
      :width: 90%

#. Clicca su **OS**.

   * Scorri verso il basso e seleziona **Misc utility images**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Seleziona **Bootloader (Pi 5 family)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Scegli **NVMe/USB Boot** per impostare l'ordine di avvio, poi clicca su **NEXT**.

     .. image:: img/nvme_boot.png
        :width: 90%

#. In **Storage**, seleziona la scheda Micro SD o l'SSD NVMe corretto, poi clicca su **NEXT**.

   .. note::

      Assicurati che sia selezionato il dispositivo corretto. Scollega altri dispositivi di archiviazione se necessario.

   .. image:: img/imager_storage.png
      :width: 90%

#. Rivedi le impostazioni e clicca su **WRITE** per iniziare.

   .. image:: img/nvme_write.png
      :width: 90%

#. Conferma l'avviso e consenti a Raspberry Pi Imager di cancellare e scrivere il bootloader.

   .. image:: img/imager_erase.png
      :width: 90%

#. Attendere fino alla comparsa di **Write complete!**, quindi rimuovi in sicurezza il dispositivo di archiviazione.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Inserisci la scheda Micro SD nel Raspberry Pi e accendilo una volta per applicare l'aggiornamento del bootloader.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Attendere almeno **10 secondi** dopo che il Raspberry Pi ha terminato l'avvio, quindi spegnilo e rimuovi la scheda Micro SD o l'SSD NVMe.

Il Raspberry Pi 5 è ora pronto per avviarsi da **NVMe**.

.. end_update_bootloader

3. Installare il Sistema Operativo sull'SSD NVMe
-----------------------------------------------------------------------

Ora puoi installare il sistema operativo sul tuo SSD NVMe.

#. Inserisci l'**SSD NVMe** nel tuo computer utilizzando un adattatore.

2. Quando Raspberry Pi Imager si apre, vedrai la pagina **Device**. Seleziona il tuo modello Raspberry Pi 5 dall'elenco.

   .. image:: img/imager_device.png
      :width: 90%

3. Vai alla sezione **OS** e scegli l'opzione consigliata **Raspberry Pi OS (64-bit)**.

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