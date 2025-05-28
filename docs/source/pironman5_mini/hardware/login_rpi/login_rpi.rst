.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri utenti appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche grazie al supporto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e giveaway festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

.. _login_rpi_mini:

Accesso al sistema operativo Raspberry Pi
=================================================

In questo capitolo imparerai come accedere al sistema Raspberry Pi. Che tu abbia un monitor collegato o voglia accedere da remoto, questa sezione ti guiderà nell'apertura del terminale, che utilizzerai nei capitoli successivi per eseguire i comandi.

.. note::

    Se hai già familiarità con l’utilizzo del Raspberry Pi, puoi saltare questo capitolo.

Accesso con Schermo
------------------------------

Collegare uno schermo al tuo Raspberry Pi consente un’interazione diretta e semplificata con il sistema.

**Componenti necessari**

* Pironman 5 Mini
* Alimentatore
* Scheda Micro SD o SSD NVMe con Raspberry Pi OS preinstallato
* Alimentatore del monitor
* Cavo HDMI
* Monitor
* Mouse
* Tastiera

**Procedura**

#. Inserisci la scheda Micro SD nel Pironman 5 Mini.

#. Collega il mouse e la tastiera alle porte USB del Pironman 5 Mini.

#. Usa il cavo HDMI per collegare il monitor alla porta HDMI del Pironman 5 Mini. Assicurati che il monitor sia alimentato e acceso.

#. Accendi il Pironman 5 Mini utilizzando l’alimentatore. Dopo pochi istanti, dovrebbe apparire il desktop del sistema operativo Raspberry Pi sul monitor.

   .. image:: img/bookwarm.png
      :width: 90%
      

#. Una volta visualizzato il desktop, apri il Terminale cliccando sull’icona corrispondente o cercandolo nel menu per iniziare a inserire comandi.

Accesso da Remoto Senza Schermo
----------------------------------------------

Se non disponi di un monitor, puoi comunque utilizzare il Raspberry Pi accedendovi da remoto.

Per l’accesso tramite riga di comando, puoi usare SSH per collegarti alla shell Bash del Raspberry Pi, la shell predefinita di Linux che consente la gestione del dispositivo tramite comandi.

Se preferisci un’interfaccia grafica, puoi utilizzare un’applicazione di desktop remoto come VNC Viewer per gestire visivamente file e operazioni a distanza.

**Componenti necessari**

* Pironman 5 Mini 
* Alimentatore
* Scheda Micro SD o SSD NVMe con Raspberry Pi OS preinstallato

**Procedura**

#. Inserisci la scheda Micro SD nel Pironman 5 Mini.

#. Collega il Pironman 5 Mini a una fonte di alimentazione tramite l’alimentatore.

#. Per istruzioni dettagliate sulla configurazione dell’accesso remoto in base al sistema operativo del tuo computer, consulta le sezioni seguenti:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


