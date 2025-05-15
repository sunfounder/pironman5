.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenhilfe**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Kenntnisse zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit für spannende Projekte? Klicke auf [|link_sf_facebook|] und werde noch heute Teil der Community!

.. _install_to_sd_home_bridge_mini:

Installation des Betriebssystems auf einer Micro-SD-Karte
=============================================================

Wenn du eine Micro-SD-Karte verwendest, kannst du der folgenden Anleitung folgen, um das System darauf zu installieren.


**Erforderliche Komponenten**

* Ein Computer oder Laptop
* Eine Micro-SD-Karte und ein Kartenleser

**Schritte**

#. Stecke deine SD-Karte über einen Kartenleser in den Computer oder Laptop.

#. Öffne den |link_rpi_imager|, klicke auf **Raspberry Pi Device** und wähle im Dropdown-Menü das Modell **Raspberry Pi 5** aus.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Klicke auf den Reiter **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scrolle bis zum Ende der Liste und wähle dein Betriebssystem aus.

   .. note::

      * Für das **Ubuntu**-System klicke auf **Other general-purpose OS** -> **Ubuntu** und wähle entweder **Ubuntu Desktop 24.04 LTS (64 bit)** oder **Ubuntu Server 24.04 LTS (64 bit)**.
      * Für **Kali Linux**, **Home Assistant** oder **Homebridge** klicke auf **Other specific-purpose OS** und wähle dort das gewünschte System aus.

   .. image:: img/os_other_os.png
      :width: 90%

#. Wähle unter **Storage** das richtige Speichermedium für die Installation aus.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Klicke auf **NEXT**.

   .. note::

      * Bei Systemen, die nicht im Voraus konfiguriert werden können, wirst du nach dem Klick auf **NEXT** gefragt, ob du die Daten auf dem Gerät speichern möchtest. Wenn du bereits ein Backup erstellt hast, wähle **Yes**.
      * Bei Systemen, bei denen Hostname, WLAN und SSH im Voraus konfiguriert werden können, erscheint ein Hinweisfenster, ob die benutzerdefinierten Einstellungen übernommen werden sollen. Du kannst **Yes**, **No** oder Zurück zur Bearbeitung wählen.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Lege einen **Hostname** für deinen Raspberry Pi fest. Dieser dient als Netzwerkname, z. B. erreichbar über ``<hostname>.local`` oder ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Erstelle einen **Benutzernamen** und ein **Passwort** für das Administratorkonto deines Raspberry Pi. Ein eindeutiger Benutzername und ein sicheres Passwort sind wichtig, da es kein Standardpasswort gibt.

     .. image:: img/os_set_username.png

   * Konfiguriere das WLAN, indem du die **SSID** deines Netzwerks und das zugehörige **Passwort** eingibst.

     .. note::

       Gib für das Feld ``Wireless LAN country`` den passenden zweistelligen `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ deines Landes an.

     .. image:: img/os_set_wifi.png

   * Um dich per Fernzugriff mit deinem Raspberry Pi zu verbinden, aktiviere SSH im Reiter „Services“.

     * Für **Passwort-Authentifizierung** nutze den Benutzername und das Passwort aus dem Reiter „General“.
     * Für Public-Key-Authentifizierung wähle „Allow public-key authentication only“. Falls bereits ein RSA-Schlüssel vorhanden ist, wird dieser verwendet. Andernfalls klicke auf „Run SSH-keygen“, um ein neues Schlüsselpaar zu erzeugen.

     .. image:: img/os_enable_ssh.png

   * Im Menü **Options** kannst du das Verhalten des Imagers während des Schreibvorgangs festlegen – etwa ein Tonsignal nach Abschluss, automatisches Auswerfen des Mediums oder die Aktivierung der Telemetrie.

     .. image:: img/os_options.png

#. Wenn du die OS-Konfiguration abgeschlossen hast, klicke auf **Save**, um die Einstellungen zu speichern. Danach auf **Yes**, um die Konfiguration beim Schreiben des Images zu übernehmen.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Falls die SD-Karte bereits Daten enthält, sichere diese unbedingt. Klicke auf **Yes**, wenn kein Backup benötigt wird.

   .. image:: img/os_continue.png
      :width: 90%


#. Sobald die Meldung „Write Successful“ erscheint, wurde das Image erfolgreich geschrieben und überprüft. Jetzt bist du bereit, deinen Raspberry Pi von der Micro-SD-Karte zu starten!
