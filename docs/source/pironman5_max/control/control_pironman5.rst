.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

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