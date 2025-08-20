.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Modulo Fotocamera
====================

.. note::

    La serie Pironman 5 non include un modulo fotocamera.  
    Dovrai procurartene uno oppure acquistarlo dal nostro sito ufficiale:

    * `Modulo Fotocamera <https://www.sunfounder.com/products/ov5647-camera-module>`_

In questa sezione imparerai a:

* Smontare il Pironman 5.  
* Installare il modulo fotocamera sul Raspberry Pi 5.  
* Rimontare il case.  
* Testare il modulo fotocamera catturando foto e registrando video.

Al termine di questa sezione, avrai un modulo fotocamera completamente installato e funzionante, pronto per i tuoi progetti.

Assemblaggio del Modulo Fotocamera
------------------------------------

Segui questi passaggi per assemblare il Modulo Fotocamera:

1. Rimuovi i due pannelli in acrilico dal case.

   .. image:: img/IN.CMR.1.png
      :align: center

2. Scollega il cavo a 2 pin e l’FPC come mostrato nell’immagine.

   .. image:: img/IN.CMR.2.png
      :align: center

3. Svita le quattro viti per rimuovere il gruppo NVMe PIP e Power Switch Converter.

   .. image:: img/IN.CMR.3.png
      :align: center

4. Smonta il gruppo di moduli. Questo comporta la rimozione di un rivetto, che deve essere eseguita spingendo fuori l’asta centrale del rivetto con un cacciavite, quindi rimuovendo l’intero rivetto.

   .. image:: img/IN.CMR.4.png
      :align: center

5. Collega il Modulo Fotocamera al cavo FPC.

   .. image:: img/IN.CMR.5.png
      :align: center

6. Fai passare l’FPC attraverso il foro CAMERA del case.

   .. image:: img/IN.CMR.6.png
      :align: center

7. Continua a far passare l’FPC attraverso il foro CAMERA del case.

   .. image:: img/IN.CMR.7.png
      :align: center

8. Collega l’FPC al Raspberry Pi. Questo passaggio è molto compatto e richiede una manipolazione accurata.

   .. image:: img/IN.CMR.8.png
      :align: center

9. Accendi il Raspberry Pi 5 e verifica se il Modulo Fotocamera è collegato correttamente.

   * Per prima cosa, collega un display al Raspberry Pi o stabilisci una connessione VNC.
   * Dopo l’avvio del sistema, esegui il seguente comando per verificare il funzionamento della fotocamera: ``libcamera-hello``  
   * Se vedi una finestra di anteprima, la fotocamera funziona correttamente.

10. Rimonta il Power Switch Converter all’interno del case.

   .. image:: img/IN.CMR.9.png
      :align: center

   .. image:: img/IN.CMR.10.png
      :align: center

11. Rimonta l’NVMe PIP all’interno del case.

   .. image:: img/IN.CMR.11.png
      :align: center

   .. image:: img/IN.CMR.12.png
      :align: center

12. Rimonta il coperchio del case.

   .. image:: img/IN.CMR.13.png
      :align: center


Utilizzare il Modulo Fotocamera
---------------------------------------

**Testare la Fotocamera**

Raspberry Pi OS (Bookworm e successivi) utilizza lo stack **libcamera**.  
Dopo l’avvio del sistema, esegui il seguente comando per verificare se la fotocamera funziona:

.. code-block:: bash

    libcamera-hello

Se visualizzi una finestra di anteprima, la fotocamera funziona correttamente.

**Scattare una Foto**

.. code-block:: bash

    libcamera-jpeg -o test.jpg

Questo comando catturerà un’immagine statica e la salverà come ``test.jpg``.

**Registrare un Video**

.. code-block:: bash

    libcamera-vid -t 10000 -o test.h264

* ``-t 10000`` indica una registrazione di 10 secondi.  
* ``-o test.h264`` salva l’output come video in formato H.264.

Per convertire il video in formato MP4:

.. code-block:: bash

    ffmpeg -i test.h264 -c copy test.mp4

**Esempio in Python**

Puoi anche controllare la fotocamera con Python utilizzando la libreria ``picamera2``.

Installa le dipendenze:

.. code-block:: bash

    sudo apt install python3-picamera2 -y

Crea un file Python:

.. code-block:: bash

    nano camera_test.py

Poi incolla il seguente codice:

.. code-block:: python

    from picamera2 import Picamera2
    import time

    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)
    picam2.capture_file("image.jpg")

Salva ed esci da nano premendo ``CTRL+O``, poi ``ENTER``, e infine ``CTRL+X``.

Esegui lo script:

.. code-block:: bash

    python3 camera_test.py

