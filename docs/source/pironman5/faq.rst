.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Esplora più a fondo Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi tecnici e post-vendita con l’aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anticipo agli annunci sui nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e promozioni speciali.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

FAQ
============

1. Informazioni sui Sistemi Compatibili
-----------------------------------------

Sistemi testati su Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Informazioni sul Pulsante di Alimentazione
-----------------------------------------------

Il pulsante di accensione estende il pulsante di alimentazione del Raspberry Pi 5 e funziona esattamente come il pulsante di alimentazione originale del Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Spegnimento**

  * Se utilizzi il sistema **Raspberry Pi Bookworm Desktop**, premi due volte rapidamente il pulsante di alimentazione per spegnere il dispositivo.
  * Se utilizzi il sistema **Raspberry Pi Bookworm Lite**, premi una sola volta il pulsante per avviare lo spegnimento.
  * Per un arresto forzato, tieni premuto il pulsante di alimentazione.

* **Accensione**

  * Se la scheda Raspberry Pi è spenta ma ancora alimentata, premi una volta il pulsante per accendere il dispositivo.

* Se stai utilizzando un sistema che non supporta il pulsante di spegnimento, puoi tenerlo premuto per 5 secondi per forzare l'arresto e premere una volta per riaccendere.

3. Direzione del Flusso d'Aria
---------------------------------

Il flusso d’aria nel case Pironman 5 è progettato con precisione per massimizzare l’efficienza del raffreddamento. L'aria fresca entra nel case principalmente attraverso l'interfaccia GPIO e altre piccole aperture, garantendo un'aspirazione uniforme. Successivamente, passa attraverso il Tool Cooler, dotato di una ventola ad alte prestazioni per regolare la temperatura interna, e viene infine espulsa tramite le due ventole RGB posizionate sul pannello laterale.

Per una dimostrazione dettagliata, consulta il video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

4. Informazioni sul Tower Cooler
----------------------------------------------------------

#. I tubi di calore a forma di U sulla parte superiore del tower cooler sono compressi per facilitare il passaggio dei tubi di rame attraverso le alette di alluminio. Questo fa parte del normale processo di produzione.

   .. image::  img/tower_cooler1.png

#. Precauzioni per l’installazione del Tower Cooler:

**Applicare i Pad Termici**: Prima di installare il tower cooler, assicurati di applicare i pad termici sul Raspberry Pi per evitare danni o graffi.

 .. image::  img/tower_cooler_thermal.png

**Orientamento Corretto**: Presta attenzione alla direzione di posizionamento del tower cooler. Allinealo ai fori di posizionamento sul Raspberry Pi prima di premere le viti a molla per fissarlo.

 .. image::  img/tower_cooler_place.jpg

**Rimozione Attenta**: Se il tower cooler è stato installato nella direzione sbagliata o i pad termici non sono stati applicati, non forzare la rimozione.

- Per rimuovere il tower cooler in sicurezza, segui questi passaggi:

  Usa delle pinzette o delle pinze per afferrare la punta del dado a molla e spingilo delicatamente verso l'alto per sganciarlo.

     .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/remove_tower_cooler.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

5. Informazioni sul Raspberry Pi AI HAT+
----------------------------------------------------------

Il Raspberry Pi AI HAT+ non è compatibile con il Pironman 5.

   .. image::  img/output3.png
        :width: 400

Il Raspberry Pi AI Kit combina il Raspberry Pi M.2 HAT+ e il modulo acceleratore AI Hailo.

   .. image::  img/output2.jpg
        :width: 400

Puoi staccare il modulo acceleratore AI Hailo dal Raspberry Pi AI Kit e inserirlo direttamente nel modulo NVMe PIP del Pironman 5.

   .. image::  img/output4.png
        :width: 800

6. PI5 non si avvia (LED rosso)?
-------------------------------------------

Questo problema può essere causato da un aggiornamento del sistema, da modifiche all’ordine di avvio o da un bootloader danneggiato. Puoi provare i seguenti passaggi per risolvere il problema:

