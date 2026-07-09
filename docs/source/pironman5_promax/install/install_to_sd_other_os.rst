.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_to_sd_other_promax:

Installazione del Sistema Operativo su una Scheda Micro SD
===========================================================================

Se stai utilizzando una scheda Micro SD, puoi seguire il tutorial qui sotto per installare il sistema sulla tua scheda Micro SD.

**Componenti Richiesti**

* Un Personal Computer
* Una scheda Micro SD e un Lettore

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installare il Sistema Operativo sulla scheda microSD
--------------------------------------------------------------------------

1. Inserisci la tua scheda microSD nel tuo computer usando un lettore di schede.
   Prima di procedere, esegui il backup di tutti i dati importanti sulla scheda, poiché verranno cancellati.

   .. image:: img/insert_sd.png
      :width: 90%

2. Quando **Raspberry Pi Imager** si apre, vedrai la pagina **Device**.
   Seleziona il tuo modello **Raspberry Pi 5** dall'elenco.

   .. image:: img/imager_device.png
      :width: 90%

3. Vai alla sezione **OS**, scorri verso il basso fino alla fine della pagina e seleziona il tuo sistema operativo.

   .. note::

      * Per **Ubuntu**, clicca su **Other general-purpose OS** → **Ubuntu**, quindi seleziona
        **Ubuntu Desktop 24.04 LTS (64-bit)** o **Ubuntu Server 24.04 LTS (64-bit)**.
      * Per **Kali Linux** e **Homebridge**, clicca su
        **Other specific-purpose OS**, quindi seleziona il sistema corrispondente.

   .. warning::

      Qualunque sistema tu scelga, assicurati di selezionare una versione a **64 bit**. Su un sistema a **32 bit**, alcuni pacchetti sono disponibili solo per ``aarch64`` (64 bit) e alcune funzionalità potrebbero non installarsi o non funzionare correttamente.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Nella sezione **Storage**, seleziona la tua scheda microSD.
   Per sicurezza, si consiglia di scollegare altri dispositivi di archiviazione USB in modo che solo la scheda microSD appaia nell'elenco.

   .. image:: img/imager_storage.png
      :width: 90%

#. Clicca su **NEXT**.

   .. note::

      * Per i sistemi che **non possono essere configurati in anticipo**, cliccare su **NEXT** salterà il passaggio **Customisation** e andrà direttamente a **Writing**, dove il sistema operativo viene scritto sulla scheda microSD.
      * Per i sistemi che **supportano la pre-configurazione**, segui i passaggi di **Customisation** per configurare opzioni come **Hostname**, **WiFi** e **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Quando appare il messaggio **“Write Successful”**, l'immagine è stata completamente scritta e verificata. Ora puoi rimuovere in sicurezza la scheda microSD e usarla per avviare il tuo Raspberry Pi.