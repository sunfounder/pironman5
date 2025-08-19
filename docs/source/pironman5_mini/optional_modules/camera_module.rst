.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Enthusiasten tiefer in Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!


Kameramodul
===========================================

.. note::

    Die Pironman-5-Serie enthält kein Kameramodul.  
    Du musst eines selbst vorbereiten oder auf unserer offiziellen Website kaufen:

    * `Kameramodul <https://www.sunfounder.com/products/ov5647-camera-module>`_

In diesem Abschnitt lernst du, wie du das Kameramodul testest, indem du Fotos aufnimmst und Videos aufzeichnest.

Am Ende dieses Abschnitts wirst du ein vollständig installiertes und funktionsfähiges Kameramodul für deine Projekte haben.


**Kamera testen**

Raspberry Pi OS (Bookworm und neuer) verwendet den **libcamera**-Stack.  
Nach dem Hochfahren ins System führe den folgenden Befehl aus, um zu prüfen, ob die Kamera funktioniert:

.. code-block:: bash

    libcamera-hello

Wenn du ein Vorschaufenster siehst, funktioniert die Kamera korrekt.

**Ein Foto aufnehmen**

.. code-block:: bash

    libcamera-jpeg -o test.jpg

Dies nimmt ein Standbild auf und speichert es als ``test.jpg``.

**Ein Video aufnehmen**

.. code-block:: bash

    libcamera-vid -t 10000 -o test.h264

* ``-t 10000`` bedeutet 10 Sekunden Aufnahme.
* ``-o test.h264`` speichert die Ausgabe als H.264-Video.

Um das Video ins MP4-Format zu konvertieren:

.. code-block:: bash

    ffmpeg -i test.h264 -c copy test.mp4

**Python-Beispiel**

Du kannst die Kamera auch mit Python über die Bibliothek ``picamera2`` steuern.

Abhängigkeiten installieren:

.. code-block:: bash

    sudo apt install python3-picamera2 -y

Eine Python-Datei erstellen:

.. code-block:: bash

    nano camera_test.py

Füge dann den folgenden Code ein:

.. code-block:: python

    from picamera2 import Picamera2
    import time

    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)
    picam2.capture_file("image.jpg")

Speichere und beende nano mit ``CTRL+O``, dann ``ENTER`` und ``CTRL+X``.

Führe das Skript aus:

.. code-block:: bash

    python3 camera_test.py
