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

In diesem Abschnitt lernst du:

* Den Pironman 5 auseinanderzubauen.  
* Das Kameramodul am Raspberry Pi 5 zu installieren.  
* Das Gehäuse wieder zusammenzubauen.  
* Das Kameramodul durch das Aufnehmen von Fotos und Videos zu testen.

Am Ende dieses Abschnitts wirst du ein vollständig installiertes und funktionsfähiges Kameramodul für deine Projekte haben.

Kameramodul montieren
------------------------------------

Folge diesen Schritten, um das Kameramodul zu montieren:

1. Entferne die beiden Acrylplatten vom Gehäuse.

   .. image:: img/IN.CMR.1.png
      :align: center

2. Trenne das 2-Pin-Kabel und das FPC wie im Bild gezeigt.

   .. image:: img/IN.CMR.2.png
      :align: center

3. Schraube die vier Schrauben ab, um die NVMe PIP- und Power-Switch-Converter-Modulgruppe zu entfernen.

   .. image:: img/IN.CMR.3.png
      :align: center

4. Zerlege die Modulgruppe. Dies beinhaltet das Entfernen eines Niets, indem du die zentrale Achse des Niets mit einem Schraubendreher herausdrückst und dann den gesamten Niet entfernst.

   .. image:: img/IN.CMR.4.png
      :align: center

5. Verbinde das Kameramodul mit dem FPC-Kabel.

   .. image:: img/IN.CMR.5.png
      :align: center

6. Führe das FPC durch das CAMERA-Loch im Gehäuse.

   .. image:: img/IN.CMR.6.png
      :align: center

7. Führe das FPC weiter durch das CAMERA-Loch im Gehäuse.

   .. image:: img/IN.CMR.7.png
      :align: center

8. Verbinde das FPC mit dem Raspberry Pi. Dieser Schritt ist sehr eng und erfordert sorgfältiges Arbeiten.

   .. image:: img/IN.CMR.8.png
      :align: center

9. Schalte den Raspberry Pi 5 ein und überprüfe, ob das Kameramodul richtig angeschlossen ist.

   * Verbinde zuerst ein Display mit dem Raspberry Pi oder stelle eine VNC-Verbindung her.
   * Nach dem Hochfahren ins System führe den folgenden Befehl aus, um zu prüfen, ob die Kamera funktioniert: ``libcamera-hello``
   * Wenn du ein Vorschaufenster siehst, funktioniert die Kamera korrekt.

10. Baue den Power Switch Converter wieder in das Gehäuse ein.

   .. image:: img/IN.CMR.9.png
      :align: center

   .. image:: img/IN.CMR.10.png
      :align: center

11. Baue die NVMe PIP wieder in das Gehäuse ein.

   .. image:: img/IN.CMR.11.png
      :align: center

   .. image:: img/IN.CMR.12.png
      :align: center

12. Baue die Gehäuseabdeckung wieder zusammen.

   .. image:: img/IN.CMR.13.png
      :align: center


Kameramodul verwenden
---------------------------

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

Installiere die Abhängigkeiten:

.. code-block:: bash

    sudo apt install python3-picamera2 -y

Erstelle eine Python-Datei:

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
