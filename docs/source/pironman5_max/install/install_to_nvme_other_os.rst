.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum der Community beitreten?**

    - **Expertensupport**: Erhalte Unterstützung bei technischen Problemen und Herausforderungen nach dem Kauf – durch unsere Community und unser Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um dein Wissen zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_install_to_nvme_home_bridge:

Installation des Betriebssystems auf einer NVMe-SSD
=======================================================

Wenn du eine NVMe-SSD verwendest und einen Adapter hast, um sie zur Systeminstallation mit deinem Computer zu verbinden, kannst du die folgende Anleitung für eine schnelle Installation nutzen.

**Benötigte Komponenten**

* Ein Computer
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Micro SD-Karte und Kartenleser

.. _update_bootloader_max:

1. Bootloader aktualisieren
----------------------------------

Zuerst musst du den Bootloader des Raspberry Pi 5 aktualisieren, damit dieser zuerst von NVMe, dann USB und schließlich SD-Karte bootet.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Es wird empfohlen, in diesem Schritt eine separate Micro SD-Karte zu verwenden. Schreibe zunächst den Bootloader auf diese Karte und stecke sie dann sofort in den Raspberry Pi, um das Booten von einem NVMe-Gerät zu aktivieren.
    
    Alternativ kannst du den Bootloader auch direkt auf dein NVMe-Gerät schreiben, es dann in den Raspberry Pi einlegen, um die Bootmethode zu ändern. Danach verbindest du die NVMe-SSD wieder mit dem Computer, installierst das Betriebssystem und setzt sie anschließend erneut in den Raspberry Pi ein.

#. Stecke deine Micro SD-Karte oder NVMe-SSD über einen Kartenleser in den Computer oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle **Raspberry Pi 5** aus.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. Klicke im Reiter **Betriebssystem**, scrolle nach unten und wähle **Verschiedene Dienstprogramme**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Wähle **Bootloader (Pi 5 Familie)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Wähle **NVMe/USB-Boot**, damit der Raspberry Pi zuerst von NVMe, dann USB und zuletzt SD-Karte bootet.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Wähle im Reiter **Speicher** das entsprechende Laufwerk aus.

   .. note::

      Stelle sicher, dass du das richtige Laufwerk auswählst. Um Verwechslungen zu vermeiden, entferne bei Bedarf andere angeschlossene Geräte.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Klicke auf **WEITER**. Falls das Laufwerk Daten enthält, sichere diese vor dem Fortfahren. Klicke auf **Ja**, wenn kein Backup benötigt wird.

   .. image:: img/os_continue.png
      :width: 90%

#. Kurz darauf erhältst du die Bestätigung, dass **NVMe/USB Boot** auf dein Speichermedium geschrieben wurde.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Jetzt kannst du die Micro SD-Karte oder NVMe-SSD in den Raspberry Pi einlegen. Nach dem Einschalten mit einem USB-C-Netzteil wird der Bootloader vom Medium in den EEPROM des Raspberry Pi geschrieben.

.. note::

   Danach bootet der Raspberry Pi zuerst von NVMe, dann USB und zuletzt von der SD-Karte. 
    
   Schalte den Raspberry Pi aus und entferne die Micro SD-Karte oder NVMe-SSD.


2. Betriebssystem auf NVMe-SSD installieren
-----------------------------------------------

Nun kannst du das Betriebssystem auf deiner NVMe-SSD installieren.

**Schritte**

#. Stecke die SD-Karte über einen Kartenleser in deinen Computer oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi-Gerät** und wähle **Raspberry Pi 5** aus.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Klicke auf den Reiter **Betriebssystem**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scrolle nach unten und wähle dein gewünschtes Betriebssystem aus.

   .. note::

      * Für **Ubuntu** wähle unter **Andere Mehrzweckbetriebssysteme** -> **Ubuntu** und dann entweder **Ubuntu Desktop 24.04 LTS (64 Bit)** oder **Ubuntu Server 24.04 LTS (64 Bit)**.
      * Für **Kali Linux**, **Home Assistant** und **Homebridge** gehe zu **Andere Spezialbetriebssysteme** und wähle das entsprechende System aus.

   .. image:: img/os_other_os.png
      :width: 90%

#. Wähle im Reiter **Speicher** dein Ziel-Laufwerk aus.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Klicke auf **WEITER**.

   .. note::

      * Für Systeme, die nicht vorab konfiguriert werden können, wirst du nach dem Klick gefragt, ob die Daten überschrieben werden dürfen. Bestätige mit **Ja**, wenn du bereits ein Backup gemacht hast.

      * Bei Systemen mit konfigurierbaren Hostnamen, WLAN und SSH erscheint ein Fenster zur Eingabe benutzerdefinierter Einstellungen. Du kannst mit **Ja** bestätigen oder Änderungen vornehmen.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Definiere einen **Hostname** für deinen Raspberry Pi. Damit kannst du ihn im Netzwerk unter ``<hostname>.local`` oder ``<hostname>.lan`` erreichen.

     .. image:: img/os_set_hostname.png

   * Erstelle einen **Benutzernamen** und ein **Passwort** für das Administrator-Konto deines Raspberry Pi. Ein individuelles Passwort ist essenziell, da es kein Standardpasswort gibt.

     .. image:: img/os_set_username.png

   * Konfiguriere dein WLAN, indem du **SSID** und **Passwort** eingibst.

     .. note::

        Gib als ``Wireless LAN country`` den zweistelligen Ländercode gemäß `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ ein.

     .. image:: img/os_set_wifi.png
         
   * Aktiviere **SSH**, um dich später per Fernzugriff mit dem Raspberry Pi zu verbinden.

     * Für **Passwort-Authentifizierung** verwende die Angaben aus dem Reiter Allgemein.
     * Für Public-Key-Authentifizierung wähle „Nur Public-Key zulassen“. Falls kein RSA-Schlüssel vorhanden ist, kann über „SSH-Keygen ausführen“ ein neuer erstellt werden.

     .. image:: img/os_enable_ssh.png

   * Im Menü **Optionen** kannst du z. B. festlegen, ob nach dem Schreiben ein Ton abgespielt oder das Medium ausgeworfen werden soll.

     .. image:: img/os_options.png



#. Klicke auf **Speichern**, um die benutzerdefinierten Einstellungen zu sichern. Danach auf **Ja**, um sie beim Schreiben anzuwenden.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Falls sich Daten auf der NVMe-SSD befinden, sichere diese. Klicke auf **Ja**, um fortzufahren, wenn kein Backup nötig ist.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Sobald die Meldung **"Schreiben erfolgreich"** erscheint, ist das Image erfolgreich geschrieben und überprüft. Der Raspberry Pi kann nun direkt von der NVMe-SSD booten!
