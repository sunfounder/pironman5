.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Enthusiasten tiefer in Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _install_os_sd_rpi_max:

Installation des Betriebssystems
===================================

Bevor Sie Ihren Raspberry Pi verwenden können, müssen Sie **Raspberry Pi OS** auf einer microSD-Karte installieren.  
Diese Anleitung erklärt Schritt für Schritt und einsteigerfreundlich, wie Sie dies mit dem **Raspberry Pi Imager** durchführen.

**Erforderliche Komponenten**

* Ein Computer (Windows, macOS oder Linux)
* Eine microSD-Karte (16 GB oder größer; empfohlene Marken: SanDisk, Samsung)
* Ein microSD-Kartenleser

-------------------

.. start_install_imager

1. Raspberry Pi Imager installieren
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>   

#. Besuchen Sie die offizielle Download-Seite des Raspberry Pi Imager: |shared_link_rpi_imager|. Laden Sie das passende Installationsprogramm für Ihr Betriebssystem herunter.

   .. image:: img/imager_download.png
      :width: 70%

#. Folgen Sie den Installationsanweisungen (Sprache, Installationspfad, Bestätigung). Starten Sie nach der Installation den **Raspberry Pi Imager** über den Desktop oder das Anwendungsmenü.

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. Installation des Betriebssystems auf der microSD-Karte
---------------------------------------------------------------

1. Setzen Sie Ihre microSD-Karte mithilfe eines Kartenlesers in Ihren Computer ein. Sichern Sie vor dem Fortfahren alle wichtigen Daten.

   .. image:: img/insert_sd.png
      :width: 90%

2. Nach dem Start des Raspberry Pi Imager sehen Sie die Seite **Device**. Wählen Sie Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

3. Wechseln Sie zum Abschnitt **OS** und wählen Sie die empfohlene Option **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

4. Wählen Sie im Abschnitt **Storage** Ihre microSD-Karte aus.

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. Klicken Sie auf **Next**, um mit dem Schritt zur Anpassung fortzufahren.

   .. note::

      * Wenn Sie einen Monitor, eine Tastatur und eine Maus direkt an Ihren Raspberry Pi anschließen, können Sie **SKIP CUSTOMISATION** auswählen.  
      * Wenn Sie den Raspberry Pi *headless* (per WLAN und Fernzugriff) einrichten möchten, müssen Sie die Anpassungseinstellungen ausfüllen.

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **Hostname festlegen**

   * Geben Sie Ihrem Raspberry Pi einen eindeutigen Hostnamen.  
   * Sie können später über ``hostname.local`` eine Verbindung herstellen.

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **Lokalisierung festlegen**

   * Wählen Sie Ihre Hauptstadt aus.
   * Der Imager ergänzt automatisch Zeitzone und Tastaturlayout basierend auf Ihrer Auswahl. Sie können diese bei Bedarf anpassen. Klicken Sie anschließend auf **Next**.
   
   .. image:: img/imager_custom_local.png
      :width: 90%

#. **Benutzername & Passwort festlegen**

   Erstellen Sie ein Benutzerkonto für Ihren Raspberry Pi.
   
   .. image:: img/imager_custom_user.png
      :width: 90%

#. **WLAN konfigurieren**

   * Geben Sie Ihre WLAN-**SSID** (Netzwerkname) und das **Passwort** ein.  
   * Ihr Raspberry Pi verbindet sich beim ersten Start automatisch mit dem WLAN.
   
   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **SSH aktivieren (optional, aber empfohlen)**

   * Durch das Aktivieren von SSH können Sie sich von Ihrem Computer aus remote anmelden.  
   * Sie können sich mit Benutzername/Passwort anmelden oder SSH-Schlüssel konfigurieren.
   
   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **Raspberry Pi Connect aktivieren (optional)**


   Raspberry Pi Connect ermöglicht den Zugriff auf den Desktop Ihres Raspberry Pi über einen Webbrowser.
   
   * Aktivieren Sie **Raspberry Pi Connect** und klicken Sie anschließend auf **OPEN RASPBERRY PI CONNECT**.
   
     .. image:: img/imager_custom_connect.png
        :width: 90%

   * Die Raspberry Pi Connect-Website wird in Ihrem Standardbrowser geöffnet. Melden Sie sich mit Ihrem Raspberry Pi ID-Konto an oder registrieren Sie sich, falls Sie noch kein Konto haben.

     .. image:: img/imager_custom_open.png
        :width: 90%

   * Erstellen Sie auf der Seite **New auth key** Ihren einmaligen Authentifizierungsschlüssel. 
      
      * Wenn Ihr Raspberry Pi ID-Konto keiner Organisation angehört, wählen Sie **Create auth key and launch Raspberry Pi Imager**.
      * Wenn Sie einer oder mehreren Organisationen angehören, wählen Sie eine aus, erstellen Sie dann den Schlüssel und starten Sie den Imager.
      * Stellen Sie sicher, dass Ihr Raspberry Pi eingeschaltet und mit dem Internet verbunden ist, bevor der Schlüssel abläuft.
   
     .. image:: img/imager_custom_authkey.png
        :width: 90%
   
   * Ihr Browser fragt möglicherweise, ob der Raspberry Pi Imager geöffnet werden soll — erlauben Sie dies.

     * Der Imager öffnet sich im Tab **Raspberry Pi Connect** und zeigt das Authentifizierungstoken an.
     * Wenn das Token nicht automatisch übertragen wird, öffnen Sie den Abschnitt **Having trouble?** auf der Raspberry Pi Connect-Seite, kopieren Sie das Token und fügen Sie es manuell in den Imager ein.

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. Überprüfen Sie alle Einstellungen und klicken Sie auf **WRITE**.

   .. image:: img/imager_writing.png
      :width: 90%

#. Wenn das Speichermedium bereits Daten enthält, zeigt der Raspberry Pi Imager eine Warnung an, dass alle Daten auf dem Gerät gelöscht werden. Vergewissern Sie sich, dass Sie das richtige Laufwerk ausgewählt haben, und klicken Sie anschließend auf **I UNDERSTAND, ERASE AND WRITE**, um fortzufahren.

   .. image:: img/imager_erase.png
      :width: 90%

#. Warten Sie, bis der Schreib- und Überprüfungsvorgang abgeschlossen ist. Danach zeigt der Raspberry Pi Imager **Write complete!** sowie eine Zusammenfassung Ihrer Auswahl an. Das Speichermedium wird automatisch ausgeworfen, sodass Sie es sicher entfernen können.


   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. Entfernen Sie die microSD-Karte und setzen Sie sie in den Steckplatz an der Unterseite Ihres Raspberry Pi ein. Ihr Raspberry Pi ist nun bereit, mit dem neuen Betriebssystem zu starten!

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%

   
