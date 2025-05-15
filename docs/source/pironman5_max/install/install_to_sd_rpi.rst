.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Experten-Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu Produktneuheiten und exklusiven Einblicken.
    - **Exklusive Rabatte**: Profitiere von Sonderangeboten auf unsere neuesten Produkte.
    - **Aktionen & Gewinnspiele**: Nimm an festlichen Aktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_install_os_sd_rpi:

Installation des Betriebssystems auf einer Micro-SD-Karte
===========================================================
Wenn du eine Micro-SD-Karte verwendest, kannst du dem folgenden Tutorial folgen, um das Betriebssystem auf deiner Karte zu installieren.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Erforderliche Komponenten**

* Ein Computer
* Eine Micro-SD-Karte und ein Kartenleser

**Schritte**

#. Stecke die SD-Karte mit einem Kartenleser in deinen Computer oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi-Gerät** und wähle aus der Dropdown-Liste das Modell **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Wähle **Betriebssystem** aus und entscheide dich für die empfohlene Systemversion.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Klicke auf **Speicher auswählen** und wähle das passende Zielgerät für die Installation aus.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Klicke auf **WEITER** und anschließend auf **EINSTELLUNGEN BEARBEITEN**, um deine Systemeinstellungen anzupassen.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Lege einen **Hostname** für deinen Raspberry Pi fest. Der Hostname ist der Netzwerkname deines Raspberry Pi. Du kannst ihn über ``<hostname>.local`` oder ``<hostname>.lan`` erreichen.

     .. image:: img/os_set_hostname.png


   * Erstelle einen **Benutzernamen** und ein **Passwort** für das Administrator-Konto deines Raspberry Pi. Eine individuelle Anmeldung ist notwendig, da es kein Standardpasswort gibt.

     .. image:: img/os_set_username.png

   * Konfiguriere das WLAN, indem du die **SSID** und das **Passwort** deines Netzwerks eingibst.

     .. note::

        Setze das ``Wireless LAN country`` entsprechend dem Zwei-Buchstaben- `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ deines Landes.

     .. image:: img/os_set_wifi.png


   * Aktiviere SSH, um dich aus der Ferne mit deinem Raspberry Pi zu verbinden.

     * Für die **Passwort-Authentifizierung** verwende die Zugangsdaten aus dem Reiter Allgemein.
     * Für die Schlüssel-Authentifizierung wähle „Nur Public-Key-Authentifizierung zulassen“. Falls kein RSA-Schlüssel vorhanden ist, klicke auf „SSH-Keygen ausführen“, um ein neues Schlüsselpaar zu generieren.

     .. image:: img/os_enable_ssh.png

   * Im Reiter **Optionen** kannst du das Verhalten des Imagers beim Schreiben anpassen – z. B. Ton nach Abschluss, Medium auswerfen oder Telemetrie aktivieren.

     .. image:: img/os_options.png

#. Nachdem du deine Einstellungen vorgenommen hast, klicke auf **Speichern**, um sie zu sichern. Klicke anschließend auf **Ja**, um sie beim Schreiben anzuwenden.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Falls sich bereits Daten auf der SD-Karte befinden, erstelle vorher ein Backup. Klicke auf **Ja**, wenn du mit dem Überschreiben einverstanden bist.

   .. image:: img/os_continue.png
      :width: 90%


#. Sobald das Pop-up „Erfolgreich geschrieben“ erscheint, wurde dein Abbild erfolgreich erstellt und überprüft. Du kannst nun deinen Raspberry Pi von der Micro-SD-Karte starten!

   .. image:: img/os_finish.png
      :width: 90%
