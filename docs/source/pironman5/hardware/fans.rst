.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _fans:

Lüfter
===============

PWM-Lüfter
-----------------

Der PWM-Lüfter im Pironman 5 wird vom Raspberry Pi-System gesteuert und bildet das Herzstück der intelligenten Kühlungslösung, insbesondere unter hoher Belastung. Dieses System kombiniert einen primären PWM-Lüfter mit zwei zusätzlichen RGB-Lüftern für eine verbesserte Kühlleistung und ist eng in das Wärmemanagementsystem des Raspberry Pi 5 integriert.

.. image:: img/fan_tower_cooler.png  
  :width: 600  
  :align: center  

**Elektrische Eigenschaften**

* **Nennspannung**: 5 VDC  
* **Startspannung**: 4,0 V (bei 25°C Ein-/Ausschaltung)  
* **Betriebsspannungsbereich**: 4,0 ~ 5,5 VDC  
* **Nennstrom**: 0,05 A / MAX. 0,08 A  
* **Nennleistung**: 0,25 W / MAX. 0,40 W  
* **Nenndrehzahl**: 3500±10% U/min (bei 25°C, getestet nach 3 Minuten Betrieb)  
* **Maximaler Luftstrom**: 2,46 (MIN. 2,21) CFM (bei null statischem Druck)  
* **Maximaler statischer Druck**: 0,62 (MIN. 0,496) mmH2O (bei null Luftstrom)  
* **Geräuschpegel**: 22,31 dB(A) MAX. 25,31 dB(A)  
* **Lebensdauer**: 40.000 Stunden (bei 25°C, 65% Luftfeuchtigkeit, normale Raumbedingungen)  

**Mechanische Eigenschaften**

* **Abmessungen**: 40x10,4x40 mm (LxBxH)  
* **Rahmenmaterial**: PBT-Kunststoff  
* **Laufradmaterial**: PBT-Kunststoff  
* **Lagertyp**: Hydrauliklager  

**Umgebungsparameter**

* **Betriebstemperatur**: -10°C ~ 70°C  
* **Lagertemperatur**: -40°C ~ 75°C  
* **Betriebsfeuchtigkeit**: 5% ~ 90% RH  
* **Lagerfeuchtigkeit**: 5% ~ 95% RH  

**Lüfterdrehzahlsteuerung basierend auf der Temperatur**  

Der PWM-Lüfter arbeitet dynamisch und passt seine Geschwindigkeit an die Temperatur des Raspberry Pi 5 an:  

* **Unter 50°C**: Lüfter bleibt aus (0% Geschwindigkeit).  
* **Bei 50°C**: Lüfter läuft mit niedriger Geschwindigkeit (30% Geschwindigkeit).  
* **Bei 60°C**: Lüfter erhöht auf mittlere Geschwindigkeit (50% Geschwindigkeit).  
* **Bei 67,5°C**: Lüfter erhöht auf hohe Geschwindigkeit (70% Geschwindigkeit).  
* **Bei 75°C und darüber**: Lüfter läuft mit voller Geschwindigkeit (100% Geschwindigkeit).  

Diese Temperatur-Geschwindigkeits-Steuerung umfasst eine Hysterese von 5°C, um häufige Geschwindigkeitsänderungen zu vermeiden. Beispielsweise reduziert der Lüfter seine Geschwindigkeit erst, wenn die Temperatur 5°C unter den jeweiligen Schwellenwert fällt.  

Die folgenden Befehle ermöglichen es Benutzern, den Betrieb des PWM-Lüfters zu überwachen:  

Um den aktuellen Zustand des Lüfters zu überprüfen:  

.. code-block:: shell

  cat /sys/class/thermal/cooling_device0/cur_state

RGB-Lüfter
-------------------

.. image:: img/size_fan.png

* **Externe Abmessungen**: 40*40*10MM
* **Gewicht**: 13,5±5g/Stück
* **Lebensdauer**: 40.000 Stunden (Raumtemperatur 25°C)
* **Maximaler Luftstrom**: 2,46CFM
* **Maximaler Luftdruck**: 0,62mm-H2O
* **Schallpegel**: 22,31dBA
* **Nennleistung**: 5V/0,1A
* **Nenn-Drehzahl**: 3500±10%RPM
* **Betriebstemperatur**: -10℃~+70℃
* **Lagertemperatur**: -30℃~+85℃
