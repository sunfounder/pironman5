.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_other_mini:

Installazione del sistema operativo su un SSD NVMe
===========================================================

Se utilizzi un SSD NVMe e disponi di un adattatore per collegare l’SSD NVMe al computer per l’installazione del sistema, puoi seguire il tutorial seguente per un’installazione rapida.

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Componenti richiesti**

* Un computer personale
* Un SSD NVMe
* Un adattatore NVMe a USB
* Scheda Micro SD e lettore

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installare il sistema operativo sulla scheda microSD
------------------------------------------------------------------

#. Inserisci l’**SSD NVMe** nel computer utilizzando un adattatore.

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

   .. image:: img/imager_other_os.png
      :width: 90%

4. Nella sezione **Storage**, seleziona il tuo **SSD NVMe**. 

   .. image:: img/nvme_storage.png
      :width: 90%

#. Fai clic su **NEXT**.

   .. note::

      * Per i sistemi che **non possono essere preconfigurati**, facendo clic su **NEXT** verrà saltato il passaggio di **Customisation** e si passerà direttamente a **Writing**, dove il sistema operativo viene scritto sulla scheda microSD.
      * Per i sistemi che **supportano la preconfigurazione**, segui i passaggi di **Customisation** per configurare opzioni come **Hostname**, **WiFi** e **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Quando appare il popup **“Write Successful”**, l’immagine è stata completamente scritta e verificata. Ora puoi rimuovere in sicurezza la scheda microSD e utilizzarla per avviare il tuo Raspberry Pi.
