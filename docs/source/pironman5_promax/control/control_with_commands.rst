
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_view_control_commands:

Controllo tramite Comandi
========================================
Oltre a visualizzare i dati del Pironman 5 Pro MAX e controllare vari dispositivi attraverso la Dashboard, puoi anche utilizzare i comandi per controllarli.

Visualizzare le Configurazioni di Base
---------------------------------------

Il modulo ``pironman5`` offre configurazioni di base per Pironman, che puoi visualizzare con il seguente comando.

.. code-block:: shell

  sudo pironman5 -c

Le configurazioni standard appaiono come segue:

.. code-block:: 

  {
      "system": {
          "data_interval": 1,
          "enable_history": true,
          "rgb_color": "#ff3dbe",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 18,
          "temperature_unit": "C",
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "default_dashboard_page": "small",
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "debug_level": "INFO"
      }
  }

Personalizza queste configurazioni in base alle tue esigenze.

Usa ``pironman5`` o ``pironman5 -h`` per le istruzioni.

.. code-block::

  usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]]
                  [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-oe [OLED_ENABLE]]
                  [-or [{0,180}]] [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                  {start,stop,launch-browser} ...

  Pironman 5 Pro Max command line interface

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Database retention days
    -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                          Debug level
    -rd, --remove-dashboard
                          Remove dashboard
    -cp, --config-path [CONFIG_PATH]
                          Config path
    -eh, --enable-history [ENABLE_HISTORY]
                          Enable history, True/true/on/On/1 or False/false/off/Off/0
    -re, --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rs, --rgb-style [RGB_STYLE]
                          RGB style: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
    -rc, --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u, --temperature-unit [{C,F}]
                          Temperature unit
    -oe, --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          OLED pages, split by ',': mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds

  Subcommands:
    {start,stop,launch-browser}
      start               Start Pironman5
      stop                Stop Pironman5
      launch-browser      Launch browser

.. note::

  Ogni volta che modifichi lo stato di ``pironman5.service``, devi utilizzare il seguente comando per rendere effettive le modifiche di configurazione.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Verifica lo stato del programma ``pironman5`` utilizzando lo strumento ``systemctl``.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* In alternativa, ispeziona i file di log generati dal programma.

  .. code-block:: shell

    ls /var/log/pironman5/

**Controllo LED RGB**
----------------------
La scheda dispone di 18 LED RGB indirizzabili WS2812B: 6 sulla scheda e 12 integrati nelle ventole GPIO. Gli utenti possono controllare alimentazione, colore, luminosità, modalità di visualizzazione, velocità dell'animazione e il numero di LED attivi.

.. note::

  Dopo aver modificato la configurazione per ``pironman5.service``, è necessario riavviare il servizio per rendere effettive le modifiche:

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* **Abilita/Disabilita LED RGB**: Usa ``true`` per accendere, ``false`` per spegnere.

.. code-block:: shell

  sudo pironman5 -re true

* **Cambia Colore**: Imposta un colore utilizzando un valore esadecimale (senza il `#`), es., ``fe1a1a`` per il rosso.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* **Regola Luminosità**: Imposta la luminosità dallo 0% al 100%.

.. code-block:: shell

  sudo pironman5 -rb 75

* **Cambia Modalità di Visualizzazione**: Scegli tra diverse modalità di animazione:

  * ``solid``: Colore statico.
  * ``breathing``: Dissolvenza pulsante in entrata/uscita.
  * ``flow`` / ``flow_reverse``: Il colore scorre in una direzione.
  * ``rainbow`` / ``rainbow_reverse``: Cicla attraverso lo spettro dell'arcobaleno.
  * ``hue_cycle``: Cicla dolcemente attraverso i valori di tonalità.

.. code-block:: shell

  sudo pironman5 -rs breathing

.. note::

  Quando si utilizzano le modalità ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, il colore impostato tramite ``pironman5 -rc`` verrà sovrascritto dal ciclo automatico dei colori della modalità.

* **Regola Velocità dell'Animazione**: Controlla la velocità degli effetti dallo 0% (più lento) al 100% (più veloce).

.. code-block:: shell

  sudo pironman5 -rp 50

* **Imposta Conteggio LED**: Il sistema predefinito controlla 18 LED. Se hai esteso la catena con LED WS2812B esterni aggiuntivi, aggiorna il conteggio totale di conseguenza.

.. code-block:: shell

  sudo pironman5 -rl 12

**Ventola**
--------------------------------

Queste ventole si collegano a una porta dedicata per ventole CPU a 4 pin sul Raspberry Pi 5. La sua strategia di controllo predefinita è uno schema di regolazione della velocità intelligente a più livelli gestito dal firmware, basato sulla temperatura della CPU. Ciò significa che quando usi una ventola CPU ufficiale o compatibile e la colleghi correttamente, il sistema regolerà automaticamente la velocità della ventola in base alle variazioni della temperatura della CPU (iniziando a funzionare sopra i 50°C) senza alcun intervento manuale da parte tua.

**Controllare lo Schermo OLED**
-----------------------------------

Lo schermo OLED da 0.96" visualizza le informazioni di sistema (CPU, RAM, Disco, Temp, IP) per impostazione predefinita dopo l'installazione della libreria ``pironman5`` e il riavvio.

Se lo schermo OLED è vuoto:

1. Assicurati che il cavo FPC dell'OLED sia saldamente collegato alla scheda madre.
2. Controlla il log del servizio per eventuali errori:

    .. code-block:: shell

      sudo journalctl -u pironman5.service -f

    Oppure controlla il log specifico dell'OLED:

    .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

3. Verifica che l'OLED sia rilevato sul bus I2C (indirizzo `0x3C`):

    .. code-block:: shell

      i2cdetect -y 1

**Comandi di Configurazione OLED**

* **Abilita/Disabilita OLED**: Accende o spegne il display OLED.

    .. code-block:: shell

      sudo pironman5 -oe false

* **Ruota Display**: Imposta l'orientamento dello schermo a ``0`` (predefinito) o ``180`` gradi.

    .. code-block:: shell

      sudo pironman5 -or 180

* **Configura Pagine del Display**: Scegli quali pagine informative visualizzare in sequenza. Le pagine sono: ``mix`` (panoramica), ``performance`` (CPU/RAM dettagliati), ``ips`` (IP di rete), ``disk`` (archiviazione). Separa più pagine con virgole.

    .. code-block:: shell

      sudo pironman5 -op mix,ips,disk

* **Imposta Timeout di Sospensione**: Definisce quanti secondi di inattività prima che l'OLED si spenga (0 = mai in sospensione).

    .. code-block:: shell

      sudo pironman5 -os 120

**Controllare il Ricevitore Infrarossi**
-------------------------------------------------------------

Il ricevitore IR integrato consente il controllo tramite telecomando.

1. Installa il software necessario:

    .. code-block:: shell

      sudo apt-get install lirc -y

2. Testa il ricevitore. Esegui il seguente comando, poi punta un telecomando verso il case e premi i pulsanti. Dovresti vedere l'output del codice grezzo.

    .. code-block:: shell

      mode2 -d /dev/lirc0

3. Per impostare mapping specifici dei pulsanti del telecomando (es., per Kodi o Volumio), dovrai configurare il file `/etc/lirc/lircd.conf` con i codici del tuo telecomando.

**Comandi Generali di Sistema**
--------------------------------------------------

* **Mostra Versione**: Visualizza la versione del pacchetto ``pironman5`` installato.

.. code-block:: shell

  sudo pironman5 -v

* **Mostra Configurazione Corrente**: Visualizza tutte le impostazioni correnti.

.. code-block:: shell

  sudo pironman5 -c

* **Imposta Unità di Temperatura**: Passa tra Celsius (``C``) e Fahrenheit (``F``) per le visualizzazioni della temperatura.

.. code-block:: shell

  sudo pironman5 -u F

* **Configura la Registrazione dei Dati**:

  * **Imposta Giorni di Conservazione del Database**: Controlla per quanti giorni vengono conservati i dati storici (come i log della temperatura).

    .. code-block:: shell

      sudo pironman5 -drd 30

  * **Abilita/Disabilita Registrazione Storica**: Attiva o disattiva la raccolta dati.

    .. code-block:: shell

      sudo pironman5 -eh false

* **Imposta Verbosità del Log**: Regola il livello di dettaglio dei log di sistema. Opzioni: ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``.

.. code-block:: shell

  sudo pironman5 -dl DEBUG

* **Rimuovi Dashboard Web**: Disinstalla l'interfaccia di gestione web opzionale.

.. code-block:: shell

  sudo pironman5 -rd

* **Specifica Percorso Configurazione Personalizzato**: Usa un file di configurazione da una posizione non standard.

.. code-block:: shell

  sudo pironman5 -cp /home/pi/my_custom_config.json

**Sottocomandi di Gestione del Servizio**
------------------------------------------

* **Avvia il Servizio Pironman5**: Avvia manualmente il servizio in background che gestisce LED, ventole, OLED, ecc.

.. code-block:: shell

  sudo pironman5 start

* **Ferma il Servizio Pironman5**: Arresta correttamente il servizio in background.

.. code-block:: shell

  sudo pironman5 stop

* **Avvia la Dashboard Web nel Browser**: Se la dashboard web è installata, questo comando la aprirà nel tuo browser predefinito.

.. code-block:: shell

  sudo pironman5 launch-browser
