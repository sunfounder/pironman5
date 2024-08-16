.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _install_os_sd_rpi:

Installation des Betriebssystems auf einer Micro-SD-Karte
============================================================
Wenn Sie eine Micro-SD-Karte verwenden, können Sie der folgenden Anleitung folgen, um das System auf Ihrer Micro-SD-Karte zu installieren.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Erforderliche Komponenten**

* Ein PC
* Eine Micro-SD-Karte und ein Kartenleser

**Schritte**

#. Setzen Sie Ihre SD-Karte in Ihren Computer oder Laptop ein, indem Sie einen Kartenleser verwenden.

#. Klicken Sie im |link_rpi_imager| auf **Raspberry Pi Gerät** und wählen Sie das Modell **Raspberry Pi 5** aus der Dropdown-Liste aus.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Wählen Sie **Betriebssystem** und entscheiden Sie sich für die empfohlene Betriebssystemversion.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Klicken Sie auf **Speicher auswählen** und wählen Sie das geeignete Speichermedium für die Installation.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Klicken Sie auf **Weiter** und dann auf **Einstellungen bearbeiten**, um Ihre Betriebssystemeinstellungen anzupassen. 

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Definieren Sie einen **Hostname** für Ihren Raspberry Pi. Der Hostname ist die Netzwerkkennung Ihres Raspberry Pi. Sie können auf Ihren Pi zugreifen, indem Sie ``<hostname>.local`` oder ``<hostname>.lan`` verwenden.

     .. image:: img/os_set_hostname.png
   

   * Erstellen Sie einen **Benutzernamen** und ein **Passwort** für das Administratorkonto des Raspberry Pi. Die Einrichtung eines eindeutigen Benutzernamens und Passworts ist wichtig, um Ihren Raspberry Pi zu sichern, der kein Standardpasswort hat.

     .. image:: img/os_set_username.png      

   * Konfigurieren Sie das drahtlose Netzwerk, indem Sie die **SSID** und das **Passwort** Ihres Netzwerks angeben.

     .. note::

       Stellen Sie das ``WLAN-Land`` auf den entsprechenden Zwei-Buchstaben `ISO/IEC alpha2-Code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ ein, der Ihrem Standort entspricht.

     .. image:: img/os_set_wifi.png


   * Um sich remote mit Ihrem Raspberry Pi zu verbinden, aktivieren Sie SSH im Reiter "Dienste".

     * Für die **Passwortauthentifizierung** verwenden Sie den Benutzernamen und das Passwort aus dem Reiter "Allgemein".
     * Für die Authentifizierung per öffentlichem Schlüssel wählen Sie "Nur Authentifizierung per öffentlichem Schlüssel zulassen". Wenn Sie einen RSA-Schlüssel haben, wird dieser verwendet. Andernfalls klicken Sie auf "SSH-Keygen ausführen", um ein neues Schlüsselpaar zu generieren.

     .. image:: img/os_enable_ssh.png

   * Das **Optionen**-Menü ermöglicht es Ihnen, das Verhalten des Imagers während des Schreibvorgangs zu konfigurieren, einschließlich der Wiedergabe eines Tons bei Abschluss, des Auswerfens der Medien nach Abschluss und der Aktivierung der Telemetrie.

     .. image:: img/os_options.png

#. Nachdem Sie die Einstellungen für die Betriebssystemanpassung eingegeben haben, klicken Sie auf **Speichern**, um die Anpassung zu speichern. Klicken Sie anschließend auf **Ja**, um sie beim Schreiben des Images anzuwenden.

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. Wenn sich bereits Daten auf der SD-Karte befinden, sichern Sie diese, um Datenverlust zu vermeiden. Klicken Sie auf **Ja**, wenn keine Sicherung erforderlich ist.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Sobald das Popup "Schreiben erfolgreich" erscheint, wurde Ihr Image vollständig geschrieben und überprüft. Sie sind nun bereit, einen Raspberry Pi von der Micro-SD-Karte zu booten!

   .. image:: img/os_finish.png
      :width: 90%
      
