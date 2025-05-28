.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e difficoltà tecniche con l’aiuto della nostra community e del nostro team.
    - **Learn & Share**: Scambia consigli e tutorial per perfezionare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e ad anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway.

    👉 Pronto a scoprire e creare con noi? Clicca su [|link_sf_facebook|] ed entra a far parte della community oggi stesso!

.. _max_remote_desktop:

Accesso Desktop Remoto per Raspberry Pi
===========================================

Per chi preferisce un’interfaccia grafica (GUI) rispetto alla riga di comando, Raspberry Pi offre la funzionalità di desktop remoto. Questa guida ti accompagnerà nella configurazione e nell’uso di VNC (Virtual Network Computing) per l’accesso remoto.

Ti consigliamo di utilizzare `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ per questo scopo.

**Attivazione del servizio VNC su Raspberry Pi**

Il servizio VNC è preinstallato nel sistema operativo Raspberry Pi OS, ma disattivato per impostazione predefinita. Segui questi passaggi per abilitarlo:

#. Inserisci il seguente comando nel terminale del Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Usa la freccia verso il basso per navigare fino a **Interfacing Options**, quindi premi **Enter**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. Seleziona **VNC** dall’elenco delle opzioni.

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. Usa i tasti freccia per scegliere **<Yes>** -> **<OK>** -> **<Finish>** e completare l’attivazione del servizio VNC.

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
      

#. Ora avrai accesso all’interfaccia desktop del tuo Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%

