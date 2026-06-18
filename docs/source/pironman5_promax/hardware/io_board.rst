
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Espansore IO
================

.. image:: img/io_board.png

LED RGB
------------

.. image:: img/io_board_rgb.png

La scheda dispone di 18 LED RGB indirizzabili WS2812B: 6 sulla scheda e 12 integrati nelle ventole GPIO, offrendo un controllo personalizzabile. Gli utenti possono accenderli o spegnerli, cambiare il colore, regolare la luminosità, cambiare le modalità di visualizzazione e impostare la velocità delle variazioni.

Pin di Controllo RGB
-------------------------

Il LED RGB è pilotato da SPI e collegato a **GPIO10**, che è anche il pin SPI MOSI. I due pin mostrati sono utilizzati per collegare l'RGB a GPIO10. Se non necessario, il ponticello può essere rimosso.

  .. image:: img/io_board_rgb_pin.png

Pin RGB OUT
-------------------------

.. image:: img/io_board_rgb_out.png

I LED RGB WS2812 supportano la connessione in serie, permettendo il collegamento di una striscia LED RGB esterna. Collega il pin **SIG** al pin **DIN** della striscia esterna per l'espansione.

La scheda dispone di 18 LED RGB indirizzabili WS2812B: 6 sulla scheda e 12 integrati nelle ventole GPIO. Collega LED aggiuntivi e aggiorna il conteggio utilizzando:

.. code-block:: shell

  sudo pironman5 --rgb-led-count [quantità]

Esempio:

.. code-block:: shell

  sudo pironman5 --rgb-led-count 24

Connettore Schermo OLED
----------------------------

Il connettore dello schermo OLED, con indirizzo 0x3C, è una caratteristica chiave.

.. image:: img/io_board_oled.png

Se lo schermo OLED non visualizza nulla o visualizza in modo errato, puoi seguire questi passaggi per risolvere il problema:

Verifica che il cavo FPC dello schermo OLED sia collegato correttamente.

#. Usa il seguente comando per visualizzare i log di esecuzione del programma e controllare eventuali messaggi di errore.

    .. code-block:: shell

        cat /var/log/pironman5/pironman5.log

#. In alternativa, usa il seguente comando per verificare se l'indirizzo i2c 0x3C dell'OLED è riconosciuto:

    .. code-block:: shell

        sudo i2cdetect -y 1

#. Se i primi due passaggi non rivelano alcun problema, prova a riavviare il servizio pironman5 per vedere se risolve il problema.

    .. code-block:: shell

        sudo systemctl restart pironman5.service

Ricevitore Infrarossi
---------------------------

.. image:: img/io_board_receiver.png

* **Modello**: IRM-56384, operante a 38KHz.
* **Connessione**: Il ricevitore IR si collega a **GPIO13**.
* **D7**: Un indicatore di ricezione a infrarossi che lampeggia al rilevamento del segnale.
* **J6**: Un pin per abilitare la funzione a infrarossi. Di default, un ponticello è inserito per la funzionalità immediata. Rimuovi il cappuccio per liberare GPIO13 se il ricevitore IR non è in uso.

Per utilizzare il ricevitore IR, verifica la sua connessione e installa il modulo necessario:

* Testa la connessione:

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Installa il modulo ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Ora, testa il Ricevitore IR eseguendo il seguente comando.

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Dopo aver eseguito il comando, premi un pulsante sul telecomando e il codice di quel pulsante verrà stampato.

Pin ventole GPIO
--------------------

.. image:: img/io_board_pin_fan.png

La scheda di espansione IO supporta fino a tre ventole CPU da 5V. Tutte le ventole sono controllate insieme.

Il segnale di controllo della ventola è collegato alla porta **FAN IN** sulla scheda di espansione IO, e quindi emesso dalle tre porte dedicate per ventole. Queste porte sono numerate dall'alto verso il basso come **REAR UPPER**, **REAR LOWER** e **CPU FAN**. Collegale secondo la serigrafia, altrimenti influenzerà il controllo RGB sulla ventola.

Pin Header
--------------

.. image:: img/io_board_pin_header.png

Due connettori header ad angolo retto estendono il GPIO del Raspberry Pi, ma nota che il ricevitore IR, il LED RGB e la ventola occupano alcuni pin. Rimuovi i corrispondenti ponticelli per utilizzare questi pin per altre funzioni.

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 MAX
    - Raspberry Pi 5
  * - Ricevitore IR (Opzionale)
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - Ventola (Opzionale)
    - GPIO6
  * - FLED (Opzionale)
    - GPIO5  
  * - RGB (Opzionale)
    - GPIO10
