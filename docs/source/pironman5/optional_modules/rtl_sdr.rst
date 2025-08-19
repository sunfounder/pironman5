.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Enthusiasten tiefer in Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!


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

----

Treiber für RTL-SDR Blog V4 installieren
--------------------------------------------------

**0. Vorbereitung**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

Hinweis:  
    ``sox`` (stellt den Befehl ``play`` bereit) ist für direkte Audiotests enthalten.

**1. Vollständige Bereinigung alter Bibliotheken und Binärdateien (kritisch)**

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

Verifizierung A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: No librtlsdr found in system cache."

**2. RTL-SDR Blog V4 Treiber bauen und installieren**

.. code-block:: shell

   cd ~
   git clone https://github.com/rtlsdrblog/rtl-sdr-blog.git
   cd rtl-sdr-blog
   mkdir build && cd build
   cmake .. -DINSTALL_UDEV_RULES=ON
   make
   sudo make install
   sudo cp ../rtl-sdr.rules /etc/udev/rules.d/
   sudo ldconfig

Verifizierung B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Sollte auf /usr/local/lib/librtlsdr.so zeigen

**3. DVB-Kernelmodul deaktivieren und neu starten**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

Hinweis:  
    Sofortige Reload-Befehle (``udevadm control --reload-rules`` und ``udevadm trigger``)  
    sind optional, wenn du ohnehin sofort neu startest.

**4. Treiber nach dem Neustart überprüfen**

.. code-block:: shell

   rtl_test -t

Erwartet:  
    Die Ausgabe sollte ``RTL-SDR Blog V4 Detected`` enthalten, ohne ``[R82XX] PLL not locked!`` Meldungen.  
    Die Zeile ``Using device 0: Generic RTL2832U OEM`` ist normal — das ist nur der USB-Name.


**6. UKW-Empfang von der Kommandozeile testen**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

Tipps:

    * ``-g``: Versuche Werte zwischen 25–35 dB; höher ist nicht immer besser.
    * Reduziere ``-s`` auf ~170k–180k, um Rauschen zu verringern.
    * Passe die Frequenz leicht an (z. B. ``97.1005M``) für Feintuning.
    * Schließe andere SDR-Software, die das Gerät blockieren könnte.

----

Installation gängiger Radio-Software
------------------------------------------------

In diesem Abschnitt werden vier weit verbreitete SDR-Anwendungen vorgestellt, mit kurzen Beschreibungen, Installationsanweisungen und grundlegenden Einrichtungstipps für Debian-basierte Systeme.

* :ref:`install_gqrx`
* :ref:`install_sdrpp`
* :ref:`install_rtl433`
* :ref:`install_dump1090`


----

.. _install_gqrx:

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

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Du kannst sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked! Meldungen.

**Ersteinrichtung**

* **I/O-Geräte**:

  * Gerät: ``RTL-SDR (V4)``.
  * Eingaberate: ``1.8 MSPS`` (1800000).

* **Eingabesteuerung**:

  * **LNA Gain**: Beginne bei etwa 25–35 dB und passe nach Bedarf an.

* **Empfängeroptionen**:

  * Frequenzkorrektur (PPM) aus deiner Kalibrierung setzen.
  * Modus: ``WFM (mono oder stereo)`` für UKW-Rundfunk.

----

.. _install_sdrpp:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ ist ein modernes, schnelles, plattformübergreifendes Software-defined-Radio-(SDR)-Programm, das eine Vielzahl von Geräten unterstützt, darunter auch den RTL-SDR Blog V4. Es bietet eine klare, benutzerfreundliche Oberfläche, breite Modulationsunterstützung, erweiterte DSP-Filterung und Aufzeichnungsfunktionen.

Das offizielle Benutzerhandbuch findest du hier: https://www.sdrpp.org/manual.pdf

**Aus dem Quellcode installieren**

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends build-essential cmake git pkg-config \
     libfftw3-dev libvolk2-dev libglfw3-dev libglew-dev \
     libzstd-dev librtaudio-dev

   git clone https://github.com/AlexandreRouma/SDRPlusPlus
   cd SDRPlusPlus
   mkdir build && cd build
   cmake .. -DOPT_BUILD_RTL_SDR_SOURCE=ON
   make
   sudo make install

**Verhindern von Treiberüberschreibungen**

Beim Installieren von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltete ``librtlsdr`` neu installieren.  
Überprüfe nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führe aus:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Du kannst sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

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

.. _install_rtl433:

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

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Du kannst sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked! Meldungen.

**Grundlegende Nutzung:**

* Führe ``rtl_433`` aus, um automatisch gängige 433-MHz-Geräte zu erkennen und zu dekodieren.
* Verwende ``rtl_433 -G``, um alle unterstützten Protokolle anzuzeigen.

----

.. _install_dump1090:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability ist ein Mode-S-Decoder für ADS-B-Flugtransponderdaten. Er empfängt und dekodiert Flugzeugpositionen, Geschwindigkeiten und andere Flugdaten und kann eine Live-Karte über den Webbrowser bereitstellen.

**Installation:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**Verhindern von Treiberüberschreibungen**

Beim Installieren von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltete ``librtlsdr`` neu installieren.  
Überprüfe nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führe aus:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Du kannst sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked! Meldungen.

**Grundlegende Nutzung:**

* Starte: ``dump1090 --interactive --net``.
* Öffne ``http://<raspberrypi-ip>:8080`` in deinem Browser, um das Live-Flugtracking anzuzeigen.



