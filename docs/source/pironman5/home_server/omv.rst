.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit Gleichgesinnten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und festlichen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!


.. _omv_5:


Einrichtung von OpenMediaVault
=============================================

.. warning::

   OpenMediaVault **unterstützt keine** Installation auf dem Raspberry Pi OS mit Desktop-Oberfläche.

   Bitte stellen Sie sicher, dass Sie das richtige Betriebssystem installiert und die Netzwerkkonfiguration vorgenommen haben.
   Die Vorgehensweise entspricht der Anleitung unter :ref:`install_os_sd_rpi`, jedoch wählen Sie beim Auswählen des Images bitte „Raspberry Pi OS Lite“ aus der Kategorie „Raspberry Pi OS (other)“.

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (kurz OMV) ist ein quelloffenes Network Attached Storage (NAS)-Betriebssystem auf Basis von Debian Linux. Es wurde für den Einsatz in privaten Haushalten und kleinen Büros entwickelt und soll die Speicherverwaltung vereinfachen sowie umfangreiche Netzwerkdienste bieten.

Bitte folgen Sie diesen Schritten, um OpenMediaVault auf Ihrem Raspberry Pi zu installieren:

1. Verbindung zum Raspberry Pi über SSH herstellen
-----------------------------------------------------

   Geben Sie im Terminal den folgenden Befehl ein:

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Wenn Sie Windows verwenden, nutzen Sie PuTTY oder einen anderen SSH-Client zur Verbindung mit dem Raspberry Pi.

2. OpenMediaVault installieren
----------------------------------

   Geben Sie im Terminal den folgenden Befehl ein:

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   Dies lädt das Installationsskript herunter und führt es aus. Starten Sie den Raspberry Pi nach der Installation nicht neu.

3. Zugriff auf OpenMediaVault
---------------------------------

   Öffnen Sie Ihren Browser und geben Sie folgende Adresse ein:

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: Falls die obige Adresse nicht erreichbar ist, versuchen Sie es mit der IP-Adresse, z. B. http://192.168.1.100.

   Es erscheint eine Login-Seite. Melden Sie sich mit dem Standardbenutzernamen und Passwort an. Der Standardbenutzername ist ``admin``, das Passwort lautet ``openmediavault``.

   .. image:: img/omv/omv-login.png

   Nach der Anmeldung sehen Sie die Hauptoberfläche von OpenMediaVault.

   .. image:: img/omv/omv-main.png

   Sie haben OpenMediaVault erfolgreich installiert und können nun mit der Konfiguration und Verwaltung Ihres Speichers beginnen.



