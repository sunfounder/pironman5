.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e difficoltà tecniche grazie al supporto del nostro team e della nostra community.
    - **Learn & Share**: Scambia suggerimenti e tutorial per sviluppare ulteriormente le tue abilità.
    - **Exclusive Previews**: Ottieni accesso anticipato ai nuovi annunci di prodotto e ad anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway riservati alla community.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

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

2. Installation des Betriebssystems auf der NVMe-SSD
-------------------------------------------------------------------------

**Schritte**

1. Lade das neueste Umbrel-OS-Image herunter und entpacke es. Du kannst auch die `Umbrel-Release-Seite <https://github.com/getumbrel/umbrel/releases>`_ besuchen, um eine bestimmte Version auszuwählen.

   * :download:`Neueste Umbrel-OS-Image-Datei <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. Öffne |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle **Raspberry Pi 5** aus dem Dropdown-Menü.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. Starte den **Raspberry Pi Imager** und klicke auf **CHOOSE OS**.

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. Scrolle bis zum Ende und wähle **Use custom**.

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. Wähle die zuvor heruntergeladene Umbrel-OS-Image-Datei aus und klicke auf **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. Wähle unter **Storage** die NVMe-SSD als Ziel für die Installation aus.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. Klicke auf **NEXT** und dann auf **NO**. Umbrel OS initialisiert automatisch sein eigenes System und die Benutzereinrichtung beim ersten Start und verwendet keine im Raspberry Pi Imager gesetzten Benutzer- oder Passwortdaten.

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. Wenn sich auf der NVMe-SSD bereits Daten befinden, erstelle vor dem Fortfahren ein Backup, um Datenverlust zu vermeiden. Klicke auf **Yes**, um fortzufahren, wenn kein Backup erforderlich ist.

   .. image:: img/nvme_erase.png
      :width: 90%

9. Wenn die Meldung „Write Successful“ erscheint, bedeutet das, dass das Image vollständig geschrieben und überprüft wurde. Deine NVMe-SSD ist nun bereit, den Raspberry Pi zu starten!

   .. image:: img/umbrel_finish.png
      :width: 90%
