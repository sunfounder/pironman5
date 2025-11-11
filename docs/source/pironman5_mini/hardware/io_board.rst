.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Entdecke gemeinsam mit anderen Technikbegeisterten noch mehr über Raspberry Pi, Arduino und ESP32.

    **Warum solltest du beitreten?**

    - **Expertenhilfe**: Erhalte Unterstützung bei technischen Problemen und Fragen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produktankündigungen und erhalte exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und kreativ zu werden? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Pironman 5 Mini HAT
===========================================


.. image:: img/pironman5mini_hat.png

RGB-LEDs
------------

.. image:: img/io_board_rgb.png

Die Platine ist mit 4 WS2812-RGB-LEDs ausgestattet, 
die individuell konfigurierbar sind. 
Nutzer:innen können sie ein- und ausschalten, 
die Farbe ändern, die Helligkeit anpassen, 
den Anzeigeeffekt wechseln und die Änderungsrate einstellen.

* Zum Ein- oder Ausschalten der RGB-LEDs – ``true`` für ein, ``false`` für aus:

.. code-block:: shell

  sudo pironman5 -re true

* Um die Farbe zu ändern, gib den gewünschten Hexadezimalwert ein, z. B. ``fe1a1a``:

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Um die Helligkeit anzupassen (0–100 %):

.. code-block:: shell

  sudo pironman5 -rb 100

* Zum Wechseln des Anzeigeeffekts stehen folgende Optionen zur Verfügung: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``

.. note::

  Wenn du den Anzeigeeffekt auf ``rainbow``, ``rainbow_reverse`` oder ``hue_cycle`` stellst, lässt sich die Farbe nicht mehr über ``sudo pironman5 -rc`` ändern.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Um die Geschwindigkeit des Effekts zu ändern (0–100 %):

.. code-block:: shell

  sudo pironman5 -rp 80

RGB-Steuerpin
-------------------------

Die RGB-LEDs werden per SPI angesteuert und sind an **GPIO10** (SPI MOSI) angeschlossen. 
Zwei Pins verbinden die RGB-LEDs mit GPIO10. Wird diese Funktion nicht genutzt, kann der Jumper entfernt werden.

 .. image:: img/io_board_rgb_pin.png

RGB-Ausgangspins
-------------------------

 .. image:: img/io_board_rgb_out.png

Die WS2812-RGB-LEDs unterstützen serielle Kaskadierung, sodass ein externer RGB-LED-Streifen angeschlossen werden kann. Verbinde den **SIG**-Pin mit dem **DIN**-Pin des Streifens zur Erweiterung.

Standardmäßig sind 4 RGB-LEDs vorkonfiguriert. Um weitere LEDs zu nutzen, erhöhe die Anzahl mit:

.. code-block:: shell

  sudo pironman5 -rl 12



RGB-Lüfteranschlüsse
-------------------------

Die IO-Erweiterungsplatine unterstützt einen 5V-Lüfter ohne PWM-Steuerung. 

Schließe das Lüfterkabel am FAN-Port an.

 .. image:: img/io_board_fan.png

Die beiden Pinreihen unter J9 sind Aktivierungspins für den Lüfter und dessen RGB-LED. Standardmäßig sind Jumper eingesetzt, sodass GPIO6 und GPIO5 den Ein/Aus-Zustand des Lüfters und der LED steuern. Wird dies nicht benötigt, können die Jumper entfernt werden, um GPIO6 bzw. GPIO5 freizugeben.

 .. image:: img/io_board_fan_j9.png

Du kannst den Betriebsmodus des RGB-Lüfters per Befehl festlegen. Die Modi bestimmen, bei welcher Temperatur der Lüfter aktiviert wird.

  Beispiel: Im Modus **1: Performance** läuft der Lüfter ab 50 °C.

  .. code-block:: shell

    sudo pironman5 -gm 3

  * **4: Quiet** – Aktiv ab 70 °C  
  * **3: Balanced** – Aktiv ab 67,5 °C  
  * **2: Cool** – Aktiv ab 60 °C  
  * **1: Performance** – Aktiv ab 50 °C  
  * **0: Always On** – Lüfter läuft dauerhaft

