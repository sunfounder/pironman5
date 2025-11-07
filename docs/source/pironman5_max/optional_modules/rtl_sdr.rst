.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

RTL-SDR Blog V4
==============================================

.. note::

    I prodotti della serie Pironman 5 non includono i seguenti moduli.  
    Devi procurartene uno autonomamente oppure acquistarlo dal nostro sito ufficiale:

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

Questa guida illustra una procedura affidabile di installazione per l’RTL-SDR Blog V4, un ricevitore radio definito dal software (SDR) USB popolare ed economico.  
La versione V4 presenta un sintonizzatore R828D migliorato, modalità di campionamento diretto, maggiore sensibilità e bias-tee integrato per alimentare antenne attive.  
Funziona bene per ricevere FM broadcast, airband, radioamatori, ADS-B e molti altri segnali su sistemi Linux e Raspberry Pi.

Per la documentazione originale del produttore, consulta la guida ufficiale RTL-SDR Blog V4: https://www.rtl-sdr.com/V4/

----

Installazione Driver per RTL-SDR Blog V4
---------------------------------------------

**0. Preparazione**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

Nota:  
    ``sox`` (fornisce il comando ``play``) è incluso per test audio diretti.

**1. Pulizia Completa di Librerie e Binari Vecchi (Critico)**

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

Verifica A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: Nessuna librtlsdr trovata nella cache di sistema."

**2. Compilare e Installare il Driver RTL-SDR Blog V4**

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

Verifica B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Dovrebbe puntare a /usr/local/lib/librtlsdr.so

**3. Disabilitare il Modulo Kernel DVB e Riavviare**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

Nota:  
    I comandi di ricarica immediata (``udevadm control --reload-rules`` e ``udevadm trigger``)  
    sono opzionali se prevedi di riavviare subito.

**4. Verifica del Driver Dopo il Riavvio**

.. code-block:: shell

   rtl_test -t

Atteso:  
    L’output dovrebbe includere ``RTL-SDR Blog V4 Detected`` senza messaggi ``[R82XX] PLL not locked!``.  
    La riga ``Using device 0: Generic RTL2832U OEM`` è normale — è solo il nome USB.

**6. Test Ricezione FM da Riga di Comando**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

Suggerimenti:

    * ``-g``: Prova tra 25–35 dB; valori più alti non sono sempre migliori.
    * Riduci ``-s`` a ~170k–180k per diminuire il rumore.
    * Regola leggermente la frequenza (es. ``97.1005M``) per una sintonia fine.
    * Chiudi qualsiasi altro software SDR che potrebbe mantenere il dispositivo occupato.

----

Installazione Software Radio Comune
-------------------------------------

Questa sezione introduce quattro applicazioni SDR ampiamente utilizzate, con brevi descrizioni, istruzioni di installazione e suggerimenti di configurazione di base per sistemi basati su Debian.

* :ref:`install_gqrx_max`
* :ref:`install_sdrpp_max`
* :ref:`install_rtl433_max`
* :ref:`install_dump1090_max`


----

.. _install_gqrx_max:

GQRX
^^^^^^^^^^^^

GQRX è un’applicazione SDR ricevitore semplice e intuitiva con interfaccia grafica. Supporta un’ampia gamma di dispositivi SDR ed è ideale per ascoltare FM, AM, SSB e altri segnali con spettro in tempo reale e visualizzazioni waterfall.

Puoi anche fare riferimento alla guida ufficiale di installazione per Raspberry Pi qui: https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Opzione 1 – Installazione Rapida (Raccomandata per la maggior parte degli utenti)**

Veloce, semplice e integrata con gli aggiornamenti di sistema — ma potrebbe non essere la versione più recente.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Opzione 2 – Compilazione da Sorgente (Opzionale, Ultime Funzionalità)**

Garantisce la versione più recente e piena personalizzazione, ma richiede più tempo per la compilazione e più dipendenze.

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

**Prevenire la Sovrascrittura dei Driver**

Quando installi GQRX, SDR++, gnuradio-dev o gr-osmosdr, il sistema potrebbe reinstallare una versione obsoleta di ``librtlsdr``.  
Dopo ogni installazione, controlla:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Se non punta più a ``/usr/local/lib/librtlsdr.so``, esegui:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Puoi testare immediatamente (o dopo un riavvio per un ambiente pulito):

.. code-block:: shell

   rtl_test -t

Output atteso:

   * Contiene RTL-SDR Blog V4 Detected.
   * Nessun messaggio [R82XX] PLL not locked!.

**Prima Configurazione**