#. Controlla la connessione dell’adattatore USB-HDMI

   * Controlla attentamente che l’adattatore USB-HDMI sia collegato saldamente al PI5.
   * Prova a scollegare e ricollegare l’adattatore USB-HDMI.
   * Quindi ricollega l’alimentazione e verifica se il PI5 si avvia correttamente.

#. Testa il PI5 fuori dal case

   * Se ricollegare l’adattatore non risolve il problema:
   * Rimuovi il PI5 dal case Pironman 5.
   * Alimenta direttamente il PI5 con l’alimentatore (senza il case).
   * Controlla se riesce ad avviarsi normalmente.

#. Ripristina il bootloader

   * Se il PI5 continua a non avviarsi, il bootloader potrebbe essere corrotto. Puoi seguire questa guida: :ref:`update_bootloader_5` e scegliere se avviare da scheda SD o da NVMe/USB.
   * Inserisci la scheda SD preparata nel PI5, accendilo e attendi almeno 10 secondi. Una volta completato il ripristino, rimuovi e riformatta la scheda SD.
   * Poi utilizza Raspberry Pi Imager per installare l’ultima versione del Raspberry Pi OS, reinserisci la scheda e prova ad avviare nuovamente.


.. 6. Il Pironman 5 supporta i sistemi di retro gaming?
.. ---------------------------------------------------------
.. Sì, è compatibile. Tuttavia, la maggior parte dei sistemi di retro gaming sono versioni semplificate che non consentono l'installazione e l'esecuzione di software aggiuntivo. Questa limitazione può causare il malfunzionamento di alcuni componenti del Pironman 5, come il display OLED, le due ventole RGB e i 4 LED RGB, poiché richiedono l'installazione dei pacchetti software specifici del Pironman 5.

.. .. note::

..    Il sistema Batocera.linux è ora completamente compatibile con il Pironman 5. Batocera.linux è una distribuzione open-source e completamente gratuita per il retro gaming.

..    * :ref:`install_batocera`
..    * :ref:`set_up_batocera`

7. Lo schermo OLED non funziona?
-----------------------------------

Se il display OLED non mostra nulla o visualizza informazioni errate, segui questi passaggi di risoluzione:

#. Assicurati che il cavo FPC dello schermo OLED sia collegato saldamente. Si consiglia di ricollegare lo schermo OLED e poi accendere il dispositivo.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Verifica che il Raspberry Pi stia eseguendo un sistema operativo compatibile. Il Pironman 5 supporta solo i seguenti sistemi:

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Se hai installato un sistema non supportato, segui la guida per installare un sistema compatibile: :ref:`install_the_os`.

#. Quando lo schermo OLED viene alimentato per la prima volta, potrebbe visualizzare solo blocchi di pixel. È necessario seguire le istruzioni in :ref:`set_up_pironman5` per completare la configurazione prima che possa visualizzare correttamente le informazioni.

#. Usa il seguente comando per verificare se l'indirizzo I2C dello schermo OLED ``0x3C`` viene rilevato:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Se l'indirizzo I2C ``0x3C`` viene rilevato, riavvia il servizio Pironman 5 con questo comando:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Se l'indirizzo non viene rilevato, abilita l'I2C:

     * Modifica il file di configurazione eseguendo:

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Aggiungi la seguente riga alla fine del file:

       .. code-block:: shell


         dtparam=i2c_arm=on

     * Salva il file premendo ``Ctrl+X``, poi ``Y`` ed esci. Riavvia il Pironman 5 e verifica se il problema è risolto.

Se il problema persiste dopo aver eseguito questi passaggi, invia un'email a service@sunfounder.com. Ti risponderemo il prima possibile.

8. Il modulo NVMe PIP non funziona?
---------------------------------------

1. Assicurati che il cavo FPC che collega il modulo NVMe PIP al Raspberry Pi 5 sia collegato correttamente.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

