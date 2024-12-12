.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme agli altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni speciali per le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

FAQ
============
1. Sistemi Compatibili
-------------------------------

Sistemi che hanno superato il test sul Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Pulsante di Accensione
--------------------------

Il pulsante di accensione riproduce la funzionalità del pulsante di accensione del Raspberry Pi 5 e funziona nello stesso modo.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Spegnimento**

  * Se utilizzi il sistema **Bookworm Desktop** del Raspberry Pi, puoi premere il pulsante di accensione due volte in rapida successione per spegnere.
  * Se utilizzi il sistema **Bookworm Lite** del Raspberry Pi, premi il pulsante di accensione una sola volta per avviare lo spegnimento.
  * Per forzare uno spegnimento completo, tieni premuto il pulsante di accensione.

* **Accensione**

  * Se la scheda Raspberry Pi è spenta ma ancora alimentata, premilo una volta per accendere da uno stato di spegnimento.

* Se stai utilizzando un sistema che non supporta il pulsante di spegnimento, puoi tenerlo premuto per 5 secondi per forzare uno spegnimento completo e premerlo una volta per accendere da uno stato di spegnimento.

3. Direzione del Flusso d'Aria
-------------------------------

Il flusso d'aria nel case del Pironman 5 è progettato con cura per massimizzare l'efficienza del raffreddamento. L'aria fresca entra principalmente attraverso l'interfaccia GPIO e altre piccole aperture, garantendo un ingresso uniforme. Successivamente, passa attraverso il Tool Cooler, dotato di una ventola ad alte prestazioni per regolare le temperature interne, e viene infine espulsa attraverso le due ventole RGB sul pannello laterale.

Per una dimostrazione dettagliata, consulta il video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Il tuo browser non supporta il tag video.
        </video>
    </div>


4. Il Pironman 5 supporta i sistemi di retro-gaming?
------------------------------------------------------

Sì, è compatibile. Tuttavia, la maggior parte dei sistemi di retro-gaming sono versioni ottimizzate che non possono installare ed eseguire software aggiuntivo. Questa limitazione potrebbe impedire il corretto funzionamento di alcuni componenti del Pironman 5, come il display OLED, le due ventole RGB e i 4 LED RGB, che richiedono l'installazione dei pacchetti software del Pironman 5.

.. note::

   Il sistema Batocera.linux è ora pienamente compatibile con il Pironman 5. Batocera.linux è una distribuzione open-source e completamente gratuita per il retro-gaming.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

5. Lo schermo OLED non funziona?
-----------------------------------

Se lo schermo OLED non si accende o mostra errori di visualizzazione, segui questi passaggi per la risoluzione dei problemi:

#. Assicurati che il cavo FPC dello schermo OLED sia ben collegato. Si consiglia di riconnettere lo schermo OLED e poi accendere il dispositivo.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

#. Conferma che il Raspberry Pi stia utilizzando un sistema operativo compatibile. Il Pironman 5 supporta solo i seguenti sistemi:

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Se hai installato un sistema non supportato, segui la guida per installare un sistema operativo compatibile: :ref:`install_the_os`.

#. Quando lo schermo OLED viene acceso per la prima volta, potrebbe mostrare solo blocchi di pixel. Segui le istruzioni in :ref:`set_up_pironman5` per completare la configurazione e visualizzare correttamente le informazioni.

#. Usa il seguente comando per verificare se l'indirizzo I2C ``0x3C`` dello schermo OLED è rilevato:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Se l'indirizzo I2C ``0x3C`` viene rilevato, riavvia il servizio Pironman 5 utilizzando questo comando:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Abilita I2C se l'indirizzo non è rilevato:

     * Modifica il file di configurazione eseguendo:

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Aggiungi la seguente riga alla fine del file:

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Salva il file premendo ``Ctrl+X``, poi ``Y``, ed esci. Riavvia il Pironman 5 e verifica se il problema è risolto.

Se il problema persiste dopo aver eseguito i passaggi sopra indicati, invia un'e-mail a service@sunfounder.com. Ti risponderemo il prima possibile.

6. Il modulo NVMe PIP non funziona?
---------------------------------------

1. Assicurati che il cavo FPC che collega il modulo NVMe PIP al Raspberry Pi 5 sia ben fissato.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

2. Conferma che il tuo SSD sia ben fissato al modulo NVMe PIP.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

3. Controlla lo stato dei LED del modulo NVMe PIP:

   Dopo aver verificato tutti i collegamenti, accendi il Pironman 5 e osserva i due indicatori sul modulo NVMe PIP:

   * **LED PWR**: Dovrebbe essere acceso.
   * **LED STA**: Dovrebbe lampeggiare per indicare il funzionamento normale.

   .. image:: img/nvme_pip_leds.png  

   * Se il **LED PWR** è acceso ma il **LED STA** non lampeggia, significa che l'SSD NVMe non è riconosciuto dal Raspberry Pi.
   * Se il **LED PWR** è spento, collega i pin "Force Enable" (J4) sul modulo. Se il **LED PWR** si accende, potrebbe esserci un cavo FPC allentato o una configurazione di sistema non supportata per NVMe.

     .. image:: img/nvme_pip_j4.png  

