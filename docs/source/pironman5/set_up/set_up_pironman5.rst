.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_pironman5_5:

4. Software einrichten oder installieren
================================================

Nachdem das System entweder auf die Micro SD oder die NVMe SSD geschrieben wurde, können Sie diese in den entsprechenden Slot des Pironman 5 einstecken. Drücken Sie dann die Einschalttaste, um das Gerät einzuschalten.

Nach dem Einschalten werden verschiedene Status-LEDs aufleuchten, aber das OLED-Display, die RGB-LEDs und die RGB-Lüfter (die beiden Lüfter an den Seiten) funktionieren noch nicht, da sie konfiguriert werden müssen. Wenn ein Anzeigeproblem auf dem Bildschirm auftritt, ignorieren Sie dies vorerst; es wird nach der Konfiguration behoben.

Bevor Sie mit der Konfiguration beginnen, müssen Sie Ihren Raspberry Pi starten und sich anmelden. Falls Sie nicht wissen, wie Sie sich anmelden können, besuchen Sie die offizielle Raspberry Pi-Website: |link_rpi_get_start|.

Sie können dann das entsprechende Konfigurations-Tutorial basierend auf Ihrem System auswählen.

.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel
    set_up_batocera


**Über den Einschaltknopf**

Der Einschaltknopf entspricht dem des Raspberry Pi 5 und erfüllt die gleiche Funktion.

* **Herunterfahren**

  * Wenn Sie das System **Raspberry Pi OS Desktop** verwenden, können Sie zweimal schnell hintereinander die Einschalttaste drücken, um das Gerät herunterzufahren. 
  * Wenn Sie das System **Raspberry Pi OS Lite** verwenden, drücken Sie die Einschalttaste einmal, um das Herunterfahren zu starten.
  * Halten Sie die Einschalttaste gedrückt, um einen erzwungenen Hard-Shutdown durchzuführen.

* **Einschalten**

  * Wenn das Raspberry Pi-Board heruntergefahren, aber noch mit Strom versorgt ist, drücken Sie einmal kurz die Einschalttaste, um es wieder einzuschalten.

* Wenn Sie ein System verwenden, das die Herunterfahren-Taste nicht unterstützt, können Sie diese 5 Sekunden lang gedrückt halten, um einen Hard-Shutdown zu erzwingen, und durch einmaliges Drücken aus dem ausgeschalteten Zustand wieder einschalten.
