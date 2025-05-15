.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Einblicke**: Erhalte frühzeitig Informationen über neue Produkte und exklusive Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Angeboten für unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an saisonalen Aktionen und Verlosungen teil.

    👉 Bereit für spannende Projekte? Klicke auf [|link_sf_facebook|] und mach noch heute mit!

.. _install_os_sd_rpi_mini:

Installation des Betriebssystems auf einer Micro-SD-Karte
==============================================================
.. If you are using a Micro SD card, you can follow the tutorial below to install the system onto your Micro SD card.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Erforderliche Komponenten**

* Ein Computer oder Laptop
* Eine Micro-SD-Karte und ein Kartenleser

**Schritte**

#. Stecke deine SD-Karte über einen Kartenleser in deinen Computer oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle aus der Dropdown-Liste das Modell **Raspberry Pi 5** aus.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Wähle **Operating System** und entscheide dich für die empfohlene Systemversion.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Klicke auf **Choose Storage** und wähle das passende Speichermedium für die Installation aus.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Klicke auf **NEXT** und dann auf **EDIT SETTINGS**, um die Einstellungen des Betriebssystems individuell anzupassen.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Lege einen **Hostname** für deinen Raspberry Pi fest. Dieser dient als Netzwerkname und ermöglicht den Zugriff z. B. über ``<hostname>.local`` oder ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png


   * Erstelle einen **Benutzernamen** und ein **Passwort** für das Administratorkonto des Raspberry Pi. Ein einzigartiger Benutzername und ein sicheres Passwort sind wichtig, da es kein Standardpasswort gibt.

     .. image:: img/os_set_username.png

   * Konfiguriere das WLAN, indem du die **SSID** deines Netzwerks und das entsprechende **Passwort** eingibst.

     .. note::

       Gib für das Feld ``Wireless LAN country`` den entsprechenden zweistelligen `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ deines Landes an.

     .. image:: img/os_set_wifi.png


   * Um dich aus der Ferne mit deinem Raspberry Pi zu verbinden, aktiviere SSH im Tab „Services“.

     * Für **password authentication** verwende den Benutzernamen und das Passwort aus dem Tab „General“.
     * Für Public-Key-Authentifizierung wähle „Allow public-key authentication only“. Wenn ein RSA-Schlüssel vorhanden ist, wird dieser genutzt. Falls nicht, klicke auf „Run SSH-keygen“, um ein neues Schlüsselpaar zu erstellen.

     .. image:: img/os_enable_ssh.png

   * Im Menü **Options** kannst du das Verhalten des Imagers beim Schreiben konfigurieren – z. B. Ton abspielen nach Abschluss, Medium automatisch auswerfen oder Telemetrie aktivieren.

     .. image:: img/os_options.png

#. Wenn du die OS-Einstellungen abgeschlossen hast, klicke auf **Save**, um die Konfiguration zu speichern. Klicke anschließend auf **Yes**, um sie beim Schreiben des Images anzuwenden.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Falls die SD-Karte bereits Daten enthält, solltest du diese vorher sichern. Klicke auf **Yes**, wenn du kein Backup benötigst.

   .. image:: img/os_continue.png
      :width: 90%


#. Sobald die Meldung „Write Successful“ erscheint, wurde das Image erfolgreich geschrieben und überprüft. Jetzt kannst du den Raspberry Pi von der Micro-SD-Karte starten!

   .. image:: img/os_finish.png
      :width: 90%
