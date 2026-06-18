.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_mini:

5. Contrôle via commandes ou tableau de bord
=======================================================

Une fois le module ``pironman5`` installé avec succès, le service ``pironman5.service`` se lance automatiquement au redémarrage.

Vous pouvez surveiller et contrôler le Pironman 5 Mini à l’aide de commandes ou en accédant au tableau de bord via la page web à l’adresse ``http://<ip>:34001``.

.. note::

    * Pour le système **Home Assistant**, la surveillance et le contrôle du Pironman 5 Mini se font uniquement via le tableau de bord, accessible à l’adresse ``http://<ip>:34001``.

    .. * Pour le système **Batocera.linux**, le contrôle et la surveillance se font uniquement par commandes. Il est important de noter que toute modification de configuration nécessite un redémarrage du service via ``pironman5 restart`` pour être prise en compte.


.. toctree::
    :maxdepth: 1

    control_with_dashboard 
    control_with_commands