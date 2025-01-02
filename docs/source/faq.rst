.. note::

    Ciao, benvenuto nella comunità Facebook degli appassionati di SunFounder Raspberry Pi, Arduino ed ESP32! Unisciti a noi per approfondire Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime speciali.
    - **Sconti esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

FAQ
============

1. Sistemi compatibili
-------------------------------

Sistemi testati su Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Pulsante di accensione
----------------------------

Il pulsante di accensione riprende la funzionalità del pulsante del Raspberry Pi 5 e opera nello stesso modo.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Spegnimento**

  * Se utilizzi il sistema Raspberry Pi **Bookworm Desktop**, premi due volte rapidamente il pulsante di accensione per spegnere.
  * Se utilizzi il sistema Raspberry Pi **Bookworm Lite**, premi una volta per avviare lo spegnimento.
  * Per uno spegnimento forzato, tieni premuto il pulsante.

* **Accensione**

  * Se il Raspberry Pi è spento ma alimentato, premi una volta per accenderlo.

* Per sistemi che non supportano il pulsante di spegnimento, tieni premuto per 5 secondi per forzare lo spegnimento e premi una volta per accenderlo.

3. Direzione del flusso d'aria
---------------------------------

Il flusso d'aria nel case Pironman 5 è progettato per massimizzare l'efficienza di raffreddamento. L'aria fresca entra principalmente attraverso l'interfaccia GPIO e altre piccole aperture, per poi attraversare il Tool Cooler dotato di una ventola ad alte prestazioni. Infine, l'aria viene espulsa attraverso le due ventole RGB sul pannello laterale.

Per una dimostrazione dettagliata, consulta il video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Il tuo browser non supporta il tag video.
        </video>
    </div>

4. Estremità dei tubi di rame del Tower Cooler
----------------------------------------------------------

I tubi a forma di U nella parte superiore del Tower Cooler sono compressi per consentire il passaggio attraverso le alette di alluminio, una fase normale del processo di produzione.

   .. image::  img/tower_cooler1.png

5. Il Pironman 5 supporta i sistemi retro gaming?
------------------------------------------------------

Sì, è compatibile. Tuttavia, la maggior parte dei sistemi retro gaming sono versioni ottimizzate che non consentono l'installazione di software aggiuntivo. Questa limitazione potrebbe impedire il funzionamento di alcuni componenti del Pironman 5, come il display OLED, le due ventole RGB e i 4 LED RGB, che richiedono l'installazione dei pacchetti software del Pironman 5.

.. note::

   Il sistema Batocera.linux è ora pienamente compatibile con Pironman 5. Batocera.linux è una distribuzione retro-gaming open-source completamente gratuita.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

6. Lo schermo OLED non funziona?
-----------------------------------

Se lo schermo OLED non visualizza nulla o visualizza in modo errato, segui questi passaggi:

#. Assicurati che il cavo FPC dello schermo OLED sia collegato saldamente. Si consiglia di ricollegare lo schermo OLED e poi accendere il dispositivo.

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

   Se hai installato un sistema non supportato, segui la guida per installare un OS compatibile: :ref:`install_the_os`.

#. Alla prima accensione dello schermo OLED, potrebbe visualizzare solo blocchi di pixel. Segui le istruzioni in :ref:`set_up_pironman5` per completare la configurazione e consentire una corretta visualizzazione.

#. Usa il seguente comando per verificare se l'indirizzo I2C ``0x3C`` dello schermo OLED è rilevato:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Se l'indirizzo I2C ``0x3C`` viene rilevato, riavvia il servizio Pironman 5 con questo comando:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Abilita I2C se l'indirizzo non viene rilevato:

     * Modifica il file di configurazione eseguendo:

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Aggiungi la seguente riga alla fine del file:

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Salva il file premendo ``Ctrl+X``, quindi ``Y`` e chiudi. Riavvia il Pironman 5 e verifica se il problema è risolto.

Se il problema persiste dopo aver seguito i passaggi sopra indicati, invia un'email a service@sunfounder.com. Risponderemo il prima possibile.

7. Modulo NVMe PIP non funzionante?
---------------------------------------

1. Assicurati che il cavo FPC che collega il modulo NVMe PIP al Raspberry Pi 5 sia saldamente collegato.

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

2. Conferma che il tuo SSD sia correttamente fissato al modulo NVMe PIP.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

3. Controlla lo stato dei LED del modulo NVMe PIP:

   Dopo aver verificato tutte le connessioni, accendi il Pironman 5 e osserva i due indicatori sul modulo NVMe PIP:

   * **LED PWR**: Dovrebbe essere acceso.
   * **LED STA**: Dovrebbe lampeggiare per indicare il funzionamento normale.

   .. image:: img/nvme_pip_leds.png  

   * Se il **LED PWR** è acceso ma il **LED STA** non lampeggia, significa che l'SSD NVMe non è riconosciuto dal Raspberry Pi.
   * Se il **LED PWR** è spento, cortocircuita i pin "Force Enable" (J4) sul modulo. Se il **LED PWR** si accende, potrebbe indicare un cavo FPC allentato o una configurazione di sistema non supportata per NVMe.

     .. image:: img/nvme_pip_j4.png  

4. Conferma che il tuo SSD NVMe abbia un sistema operativo correttamente installato. Consulta: :ref:`install_the_os`.

5. Se il cablaggio è corretto e l'OS è installato, ma l'SSD NVMe non si avvia ancora, prova ad avviare da una scheda Micro SD per verificare la funzionalità degli altri componenti. Una volta confermato, procedi con: :ref:`configure_boot_ssd`.

Se il problema persiste dopo aver seguito i passaggi precedenti, invia un'email a service@sunfounder.com. Ti risponderemo al più presto.


8. LED RGB non funzionanti?
-------------------------------

#. I due pin sull'IO Expander sopra J9 sono utilizzati per collegare i LED RGB a GPIO10. Assicurati che il ponticello su questi due pin sia correttamente posizionato.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifica che il Raspberry Pi stia utilizzando un sistema operativo compatibile. Il Pironman 5 supporta solo le seguenti versioni di OS:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Se hai installato un OS non supportato, segui la guida per installare un sistema operativo compatibile: :ref:`install_the_os`.

#. Esegui il comando ``sudo raspi-config`` per aprire il menu di configurazione. Naviga su **3 Interfacing Options** -> **I3 SPI** -> **YES**, quindi clicca su **OK** e **Finish** per abilitare SPI. Dopo aver abilitato SPI, riavvia il Pironman 5.

Se il problema persiste dopo aver eseguito i passaggi precedenti, invia un'email a service@sunfounder.com. Ti risponderemo al più presto.

9. La ventola della CPU non funziona?
----------------------------------------------

Quando la temperatura della CPU non ha raggiunto la soglia impostata, la ventola della CPU non si attiva.

**Controllo della velocità della ventola in base alla temperatura**  

La ventola PWM opera dinamicamente, regolando la velocità in base alla temperatura del Raspberry Pi 5:

* **Sotto i 50°C**: La ventola rimane spenta (0% di velocità).
* **A 50°C**: La ventola opera a bassa velocità (30% di velocità).
* **A 60°C**: La ventola aumenta a velocità media (50% di velocità).
* **A 67,5°C**: La ventola raggiunge alta velocità (70% di velocità).
* **A 75°C e oltre**: La ventola opera a piena velocità (100% di velocità).

Per maggiori dettagli consulta: :ref:`Fans`

10. Come disabilitare la dashboard web?
------------------------------------------------------

Dopo aver completato l'installazione del modulo ``pironman5``, potrai accedere alla :ref:`view_control_dashboard`.
      
Se non hai bisogno di questa funzionalità e desideri ridurre l'uso della CPU e della RAM, puoi disabilitare la dashboard durante l'installazione di ``pironman5`` aggiungendo il flag ``--disable-dashboard``.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Se hai già installato ``pironman5``, puoi rimuovere il modulo ``dashboard`` e ``influxdb``, quindi riavviare pironman5 per applicare le modifiche:
      
.. code-block:: shell
      
   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

11. Come controllare i componenti usando il comando ``pironman5``
----------------------------------------------------------------------

