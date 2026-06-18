.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Risoluzione Rapida dei Problemi
-------------------------------

* Pulsante di accensione non funzionante → :ref:`faq_power_button_not_work_promax`
* Schermo OLED non funzionante → :ref:`faq_oled_promax`
* LED RGB non funzionanti → :ref:`faq_rgb_promax`
* Ventola non funzionante → :ref:`promax_fan_faq`
* La Dashboard non mostra dati → :ref:`faq_dashboard_promax`
* SSD NVMe non rilevato → :ref:`faq_nvme_promax`
* SSD NVMe rilevato ma causa riavvio del sistema → :ref:`faq_nvme_link_down_promax`
* PI5 non si avvia → :ref:`faq_pi5_boot_fail_promax`



1. Hardware
-------------------------------


.. _com_os_promax:

Sistemi Compatibili
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_promax`

Pulsante di Accensione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_promax:

Pulsante di Accensione Non Funzionante?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Estremità dei Tubi di Rame del Dissipatore a Torre
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Raspberry Pi AI HAT+ non è compatibile con Pironman 5 Pro MAX.

.. image:: img/output3.png
    :width: 400

Il Raspberry Pi AI Kit combina il Raspberry Pi M.2 HAT+ e il modulo acceleratore AI Hailo.

.. image:: img/output2.jpg
    :width: 400

Puoi staccare il modulo acceleratore AI Hailo dal Raspberry Pi AI Kit e inserirlo direttamente nel modulo NVMe PIP di Pironman 5 Pro MAX.


Lo Schermo da 4,3 Pollici è Nero / Non Visualizza?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lo schermo DSI da 4,3 pollici è plug-and-play — non è richiesta l'installazione di driver aggiuntivi.

.. note::

   Il jumper **ON/AUTO** sulla scheda HDMI/USB controlla solo l'uscita audio dell'altoparlante. **Non ha alcun effetto** sul display dello schermo.

Se lo schermo è nero o non visualizza, controlla quanto segue:

#. Assicurati che il cavo a nastro DSI sia collegato alla porta DSI corretta sul Raspberry Pi 5.

#. Verifica che il cavo a nastro sia completamente inserito, che il morsetto sia premuto saldamente e che i contatti siano orientati nella direzione corretta.

#. Esegui il seguente comando per confermare se il sistema rileva lo schermo DSI:

   .. code-block:: shell

      sudo dmesg | grep -i dsi

   Se lo schermo viene rilevato, dovresti vedere un output simile a ``DSI display found``. Se non c'è output, lo schermo non viene riconosciuto — ricontrolla la connessione fisica.


Schermo HDMI Esterno — La Barra delle Applicazioni Appare Solo sullo Schermo da 4,3 Pollici?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando colleghi un monitor HDMI esterno a Pironman 5 Pro MAX, la barra delle applicazioni del desktop potrebbe rimanere sullo schermo DSI integrato da 4,3 pollici invece di spostarsi sul display esterno. Questo accade perché il sistema imposta lo schermo DSI come display principale.

Se desideri impostare il monitor HDMI come schermo principale all'avvio:

#. Crea uno script di avvio:

   .. code-block:: shell

      sudo nano /usr/local/bin/fix-primary-screen.sh

#. Aggiungi il seguente contenuto allo script:

   .. code-block:: bash

      #!/bin/bash
      # Check if an external HDMI monitor is connected
      if wlr-randr | grep -q "HDMI-A-1"; then
          # Turn off the DSI screen first
          wlr-randr --output DSI-1 --off
          sleep 2
          # Re-enable DSI and place it to the right of HDMI
          wlr-randr --output DSI-1 --on --right-of HDMI-A-1
      fi

#. Rendi lo script eseguibile:

   .. code-block:: shell

      sudo chmod +x /usr/local/bin/fix-primary-screen.sh

#. Aggiungi lo script all'avvio automatico. Modifica il file di autostart di labwc:

   .. code-block:: shell

      nano ~/.config/labwc/autostart

   Aggiungi la seguente riga (il ``&`` lo esegue in background):

   .. code-block:: text

      /usr/local/bin/fix-primary-screen.sh &


2. Raffreddamento e Ventole
-------------------------------


.. _promax_fan_faq:

Ventola Non Funzionante / Non Può Essere Controllata?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Pro MAX adotta la soluzione ufficiale di controllo ventola PWM del Raspberry Pi. Tutte e tre le ventole di raffreddamento sono controllate direttamente dal sistema Raspberry Pi e non dipendono dal servizio pironman5 (pertanto, non vedrai opzioni di controllo della ventola nello strumento a riga di comando o nella Dashboard).

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


La Dashboard Non Mostra la Velocità della Ventola?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Pro MAX utilizza ventole **a 5 pin** personalizzate con il seguente pinout: **PWM / 5V / GND / RGB Data In / RGB Data Out**.

Queste ventole **non** hanno un pin tachimetrico (feedback di velocità), quindi il sistema non può leggere gli RPM effettivi. È normale e previsto che la Dashboard non mostri la velocità della ventola.

La velocità della ventola è controllata dalla curva di temperatura PWM nativa del Raspberry Pi:

* < 50°C: Spenta (0%)
* 50°C+: Bassa velocità (30%)
* 60°C+: Media velocità (50%)
* 67,5°C+: Alta velocità (70%)
* 75°C+: Massima velocità (100%)



3. OLED e RGB
-------------------------------


.. _faq_oled_promax:

Lo Schermo OLED Non Funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`promax_set_up_pi_os`
.. |link_compatible_systems| replace:: :ref:`com_os_promax`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled


.. _faq_customize_oled_promax:

Come Personalizzare il Display OLED?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


.. _faq_rgb_promax:

I LED RGB Non Funzionano?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


Come Riattivare lo Schermo OLED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per risparmiare energia e prolungare la durata dello schermo, lo schermo OLED si spegnerà automaticamente dopo un periodo di inattività. Questo fa parte del normale design e non influisce sulla funzionalità del prodotto.

.. note::

   Per la configurazione dello schermo OLED (come accensione/spegnimento, tempo di sospensione, rotazione, ecc.), fare riferimento a :ref:`promax_view_control_dashboard` o :ref:`promax_view_control_commands`.



4. Dashboard e Software
-------------------------------


.. _faq_dashboard_promax:

La Dashboard Non Mostra Dati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`promax_view_control_dashboard`

Come Disabilitare la Dashboard Web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Come Disinstallare e Reinstallare il Software Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


.. |link_view_control_commands| replace:: :ref:`promax_view_control_commands`

Come Controllare i Componenti Usando il Comando ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


.. _faq_piper_tts_32bit_promax:

``pip install piper-tts`` Fallisce con "Could Not Find a Version"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando installi ``sunfounder-voice-assistant`` su Pironman 5 Pro MAX, potresti incontrare il seguente errore:

.. code-block:: text

   ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
   ERROR: No matching distribution found for piper-tts==1.3.0

Questo errore si verifica perché ``piper-tts`` 1.3.0 fornisce solo pacchetti **64-bit** (``aarch64``). Se il tuo Raspberry Pi esegue un sistema operativo **32-bit**, pip non riesce a trovare un pacchetto compatibile.

**Soluzione:** Installa una versione a 64 bit di Raspberry Pi OS.

#. Controlla l'architettura del tuo sistema attuale:

   .. code-block:: shell

      uname -m

   * ``aarch64`` → 64-bit (nessun problema)
   * ``armv7l`` → 32-bit (necessita di aggiornamento)

#. Usa `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`_ per scrivere un'immagine di Raspberry Pi OS **64-bit** sul tuo dispositivo di archiviazione.

#. Dopo aver installato il sistema operativo a 64 bit, reinstalla il software ``pironman5`` e ``sunfounder-voice-assistant``.


5. Avvio e Archiviazione
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_promax`

