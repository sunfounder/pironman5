.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _login_rpi:

Anmeldung beim Raspberry Pi OS
=====================================

In diesem Kapitel lernen Sie, wie Sie sich beim Raspberry Pi anmelden. Unabhängig davon, ob Sie einen Bildschirm angeschlossen haben oder remote darauf zugreifen müssen, wird in diesem Abschnitt erläutert, wie Sie das Terminal öffnen, das Sie in späteren Kapiteln zum Eingeben von Befehlen verwenden werden.

.. note::

    Wenn Sie bereits mit den Vorgängen auf dem Raspberry Pi vertraut sind, können Sie dieses Kapitel überspringen.

Anmeldung mit einem Bildschirm
------------------------------------

Ein angeschlossener Bildschirm erleichtert die direkte Interaktion mit dem Raspberry Pi.

**Erforderliche Komponenten**

* Pironman 5
* Netzadapter
* Micro-SD-Karte oder NVMe-SSD mit vorinstalliertem Raspberry Pi OS
* Monitor-Netzadapter
* HDMI-Kabel
* Monitor
* Maus
* Tastatur

**Schritte**

#. Legen Sie die Micro-SD-Karte in den Pironman 5 ein.

#. Schließen Sie Maus und Tastatur an die USB-Ports des Pironman 5 an.

#. Verbinden Sie den Monitor mit dem HDMI-Anschluss des Pironman 5 über das HDMI-Kabel. Stellen Sie sicher, dass der Monitor an eine Stromquelle angeschlossen und eingeschaltet ist.

#. Schalten Sie den Pironman 5 mit dem Netzadapter ein. Der Desktop von Raspberry Pi OS sollte bald auf dem Monitor erscheinen.

    .. image:: img/bookwarm.png
        :align: center

#. Sobald der Desktop sichtbar ist, öffnen Sie das Terminal, indem Sie auf das Terminal-Symbol klicken oder es im Menü suchen, um mit der Eingabe von Befehlen zu beginnen.

Remote-Anmeldung ohne Bildschirm
------------------------------------

Wenn Sie keinen Zugriff auf einen Monitor haben, können Sie den Raspberry Pi trotzdem remote verwenden.

Für den Zugriff auf die Befehlszeile können Sie SSH verwenden, um sich mit der Bash-Shell des Raspberry Pi zu verbinden, der standardmäßigen Linux-Shell, mit der Sie das Gerät über Befehle verwalten können.

Für diejenigen, die eine grafische Benutzeroberfläche bevorzugen, bietet die Verwendung einer Remote-Desktop-Anwendung wie VNC Viewer eine visuelle Möglichkeit, Dateien und Vorgänge remote zu verwalten.

**Erforderliche Komponenten**

* Pironman 5 
* Netzadapter
* Micro-SD-Karte oder NVMe-SSD mit vorinstalliertem Raspberry Pi OS

Schritte:

#. Legen Sie die Micro-SD-Karte in den Pironman 5 ein.

#. Schließen Sie den Pironman 5 mit dem Netzadapter an eine Stromquelle an.

#. Für detaillierte Anleitungen zur Einrichtung des Remote-Zugriffs, abhängig vom Betriebssystem Ihres Computers, siehe die folgenden Abschnitte:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


