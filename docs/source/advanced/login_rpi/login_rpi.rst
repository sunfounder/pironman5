.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _login_rpi:

Anmeldung bei Raspberry Pi OS
=====================================

In diesem Kapitel erfahren Sie, wie Sie sich bei Ihrem Raspberry Pi anmelden. Ob Sie einen Bildschirm angeschlossen haben oder aus der Ferne darauf zugreifen müssen – dieser Abschnitt führt Sie durch das Öffnen des Terminals, das Sie in den späteren Kapiteln zur Eingabe von Befehlen verwenden werden.

.. note::

    Wenn Sie bereits mit der Bedienung des Raspberry Pi vertraut sind, können Sie dieses Kapitel überspringen.

Anmeldung mit Bildschirm
---------------------------

Wenn ein Bildschirm an Ihren Raspberry Pi angeschlossen ist, wird die direkte Interaktion mit dem System erleichtert.

**Erforderliche Komponenten**

* Pironman 5
* Netzadapter
* Micro-SD-Karte oder NVMe SSD mit vorinstalliertem Raspberry Pi OS
* Monitor-Netzadapter
* HDMI-Kabel
* Monitor
* Maus
* Tastatur

**Schritte**

#. Legen Sie die Micro-SD-Karte in den Pironman 5 ein.

#. Schließen Sie Maus und Tastatur an die USB-Ports des Pironman 5 an.

#. Verwenden Sie das HDMI-Kabel, um den Monitor mit dem HDMI-Anschluss des Pironman 5 zu verbinden. Stellen Sie sicher, dass der Monitor mit einer Stromquelle verbunden ist und eingeschaltet ist.

#. Schalten Sie den Pironman 5 mit dem Netzadapter ein. Der Raspberry Pi OS-Desktop sollte bald auf dem Monitor erscheinen.

   .. image:: img/bookwarm.png
      :width: 90%
      

#. Sobald der Desktop sichtbar ist, öffnen Sie das Terminal, indem Sie auf das Terminal-Symbol klicken oder es im Menü suchen, um mit der Eingabe von Befehlen zu beginnen.

Anmeldung ohne Bildschirm
------------------------------------

Falls Sie keinen Zugang zu einem Monitor haben, können Sie Ihren Raspberry Pi dennoch nutzen, indem Sie sich aus der Ferne anmelden.

Für den Zugriff auf die Befehlszeile können Sie SSH verwenden, um sich mit der Bash-Shell des Raspberry Pi zu verbinden, der Standard-Linux-Shell, die es ermöglicht, das Gerät über Befehle zu verwalten.

Für diejenigen, die eine grafische Benutzeroberfläche bevorzugen, bietet eine Remote-Desktop-Anwendung wie VNC Viewer eine visuelle Möglichkeit, Dateien und Operationen aus der Ferne zu verwalten.

**Erforderliche Komponenten**

* Pironman 5 
* Netzadapter
* Micro-SD-Karte oder NVMe SSD mit vorinstalliertem Raspberry Pi OS

Schritte:

#. Legen Sie die Micro-SD-Karte in den Pironman 5 ein.

#. Schließen Sie den Pironman 5 an eine Stromquelle mit dem Netzadapter an.

#. Ausführliche Tutorials zum Einrichten des Fernzugriffs, je nach Betriebssystem Ihres Computers, finden Sie in den folgenden Abschnitten:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop
