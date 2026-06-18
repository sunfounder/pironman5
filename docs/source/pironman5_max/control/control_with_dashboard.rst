.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_dashboard:

Dashboard-Ansicht und -Steuerung
=========================================

Sobald du das ``pironman5``-Modul erfolgreich installiert hast, wird der ``pironman5.service`` nach dem Neustart automatisch gestartet.

Nun kannst du die Überwachungsseite in deinem Browser öffnen, um Informationen über deinen Raspberry Pi anzuzeigen, das RGB zu konfigurieren und den Lüfter zu steuern usw. Der Seitenlink lautet: ``http://<ip>:34001``.

Diese Seite enthält die Seiten **Dashboard**, **Verlauf**, **Log** und **Einstellungen**.

.. image:: img/dashboard_home.png


Dashboard
-----------------------

Es gibt mehrere Karten, um den relevanten Status des Raspberry Pi anzuzeigen, darunter:

* **Temperatur**: Zeigt die CPU/GPU-Temperatur des Raspberry Pi und die CPU-Lüftergeschwindigkeit an. **GPIO-Lüfterstatus** zeigt den Status der beiden seitlichen GPIO-Lüfter.

  .. image:: img/dashboard_tem.png
    :width: 90%

* **Speicher**: Zeigt die Speicherkapazität des Raspberry Pi an, mit verschiedenen Datenträgerpartitionen und deren belegtem und verfügbarem Speicherplatz.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Arbeitsspeicher**: Zeigt die RAM-Auslastung und den Prozentsatz des Raspberry Pi an.

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Netzwerk**: Zeigt den aktuellen Netzwerkverbindungstyp sowie Upload- und Download-Geschwindigkeiten an.

  .. image:: img/dashboard_network.png
    :width: 90%


* **Prozessor**: Zeigt die CPU-Leistung des Raspberry Pi an, einschließlich des Status seiner vier Kerne, Betriebsfrequenzen und CPU-Auslastung in Prozent.

  .. image:: img/dashboard_processor.png
    :width: 90%


Verlauf
--------------

Die Seite Verlauf ermöglicht es dir, historische Daten anzuzeigen. Wähle in der linken Seitenleiste die Daten aus, die du anzeigen möchtest, dann wähle den Zeitraum aus, um die Daten für diesen Zeitraum zu sehen. Du kannst sie auch herunterladen.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Log
------------

Die Log-Seite zeigt das Laufzeitprotokoll des pironman5-Dienstes an.

* Logeinträge können nach Schweregrad gefiltert werden (Debug, Info, Warning, Error oder Critical).
* Die Logdatei kann auch lokal heruntergeladen werden.

.. image:: img/dashboard_log.png
  :width: 90%

Einstellungen
---------------

Die Seite Einstellungen ermöglicht es dir, die Dashboard-Anzeige, Systemeinstellungen, den OLED-Bildschirm, die RGB-Beleuchtung und das Lüfterverhalten anzupassen. Sie zeigt auch grundlegende Netzwerkinformationen wie die MAC-Adresse und IP-Adresse an.

.. image:: img/dashboard_setting.png
    :width: 600


* **Oberfläche**

  Konfiguriere das Erscheinungsbild und das Anzeigeverhalten des Dashboards.

  .. image:: img/dashboard_setting_interface.png
      :width: 600

  * **Dark Mode**: Dunkles Design aktivieren oder deaktivieren.
  * **Show unmounted disk**: Nicht eingehängte Datenträger auf der Speicherkarte anzeigen.
  * **Show all cores**: Alle CPU-Kerne auf der Prozessorkarte anzeigen.
  * **Card layout**: Das Dashboard-Kartenlayout anpassen.
  * **Temperature Unit**: Zwischen Celsius und Fahrenheit umschalten.
  * **Web UI Version**: Zeigt die aktuelle Dashboard-Version an.


* **OLED**

  Konfiguriere die Anzeige und das Verhalten des OLED-Bildschirms.

  .. image:: img/dashboard_setting_oled.png
      :width: 600

  * **OLED Enable**: OLED-Bildschirm aktivieren oder deaktivieren.
  * **OLED Rotation**: OLED-Anzeige zwischen ``0°`` und ``180°`` drehen.
  * **OLED Sleep Timeout**: Legt fest, wie lange der OLED-Bildschirm eingeschaltet bleibt, bevor er sich automatisch ausschaltet.
  * **OLED Pages**: Konfiguriere, welche Seiten auf dem OLED-Bildschirm angezeigt werden, und passe deren Anzeigereihenfolge an.

    Verfügbare Seiten umfassen:

    * **IP Addresses**: Zeigt IP-Adressen für alle physischen Netzwerkschnittstellen an.
    * **Disk Usage**: Zeigt Datenträgerinformationen für alle Datenträger an.
    * **Performance Metrics**: Zeigt CPU-Auslastung, CPU-Temperatur, RAM-Auslastung und Lüftergeschwindigkeit an.
    * **System Mix**: Zeigt CPU-Auslastung, CPU-Temperatur und IP-Adresse an.


* **RGB**

  Konfiguriere die RGB-LED-Beleuchtungseffekte und das Verhalten.

  .. image:: img/dashboard_setting_rgb.png
      :width: 600

  * **RGB Enable**: RGB-LEDs aktivieren oder deaktivieren.
  * **RGB Color**: RGB-LED-Farbe festlegen.
  * **RGB Brightness**: RGB-LED-Helligkeit anpassen.
  * **RGB Style**: Wähle den RGB-Beleuchtungseffekt, einschließlich ``None``, ``Solid``, ``Breathing``, ``Flow``, ``Flow Reverse``, ``Rainbow``, ``Rainbow Reverse`` und ``Hue Cycle``.
  * **RGB Speed**: Animationsgeschwindigkeit des ausgewählten RGB-Effekts anpassen.
  * **RGB Led**: Anzahl der aktiven RGB-LEDs festlegen.


* **GPIO-Lüfter**

  Konfiguriere den Betriebsmodus und das LED-Verhalten der beiden GPIO-Lüfter.

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  * **Fan LED**

    Steuert das RGB-Beleuchtungsverhalten der GPIO-Lüfter.

    * **ON**: Fan-LEDs leuchten immer.
    * **OFF**: Fan-LEDs bleiben aus.
    * **FOLLOW**: Fan-LEDs folgen den System-RGB-Beleuchtungseffekten.

  * **GPIO-Lüftermodus**

    Der ausgewählte Modus bestimmt, wann die GPIO-Lüfter aktiviert werden.

    * **Quiet**: Die GPIO-Lüfter werden bei 70°C aktiviert.
    * **Balanced**: Die GPIO-Lüfter werden bei 67,5°C aktiviert.
    * **Cool**: Die GPIO-Lüfter werden bei 60°C aktiviert.
    * **Performance**: Die GPIO-Lüfter werden bei 50°C aktiviert.
    * **Always On**: Die GPIO-Lüfter bleiben immer aktiv.


* **System**

  Konfiguriere das Systemverhalten und zeige Geräteinformationen an.

  .. image:: img/dashboard_setting_system.png
      :width: 600

  * **Debug Level**: Legt die Protokollierungsebene des pironman5-Dienstes fest.
  * **Mac Address**: Zeigt die MAC-Adressen der Netzwerkschnittstellen des Raspberry Pi an.
  * **IP Address**: Zeigt die IP-Adressen der Netzwerkschnittstellen des Raspberry Pi an.
  * **History Retention**: Legt fest, wie viele Tage historische Daten gespeichert werden.
  * **Clear All Data**: Alle aufgezeichneten Verlaufsdaten löschen.
  * **Reboot**: Starte den Raspberry Pi aus der Ferne über das Dashboard neu.
  * **Shutdown**: Fahre den Raspberry Pi aus der Ferne über das Dashboard sicher herunter.
