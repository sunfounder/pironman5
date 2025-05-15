.. note:: 

    Hallo und herzlich willkommen in der SunFounder Facebook-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitig Informationen zu neuen Produkten und erste Einblicke.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen & Verlosungen**: Nimm an saisonalen Gewinnspielen und Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _install_to_nvme_home_bridge_mini:

Installation des Betriebssystems auf einer NVMe-SSD
=========================================================

Wenn du eine NVMe-SSD verwendest und einen Adapter hast, um sie mit deinem Computer zu verbinden, kannst du das folgende Tutorial für eine schnelle Installation nutzen.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Erforderliche Komponenten**

* Ein PC oder Laptop
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Eine Micro-SD-Karte und ein Kartenleser

.. _update_bootloader_mini:

1. Bootloader aktualisieren
-------------------------------

Zunächst musst du den Bootloader deines Raspberry Pi 5 aktualisieren, damit er zuerst von der NVMe-SSD, danach über USB und zuletzt von der SD-Karte startet.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Verwende in diesem Schritt idealerweise eine Ersatz-Micro-SD-Karte. Schreibe den Bootloader auf diese SD-Karte und stecke sie sofort in den Raspberry Pi, um den Start von NVMe zu ermöglichen.

    Alternativ kannst du den Bootloader direkt auf die NVMe-SSD schreiben, diese dann in den Raspberry Pi einsetzen, um den Bootmodus zu ändern. Anschließend kannst du das Betriebssystem über deinen Computer installieren und die SSD danach wieder in den Raspberry Pi einsetzen.

#. Setze die Micro-SD-Karte oder NVMe-SSD über einen Kartenleser in deinen PC oder Laptop ein.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi-Gerät** und wähle **Raspberry Pi 5** aus der Dropdown-Liste.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. Klicke im Reiter **Betriebssystem** nach unten und wähle **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Wähle **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Wähle **NVMe/USB Boot**, um den Raspberry Pi 5 so zu konfigurieren, dass er von NVMe bootet, bevor USB oder SD-Karte geprüft werden.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Wähle im Bereich **Speicher** das richtige Gerät für die Installation aus.

   .. note::

      Achte darauf, das korrekte Speichermedium auszuwählen. Trenne ggf. andere Geräte, um Verwechslungen zu vermeiden.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Klicke nun auf **WEITER**. Wenn das gewählte Laufwerk Daten enthält, sichere diese vorher. Fahre mit **Ja** fort, wenn keine Sicherung nötig ist.

   .. image:: img/os_continue.png
      :width: 90%


#. Kurz darauf erhältst du die Meldung, dass **NVMe/USB Boot** erfolgreich geschrieben wurde.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Jetzt kannst du die SD-Karte oder die NVMe-SSD in den Raspberry Pi einlegen. Nach dem Einschalten über USB-C wird der Bootloader automatisch ins EEPROM des Raspberry Pi geschrieben.

.. note::

   Danach wird der Raspberry Pi standardmäßig zuerst von NVMe booten, gefolgt von USB und SD-Karte.

   Schalte den Raspberry Pi aus und entferne die SD-Karte oder NVMe-SSD.


2. Betriebssystem auf NVMe-SSD installieren
-----------------------------------------------

Nun kannst du das Betriebssystem auf die NVMe-SSD installieren.

**Schritte**

#. Stecke deine SD-Karte per Kartenleser in deinen PC oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi-Gerät** und wähle **Raspberry Pi 5** aus der Liste.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Klicke auf den Reiter **Betriebssystem**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scrolle ganz nach unten und wähle dein gewünschtes Betriebssystem.

   .. note::

      * Für **Ubuntu**: Wähle **Other general-purpose OS** → **Ubuntu**, und dann z. B. **Ubuntu Desktop 24.04 LTS (64 bit)** oder **Ubuntu Server 24.04 LTS (64 bit)**.
      * Für **Kali Linux**, **Home Assistant** und **Homebridge**: Wähle **Other specific-purpose OS** und dann das gewünschte System.

   .. image:: img/os_other_os.png
      :width: 90%

#. Wähle im **Speicher**-Menü das passende Gerät aus.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Klicke auf **WEITER**.

   .. note::

      * Bei Systemen ohne Vorkonfiguration wirst du gefragt, ob du Daten auf dem Gerät behalten möchtest. Wenn du sicher bist, dass ein Backup vorhanden ist, wähle **Ja**.
      * Bei vorkonfigurierbaren Systemen (Hostname, WLAN, SSH) erscheint ein Dialog zur Anwendung der Einstellungen. Du kannst **Ja**, **Nein** oder **Zurück** wählen, um weiter zu konfigurieren.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Lege einen **Hostname** für deinen Raspberry Pi fest. Dieser dient als Netzwerkname (z. B. ``<hostname>.local``).

     .. image:: img/os_set_hostname.png

   * Erstelle einen **Benutzernamen** und ein **Passwort** für das Administratorkonto. Dies ist wichtig, da es kein Standardpasswort gibt.

     .. image:: img/os_set_username.png

   * Konfiguriere dein WLAN mit **SSID** und **Passwort**.

     .. note::

       Stelle das ``Wireless LAN country`` auf den zweistelligen `ISO/IEC-Alpha-2-Code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ deines Landes ein.

     .. image:: img/os_set_wifi.png
         
   * Aktiviere SSH unter Dienste, um dich aus der Ferne zu verbinden.

     * Für **Passwort-Authentifizierung** verwende die Angaben aus dem Tab Allgemein.
     * Für öffentliche Schlüssel wähle „Nur öffentliche Schlüssel erlauben“ – oder klicke auf „SSH-Keygen ausführen“, um ein neues Schlüsselpaar zu generieren.

     .. image:: img/os_enable_ssh.png

   * Im Menü **Optionen** kannst du das Verhalten des Imager-Tools anpassen – etwa automatische Benachrichtigung, Medium-Auswurf oder Telemetrie.

     .. image:: img/os_options.png



#. Nachdem du alle Einstellungen vorgenommen hast, klicke auf **Speichern**, dann auf **Ja**, um das Image zu schreiben.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Wenn deine NVMe-SSD bereits Daten enthält, sichere sie vorher. Klicke auf **Ja**, wenn keine Sicherung notwendig ist.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Sobald die Meldung Write Successful erscheint, wurde das Image vollständig geschrieben und überprüft. Dein Raspberry Pi ist nun bereit, direkt von der NVMe-SSD zu booten!
