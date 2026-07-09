.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_os_sd_rpi_promax:

Das Betriebssystem installieren
===================================

Bevor Sie Ihren Raspberry Pi verwenden können, müssen Sie **Raspberry Pi OS** auf einer microSD-Karte installieren.
Diese Anleitung erklärt, wie das mit **Raspberry Pi Imager** auf einfache, anfängergerechte Weise funktioniert.

**Benötigte Komponenten**

* Ein Computer (Windows, macOS oder Linux)
* Eine microSD-Karte (16 GB oder größer; empfohlene Marken: SanDisk, Samsung)
* Ein microSD-Kartenleser

-------------------

.. start_install_imager

1. Raspberry Pi Imager installieren
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>

#. Besuchen Sie die offizielle Download-Seite für Raspberry Pi Imager: |shared_link_rpi_imager|. Laden Sie das richtige Installationsprogramm für Ihr Betriebssystem herunter.

   .. image:: img/imager_download.png
      :width: 70%

#. Folgen Sie den Installationsaufforderungen (Sprache, Installationspfad, Bestätigung). Starten Sie nach der Installation **Raspberry Pi Imager** von Ihrem Desktop oder aus dem Anwendungsmenü.

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. Betriebssystem auf der microSD-Karte installieren
-----------------------------------------------------------------------------

1. Legen Sie Ihre microSD-Karte mit einem Kartenleser in Ihren Computer ein. Sichern Sie vor dem Fortfahren alle wichtigen Daten.

   .. image:: img/insert_sd.png
      :width: 90%

2. Wenn Raspberry Pi Imager geöffnet wird, sehen Sie die Seite **Gerät**. Wählen Sie Ihr Raspberry Pi 5-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

3. Gehen Sie zum Bereich **Betriebssystem** und wählen Sie die empfohlene Option **Raspberry Pi OS (64-bit)**.

   .. warning::

      Achten Sie darauf, eine **64-Bit**-Version zu wählen. Wenn Sie ein **32-Bit**-System installieren, sind einige Pakete nur für ``aarch64`` (64 Bit) verfügbar, und bestimmte Funktionen lassen sich möglicherweise nicht installieren oder funktionieren nicht richtig.

   .. image:: img/imager_os.png
      :width: 90%

4. Wählen Sie im Bereich **Speicher** Ihre microSD-Karte aus.

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. Klicken Sie auf **Weiter**, um zum Anpassungsschritt zu gelangen.

   .. note::

      * Wenn Sie Monitor, Tastatur und Maus direkt an Ihren Raspberry Pi anschließen, können Sie auf **ANPASSUNG ÜBERSPRINGEN** klicken.
      * Wenn Sie den Raspberry Pi *headless* einrichten möchten (WLAN-Fernzugriff), müssen Sie die Anpassungseinstellungen vornehmen.

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **Hostname festlegen**

   * Geben Sie Ihrem Raspberry Pi einen eindeutigen Hostnamen.
   * Sie können später über ``hostname.local`` eine Verbindung herstellen.

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **Lokalisierung einstellen**

   * Wählen Sie Ihre Hauptstadt.
   * Der Imager vervollständigt automatisch die Zeitzone und das Tastaturlayout basierend auf Ihrer Auswahl, Sie können diese bei Bedarf jedoch anpassen. Klicken Sie auf Weiter.

   .. image:: img/imager_custom_local.png
      :width: 90%

#. **Benutzername & Passwort festlegen**

   Erstellen Sie ein Benutzerkonto für Ihren Raspberry Pi.

   .. image:: img/imager_custom_user.png
      :width: 90%

#. **WLAN konfigurieren**

   * Geben Sie Ihre WLAN-**SSID** (Netzwerkname) und Ihr **Passwort** ein.
   * Ihr Raspberry Pi wird sich beim ersten Start automatisch verbinden.

   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **SSH aktivieren (optional, aber empfohlen)**

   * Die Aktivierung von SSH ermöglicht es Ihnen, sich von Ihrem Computer aus remote anzumelden.
   * Sie können sich mit Ihrem Benutzernamen/Passwort anmelden oder SSH-Schlüssel konfigurieren.

   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **Raspberry Pi Connect aktivieren (optional)**


   Raspberry Pi Connect ermöglicht es Ihnen, von einem Webbrowser aus auf den Desktop Ihres Raspberry Pi zuzugreifen.

   * Aktivieren Sie **Raspberry Pi Connect** und klicken Sie dann auf **RASPBERRY PI CONNECT ÖFFNEN**.

     .. image:: img/imager_custom_connect.png
        :width: 90%

   * Die Raspberry Pi Connect-Website wird in Ihrem Standardbrowser geöffnet. Melden Sie sich bei Ihrem Raspberry Pi-ID-Konto an, oder registrieren Sie sich, falls Sie noch keins haben.

     .. image:: img/imager_custom_open.png
        :width: 90%

   * Erstellen Sie auf der Seite **Neuer Authentifizierungsschlüssel** Ihren einmaligen Authentifizierungsschlüssel.

      * Wenn Ihr Raspberry Pi-ID-Konto keiner Organisation angehört, wählen Sie **Authentifizierungsschlüssel erstellen und Raspberry Pi Imager starten**.
      * Wenn Sie einer oder mehreren Organisationen angehören, wählen Sie eine aus, erstellen Sie dann den Schlüssel und starten Sie den Imager.
      * Stellen Sie sicher, dass Sie Ihren Raspberry Pi einschalten und mit dem Internet verbinden, bevor der Schlüssel abläuft.

     .. image:: img/imager_custom_authkey.png
        :width: 90%

   * Ihr Browser fragt möglicherweise, ob Raspberry Pi Imager geöffnet werden soll — erlauben Sie dies.

     * Der Imager wird auf dem Raspberry Pi Connect-Tab geöffnet und zeigt das Authentifizierungstoken an.
     * Wenn das Token nicht automatisch übertragen wird, öffnen Sie den Abschnitt **Probleme?** auf der Raspberry Pi Connect-Seite, kopieren Sie das Token und fügen Sie es manuell in den Imager ein.

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. Überprüfen Sie alle Einstellungen und klicken Sie auf **SCHREIBEN**.

   .. image:: img/imager_writing.png
      :width: 90%

#. Wenn die Karte bereits Daten enthält, zeigt Raspberry Pi Imager eine Warnung an, dass alle Daten auf dem Gerät gelöscht werden. Überprüfen Sie noch einmal, dass Sie das richtige Laufwerk ausgewählt haben, und klicken Sie dann auf **ICH VERSTEHE, LÖSCHEN UND SCHREIBEN**, um fortzufahren.

   .. image:: img/imager_erase.png
      :width: 90%

#. Warten Sie, bis der Schreibvorgang und die Überprüfung abgeschlossen sind. Wenn dies erledigt ist, zeigt Raspberry Pi Imager **Schreiben abgeschlossen!** und eine Zusammenfassung Ihrer Auswahl an. Das Speichergerät wird automatisch ausgeworfen, sodass Sie es sicher entfernen können.

   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. Entfernen Sie die microSD-Karte und stecken Sie sie in den Steckplatz auf der Unterseite Ihres Raspberry Pi. Ihr Raspberry Pi ist nun bereit, mit dem neuen Betriebssystem zu booten!

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%