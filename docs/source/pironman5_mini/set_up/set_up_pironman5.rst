.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_pironman5_mini:

4. Einrichtung und Softwareinstallation
================================================

Nachdem das System erfolgreich auf die Micro-SD-Karte oder die NVMe-SSD geschrieben wurde, kannst du das jeweilige Speichermedium in den Raspberry Pi einsetzen. Drücke anschließend den Netzschalter, um das Gerät einzuschalten.

Nach dem Einschalten leuchten die verschiedenen Status-LEDs, allerdings funktionieren die RGB-LEDs und der RGB-Lüfter noch nicht, 
da diese zunächst konfiguriert werden müssen. Falls es zu einer verzerrten Darstellung auf dem Bildschirm kommt, kann dies zunächst ignoriert werden – das Problem wird nach der Konfiguration behoben sein.

Bevor du mit der Konfiguration beginnst, musst du dein Raspberry Pi starten und dich anmelden. Falls du nicht weißt, wie das geht, findest du Hilfe auf der offiziellen Raspberry Pi Website: |link_rpi_get_start|.

Wähle dann das passende Konfigurations-Tutorial entsprechend deinem verwendeten System:


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel
    set_up_batocera

**Zum Netzschalter**

Der Netzschalter entspricht dem physischen Power-Button des Raspberry Pi 5 und verhält sich funktional genauso.

* **Herunterfahren**

    * Wenn du das **Raspberry Pi OS Desktop**-System verwendest, kannst du durch zweimaliges kurzes Drücken des Netzschalters den Shutdown-Vorgang auslösen.
    * Beim **Bookworm Lite**-System reicht ein einfaches Drücken zum Einleiten des Herunterfahrens.
    * Für ein erzwungenes Herunterfahren halte den Knopf gedrückt.

* **Einschalten**

    * Wenn das Raspberry Pi ausgeschaltet, aber noch mit Strom versorgt ist, genügt ein kurzer Druck, um es wieder einzuschalten.

* Wenn du ein System verwendest, das den Shutdown-Knopf nicht unterstützt, kannst du ihn für 5 Sekunden gedrückt halten, um ein erzwungenes Herunterfahren durchzuführen, und anschließend mit einem kurzen Druck wieder einschalten.



