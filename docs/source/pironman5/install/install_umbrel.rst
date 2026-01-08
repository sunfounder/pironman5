.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!


Installazione di Umbrel OS
============================================

Umbrel è una piattaforma/sistema operativo open-source e self-hosted per home server che ti consente di gestire il tuo nodo Bitcoin, installare una varietà di app self-hosted con un solo clic e trasformare il tuo hardware nel tuo cloud domestico personale. È un ottimo punto di partenza per l’autocustodia e la tutela della privacy.

**Componenti richiesti**

* Un computer personale
* Un SSD NVMe
* Un adattatore NVMe a USB
* Scheda Micro SD e lettore

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installare il sistema operativo sull’SSD NVMe
-----------------------------------------------------------

Ora sei pronto per installare il sistema operativo sul tuo **SSD NVMe**.  
Segui attentamente i passaggi riportati di seguito — questa guida è pensata per i principianti ed è facile da seguire.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Rilasci di Umbrel OS</a>

#. Scarica l’ultima immagine di **Umbrel OS** ed estrai il file. Se desideri utilizzare una versione specifica, puoi anche visitare la pagina |link_umbrel_release|.

   * :download:`Ultima immagine di Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Inserisci l’**SSD NVMe** nel computer utilizzando un **adattatore NVMe a USB**.

#. Apri **Raspberry Pi Imager**. Nella schermata **Device**, seleziona il tuo modello di **Raspberry Pi 5** dall’elenco.

   .. image:: img/imager_device.png
      :width: 90%

#. Vai alla sezione **OS**, scorri fino in fondo e seleziona **Use custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Seleziona il **file immagine di Umbrel OS** che hai scaricato ed estratto in precedenza, quindi fai clic su **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Fai clic su **Next** per continuare.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. Nella sezione **Storage**, seleziona il tuo **SSD NVMe**. Assicurati di scegliere l’SSD NVMe e non un’altra unità presente sul computer.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Rivedi attentamente tutte le impostazioni, quindi fai clic su **WRITE**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. Se l’SSD NVMe contiene già dei dati, Raspberry Pi Imager mostrerà un avviso indicando che tutti i dati verranno cancellati. Verifica di aver selezionato l’unità corretta, quindi fai clic su **I UNDERSTAND, ERASE AND WRITE**.

   .. image:: img/imager_erase.png
      :width: 90%

#. Quando appare il messaggio **“Write Complete”**, l’immagine è stata scritta e verificata correttamente.

   .. image:: img/imager_umbrel_finish.png
      :width: 90%

