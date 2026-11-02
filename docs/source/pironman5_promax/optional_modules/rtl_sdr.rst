.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


RTL-SDR Blog V4
==============================================

.. note::

    Die Pironman-5-Serienprodukte enthalten die folgenden Module nicht.
    Sie müssen eines selbst vorbereiten oder auf unserer offiziellen Website erwerben:

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

Diese Anleitung beschreibt ein zuverlässiges Installationsverfahren für den RTL-SDR Blog V4, einen beliebten und erschwinglichen USB-Software-defined-Radio (SDR)-Empfänger.
Die V4-Version verfügt über einen verbesserten R828D-Tuner, einen Direktabtastmodus, bessere Empfindlichkeit und einen integrierten Bias-T zur Stromversorgung aktiver Antennen.
Er eignet sich gut für den Empfang von UKW-Rundfunk, Flugfunk, Amateurfunk, ADS-B und vielen anderen Signalen unter Linux- und Raspberry-Pi-Systemen.

Die ursprüngliche Dokumentation des Herstellers finden Sie im offiziellen RTL-SDR Blog V4-Leitfaden: https://www.rtl-sdr.com/V4/

.. note::

    Es sind zwei Varianten im Umlauf: der **RTL-SDR Blog V4** und der **RTL-SDR Blog V4 Lite**.
    Sie haben unterschiedliche EEPROM-Produktstrings, daher meldet ``rtl_test`` entweder
    ``RTL-SDR Blog V4 Detected`` oder ``RTL-SDR Blog V4 Lite Detected``. Beide sind korrekt,
    und alle folgenden Schritte gelten für beide.

----

Treiber für RTL-SDR Blog V4 installieren
--------------------------------------------------------------------

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
    Die Ausgabe sollte ``RTL-SDR Blog V4 Detected`` enthalten und keine ``[R82XX] PLL not locked!``-Meldungen.
    Die Zeile ``Using device 0: Generic RTL2832U OEM`` ist normal – das ist nur der USB-Name.


**6. FM-Empfang von der Befehlszeile aus testen**

.. code-block:: shell

   # 1) Scan the FM band and find a frequency that has a station near you
   rtl_power -f 87.5M:108M:100k -i 3 -e 10 scan.csv

   # 2) Listen to one of the strongest ones (replace 104.9M with your own)
   #    Note: -M wbfm outputs the 180 kHz MPX, not 48 kHz audio, and -r is ignored.
   #    The playback rate must match -s, otherwise the audio plays at the wrong speed.
   rtl_fm -f 104.9M -M wbfm -s 180000 -g 28 | play -t raw -r 180k -e s -b 16 -c 1 -

Tipps:

    * ``-g``: Versuchen Sie Werte zwischen 25–35 dB; höher ist nicht immer besser.
    * Reduzieren Sie ``-s`` auf ~170k–180k, um Rauschen zu verringern.
    * Passen Sie die Frequenz leicht an (z.B. ``97.1005M``) für die Feineinstellung.
    * Schließen Sie andere SDR-Software, die das Gerät möglicherweise belegt.

----

Häufig verwendete Funksoftware installieren
-------------------------------------------------------------------

Dieser Abschnitt stellt vier weit verbreitete SDR-Anwendungen vor, mit kurzen Beschreibungen, Installationsanweisungen und grundlegenden Einrichtungstipps für Debian-basierte Systeme.

* :ref:`install_gqrx_promax`
* :ref:`install_sdrpp_promax`
* :ref:`install_rtl433_promax`
* :ref:`install_dump1090_promax`


----

.. _install_gqrx_promax:

GQRX
^^^^^^^^^^^^

GQRX ist eine einfache, benutzerfreundliche SDR-Empfängeranwendung mit grafischer Oberfläche. Es unterstützt eine Vielzahl von SDR-Geräten und ist ideal zum Hören von FM, AM, SSB und anderen Signalen mit Echtzeit-Spektrum- und Wasserfalldiagrammen.

Sie können auch die offizielle Raspberry-Pi-Installationsanleitung hier finden: https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Option 1 – Schnellinstallation (Empfohlen für die meisten Benutzer)**

Schnell, einfach und in Systemaktualisierungen integriert – ist aber möglicherweise nicht die neueste Version.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Option 2 – Aus dem Quellcode erstellen (Optional, neueste Funktionen)**

Stellt die neueste Version und vollständige Anpassbarkeit sicher, benötigt aber länger zum Kompilieren und erfordert mehr Abhängigkeiten.

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

**Treiber-Überschreibung verhindern**

Bei der Installation von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltetes ``librtlsdr`` neu installieren.
Überprüfen Sie nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führen Sie aus:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Sie können sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked!-Meldungen.

