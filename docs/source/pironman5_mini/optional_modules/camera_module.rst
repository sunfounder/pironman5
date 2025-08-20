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

In questa sezione imparerai come testare il modulo fotocamera catturando foto e registrando video.

Al termine di questa sezione, avrai un modulo fotocamera completamente installato e funzionante, pronto per i tuoi progetti.


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

