.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme agli altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni speciali per le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _set_up_batocera:

Configurazione su Batocera.linux
=========================================================

Se hai installato il sistema operativo Batocera.linux, puoi accedere al sistema in remoto tramite SSH e seguire i passaggi seguenti per completare la configurazione.

#. Una volta avviato il sistema, usa SSH per connetterti in remoto a Pironman5. Su Windows puoi aprire **Powershell**, mentre su macOS e Linux puoi aprire direttamente il **Terminale**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Il nome host predefinito per Batocera è ``batocera``, con utente ``root`` e password ``linux``. Puoi accedere digitando ``ssh root@batocera.local`` e inserendo la password ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Esegui il comando: ``/etc/init.d/S92switch setup`` per accedere al menu delle impostazioni.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Usa la freccia giù per scorrere fino in fondo, seleziona e attiva i servizi **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Dopo aver attivato il servizio Pironman5, seleziona **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Esegui il comando ``reboot`` per riavviare Pironman5.

   .. code-block:: shell

      reboot

#. Al riavvio, il servizio ``pironman5.service`` si avvierà automaticamente. Ecco le funzionalità principali configurate per il Pironman 5:

   * Lo schermo OLED mostrerà CPU, RAM, utilizzo del disco, temperatura della CPU e indirizzo IP del Raspberry Pi.
   * Quattro LED WS2812 RGB si illumineranno di blu con effetto respiro.

   .. note::

     Le ventole RGB non si attivano finché la temperatura non raggiunge i 60°C. Per modificare la temperatura di attivazione, consulta :ref:`cc_control_fan`.


Ora puoi collegare il Pironman 5 a uno schermo, controller di gioco, cuffie e altro ancora per immergerti nel tuo mondo videoludico.

