.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_mini:

5. Controllo tramite Comandi o Dashboard
=======================================================

Dopo aver installato con successo il modulo ``pironman5``, il servizio ``pironman5.service`` si avvierà automaticamente al riavvio del sistema.

Puoi monitorare e controllare il Pironman 5 Mini tramite comandi, oppure accedendo alla dashboard tramite la pagina web all’indirizzo ``http://<ip>:34001``.

.. note::

    * Per il sistema **Home Assistant**, è possibile monitorare e controllare il Pironman 5 Mini solo attraverso la dashboard, accedendo alla pagina web ``http://<ip>:34001``.

    .. * Per il sistema **Batocera.linux**, il controllo e il monitoraggio del Pironman 5 Mini sono disponibili solo tramite comandi. È importante ricordare che ogni modifica alla configurazione richiede un riavvio del servizio tramite ``pironman5 restart`` per essere applicata.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands