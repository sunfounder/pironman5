.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche gemeinsam mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum der Beitritt lohnt?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Problemen und Fragen nach dem Kauf – von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Wissen, Tipps und Tutorials aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitige Informationen zu neuen Produkten und spannende Einblicke vor der Veröffentlichung.
    - **Spezielle Rabatte**: Nutze exklusive Preisnachlässe auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an saisonalen Events und Gewinnspielen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und kreativ zu werden? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

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

    control_with dashboard 
    control_with_commands