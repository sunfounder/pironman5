.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


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

