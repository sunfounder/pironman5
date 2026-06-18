.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============

1. Informazioni sui Sistemi Compatibili
----------------------------------------------------------

Sistemi che hanno superato il test su Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Informazioni sul Pulsante di Accensione
-----------------------------------------------------

Il pulsante di accensione richiama il pulsante di accensione del Raspberry Pi 5 e funziona esattamente come il pulsante di accensione del Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Spegnimento**

  * Se esegui il sistema **Raspberry Pi OS Desktop**, puoi premere il pulsante di accensione due volte rapidamente per spegnere.
  * Se esegui il sistema **Raspberry Pi OS Lite**, premi il pulsante di accensione una volta per avviare lo spegnimento.
  * Per forzare uno spegnimento brusco, tieni premuto il pulsante di accensione.

* **Accensione**

  * Se la scheda Raspberry Pi è spenta, ma ancora alimentata, premi una volta per accendere da uno stato di spegnimento.

* Se stai eseguendo un sistema che non supporta un pulsante di spegnimento, puoi tenerlo premuto per 5 secondi per forzare uno spegnimento brusco, e premerlo una volta per accendere da uno stato di spegnimento.

3. Informazioni sul Raspberry Pi AI HAT+
----------------------------------------------------------------------------------------------------------------

Il Raspberry Pi AI HAT+ non è compatibile con Pironman 5.

   .. image::  img/output3.png
        :width: 400

Il Raspberry Pi AI Kit combina il Raspberry Pi M.2 HAT+ e il modulo acceleratore AI Hailo.

   .. image::  img/output2.jpg
        :width: 400

Puoi staccare il modulo acceleratore AI Hailo dal Raspberry Pi AI Kit e inserirlo direttamente nel modulo NVMe PIP di Pironman 5 MAX.

   .. .. image::  img/output4.png
   ..      :width: 800

4. Informazioni sulle Estremità dei Tubi di Rame del Dissipatore a Torre
----------------------------------------------------------------------------------------------------------------

I tubi di calore a forma di U nella parte superiore del dissipatore a torre sono compressi per facilitare il passaggio dei tubi di rame attraverso le alette in alluminio, il che fa parte del normale processo di produzione dei tubi di rame.

   .. image::  img/tower_cooler1.png

5. Il PI5 non si avvia (LED rosso)?
----------------------------------------------------------------------

Questo problema può essere causato da un aggiornamento del sistema, modifiche all'ordine di avvio o un bootloader corrotto. Puoi provare i seguenti passaggi per risolvere il problema:

#. Controlla la Connessione dell'Adattatore USB-HDMI

   * Controlla attentamente se l'adattatore USB-HDMI è saldamente collegato al PI5.
   * Prova a scollegare e ricollegare l'adattatore USB-HDMI.
   * Quindi ricollega l'alimentazione e verifica se il PI5 si avvia correttamente.

#. Testa il PI5 Fuori dal Case

   * Se ricollegare l'adattatore non risolve il problema:
   * Rimuovi il PI5 dal case Pironman 5.
   * Alimenta il PI5 direttamente con l'alimentatore (senza il case).
   * Controlla se si avvia normalmente.

#. Ripristina il Bootloader

   * Se il PI5 ancora non si avvia, il bootloader potrebbe essere corrotto. Puoi seguire questa guida: :ref:`update_bootloader_promax` e scegliere se avviare da SD card o NVMe/USB.
   * Inserisci la scheda SD preparata nel PI5, accendilo e attendi almeno 10 secondi. Una volta completato il ripristino, rimuovi e riformatta la scheda SD.
   * Quindi, usa Raspberry Pi Imager per scrivere l'ultima versione di Raspberry Pi OS, reinserisci la scheda e prova ad avviare di nuovo.

6. Lo Schermo OLED non Funziona?
---------------------------------------------------------

Se lo schermo OLED non visualizza nulla o visualizza in modo errato, segui questi passaggi di risoluzione:

1. **Controlla la Connessione dello Schermo OLED**

   Assicurati che il cavo FPC dello schermo OLED sia collegato correttamente.

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Oled-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

   .. todo 更新MP4

2. **Controlla la Compatibilità del Sistema Operativo**

   Assicurati di eseguire un sistema operativo compatibile sul tuo Raspberry Pi.

3. **Controlla l'Indirizzo I2C**

   Esegui il seguente comando per verificare se l'indirizzo I2C dell'OLED (0x3C) è riconosciuto:

   .. code-block:: shell

      sudo i2cdetect -y 1

   Se l'indirizzo non viene rilevato, abilita I2C usando il seguente comando:

   .. code-block:: shell

      sudo raspi-config

4. **Riavvia il Servizio pironman5**

   Riavvia il servizio `pironman5` per vedere se risolve il problema:

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **Controlla il File di Log**

   Se il problema persiste, controlla il file di log per eventuali messaggi di errore e fornisci le informazioni al supporto clienti per ulteriori analisi:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

7. Il Modulo NVMe PIP non Funziona?
------------------------------------------------------------------

