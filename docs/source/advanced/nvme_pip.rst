.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Pi5 NVMe PIP
=================

Das Pi5 NVMe PIP (PCIe Peripheral Board), wie von der Raspberry Pi Foundation definiert, ist eine PCIe-Adapterplatine, die speziell für NVMe-Solid-State-Laufwerke entwickelt wurde. Sie unterstützt vier verschiedene Größen von NVMe-SSDs: 2230, 2242, 2260 und 2280, die alle in einen M.2 M-Key-Slot passen.

.. image:: img/nvme_pip.jpeg

* Die Platine wird über ein 16-poliges 0,5mm umgekehrtes FFC (Flexible Flat Cable) oder ein kundenspezifisches impedanzangepasstes FPC (Flexible Printed Circuit) Kabel verbunden.
* **STA**: Eine Status-LED-Anzeige.
* **PWR**: Eine Strom-LED-Anzeige.
* Die integrierte 3,3V-Stromversorgung kann bis zu 3A Ausgang unterstützen. Da die Raspberry Pi PCIe-Schnittstelle jedoch auf die Bereitstellung von 5V/1A Ausgang (entspricht 5W) begrenzt ist, kann zusätzliche Leistung für die Nutzung von 3,3V/3A über den J3-Anschluss von einer 5V-Quelle geliefert werden.

Über das Modell
---------------------------

M.2-SSDs sind für ihre kompakte Größe bekannt und kommen in verschiedenen Typen, die hauptsächlich durch ihre Keying (Kerben-Design am Stecker) und die verwendete Schnittstelle unterschieden werden. Hier sind die wichtigsten Typen:

* **M.2 SATA SSDs**: Diese nutzen die SATA-Schnittstelle, ähnlich wie 2,5-Zoll-SATA-SSDs, aber in der kleineren M.2-Form. Sie sind durch die SATA III-Höchstgeschwindigkeit von etwa 600 MB/s begrenzt. Diese SSDs sind mit M.2-Steckplätzen kompatibel, die für B- und M-Keys ausgelegt sind.
* **M.2 NVMe SSDs**: Diese SSDs nutzen das NVMe-Protokoll über PCIe-Lanes und sind erheblich schneller als M.2 SATA-SSDs. Sie eignen sich für Anwendungen, die hohe Lese-/Schreibgeschwindigkeiten erfordern, wie Gaming, Videobearbeitung und datenintensive Aufgaben. Diese SSDs benötigen typischerweise M-gekippte Steckplätze. Diese Laufwerke nutzen die PCIe (Peripheral Component Interconnect Express)-Schnittstelle mit verschiedenen Versionen wie 3.0, 4.0 und 5.0. Jede neue Version von PCIe verdoppelt effektiv die Datenübertragungsgeschwindigkeit ihres Vorgängers. Der Raspberry Pi 5 verwendet jedoch eine PCIe 3.0-Schnittstelle, die Übertragungsgeschwindigkeiten von bis zu 3.500 MB/s liefern kann.

M.2-SSDs gibt es in drei Key-Typen: B-Key, M-Key und B+M-Key. Später wurde der B+M-Key eingeführt, der die Funktionen des B-Keys und M-Keys kombiniert. Infolgedessen ersetzte er den eigenständigen B-Key. Bitte beachten Sie das folgende Bild.

.. image:: img/ssd_key.png

Im Allgemeinen sind M.2 SATA-SSDs B+M-gekippte (können in Steckplätze für B- und M-gekippte Module passen), während M.2 NVMe-SSDs für PCIe 3.0 x4-Lane M-gekippte sind.

.. image:: img/ssd_model2.png

Über die Länge
-----------------------

M.2-Module gibt es in verschiedenen Größen und können auch für Wi-Fi, WWAN, Bluetooth, GPS und NFC genutzt werden.

Pironman 5 unterstützt vier (PCIE2.0 / PCIE 3.0) NVMe M.2-SSD-Größen basierend auf ihren Bezeichnungen: 2230, 2242, 2260 und 2280. Die "22" ist die Breite in Millimetern (mm) und die beiden folgenden Zahlen die Länge. Je länger das Laufwerk, desto mehr NAND-Flash-Chips können montiert werden; daher mehr Kapazität.

.. image:: img/m2_ssd_size.png
  :width: 600
