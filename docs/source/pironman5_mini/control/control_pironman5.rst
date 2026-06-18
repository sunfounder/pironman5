.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_mini:

5. Steuerung per Befehlen oder Dashboard
=======================================================

Nach erfolgreicher Installation des ``pironman5``-Moduls wird der Dienst ``pironman5.service`` bei jedem Systemneustart automatisch gestartet.

Du kannst den Pironman 5 Mini entweder über die Kommandozeile steuern oder über das Web-Dashboard unter ``http://<ip>:34001`` darauf zugreifen und ihn überwachen.

.. note::

    * Beim System **Home Assistant** erfolgt die Überwachung und Steuerung des Pironman 5 Mini ausschließlich über das Dashboard unter ``http://<ip>:34001``.

    .. * Beim System **Batocera.linux** kann der Pironman 5 Mini ausschließlich über Befehle gesteuert werden. Beachte, dass Änderungen an der Konfiguration erst nach einem Neustart des Dienstes mit ``pironman5 restart`` wirksam werden.


.. toctree::
    :maxdepth: 1

    control_with_dashboard 
    control_with_commands