.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_login_rpi:

Anmeldung beim Raspberry Pi OS
=====================================

In diesem Kapitel lernst du, wie du dich beim Raspberry Pi anmeldest. Egal, ob du einen Bildschirm angeschlossen hast oder die Anmeldung remote durchführen musst, dieser Abschnitt zeigt dir, wie du das Terminal öffnest, das du in späteren Kapiteln zum Eingeben von Befehlen verwenden wirst.

.. note::

    Wenn du bereits mit der Bedienung des Raspberry Pi vertraut bist, kannst du dieses Kapitel überspringen.

Anmeldung mit einem Bildschirm
------------------------------------

Ein angeschlossener Bildschirm erleichtert die direkte Interaktion mit dem System.

**Benötigte Komponenten**

* Pironman 5 MAX
* Netzteil
* Micro SD-Karte oder NVMe SSD mit vorinstalliertem Raspberry Pi OS
* Monitor-Netzteil
* HDMI-Kabel
* Monitor
* Maus
* Tastatur

**Schritte**

#. Stecke die Micro SD-Karte in das Pironman 5 MAX.

#. Verbinde die Maus und die Tastatur mit den USB-Ports des Pironman 5 MAX.

#. Verwende das HDMI-Kabel, um den Monitor mit dem HDMI-Port des Pironman 5 MAX zu verbinden. Stelle sicher, dass der Monitor mit einer Stromquelle verbunden und eingeschaltet ist.

#. Schalte das Pironman 5 MAX mit dem Netzteil ein. Kurz darauf sollte der Raspberry Pi OS-Desktop auf dem Monitor erscheinen.

   .. image:: img/bookwarm.png
      :width: 90%


#. Sobald der Desktop sichtbar ist, öffne das Terminal, indem du auf das Terminal-Symbol klickst oder im Menü danach suchst, um mit der Eingabe von Befehlen zu beginnen.

Remote-Anmeldung ohne Bildschirm
------------------------------------

Wenn du keinen Monitor zur Verfügung hast, kannst du dich dennoch remote in deinen Raspberry Pi einloggen.

Für den Zugang über die Kommandozeile kannst du SSH verwenden, um dich mit der Bash-Shell des Raspberry Pi zu verbinden, der Standard-Linux-Shell, die die Verwaltung des Geräts über Befehle ermöglicht.

Wer eine grafische Oberfläche bevorzugt, kann eine Remote-Desktop-Anwendung wie VNC Viewer verwenden, um Dateien und Operationen visuell zu verwalten.

**Benötigte Komponenten**

* Pironman 5 MAX 
* Netzteil
* Micro SD-Karte oder NVMe SSD mit vorinstalliertem Raspberry Pi OS

Schritte:

#. Stecke die Micro SD-Karte in das Pironman 5 MAX.

#. Verbinde das Pironman 5 MAX mit einer Stromquelle, indem du das Netzteil verwendest.

#. Weitere detaillierte Tutorials zur Einrichtung des Remote-Zugriffs je nach Betriebssystem deines Computers findest du in den folgenden Abschnitten:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


