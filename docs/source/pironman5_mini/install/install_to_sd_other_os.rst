.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_sd_home_bridge_mini:

Installazione del sistema operativo su una scheda Micro SD
====================================================================

Se utilizzi una scheda Micro SD, puoi seguire il tutorial seguente per installare il sistema sulla tua scheda Micro SD.


**Componenti richiesti**

* Un computer personale
* Una scheda Micro SD e un lettore

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installare il sistema operativo sulla scheda microSD
--------------------------------------------------------------------------

1. Inserisci la scheda microSD nel computer utilizzando un lettore di schede.  
   Prima di procedere, esegui il backup di eventuali dati importanti presenti sulla scheda, poiché verranno cancellati.

   .. image:: img/insert_sd.png
      :width: 90%

2. Quando si apre **Raspberry Pi Imager**, vedrai la pagina **Device**.  
   Seleziona il tuo modello di **Raspberry Pi 5** dall’elenco.

   .. image:: img/imager_device.png
      :width: 90%

3. Vai alla sezione **OS**, scorri fino in fondo alla pagina e seleziona il tuo sistema operativo.

   .. note::

      * Per **Ubuntu**, fai clic su **Other general-purpose OS** → **Ubuntu**, quindi seleziona  
        **Ubuntu Desktop 24.04 LTS (64-bit)** oppure **Ubuntu Server 24.04 LTS (64-bit)**.
      * Per **Kali Linux**, **Home Assistant** e **Homebridge**, fai clic su  
        **Other specific-purpose OS**, quindi seleziona il sistema corrispondente.

   .. warning::

      Qualunque sistema tu scelga, assicurati di selezionare una versione a **64 bit**. Su un sistema a **32 bit**, alcuni pacchetti sono disponibili solo per ``aarch64`` (64 bit) e alcune funzionalità potrebbero non installarsi o non funzionare correttamente.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Nella sezione **Storage**, seleziona la tua scheda microSD.  
   Per sicurezza, si consiglia di scollegare altri dispositivi di archiviazione USB in modo che nell’elenco compaia solo la scheda microSD.

   .. image:: img/imager_storage.png
      :width: 90%

#. Fai clic su **NEXT**.

   .. note::

      * Per i sistemi che **non possono essere preconfigurati**, facendo clic su **NEXT** verrà saltato il passaggio di **Customisation** e si passerà direttamente a **Writing**, dove il sistema operativo viene scritto sulla scheda microSD.
      * Per i sistemi che **supportano la preconfigurazione**, segui i passaggi di **Customisation** per configurare opzioni come **Hostname**, **WiFi** e **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Quando appare il popup **“Write Successful”**, l’immagine è stata completamente scritta e verificata. Ora puoi rimuovere in sicurezza la scheda microSD e utilizzarla per avviare il tuo Raspberry Pi.
