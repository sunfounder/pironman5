.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche grazie al supporto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e iniziative promozionali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

Pironman 5 Mini HAT
===========================================


.. image:: img/pironman5mini_hat.png

LED RGB
------------

.. image:: img/io_board_rgb.png

La scheda integra 4 LED RGB WS2812, 
con controllo completamente personalizzabile. 
Gli utenti possono accenderli o spegnerli, modificarne il colore, 
regolare la luminosità, cambiare le modalità di visualizzazione e impostare la velocità degli effetti.

* Per accendere o spegnere i LED RGB, usa ``true`` per accenderli, ``false`` per spegnerli.

.. code-block:: shell

  sudo pironman5 -re true

* Per modificarne il colore, inserisci un valore esadecimale come ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Per regolare la luminosità (intervallo: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* Per cambiare modalità di visualizzazione, scegli tra: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Se imposti la modalità su ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, non potrai cambiare il colore tramite ``sudo pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Per regolare la velocità degli effetti (intervallo: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rp 80

Pin di Controllo RGB
-------------------------

Il controllo dei LED RGB avviene tramite SPI, connessi a **GPIO10**, che corrisponde al pin MOSI SPI. 
Due pin sono utilizzati per collegare i LED a GPIO10. Se non necessari, i ponticelli possono essere rimossi.

.. image:: img/io_board_rgb_pin.png

Pin di Uscita RGB
-------------------------

.. image:: img/io_board_rgb_out.png

I LED WS2812 supportano connessioni in serie, permettendo l'aggiunta di una striscia LED RGB esterna. Collega il pin **SIG** della scheda al pin **DIN** della striscia esterna.

La configurazione predefinita prevede 4 LED RGB. Per aggiungerne altri, aggiorna il numero con:

.. code-block:: shell

  sudo pironman5 -rl 12



Pin della Ventola RGB
----------------------------

La scheda di espansione IO supporta una ventola da 5V non-PWM. 

Collega i fili della ventola alla porta FAN.

.. image:: img/io_board_fan.png

I due gruppi di pin sotto J9 abilitano il controllo della ventola e dei suoi LED. Di default, i ponticelli sono inseriti per permettere a GPIO6 e GPIO5 di controllarne accensione e spegnimento. Se non desideri controllare la ventola o i LED, rimuovi i ponticelli corrispondenti per liberare GPIO6 o GPIO5.

.. image:: img/io_board_fan_j9.png

Puoi configurare la modalità operativa della ventola RGB tramite comando. Le modalità determinano le condizioni di attivazione della ventola.

  Ad esempio, impostando la modalità **1: Performance**, la ventola RGB si attiverà a 50°C.

  .. code-block:: shell

    sudo pironman5 -gm 3

  * **4: Quiet**: la ventola si attiva a 70°C.
  * **3: Balanced**: la ventola si attiva a 67,5°C.
  * **2: Cool**: la ventola si attiva a 60°C.
  * **1: Performance**: la ventola si attiva a 50°C.
  * **0: Always On**: la ventola resta sempre accesa.

Se colleghi il pin di controllo della ventola RGB a un altro pin del Raspberry Pi, puoi modificarlo con:

.. code-block:: shell

  sudo pironman5 -gp 18


Convertitore Interruttore di Alimentazione
------------------------------------------------

**Aggiunta del Pulsante di Accensione**

* Il Raspberry Pi 5 dispone di un jumper **J2**, situato tra il connettore della batteria RTC e il bordo della scheda. Collegando un pulsante momentaneo NO ai due pad, è possibile aggiungere un pulsante di accensione personalizzato.

  .. image:: img/pi5_j2.jpg

* Il Pironman 5 Mini estende il jumper **J2** a un pulsante esterno tramite due pin a molla (Pogo pins).

  .. image:: img/power_switch_j2.jpeg

  .. image:: img/power_switch_j2_2.jpeg

* Ora è possibile accendere e spegnere il Raspberry Pi 5 utilizzando il pulsante.

  .. image:: img/pironman_button.JPG

**Ciclo di Alimentazione**

All’avvio iniziale, il Raspberry Pi 5 si accende automaticamente senza bisogno di premere il pulsante.

Se è in esecuzione il Raspberry Pi Desktop, una breve pressione sul pulsante avvia uno spegnimento sicuro. Apparirà un menu con opzioni per spegnere, riavviare o disconnettere. Scegli un'opzione oppure premi di nuovo per procedere con lo spegnimento.

.. image:: img/button_shutdown.png

**Spegnimento**

  * Se utilizzi il sistema **Raspberry Pi OS Desktop**, premi il pulsante due volte velocemente per spegnere.
  * Se utilizzi **Raspberry Pi OS Lite** (senza desktop), premi il pulsante una sola volta per avviare lo spegnimento.
  * Per forzare lo spegnimento, tieni premuto il pulsante.


**Accensione**

  * Se la scheda Raspberry Pi è spenta ma alimentata, premi una volta per accenderla.

.. note::

    Se il tuo sistema non supporta lo spegnimento tramite pulsante, tienilo premuto per 5 secondi per spegnere forzatamente e premi una volta per riaccendere.




Modulo NVMe
-------------------------------------------


Il Pironman 5 Mini integra un modulo adattatore PCIe per SSD NVMe. Supporta quattro formati: 2230, 2242, 2260 e 2280, tutti compatibili con slot M.2 M key.

.. image:: img/nvme_p.png


* **STA**: Indicatore LED di stato  
* **PWR**: Indicatore LED di alimentazione  

  .. image:: img/nvme_led.png

* Il modulo si collega tramite un cavo FFC 0,5mm 16P inverso o un cavo FPC personalizzato con impedenza controllata.

  .. image:: img/nvme_pcie.png

* **FORCE ENABLE**: L’alimentazione integrata si attiva tramite un segnale dallo slot PCIe. Dopo l'accensione, il Raspberry Pi invia un segnale per attivare l’alimentazione 3,3V. Se il sistema non supporta tale segnale, è possibile cortocircuitare il jumper J2 FORCE ENABLE saldando un filo per forzare l'alimentazione del modulo NVMe.

  .. image:: img/nvme_j2.png

**Informazioni sul Modello**

Gli SSD M.2, compatti e ad alte prestazioni, si distinguono per chiave (B, M, B+M) e interfaccia (SATA o PCIe).  

* **M.2 SATA SSD**: usano l’interfaccia SATA, simile agli SSD da 2,5", con velocità fino a 600 MB/s. Compatibili con slot B e M key.  
* **M.2 NVMe SSD**: utilizzano il protocollo NVMe su interfaccia PCIe, offrendo prestazioni elevate per gaming, editing video e carichi intensivi. Richiedono slot M key e supportano PCIe 3.0, 4.0, 5.0. Raspberry Pi 5 supporta PCIe 3.0, fino a 3.500 MB/s.

Gli SSD M.2 sono disponibili in versioni B key, M key e B+M key. Il tipo B+M combina entrambi gli standard.  

.. image:: img/ssd_key.png


In generale, gli SSD SATA sono B+M key, mentre gli NVMe per PCIe 3.0 x4 sono M key.

.. image:: img/ssd_model2.png

**Informazioni sulla Lunghezza**

I moduli M.2 sono disponibili in varie lunghezze e possono essere utilizzati anche per Wi-Fi, WWAN, Bluetooth, GPS e NFC.

Pironman 5 supporta quattro formati NVMe PCIe Gen 2.0 / Gen 3.0: 2230, 2242, 2260 e 2280. Il numero "22" indica la larghezza (in mm), i successivi la lunghezza. Moduli più lunghi offrono maggiore capacità.


.. image:: img/m2_ssd_size.png
  :width: 600


Portabatteria 1220RTC
---------------------------------

.. image:: img/battery_holder.png


Il portabatteria 1220RTC integrato consente l’installazione di una batteria RTC, collegandosi all’interfaccia RTC del Raspberry Pi tramite cavo SH1.0 2P inverso.

È compatibile con batterie CR1220 e ML1220. La ML1220 può essere ricaricata dal Raspberry Pi. La CR1220 non è ricaricabile.

**Abilitare la Carica Lenta**

.. warning::

  Non abilitare la carica lenta con batterie CR1220: può danneggiarle irreparabilmente e compromettere la scheda.

Di default, la carica lenta è disattivata. I file ``sysfs`` mostrano la tensione di carica corrente:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Per abilitare la carica lenta, aggiungi ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``:

  * Apri ``/boot/firmware/config.txt``.

    .. code-block:: shell

      sudo nano /boot/firmware/config.txt

  * Aggiungi ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``.

    .. code-block:: shell

      dtparam=rtc_bbat_vchg=3000000

Dopo il riavvio, verifica:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Per disattivare, rimuovi la riga ``dtparam`` da ``config.txt``.



Header GPIO
--------------

.. image:: img/io_board_pin_header.png

Due connettori angolati espandono i GPIO del Raspberry Pi. Nota: il ricevitore IR, i LED RGB e la ventola utilizzano alcuni pin. Rimuovi i ponticelli corrispondenti per liberare i pin.

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 Mini
    - Raspberry Pi 5
  * - FAN (Opzionale)
    - GPIO6
  * - FAN RGB (Opzionale)
    - GPIO5
  * - RGB (Opzionale)
    - GPIO10