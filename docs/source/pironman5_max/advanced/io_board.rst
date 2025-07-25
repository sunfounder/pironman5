.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e difficoltà tecniche con l’aiuto della nostra community e del nostro team.
    - **Learn & Share**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato a nuovi annunci di prodotto e anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra nella community oggi stesso!

Espansore IO
================

LED RGB
------------

.. image:: img/io_board_rgb.png

La scheda è dotata di 4 LED RGB WS2812 completamente configurabili. È possibile accenderli o spegnerli, cambiare colore, regolare la luminosità, selezionare diverse modalità di visualizzazione e impostare la velocità delle transizioni.

* Per modificare lo stato acceso/spento dei LED RGB, ``true`` li accende, ``false`` li spegne.

.. code-block:: shell

  sudo pironman5 -re true

* Per cambiare colore, inserire il valore esadecimale desiderato, ad esempio ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Per regolare la luminosità dei LED RGB (intervallo: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* Per cambiare modalità di visualizzazione dei LED RGB, scegli tra: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Se imposti la modalità su ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, non potrai modificare il colore con ``pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Per modificare la velocità della transizione (intervallo: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rp 80

Pin di controllo RGB
-------------------------

I LED RGB sono controllati tramite SPI e collegati a **GPIO10**, che corrisponde anche al pin SPI MOSI. I due pin mostrati servono a collegare i LED RGB a GPIO10. Se non utilizzati, è possibile rimuovere il ponticello.

  .. image:: img/io_board_rgb_pin.png

Pin di uscita RGB
-------------------------

.. image:: img/io_board_rgb_out.png

I LED RGB WS2812 supportano la connessione in serie, permettendo l'espansione tramite una striscia LED RGB esterna. Collega il pin **SIG** al pin **DIN** della striscia esterna.

La configurazione predefinita include 4 LED RGB. Per aggiungere altri LED, aggiorna il numero con il comando:

.. code-block:: shell

  sudo pironman5 --rgb-led-count [quantity]

Esempio:

.. code-block:: shell

  sudo pironman5 --rgb-led-count 12



Connettore Schermo OLED
----------------------------

Il connettore per schermo OLED, con indirizzo 0x3C, è una delle componenti principali.

.. image:: img/io_board_oled.png

Se il display OLED non mostra nulla o mostra dati errati, prova questi passaggi per la diagnosi:

Verifica che il cavo FPC dello schermo OLED sia collegato correttamente.

#. Usa il comando seguente per visualizzare i log del programma e verificare eventuali errori.

    .. code-block:: shell

        cat /var/log/pironman5/pm_auto.oled.log

#. In alternativa, usa questo comando per verificare se l'indirizzo i2c 0x3C dello schermo OLED viene rilevato:
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. Se i primi due passaggi non mostrano problemi, prova a riavviare il servizio pironman5 per risolvere:


    .. code-block:: shell

        sudo systemctl restart pironman5.service


Trigger di Riattivazione
-------------------------

.. image:: img/io_board_vib.png

L'interruttore a vibrazione integrato viene utilizzato per riattivare il display OLED dalla modalità di sospensione. Quando viene rilevata una vibrazione, viene inviato un segnale per riattivare l'OLED, consentendo al display di rimanere spento quando inattivo e di riaccendersi automaticamente al rilevamento di un movimento.

Se si rimuove il ponticello etichettato per l'interruttore a vibrazione, la funzione di riattivazione verrà disabilitata. Una volta che l'OLED entra in modalità di sospensione, non sarà più possibile riattivarlo. Questa opzione è pensata per utenti esperti che desiderano riutilizzare il pin GPIO corrispondente per altre applicazioni.

.. note::

  Ponticello installato: la riattivazione tramite vibrazione è abilitata.

  Ponticello rimosso: l’OLED non può essere riattivato una volta spento. Il pin è liberato per altri utilizzi.



Ricevitore a Infrarossi
---------------------------

.. image:: img/io_board_receiver.png

* **Modello**: IRM-56384, frequenza di funzionamento 38KHz.
* **Connessione**: Il ricevitore IR è collegato a **GPIO13**.
* **D1**: LED indicatore che lampeggia alla ricezione di segnali IR.
* **J8**: Pin per l'attivazione della funzione IR. Di default è presente un jumper. Rimuovilo se non si usa il ricevitore e si desidera liberare GPIO13.

Per utilizzare il ricevitore IR, assicurati che sia collegato e installa il modulo necessario:

* Verifica la connessione:

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Installa il modulo ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Testa il ricevitore IR con il comando:

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Dopo aver lanciato il comando, premi un tasto sul telecomando: verrà stampato il codice corrispondente.


Pin ventole RGB
------------------

La scheda di espansione IO supporta fino a due ventole non-PWM a 5V, controllate simultaneamente.

**FAN1** e **FAN2** sono due set di pin. Collega il filo rosso della ventola a "+" e il filo nero a "-".

.. image:: img/io_board_fan.png

Ci sono due connettori a 2 pin e due jumper per il controllo delle ventole RGB e dei relativi LED. 
I jumper sono connessi ai pin GPIO6 e GPIO5 per il controllo da software. 
Se non è necessario controllare le ventole, rimuovi i jumper per liberare questi pin GPIO.

.. image:: img/io_board_fan_j9.png


Dopo aver rimosso i jumper, le ventole e i LED non si accenderanno. 
Per attivarli comunque all’avvio, è possibile saldare i due pad sottostanti. 
In questo modo si accenderanno all'accensione del sistema e si spegneranno allo spegnimento, 
ma non saranno più controllabili via GPIO.

.. image:: img/io_board_fan_hanpan.png

.. **D2** è un LED indicatore che si accende quando la ventola è in funzione.

.. .. image:: img/io_board_fan_d2.png

.. Puoi usare un comando per impostare la modalità di funzionamento delle ventole RGB. Ogni modalità corrisponde a una soglia di attivazione termica.

Ad esempio, la modalità **1: Performance** attiva le ventole a 50°C.

.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: le ventole si attivano a 70°C.
* **3: Balanced**: le ventole si attivano a 67.5°C.
* **2: Cool**: le ventole si attivano a 60°C.
* **1: Performance**: le ventole si attivano a 50°C.
* **0: Always On**: le ventole sono sempre accese.

Se colleghi il pin di controllo delle ventole RGB a un GPIO diverso, usa questo comando per aggiornarlo:

.. code-block:: shell

  sudo pironman5 -gp 18

Header Pin
--------------

.. image:: img/io_board_pin_header.png

Due header angolati estendono i GPIO del Raspberry Pi. Nota che ricevitore IR, LED RGB e ventole occupano alcuni pin. Rimuovi i jumper corrispondenti se vuoi riutilizzare questi pin per altri scopi.

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
  * - LED Ventola (Opzionale)
    - GPIO5  
  * - RGB (Opzionale)
    - GPIO10
