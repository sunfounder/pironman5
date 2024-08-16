.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lüfter
===============

PWM-Lüfter
-------------

Der PWM-Lüfter im Pironman 5 wird vom Raspberry Pi-System gesteuert.

Bezüglich der Kühlung des Raspberry Pi 5, insbesondere unter hoher Last, verfügt der Pironman 5 über ein intelligentes Kühlsystem. Es umfasst einen primären PWM-Lüfter und zwei zusätzliche RGB-Lüfter. Die Kühlstrategie ist eng mit dem Wärmemanagementsystem des Raspberry Pi 5 verzahnt.

Die Steuerung des PWM-Lüfters basiert auf der Temperatur des Raspberry Pi 5:

* Unter 50°C bleibt der PWM-Lüfter ausgeschaltet (0% Drehzahl).
* Bei 50°C beginnt der Lüfter mit einer niedrigen Drehzahl (30% Drehzahl).
* Erreicht die Temperatur 60°C, erhöht der Lüfter die Drehzahl auf ein mittleres Niveau (50% Drehzahl).
* Bei 67,5°C steigert der Lüfter seine Geschwindigkeit auf ein hohes Niveau (70% Drehzahl).
* Ab 75°C und darüber arbeitet der Lüfter mit voller Geschwindigkeit (100% Drehzahl).

Dieses Temperatur-Drehzahl-Verhältnis gilt auch beim Abfall der Temperatur, mit einer Hysterese von 5°C. Die Lüftergeschwindigkeit reduziert sich, wenn die Temperatur um 5°C unter die jeweiligen Schwellenwerte fällt.

* Befehle zur Überwachung des PWM-Lüfters. Um den Status des PWM-Lüfters zu überprüfen:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Um die Geschwindigkeit des PWM-Lüfters anzuzeigen:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Im Pironman 5 ist der PWM-Lüfter ein entscheidender Bestandteil zur Aufrechterhaltung optimaler Betriebstemperaturen, insbesondere bei intensiven Aufgaben, und sorgt dafür, dass der Raspberry Pi 5 effizient und zuverlässig arbeitet.

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
