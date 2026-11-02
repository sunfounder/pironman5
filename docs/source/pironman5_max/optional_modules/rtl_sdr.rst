.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


RTL-SDR Blog V4
==============================================

.. note::

    Die Produkte der Pironman-5-Serie enthalten die folgenden Module nicht.  
    Du musst eines selbst vorbereiten oder auf unserer offiziellen Website kaufen:

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

Diese Anleitung beschreibt ein zuverlässiges Installationsverfahren für den RTL-SDR Blog V4, einen beliebten und erschwinglichen USB-Software-defined-Radio-(SDR)-Empfänger.  
Die V4-Version verfügt über einen verbesserten R828D-Tuner, Direct-Sampling-Modus, bessere Empfindlichkeit und ein integriertes Bias-Tee zur Versorgung aktiver Antennen.  
Er eignet sich gut zum Empfang von UKW-Rundfunk, Airband, Amateurfunk, ADS-B und vielen weiteren Signalen unter Linux- und Raspberry-Pi-Systemen.

Die Originaldokumentation des Herstellers findest du im offiziellen RTL-SDR Blog V4 Guide: https://www.rtl-sdr.com/V4/

.. note::

    Es sind zwei Varianten im Umlauf: der **RTL-SDR Blog V4** und der **RTL-SDR Blog V4 Lite**.
    Sie haben unterschiedliche EEPROM-Produktstrings, daher meldet ``rtl_test`` entweder
    ``RTL-SDR Blog V4 Detected`` oder ``RTL-SDR Blog V4 Lite Detected``. Beide sind korrekt,
    und alle folgenden Schritte gelten für beide.

----

Treiber für RTL-SDR Blog V4 installieren
------------------------------------------------

Unter Linux ist das Vorgehen ebenfalls einfach: alte RTL-SDR-Treiber entfernen und eine aktualisierte Version installieren.

**1. Alten Treiber entfernen**

.. code-block:: shell

   sudo apt purge ^librtlsdr
   sudo rm -rvf /usr/lib/librtlsdr* /usr/include/rtl-sdr* /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* /usr/local/include/rtl_* /usr/local/bin/rtl_*

Verifizierung A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: Kein librtlsdr im System-Cache gefunden."

**2. Neueste Treiber installieren**

.. code-block:: shell

   sudo apt-get install libusb-1.0-0-dev git cmake pkg-config build-essential
   git clone https://github.com/osmocom/rtl-sdr
   cd rtl-sdr
   mkdir build
   cd build
   cmake ../ -DINSTALL_UDEV_RULES=ON
   make
   sudo make install
   sudo cp ../rtl-sdr.rules /etc/udev/rules.d/
   sudo ldconfig

Hinweis:
    Wenn zusätzlich der FM-Empfang über die Kommandozeile getestet werden soll (siehe unten),
    wird ``sox`` benötigt, das den Befehl ``play`` bereitstellt:

    .. code-block:: shell

       sudo apt install -y sox

Verifizierung B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Sollte auf /usr/local/lib/librtlsdr.so zeigen

**3. DVB-T-TV-Treiber blacklisten**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

**4. Neustart**

.. code-block:: shell

   sudo reboot

**5. Treiber nach dem Neustart überprüfen**

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartet:  
    Die Ausgabe sollte ``RTL-SDR Blog V4 Detected`` enthalten, ohne ``[R82XX] PLL not locked!`` Meldungen.  
    Die Zeile ``Using device 0: Generic RTL2832U OEM`` ist normal — das ist nur der USB-Name.


**6. UKW-Empfang von der Kommandozeile testen**

.. code-block:: shell

   # 1) Scan the FM band and find a frequency that has a station near you
   rtl_power -f 87.5M:108M:100k -i 3 -e 10 scan.csv

   # 2) Listen to one of the strongest ones (replace 104.9M with your own)
   #    Note: -M wbfm outputs the 180 kHz MPX, not 48 kHz audio, and -r is ignored.
   #    The playback rate must match -s, otherwise the audio plays at the wrong speed.
   rtl_fm -f 104.9M -M wbfm -s 180000 -g 28 | play -t raw -r 180k -e s -b 16 -c 1 -

