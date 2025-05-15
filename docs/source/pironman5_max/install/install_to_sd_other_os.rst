.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Experten-Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Profitiere von Sonderangeboten für unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an festlichen Aktionen und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu erschaffen? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _max_install_to_sd_home_bridge:

Installation des Betriebssystems auf einer Micro-SD-Karte
=============================================================

Wenn du eine Micro-SD-Karte verwendest, kannst du das folgende Tutorial nutzen, um das System auf deine Karte zu installieren.


**Erforderliche Komponenten**

* Ein Computer
* Eine Micro-SD-Karte und ein Kartenleser

**Schritte**

#. Stecke die SD-Karte mit einem Kartenleser in deinen Computer oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi-Gerät** und wähle aus der Dropdown-Liste das Modell **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Klicke auf den Reiter **Betriebssystem**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scrolle nach unten und wähle dein gewünschtes Betriebssystem aus.

   .. note::

      * Für das **Ubuntu**-System: Klicke auf **Other general-purpose OS** -> **Ubuntu** und wähle **Ubuntu Desktop 24.04 LTS (64 bit)** oder **Ubuntu Server 24.04 LTS (64 bit)**.
      * Für **Kali Linux**, **Home Assistant** und **Homebridge**: Klicke auf **Other specific-purpose OS** und wähle das entsprechende System aus.

   .. image:: img/os_other_os.png
      :width: 90%

#. Unter **Speicher** wählst du das passende Zielgerät für die Installation aus.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Klicke auf **WEITER**.

   .. note::

      * Bei Systemen, die nicht im Voraus konfiguriert werden können, wirst du nach dem Klick auf **WEITER** gefragt, ob du die Daten auf dem Gerät behalten möchtest. Falls du bereits ein Backup erstellt hast, klicke auf **Ja**.

      * Bei Systemen, bei denen Hostname, WLAN und SSH vorab konfiguriert werden können, erscheint ein Pop-up, in dem du gefragt wirst, ob du die benutzerdefinierten Einstellungen anwenden möchtest. Du kannst **Ja**, **Nein** oder **Zurück zur Bearbeitung** wählen.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Lege einen **Hostname** für deinen Raspberry Pi fest. Der Hostname ist der Netzwerkname deines Raspberry Pi. Du kannst deinen Pi unter ``<hostname>.local`` oder ``<hostname>.lan`` erreichen.

     .. image:: img/os_set_hostname.png  

   * Erstelle einen **Benutzernamen** und ein **Passwort** für das Administrator-Konto des Raspberry Pi. Ein individueller Benutzername und ein sicheres Passwort sind wichtig, da es kein Standardpasswort gibt.

     .. image:: img/os_set_username.png

   * Konfiguriere das WLAN, indem du **SSID** und **Passwort** deines Netzwerks angibst.

     .. note::

        Stelle das Land für das drahtlose Netzwerk auf den entsprechenden `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ ein.

     .. image:: img/os_set_wifi.png

   * Um dich remote mit deinem Raspberry Pi zu verbinden, aktiviere SSH im Tab Dienste.

     * Für **Passwort-Authentifizierung** verwende die Zugangsdaten aus dem Reiter Allgemein.
     * Für Public-Key-Authentifizierung wähle "Nur Public-Key-Authentifizierung zulassen". Wenn bereits ein RSA-Schlüssel vorhanden ist, wird dieser genutzt. Falls nicht, klicke auf "SSH-Keygen ausführen", um ein neues Schlüsselpaar zu generieren.

     .. image:: img/os_enable_ssh.png

   * Im Reiter **Optionen** kannst du festlegen, wie sich der Imager nach dem Schreiben verhält – z. B. Ton abspielen, Medium auswerfen oder Telemetrie aktivieren.

     .. image:: img/os_options.png

#. Wenn du alle Einstellungen vorgenommen hast, klicke auf **Speichern**, um deine Anpassungen zu sichern. Danach klicke auf **Ja**, um sie beim Schreiben des Images anzuwenden.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Wenn sich auf der SD-Karte bereits Daten befinden, solltest du ein Backup erstellen. Klicke auf **Ja**, wenn du mit dem Überschreiben einverstanden bist.

   .. image:: img/os_continue.png
      :width: 90%


#. Sobald das Pop-up „Schreiben erfolgreich“ erscheint, wurde dein Image erfolgreich geschrieben und überprüft. Du kannst jetzt deinen Raspberry Pi von der Micro-SD-Karte starten!