4. RAID einrichten (optional)
-----------------------------

   NVMe-RAID ist eine Speicherlösung, bei der mehrere NVMe-SSDs mithilfe von RAID-Technologie kombiniert werden. Ziel ist es, die hohe Geschwindigkeit des NVMe-Protokolls mit den Redundanz- und Leistungsmerkmalen von RAID zu vereinen. Häufig genutzte Modi sind RAID 0, 1, 5, 10 usw. Bei zwei NVMe-SSDs sind RAID 0 und RAID 1 die gängigsten Optionen.

   * RAID 0 nutzt Striping, bei dem Daten in Blöcke aufgeteilt und auf mehrere Laufwerke verteilt werden – für höhere Lese-/Schreibgeschwindigkeit. RAID 0 bietet keine Redundanz: fällt ein Laufwerk aus, gehen alle Daten verloren.

   * RAID 1 nutzt Mirroring: Daten werden auf mehrere Laufwerke gespiegelt, was Redundanz bietet. Die Geschwindigkeit hängt vom langsamsten Laufwerk ab. Bei Ausfall eines Laufwerks bleibt der Zugriff auf die Daten über das andere erhalten.

   .. note:: Für RAID 0 oder RAID 1 sind mindestens zwei Laufwerke erforderlich. Bei RAID 0 entspricht die Gesamtkapazität der Summe aller Laufwerke, bei RAID 1 der Kapazität des kleinsten Laufwerks.

   1. Wählen Sie im Menü ``System`` den Punkt ``Plugins``, suchen Sie nach dem Plugin ``openmediavault-md`` und installieren Sie es.

   .. image:: img/omv/omv-raid-1.png

   2. Klicken Sie im Menü ``Speicher`` auf ``Laufwerke`` und löschen Sie die beiden SSDs.

   .. image:: img/omv/omv-raid-2.png

   3. Achtung: Durch diesen Vorgang werden **alle Daten** auf den Laufwerken gelöscht. Sichern Sie vorher wichtige Daten.

   .. image:: img/omv/omv-raid-3.png

   4. Wählen Sie beim Löschmodus ``SCHNELL`` – das ist ausreichend.

   .. image:: img/omv/omv-raid-4.png

   5. Gehen Sie zum Reiter ``Mehrere Geräte`` und klicken Sie auf ``Erstellen``.

   .. image:: img/omv/omv-raid-5.png

   6. Wählen Sie unter ``Level`` entweder Striping (RAID 0) oder Mirroring (RAID 1). Unter ``Geräte`` wählen Sie die zuvor gelöschten Laufwerke. Klicken Sie auf ``Speichern`` und warten Sie, bis die RAID-Konfiguration abgeschlossen ist.

   .. image:: img/omv/omv-raid-6.png

   .. note:: Bei einem Fehler (500 - Internal Server Error) starten Sie OMV neu.

   7. Übernehmen Sie die Änderungen mit einem Klick auf ``Übernehmen``.

   .. image:: img/omv/omv-raid-7.png

   8. Warten Sie, bis der Status des RAID-Verbunds ``100%`` erreicht hat.

   .. image:: img/omv/omv-raid-8.png

   9. Nach Abschluss der Konfiguration sind Ihre Laufwerke im RAID 0- oder RAID 1-Verbund nutzbar und stehen als ein gemeinsamer Speicher zur Verfügung.

5. Speicher konfigurieren
-------------------------

   In der Hauptoberfläche von OpenMediaVault klicken Sie im Menü links auf ``Speicher``. Auf der ``Speicher``-Seite wählen Sie den Reiter ``Laufwerke``. Dort sehen Sie alle an Ihren Raspberry Pi angeschlossenen Laufwerke. Vergewissern Sie sich, dass Ihr NVMe-Gehäuse ein Laufwerk enthält.

   .. image:: img/omv/omv-disk.png

   1. Klicken Sie in der Seitenleiste auf ``Dateisysteme``. Erstellen und mounten Sie ein neues Dateisystem. Wählen Sie ``ext4`` als Typ.

   .. image:: img/omv/omv-mount.png

   2. Wählen Sie das Gerät aus und klicken Sie auf Speichern.

   .. note:: Wenn Sie ein RAID eingerichtet haben, wird das RAID-Gerät in der Liste angezeigt. Wählen Sie es einfach aus und speichern Sie.

   .. image:: img/omv/omv-mount-2.png

   3. Es erscheint ein Fenster mit dem Hinweis, dass das Dateisystem erstellt wird. Bitte einen Moment warten.

   .. image:: img/omv/omv-mount-3.png

   4. Nach Abschluss gelangen Sie zur ``Mount``-Oberfläche. Wählen Sie das erstellte Dateisystem aus und mounten Sie es auf Ihrem Raspberry Pi.

   .. image:: img/omv/omv-mount-4.png

   .. note:: Wenn Sie zwei Laufwerke (ohne RAID) verwenden, wiederholen Sie die obigen Schritte auch für das zweite Laufwerk.

   5. Nach dem Mounten klicken Sie auf ``Übernehmen``. Anschließend wird das Laufwerk im Dateisystem angezeigt.

   .. image:: img/omv/omv-mount-5.png

   Sie haben nun OpenMediaVault erfolgreich konfiguriert und Ihre Laufwerke eingebunden. Die Speicherverwaltung kann beginnen.


6. Gemeinsamen Ordner erstellen
-------------------------------

   1. Wechseln Sie in der ``Storage``-Seite zum Reiter ``Shared Folders`` und klicken Sie auf ``Create``.

   .. image:: img/omv/omv-share-1.png

   2. Geben Sie einen Namen ein, wählen Sie das gewünschte Laufwerk, den Pfad und die Berechtigungen des Ordners. Klicken Sie auf ``Speichern``.

   .. image:: img/omv/omv-share-2.png

   3. Der neu erstellte Ordner erscheint nun in der Liste. Prüfen Sie die Angaben und übernehmen Sie die Konfiguration.

   .. image:: img/omv/omv-share-3.png

   Der freigegebene Ordner wurde erfolgreich erstellt.