.. _faq_pi5_boot_fail_promax:

Il PI5 Non Si Avvia (LED Rosso)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail


.. _faq_nvme_promax:

Il Modulo NVMe PIP Non Funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_dual| replace:: :ref:`install_the_os_promax`

.. include:: ../pironman5_max/faq.rst
   :start-after: start_faq_nvme_pip_dual
   :end-before: end_faq_nvme_pip_dual

#. Se il cablaggio è corretto e il sistema operativo è installato, ma l'SSD NVMe ancora non si avvia, prova ad avviare da una scheda Micro SD per verificare la funzionalità degli altri componenti. Una volta confermato, procedi a :ref:`configure_boot_ssd_promax`.

#. Se il problema persiste dopo aver eseguito i passaggi sopra, invia un'email a service@sunfounder.com. Ti risponderemo il prima possibile.


.. _faq_nvme_link_down_promax:

SSD NVMe Rilevato ma Causa Riavvio del Sistema in Lettura/Scrittura?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_promax`

Come Cambiare l'Ordine di Avvio del Raspberry Pi Usando i Comandi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Come Modificare l'Ordine di Avvio con Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_promax`

Come Copiare il Sistema dalla Scheda SD a un SSD NVMe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme



6. Utilizzo Avanzato
-------------------------------