Puoi fare riferimento al seguente tutorial per controllare i componenti del Pironman 5 usando il comando ``pironman5``:

* :ref:`view_control_commands`

12. Come modificare l'ordine di avvio del Raspberry Pi utilizzando i comandi
----------------------------------------------------------------------------------

Se sei già collegato al tuo Raspberry Pi, puoi modificare l'ordine di avvio utilizzando i comandi. Le istruzioni dettagliate sono le seguenti:

* :ref:`configure_boot_ssd`

13. Come modificare l'ordine di avvio con Raspberry Pi Imager?
-----------------------------------------------------------------

Oltre a modificare il parametro ``BOOT_ORDER`` nella configurazione EEPROM, puoi anche utilizzare il **Raspberry Pi Imager** per cambiare l'ordine di avvio del tuo Raspberry Pi.

Si consiglia di utilizzare una scheda di riserva per questo passaggio.

* :ref:`update_bootloader`

14. Come copiare il sistema dalla scheda SD a un SSD NVMe?
--------------------------------------------------------------

Se possiedi un SSD NVMe ma non disponi di un adattatore per collegare l'SSD NVMe al tuo computer, puoi prima installare il sistema sulla tua scheda Micro SD. Una volta che il Pironman 5 si è avviato correttamente, puoi copiare il sistema dalla scheda Micro SD all'SSD NVMe. Le istruzioni dettagliate sono le seguenti:

* :ref:`copy_sd_to_nvme_rpi`

15. Come rimuovere la pellicola protettiva dai pannelli acrilici
--------------------------------------------------------------------

Nel pacchetto sono inclusi due pannelli acrilici, entrambi ricoperti da una pellicola protettiva gialla/trasparente su entrambi i lati per prevenire graffi. La pellicola protettiva potrebbe essere un po' difficile da rimuovere. Usa un cacciavite per raschiare delicatamente gli angoli, quindi rimuovi con cura l'intera pellicola.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center


.. _openssh_powershell:

16. Come installare OpenSSH tramite PowerShell
----------------------------------------------------

Quando tenti di usare ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) per connetterti al tuo Raspberry Pi, potrebbe apparire il seguente messaggio di errore:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Ciò significa che il tuo sistema operativo è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato. Segui il tutorial sottostante per installarlo manualmente.

#. Digita ``powershell`` nella barra di ricerca del tuo desktop Windows, fai clic con il pulsante destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore`` dal menu che appare.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Usa il seguente comando per installare ``OpenSSH.Client``:

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Dopo l'installazione, verrà mostrata la seguente uscita:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l'installazione usando il seguente comando:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora dovrebbe indicarti che ``OpenSSH.Client`` è stato installato correttamente:

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning::
        Se non appare la suddetta informazione, significa che il tuo sistema Windows è ancora troppo vecchio. Si consiglia di installare uno strumento SSH di terze parti, come |link_putty|.

#. Riavvia PowerShell ed eseguilo nuovamente come amministratore. Ora sarai in grado di accedere al tuo Raspberry Pi usando il comando ``ssh``, dove ti verrà richiesto di inserire la password configurata in precedenza.

   .. image:: img/powershell_login.png

17. Come accendere/spegnere lo schermo OLED
-----------------------------------------------

Puoi scegliere di accendere o spegnere lo schermo OLED tramite il pannello di controllo o la riga di comando.

1. Accendere/spegnere lo schermo OLED dal pannello di controllo.

   .. note::

    Prima di usare il pannello di controllo, è necessario configurarlo in Home Assistant. Consulta: :ref:`view_control_dashboard`.

- Una volta completata la configurazione, segui questi passaggi per accendere, spegnere o configurare il tuo schermo OLED.

   .. image:: img/set_up_on_dashboard.jpg
      :width: 90%

2. Accendere/spegnere lo schermo OLED dalla riga di comando.

- Usa il seguente comando per accendere o spegnere lo schermo OLED:

.. code-block::

    sudo pironman5 -oe on/off

.. note::

    Potresti dover riavviare il servizio pironman5 affinché le modifiche abbiano effetto. Usa il seguente comando per riavviare il servizio:

      .. code-block::

        sudo systemctl restart pironman5.service