7. Neuen Benutzer anlegen
-----------------------------

   Um auf den Ordner zugreifen zu können, erstellen Sie einen neuen Benutzer:

   1. Gehen Sie zur ``User``-Seite und klicken Sie auf ``Create``.

   .. image:: img/omv/omv-user-1.png

   2. Geben Sie Benutzername und Passwort ein und klicken Sie auf ``Save``.

   .. image:: img/omv/omv-user-2.png

   Der Benutzer wurde erfolgreich erstellt.


8. Berechtigungen festlegen
---------------------------------

   1. Klicken Sie auf der Seite ``Shared Folders`` auf den eben erstellten Ordner. Dann auf ``Permissions``.

   .. image:: img/omv/omv-user-3.png

   2. Legen Sie die Zugriffsrechte fest und klicken Sie auf ``Save``.

   .. image:: img/omv/omv-user-4.png

   3. Klicken Sie anschließend auf ``Apply``.

   .. image:: img/omv/omv-user-5.png

   Der neue Benutzer kann nun auf den Ordner zugreifen.


9. SMB-Dienst konfigurieren
-------------------------------

   1. Gehen Sie zur Seite ``Services``, öffnen Sie den Reiter ``SMB/CIFS`` > ``Setting`` und aktivieren Sie die Option ``Enable``. Dann auf ``Save`` klicken.

   .. image:: img/omv/omv-smb-1.png

   2. Übernehmen Sie die Änderungen mit ``Apply``.

   .. image:: img/omv/omv-smb-2.png

   3. Wechseln Sie zur Seite ``Shares`` und klicken Sie auf ``Create``.

   .. image:: img/omv/omv-smb-3.png

   4. Wählen Sie auf der Seite ``Create Share`` den Pfad zum freigegebenen Ordner. Klicken Sie auf ``Save``. Weitere Optionen auf dieser Seite können nach Bedarf angepasst werden.

   .. image:: img/omv/omv-smb-4.png

   5. Klicken Sie auf ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   Der SMB-Dienst wurde erfolgreich eingerichtet. Sie können nun per SMB auf den Ordner zugreifen.


10. Zugriff auf freigegebenen Ordner unter Windows
--------------------------------------------------

   1. Öffnen Sie ``This PC`` und klicken Sie auf ``Map network drive``.

   .. image:: img/omv/omv-network-location-1.png

   2. Geben Sie im Dialogfeld die IP-Adresse des Raspberry Pi im Feld ``Folder`` ein, z. B. ``\\192.168.1.100\`` oder den Hostnamen ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Klicken Sie auf Durchsuchen, wählen Sie den Ordner aus und geben Sie bei Aufforderung die Zugangsdaten ein.

   .. image:: img/omv/omv-network-location-3.png

   4. Aktivieren Sie „Verbindung bei Anmeldung wiederherstellen“ und klicken Sie auf ``Finish``.

   .. image:: img/omv/omv-network-location-4.png

   5. Sie können nun auf den NAS-Ordner zugreifen.

   .. image:: img/omv/omv-network-location-5.png

10. Zugriff auf freigegebenen Ordner unter macOS
------------------------------------------------

   1. Wählen Sie im ``Go``-Menü die Option ``Connect to Server``.

   .. image:: img/omv/omv-mac-1.png

   2. Geben Sie im Dialog ``smb://192.168.1.100`` oder ``smb://pi.local`` ein.

   .. image:: img/omv/omv-mac-2.png

   3. Klicken Sie auf ``Connect``.

   .. image:: img/omv/omv-mac-3.png

   4. Geben Sie Benutzername und Passwort ein und klicken Sie auf ``Connect``.

   .. image:: img/omv/omv-mac-4.png

   5. Sie können nun auf den NAS-Ordner zugreifen.

   .. image:: img/omv/omv-mac-5.png