Come Rimuovere la Pellicola Protettiva
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film


.. _promax_openssh_powershell:

Come Installare OpenSSH tramite Powershell?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


Se Configuro OMV, Posso Ancora Usare le Funzioni di Pironman5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sì, OpenMediaVault è configurato sul sistema Raspberry Pi. Segui i passaggi di :ref:`promax_set_up_pi_os` per continuare la configurazione.


La Fotocamera del Raspberry Pi Non Funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando la fotocamera non funziona, il 90% dei problemi è legato alla connessione del cavo a nastro o alla fotocamera stessa.

Prima, usa ``rpicam-hello --list-cameras`` per confermare se la fotocamera viene rilevata. Se viene rilevata con successo, dovresti vedere un messaggio simile al seguente:

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

Se la fotocamera non viene rilevata, controlla se il cavo a nastro è invertito o non completamente inserito. Se il problema persiste, prova a sostituire il cavo a nastro o il modulo fotocamera per un test incrociato.


Posso Installare Home Assistant OS su Pironman 5 Pro MAX?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pironman 5 Pro MAX non ha un proprio add-on dedicato per Home Assistant. Tuttavia, puoi utilizzare l'add-on di **Pironman 5 MAX** — segui la `guida al repository degli add-on di SunFounder <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5_max/set_up/set_up_home_assistant.html#add-the-sunfounder-add-ons-repository>`_.

Tieni presente le seguenti limitazioni:

* **Schermo da 4,3 pollici**: Home Assistant OS è un sistema **Lite** senza ambiente desktop. Lo schermo da 4,3 pollici integrato nel Pro MAX non visualizzerà nulla.

* **NVMe PIP duali**: Home Assistant OS non può leggere entrambi gli SSD NVMe sul modulo NVMe PIP duale del Pro MAX.

* **Schermo OLED e LED RGB**: Questi componenti funzionano normalmente dopo l'installazione dell'add-on — non è richiesta alcuna configurazione aggiuntiva.

* **Ventola CPU**: La ventola CPU richiede una configurazione manuale per funzionare sotto Home Assistant OS. Aggiungi quanto segue a ``/boot/firmware/config.txt``:

  .. code-block:: text

     dtparam=cooling_fan=on
     dtparam=fan_temp0=40000
     dtparam=fan_temp0_hyst=10000
     dtparam=fan_temp0_speed=125

  Dopo aver salvato e riavviato, la ventola CPU sarà controllata dal sistema Raspberry Pi in base alla temperatura della CPU. Puoi anche controllarla manualmente tramite comandi ``pinctrl`` — vedi :ref:`promax_fan_faq`.