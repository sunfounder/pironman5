.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Power-Schalter-Konverter
==============================

Dies ist ein Modul, das den Power-Schalter des Raspberry Pi 5 nach außen erweitert.

.. image:: img/power_switch_conventor.jpeg

**Hinzufügen des Power-Knopfes**

* Der Raspberry Pi 5 verfügt über einen **J2** Jumper, der sich zwischen dem RTC-Batterieanschluss und dem Platinenrand befindet. Dieser Breakout ermöglicht das Hinzufügen eines benutzerdefinierten Power-Knopfes, indem ein normalerweise offener (NO) Taster über die beiden Pads verbunden wird. Ein kurzes Drücken dieses Schalters ahmt die Funktionalität des internen Power-Knopfes nach.

   .. image:: img/pi5_j2.jpg

* Auf dem Pironman 5 gibt es einen **Power Switch Converter**, der den **J2** Jumper mit zwei Pogo-Pins zu einem externen Power-Knopf erweitert.

   .. image:: img/power_switch_convertor.png

* Nun kann der Raspberry Pi 5 über den Power-Knopf ein- und ausgeschaltet werden.

   .. image:: img/pironman_button.JPG

**Power-Cycling**

Beim ersten Einschalten deines Raspberry Pi 5 wird er automatisch hochgefahren und startet das Betriebssystem, ohne dass der Knopf gedrückt werden muss.

Wenn der Raspberry Pi Desktop läuft, wird durch ein kurzes Drücken des Power-Knopfes der Herunterfahrvorgang eingeleitet. Ein Menü erscheint, in dem Optionen zum Herunterfahren, Neustarten oder Abmelden angeboten werden. Das Auswählen einer Option oder das erneute Drücken des Power-Knopfes startet das saubere Herunterfahren.

.. image:: img/button_shutdown.png

**Herunterfahren**

    * Wenn du das **Raspberry Pi OS Desktop**-System verwendest, kannst du den Power-Knopf zweimal schnell hintereinander drücken, um das System herunterzufahren.
    * Wenn du das **Raspberry Pi OS Lite**-System ohne Desktop verwendest, drücke den Power-Knopf einmal, um das Herunterfahren einzuleiten.
    * Um einen harten Shutdown zu erzwingen, halte den Power-Knopf gedrückt.


**Einschalten**

    * Wenn das Raspberry Pi-Board heruntergefahren ist, aber noch mit Strom versorgt wird, drücke einmal, um es aus dem Shutdown-Zustand einzuschalten.

.. note::

    Wenn du ein System betreibst, das keinen Shutdown-Knopf unterstützt, kannst du den Power-Knopf 5 Sekunden lang gedrückt halten, um einen harten Shutdown zu erzwingen, und einmal drücken, um es aus dem Shutdown-Zustand einzuschalten.