Tipps:

    * ``-g``: Versuche Werte zwischen 25–35 dB; höher ist nicht immer besser.
    * Reduziere ``-s`` auf ~170k–180k, um Rauschen zu verringern.
    * Passe die Frequenz leicht an (z. B. ``97.1005M``) für Feintuning.
    * Schließe andere SDR-Software, die das Gerät blockieren könnte.

----

Installation gängiger Radio-Software
---------------------------------------

In diesem Abschnitt werden vier weit verbreitete SDR-Anwendungen vorgestellt, mit kurzen Beschreibungen, Installationsanweisungen und grundlegenden Einrichtungstipps für Debian-basierte Systeme.

* :ref:`install_gqrx_max`
* :ref:`install_sdrpp_max`
* :ref:`install_rtl433_max`
* :ref:`install_dump1090_max`


----

.. _install_gqrx_max:

GQRX
^^^^^^^^^^^^

GQRX ist eine einfache, benutzerfreundliche SDR-Empfängeranwendung mit grafischer Oberfläche. Sie unterstützt eine Vielzahl von SDR-Geräten und eignet sich ideal zum Hören von FM, AM, SSB und anderen Signalen mit Echtzeit-Spektrum- und Wasserfalldarstellung.

Du kannst auch den offiziellen Raspberry-Pi-Installationsleitfaden hier einsehen: https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Option 1 – Schnelle Installation (Empfohlen für die meisten Nutzer)**

Schnell, einfach und integriert in Systemupdates – möglicherweise jedoch nicht die neueste Version.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Option 2 – Aus dem Quellcode kompilieren (Optional, neueste Funktionen)**

Stellt sicher, dass du die neueste Version und volle Anpassungsmöglichkeiten erhältst, benötigt jedoch längere Kompilierzeit und mehr Abhängigkeiten.

.. code-block:: shell

   sudo apt update

   sudo apt-get install -y --no-install-recommends \
     cmake gnuradio-dev gr-osmosdr qt6-base-dev qt6-svg-dev \
     libasound2-dev libjack-jackd2-dev portaudio19-dev libpulse-dev

   git clone https://github.com/gqrx-sdr/gqrx.git
   cd gqrx
   mkdir build && cd build
   cmake ..
   make
   sudo make install

**Verhindern von Treiberüberschreibungen**

Beim Installieren von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltete ``librtlsdr`` neu installieren.  
Überprüfe nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führe aus:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Du kannst sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked! Meldungen.

**Ersteinrichtung**

* **I/O-Geräte**:

  * Gerät: ``RTL-SDR (V4)``.
  * Eingaberate: ``1.8 MSPS`` (1800000).
  * Audio Output (Audioausgabe): Wähle deinen USB-Lautsprecher oder deine Soundkarte. Beim
    Raspberry Pi 5 ist die Standardausgabe oft HDMI — ein daran angeschlossener USB-Lautsprecher
    bleibt dann stumm.

* **Eingabesteuerung**:

  * **LNA Gain**: Beginne bei etwa 25–35 dB und passe nach Bedarf an.

* **Empfängeroptionen**:

  * Frequenzkorrektur (PPM) aus deiner Kalibrierung setzen.
  * Modus: ``WFM (mono oder stereo)`` für UKW-Rundfunk.

----

.. _install_sdrpp_max:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ ist ein modernes, schnelles, plattformübergreifendes Software-defined-Radio-(SDR)-Programm, das eine Vielzahl von Geräten unterstützt, darunter auch den RTL-SDR Blog V4. Es bietet eine klare, benutzerfreundliche Oberfläche, breite Modulationsunterstützung, erweiterte DSP-Filterung und Aufzeichnungsfunktionen.

Das offizielle Benutzerhandbuch findest du hier: https://www.sdrpp.org/manual.pdf

