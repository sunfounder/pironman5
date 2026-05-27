.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _max_view_control_commands:

Controllo con Comandi
========================================
Oltre a visualizzare i dati del Pironman 5 MAX e controllare i vari dispositivi tramite la Dashboard, puoi anche usare comandi per gestirli.

.. note::

  * Per il sistema **Home Assistant**, puoi solo monitorare e controllare il Pironman 5 MAX tramite la dashboard, aprendo la pagina web ``http://<ip>:34001``.

Visualizzare le Configurazioni di Base
-----------------------------------------

Il modulo ``pironman5`` offre configurazioni di base per Pironman, che puoi consultare con il seguente comando.

.. code-block:: shell

  sudo pironman5 -c

Le configurazioni standard appaiono come segue:

.. code-block::

  {
      "system": {
          "data_interval": 1,
          "database_retention_days": 30,
          "temperature_unit": "C",
          "enable_history": true,
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "rgb_enable": true,
          "rgb_color": "#0a1aff",
          "rgb_brightness": 100,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_led_count": 4,
          "rgb_led_count_min": 4,
          "gpio_fan_pin": 6,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "on",
          "gpio_fan_led_pin": 5,
          "debug_level": "INFO"
      }
  }

Personalizza queste configurazioni in base alle tue esigenze.

Usa ``pironman5`` o ``pironman5 -h`` per le istruzioni.

.. code-block::


  usage: pironman5-service [-h] [-v] [-c] [-dl [{debug,info,warning,error,critical}]] [--background [BACKGROUND]] [-rd] [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-oe [OLED_ENABLE]]
                          [-od [OLED_DISK]] [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]]
                          [{start,restart,stop}]

  Interfaccia a riga di comando Pironman 5 MAX

  argomenti posizionali:
    {start,restart,stop}  Comando

  opzioni:
    -h, --help            Mostra questo messaggio di aiuto ed esci
    -v, --version         Mostra la versione
    -c, --config          Mostra la configurazione
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Giorni di conservazione del database
    -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                          Livello di debug
    -rd, --remove-dashboard
                          Rimuovi dashboard
    -cp, --config-path [CONFIG_PATH]
                          Percorso configurazione
    -eh, --enable-history [ENABLE_HISTORY]
                          Abilita cronologia, True/true/on/On/1 o False/false/off/Off/0
    -re, --rgb-enable [RGB_ENABLE]
                          Abilita RGB True/False
    -rs, --rgb-style [RGB_STYLE]
                          Stile RGB: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
    -rc, --rgb-color [RGB_COLOR]
                          Colore RGB in formato esadecimale senza # (es. 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          Luminosità RGB 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          Velocità RGB 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          Numero LED RGB (intero)
    -u, --temperature-unit [{C,F}]
                          Unità di temperatura
    -gm, --gpio-fan-mode [GPIO_FAN_MODE]
                          Modalità ventola GPIO, 0: Sempre attiva, 1: Prestazioni, 2: Fresco, 3: Bilanciato, 4: Silenzioso
    -gp, --gpio-fan-pin [GPIO_FAN_PIN]
                          Pin ventola GPIO
    -oe, --oled-enable [OLED_ENABLE]
                          Abilita OLED True/true/on/On/1 o False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Ruota display OLED, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          Pagine OLED, separate da ',': mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          Timeout sospensione OLED in secondi

  Sottocomandi:
    {start,stop,launch-browser}
      start               Avvia Pironman5
      stop                Ferma Pironman5
      launch-browser      Avvia browser

.. note::

   Ogni volta che modifichi lo stato di ``pironman5.service``, devi usare il seguente comando per applicare le modifiche alla configurazione.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

* Verifica lo stato del programma ``pironman5`` usando lo strumento ``systemctl``.

  .. code-block:: shell

     sudo systemctl status pironman5.service

* In alternativa, ispeziona i file di log generati dal programma.

  .. code-block:: shell

     cat /var/log/pironman5/pironman5.log


