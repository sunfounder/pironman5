.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Konfiguration von NextCloudPi
=======================================

NextCloud ist eine Open-Source-Lösung für privaten Cloud-Speicher, ähnlich wie Google Drive oder Dropbox.
Sie kann zum Speichern von Dateien, Teilen von Dokumenten, Synchronisieren von Fotos sowie Verwalten von Kalendern und Kontakten genutzt werden.
Im Gegensatz zu öffentlichen Cloud-Diensten gibt NextCloud den Nutzern die vollständige Kontrolle über ihre Daten, was es zu einer idealen Lösung für Einzelpersonen und kleine Teams macht, die Wert auf Datenschutz und Datensicherheit legen.

Die Pironman5-Serie, betrieben von Raspberry Pi, bietet niedrigen Energieverbrauch, kompakte Größe und zuverlässige Leistung, was sie zu einer ausgezeichneten Wahl für einen privaten Heim-Cloud-Server macht. In Kombination mit NextCloud kann sie als kostengünstiges NAS-System dienen.

**Vorbereitung**

* MicroSD-Karte (16 GB+, Klasse 10 empfohlen)
* Offizielles Raspberry Pi OS (oder Raspberry Pi OS Lite)
* Stabile Netzwerkverbindung (verkabelte Ethernet-Verbindung empfohlen)
* Externe Festplatte oder USB-Stick (für erweiterten Speicher)

**Portainer installieren**

Öffne das Terminal und gebe die folgenden Befehle ein:

1. Docker installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Portainer installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Starte deinen Raspberry Pi neu. (Führe dann die folgenden Schritte **SOFORT** durch.)

4. Nachdem dein Raspberry Pi gestartet ist, öffne einen Webbrowser und rufe deine Portainer-Adresse auf: ``https://<deine-rpi-ip-adresse>:9443``.

5. Standardmäßig erscheint eine Warnung, dass die Seite ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer anerkannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Browser zeigen eine solche Warnung an. In diesem Fall kannst du die Warnung gefahrlos ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png

#. Beim ersten Anmelden musst du ein Administratorkennwort festlegen.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Nach der Registrierung des Administratorkontos gelangst du zur Portainer-Oberfläche. Klicke in der linken Navigationsleiste auf **Settings (Einstellungen) -> General (Allgemein)**, finde **App Templates (Anwendungsvorlagen)** und trage die folgende URL in das Feld ein: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Klicke auf **Save Application Settings (Anwendungseinstellungen speichern)**. Die Konfiguration dauert etwa 10 Sekunden.

**NextCloud installieren**

1. Klicke in der linken Navigationsleiste auf **Home (Startseite) -> local**

   .. image:: img/home_server_app/ptn_home_local.png

2. Gehe zu **Templates (Vorlagen) -> Application (Anwendung)**. Tippe *nextcloud* in die Suchleiste oben rechts und klicke darauf.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. Klicke auf **Deploy the stack (Stack bereitstellen)** und warte, bis die Bereitstellung abgeschlossen ist. Dies dauert in der Regel etwa zwei Minuten.

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. Nach Abschluss ist NextCloud installiert.

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png

**NextCloud verwenden**

1. Öffne deinen Browser und rufe deine NextCloud-Adresse auf: ``https://<deine-rpi-ip-adresse>:32768``.

.. note::

   Ebenso erscheint eine Warnung, dass die Seite ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer anerkannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Browser zeigen eine solche Warnung an.
   In diesem Fall kannst du die Warnung gefahrlos ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png

2. Beim ersten Anmelden musst du ein Administratorkennwort festlegen.

   .. image:: img/home_server_app/nc_admin_install.png

3. Nach der Registrierung kannst du NextCloud nutzen.

   .. image:: img/home_server_app/nc_dashboard.png