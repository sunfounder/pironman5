.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

RTL-SDR Blog V4
==============================================

.. note::

    I prodotti della serie Pironman 5 non includono i seguenti moduli.
    Devi procurartene uno da solo o acquistarlo dal nostro sito web ufficiale:

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

Questa guida copre una procedura di installazione affidabile per RTL-SDR Blog V4, un ricevitore radio software-defined (SDR) USB popolare ed economico.
La versione V4 presenta un tuner R828D migliorato, modalità di campionamento diretto, migliore sensibilità e bias-tee integrato per alimentare antenne attive.
Funziona bene per ricevere FM broadcast, airband, radioamatori, ADS-B e molti altri segnali su sistemi Linux e Raspberry Pi.

Per la documentazione originale del produttore, consulta la guida ufficiale di RTL-SDR Blog V4: https://www.rtl-sdr.com/V4/

----

Installare il Driver per RTL-SDR Blog V4
----------------------------------------

Su Linux la procedura è altrettanto semplice: rimuovere i driver RTL-SDR esistenti e installare una versione aggiornata.

**1. Rimuovere il driver precedente**

.. code-block:: shell

   sudo apt purge ^librtlsdr
   sudo rm -rvf /usr/lib/librtlsdr* /usr/include/rtl-sdr* /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* /usr/local/include/rtl_* /usr/local/bin/rtl_*

Verifica A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: nessun librtlsdr trovato nella cache di sistema."

**2. Installare i driver più recenti**

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

Nota:
    Se si desidera testare anche la ricezione FM da riga di comando (vedi sotto),
    è necessario ``sox``, che fornisce il comando ``play``.

    .. code-block:: shell

       sudo apt install -y sox

Verifica B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Dovrebbe puntare a /usr/local/lib/librtlsdr.so

**3. Bloccare i driver DVB-T TV**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

**4. Riavviare**

.. code-block:: shell

   sudo reboot

**5. Verifica del driver dopo il riavvio**

.. code-block:: shell

   rtl_test -t

Risultato atteso:
    L'output dovrebbe includere ``RTL-SDR Blog V4 Detected`` senza messaggi ``[R82XX] PLL not locked!``.
    La riga ``Using device 0: Generic RTL2832U OEM`` è normale — è solo il nome USB.

**6. Test di Ricezione FM dalla Riga di Comando**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

Suggerimenti:

    * ``-g``: Prova tra 25–35 dB; più alto non è sempre meglio.
    * Riduci ``-s`` a ~170k–180k per ridurre il rumore.
    * Regola leggermente la frequenza (es., ``97.1005M``) per una messa a punto fine.
    * Chiudi qualsiasi altro software SDR che potrebbe tenere occupato il dispositivo.

----

Installazione di Software Radio Comune
----------------------------------------

Questa sezione introduce quattro applicazioni SDR ampiamente utilizzate, con brevi descrizioni, istruzioni di installazione e suggerimenti di configurazione di base per sistemi Debian-based.

* :ref:`install_gqrx_promax`
* :ref:`install_sdrpp_promax`
* :ref:`install_rtl433_promax`
* :ref:`install_dump1090_promax`

----

.. _install_gqrx_promax:

GQRX
^^^^^^^^^^^^

GQRX è un'applicazione ricevitore SDR semplice e facile da usare con interfaccia grafica. Supporta un'ampia gamma di dispositivi SDR ed è ideale per ascoltare FM, AM, SSB e altri segnali con display a spettro e waterfall in tempo reale.

Puoi anche consultare la guida ufficiale all'installazione per Raspberry Pi qui: https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Opzione 1 – Installazione Rapida (Consigliata per la maggior parte degli utenti)**

Veloce, semplice e si integra con gli aggiornamenti di sistema — ma potrebbe non essere l'ultima versione.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Opzione 2 – Compilare dal Sorgente (Opzionale, Ultime Funzionalità)**

Assicura l'ultima versione e la piena personalizzazione, ma richiede più tempo per la compilazione e più dipendenze.

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

**Prevenire la Sovrascrittura del Driver**

Quando si installano GQRX, SDR++, gnuradio-dev o gr-osmosdr, il sistema potrebbe reinstallare ``librtlsdr`` obsoleti.
Dopo ogni installazione, controlla:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Se non punta più a ``/usr/local/lib/librtlsdr.so``, esegui:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Puoi testare immediatamente (o dopo un riavvio per un ambiente pulito):

.. code-block:: shell

   rtl_test -t

Risultato atteso:

   * Contiene RTL-SDR Blog V4 Detected.
   * Nessun messaggio [R82XX] PLL not locked!.

**Configurazione del Primo Avvio**

