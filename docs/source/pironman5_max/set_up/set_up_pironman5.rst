.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Experten-Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorabinformationen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_set_up_pironman5:

4. Software einrichten oder installieren
================================================

Sobald das System auf die Micro-SD-Karte oder die NVMe-SSD geschrieben wurde, kannst du das Speichermedium in den entsprechenden Slot am Pironman 5 MAX einsetzen. Drücke anschließend den Power-Button, um das Gerät einzuschalten.

Nach dem Einschalten leuchten die verschiedenen Status-LEDs. Das OLED-Display, die RGB-LEDs und die RGB-Lüfter (die beiden seitlichen Lüfter) funktionieren jedoch zunächst nicht, da sie erst konfiguriert werden müssen. Falls es zu einer verzerrten Darstellung auf dem Bildschirm kommt, kann dies zunächst ignoriert werden – das Problem wird nach der Konfiguration behoben.

Vor der Konfiguration musst du deinen Raspberry Pi starten und dich anmelden. Wenn du nicht weißt, wie das funktioniert, findest du Hilfe auf der offiziellen Raspberry-Pi-Webseite: |link_rpi_get_start|.

Wähle anschließend das passende Konfigurations-Tutorial entsprechend deinem Betriebssystem aus:


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel

.. set_up_batocera


**Zum Power-Button**

Der Power-Button ist direkt mit dem des Raspberry Pi 5 verbunden und übernimmt exakt dessen Funktion.

* **Herunterfahren**

  * Wenn du das System **Raspberry Pi OS Desktop** verwendest, kannst du den Netzschalter zweimal schnell hintereinander drücken, um das Gerät auszuschalten.  
  * Wenn du das System **Raspberry Pi OS Lite** verwendest, drücke den Netzschalter einmal, um den Herunterfahrvorgang zu starten.  
  * Um ein sofortiges Ausschalten zu erzwingen, halte den Netzschalter gedrückt.

* **Einschalten**

  * Wenn der Raspberry Pi heruntergefahren, aber weiterhin mit Strom versorgt ist, genügt ein kurzer Tastendruck zum Einschalten.

* Falls du ein System verwendest, das den Shutdown-Button nicht unterstützt, kannst du den Button für 5 Sekunden gedrückt halten, um ein erzwungenes Herunterfahren durchzuführen. Ein kurzer Druck startet das System anschließend wieder.



