.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_5:

5. Contrôle par Commandes ou Tableau de Bord
=======================================================

Une fois le module ``pironman5`` installé avec succès, le service ``pironman5.service`` démarrera automatiquement lors du redémarrage.

Vous pouvez surveiller et contrôler le Pironman 5 via des commandes, ou en accédant au tableau de bord via la page web à l'adresse ``http://<ip>:34001``.

.. note::

    * Pour le système **Home Assistant**, vous pouvez uniquement surveiller et contrôler le Pironman 5 via le tableau de bord en ouvrant la page web à l'adresse ``http://<ip>:34001``.

.. * Pour le système **Batocera.linux**, vous pouvez uniquement surveiller et contrôler le Pironman 5 via des commandes. Il est important de noter que toute modification de la configuration nécessite un redémarrage du service à l'aide de la commande ``pironman5 restart`` pour être prise en compte.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands