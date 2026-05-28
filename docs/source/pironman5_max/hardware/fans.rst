.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _fan_max:

Lüfter
============

CPU-Lüfter
-------------

Der CPU-Lüfter im Pironman 5 MAX wird vom Raspberry Pi System gesteuert.

Im Hinblick auf Kühlungslösungen für den Raspberry Pi 5, insbesondere unter hoher Last, ist das Design des Pironman 5 MAX mit einem intelligenten Kühlsystem ausgestattet. Es umfasst einen Haupt-CPU-Lüfter und zwei ergänzende GPIO-Lüfter. Die Kühlstrategie ist eng mit dem thermischen Managementsystem des Raspberry Pi 5 integriert.

Der Betrieb des CPU-Lüfters basiert auf der Temperatur des Raspberry Pi 5:

* Unter 50°C bleibt der CPU-Lüfter aus (0 % Geschwindigkeit).
* Bei 50°C startet der Lüfter mit niedriger Geschwindigkeit (30 % Geschwindigkeit).
* Bei 60°C erhöht der Lüfter die Geschwindigkeit auf mittlere Stufe (50 % Geschwindigkeit).
* Bei 67,5°C steigert sich die Lüftergeschwindigkeit auf hohe Stufe (70 % Geschwindigkeit).
* Ab 75°C läuft der Lüfter mit maximaler Geschwindigkeit (100 % Geschwindigkeit).

Diese Temperatur-Geschwindigkeits-Beziehung gilt auch, wenn die Temperatur sinkt, mit einer Hysterese von 5°C. Die Lüftergeschwindigkeit reduziert sich, wenn die Temperatur 5°C unterhalb eines dieser Schwellenwerte fällt.

* Befehle zur Überwachung des CPU-Lüfters. Um den Status des CPU-Lüfters zu prüfen:

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Um die Lüftergeschwindigkeit des CPU-Lüfters anzuzeigen:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Im Pironman 5 MAX ist der CPU-Lüfter eine kritische Komponente, um optimale Betriebstemperaturen aufrechtzuerhalten, insbesondere bei intensiven Aufgaben, und sorgt dafür, dass der Raspberry Pi 5 effizient und zuverlässig läuft.

GPIO-Lüfter
-------------------

.. image:: img/size_fan.png

* **Außenabmessung**: 40*40*10MM
* **Gewicht**: 13,5±5g/Stück
* **Lebensdauer**: 30.000 Stunden (Raumtemperatur 25°C)
* **Maximaler Luftstrom**: 2,46CFM
* **Max. Luftdruck**: 0,62mm-H2O
* **Akustischer Schall**: 22,31dBA
* **Nenn-Eingangsleistung**: 5V/0,15A
* **Nenn-Drehzahl**: 3500±10%RPM
* **Betriebstemperatur**: -10℃~+60℃
* **Lagerungstemperatur**: -20℃~+70℃