1. Assicurati che il cavo FPC che collega il modulo NVMe PIP al Raspberry Pi 5 sia saldamente fissato.

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

.. todo 更新MP4

2. Conferma che il tuo SSD sia saldamente fissato al modulo NVMe PIP.

3. Controlla lo stato dei LED del modulo NVMe PIP:

   Dopo aver confermato tutte le connessioni, accendi Pironman 5 MAX e osserva i due indicatori sul modulo NVMe PIP:

   * **PWR LED**: Dovrebbe essere acceso.
   * **STA LED**: Dovrebbe lampeggiare per indicare il normale funzionamento.

   .. image:: img/dual_nvme_pip_leds.png

   * Se il **PWR LED** è acceso ma lo **STA LED** non lampeggia, indica che l'SSD NVMe non è riconosciuto dal Raspberry Pi.
   * Se il **PWR LED** è spento, cortocircuita i pin "Force Enable" sul modulo. Se il **PWR LED** si accende, potrebbe indicare un cavo FPC allentato o una configurazione di sistema non supportata per NVMe.

   .. image:: img/dual_nvme_pip_j4.png

4. Conferma che il tuo SSD NVMe abbia un sistema operativo installato correttamente. Fare riferimento a: :ref:`install_the_os_promax`.

5. Se il cablaggio è corretto e il sistema operativo è installato, ma l'SSD NVMe ancora non si avvia, prova ad avviare da una scheda Micro SD per verificare la funzionalità degli altri componenti. Una volta confermato, procedi a: :ref:`configure_boot_ssd_promax`.

Se il problema persiste dopo aver eseguito i passaggi sopra, invia un'email a service@sunfounder.com. Ti risponderemo il prima possibile.

8. I LED RGB non Funzionano?
-----------------------------------------------------

#. I due pin sull'IO Expander sopra J9 sono usati per collegare i LED RGB a GPIO10. Assicurati che il ponticello su questi due pin sia correttamente posizionato.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifica che il Raspberry Pi stia eseguendo un sistema operativo compatibile. Pironman 5 supporta solo le seguenti versioni di sistema operativo:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Se hai installato un sistema operativo non supportato, segui la guida per installare un sistema operativo compatibile: :ref:`install_the_os_promax`.

#. Esegui il comando ``sudo raspi-config`` per aprire il menu di configurazione. Naviga a **3 Interfacing Options** -> **I3 SPI** -> **YES**, quindi clicca **OK** e **Finish** per abilitare SPI. Dopo aver abilitato SPI, riavvia Pironman 5.

Se il problema persiste dopo aver eseguito i passaggi sopra, invia un'email a service@sunfounder.com. Ti risponderemo il prima possibile.

.. _promax_fan_faq:

9. La ventola non funziona / non può essere controllata?
-------------------------------------------------------------------------

Il Pro / MAX adotta la soluzione ufficiale di controllo della ventola CPU del Raspberry Pi. Tutte e tre le ventole di raffreddamento sono controllate direttamente dal sistema Raspberry Pi e non dipendono dal servizio pironman5 (pertanto, non vedrai opzioni di controllo della ventola nello strumento a riga di comando o nella Dashboard).

**Testare se la ventola funziona correttamente**

Puoi controllare manualmente la ventola usando i seguenti comandi:

.. code-block:: bash

   pinctrl FAN_PWM op dl   # abilita ventola (attivo basso)
   pinctrl FAN_PWM op dh   # disabilita ventola (attivo alto)
   pinctrl FAN_PWM a0      # modalità automatica (controllo temperatura di sistema)

**Controllo della Velocità della ventola in Base alla Temperatura**

La ventola CPU funziona dinamicamente, regolando la sua velocità in base alla temperatura del Raspberry Pi 5:

* **Sotto i 50°C**: Ventola spenta (velocità 0%).
* **A 50°C**: Ventola a bassa velocità (velocità 30%).
* **A 60°C**: Ventola a velocità media (velocità 50%).
* **A 67.5°C**: Ventola ad alta velocità (velocità 70%).
* **A 75°C e oltre**: Ventola a piena velocità (velocità 100%).

10. Come riattivare lo schermo OLED?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Per risparmiare energia e prolungare la durata dello schermo, lo schermo OLED si spegnerà automaticamente dopo un periodo di inattività. Questo fa parte del normale design e non influisce sulla funzionalità del prodotto.

.. note::

   Per la configurazione dello schermo OLED (come accensione/spegnimento, tempo di sospensione, rotazione, ecc.), fare riferimento a: :ref:`promax_view_control_dashboard` o :ref:`promax_view_control_commands`.

11. Come disabilitare la dashboard web?
------------------------------------------------------------------------------------------------------------

Una volta completata l'installazione del modulo ``pironman5``, potrai accedere a :ref:`promax_view_control_dashboard`.