* **Dispositivi I/O**:

  * Dispositivo: ``RTL-SDR (V4)``.
  * Frequenza di Campionamento: ``1.8 MSPS`` (1800000).

* **Controlli di Input**:

  * **LNA Gain**: Inizia da circa 25–35 dB, regola se necessario.


* **Opzioni del Ricevitore**:

  * Imposta la Correzione di Frequenza (PPM) in base alla tua calibrazione.
  * Modalità: ``WFM (mono o stereo)`` per FM broadcast.

----

.. _install_sdrpp_max:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ è un ricevitore SDR moderno, veloce e multipiattaforma che supporta una varietà di dispositivi, incluso RTL-SDR Blog V4. Offre un’interfaccia pulita e intuitiva, ampio supporto alle modulazioni, filtri DSP avanzati e capacità di registrazione.

Puoi fare riferimento al manuale utente ufficiale qui: https://www.sdrpp.org/manual.pdf


**Installazione da Sorgente**

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

**Prevenire la Sovrascrittura dei Driver**

Quando installi GQRX, SDR++, gnuradio-dev o gr-osmosdr, il sistema potrebbe reinstallare una versione obsoleta di ``librtlsdr``.  
Dopo ogni installazione, controlla:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Se non punta più a ``/usr/local/lib/librtlsdr.so``, esegui:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Puoi testare immediatamente (o dopo un riavvio per un ambiente pulito):

.. code-block:: shell

   rtl_test -t

Output atteso:

   * Contiene RTL-SDR Blog V4 Detected.
   * Nessun messaggio [R82XX] PLL not locked!.


**Note al Primo Avvio:**

Dopo l’installazione, SDR++ apparirà nel menu del desktop (solitamente sotto "Altro"), oppure puoi eseguire:

   .. code-block:: shell

      sdrpp

* **Dispositivo:** Seleziona **RTL-SDR (V4)** nel menu **Source**.
* **Sample Rate:** 1.8 MSPS è tipico; riduci se il carico della CPU è elevato.
* **Gain:** Disabilita l’AGC e imposta il guadagno manuale (inizia da ~35 dB).
* **Correzione PPM:** Inserisci il valore di calibrazione da ``rtl_test -p``.
* **Modalità di Demodulazione:** Scegli WFM per broadcast FM, SSB per bande radioamatoriali, ecc.

----

.. _install_rtl433_max:

rtl_433
^^^^^^^^^^^^

rtl_433 è uno strumento da riga di comando per decodificare trasmissioni radio da dispositivi che operano nella banda ISM a 433 MHz, come stazioni meteo, sensori di pressione pneumatici e termometri wireless.

**Installazione:**

.. code-block:: shell

   sudo apt install -y rtl-433

**Prevenire la Sovrascrittura dei Driver**

Quando installi GQRX, SDR++, gnuradio-dev o gr-osmosdr, il sistema potrebbe reinstallare una versione obsoleta di ``librtlsdr``.  
Dopo ogni installazione, controlla:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Se non punta più a ``/usr/local/lib/librtlsdr.so``, esegui:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Puoi testare immediatamente (o dopo un riavvio per un ambiente pulito):

.. code-block:: shell

   rtl_test -t

Output atteso:

   * Contiene RTL-SDR Blog V4 Detected.
   * Nessun messaggio [R82XX] PLL not locked!.

**Uso di Base:**

* Esegui ``rtl_433`` per rilevare e decodificare automaticamente i dispositivi a 433 MHz più comuni.
* Usa ``rtl_433 -G`` per elencare tutti i protocolli supportati.

----

.. _install_dump1090_max:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability è un decodificatore Mode S per dati transponder ADS-B degli aerei. Riceve e decodifica posizioni degli aerei, velocità e altri dati di volo, e può fornire una mappa live tramite browser web.

**Installazione:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**Prevenire la Sovrascrittura dei Driver**

Quando installi GQRX, SDR++, gnuradio-dev o gr-osmosdr, il sistema potrebbe reinstallare una versione obsoleta di ``librtlsdr``.  
Dopo ogni installazione, controlla:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Se non punta più a ``/usr/local/lib/librtlsdr.so``, esegui:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Puoi testare immediatamente (o dopo un riavvio per un ambiente pulito):

.. code-block:: shell

   rtl_test -t

Output atteso:

   * Contiene RTL-SDR Blog V4 Detected.
   * Nessun messaggio [R82XX] PLL not locked!.

**Uso di Base:**

* Esegui: ``dump1090 --interactive --net``.
* Apri ``http://<raspberrypi-ip>:8080`` nel tuo browser per visualizzare il tracciamento live degli aerei.
