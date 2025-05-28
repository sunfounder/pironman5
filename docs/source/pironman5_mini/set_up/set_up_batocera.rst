.. note:: 

    Ciao, benvenuto nella community SunFounder dedicata agli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche grazie al supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per accrescere le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _set_up_batocera_mini:

Configurazione di Batocera.linux
=========================================================

Se hai installato il sistema operativo Batocera.linux, puoi accedere da remoto al sistema tramite SSH e seguire i passaggi qui sotto per completare la configurazione.

#. Dopo l'avvio del sistema, usa ssh per connetterti da remoto a Pironman5. Su Windows, puoi aprire **Powershell**, mentre su Mac OS X e Linux puoi aprire direttamente il **Terminale**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. L'hostname predefinito del sistema Batocera è ``batocera``, con nome utente ``root`` e password ``linux``. Puoi quindi accedere digitando ``ssh root@batocera.local`` e inserendo la password ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Esegui il comando: ``/etc/init.d/S92switch setup`` per accedere alla pagina delle impostazioni.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Usa la freccia in basso per scorrere fino in fondo, seleziona e attiva i servizi **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Dopo aver attivato il servizio pironman5, seleziona **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Esegui il comando ``reboot`` per riavviare Pironman5.

   .. code-block:: shell

      reboot

#. Dopo il riavvio, il servizio ``pironman5.service`` verrà avviato automaticamente. Ecco le principali configurazioni per Pironman 5:
   
   * Quattro LED RGB WS2812 si illumineranno di blu in modalità "breathing".
   
   .. note::
    
     La ventola RGB non inizierà a girare finché la temperatura non raggiungerà i 60°C. Per temperature di attivazione differenti, vedi :ref:`cc_control_fan_mini`.

Ora puoi collegare il tuo Pironman 5 a uno schermo, a dei controller di gioco, a cuffie e molto altro, per immergerti completamente nel tuo mondo videoludico.
