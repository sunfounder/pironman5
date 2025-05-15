.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 – gemeinsam mit Gleichgesinnten.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Unterstützung bei technischen Problemen und Fragen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produktankündigungen und erhalte exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _login_rpi_mini:

Anmeldung bei Raspberry Pi OS
=====================================

In diesem Kapitel lernst du, wie du dich beim Raspberry Pi anmeldest. Egal ob mit angeschlossenem Bildschirm oder per Fernzugriff – hier erfährst du, wie du das Terminal öffnest, das du in den folgenden Kapiteln für die Eingabe von Befehlen benötigst.

.. note::

    Wenn du bereits mit dem Raspberry Pi vertraut bist, kannst du dieses Kapitel überspringen.

Anmeldung mit Bildschirm
---------------------------

Ein angeschlossener Bildschirm erleichtert die direkte Interaktion mit dem Raspberry Pi-System.

**Benötigte Komponenten**

* Pironman 5 Mini  
* Netzteil  
* Micro-SD-Karte oder NVMe-SSD mit vorinstalliertem Raspberry Pi OS  
* Netzteil für den Monitor  
* HDMI-Kabel  
* Monitor  
* Maus  
* Tastatur  

**Schritte**

#. Setze die Micro-SD-Karte in den Pironman 5 Mini ein.

#. Schließe Maus und Tastatur an die USB-Anschlüsse des Pironman 5 Mini an.

#. Verbinde den Monitor über das HDMI-Kabel mit dem HDMI-Anschluss des Pironman 5 Mini. Stelle sicher, dass der Monitor mit Strom versorgt wird und eingeschaltet ist.

#. Schalte den Pironman 5 Mini mit dem Netzteil ein. Kurz darauf sollte der Desktop von Raspberry Pi OS auf dem Monitor erscheinen.

   .. image:: img/bookwarm.png
      :width: 90%


#. Sobald der Desktop sichtbar ist, öffne das Terminal, indem du auf das Terminalsymbol klickst oder es über das Menü suchst, um mit der Eingabe von Befehlen zu beginnen.

Anmeldung ohne Bildschirm (Remote-Zugriff)
----------------------------------------------

Falls kein Monitor zur Verfügung steht, kannst du den Raspberry Pi auch per Fernzugriff nutzen.

Für den Zugriff auf die Kommandozeile kannst du per SSH eine Verbindung zur Bash-Shell des Raspberry Pi herstellen – der Standard-Linux-Shell zur Verwaltung des Geräts über Befehle.

Für eine grafische Benutzeroberfläche empfiehlt sich die Nutzung einer Fernzugriffssoftware wie VNC Viewer, um Dateien und Vorgänge visuell zu steuern.

**Benötigte Komponenten**

* Pironman 5 Mini  
* Netzteil  
* Micro-SD-Karte oder NVMe-SSD mit vorinstalliertem Raspberry Pi OS  

Schritte

#. Setze die Micro-SD-Karte in den Pironman 5 Mini ein.

#. Verbinde den Pironman 5 Mini über das Netzteil mit einer Stromquelle.

#. Ausführliche Anleitungen zur Einrichtung des Fernzugriffs – je nach Betriebssystem deines Computers – findest du in den folgenden Abschnitten:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


