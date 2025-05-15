.. note:: 

    Hallo und herzlich willkommen in der SunFounder Facebook-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenhilfe**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Einblicke**: Erhalte frühzeitige Informationen über neue Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen & Verlosungen**: Nimm an Aktionen und Gewinnspielen rund um Feiertage teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _install_to_nvme_ubuntu_mini:

Betriebssystem auf einer NVMe-SSD installieren
===============================================

Wenn du eine NVMe-SSD verwendest und über einen Adapter verfügst, um sie mit deinem Computer zu verbinden, kannst du mit dem folgenden Tutorial eine schnelle Installation durchführen.

**Benötigte Komponenten**

* Ein Computer
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Eine Micro-SD-Karte und ein Kartenleser

.. _update_bootloader_mini:

1. Bootloader aktualisieren
------------------------------

Zuerst musst du den Bootloader des Raspberry Pi 5 aktualisieren, damit dieser zuerst von NVMe, dann über USB und zuletzt von der SD-Karte startet.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    In diesem Schritt wird empfohlen, eine Ersatz-Micro-SD-Karte zu verwenden. Schreibe den Bootloader zunächst auf diese SD-Karte und stecke sie dann sofort in den Raspberry Pi, um den Start von NVMe zu ermöglichen.

    Alternativ kannst du den Bootloader direkt auf dein NVMe-Gerät schreiben, dieses dann in den Raspberry Pi einlegen, um die Startreihenfolge zu ändern. Anschließend verbindest du die NVMe-SSD mit einem Computer zur Installation des Betriebssystems und steckst sie nach Abschluss der Installation wieder in den Raspberry Pi ein.

#. Setze deine Ersatz-Micro-SD-Karte oder NVMe-SSD mit einem Kartenleser in deinen Computer ein.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle aus der Liste das Modell **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Klicke im Reiter **Operating System** nach unten und wähle **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. Wähle **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Wähle **NVMe/USB Boot**, um den Raspberry Pi 5 so zu konfigurieren, dass er zuerst von NVMe startet.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Wähle unter **Speicher** das passende Gerät für die Installation.

   .. note::

      Achte darauf, das richtige Speichergerät auszuwählen. Um Verwechslungen zu vermeiden, entferne ggf. andere Speichermedien.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Klicke auf **WEITER**. Wenn sich bereits Daten auf dem Speicher befinden, sichere sie vorher. Klicke auf **Ja**, wenn du fortfahren möchtest.

   .. image:: img/os_continue.png
      :width: 90%


#. Nach kurzer Zeit erhältst du die Meldung, dass **NVMe/USB Boot** erfolgreich geschrieben wurde.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Nun kannst du die Micro-SD-Karte oder die NVMe-SSD in den Raspberry Pi einsetzen. Sobald du ihn mit dem Typ-C-Netzteil einschaltest, wird der Bootloader vom eingelegten Medium ins EEPROM des Raspberry Pi geschrieben.

.. note::

    Danach bootet der Raspberry Pi vorrangig von NVMe, danach von USB und zuletzt von der SD-Karte.

    Schalte den Raspberry Pi aus und entferne die Micro-SD-Karte oder NVMe-SSD.


2. Betriebssystem auf NVMe-SSD installieren
-----------------------------------------------

Jetzt kannst du das Betriebssystem auf deiner NVMe-SSD installieren.

**Schritte**

#. Besuche die Seite |link_batocera_download|, wähle **Raspberry Pi 5 B** und lade das System herunter.

   .. image:: img/batocera_download.png
      :width: 90%



#. Entpacke die heruntergeladene Datei ``batocera-xxx-xx-xxxxxxxx.img.gz``.


#. Setze deine SD-Karte mit einem Kartenleser in den Computer ein.


#. Öffne den |link_rpi_imager| und klicke auf den Reiter **Betriebssystem**.


   .. image:: img/os_choose_os.png
      :width: 90%

#. Scrolle nach unten und wähle **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. Wähle die entpackte Datei ``batocera-xxx-xx-xxxxxxxx.img`` und klicke auf **Öffnen**.


   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Wähle unter **Speicher** das passende Speichergerät für die Installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. Klicke auf **WEITER**. Wenn sich bereits Daten auf dem Speicher befinden, sichere sie vorher. Klicke auf **Ja**, wenn keine Sicherung nötig ist.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Sobald die Meldung Write Successful erscheint, wurde das Image erfolgreich geschrieben und überprüft. Jetzt kannst du deinen Raspberry Pi direkt von der NVMe-SSD starten!
