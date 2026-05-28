.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Pi5 NVMe PIP
=================

Das Pi5 NVMe PIP (PCIe Peripheral Board), wie von der Raspberry Pi Foundation definiert, ist ein PCIe-Adapterboard, das speziell für NVMe-SSDs entwickelt wurde. Es unterstützt vier verschiedene Größen von NVMe-SSDs: 2230, 2242, 2260 und 2280, die alle in einen M.2 M-Key-Steckplatz passen.

.. image:: img/nvme_pip.png

* Das Board wird über ein 16P 0,5mm Reverse FFC (Flexible Flat Cable) oder ein maßgeschneidertes impedanzangepasstes FPC (Flexible Printed Circuit) Kabel angeschlossen.
* **STA**: Eine Status-LED-Anzeige.
* **PWR**: Eine Leistungs-LED-Anzeige.
* Die integrierte 3,3V-Stromversorgung kann bis zu 3A Ausgang unterstützen. Da die Raspberry Pi PCIe-Schnittstelle jedoch nur 5V/1A Ausgang liefern kann (entspricht 5W), kann zusätzliche Leistung für 3,3V/3A über den J3-Anschluss von einer 5V-Quelle bereitgestellt werden.
* **FORCE ENABLE**: Die integrierte Stromversorgung wird durch das Schaltsignal der PCIe-Schnittstelle aktiviert. Nach dem Einschalten des Raspberry Pi sendet dieser ein Signal, um die 3,3V-Stromversorgung einzuschalten. Wenn einige Systeme das Schaltsignal nicht unterstützen oder aus anderen Gründen, können Sie J4 FORCE ENABLE durch Löten eines Drahtes zwischen den beiden Pads kurzschließen, um die integrierte 3,3V-Stromversorgung zu aktivieren und die NVMe mit Strom zu versorgen.

Über das Modell
---------------------------

M.2-SSDs, bekannt für ihre kompakte Größe, gibt es in verschiedenen Typen, die sich hauptsächlich durch ihre Keying (Kerbendesign am Stecker) und die Schnittstelle unterscheiden, die sie verwenden. Hier sind die Haupttypen:

* **M.2 SATA SSDs**: Diese verwenden die SATA-Schnittstelle, ähnlich wie 2,5-Zoll-SATA-SSDs, jedoch im kleineren M.2-Formfaktor. Sie sind auf die maximalen SATA III-Geschwindigkeiten von etwa 600 MB/s begrenzt. Diese SSDs sind kompatibel mit M.2-Steckplätzen, die für B- und M-Key ausgelegt sind.
* **M.2 NVMe SSDs**: Diese SSDs verwenden das NVMe-Protokoll über PCIe-Lanes und sind wesentlich schneller als M.2 SATA SSDs. Sie eignen sich für Anwendungen, die hohe Lese-/Schreibgeschwindigkeiten erfordern, wie z. B. Gaming, Videobearbeitung und datenintensive Aufgaben. Diese SSDs benötigen in der Regel M-Key-Steckplätze. Diese Laufwerke nutzen die PCIe-Schnittstelle (Peripheral Component Interconnect Express) in verschiedenen Versionen wie 3.0, 4.0 und 5.0. Jede neue Version von PCIe verdoppelt effektiv die Datenübertragungsgeschwindigkeit ihres Vorgängers. Der Raspberry Pi 5 verwendet jedoch eine PCIe 3.0-Schnittstelle, die Übertragungsgeschwindigkeiten von bis zu 3.500 MB/s ermöglicht.

M.2-SSDs gibt es in drei Schlüsseltypen: B-Key, M-Key und B+M-Key. Später wurde jedoch der B+M-Key eingeführt, der die Funktionen des B-Key und des M-Key kombiniert. Dadurch ersetzte er den eigenständigen B-Key. Siehe das Bild unten.

.. image:: img/ssd_key.png

Im Allgemeinen sind M.2 SATA-SSDs B+M-Keyed (sie passen in Steckplätze für B-Keyed und M-Keyed-Module), während M.2 NVMe-SSDs für PCIe 3.0 x4-Lanes M-Keyed sind.

.. image:: img/ssd_model2.png

Über die Länge
-----------------------

M.2-Module sind in verschiedenen Größen erhältlich und können auch für Wi-Fi, WWAN, Bluetooth, GPS und NFC verwendet werden.

Der Pironman 5 unterstützt vier (PCIe Gen 2.0 / PCIe Gen 3.0) NVMe M.2 SSD-Größen basierend auf ihren Bezeichnungen: 2230, 2242, 2260 und 2280. Die "22" ist die Breite in Millimetern (mm), und die beiden folgenden Zahlen sind die Länge. Je länger das Laufwerk, desto mehr NAND-Flash-Chips können montiert werden; daher mehr Kapazität.

.. image:: img/m2_ssd_size.png
  :width: 600

