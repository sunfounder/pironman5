.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_dashboard:

Anzeige und Steuerung uber das Dashboard
=========================================

Nachdem du das ``pironman5``-Modul erfolgreich installiert hast, wird der ``pironman5.service`` nach dem Neustart automatisch gestartet.

Nun kannst du die Uberwachungsseite in deinem Browser offnen, um Informationen uber deinen Raspberry Pi anzuzeigen, die RGB-Einstellungen zu konfigurieren und den Lufter zu steuern. Der Link zur Seite lautet: ``http://<ip>:34001``.

Diese Seite enthalt die Bereiche **Dashboard**, **Verlauf**, **Protokoll** und **Einstellungen**.

.. image:: img/dashboard_home.png


Dashboard
---------

Es gibt mehrere Karten, um den relevanten Status des Raspberry Pi anzuzeigen, darunter:

* **Temperatur**: Zeigt die CPU/GPU-Temperatur des Raspberry Pi und die CPU-Luftergeschwindigkeit an. **GPIO Luefterstatus** zeigt den Status der beiden seitlichen GPIO-Lufter an.

  .. image:: img/dashboard_tem.png
    :width: 90%

* **Speicher**: Zeigt die Speicherkapazitat des Raspberry Pi an und zeigt verschiedene Festplattenpartitionen mit ihrem belegten und verfugbaren Speicherplatz.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Arbeitsspeicher**: Zeigt die RAM-Nutzung des Raspberry Pi und den Prozentsatz an.

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Netzwerk**: Zeigt den aktuellen Verbindungstyp des Netzwerks sowie die Upload- und Download-Geschwindigkeiten an.

  .. image:: img/dashboard_network.png
    :width: 90%


* **Prozessor**: Zeigt die CPU-Leistung des Raspberry Pi an, einschlieslich des Status der vier Kerne, der Betriebsfrequenzen und des CPU-Nutzungsprozentsatzes.

  .. image:: img/dashboard_processor.png
    :width: 90%


Verlauf
-------

Die Verlauf-Seite ermoglicht es dir, historische Daten anzuzeigen. Wahle im linken Seitenbereich die Daten aus, die du anzeigen mochtest, wahle dann den Zeitraum aus, um die Daten fur diesen Zeitraum zu sehen. Du kannst sie auch herunterladen.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Protokoll
---------

Die Protokoll-Seite zeigt das Laufzeitprotokoll des Pironman5-Dienstes an.

* Protokolleintrage konnen nach Ebene gefiltert werden (Debug, Info, Warnung, Fehler oder Kritisch).
* Die Protokolldatei kann auch lokal heruntergeladen werden.

.. image:: img/dashboard_log.png
  :width: 90%

Einstellungen
-------------

Auf der Seite Einstellungen kannst du die Dashboard-Anzeige, Systemeinstellungen, den OLED-Bildschirm, die RGB-Beleuchtung und das Lufterverhalten anpassen. Sie zeigt auch grundlegende Netzwerkinformationen wie die MAC-Adresse und die IP-Adresse an.

.. image:: img/dashboard_setting.png
    :width: 600


* **Oberflache**

  Konfiguriere das Erscheinungsbild des Dashboards und das Anzeigeverhalten.

  .. image:: img/dashboard_setting_interface.png
      :width: 600

  * **Dark Mode**: Aktiviere oder deaktiviere das dunkle Design.
  * **Show unmounted disk**: Zeige nicht eingehangte Speichergerate auf der Speicherkarte an.
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

    Verfugbare Seiten:

    * **IP Addresses**: Zeigt IP-Adressen fur alle physischen Netzwerkschnittstellen an.
    * **Disk Usage**: Zeigt Speicherplatznutzungsinformationen fur alle Datentrager an.
    * **Performance Metrics**: Zeigt CPU-Auslastung, CPU-Temperatur, RAM-Auslastung und Luftergeschwindigkeit an.
    * **System Mix**: Zeigt CPU-Auslastung, CPU-Temperatur und IP-Adresse an.


* **RGB**

  Konfiguriere die RGB-LED-Beleuchtungseffekte und das Verhalten.

  .. image:: img/dashboard_setting_rgb.png
      :width: 600

  * **RGB Enable**: Aktiviere oder deaktiviere die RGB-LEDs.
  * **RGB Color**: Lege die Farbe der RGB-LEDs fest.
  * **RGB Brightness**: Passe die Helligkeit der RGB-LEDs an.
  * **RGB Style**: Wahle den RGB-Beleuchtungseffekt aus, einschlielich ``None``, ``Solid``, ``Breathing``, ``Flow``, ``Flow Reverse``, ``Rainbow``, ``Rainbow Reverse`` und ``Hue Cycle``.
  * **RGB Speed**: Passe die Animationsgeschwindigkeit des ausgewahlten RGB-Effekts an.
  * **RGB Led**: Lege die Anzahl der aktiven RGB-LEDs fest.


* **Luefter-LED**

  Konfiguriere den Modus der Luefter-LED.

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  * **Aus**: RGB ausschalten.
  * **Ein**: RGB einschalten.
  * **Folgen**: RGB automatisch je nach Betriebszustand des Luefters einschalten.


* **GPIO-Luefter**

  Konfiguriere den Betriebsmodus der beiden GPIO-Luefter.

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  Der ausgewahlte Modus bestimmt, wann die GPIO-Luefter aktiviert werden.

  * **Quiet**: Die GPIO-Luefter werden bei 70 °C aktiviert.
  * **Balanced**: Die GPIO-Luefter werden bei 67,5 °C aktiviert.
  * **Cool**: Die GPIO-Luefter werden bei 60 °C aktiviert.
  * **Performance**: Die GPIO-Luefter werden bei 50 °C aktiviert.
  * **Always On**: Die GPIO-Luefter sind immer eingeschaltet.


* **System**

  Konfiguriere das Systemverhalten und zeige Gerateinformationen an.

  .. image:: img/dashboard_setting_system.png
      :width: 600

  * **Debug Level**: Lege die Protokollebene des Pironman-5-Dienstes fest.
  * **Mac Address**: Zeigt die MAC-Adressen der Raspberry-Pi-Netzwerkschnittstellen an.
  * **IP Address**: Zeigt die IP-Adressen der Raspberry-Pi-Netzwerkschnittstellen an.
  * **History Retention**: Lege fest, wie viele Tage historische Daten gespeichert werden.
  * **Clear All Data**: Losche alle aufgezeichneten Verlaufsdaten.
  * **Reboot**: Starte den Raspberry Pi aus der Ferne uber das Dashboard neu.
  * **Shutdown**: Fahre den Raspberry Pi aus der Ferne uber das Dashboard sicher herunter.