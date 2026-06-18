.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _max_set_up_batocera:

Configurazione su Batocera.linux
=========================================================

Se hai installato il sistema operativo Batocera.linux, puoi accedere da remoto tramite SSH e seguire i passaggi qui sotto per completare la configurazione.

#. Una volta avviato il sistema, utilizza SSH per collegarti da remoto a Pironman 5 MAX. Su Windows puoi aprire **Powershell**, mentre su Mac OS X e Linux puoi usare direttamente il **Terminale**.

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

#. Al riavvio, il servizio ``pironman5.service`` si avvierà automaticamente. Ecco le funzionalità principali di Pironman 5 MAX:

   * Il display OLED mostrerà CPU, RAM, utilizzo del disco, temperatura della CPU e indirizzo IP del Raspberry Pi.
   * Quattro LED RGB WS2812 si accenderanno di blu con effetto respiro.
   * Le ventole GPIO sono impostate di default sulla modalità **Bilanciata**. Per modificare la temperatura di attivazione, consulta :ref:`cc_control_fan_max`.

Ora puoi collegare Pironman 5 MAX a uno schermo, controller di gioco, cuffie e altri dispositivi per immergerti nel tuo mondo videoludico.


.. note::

   A questo punto, hai completato con successo la configurazione del Pironman 5 MAX ed è pronto per l’uso.
   
   Per un controllo avanzato dei suoi componenti, fai riferimento a :ref:`max_view_control_commands`.