Wenn du den Steuerpin des Lüfters auf einen anderen GPIO legst, kannst du ihn mit folgendem Befehl anpassen:

.. code-block:: shell

  sudo pironman5 -gp 18


Power-Switch-Adapter
--------------------------------------

**Power-Taste hinzufügen**

* Der Raspberry Pi 5 verfügt über einen **J2**-Jumper, der sich zwischen dem RTC-Batterieanschluss und dem Rand der Platine befindet. Über diesen lässt sich eine externe Power-Taste anschließen, indem ein normalerweise offener Taster (NO) über die zwei Lötpunkte verbunden wird. Ein kurzer Druck simuliert den eingebauten Power-Button.

  .. image:: img/pi5_j2.jpg

* Der Pironman 5 Mini leitet den **J2**-Jumper über zwei Pogo-Pins zu einem externen Power-Button weiter.

  .. image:: img/power_switch_j2.jpeg

  .. image:: img/power_switch_j2_2.jpeg

* Dadurch lässt sich der Raspberry Pi 5 nun über die Power-Taste ein- und ausschalten.

  .. image:: img/pironman_button.JPG

**Power Cycling** 

Beim erstmaligen Einschalten deines Raspberry Pi 5 startet das Gerät automatisch und bootet in das Betriebssystem, ohne dass der Power-Button gedrückt werden muss.

Wenn das Raspberry Pi Desktop-System läuft, führt ein kurzer Druck auf den Power-Button einen sauberen Herunterfahrvorgang ein. Es erscheint ein Menü mit Optionen zum Herunterfahren, Neustarten oder Abmelden. Wird eine Option ausgewählt oder der Power-Button erneut gedrückt, wird der Shutdown-Prozess gestartet.

.. image:: img/button_shutdown.png

**Herunterfahren**

    * Bei Nutzung des **Raspberry Pi OS Desktop** kannst du den Power-Button zweimal kurz drücken, um das System herunterzufahren.
    * Bei Nutzung des **Raspberry Pi OS Lite** (ohne Desktop) genügt ein einmaliger Druck auf den Power-Button.
    * Für ein erzwungenes Abschalten halte den Power-Button gedrückt.


**Einschalten**

    * Wenn der Raspberry Pi heruntergefahren, aber weiterhin mit Strom versorgt ist, genügt ein kurzer Druck auf den Power-Button, um ihn wieder einzuschalten.

.. note::

    Wenn du ein System nutzt, das keine Unterstützung für den Power-Button bietet, kannst du den Button für 5 Sekunden gedrückt halten, um ein erzwungenes Abschalten durchzuführen. Ein kurzer Druck schaltet das Gerät dann wieder ein.




NVMe-Modul
-------------------------------------------


Der Pironman 5 Mini enthält ein integriertes PCIe-Adaptermodul für NVMe-SSDs. Es unterstützt vier Formfaktoren: 2230, 2242, 2260 und 2280 – alle passend für den M.2-M-Key-Slot.

.. image:: img/nvme_p.png


* **STA**: Status-LED
* **PWR**: Stromversorgungs-LED

  .. image:: img/nvme_led.png

* Das Modul wird über ein 16-poliges 0,5 mm Reverse-FFC-Kabel oder ein angepasstes FPC-Kabel (Flexible Printed Circuit) mit impedanzangepasstem Design verbunden.

  .. image:: img/nvme_pcie.png

* **FORCE ENABLE**: Die integrierte Stromversorgung wird durch ein Signal vom PCIe-Interface aktiviert. Nach dem Start des Raspberry Pi schaltet dieses Signal die 3,3 V-Stromversorgung ein. Falls ein System das Schaltsignal nicht unterstützt, kann durch Überbrücken von J2 FORCE ENABLE (zwei Lötpads) die 3,3 V-Stromversorgung dauerhaft aktiviert werden.

  .. image:: img/nvme_j2.png

**Zum SSD-Typ**

M.2-SSDs zeichnen sich durch ihre kompakte Bauform aus. Sie unterscheiden sich hauptsächlich durch ihre Anschlussart (Keying) und Schnittstelle:

* **M.2 SATA SSDs** – Verwenden die SATA-Schnittstelle, ähnlich wie 2,5"-SSDs, aber im M.2-Format. Die Geschwindigkeit ist durch SATA III auf ca. 600 MB/s begrenzt. Kompatibel mit B- und M-Key-Slots.
* **M.2 NVMe SSDs** – Nutzen das NVMe-Protokoll über PCIe-Lanes und bieten deutlich höhere Übertragungsraten. Ideal für Gaming, Videoschnitt und datenintensive Anwendungen. Sie benötigen in der Regel einen M-Key-Slot. Raspberry Pi 5 unterstützt PCIe 3.0 mit einer theoretischen Geschwindigkeit bis zu 3.500 MB/s.

M.2-SSDs gibt es mit B-Key, M-Key und B+M-Key. Letzterer kombiniert beide Steckertypen. Siehe Abbildung:

.. image:: img/ssd_key.png


Allgemein gilt: M.2 SATA SSDs sind B+M-keyed (passen in B- und M-Key-Slots), während M.2 NVMe SSDs (PCIe 3.0 x4) ausschließlich M-Keyed sind.

.. image:: img/ssd_model2.png

**Zur Länge**

M.2-Module gibt es in verschiedenen Längen und werden auch für WLAN, WWAN, Bluetooth, GPS und NFC verwendet.

Der Pironman 5 Mini unterstützt vier NVMe M.2 SSD-Größen (für PCIe Gen 2.0 / Gen 3.0): 2230, 2242, 2260 und 2280. Die Zahl 22 steht für die Breite in mm, die nachfolgenden Ziffern für die Länge. Längere Module bieten Platz für mehr NAND-Chips und damit mehr Speicherkapazität.


.. image:: img/m2_ssd_size.png
  :width: 600


1220RTC-Batteriehalter
---------------------------------

.. image:: img/battery_holder.png


Ein integrierter 1220RTC-Batteriehalter ermöglicht die einfache Nutzung einer RTC-Batterie. Er wird über ein SH1.0 2P-Reverse-Kabel mit dem RTC-Anschluss des Raspberry Pi verbunden.

Kompatibel mit CR1220 und ML1220 Batterien. Bei Verwendung einer ML1220-Batterie (wiederaufladbar) kann das Laden direkt über den Raspberry Pi aktiviert werden. Die CR1220 ist nicht wiederaufladbar.

**Trickle Charging aktivieren**

.. warning::

    Wenn du eine CR1220-Batterie verwendest, aktiviere kein Trickle Charging – dies kann die Batterie und das Board beschädigen.

Standardmäßig ist die Trickle-Charging-Funktion deaktiviert. Die aktuellen Spannungswerte können über folgende Dateien eingesehen werden:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Um das Trickle Charging zu aktivieren, füge ``rtc_bbat_vchg`` zur Datei ``/boot/firmware/config.txt`` hinzu: 

  * Öffne die Datei ``/boot/firmware/config.txt``.

    .. code-block:: shell

      sudo nano /boot/firmware/config.txt
      
* Füge ``rtc_bbat_vchg`` zur Datei ``/boot/firmware/config.txt`` hinzu.

    .. code-block:: shell

      dtparam=rtc_bbat_vchg=3000000

Nach dem Neustart zeigt das System:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Dies bestätigt, dass die Batterie nun im Trickle-Charging-Modus betrieben wird. Um diese Funktion zu deaktivieren, entferne einfach die ``dtparam``-Zeile aus der ``config.txt``.



Pin Header
--------------

.. image:: img/io_board_pin_header.png

Zwei rechtwinklige Header-Verbinder führen die GPIO-Pins des Raspberry Pi heraus. Beachte jedoch, dass IR-Empfänger, RGB-LED und Lüfter bestimmte Pins belegen. Entferne bei Bedarf die Jumper, um diese Pins anderweitig zu nutzen.

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 Mini
    - Raspberry Pi 5
  * - FAN (optional)
    - GPIO6
  * - FAN RGB (optional)
    - GPIO5
  * - RGB (optional)
    - GPIO10