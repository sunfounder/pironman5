.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_max:

5. Steuerung mit Befehlen oder Dashboard
=======================================================

Sobald du das ``pironman5``-Modul erfolgreich installiert hast, wird der ``pironman5.service`` nach dem Neustart automatisch gestartet.

Du kannst den Pironman 5 entweder über Befehle überwachen und steuern oder auf das Dashboard zugreifen, indem du die Webseite unter ``http://<ip>:34001`` öffnest.

.. note::

    * Beim **Home Assistant**-System kannst du den Pironman 5 nur über das Dashboard überwachen und steuern, indem du die Webseite unter ``http://<ip>:34001`` öffnest.

.. * Beim **Batocera.linux**-System kannst du den Pironman 5 nur über Befehle überwachen und steuern. Beachte, dass Änderungen an der Konfiguration einen Neustart des Dienstes mit dem Befehl ``pironman5 restart`` erfordern, damit sie wirksam werden.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands