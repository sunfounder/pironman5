.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_batocera:

Configurazione su Batocera.linux
=========================================================

Se hai installato il sistema operativo Batocera.linux, puoi accedere a questo sistema in remoto tramite SSH e seguire i passaggi seguenti per completare la configurazione.

#. Una volta avviato il sistema, usa ssh per connetterti in remoto a Pironman5. Per Windows, puoi aprire **Powershell**, mentre per Mac OS X e Linux puoi aprire direttamente **Terminale**.

   .. image:: img/batocera_powershell.png
      :width: 90%
      

#. Il nome host predefinito per il sistema Batocera è ``batocera``, con l'utente predefinito ``root`` e la password ``linux``. Puoi quindi accedere digitando ``ssh root@batocera.local`` ed inserendo la password ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Esegui il comando: ``/etc/init.d/S92switch setup`` per accedere alla pagina delle impostazioni del menu.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Usa la freccia verso il basso per navigare fino alla fine, seleziona e attiva i servizi **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Dopo aver attivato il servizio Pironman5, seleziona **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Esegui il comando ``reboot`` per riavviare Pironman5.

   .. code-block:: shell

      reboot

#. Al riavvio, il servizio ``pironman5.service`` si avvierà automaticamente. Ecco le principali configurazioni per Pironman 5:

   * Lo schermo OLED mostrerà CPU, RAM, utilizzo del disco, temperatura della CPU e l'indirizzo IP del Raspberry Pi.
   * Quattro LED RGB WS2812 si illumineranno di blu con una modalità di respirazione.
   * Le ventole GPIO sono impostate di default sulla modalità **Bilanciata**. Per temperature di attivazione diverse, consulta :ref:`cc_control_fan`.


Ora puoi collegare il Pironman 5 a uno schermo, controller di gioco, cuffie e molto altro per immergerti nel tuo mondo di gioco.

.. note::

   A questo punto, hai completato con successo la configurazione del Pironman 5 ed è pronto per l’uso.
   
   Per un controllo avanzato dei suoi componenti, fai riferimento a :ref:`view_control_commands_5`.
