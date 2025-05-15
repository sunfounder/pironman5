.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum mitmachen?**

    - **Experten-Support**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Profitiere von Sonderangeboten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns Neues zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _install_to_nvme_rpi_mini:

Installation des Betriebssystems auf einer NVMe-SSD
========================================================
Wenn du eine NVMe-SSD verwendest und einen Adapter besitzt, um diese für die Systeminstallation mit deinem Computer zu verbinden, kannst du das folgende Tutorial für eine schnelle Einrichtung nutzen.

**Erforderliche Komponenten**

* Ein Computer oder Laptop
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Eine Micro-SD-Karte und ein Kartenleser

.. _update_bootloader_mini:

1. Bootloader aktualisieren
--------------------------------

Zunächst musst du den Bootloader des Raspberry Pi 5 aktualisieren, sodass er zuerst von der NVMe-SSD, dann per USB und zuletzt von der SD-Karte startet.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Es wird empfohlen, für diesen Schritt eine Ersatz-Micro-SD-Karte zu verwenden. Schreibe den Bootloader zuerst auf diese Karte und stecke sie dann in den Raspberry Pi, um das Booten von NVMe zu ermöglichen.
    
    Alternativ kannst du den Bootloader auch direkt auf dein NVMe-Laufwerk schreiben, es dann in den Raspberry Pi einlegen, um die Bootreihenfolge zu ändern. Danach installierst du das Betriebssystem über den Computer und setzt das Laufwerk anschließend zurück in den Raspberry Pi.

#. Stecke die Ersatz-Micro-SD-Karte oder NVMe-SSD über einen Kartenleser in deinen Computer oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle **Raspberry Pi 5** aus der Dropdown-Liste.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Scrolle im Tab **Operating System** nach unten und wähle **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Wähle **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Wähle **NVMe/USB Boot**, um das Booten von NVMe vor USB und SD-Karte zu aktivieren.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Wähle im Tab **Storage** das passende Speichermedium für die Installation aus.

   .. note::

      Stelle sicher, dass du das richtige Gerät auswählst. Um Verwechslungen zu vermeiden, entferne andere angeschlossene Speichermedien.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Klicke nun auf **NEXT**. Wenn das Speichermedium Daten enthält, sichere sie vorab. Klicke auf **Yes**, wenn keine Sicherung erforderlich ist.

   .. image:: img/os_continue.png
      :width: 90%


#. Kurz darauf erscheint die Meldung, dass **NVMe/USB Boot** erfolgreich auf das Speichermedium geschrieben wurde.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Nun kannst du die Micro-SD-Karte oder die NVMe-SSD in den Raspberry Pi einsetzen. Nach dem Einschalten über den USB-C-Anschluss wird der Bootloader aus dem Medium in den EEPROM des Raspberry Pi geschrieben.

.. note::

    Danach wird der Raspberry Pi in folgender Reihenfolge booten: NVMe → USB → SD-Karte. 
    
    Schalte den Raspberry Pi aus und entferne das Installationsmedium.


2. Betriebssystem auf NVMe-SSD installieren
----------------------------------------------

Jetzt kannst du das Betriebssystem auf der NVMe-SSD installieren.


#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle das Modell **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Wähle im Tab **Operating System** die empfohlene Version aus.

   .. image:: img/os_choose_os.png
      :width: 90%


#. Wähle im Bereich **Storage** das richtige Zielmedium.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Klicke auf **NEXT** und anschließend auf **EDIT SETTINGS**, um die OS-Einstellungen individuell anzupassen.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Lege einen **Hostname** für deinen Raspberry Pi fest. Dies ist der Netzwerkname, unter dem dein Gerät erreichbar ist (z. B. ``<hostname>.local`` oder ``<hostname>.lan``).

     .. image:: img/os_set_hostname.png

   * Richte einen **Benutzernamen** und ein **Passwort** für das Admin-Konto ein. Ein eindeutiger Login ist entscheidend für die Systemsicherheit.

     .. image:: img/os_set_username.png

   * Konfiguriere das WLAN durch Eingabe von **SSID** und **Passwort** deines Netzwerks.

     .. note::

       Stelle das ``Wireless LAN country`` auf den zweibuchstabigen `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ deiner Region ein.

     .. image:: img/os_set_wifi.png

   * Aktiviere SSH im Tab Services, um den Raspberry Pi fernzusteuern.

     * Für **Passwortauthentifizierung** verwende den Benutzernamen und das Passwort aus dem Tab **General**.
     * Für Public-Key-Authentifizierung wähle „Nur Public-Key-Authentifizierung zulassen“. Falls kein Schlüssel vorhanden ist, kannst du über „SSH-Keygen ausführen“ ein neues Schlüsselpaar erzeugen.

     .. image:: img/os_enable_ssh.png

   * Im Menü **Options** kannst du definieren, was der Imager nach dem Schreiben tun soll – z. B. Ton abspielen, Medium auswerfen, Telemetrie aktivieren.

     .. image:: img/os_options.png

#. Wenn du die Anpassungen abgeschlossen hast, klicke auf **Save**, anschließend auf **Yes**, um sie beim Schreiben anzuwenden.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Wenn sich noch Daten auf der NVMe-SSD befinden, sichere diese vorher. Klicke auf **Yes**, um fortzufahren, falls keine Sicherung nötig ist.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Sobald die Meldung „Write Successful“ erscheint, wurde das System erfolgreich geschrieben und überprüft. Du kannst nun deinen Raspberry Pi direkt von der NVMe-SSD starten!

   .. image:: img/nvme_install_finish.png
      :width: 90%