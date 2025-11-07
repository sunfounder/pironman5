.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti come te.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e difficoltà tecniche con il supporto del nostro team e della community.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotto e anticipazioni esclusive.
    - **Sconti speciali**: Approfitta di sconti riservati sui prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _max_login_rpi:

Accedere al sistema operativo Raspberry Pi
============================================

In questo capitolo imparerai come accedere al Raspberry Pi. Che tu abbia un monitor collegato o debba accedere da remoto, questa sezione ti guiderà all’apertura del terminale, che utilizzerai nei capitoli successivi per inserire comandi.

.. note::

    Se hai già familiarità con l’uso del Raspberry Pi, puoi saltare questo capitolo.

Accesso con monitor
-----------------------

Collegare uno schermo al Raspberry Pi rende più semplice interagire direttamente con il sistema.

**Componenti necessari**

* Pironman 5 MAX
* Alimentatore
* Scheda Micro SD o SSD NVMe con Raspberry Pi OS preinstallato
* Alimentatore del monitor
* Cavo HDMI
* Monitor
* Mouse
* Tastiera

**Procedura**

#. Inserisci la scheda Micro SD nel Pironman 5 MAX.

#. Collega il mouse e la tastiera alle porte USB del Pironman 5 MAX.

#. Usa il cavo HDMI per collegare il monitor alla porta HDMI del Pironman 5 MAX. Assicurati che il monitor sia alimentato e acceso.

#. Accendi il Pironman 5 MAX usando l’alimentatore. Entro pochi secondi dovrebbe comparire il desktop del Raspberry Pi OS sul monitor.

   .. image:: img/bookwarm.png
      :width: 90%
      

#. Una volta visualizzato il desktop, apri il Terminale cliccando sull’icona corrispondente o cercandolo nel menu per iniziare a inserire i comandi.

Accesso remoto senza monitor
--------------------------------

Se non hai accesso a un monitor, puoi comunque utilizzare il Raspberry Pi accedendo da remoto.

Per l’accesso da riga di comando, puoi utilizzare SSH per collegarti alla shell Bash del Raspberry Pi, la shell Linux predefinita che consente di gestire il dispositivo tramite comandi.

Per chi preferisce un’interfaccia grafica, è possibile usare un’applicazione di desktop remoto come VNC Viewer per gestire file e operazioni da remoto in modo visivo.

**Componenti necessari**

* Pironman 5 MAX 
* Alimentatore
* Scheda Micro SD o SSD NVMe con Raspberry Pi OS preinstallato

**Procedura**

#. Inserisci la scheda Micro SD nel Pironman 5 MAX.

#. Collega il Pironman 5 MAX a una fonte di alimentazione tramite l’alimentatore.

#. Per tutorial dettagliati su come configurare l’accesso remoto in base al sistema operativo del tuo computer, consulta le seguenti sezioni:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


