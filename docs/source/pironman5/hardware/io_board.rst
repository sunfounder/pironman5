.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

IO Expander
================

LED RGB
------------

.. image:: img/io_board_rgb.png

La scheda è dotata di 4 LED RGB WS2812, che offrono un controllo personalizzabile. Gli utenti possono accenderli o spegnerli, cambiare colore, regolare la luminosità, cambiare modalità di visualizzazione e impostare la velocità delle transizioni.

* Per modificare lo stato di accensione e spegnimento dei LED RGB, usa ``true`` per accenderli e ``false`` per spegnerli.

.. code-block:: shell

  pironman5 -re true

* Per cambiare il colore, inserisci i valori esadecimali del colore desiderato, ad esempio ``fe1a1a``.

.. code-block:: shell

  pironman5 -rc fe1a1a

* Per modificare la luminosità dei LED RGB (intervallo: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rb 100

* Per cambiare le modalità di visualizzazione dei LED RGB, scegli tra le opzioni: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Se imposti la modalità di visualizzazione dei LED RGB su ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, non sarà possibile impostare il colore tramite ``pironman5 -rc``.

.. code-block:: shell

  pironman5 -rs breathing

* Per modificare la velocità delle transizioni (intervallo: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rp 80

Pin di Controllo RGB
-------------------------

I LED RGB sono controllati tramite SPI e collegati a **GPIO10**, che è anche il pin SPI MOSI. I due pin sopra J9 vengono utilizzati per collegare i LED RGB a GPIO10. Se non necessario, il ponticello può essere rimosso.

  .. image:: img/io_board_rgb_pin.png

Pin RGB OUT
-------------------------

.. image:: img/io_board_rgb_out.png

I LED RGB WS2812 supportano la connessione in serie, consentendo l'aggiunta di una striscia LED RGB esterna. Collega il pin **SIG** al pin **DIN** della striscia esterna per l'espansione.

Il setup predefinito include 4 LED RGB. Collega ulteriori LED e aggiorna il conteggio utilizzando:

.. code-block:: shell

  pironman5 -rl 12


Connettore dello Schermo OLED
---------------------------------

Il connettore dello schermo OLED, con un indirizzo di 0x3C, è una caratteristica chiave.

.. image:: img/io_board_oled.png

Se lo schermo OLED non visualizza nulla o visualizza in modo errato, segui questi passaggi per risolvere il problema:

Verifica che il cavo FPC dello schermo OLED sia correttamente collegato.

#. Usa il seguente comando per visualizzare i log del programma e controllare eventuali messaggi di errore.

    .. code-block:: shell

        cat /opt/pironman5/log

#. In alternativa, usa il seguente comando per verificare se l'indirizzo i2c dello schermo OLED (0x3C) viene riconosciuto:
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. Se i primi due passaggi non rivelano problemi, prova a riavviare il servizio pironman5 per vedere se il problema viene risolto.

    .. code-block:: shell

        sudo systemctl restart pironman5.service


Ricevitore Infrarossi
---------------------------

.. image:: img/io_board_receiver.png

* **Modello**: IRM-56384, funzionante a 38KHz.
* **Connessione**: Il ricevitore IR è collegato a **GPIO13**.
* **D1**: Un indicatore di ricezione a infrarossi che lampeggia al rilevamento del segnale.
* **J8**: Un pin per abilitare la funzione a infrarossi. Di default, un cappuccio ponticello è inserito per l'uso immediato. Rimuovi il cappuccio per liberare GPIO13 se il ricevitore IR non è in uso.

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

* Dopo aver eseguito il comando, premi un pulsante sul telecomando e il codice di quel pulsante verrà stampato.


Pin Ventola RGB
------------------

La scheda di espansione IO supporta fino a due ventole non-PWM da 5V. Entrambe le ventole sono controllate insieme.

**FAN1** e **FAN 2** sono due set di pin per ventole. Devi collegare il filo rosso della ventola a "+", e il filo nero a "-".

.. image:: img/io_board_fan.png

I due pin sotto J9 sono i pin di abilitazione per le ventole RGB. Di default, un ponticello è inserito su questi pin, consentendo il controllo dello stato di accensione e spegnimento delle ventole tramite GPIO6. Se non è desiderata l'operazione delle ventole, il ponticello può essere rimosso per liberare GPIO6.

.. image:: img/io_board_fan_j9.png

**D2** è un indicatore di segnale della ventola che si illumina quando la ventola è attiva.

.. image:: img/io_board_fan_d2.png

Puoi usare un comando per configurare la modalità operativa delle due ventole RGB. Queste modalità determinano le condizioni in cui le ventole RGB si attiveranno.

Ad esempio, se impostato su **1: Performance**, le ventole RGB si attiveranno a 50°C.

.. code-block:: shell

  pironman5 -gm 3

* **4: Quiet**: Le ventole RGB si attiveranno a 70°C.
* **3: Balanced**: Le ventole RGB si attiveranno a 67,5°C.
* **2: Cool**: Le ventole RGB si attiveranno a 60°C.
* **1: Performance**: Le ventole RGB si attiveranno a 50°C.
* **0: Sempre Accese**: Le ventole RGB saranno sempre accese.

Se colleghi il pin di controllo della ventola RGB a diversi pin sul Raspberry Pi, puoi usare il seguente comando per cambiare il numero di pin.

.. code-block:: shell

  sudo pironman5 -gp 18

Intestazioni Pin
--------------------

.. image:: img/io_board_pin_header.png

Due connettori ad angolo retto estendono il GPIO del Raspberry Pi, ma tieni presente che il ricevitore IR, i LED RGB e la ventola occupano alcuni pin. Rimuovi i ponticelli corrispondenti per utilizzare questi pin per altre funzioni.

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5
    - Raspberry Pi 5
  * - Ricevitore IR(Opzionale)
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - VENTOLA(Opzionale)
    - GPIO6
  * - RGB(Opzionale)
    - GPIO10
  * - RGB(Opzionale)
    - GPIO12
  * - RGB(Opzionale)
    - GPIO21

