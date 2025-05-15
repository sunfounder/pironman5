.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Entdecken Sie gemeinsam mit Gleichgesinnten die faszinierende Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lassen Sie sich bei Problemen und technischen Herausforderungen nach dem Kauf von unserer Community und unserem Team unterstützen.
    - **Lernen & Teilen**: Profitieren Sie vom Austausch über Tipps, Tricks und Tutorials, um Ihre Kenntnisse zu vertiefen.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugriff auf neue Produktankündigungen und Einblicke.
    - **Sonderrabatte**: Sichern Sie sich exklusive Rabatte auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nehmen Sie an spannenden Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _set_up_pironman5:

4. Software einrichten oder installieren
================================================

Nachdem das System entweder auf die Micro-SD-Karte oder die NVMe-SSD geschrieben wurde, setzen Sie das Speichermedium in den entsprechenden Slot des Pironman 5 ein. Drücken Sie anschließend die Einschalttaste, um das Gerät zu starten.

Nach dem Einschalten leuchten verschiedene Status-LEDs auf. OLED-Display, RGB-LEDs und die seitlichen RGB-Lüfter funktionieren zu diesem Zeitpunkt jedoch noch nicht, da sie zunächst konfiguriert werden müssen. Sollte das Display vorübergehend eine fehlerhafte Anzeige zeigen, ignorieren Sie dies – das Problem wird nach der Konfiguration behoben.

Bevor Sie mit der Einrichtung fortfahren, müssen Sie Ihren Raspberry Pi starten und sich anmelden. Wenn Sie nicht wissen, wie Sie sich anmelden können, besuchen Sie die offizielle Raspberry Pi-Webseite: |link_rpi_get_start|.

Wählen Sie anschließend das passende Konfigurations-Tutorial entsprechend Ihrem System aus.

.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_batocera


**Über den Einschaltknopf**

Der Einschaltknopf entspricht dem des Raspberry Pi 5 und erfüllt die gleiche Funktionalität.

* **Herunterfahren**

    * Beim System Raspberry Pi **Bookworm Desktop** können Sie durch zweimaliges schnelles Drücken der Einschalttaste den Shutdown-Vorgang einleiten.
    * Beim System Raspberry Pi **Bookworm Lite** genügt ein einmaliges Drücken der Taste, um das Gerät herunterzufahren.
    * Durch langes Drücken führen Sie einen erzwungenen Hard-Shutdown durch.

* **Einschalten**

    * Wenn das Raspberry Pi-Board heruntergefahren, aber noch mit Strom versorgt ist, drücken Sie kurz die Taste, um es wieder einzuschalten.

* Falls Ihr System die Herunterfahren-Funktion nicht unterstützt, halten Sie die Taste für 5 Sekunden gedrückt, um einen Hard-Shutdown zu erzwingen. Zum Einschalten genügt dann ein kurzes Drücken der Taste.
