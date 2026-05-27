.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Installazione del sistema operativo Batocera
==========================================================

Segui il tutorial qui sotto per installare il sistema sulla tua scheda microSD.

**Componenti richiesti**

* Un computer personale
* Una scheda Micro SD e un lettore di schede

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installare il sistema operativo sulla scheda microSD
-------------------------------------------------------------------

1. Inserisci la tua scheda microSD nel tuo computer utilizzando un lettore di schede.  
   Prima di procedere, esegui il backup di tutti i dati importanti presenti sulla scheda, poiché verranno cancellati.

   .. image:: img/insert_sd.png
      :width: 90%

2. Quando si apre **Raspberry Pi Imager**, vedrai la pagina **Device (Dispositivo)**.  
   Seleziona il tuo modello di **Raspberry Pi 5** dalla lista.

   .. image:: img/imager_device.png
      :width: 90%

3. Vai nella sezione **OS (Sistema Operativo)**, scorri verso il fondo della pagina e seleziona il tuo sistema operativo.

   .. note::

      * Per **Ubuntu**, clicca su **Other general-purpose OS (Altri OS generici)** → **Ubuntu**, poi seleziona  
        **Ubuntu Desktop 24.04 LTS (64-bit)** o **Ubuntu Server 24.04 LTS (64-bit)**.
      * Per **Kali Linux**, **Home Assistant** e **Homebridge**, clicca su  
        **Other specific-purpose OS (Altri OS per scopi specifici)**, poi seleziona il sistema corrispondente.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Nella sezione **Storage (Memorizzazione)**, seleziona la tua scheda microSD.  
   Per maggiore sicurezza, si consiglia di scollegare gli altri dispositivi di archiviazione USB in modo che solo la scheda microSD appaia nella lista.

   .. image:: img/imager_storage.png
      :width: 90%

#. Clicca su **NEXT (AVANTI)**.

   .. note::

      * Per i sistemi che **non possono essere preconfigurati**, cliccare su **NEXT (AVANTI)** salterà il passaggio di **Customisation (Personalizzazione)** e passerà direttamente a **Writing (Scrittura)**, dove il sistema operativo viene scritto sulla scheda microSD.
      * Per i sistemi che **supportano la preconfigurazione**, segui i passi di **Customisation (Personalizzazione)** per configurare opzioni come **Hostname**, **WiFi** e l'**abilitazione di SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Quando appare la finestra pop-up **« Write Successful (Scrittura Riuscita) »**, l'immagine è stata completamente scritta e verificata. Ora puoi rimuovere in sicurezza la scheda microSD e usarla per avviare il tuo Raspberry Pi.