2. Verifica che il tuo SSD sia correttamente fissato al modulo NVMe PIP.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

3. Controlla lo stato dei LED del modulo NVMe PIP:

   Dopo aver verificato tutti i collegamenti, accendi il Pironman 5 e osserva i due indicatori sul modulo NVMe PIP:  

   * **PWR LED**: Deve essere acceso.  
   * **STA LED**: Deve lampeggiare per indicare il funzionamento normale.  

   .. image:: img/nvme_pip_leds.png  

   * Se il **PWR LED** è acceso ma il **STA LED** non lampeggia, significa che l’SSD NVMe non è riconosciuto dal Raspberry Pi.  
   * Se il **PWR LED** è spento, cortocircuita i pin "Force Enable" (J4) sul modulo. Se il **PWR LED** si accende, potrebbe esserci un cavo FPC allentato o una configurazione di sistema non supportata per NVMe.

     .. image:: img/nvme_pip_j4.png  


4. Assicurati che il tuo SSD NVMe abbia un sistema operativo installato correttamente. Consulta: :ref:`install_the_os`.

5. Se il cablaggio è corretto e il sistema operativo è installato, ma l’SSD NVMe non si avvia, prova ad avviare il Raspberry Pi da una Micro SD per verificare il funzionamento degli altri componenti. Una volta confermato, segui la guida: :ref:`configure_boot_ssd`.

Se il problema persiste dopo aver eseguito questi passaggi, invia un'email a service@sunfounder.com. Ti risponderemo il prima possibile.

9. I LED RGB non funzionano?
------------------------------

#. I due pin sull'IO Expander sopra J9 vengono utilizzati per collegare i LED RGB al GPIO10. Assicurati che il jumper su questi due pin sia correttamente posizionato.

   .. image:: img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifica che il Raspberry Pi stia eseguendo un sistema operativo compatibile. Il Pironman 5 supporta solo le seguenti versioni:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Se hai installato un sistema operativo non supportato, segui la guida per installare un sistema compatibile: :ref:`install_the_os`.

#. Esegui il comando ``sudo raspi-config`` per aprire il menu di configurazione. Vai su **3 Interfacing Options** -> **I3 SPI** -> **YES**, quindi clicca su **OK** e **Finish** per abilitare SPI. Dopo aver abilitato SPI, riavvia il Pironman 5.

Se il problema persiste dopo aver eseguito questi passaggi, invia un'email a service@sunfounder.com. Ti risponderemo il prima possibile.

10. La ventola della CPU non funziona?
----------------------------------------------

Quando la temperatura della CPU non ha raggiunto la soglia impostata, la ventola della CPU non si attiva.

**Controllo della velocità della ventola in base alla temperatura**  

La ventola PWM opera dinamicamente, regolando la sua velocità in base alla temperatura del Raspberry Pi 5:  

* **Sotto i 50°C**: La ventola rimane spenta (0% della velocità).  
* **A 50°C**: La ventola funziona a bassa velocità (30% della velocità).  
* **A 60°C**: La ventola aumenta a velocità media (50% della velocità).  
* **A 67,5°C**: La ventola accelera ad alta velocità (70% della velocità).  
* **A 75°C e oltre**: La ventola funziona alla massima velocità (100% della velocità).  

Per maggiori dettagli, fare riferimento a: :ref:`Fans`

11. Come disabilitare il web dashboard?
------------------------------------------------------

Dopo aver completato l'installazione del modulo ``pironman5``, sarà possibile accedere al :ref:`view_control_dashboard`.
      
Se non hai bisogno di questa funzionalità e desideri ridurre il consumo della CPU e della RAM, puoi disabilitare il dashboard durante l'installazione di ``pironman5`` aggiungendo il flag ``--disable-dashboard``.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Se hai già installato ``pironman 5``, puoi rimuovere il modulo ``dashboard`` e ``influxdb``, quindi riavviare pironman5 per applicare le modifiche:
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

