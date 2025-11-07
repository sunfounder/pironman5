.. note::

    Ciao, benvenuto nella Community SunFounder dedicata agli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni stagionali e giveaway.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!


Installazione di Umbrel OS
============================================

Umbrel è una piattaforma/OS open-source per server domestici che ti consente di eseguire il tuo nodo Bitcoin, installare una varietà di app self-hosted con un clic e trasformare il tuo hardware nel tuo cloud personale. È un modo eccellente per iniziare con l’autocustodia e la privacy.

**Componenti richiesti**

* Un computer personale  
* Un SSD NVMe  
* Un adattatore NVMe a USB  
* Una scheda Micro SD e un lettore

1. Aggiornare il Bootloader
--------------------------------

Per prima cosa, è necessario aggiornare il bootloader del Raspberry Pi 5 in modo che esegua l’avvio da NVMe prima di provare da USB e poi dalla scheda SD.

.. note::

    * In questo passaggio, è consigliato utilizzare una scheda Micro SD di riserva. Prima scrivi il bootloader su questa scheda Micro SD e poi inseriscila immediatamente nel Raspberry Pi per abilitare l’avvio da un dispositivo NVMe.  
    * In alternativa, puoi scrivere il bootloader direttamente sul tuo dispositivo NVMe, quindi inserirlo nel Raspberry Pi per modificare il metodo di avvio. Successivamente, collega l’SSD NVMe a un computer per installare il sistema operativo e, una volta completata l’installazione, reinseriscilo nel Raspberry Pi.

#. Inserisci la tua scheda Micro SD o SSD NVMe nel computer o laptop utilizzando un lettore.

#. All’interno di |link_rpi_imager|, fai clic su **Raspberry Pi Device** e seleziona il modello **Raspberry Pi 5** dal menu a discesa.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Nella scheda **Operating System**, scorri verso il basso e seleziona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Seleziona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Seleziona **NVMe/USB Boot** per consentire al Raspberry Pi 5 di avviarsi da NVMe prima di provare USB e poi la scheda SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      
#. Nell’opzione **Storage**, seleziona il dispositivo di archiviazione appropriato per l’installazione.

   .. note::

      Assicurati di selezionare il dispositivo di archiviazione corretto. Per evitare confusione, scollega eventuali dispositivi di archiviazione aggiuntivi se ne sono collegati più di uno.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Ora puoi cliccare su **NEXT**. Se il dispositivo di archiviazione contiene dati esistenti, assicurati di eseguire un backup per evitare la perdita di dati. Procedi cliccando su **Yes** se non è necessario alcun backup.

   .. image:: img/os_continue.png
      :width: 90%
      

#. A breve ti verrà comunicato che **NVMe/USB Boot** è stato scritto sul tuo dispositivo di archiviazione.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Inserisci la tua scheda Micro SD o SSD NVMe nel Raspberry Pi. Dopo aver collegato l’adattatore di alimentazione Type-C, il bootloader dalla scheda Micro SD o dall’SSD NVMe verrà scritto nella EEPROM del Raspberry Pi.

   .. note::

      * Dopo l’aggiornamento, il Raspberry Pi si avvierà prima dall’unità NVMe, poi da USB e infine dalla scheda Micro SD.  
      * Attendi uno o due minuti, poi spegni il Raspberry Pi e rimuovi la scheda Micro SD o l’SSD NVMe.


2. Installare il sistema operativo sull’SSD NVMe
-------------------------------------------------------------

**Passaggi**

1. Scarica l’ultima immagine di Umbrel OS ed estraila. Puoi anche visitare la `pagina dei rilasci di Umbrel <https://github.com/getumbrel/umbrel/releases>`_ per scegliere una versione specifica.

   * :download:`Ultima immagine di Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. In |link_rpi_imager|, fai clic su **Raspberry Pi Device** e seleziona **Raspberry Pi 5** dal menu a discesa.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. Avvia il **Raspberry Pi Imager** e fai clic su **CHOOSE OS**.

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. Scorri fino in fondo e seleziona **Use custom**.

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. Seleziona il file immagine di Umbrel OS che hai scaricato in precedenza e fai clic su **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. Nella sezione **Storage**, seleziona l’SSD NVMe come destinazione per l’installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. Clicca su **NEXT**, poi seleziona **NO**. Umbrel OS inizializzerà automaticamente il proprio sistema e la configurazione dell’utente durante il primo avvio e non utilizza il nome utente o la password impostati nel Raspberry Pi Imager.

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. Se l’SSD NVMe contiene dati esistenti, esegui un backup prima di procedere per evitare la perdita di dati. Clicca su **Yes** per continuare se non è necessario alcun backup.

   .. image:: img/nvme_erase.png
      :width: 90%

9. Quando appare il messaggio “Write Successful”, significa che l’immagine è stata completamente scritta e verificata. Il tuo SSD NVMe è ora pronto per avviare il Raspberry Pi!

   .. image:: img/umbrel_finish.png
      :width: 90%


