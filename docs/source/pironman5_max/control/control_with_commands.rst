.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e difficoltà tecniche con l’aiuto della nostra community e del nostro team.
    - **Learn & Share**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato a nuovi annunci di prodotto e anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra nella community oggi stesso!

.. _max_view_control_commands:

Controllo tramite Comandi
========================================
Oltre a visualizzare i dati del Pironman 5 e controllare i vari dispositivi tramite la Dashboard, puoi anche utilizzare comandi per gestirli.

.. note::

  * Per il sistema **Home Assistant**, è possibile monitorare e controllare il Pironman 5 solo tramite la dashboard accedendo alla pagina ``http://<ip>:34001``.
  * Per il sistema **Batocera.linux**, è possibile monitorare e controllare il Pironman 5 solo tramite comandi. Ricorda che ogni modifica alla configurazione richiede il riavvio del servizio con ``pironman5 restart`` affinché abbia effetto.

Visualizzare le Configurazioni di Base
-----------------------------------------

Il modulo ``pironman5`` offre configurazioni base per Pironman, consultabili con il comando seguente:

.. code-block:: shell

  pironman5 -c

Le configurazioni standard appariranno così:

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

Personalizza queste impostazioni in base alle tue esigenze.

Utilizza ``pironman5`` o ``pironman5 -h`` per istruzioni.

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc RGB_COLOR] [-rb RGB_BRIGHTNESS] [-rs {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}] [-rp RGB_SPEED] [-re RGB_ENABLE]
                          [-rl RGB_LED_COUNT] [-u {C,F}] [-gm GPIO_FAN_MODE] [-gp GPIO_FAN_PIN]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc RGB_COLOR, --rgb-color RGB_COLOR
                          RGB color
    -rb RGB_BRIGHTNESS, --rgb-brightness RGB_BRIGHTNESS
                          RGB brightness
    -rs {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}, --rgb-style {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}
                          RGB style
    -rp RGB_SPEED, --rgb-speed RGB_SPEED
                          RGB speed
    -re RGB_ENABLE, --rgb-enable RGB_ENABLE
                          RGB enable
    -rl RGB_LED_COUNT, --rgb-led-count RGB_LED_COUNT
                          RGB LED count
    -u {C,F}, --temperature-unit {C,F}
                          Temperature unit
    -gm GPIO_FAN_MODE, --gpio-fan-mode GPIO_FAN_MODE
                          GPIO fan mode, 0-4, ['Always On', 'Performance', 'Cool', 'Balanced', 'Quiet']
    -gp GPIO_FAN_PIN, --gpio-fan-pin GPIO_FAN_PIN
                          GPIO fan pin



.. note::

  Ogni volta che modifichi lo stato di ``pironman5.service``, usa il comando seguente per applicare i cambiamenti:

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verifica lo stato del programma ``pironman5`` con lo strumento ``systemctl``:

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Oppure ispeziona i log generati dal programma:

  .. code-block:: shell

    ls /var/log/pironman5/


Controllo dei LED RGB
-------------------------
La scheda è dotata di 4 LED RGB WS2812 con controllo personalizzabile. Puoi accenderli/spegnerli, cambiare colore, regolare luminosità, stile e velocità di animazione.

.. note::

  Ogni volta che modifichi lo stato di ``pironman5.service``, è necessario utilizzare il seguente comando per applicare le modifiche alla configurazione.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Per modificare lo stato di accensione dei LED RGB, usa ``true`` per accenderli e ``false`` per spegnerli.

.. code-block:: shell

  pironman5 -re true

* Per cambiarne il colore, inserisci il valore esadecimale desiderato, ad esempio ``fe1a1a``.

.. code-block:: shell

  pironman5 -rc fe1a1a

* Per regolare la luminosità (0 ~ 100%):

.. code-block:: shell

  pironman5 -rb 100

* Per cambiare la modalità di visualizzazione dei LED RGB, scegli tra le seguenti opzioni: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Se imposti la modalità di visualizzazione dei LED RGB su ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, non potrai modificare il colore utilizzando ``pironman5 -rc``.

.. code-block:: shell

  pironman5 -rs breathing

* Per modificare la velocità dell'effetto (intervallo: 0 ~ 100%):

.. code-block:: shell

  pironman5 -rp 80

* La configurazione predefinita include 4 LED RGB. Collega LED aggiuntivi e aggiorna il conteggio utilizzando:

.. code-block:: shell

  pironman5 -rl 12

.. _max_cc_control_fan:

Controllo delle Ventole RGB 
-------------------------------
La scheda di espansione IO supporta fino a due ventole da 5V non-PWM. Entrambe vengono controllate simultaneamente.

.. note::

  Ogni volta che modifichi lo stato del servizio ``pironman5.service``, devi eseguire il seguente comando per applicare le modifiche alla configurazione.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Puoi utilizzare un comando per configurare la modalità operativa delle due ventole RGB. Queste modalità determinano le condizioni in cui le ventole si attiveranno.

Ad esempio, se imposti la modalità su **1: Performance**, le ventole RGB si attiveranno a 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: le ventole RGB si attivano a 70°C.
* **3: Balanced**: le ventole RGB si attivano a 67.5°C.
* **2: Cool**: le ventole RGB si attivano a 60°C.
* **1: Performance**: le ventole RGB si attivano a 50°C.
* **0: Always On**: le ventole RGB restano sempre accese.

* Se colleghi il pin di controllo delle ventole RGB a pin diversi sul Raspberry Pi, puoi usare il comando seguente per modificarne il numero:

.. code-block:: shell

  sudo pironman5 -gp 18


Verifica dello Schermo OLED
-----------------------------------

Dopo aver installato la libreria ``pironman5``, lo schermo OLED visualizzerà informazioni su CPU, RAM, utilizzo del disco, temperatura della CPU e indirizzo IP del Raspberry Pi, mostrandole a ogni riavvio.

Se lo schermo OLED non mostra alcun contenuto, verifica prima che il cavo FPC dell'OLED sia collegato correttamente.

Puoi poi controllare il log del programma per identificare il problema con il seguente comando:

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

Oppure verifica se l'indirizzo i2c 0x3C dello schermo OLED è rilevato:

.. code-block:: shell

  i2cdetect -y 1

Verifica del Ricevitore Infrarossi
---------------------------------------



* Installa il modulo ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Ora testa il ricevitore IR eseguendo il comando:

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Dopo aver eseguito il comando, premi un tasto sul telecomando: verrà stampato il codice corrispondente.

