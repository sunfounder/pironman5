.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_install_to_nvme_rpi:

Installation des Betriebssystems auf einer NVMe-SSD
======================================================

Wenn du eine NVMe-SSD verwendest und über einen Adapter verfügst, um sie mit deinem Computer zur Installation zu verbinden, kannst du das folgende Tutorial für eine schnelle Einrichtung nutzen.

**Erforderliche Komponenten**

* Ein PC oder Laptop
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Eine Micro-SD-Karte und ein Kartenleser

.. _max_update_bootloader:

1. Bootloader aktualisieren
----------------------------

Zuerst musst du den Bootloader des Raspberry Pi 5 aktualisieren, damit er zuerst von NVMe, dann USB und zuletzt von der SD-Karte bootet.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Es wird empfohlen, eine Ersatz-Micro-SD-Karte zu verwenden. Schreibe zuerst den Bootloader auf diese SD-Karte und stecke sie dann direkt in den Raspberry Pi, um das Booten von einem NVMe-Gerät zu aktivieren.
    
    Alternativ kannst du den Bootloader direkt auf das NVMe-Gerät schreiben, dieses in den Raspberry Pi einsetzen, um die Bootreihenfolge zu ändern, anschließend das Betriebssystem installieren und die SSD danach wieder einsetzen.

#. Stecke die Micro-SD-Karte oder NVMe-SSD mit einem Lesegerät in deinen Computer.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi-Gerät** und wähle **Raspberry Pi 5** aus der Liste.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Scrolle im Reiter **Betriebssystem** nach unten und wähle **Verschiedene Dienstprogramme**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Wähle **Bootloader (Pi 5 Familie)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Wähle **NVMe/USB-Boot**, damit der Raspberry Pi 5 zuerst von NVMe bootet, dann USB und zuletzt von der SD-Karte.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Wähle unter **Speicher** das richtige Zielgerät für die Installation.

   .. note::

      Stelle sicher, dass du das richtige Gerät auswählst. Trenne andere angeschlossene Geräte zur Sicherheit.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Klicke auf **WEITER**. Wenn das Gerät Daten enthält, sichere diese vorher. Klicke auf **Ja**, wenn kein Backup erforderlich ist.

   .. image:: img/os_continue.png
      :width: 90%


#. Kurz darauf wirst du informiert, dass **NVMe/USB-Boot** erfolgreich geschrieben wurde.

   .. image:: img/nvme_boot_finish.png
      :width: 90%

#. Setze nun die Micro-SD-Karte oder NVMe-SSD in deinen Raspberry Pi ein. Nach dem Einschalten wird der Bootloader in den EEPROM des Raspberry Pi geschrieben.

.. note::

    Danach wird der Raspberry Pi von NVMe booten, dann von USB und schließlich von der SD-Karte.
    
    Schalte den Raspberry Pi aus und entferne die Micro-SD-Karte oder NVMe-SSD.


2. Installation des Betriebssystems auf die NVMe-SSD
-----------------------------------------------------

Jetzt kannst du das Betriebssystem auf deiner NVMe-SSD installieren.


#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi-Gerät** und wähle **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Wähle unter **Betriebssystem** die empfohlene OS-Version aus.

   .. image:: img/os_choose_os.png
      :width: 90%


#. Wähle unter **Speicher** das Zielgerät (deine NVMe-SSD).

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Klicke auf **WEITER** und dann auf **EINSTELLUNGEN BEARBEITEN**, um dein OS anzupassen.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Vergib einen **Hostname** für deinen Raspberry Pi. Dies ist der Netzwerkname, über den du deinen Pi z. B. unter ``<hostname>.local`` erreichst.

     .. image:: img/os_set_hostname.png

   * Erstelle einen **Benutzernamen** und ein **Passwort** für das Administrator-Konto.

     .. image:: img/os_set_username.png

   * Konfiguriere WLAN mit **SSID** und **Passwort**.

     .. note::

        Gib das Land mit dem entsprechenden `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ an.

     .. image:: img/os_set_wifi.png

   * Aktiviere SSH, um Fernzugriff zu ermöglichen.

     * Für **Passwort-Authentifizierung** nutze Benutzername und Passwort aus dem Allgemein-Reiter.
     * Für Public-Key-Authentifizierung wähle "Nur Public-Key zulassen". Falls kein RSA-Schlüssel vorhanden ist, generiere einen mit **SSH-Keygen ausführen**.

     .. image:: img/os_enable_ssh.png

   * Über **Optionen** kannst du konfigurieren, ob z. B. ein Ton beim Abschluss gespielt oder das Medium ausgeworfen werden soll.

     .. image:: img/os_options.png

#. Klicke auf **Speichern**, um deine Einstellungen zu sichern, und anschließend auf **Ja**, um mit dem Schreiben des Images zu beginnen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Wenn auf der NVMe-SSD bereits Daten vorhanden sind, sichere sie vorher. Klicke auf **Ja**, um fortzufahren, wenn kein Backup nötig ist.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Sobald die Meldung „Schreiben erfolgreich“ erscheint, wurde das Image vollständig geschrieben und überprüft. Dein Raspberry Pi ist jetzt bereit, von der NVMe-SSD zu booten!

   .. image:: img/nvme_install_finish.png
      :width: 90%