**Aus dem Quellcode installieren**

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends build-essential cmake git pkg-config \
     libfftw3-dev libvolk-dev libglfw3-dev libglew-dev \
     libzstd-dev librtaudio-dev

   git clone https://github.com/AlexandreRouma/SDRPlusPlus
   cd SDRPlusPlus
   mkdir build && cd build
   cmake .. -DOPT_BUILD_RTL_SDR_SOURCE=ON
   make
   sudo make install

.. note::

   Ab Debian 13 (trixie) heißt das Paket ``libvolk-dev``. Unter Debian 12 (bookworm) — und
   damit auch unter dem darauf basierenden Raspberry Pi OS — heißt es ``libvolk2-dev``; mit
   dem falschen Namen meldet ``apt`` *Unable to locate package*.

**Verhindern von Treiberüberschreibungen**

Beim Installieren von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltete ``librtlsdr`` neu installieren.  
Überprüfe nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führe aus:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Du kannst sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked! Meldungen.

**Hinweise beim ersten Start:**

Nach der Installation erscheint SDR++ im Desktopmenü (meist unter "Sonstiges"), oder du kannst es starten mit:

   .. code-block:: shell

      sdrpp

* **Gerät:** Wähle **RTL-SDR (V4)** im Menü **Source**.
* **Abtastrate:** 1.8 MSPS ist typisch; reduziere sie, wenn die CPU-Last hoch ist.
* **Gain:** AGC deaktivieren und manuell einstellen (beginne bei ~35 dB).
* **PPM-Korrektur:** Gib deinen Kalibrierungswert von ``rtl_test -p`` ein.
* **Demodulationsmodus:** Wähle WFM für UKW-Rundfunk, SSB für Amateurfunkbänder etc.

----

.. _install_rtl433_max:

rtl_433
^^^^^^^^^^^^

rtl_433 ist ein Kommandozeilen-Tool zum Dekodieren von Funksignalen von Geräten im 433-MHz-ISM-Band, wie Wetterstationen, Reifendrucksensoren und drahtlosen Thermometern.

**Installation:**

.. code-block:: shell

   sudo apt install -y rtl-433

**Verhindern von Treiberüberschreibungen**

Beim Installieren von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltete ``librtlsdr`` neu installieren.  
Überprüfe nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führe aus:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Du kannst sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked! Meldungen.

**Grundlegende Nutzung:**

* Führe ``rtl_433`` aus, um automatisch gängige 433-MHz-Geräte zu erkennen und zu dekodieren.
* Führe ``rtl_433 -R`` ohne Argument aus, um alle unterstützten Protokolle aufzulisten.
  Die ältere Option ``-G`` listet sie nicht mehr; sie ist seit 25.02 veraltet.

----

.. _install_dump1090_max:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability ist ein Mode-S-Decoder für ADS-B-Flugtransponderdaten. Er empfängt und dekodiert Flugzeugpositionen, Geschwindigkeiten und andere Flugdaten und kann eine Live-Karte über den Webbrowser bereitstellen.

**Installation:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

.. note::

   ``dump1090-mutability`` ist in Debian 12 (bookworm), bullseye und älter verfügbar,
   **nicht aber in Debian 13 (trixie)** — das Paket wurde aus dem Archiv entfernt, ``apt``
   meldet *Unable to locate package dump1090-mutability*.

   Unter Debian 13 gibt es dafür keinen direkten Ersatz im Archiv: Das Paket ``readsb`` ist
   **ohne** RTL-SDR-Unterstützung gebaut (``readsb --device-type rtlsdr`` antwortet *SDR type
   'rtlsdr' not recognized*). Auf solchen Systemen muss der Decoder aus dem Quellcode gebaut
   werden — zum Beispiel ``readsb`` mit ``make RTLSDR=yes`` oder ``dump1090-fa``.

**Verhindern von Treiberüberschreibungen**

Beim Installieren von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltete ``librtlsdr`` neu installieren.  
Überprüfe nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führe aus:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Du kannst sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked! Meldungen.

**Grundlegende Nutzung:**

* Starte: ``dump1090 --interactive --net``.
* Öffne ``http://<raspberrypi-ip>:8080`` in deinem Browser, um das Live-Flugtracking anzuzeigen.



