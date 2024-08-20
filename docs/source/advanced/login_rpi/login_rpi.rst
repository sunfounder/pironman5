.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _login_rpi:

Accedi al Raspberry Pi OS
=====================================

In questo capitolo, imparerai come accedere al Raspberry Pi. Che tu abbia uno schermo collegato o che debba accedervi da remoto, questa sezione ti guiderà nell'apertura del terminale, che utilizzerai nei capitoli successivi per inserire i comandi.

.. note::

    Se hai già familiarità con le operazioni di Raspberry Pi, puoi saltare questo capitolo.

Accesso con schermo
---------------------------

Avere uno schermo collegato al tuo Raspberry Pi rende più facile interagire direttamente con il sistema.

**Componenti necessari**

* Pironman 5
* Adattatore di alimentazione
* Scheda Micro SD o NVMe SSD con Raspberry Pi OS preinstallato
* Adattatore di alimentazione del monitor
* Cavo HDMI
* Monitor
* Mouse
* Tastiera

**Passaggi**

#. Inserisci la scheda Micro SD nel Pironman 5.

#. Collega il mouse e la tastiera alle porte USB del Pironman 5.

#. Utilizza il cavo HDMI per collegare il monitor alla porta HDMI del Pironman 5. Assicurati che il monitor sia collegato a una fonte di alimentazione e acceso.

#. Accendi il Pironman 5 utilizzando l'adattatore di alimentazione. Dovresti vedere apparire il desktop del Raspberry Pi OS sul monitor entro poco tempo.

   .. image:: img/bookwarm.png
      :width: 90%
      

#. Una volta visibile il desktop, apri il Terminale cliccando sull'icona del terminale o cercandolo nel menu per iniziare a inserire comandi.

Accesso remoto senza schermo
------------------------------------

Se non hai accesso a un monitor, puoi comunque utilizzare il tuo Raspberry Pi accedendo da remoto.

Per l'accesso alla riga di comando, puoi utilizzare SSH per connetterti alla shell Bash del Raspberry Pi, la shell predefinita di Linux che consente di gestire il dispositivo tramite comandi.

Per chi preferisce un'interfaccia grafica, l'uso di un'applicazione di desktop remoto come VNC Viewer offre un modo visivo per gestire file e operazioni da remoto.

**Componenti necessari**

* Pironman 5 
* Adattatore di alimentazione
* Scheda Micro SD o NVMe SSD con Raspberry Pi OS preinstallato

Passaggi:

#. Inserisci la scheda Micro SD nel Pironman 5.

#. Collega il Pironman 5 a una fonte di alimentazione utilizzando l'adattatore di alimentazione.

#. Per tutorial dettagliati su come configurare l'accesso remoto in base al sistema operativo del tuo computer, consulta le sezioni seguenti:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


