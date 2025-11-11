.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum der Community beitreten?**

    - **Expertensupport**: Erhalte Hilfe bei technischen Problemen und nach dem Kauf – durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitig Einblicke in neue Produkte und Ankündigungen.
    - **Sonderrabatte**: Nutze exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_install_to_nvme_ubuntu:

Installation des Betriebssystems auf einer NVMe-SSD
=======================================================

Wenn du eine NVMe-SSD und einen Adapter hast, um sie zur Systeminstallation mit deinem Computer zu verbinden, kannst du die folgende Anleitung für eine schnelle Einrichtung nutzen.

**Benötigte Komponenten**

* Ein Computer oder Laptop
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Micro SD-Karte und Kartenleser

1. Bootloader aktualisieren
----------------------------------

Zuerst musst du den Bootloader des Raspberry Pi 5 aktualisieren, damit er von einer NVMe-SSD booten kann – noch vor USB und SD-Karte.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Für diesen Schritt wird empfohlen, eine separate Micro SD-Karte zu verwenden. Schreibe zunächst den Bootloader auf diese Micro SD-Karte und stecke sie dann direkt in den Raspberry Pi, um das Booten von einem NVMe-Gerät zu aktivieren.

    Alternativ kannst du den Bootloader direkt auf die NVMe-SSD schreiben, diese anschließend in den Raspberry Pi einsetzen, um die Boot-Methode zu ändern. Danach kannst du die SSD mit dem Computer verbinden, das Betriebssystem installieren und sie schließlich wieder in den Raspberry Pi einsetzen.

#. Stecke deine Ersatz-Micro-SD-Karte oder NVMe-SSD mit einem Kartenleser in deinen Computer oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle **Raspberry Pi 5** aus der Dropdown-Liste.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Klicke im Tab **Betriebssystem** nach unten und wähle **Sonstige Dienstprogramme**.

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. Wähle **Bootloader (Pi 5 Familie)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Wähle **NVMe/USB-Boot**, damit der Raspberry Pi 5 zuerst von NVMe, dann USB und zuletzt von der SD-Karte bootet.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Wähle unter **Speicher** das passende Speichermedium für die Installation.

   .. note::

      Stelle sicher, dass du das richtige Speichermedium auswählst. Um Verwechslungen zu vermeiden, entferne ggf. andere angeschlossene Speichergeräte.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Klicke nun auf **NEXT**. Falls sich auf dem Laufwerk bereits Daten befinden, sichere sie zuvor. Klicke auf **Yes**, wenn kein Backup nötig ist.

   .. image:: img/os_continue.png
      :width: 90%


#. Kurz darauf erscheint die Meldung, dass **NVMe/USB-Boot** auf das Speichermedium geschrieben wurde.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Jetzt kannst du die Micro SD-Karte oder NVMe-SSD in den Raspberry Pi einsetzen. Nach dem Einschalten mit einem USB-C-Netzteil wird der Bootloader von der Micro SD-Karte oder NVMe-SSD in den EEPROM des Raspberry Pi geschrieben.

.. note::

    Danach bootet der Raspberry Pi standardmäßig von NVMe, danach USB und zuletzt von der SD-Karte.

    Schalte den Raspberry Pi danach aus und entferne die Micro SD-Karte oder NVMe-SSD.


2. Betriebssystem auf NVMe-SSD installieren
-------------------------------------------------

Nun kannst du das Betriebssystem auf deiner NVMe-SSD installieren.

**Schritte**

#. Gehe zunächst zur |link_batocera_download| Seite, wähle **Raspberry Pi 5 B** und starte den Download.

   .. image:: img/batocera_download.png
      :width: 90%


#. Entpacke die heruntergeladene Datei ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Stecke deine SSD oder SD-Karte über einen Kartenleser in den Computer oder Laptop.

#. Öffne den |link_rpi_imager| und klicke auf den Tab **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scrolle ganz nach unten und wähle **Benutzerdefiniert verwenden**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. Wähle die entpackte Systemdatei ``batocera-xxx-xx-xxxxxxxx.img`` aus und klicke auf **Öffnen**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Wähle unter **Speicher** das Zielgerät für die Installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. Klicke auf **WEITER**. Wenn sich bereits Daten auf dem Laufwerk befinden, sichere diese. Klicke auf **Yes**, um fortzufahren, wenn kein Backup erforderlich ist.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Sobald die Meldung "Schreiben erfolgreich" erscheint, wurde das Image erfolgreich geschrieben und überprüft. Dein Raspberry Pi ist jetzt bereit, von der NVMe-SSD zu booten!