**Erstmalige Einrichtung**

* **I/O-Geräte**:

  * Gerät: ``RTL-SDR (V4)``.
  * Eingangsrate: ``1.8 MSPS`` (1800000).
  * Audio Output (Audioausgabe): Wähle deinen USB-Lautsprecher oder deine Soundkarte. Beim
    Raspberry Pi 5 ist die Standardausgabe oft HDMI — ein daran angeschlossener USB-Lautsprecher
    bleibt dann stumm.

* **Eingangssteuerung**:

  * **LNA-Verstärkung**: Beginnen Sie mit etwa 25–35 dB, passen Sie nach Bedarf an


* **Empfängeroptionen**:

  * Stellen Sie die Frequenzkorrektur (PPM) aus Ihrer Kalibrierung ein.
  * Modus: ``WFM (mono oder stereo)`` für UKW-Rundfunk.

----

.. _install_sdrpp_promax:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ ist ein moderner, schneller, plattformübergreifender Software-defined Radio (SDR)-Empfänger, der eine Vielzahl von Geräten unterstützt, einschließlich des RTL-SDR Blog V4. Es bietet eine übersichtliche, benutzerfreundliche Oberfläche, breite Modulationsunterstützung, erweiterte DSP-Filterung und Aufnahmefunktionen.

Das offizielle Benutzerhandbuch finden Sie hier: https://www.sdrpp.org/manual.pdf


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

**Treiber-Überschreibung verhindern**

Bei der Installation von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltetes ``librtlsdr`` neu installieren.
Überprüfen Sie nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führen Sie aus:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Sie können sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked!-Meldungen.


**Hinweise zum ersten Start:**

Nach der Installation erscheint SDR++ in Ihrem Desktop-Menü (normalerweise unter "Sonstige"), oder Sie können es ausführen mit:

   .. code-block:: shell

      sdrpp

* **Gerät:** Wählen Sie **RTL-SDR (V4)** im Menü **Source**.
* **Abtastrate:** 1,8 MSPS ist typisch; niedriger, wenn die CPU-Last hoch ist.
* **Verstärkung:** Deaktivieren Sie AGC und stellen Sie die manuelle Verstärkung ein (beginnen Sie mit ~35 dB).
* **PPM-Korrektur:** Geben Sie Ihren Kalibrierungswert von ``rtl_test -p`` ein.
* **Demodulationsmodus:** Wählen Sie WFM für UKW-Rundfunk, SSB für Amateurbänder usw.

----

.. _install_rtl433_promax:

rtl_433
^^^^^^^^^^^^


rtl_433 ist ein Befehlszeilenwerkzeug zum Dekodieren von Funkübertragungen von Geräten, die im 433-MHz-ISM-Band arbeiten, wie z.B. Wetterstationen, Reifendrucksensoren und drahtlosen Thermometern.

**Installieren:**

.. code-block:: shell

   sudo apt install -y rtl-433

**Treiber-Überschreibung verhindern**

Bei der Installation von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltetes ``librtlsdr`` neu installieren.
Überprüfen Sie nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führen Sie aus:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Sie können sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked!-Meldungen.

**Grundlegende Verwendung:**

* Führen Sie ``rtl_433`` aus, um gängige 433-MHz-Geräte automatisch zu erkennen und zu dekodieren.
* Führe ``rtl_433 -R`` ohne Argument aus, um alle unterstützten Protokolle aufzulisten.
  Die ältere Option ``-G`` listet sie nicht mehr; sie ist seit 25.02 veraltet.

----

.. _install_dump1090_promax:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability ist ein Mode-S-Decoder für ADS-B-Flugzeugtransponderdaten. Es empfängt und dekodiert Flugzeugpositionen, Geschwindigkeiten und andere Flugdaten und kann eine Live-Karte über einen Webbrowser bereitstellen.

**Installieren:**

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

**Treiber-Überschreibung verhindern**

Bei der Installation von GQRX, SDR++, gnuradio-dev oder gr-osmosdr kann das System veraltetes ``librtlsdr`` neu installieren.
Überprüfen Sie nach jeder Installation:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Wenn es nicht mehr auf ``/usr/local/lib/librtlsdr.so`` zeigt, führen Sie aus:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Sie können sofort testen (oder nach einem Neustart für eine saubere Umgebung):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Erwartete Ausgabe:

   * Enthält RTL-SDR Blog V4 Detected.
   * Keine [R82XX] PLL not locked!-Meldungen.

**Grundlegende Verwendung:**

* Führen Sie aus: ``dump1090 --interactive --net``.
* Öffnen Sie ``http://<raspberrypi-ip>:8080`` in Ihrem Browser, um die Live-Flugzeugverfolgung anzuzeigen.