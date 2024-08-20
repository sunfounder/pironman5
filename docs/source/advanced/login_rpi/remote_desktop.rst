.. nota::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _remote_desktop:

Accesso Desktop Remoto per Raspberry Pi
==================================================

Per coloro che preferiscono un'interfaccia grafica (GUI) rispetto all'accesso tramite linea di comando, il Raspberry Pi supporta la funzionalità di desktop remoto. Questa guida ti mostrerà come configurare e utilizzare VNC (Virtual Network Computing) per l'accesso remoto.

Raccomandiamo l'uso di `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ per questo scopo.

**Abilitazione del Servizio VNC su Raspberry Pi**

Il servizio VNC è preinstallato nel sistema operativo Raspberry Pi OS, ma è disabilitato di default. Segui questi passaggi per abilitarlo:

#. Inserisci il seguente comando nel terminale del Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Usa la freccia giù per navigare verso **Opzioni Interfaccia**, quindi premi **Invio**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. Seleziona **VNC** tra le opzioni.

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. Usa i tasti freccia per scegliere **<Sì>** -> **<OK>** -> **<Fine>** e completa l'attivazione del servizio VNC.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**Accesso tramite VNC Viewer**

#. Scarica e installa `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sul tuo computer personale.

#. Una volta installato, avvia VNC Viewer. Inserisci il nome host o l'indirizzo IP del tuo Raspberry Pi e premi Invio.

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. Quando richiesto, inserisci il nome utente e la password del tuo Raspberry Pi, quindi clicca su **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. Ora avrai accesso all'interfaccia desktop del tuo Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%
      
