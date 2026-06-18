.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _view_control_commands_mini:

Controllo tramite Comandi
========================================

Oltre a visualizzare i dati del Pironman 5 Mini e a controllare i dispositivi dal Dashboard, puoi utilizzare anche i comandi per gestirli.

.. note::

  * Per il sistema **Home Assistant**, puoi monitorare e controllare il Pironman 5 Mini esclusivamente tramite il dashboard aprendo la pagina ``http://<ip>:34001``.
  * È importante notare che qualsiasi modifica alla configurazione richiede il riavvio del servizio con il comando ``pironman5 restart`` per avere effetto.

Visualizzare le Configurazioni di Base
-----------------------------------------------

Il modulo ``pironman5`` offre una serie di configurazioni di base per il Pironman, che puoi consultare con il seguente comando.

.. code-block:: shell

  sudo pironman5 -c

Le configurazioni standard appaiono nel seguente formato:

.. code-block:: 

  {
      "system": {
          "rgb_color": "feff00",
          "rgb_brightness": 30,
          "rgb_style": "hue_cycle",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 12,
          "temperature_unit": "C",
          "gpio_fan_pin": 5,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "follow",
          "gpio_fan_led_pin": 6
      }
  }

Personalizza queste configurazioni secondo le tue esigenze.

Utilizza ``pironman5`` oppure ``pironman5 -h`` per ottenere istruzioni.

.. code-block::


  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] 
                          [{start,restart,stop}]

  Pironman 5 command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                          Debug level
    --background [BACKGROUND]
                          Run in background
    -rd, --remove-dashboard
                          Remove dashboard
    -cp [CONFIG_PATH], --config-path [CONFIG_PATH]
                          Config path
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                          GPIO fan LED state on/off/follow
    -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                          GPIO fan LED pin




.. note::

  Ogni volta che modifichi lo stato del servizio ``pironman5.service``, utilizza il seguente comando per applicare le modifiche.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verifica lo stato del programma ``pironman5`` utilizzando lo strumento ``systemctl``.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* In alternativa, consulta i file di log generati dal programma.

  .. code-block:: shell

    ls /var/log/pironman5/
    cat /var/log/pironman5/main.log

Controllo dei LED RGB
--------------------------
La scheda è dotata di 4 LED RGB WS2812, che possono essere controllati in modo personalizzato. L’utente può accenderli o spegnerli, cambiarne il colore, regolare la luminosità, selezionare lo stile di visualizzazione e modificarne la velocità.

.. note::

  Ogni volta che modifichi lo stato del servizio ``pironman5.service``, utilizza il seguente comando per applicare le modifiche.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Per accendere o spegnere i LED RGB: usa ``true`` per accenderli, ``false`` per spegnerli.

.. code-block:: shell

  sudo pironman5 -re true

* Per cambiarne il colore, inserisci il valore esadecimale desiderato, ad esempio ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Per regolare la luminosità dei LED RGB (intervallo: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* Per cambiare la modalità di visualizzazione dei LED RGB, scegli tra: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Se imposti la modalità di visualizzazione su ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, non potrai modificare il colore con ``sudo pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Per regolare la velocità del cambiamento (intervallo: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rp 80

* La configurazione predefinita include 4 LED RGB. Per collegare LED aggiuntivi e aggiornare il numero, utilizza:

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_mini:

Controllo della ventola GPIO
-----------------------------------

La scheda di espansione IO supporta una ventola da 5V non-PWM.

.. note::

  Ogni volta che modifichi lo stato del servizio ``pironman5.service``, utilizza il seguente comando per applicare le modifiche.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Puoi utilizzare i comandi per configurare la modalità operativa della ventola GPIO. Ogni modalità determina la soglia di temperatura a cui la ventola si attiva.

Ad esempio, se imposti la modalità **1: Performance**, la ventola GPIO si attiverà a 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: la ventola GPIO si attiva a 70°C.
* **3: Balanced**: la ventola GPIO si attiva a 67,5°C.
* **2: Cool**: la ventola GPIO si attiva a 60°C.
* **1: Performance**: la ventola GPIO si attiva a 50°C.
* **0: Always On**: la ventola GPIO rimane sempre accesa.

* Se colleghi il pin di controllo della ventola GPIO a un altro pin del Raspberry Pi, puoi usare il seguente comando per modificarne il numero.

.. code-block:: shell

  sudo pironman5 -gp 18

**Informazioni sulla ventola principale**

La ventola principale si collega a una porta PWM a 4 pin dedicata sul Raspberry Pi 5. La sua strategia di controllo predefinita è uno schema di regolazione intelligente della velocità multilivello gestito dal firmware, basato sulla temperatura della CPU. Ciò significa che quando si utilizza una ventola CPU ufficiale o compatibile e la si collega correttamente, il sistema regolerà automaticamente la velocità della ventola in base alle variazioni di temperatura della CPU (iniziando a funzionare oltre i 50 °C) senza alcun intervento manuale da parte dell'utente.