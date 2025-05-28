.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e difficoltà tecniche grazie al supporto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

.. _remote_desktop_mini:

Accesso Desktop Remoto per Raspberry Pi
==================================================

Per chi preferisce un’interfaccia grafica (GUI) rispetto alla riga di comando, Raspberry Pi supporta la funzionalità di desktop remoto. Questa guida ti accompagnerà nella configurazione e nell'utilizzo di VNC (Virtual Network Computing) per l’accesso remoto.

Ti consigliamo di utilizzare `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ per questo scopo.

**Abilitare il Servizio VNC sul Raspberry Pi**

Il servizio VNC è preinstallato nel sistema operativo Raspberry Pi, ma disabilitato per impostazione predefinita. Segui questi passaggi per attivarlo:

#. Inserisci il seguente comando nel terminale del Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Usa la freccia giù per navigare su **Interfacing Options**, quindi premi **Enter**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. Seleziona **VNC** dall’elenco delle opzioni.

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. Utilizza le frecce per selezionare **<Yes>** -> **<OK>** -> **<Finish>** e completare l’attivazione del servizio VNC.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**Accesso tramite VNC Viewer**

#. Scarica e installa `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sul tuo computer.

#. Una volta installato, avvia VNC Viewer. Inserisci il nome host o l’indirizzo IP del tuo Raspberry Pi e premi Invio.

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. Quando richiesto, inserisci il nome utente e la password del tuo Raspberry Pi, quindi clicca su **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. Ora potrai accedere all’interfaccia desktop del tuo Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%

