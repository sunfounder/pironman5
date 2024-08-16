.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _view_control_dashboard:

Überwachen und Steuern über das Dashboard
==============================================

Nach der erfolgreichen Installation des ``pironman5``-Moduls startet der ``pironman5.service`` automatisch nach jedem Neustart.

Nun können Sie die Überwachungsseite in Ihrem Browser öffnen, um Informationen über Ihren Raspberry Pi anzuzeigen, die RGB-LEDs zu konfigurieren und den Lüfter zu steuern. Der Link zur Seite lautet: ``http://<ip>:34001``.

Diese Seite enthält die Bereiche **Dashboard**, **Verlauf**, **Log** und **Einstellungen**.

.. image:: img/dashboard_tab.png
  :width: 90%
  
  
Dashboard
-----------------------

Es gibt mehrere Karten, um den relevanten Status des Raspberry Pi anzuzeigen, einschließlich:

* **Lüfter**: Zeigt die CPU-Temperatur des Raspberry Pi und die PWM-Lüftergeschwindigkeit an. Der **GPIO-Lüfterstatus** zeigt den Zustand der beiden seitlichen RGB-Lüfter an. Bei der aktuellen Temperatur sind die beiden RGB-Lüfter ausgeschaltet.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Speicher**: Zeigt die Speicherkapazität des Raspberry Pi an und zeigt verschiedene Festplattenpartitionen mit ihrem belegten und freien Speicherplatz.

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Arbeitsspeicher**: Zeigt die RAM-Nutzung des Raspberry Pi und den prozentualen Anteil an.

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Netzwerk**: Zeigt den aktuellen Verbindungstyp sowie Upload- und Download-Geschwindigkeiten an.

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Prozessor**: Stellt die CPU-Leistung des Raspberry Pi dar, einschließlich des Status seiner vier Kerne, der Betriebshäufigkeiten und des CPU-Nutzungsanteils.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

Verlauf
--------------

Auf der Verlaufsseite können Sie historische Daten anzeigen. Wählen Sie die Daten, die Sie ansehen möchten, in der linken Seitenleiste aus, wählen Sie den Zeitraum aus, und Sie können die Daten für diesen Zeitraum anzeigen und auch herunterladen.

.. image:: img/dashboard_history.png
  :width: 90%
  

Log
------------

Auf der Log-Seite können Sie die Protokolle des derzeit laufenden Pironman5-Dienstes anzeigen. Der Pironman5-Dienst umfasst mehrere Untersysteme, die jeweils eigene Protokolle führen. Wählen Sie das Protokoll aus, das Sie ansehen möchten, und die Protokolldaten werden rechts angezeigt. Wenn es leer ist, bedeutet dies möglicherweise, dass keine Protokolldaten vorhanden sind.

* Jedes Protokoll hat eine feste Größe von 10MB. Wenn diese Größe überschritten wird, wird ein zweites Protokoll erstellt.
* Die Anzahl der Protokolle für denselben Dienst ist auf 10 begrenzt. Wenn diese Anzahl überschritten wird, wird das älteste Protokoll automatisch gelöscht.
* Es gibt Filterwerkzeuge über dem Protokollbereich auf der rechten Seite. Sie können den Protokollierungsgrad auswählen, nach Stichwörtern filtern und verschiedene praktische Werkzeuge nutzen, darunter **Zeilenumbruch**, **Automatisches Scrollen** und **Automatische Aktualisierung**.
* Protokolle können auch lokal heruntergeladen werden.

.. image:: img/dashboard_log.png
  :width: 90%
  

Einstellungen
-----------------

Es gibt ein Einstellungsmenü in der oberen rechten Ecke der Seite. 
.. note::
    
    Nach Änderungen müssen Sie auf die **SPEICHERN**-Schaltfläche am unteren Rand der Seite klicken, um die Einstellungen zu speichern.

.. image:: img/dashboard_settings.png
  :width: 90%
  

* **Dunkelmodus**: Wechseln Sie zwischen den Themen Hell und Dunkel. Diese Einstellung wird im Browsercache gespeichert. Ein Wechsel des Browsers oder das Löschen des Caches stellt das Standard-Hellthema wieder her.
* **Temperatureinheit**: Legen Sie die im System angezeigte Temperatureinheit fest.
* **Lüftermodus**: Sie können den Betriebsmodus der beiden RGB-Lüfter einstellen. Diese Modi bestimmen, unter welchen Bedingungen die RGB-Lüfter aktiviert werden.

    * **Leise**: Die RGB-Lüfter werden bei 70°C aktiviert.
    * **Ausgewogen**: Die RGB-Lüfter werden bei 67,5°C aktiviert.
    * **Kühl**: Die RGB-Lüfter werden bei 60°C aktiviert.
    * **Leistung**: Die RGB-Lüfter werden bei 50°C aktiviert.
    * **Immer An**: Die RGB-Lüfter sind immer eingeschaltet.

    Wenn zum Beispiel der **Leistung**-Modus eingestellt ist, werden die RGB-Lüfter bei 50°C aktiviert.

    Nach dem Speichern, wenn die CPU-Temperatur 50°C überschreitet, sehen Sie im Dashboard, dass der **GPIO-Lüfterstatus** auf ON wechselt und die seitlichen RGB-Lüfter zu drehen beginnen.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300
    

* **RGB-Helligkeit**: Sie können die Helligkeit der RGB-LEDs über einen Schieberegler anpassen.
* **RGB-Farbe**: Stellen Sie die Farbe der RGB-LEDs ein.
* **RGB-Stil**: Wählen Sie den Anzeigemodus der RGB-LEDs. Optionen sind **Statisch**, **Atmend**, **Fließend**, **Fließend Rückwärts**, **Regenbogen**, **Regenbogen Rückwärts** und **Farbzyklus**.

.. note::

  Wenn Sie den **RGB-Stil** auf **Regenbogen**, **Regenbogen Rückwärts** oder **Farbzyklus** einstellen, können Sie die Farbe nicht ändern.


* **RGB-Geschwindigkeit**: Legen Sie die Geschwindigkeit der RGB-LED-Änderungen fest.