4. Conferma che il tuo SSD NVMe abbia un sistema operativo installato correttamente. Consulta: :ref:`install_the_os`.

5. Se i collegamenti sono corretti e il sistema operativo è installato, ma l'SSD NVMe non si avvia, prova ad avviare da una scheda Micro SD per verificare il funzionamento degli altri componenti. Una volta confermato, procedi a: :ref:`configure_boot_ssd`.

Se il problema persiste dopo aver eseguito i passaggi sopra indicati, invia un'e-mail a service@sunfounder.com. Ti risponderemo il prima possibile.


7. LED RGB non funzionano?
--------------------------

#. I due pin sull'espansore IO sopra J9 sono utilizzati per collegare i LED RGB a GPIO10. Assicurati che il ponticello su questi due pin sia correttamente posizionato.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifica che il Raspberry Pi stia utilizzando un sistema operativo compatibile. Il Pironman 5 supporta solo le seguenti versioni di sistema operativo:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Se hai installato un sistema operativo non supportato, segui la guida per installare un sistema operativo compatibile: :ref:`install_the_os`.

#. Esegui il comando ``sudo raspi-config`` per aprire il menu di configurazione. Vai a **3 Interfacing Options** -> **I3 SPI** -> **YES**, quindi clicca su **OK** e **Finish** per abilitare SPI. Dopo aver abilitato SPI, riavvia il Pironman 5.

Se il problema persiste dopo aver eseguito i passaggi sopra indicati, invia un'e-mail a service@sunfounder.com. Ti risponderemo il prima possibile.

8. Come disabilitare la dashboard web?
------------------------------------------------------

Una volta completata l'installazione del modulo ``pironman5``, potrai accedere alla :ref:`view_control_dashboard`.

Se non hai bisogno di questa funzionalità e vuoi ridurre l'uso di CPU e RAM, puoi disabilitare la dashboard durante l'installazione di ``pironman5`` aggiungendo il flag ``--disable-dashboard``.

.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Se hai già installato ``pironman5``, puoi rimuovere il modulo ``dashboard`` e ``influxdb``, quindi riavviare pironman5 per applicare le modifiche:

.. code-block:: shell
      
   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

9. Come controllare i componenti usando il comando ``pironman5``
----------------------------------------------------------------------

Puoi consultare il seguente tutorial per controllare i componenti del Pironman 5 utilizzando il comando ``pironman5``.

* :ref:`view_control_commands`

10. Come modificare l'ordine di avvio del Raspberry Pi utilizzando i comandi
------------------------------------------------------------------------------------

Se sei già connesso al tuo Raspberry Pi, puoi modificare l'ordine di avvio utilizzando i comandi. Le istruzioni dettagliate sono le seguenti:

* :ref:`configure_boot_ssd`

11. Come modificare l'ordine di avvio con Raspberry Pi Imager?
---------------------------------------------------------------

Oltre a modificare il ``BOOT_ORDER`` nella configurazione EEPROM, puoi anche utilizzare il **Raspberry Pi Imager** per modificare l'ordine di avvio del tuo Raspberry Pi.

Si consiglia di utilizzare una scheda di riserva per questo passaggio.

* :ref:`update_bootloader`

12. Come copiare il sistema dalla scheda SD a un SSD NVMe?
-------------------------------------------------------------

Se hai un SSD NVMe ma non hai un adattatore per collegare l'NVMe al computer, puoi prima installare il sistema sulla scheda Micro SD. Una volta che il Pironman 5 si avvia con successo, puoi copiare il sistema dalla scheda Micro SD al tuo SSD NVMe. Le istruzioni dettagliate sono le seguenti:

* :ref:`copy_sd_to_nvme_rpi`

13. Come rimuovere la pellicola protettiva dalle lastre acriliche
-----------------------------------------------------------------

Nel pacchetto sono incluse due pannelli acrilici, entrambi ricoperti con una pellicola protettiva gialla/trasparente su entrambi i lati per prevenire graffi. La pellicola protettiva può essere un po' difficile da rimuovere. Usa un cacciavite per raschiare delicatamente gli angoli, quindi stacca con attenzione l'intera pellicola.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center


.. _openssh_powershell:

14. Come installare OpenSSH tramite Powershell?
---------------------------------------------------

Quando utilizzi il comando ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) per connetterti al tuo Raspberry Pi, ma appare il seguente messaggio di errore:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Significa che il tuo sistema operativo è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato. Devi seguire il tutorial qui sotto per installarlo manualmente.

#. Digita ``powershell`` nella barra di ricerca del desktop di Windows, fai clic destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore`` dal menu che appare.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Usa il seguente comando per installare ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Dopo l'installazione, verrà mostrato il seguente output:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l'installazione utilizzando il seguente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora ti verrà mostrato che ``OpenSSH.Client`` è stato installato con successo.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Se il messaggio sopra non appare, significa che il tuo sistema Windows è ancora troppo vecchio e ti consigliamo di installare uno strumento SSH di terze parti, come |link_putty|.

#. Ora riavvia PowerShell e continua a eseguirlo come amministratore. A questo punto sarai in grado di accedere al tuo Raspberry Pi utilizzando il comando ``ssh``, dove ti verrà richiesto di inserire la password configurata in precedenza.

   .. image:: img/powershell_login.png

