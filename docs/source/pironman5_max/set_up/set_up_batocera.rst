.. note::

    Ciao! Benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue competenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e difficoltà tecniche con il supporto del nostro team e della nostra community.
    - **Learn & Share**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Accedi in anteprima ai nuovi annunci di prodotto e ad anticipazioni esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni stagionali e giveaway dedicati.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

.. _max_set_up_batocera:

Configurazione su Batocera.linux
=========================================================

Se hai installato il sistema operativo Batocera.linux, puoi accedere da remoto tramite SSH e seguire i passaggi qui sotto per completare la configurazione.

#. Una volta avviato il sistema, utilizza SSH per collegarti da remoto a Pironman5. Su Windows puoi aprire **Powershell**, mentre su Mac OS X e Linux puoi usare direttamente il **Terminale**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. L'hostname predefinito del sistema Batocera è ``batocera``, con nome utente ``root`` e password ``linux``. Puoi quindi accedere digitando ``ssh root@batocera.local`` e inserendo la password ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Esegui il comando: ``/etc/init.d/S92switch setup`` per accedere alla pagina delle impostazioni del menu.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Usa la freccia in giù per scorrere fino in fondo, seleziona e attiva i servizi **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Dopo aver attivato il servizio pironman5, seleziona **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Esegui il comando ``reboot`` per riavviare Pironman5.

   .. code-block:: shell

      reboot

#. Al riavvio, il servizio ``pironman5.service`` si avvierà automaticamente. Ecco le funzionalità principali di Pironman 5:

   * Il display OLED mostrerà CPU, RAM, utilizzo del disco, temperatura della CPU e indirizzo IP del Raspberry Pi.
   * Quattro LED RGB WS2812 si accenderanno di blu con effetto respiro.

   .. note::

     Le ventole RGB non si attiveranno finché la temperatura non raggiungerà i 60 °C. Per modificare la temperatura di attivazione, consulta :ref:`max_cc_control_fan`.

Ora puoi collegare Pironman 5 a uno schermo, controller di gioco, cuffie e altri dispositivi per immergerti nel tuo mondo videoludico.