* **Dispositivi I/O**:

  * Device: ``RTL-SDR (V4)``.
  * Input Rate: ``1.8 MSPS`` (1800000).

* **Controlli di Ingresso**:

  * **LNA Gain**: Inizia intorno a 25–35 dB, regola come necessario.

* **Opzioni Ricevitore**:

  * Imposta Frequency Correction (PPM) dalla tua calibrazione.
  * Mode: ``WFM (mono o stereo)`` per FM broadcast.

----

.. _install_sdrpp_promax:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ è un ricevitore radio software-defined (SDR) moderno, veloce e cross-platform che supporta una varietà di dispositivi, incluso RTL-SDR Blog V4. Offre un'interfaccia pulita e facile da usare, ampio supporto di modulazione, filtraggio DSP avanzato e capacità di registrazione.

Puoi consultare il manuale utente ufficiale qui: https://www.sdrpp.org/manual.pdf

**Installare dal Sorgente**

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

**Prevenire la Sovrascrittura del Driver**

Quando si installano GQRX, SDR++, gnuradio-dev o gr-osmosdr, il sistema potrebbe reinstallare ``librtlsdr`` obsoleti.
Dopo ogni installazione, controlla:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Se non punta più a ``/usr/local/lib/librtlsdr.so``, esegui:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Puoi testare immediatamente (o dopo un riavvio per un ambiente pulito):

.. code-block:: shell

   rtl_test -t

Risultato atteso:

   * Contiene RTL-SDR Blog V4 Detected.
   * Nessun messaggio [R82XX] PLL not locked!.

**Note sul Primo Avvio:**

Dopo l'installazione, SDR++ apparirà nel menu del desktop (solitamente sotto "Other"), oppure puoi eseguire:

   .. code-block:: shell

      sdrpp

* **Device:** Seleziona **RTL-SDR (V4)** nel menu **Source**.
* **Sample Rate:** 1.8 MSPS è tipico; più basso se il carico della CPU è elevato.
* **Gain:** Disabilita AGC e imposta il guadagno manuale (inizia ~35 dB).
* **PPM Correction:** Inserisci il valore di calibrazione da ``rtl_test -p``.
* **Demodulation Mode:** Scegli WFM per FM broadcast, SSB per bande radioamatoriali, ecc.

----

.. _install_rtl433_promax:

rtl_433
^^^^^^^^^^^^

rtl_433 è uno strumento a riga di comando per decodificare trasmissioni radio da dispositivi che operano nella banda ISM a 433 MHz, come stazioni meteorologiche, sensori di pressione dei pneumatici e termometri wireless.

**Installare:**

.. code-block:: shell

   sudo apt install -y rtl-433

**Prevenire la Sovrascrittura del Driver**

Quando si installano GQRX, SDR++, gnuradio-dev o gr-osmosdr, il sistema potrebbe reinstallare ``librtlsdr`` obsoleti.
Dopo ogni installazione, controlla:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Se non punta più a ``/usr/local/lib/librtlsdr.so``, esegui:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Puoi testare immediatamente (o dopo un riavvio per un ambiente pulito):

.. code-block:: shell

   rtl_test -t

Risultato atteso:

   * Contiene RTL-SDR Blog V4 Detected.
   * Nessun messaggio [R82XX] PLL not locked!.

**Uso di Base:**

* Esegui ``rtl_433`` per rilevare e decodificare automaticamente i dispositivi comuni a 433 MHz.
* Usa ``rtl_433 -G`` per elencare tutti i protocolli supportati.

----

.. _install_dump1090_promax:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability è un decoder Mode S per i dati dei transponder degli aeromobili ADS-B. Riceve e decodifica posizioni, velocità e altri dati di volo degli aeromobili, e può servire una mappa in tempo reale tramite un browser web.

**Installare:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**Prevenire la Sovrascrittura del Driver**

Quando si installano GQRX, SDR++, gnuradio-dev o gr-osmosdr, il sistema potrebbe reinstallare ``librtlsdr`` obsoleti.
Dopo ogni installazione, controlla:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Se non punta più a ``/usr/local/lib/librtlsdr.so``, esegui:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Puoi testare immediatamente (o dopo un riavvio per un ambiente pulito):

.. code-block:: shell

   rtl_test -t

Risultato atteso:

   * Contiene RTL-SDR Blog V4 Detected.
   * Nessun messaggio [R82XX] PLL not locked!.

**Uso di Base:**

* Esegui: ``dump1090 --interactive --net``.
* Apri ``http://<raspberrypi-ip>:8080`` nel tuo browser per visualizzare il tracciamento degli aeromobili in tempo reale.