12. Come controllare i componenti usando il comando ``pironman5``
----------------------------------------------------------------------

Puoi fare riferimento al seguente tutorial per controllare i componenti del Pironman 5 utilizzando il comando ``pironman5``.

* :ref:`view_control_commands`

13. Come cambiare l'ordine di avvio del Raspberry Pi utilizzando i comandi
-------------------------------------------------------------------------------

Se sei già connesso al tuo Raspberry Pi, puoi modificare l'ordine di avvio utilizzando i comandi. Le istruzioni dettagliate sono le seguenti:

* :ref:`configure_boot_ssd`

14. Come modificare l'ordine di avvio con Raspberry Pi Imager?
-----------------------------------------------------------------

Oltre a modificare il parametro ``BOOT_ORDER`` nella configurazione dell'EEPROM, puoi anche utilizzare il **Raspberry Pi Imager** per cambiare l'ordine di avvio del tuo Raspberry Pi.

Si consiglia di utilizzare una scheda di memoria di riserva per questo passaggio.

* :ref:`update_bootloader_5`

15. Come copiare il sistema dalla scheda SD a un SSD NVMe?
-------------------------------------------------------------

Se disponi di un SSD NVMe ma non hai un adattatore per collegarlo al tuo computer, puoi prima installare il sistema sulla scheda Micro SD. Una volta che il Pironman 5 si avvia correttamente, puoi copiare il sistema dalla scheda Micro SD al tuo SSD NVMe. Le istruzioni dettagliate sono le seguenti:

* :ref:`copy_sd_to_nvme_rpi`

16. Come Rimuovere la Pellicola Protettiva dalle Piastre Acriliche
----------------------------------------------------------------------

Nel pacchetto sono incluse due pannelli acrilici, entrambi rivestiti su entrambi i lati da una pellicola protettiva gialla/trasparente per prevenire graffi. La pellicola protettiva potrebbe essere difficile da rimuovere. Usa un cacciavite per grattare delicatamente gli angoli, quindi stacca con attenzione l'intera pellicola.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center



.. _openssh_powershell:

17. Come Installare OpenSSH tramite PowerShell?
-------------------------------------------------

Se provi a connetterti al tuo Raspberry Pi utilizzando il comando ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``), ma compare il seguente messaggio di errore:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Significa che il tuo sistema operativo è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato. Dovrai quindi installarlo manualmente seguendo la guida qui sotto.

#. Digita ``powershell`` nella barra di ricerca del desktop di Windows, fai clic con il tasto destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore`` dal menu che appare.

   .. image:: img/powershell_ssh.png
      :width: 90%
      
#. Usa il seguente comando per installare ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Dopo l'installazione, dovresti ottenere il seguente output:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l'installazione con il comando:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora il sistema conferma che ``OpenSSH.Client`` è stato installato con successo.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

.. warning:: 
    If the above prompt does not appear, it means that your Windows system is still too old, and you are advised to install a third-party SSH tool, like |link_putty|.

6. Ora riavvia PowerShell ed eseguilo nuovamente come amministratore. A questo punto, potrai accedere al tuo Raspberry Pi utilizzando il comando ``ssh``, che ti chiederà di inserire la password impostata in precedenza.

   .. image:: img/powershell_login.png


.. 18. Perché lo schermo OLED si spegne automaticamente?
.. ---------------------------------------------------------------------------------

.. Per risparmiare energia e prolungare la durata dello schermo, lo schermo OLED si spegne automaticamente dopo un periodo di inattività.  
.. Questo fa parte del normale design e non influisce sulla funzionalità del prodotto.

.. Premi semplicemente una volta il pulsante sul dispositivo per riattivare lo schermo OLED e riprendere la visualizzazione.

.. .. note::

..    Per la configurazione dello schermo OLED (come accensione/spegnimento, tempo di sospensione, rotazione, ecc.), fai riferimento a: :ref:`view_control_dashboard` o :ref:`view_control_commands`.
