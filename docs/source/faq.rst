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

Il Pironman 5 supporta i sistemi di gioco retrò?
------------------------------------------------------
Sì, è compatibile. Tuttavia, la maggior parte dei sistemi di gioco retrò sono versioni semplificate che non possono installare ed eseguire software aggiuntivi. Questa limitazione può causare il malfunzionamento di alcuni componenti del Pironman 5, come lo schermo OLED, le due ventole RGB e i 4 LED RGB, poiché richiedono l'installazione dei pacchetti software di Pironman 5.


.. note::

    Il sistema Batocera.linux è ora completamente compatibile con Pironman 5. Batocera.linux è una distribuzione open-source e completamente gratuita per il retro-gaming.

    * :ref:`install_batocera`
    * :ref:`set_up_batocera`

Come controllare i componenti usando il comando ``pironman5``
----------------------------------------------------------------------
Puoi fare riferimento al seguente tutorial per controllare i componenti del Pironman 5 utilizzando il comando ``pironman5``.

* :ref:`view_control_commands`

Come modificare l'ordine di avvio del Raspberry Pi utilizzando i comandi
----------------------------------------------------------------------------

Se hai già effettuato l'accesso al tuo Raspberry Pi, puoi modificare l'ordine di avvio utilizzando i comandi. Le istruzioni dettagliate sono le seguenti:

* :ref:`configure_boot_ssd`


Come modificare l'ordine di avvio con Raspberry Pi Imager?
---------------------------------------------------------------

Oltre a modificare il ``BOOT_ORDER`` nella configurazione dell'EEPROM, puoi anche utilizzare **Raspberry Pi Imager** per cambiare l'ordine di avvio del tuo Raspberry Pi.

È consigliato utilizzare una scheda di riserva per questo passaggio.

* :ref:`update_bootloader`

Come copiare il sistema dalla scheda SD a un NVMe SSD?
-------------------------------------------------------------

Se possiedi un NVMe SSD ma non hai un adattatore per collegarlo al tuo computer, puoi prima installare il sistema sulla tua scheda Micro SD. Una volta che il Pironman 5 si è avviato con successo, puoi copiare il sistema dalla tua scheda Micro SD al tuo NVMe SSD. Le istruzioni dettagliate sono le seguenti:

* :ref:`copy_sd_to_nvme_rpi`


Lo schermo OLED non funziona?
---------------------------------

Se lo schermo OLED non viene visualizzato correttamente o non funziona affatto, segui questi passaggi per risolvere il problema:

Controlla se il cavo FPC dello schermo OLED è collegato correttamente.

#. Usa il seguente comando per visualizzare i log di esecuzione del programma e controllare i messaggi di errore.

   .. code-block:: shell

      cat /opt/pironman5/log

#. In alternativa, usa il seguente comando per verificare se l'indirizzo i2c dello schermo OLED 0x3C è riconosciuto:
    
   .. code-block:: shell
        
        sudo i2cdetect -y 1

#. Se i primi due passaggi non rivelano problemi, prova a riavviare il servizio pironman5 per vedere se il problema viene risolto.


   .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _openssh_powershell:

Installare OpenSSH tramite Powershell
---------------------------------------

Quando utilizzi ``ssh <username>@<hostname>.local`` (oppure ``ssh <username>@<indirizzo IP>``) per connetterti al tuo Raspberry Pi, ma compare il seguente messaggio di errore.

    .. code-block::

        ssh: Il termine 'ssh' non è riconosciuto come il nome di un cmdlet, una funzione, un file di script o un programma eseguibile. Controlla l'ortografia del nome o, se è incluso un percorso, verifica che il percorso sia corretto e riprova.


Significa che il tuo sistema operativo è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato. Dovrai seguire il tutorial qui sotto per installarlo manualmente.

#. Digita ``powershell`` nella barra di ricerca del tuo desktop Windows, fai clic con il pulsante destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore`` dal menu che appare.

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

#. Verifica l'installazione utilizzando il seguente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora ti verrà indicato che ``OpenSSH.Client`` è stato installato correttamente.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Se il prompt sopra non appare, significa che il tuo sistema Windows è ancora troppo vecchio e ti consigliamo di installare uno strumento SSH di terze parti, come |link_putty|.

#. Ora riavvia PowerShell e continua a eseguirlo come amministratore. A questo punto sarai in grado di accedere al tuo Raspberry Pi utilizzando il comando ``ssh``, dove ti verrà richiesto di inserire la password che hai impostato in precedenza.

   .. image:: img/powershell_login.png

