.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto della nostra community e del nostro team.
    - **Learn & Share**: Condividi suggerimenti e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato a nuovi annunci e anteprime sui prodotti.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway esclusivi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

FAQ
============

Come disabilitare la dashboard web?
------------------------------------------------------

Una volta completata l’installazione del modulo ``pironman5``, potrai accedere alla :ref:`max_view_control_dashboard`.

Se non ti serve questa funzione e desideri ridurre l’utilizzo di CPU e RAM, puoi disabilitare la dashboard durante l’installazione di ``pironman5`` aggiungendo il flag ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Se hai già installato ``pironman5``, puoi rimuovere il modulo ``dashboard`` e ``influxdb``, quindi riavviare il servizio per applicare le modifiche:

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

Il Pironman 5 supporta i sistemi di retro gaming?
--------------------------------------------------------

Sì, è compatibile. Tuttavia, la maggior parte dei sistemi retro gaming sono versioni semplificate che non consentono l’installazione di software aggiuntivo. Questo può impedire il corretto funzionamento di alcuni componenti del Pironman 5, come il display OLED, le due ventole RGB e i quattro LED RGB, che richiedono i pacchetti software del Pironman 5 per funzionare.

.. note::

    Il sistema Batocera.linux è ora pienamente compatibile con il Pironman 5. Batocera.linux è una distribuzione open-source e completamente gratuita dedicata al retro gaming.

    * :ref:`max_install_batocera`
    * :ref:`max_set_up_batocera`

Come controllare i componenti con il comando ``pironman5``?
----------------------------------------------------------------------
Consulta il seguente tutorial per controllare i componenti del Pironman 5 usando il comando ``pironman5``.

* :ref:`max_view_control_commands`

Come modificare l’ordine di avvio del Raspberry Pi da terminale?
---------------------------------------------------------------------------

Se hai già effettuato l’accesso al tuo Raspberry Pi, puoi modificare l’ordine di avvio tramite riga di comando. Ecco la guida dettagliata:

* :ref:`max_configure_boot_ssd`


Come modificare l’ordine di avvio con Raspberry Pi Imager?
---------------------------------------------------------------

Oltre a modificare il parametro ``BOOT_ORDER`` nella configurazione EEPROM, puoi utilizzare **Raspberry Pi Imager** per cambiare l’ordine di avvio del tuo Raspberry Pi.

Si consiglia di utilizzare una scheda SD di riserva per questo passaggio.

* :ref:`max_update_bootloader`

Come copiare il sistema dalla scheda SD a un SSD NVMe?
-------------------------------------------------------------

Se disponi di un SSD NVMe ma non di un adattatore per collegarlo al computer, puoi prima installare il sistema su una scheda Micro SD. Una volta che il Pironman 5 si avvia correttamente, puoi copiare il sistema dalla scheda SD all’SSD NVMe. Consulta la guida dettagliata:


* :ref:`max_copy_sd_to_nvme_rpi`


Lo schermo OLED non funziona?
-------------------------------

Se lo schermo OLED non mostra nulla o visualizza in modo errato, prova i seguenti passaggi:

Controlla che il cavo FPC dello schermo OLED sia collegato correttamente.

#. Usa questo comando per visualizzare i log e controllare eventuali messaggi di errore:

   .. code-block:: shell

      cat /opt/pironman5/log

#. In alternativa, verifica se l’indirizzo i2c 0x3C dello schermo OLED viene rilevato:

   .. code-block:: shell

        sudo i2cdetect -y 1

#. Se non emergono problemi, prova a riavviare il servizio pironman5 per vedere se lo schermo riprende a funzionare:


   .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _max_openssh_powershell:

Installare OpenSSH tramite PowerShell
-------------------------------------------

Se provi a connetterti al tuo Raspberry Pi usando ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<indirizzo IP>``) e ricevi il seguente messaggio di errore:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Significa che il tuo sistema Windows è obsoleto e non include `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato. Segui la guida qui sotto per installarlo manualmente.

#. Digita ``powershell`` nella barra di ricerca di Windows, clicca col tasto destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Usa il seguente comando per installare ``OpenSSH.Client``:

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Dopo l’installazione, vedrai un output simile:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l’installazione con il comando:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. A questo punto il sistema ti confermerà che ``OpenSSH.Client`` è stato installato correttamente:

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Se il messaggio sopra non compare, significa che il tuo sistema è ancora troppo obsoleto. In tal caso, ti consigliamo di installare un client SSH di terze parti come |link_putty|.

#. Ora riavvia PowerShell ed eseguilo nuovamente come amministratore. Da qui potrai accedere al tuo Raspberry Pi con il comando ``ssh``, e ti verrà chiesta la password configurata in precedenza.

   .. image:: img/powershell_login.png



Se configuro OMV, posso comunque usare le funzionalità del Pironman 5?
--------------------------------------------------------------------------------------------------------

Sì, OpenMediaVault viene eseguito su un sistema Raspberry Pi. Segui i passaggi descritti in :ref:`max_set_up_pi_os` per completare la configurazione.