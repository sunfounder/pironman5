.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_dashboard_5:

Anzeigen und Steuern über das Dashboard
=========================================

Nach erfolgreicher Installation des Moduls ``pironman5`` startet der Dienst ``pironman5.service`` automatisch beim Neustart.

Jetzt kannst du die Überwachungsseite in deinem Browser öffnen, um Informationen zu deinem Raspberry Pi anzuzeigen, die RGB-LEDs zu konfigurieren und den Lüfter zu steuern. Der Link zur Seite lautet: ``http://<ip>:34001``.

Diese Seite umfasst **Dashboard**, **Verlauf**, **Protokoll** und eine **Einstellungen**-Seite.

.. image:: img/dashboard_home.png


Dashboard
-----------------------

Es gibt mehrere Karten zur Anzeige des relevanten Status des Raspberry Pi, darunter:

* **Temperatur**: Zeigt die CPU/GPU-Temperatur des Raspberry Pi und die CPU-Lüftergeschwindigkeit an. **GPIO Fan State** zeigt den Status der beiden seitlichen GPIO-Lüfter.

  .. image:: img/dashboard_tem.png
    :width: 90%

* **Speicher**: Zeigt die Speicherkapazität des Raspberry Pi an, einschließlich der verschiedenen Datenträgerpartitionen mit ihrem belegten und verfügbaren Speicherplatz.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Arbeitsspeicher**: Zeigt die RAM-Auslastung des Raspberry Pi und den Prozentsatz an.

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Netzwerk**: Zeigt den aktuellen Netzwerkverbindungstyp sowie Upload- und Download-Geschwindigkeiten an.

  .. image:: img/dashboard_network.png
    :width: 90%


* **Prozessor**: Veranschaulicht die CPU-Leistung des Raspberry Pi, einschließlich des Status seiner vier Kerne, der Betriebsfrequenzen und der CPU-Auslastung in Prozent.

  .. image:: img/dashboard_processor.png
    :width: 90%


Verlauf
--------------

Auf der Seite „Verlauf“ kannst du historische Daten anzeigen. Wähle im linken Seitenmenü die gewünschten Daten aus, lege den Zeitraum fest, um die Daten für diesen Zeitraum anzuzeigen. Du kannst die Daten auch herunterladen.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Protokoll
------------

Die Seite „Protokoll“ zeigt das Laufzeitprotokoll des Pironman5-Dienstes an.

* Protokolleinträge können nach Ebene gefiltert werden (Debug, Info, Warnung, Fehler oder Kritisch).
* Die Protokolldatei kann auch lokal heruntergeladen werden.

.. image:: img/dashboard_log.png
  :width: 90%

Einstellungen
-------------

Auf der Seite „Einstellungen“ kannst du die Dashboard-Anzeige, Systemeinstellungen, den OLED-Bildschirm, die RGB-Beleuchtung und das Lüfterverhalten anpassen. Sie zeigt auch grundlegende Netzwerkinformationen wie die MAC-Adresse und die IP-Adresse an.

.. image:: img/dashboard_setting.png
    :width: 600


* **Oberfläche**

  Konfiguriere das Erscheinungsbild des Dashboards und das Anzeigeverhalten.

  .. image:: img/dashboard_setting_interface.png
      :width: 600

  * **Dark Mode**: Aktiviere oder deaktiviere das dunkle Design.
  * **Show unmounted disk**: Zeige nicht eingehängte Speichergeräte auf der Speicherkarte an.
  * **Show all cores**: Zeige alle CPU-Kerne auf der Prozessorkarte an.
  * **Card layout**: Passe das Layout der Dashboard-Karten an.
  * **Temperature Unit**: Wechsle zwischen Celsius und Fahrenheit.
  * **Web UI Version**: Zeigt die aktuelle Dashboard-Version an.


* **OLED**

  Konfiguriere die Anzeige und das Verhalten des OLED-Bildschirms.

  .. image:: img/dashboard_setting_oled.png
      :width: 600

  * **OLED Enable**: Aktiviere oder deaktiviere den OLED-Bildschirm.
  * **OLED Rotation**: Drehe die OLED-Anzeige zwischen ``0°`` und ``180°``.
  * **OLED Sleep Timeout**: Lege fest, wie lange der OLED-Bildschirm eingeschaltet bleibt, bevor er sich automatisch ausschaltet.
  * **OLED Pages**: Konfiguriere, welche Seiten auf dem OLED-Bildschirm angezeigt werden, und passe ihre Anzeigereihenfolge an.

    Verfügbare Seiten:

    * **IP Addresses**: Zeigt IP-Adressen für alle physischen Netzwerkschnittstellen an.
    * **Disk Usage**: Zeigt Speicherplatznutzungsinformationen für alle Datenträger an.
    * **Performance Metrics**: Zeigt CPU-Auslastung, CPU-Temperatur, RAM-Auslastung und Lüftergeschwindigkeit an.
    * **System Mix**: Zeigt CPU-Auslastung, CPU-Temperatur und IP-Adresse an.


* **RGB**

  Konfiguriere die RGB-LED-Beleuchtungseffekte und das Verhalten.

  .. image:: img/dashboard_setting_rgb.png
      :width: 600

  * **RGB Enable**: Aktiviere oder deaktiviere die RGB-LEDs.
  * **RGB Color**: Lege die Farbe der RGB-LEDs fest.
  * **RGB Brightness**: Passe die Helligkeit der RGB-LEDs an.
  * **RGB Style**: Wähle den RGB-Beleuchtungseffekt aus, einschließlich ``None``, ``Solid``, ``Breathing``, ``Flow``, ``Flow Reverse``, ``Rainbow``, ``Rainbow Reverse`` und ``Hue Cycle``.
  * **RGB Speed**: Passe die Animationsgeschwindigkeit des ausgewählten RGB-Effekts an.
  * **RGB Led**: Lege die Anzahl der aktiven RGB-LEDs fest.


* **GPIO-Lüfter**

  Konfiguriere den Betriebsmodus der beiden GPIO-Lüfter.

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  Der ausgewählte Modus bestimmt, wann die GPIO-Lüfter aktiviert werden.

  * **Quiet**: Die GPIO-Lüfter werden bei 70 °C aktiviert.
  * **Balanced**: Die GPIO-Lüfter werden bei 67,5 °C aktiviert.
  * **Cool**: Die GPIO-Lüfter werden bei 60 °C aktiviert.
  * **Performance**: Die GPIO-Lüfter werden bei 50 °C aktiviert.
  * **Always On**: Die GPIO-Lüfter sind immer eingeschaltet.


* **System**

  Konfiguriere das Systemverhalten und zeige Geräteinformationen an.

  .. image:: img/dashboard_setting_system.png
      :width: 600

  * **Debug Level**: Lege die Protokollebene des Pironman-5-Dienstes fest.
  * **Mac Address**: Zeigt die MAC-Adressen der Raspberry-Pi-Netzwerkschnittstellen an.
  * **IP Address**: Zeigt die IP-Adressen der Raspberry-Pi-Netzwerkschnittstellen an.
  * **History Retention**: Lege fest, wie viele Tage historische Daten gespeichert werden.
  * **Clear All Data**: Lösche alle aufgezeichneten Verlaufsdaten.
  * **Reboot**: Starte den Raspberry Pi aus der Ferne über das Dashboard neu.
  * **Shutdown**: Fahre den Raspberry Pi aus der Ferne über das Dashboard sicher herunter.