Controllo dei LED RGB
----------------------
La scheda dispone di 4 LED RGB WS2812, con controllo personalizzabile. Puoi accenderli o spegnerli, cambiare colore, regolare la luminosità, cambiare modalità di visualizzazione e impostare la velocità delle animazioni.

.. note::

  Ogni volta che modifichi lo stato di ``pironman5.service``, devi usare il seguente comando per applicare le modifiche alla configurazione.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Per modificare lo stato di accensione dei LED RGB, usa ``true`` per accenderli o ``false`` per spegnerli.

.. code-block:: shell

  sudo pironman5 -re true

* Per cambiare il loro colore, inserisci il valore esadecimale desiderato, ad esempio ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Per modificare la luminosità dei LED RGB (intervallo: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* Per cambiare la modalità di visualizzazione dei LED RGB, scegli tra: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Se imposti la modalità di visualizzazione su ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, non potrai impostare il colore con ``pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Per modificare la velocità di cambiamento (intervallo: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rp 80

* La configurazione predefinita include 4 LED RGB. Collega LED aggiuntivi e aggiorna il conteggio usando:

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_max:

Controllo delle Ventole GPIO
-----------------------------------
La scheda di espansione IO supporta fino a due ventole 5V non-CPU. Entrambe le ventole sono controllate insieme.

.. note::

  Ogni volta che modifichi lo stato di ``pironman5.service``, devi usare il seguente comando per applicare le modifiche alla configurazione.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Puoi configurare la modalità operativa delle due ventole GPIO usando i comandi. Queste modalità determinano le condizioni in cui le ventole GPIO si attiveranno.

Ad esempio, se impostata sulla modalità **1: Prestazioni**, le ventole GPIO si attiveranno a 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Silenzioso**: Le ventole GPIO si attiveranno a 70°C.
* **3: Bilanciato**: Le ventole GPIO si attiveranno a 67,5°C.
* **2: Fresco**: Le ventole GPIO si attiveranno a 60°C.
* **1: Prestazioni**: Le ventole GPIO si attiveranno a 50°C.
* **0: Sempre attive**: Le ventole GPIO rimarranno sempre accese.

* Se colleghi il pin di controllo della ventola RGB a un pin GPIO diverso del Raspberry Pi, puoi cambiare il numero del pin con:

  .. code-block:: shell

     sudo pironman5 -gp 18


Informazioni sulla Ventola CPU
--------------------------------

La ventola CPU si collega a una porta dedicata a 4 pin per ventola CPU sul Raspberry Pi 5.

La sua strategia di controllo predefinita è uno schema di regolazione intelligente della velocità a più livelli gestito dal firmware, basato sulla temperatura della CPU. Quando usi una ventola CPU ufficiale o compatibile e la colleghi correttamente, il sistema regolerà automaticamente la velocità in base ai cambiamenti di temperatura della CPU (a partire da ``50°C``) senza richiedere intervento manuale.


Verifica dello Schermo OLED
-------------------------------

Quando la libreria ``pironman5`` è installata, lo schermo OLED mostra automaticamente l'utilizzo della CPU, della RAM, del disco, la temperatura della CPU e l'indirizzo IP del Raspberry Pi dopo ogni riavvio.

Se lo schermo OLED non mostra alcun contenuto, controlla prima che il cavo FPC dell'OLED sia collegato correttamente.

Poi ispeziona il log del programma usando il seguente comando:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

Puoi anche verificare se l'indirizzo I2C ``0x3C`` dell'OLED viene rilevato:

.. code-block:: shell

   i2cdetect -y 1


Verifica del Ricevitore a Infrarossi
---------------------------------------

* Installa il modulo ``lirc``:

  .. code-block:: shell

     sudo apt-get install lirc -y

* Testa il ricevitore IR usando il seguente comando:

  .. code-block:: shell

     mode2 -d /dev/lirc0

* Dopo aver eseguito il comando, premi un pulsante sul telecomando. Il codice IR corrispondente verrà stampato nel terminale.