Se non hai bisogno di questa funzionalità e desideri ridurre l'uso di CPU e RAM, puoi disabilitare la dashboard durante l'installazione di ``pironman5`` aggiungendo il flag ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Se hai già installato ``pironman5``, puoi rimuovere il modulo ``dashboard`` e ``influxdb``, quindi riavviare pironman5 per applicare le modifiche:

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. Pironman 5 MAX supporta i sistemi di retro gaming?
.. ------------------------------------------------------------------------------------------------------------
.. Sì, è compatibile. Tuttavia, la maggior parte dei sistemi di retro gaming sono versioni ridotte che non possono installare ed eseguire software aggiuntivo. Questa limitazione può causare il malfunzionamento di alcuni componenti su Pironman 5 MAX, come il display OLED, le due ventole GPIO e i 4 LED RGB, poiché questi componenti richiedono l'installazione dei pacchetti software di Pironman 5 MAX.

.. .. note::

..     Il sistema Batocera.linux è ora completamente compatibile con Pironman 5 MAX. Batocera.linux è una distribuzione di retro gaming open-source e completamente gratuita.

..     * :ref:`promax_install_batocera`
..     * :ref:`promax_set_up_batocera`

12. Come Controllare i Componenti Usando il Comando ``pironman5``
----------------------------------------------------------------------------------------------------------------------------

Puoi fare riferimento al seguente tutorial per controllare i componenti di Pironman 5 MAX usando il comando ``pironman5``.

* :ref:`promax_view_control_commands`

13. Come Cambiare l'Ordine di Avvio del Raspberry Pi Usando i Comandi
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Se sei già collegato al tuo Raspberry Pi, puoi cambiare l'ordine di avvio usando i comandi. Le istruzioni dettagliate sono le seguenti:

* :ref:`configure_boot_ssd_promax`

14. Come Modificare l'Ordine di Avvio con Raspberry Pi Imager?
---------------------------------------------------------------------------------------------------------------------

Oltre a modificare ``BOOT_ORDER`` nella configurazione EEPROM, puoi anche usare **Raspberry Pi Imager** per cambiare l'ordine di avvio del tuo Raspberry Pi.

Si consiglia di usare una scheda di riserva per questo passaggio.

* :ref:`update_bootloader_promax`

15. Come Copiare il Sistema dalla Scheda SD a un SSD NVMe?
-------------------------------------------------------------------------------------------------------------------

Se hai un SSD NVMe ma non hai un adattatore per collegare il tuo NVMe al tuo computer, puoi prima installare il sistema sulla tua scheda Micro SD. Una volta che Pironman 5 MAX si avvia con successo, puoi copiare il sistema dalla tua scheda Micro SD al tuo SSD NVMe. Le istruzioni dettagliate sono le seguenti:

* :ref:`copy_sd_to_nvme_promax`

16. Come Rimuovere la Pellicola Protettiva dalle Lastre Acriliche
-----------------------------------------------------------------------------------------------------------------------

Due pannelli acrilici sono inclusi nella confezione, entrambi coperti da pellicola protettiva gialla/trasparente su entrambi i lati per prevenire graffi. La pellicola protettiva potrebbe essere un po' difficile da rimuovere. Usa un cacciavite per grattare delicatamente gli angoli, quindi stacca con cura l'intera pellicola.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _promax_openssh_powershell:

17. Come Installare OpenSSH tramite Powershell?
--------------------------------------------------------------------------------------------------------

Quando usi ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<indirizzo IP>``) per connetterti al tuo Raspberry Pi, ma appare il seguente messaggio di errore.

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Significa che il tuo sistema computer è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato, devi seguire il tutorial qui sotto per installarlo manualmente.

#. Digita ``powershell`` nella casella di ricerca del tuo desktop Windows, fai clic con il pulsante destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore`` dal menu che appare.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Usa il seguente comando per installare ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Dopo l'installazione, verrà restituito il seguente output.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l'installazione usando il seguente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora ti dice che ``OpenSSH.Client`` è stato installato con successo.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Se il prompt sopra non appare, significa che il tuo sistema Windows è ancora troppo vecchio, e ti consigliamo di installare uno strumento SSH di terze parti, come |link_putty|.

#. Ora riavvia PowerShell e continua a eseguirlo come amministratore. A questo punto potrai accedere al tuo Raspberry Pi usando il comando ``ssh``, dove ti verrà chiesto di inserire la password che hai impostato in precedenza.

   .. image:: img/powershell_login.png

18. Se configuro OMV, posso ancora usare le funzioni di Pironman5?
--------------------------------------------------------------------------------------------------------

Sì, OpenMediaVault è configurato sul sistema Raspberry Pi. Segui i passaggi di :ref:`promax_set_up_pi_os` per continuare la configurazione.

19. La fotocamera del Raspberry Pi non funziona?
-------------------------------------------------------------------------------

Quando la fotocamera non funziona, il 90% dei problemi è legato alla connessione del cavo a nastro o alla fotocamera stessa.

Prima, usa ``rpicam-hello --list-cameras`` per confermare se la fotocamera viene rilevata. Se viene rilevata con successo, dovresti vedere un messaggio simile al seguente:

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

Se la fotocamera non viene rilevata, controlla se il cavo a nastro è invertito o non completamente inserito. Se il problema persiste, prova a sostituire il cavo a nastro o il modulo fotocamera per un test incrociato.