.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _control_commands_dashboard_max:

5. Controllo con Comandi o Dashboard
=======================================================

Una volta installato correttamente il modulo ``pironman5``, il servizio ``pironman5.service`` si avvierà automaticamente al riavvio.

Puoi monitorare e controllare il Pironman 5 tramite comandi, o accedendo alla dashboard dalla pagina web ``http://<ip>:34001``.

.. note::

    * Per il sistema **Home Assistant**, puoi solo monitorare e controllare il Pironman 5 tramite la dashboard, aprendo la pagina web ``http://<ip>:34001``.

.. * Per il sistema **Batocera.linux**, puoi solo monitorare e controllare il Pironman 5 tramite comandi. È importante notare che qualsiasi modifica alla configurazione richiede il riavvio del servizio con ``pironman5 restart`` per avere effetto.


.. toctree::
    :maxdepth: 1

    control_with_dashboard
    control_with_commands
