
.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Entdecke gemeinsam mit anderen Technikbegeisterten noch mehr rund um Raspberry Pi, Arduino und ESP32.

    **Warum solltest du beitreten?**

    - **Expertenhilfe**: Erhalte Unterstützung bei technischen Problemen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um deine Fähigkeiten weiter auszubauen.
    - **Exklusive Vorschauen**: Erhalte frühzeitige Informationen zu neuen Produktankündigungen und exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an spannenden Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _view_control_dashboard_mini:

Anzeigen und Steuern über das Dashboard
============================================

Nach erfolgreicher Installation des ``pironman5``-Moduls wird der Dienst ``pironman5.service`` beim Neustart automatisch gestartet.

Du kannst nun im Browser die Überwachungsseite öffnen, um Informationen über deinen Raspberry Pi einzusehen, die RGB-LEDs zu konfigurieren, den Lüfter zu steuern und mehr. Der Seitenlink lautet: ``http://<ip>:34001``.

Die Seite umfasst die Bereiche **Dashboard**, **History**, **Log** und **Settings**.

.. image:: img/dashboard_tab.png
  :width: 90%


Dashboard
-----------------------

Das Dashboard zeigt verschiedene Statuskarten deines Raspberry Pi an, darunter:

* **Fan**: Zeigt die CPU-Temperatur des Raspberry Pi sowie die Drehzahl des PWM-Lüfters. **GPIO Fan State** gibt den Status des RGB-Lüfters an. Bei der aktuellen Temperatur ist der RGB-Lüfter ausgeschaltet.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%


* **Storage**: Zeigt die Speicherkapazität des Raspberry Pi an – mit Übersicht über die Partitionen, den belegten und verfügbaren Speicherplatz.

  .. image:: img/dashboard_storage.png
    :width: 90%


* **Memory**: Zeigt den aktuellen RAM-Verbrauch des Raspberry Pi in Prozent und absoluten Werten.

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Network**: Zeigt den aktuellen Verbindungstyp sowie Upload- und Download-Geschwindigkeit.

  .. image:: img/dashboard_network.png
    :width: 90%


* **Processor**: Veranschaulicht die CPU-Auslastung des Raspberry Pi inklusive Status der vier Kerne, deren Taktfrequenzen und Auslastung.

  .. image:: img/dashboard_processor.png
    :width: 90%


History
--------------

Auf der History-Seite kannst du historische Daten einsehen. Wähle links die gewünschten Metriken und anschließend den Zeitraum aus. Die Daten können zudem heruntergeladen werden.

.. image:: img/dashboard_history.png
  :width: 90%


Log
------------

Die Log-Seite dient zur Ansicht der Protokolle des aktuell laufenden pironman5-Dienstes. Dieser umfasst mehrere Untersysteme, die jeweils eigene Logdateien führen. Wähle das gewünschte Log aus, um die Inhalte anzuzeigen. Ist das Feld leer, bedeutet dies, dass keine Logdaten vorhanden sind.

* Jede Logdatei hat eine feste Größe von 10 MB. Wird diese überschritten, wird eine neue Logdatei erstellt.
* Es sind maximal 10 Logdateien pro Dienst zulässig. Wird diese Grenze überschritten, wird die älteste automatisch gelöscht.
* Über dem Logbereich befinden sich Filterfunktionen. Du kannst nach Log-Level oder Stichwörtern filtern und Tools wie **Line Wrap**, **Auto Scroll** und **Auto Update** nutzen.
* Logdateien lassen sich auch lokal speichern.

.. image:: img/dashboard_log.png
  :width: 90%


Settings
-----------------

Im rechten oberen Bereich befindet sich das Einstellungsmenü.

.. note::

    Nach Änderungen musst du unten auf **SAVE** klicken, um die Einstellungen zu übernehmen.

.. image:: img/dashboard_settings.png
  :width: 90%


* **Dark Mode**: Wechsle zwischen hellem und dunklem Design. Die Einstellung wird im Browsercache gespeichert – ein Browserwechsel oder das Leeren des Caches setzt das Design auf hell zurück.
* **Temperature Unit**: Lege die Temperaturanzeige in Celsius oder Fahrenheit fest.
* **Fan Mode**: Bestimme das Betriebsverhalten des RGB-Lüfters. Die Modi definieren die Temperaturgrenze, ab der der Lüfter aktiv wird.

    * **Quiet**: Aktiviert bei 70°C.
    * **Balanced**: Aktiviert bei 67.5 °C.
    * **Cool**: Aktiviert bei 60°C.
    * **Performance**: Aktiviert bei 50°C.
    * **Always On**: Lüfter läuft dauerhaft.

    Beispiel: Wenn der Modus **Performance** gewählt ist, startet der RGB-Lüfter bei 50 °C automatisch.

    Wird die Einstellung gespeichert und die CPU-Temperatur übersteigt 50 °C, zeigt das Dashboard den **GPIO Fan State** als ON an und der Lüfter beginnt zu drehen.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300


* **RGB Brightness**: Mit dem Schieberegler lässt sich die Helligkeit der RGB-LEDs anpassen.
* **RGB Color**: Definiere die Farbe der RGB-LEDs.
* **RGB Style**: Wähle den Anzeigemodus der RGB-LEDs. Verfügbare Optionen sind **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse** und **Hue Cycle**.

.. note::

    Wenn du den **RGB Style** auf **Rainbow**, **Rainbow Reverse** oder **Hue Cycle** einstellst, kannst du keine Farbe manuell wählen.


* **RGB Speed**: Stelle die Animationsgeschwindigkeit der RGB-LEDs ein.