.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _view_control_commands:

Controllo tramite Comandi
========================================
Oltre a visualizzare i dati del Pironman 5 e controllare vari dispositivi tramite la Dashboard, puoi anche utilizzare i comandi per controllarli.

.. note::

  * Per il sistema **Home Assistant**, puoi monitorare e controllare il Pironman 5 solo tramite la dashboard aprendo la pagina web all'indirizzo ``http://<ip>:34001``.
  * Per il sistema **Batocera.linux**, puoi monitorare e controllare il Pironman 5 solo tramite comandi. È importante notare che qualsiasi modifica alla configurazione richiede il riavvio del servizio utilizzando ``pironman5 restart`` affinché abbia effetto.


Visualizza le Configurazioni di Base
-------------------------------------------

Il modulo ``pironman5`` offre configurazioni di base per Pironman, che puoi visualizzare con il seguente comando.

.. code-block:: shell

  pironman5 -c

Le configurazioni standard appaiono come segue:

.. code-block:: 

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

Personalizza queste configurazioni in base alle tue esigenze.

Usa ``pironman5`` o ``pironman5 -h`` per le istruzioni.

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format with or without # (e.g. #FF0000 or 00aabb)
    -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                          RGB style
    -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin

.. note::

  Ogni volta che modifichi lo stato di ``pironman5.service``, devi utilizzare il seguente comando per applicare le modifiche alla configurazione.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verifica lo stato del programma ``pironman5`` utilizzando lo strumento ``systemctl``.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* In alternativa, controlla i file di log generati dal programma.

  .. code-block:: shell

    cat /opt/pironman5/log


Controllo dei LED RGB
---------------------------
La scheda è dotata di 4 LED RGB WS2812, offrendo un controllo personalizzabile. Gli utenti possono accenderli o spegnerli, cambiare il colore, regolare la luminosità, cambiare le modalità di visualizzazione dei LED RGB e impostare la velocità dei cambiamenti.

.. note::

  Ogni volta che modifichi lo stato di ``pironman5.service``, devi utilizzare il seguente comando per applicare le modifiche alla configurazione.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Per modificare lo stato di accensione e spegnimento dei LED RGB, usa ``true`` per accendere i LED RGB e ``false`` per spegnerli.

.. code-block:: shell

  pironman5 -re true

* Per cambiare il loro colore, inserisci i valori esadecimali del colore desiderato, ad esempio ``fe1a1a``.

.. code-block:: shell

  pironman5 -rc fe1a1a

* Per cambiare la luminosità dei LED RGB (intervallo: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rb 100

* Per cambiare le modalità di visualizzazione dei LED RGB, scegli tra le opzioni: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Se imposti la modalità di visualizzazione dei LED RGB su ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, non potrai impostare il colore utilizzando ``pironman5 -rc``.

.. code-block:: shell

  pironman5 -rs breathing

* Per modificare la velocità del cambiamento (intervallo: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rp 80

* La configurazione predefinita include 4 LED RGB. Collega ulteriori LED e aggiorna il conteggio utilizzando:

.. code-block:: shell

  pironman5 -rl 12

.. _cc_control_fan:

Controllo delle Ventole RGB
-----------------------------------
La scheda di espansione IO supporta fino a due ventole non PWM da 5V. Entrambe le ventole sono controllate insieme. 

.. note::

  Ogni volta che modifichi lo stato di ``pironman5.service``, devi utilizzare il seguente comando per applicare le modifiche alla configurazione.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Puoi utilizzare il comando per configurare la modalità operativa delle due ventole RGB. Queste modalità determinano le condizioni in cui le ventole RGB si attiveranno. 

Ad esempio, se impostato su modalità **1: Performance**, le ventole RGB si attiveranno a 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Silenziosa**: Le ventole RGB si attiveranno a 70°C.
* **3: Bilanciata**: Le ventole RGB si attiveranno a 67,5°C.
* **2: Fresca**: Le ventole RGB si attiveranno a 60°C.
* **1: Performance**: Le ventole RGB si attiveranno a 50°C.
* **0: Sempre Accese**: Le ventole RGB saranno sempre accese.

* Se colleghi il pin di controllo della ventola RGB a pin diversi sul Raspberry Pi, puoi utilizzare il seguente comando per cambiare il numero del pin.

.. code-block:: shell

  sudo pironman5 -gp 18


Controllo dello Schermo OLED
-----------------------------------

Quando hai installato la libreria ``pironman5``, lo schermo OLED visualizza l'utilizzo della CPU, RAM, Disco, la temperatura della CPU e l'indirizzo IP del Raspberry Pi, e lo mostra ogni volta che riavvii.

Se il tuo schermo OLED non visualizza alcun contenuto, devi prima verificare se il cavo FPC dell'OLED è collegato correttamente.

Poi puoi controllare il log del programma per vedere qual è il problema con il seguente comando.

.. code-block:: shell

  cat /var/log/pironman5/

Oppure controlla se l'indirizzo i2c dell'OLED 0x3C viene riconosciuto:

.. code-block:: shell

  i2cdetect -y 1

Controllo del Ricevitore Infrarossi
---------------------------------------

Per utilizzare il ricevitore IR, verifica la connessione e installa il modulo necessario:

* Testa la connessione:

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Installa il modulo ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Ora, testa il ricevitore IR eseguendo il seguente comando. 

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Dopo aver eseguito il comando, premi un pulsante sul telecomando e verrà stampato il codice di quel pulsante.


