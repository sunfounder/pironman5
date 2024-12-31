.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _view_control_dashboard:

Überblick und Steuerung vom Dashboard
========================================

Nach der erfolgreichen Installation des Moduls ``pironman5`` startet der Dienst ``pironman5.service`` automatisch nach jedem Neustart.

Sie können die Überwachungsseite in Ihrem Browser öffnen, um Informationen über Ihren Raspberry Pi zu sehen, RGBs zu konfigurieren, den Lüfter zu steuern usw. Der Link zur Seite lautet: ``http://<ip>:34001``.

Diese Seite enthält **Dashboard**, **History**, **Log** und eine **Einstellungen**-Seite.

.. image:: img/dashboard_tab_new.jpg

  
Dashboard
-------------

Es gibt mehrere Karten, um den aktuellen Status des Raspberry Pi anzuzeigen, darunter:

* **Lüfter**: Zeigt die CPU-Temperatur des Raspberry Pi und die PWM-Lüftergeschwindigkeit an. **GPIO Fan State** zeigt den Status der beiden seitlichen RGB-Lüfter an. Bei der aktuellen Temperatur sind die beiden RGB-Lüfter ausgeschaltet.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%

* **Speicher**: Zeigt die Speicherkapazität des Raspberry Pi an und gibt die belegten und verfügbaren Bereiche der verschiedenen Partitionen an.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Arbeitsspeicher**: Zeigt die Nutzung und den Prozentsatz des RAMs des Raspberry Pi an.

  .. image:: img/dashboard_memory.png
    :width: 90%

* **Netzwerk**: Zeigt die aktuelle Art der Netzwerkverbindung sowie die Upload- und Download-Geschwindigkeiten an.

  .. image:: img/dashboard_network.png
    :width: 90%

* **Prozessor**: Veranschaulicht die CPU-Leistung des Raspberry Pi, einschließlich des Status seiner vier Kerne, der Betriebshäufigkeiten und der CPU-Auslastung in Prozent.

  .. image:: img/dashboard_processor.png
    :width: 90%

Verlauf
----------

Auf der Verlaufsseite können Sie historische Daten einsehen. Wählen Sie die gewünschten Daten in der linken Seitenleiste aus, legen Sie den Zeitraum fest und laden Sie die Daten für diesen Zeitraum herunter.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Protokoll
------------

Die Protokollseite dient zur Ansicht der Protokolle des derzeit laufenden Pironman5-Dienstes. Der Dienst umfasst mehrere Unterdienste, die jeweils ein eigenes Protokoll haben. Wählen Sie das gewünschte Protokoll aus, um die Daten auf der rechten Seite anzuzeigen. Wenn diese leer ist, bedeutet dies möglicherweise, dass es keinen Inhalt gibt.

* Jedes Protokoll hat eine feste Größe von 10 MB. Überschreitet es diese Größe, wird ein weiteres Protokoll erstellt.
* Die Anzahl der Protokolle für denselben Dienst ist auf 10 begrenzt. Überschreitet die Anzahl dieses Limit, wird das älteste Protokoll automatisch gelöscht.
* Es gibt Filtertools über dem Protokollbereich auf der rechten Seite. Sie können die Protokollebene auswählen, nach Schlüsselwörtern filtern und praktische Werkzeuge wie **Zeilenumbruch**, **Auto-Scroll** und **Auto-Update** verwenden.
* Protokolle können auch lokal heruntergeladen werden.

.. image:: img/dashboard_log1.png
  :width: 90%

.. image:: img/dashboard_log2.png
  :width: 90%

Einstellungen
-----------------

Im Menü oben rechts auf der Seite können Sie die Einstellungen nach Ihren Wünschen anpassen. Die Änderungen werden automatisch gespeichert. Wenn erforderlich, können Sie unten die Schaltfläche CLEAR verwenden, um die historischen Daten zu löschen.

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **Dunkelmodus**: Wechseln Sie zwischen hellen und dunklen Themen. Die Option wird im Browser-Cache gespeichert. Ein Wechsel des Browsers oder das Löschen des Caches stellt das Standard-Design zurück.
* **Temperatureinheit**: Stellen Sie die Temperatureinheit ein, die vom System angezeigt wird.

**Über das OLED-Display**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **OLED aktivieren**: Aktivieren oder deaktivieren Sie das OLED.
* **OLED-Disk**: Legen Sie die OLED-Disk fest.
* **OLED-Netzwerkschnittstelle**:

  * **all**: Wechselt zwischen der Anzeige der Ethernet-IP und der Wi-Fi-IP.
  * **eth0**: Zeigt nur die Ethernet-IP an.
  * **wlan0**: Zeigt nur die Wi-Fi-IP an.

* **OLED-Rotation**: Legen Sie die OLED-Rotation fest.

**Über RGB-LEDs**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **RGB aktivieren**: Aktivieren oder deaktivieren Sie die RGB-LEDs.
* **RGB-Farbe**: Stellen Sie die Farbe der RGB-LEDs ein.
* **RGB-Helligkeit**: Passen Sie die Helligkeit der RGB-LEDs mit einem Schieberegler an.
* **RGB-Stil**: Wählen Sie den Anzeigemodus der RGB-LEDs. Optionen sind **Statisch**, **Atmen**, **Fluss**, **Fluss umkehren**, **Regenbogen**, **Regenbogen umkehren** und **Farbkreis**.

  .. note::

     Wenn Sie den **RGB-Stil** auf **Regenbogen**, **Regenbogen umkehren** oder **Farbkreis** setzen, können Sie keine Farbe einstellen.

* **RGB-Geschwindigkeit**: Legen Sie die Geschwindigkeit der RGB-LED-Änderungen fest.

**Über RGB-Lüfter**

.. image:: img/RGB_fans.png
  :width: 600

* **Lüfter-LED**: Sie können die Lüfter-LED auf AN, AUS oder FOLGEN-Modus einstellen.
* **Lüftermodus**: Legen Sie den Betriebsmodus der beiden RGB-Lüfter fest. Diese Modi bestimmen die Bedingungen, unter denen die RGB-Lüfter aktiviert werden.

    * **Leise**: Die RGB-Lüfter werden bei 70°C aktiviert.
    * **Ausgeglichen**: Die RGB-Lüfter werden bei 67,5°C aktiviert.
    * **Kühl**: Die RGB-Lüfter werden bei 60°C aktiviert.
    * **Leistung**: Die RGB-Lüfter werden bei 50°C aktiviert.
    * **Immer An**: Die RGB-Lüfter sind immer eingeschaltet.

Beispielsweise werden die RGB-Lüfter im Modus **Leistung** bei 50°C aktiviert.

Nach dem Speichern, wenn die CPU-Temperatur 50°C übersteigt, sehen Sie, dass sich der **GPIO Fan State** im Dashboard auf EIN ändert und die seitlichen RGB-Lüfter zu drehen beginnen.

.. image:: img/dashboard_rgbfan_on.png
  :width: 300
