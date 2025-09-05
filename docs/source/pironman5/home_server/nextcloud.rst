Einrichtung von NextCloudPi
=======================================

NextCloud ist eine Open-Source-Private-Cloud-Speicherlösung, ähnlich wie Google Drive oder Dropbox. Sie kann verwendet werden, um Dateien zu speichern, Dokumente zu teilen, Fotos zu synchronisieren sowie Kalender und Kontakte zu verwalten.  
Im Gegensatz zu öffentlichen Cloud-Diensten gibt NextCloud den Nutzern die vollständige Kontrolle über ihre Daten, was sie ideal für Einzelpersonen und kleine Teams macht, die Wert auf Privatsphäre und Datensicherheit legen.

Die Pironman5-Serie, betrieben von Raspberry Pi, bietet geringen Stromverbrauch, kompakte Größe und zuverlässige Leistung, was sie zu einer ausgezeichneten Wahl für einen privaten Heim-Cloud-Server macht. In Kombination mit NextCloud kann sie als kostengünstiges NAS-System dienen.


**Vorbereitung**

* MicroSD-Karte (16GB+, Class 10 empfohlen)  
* Offizielles Raspberry Pi Betriebssystem Raspberry Pi OS (oder Raspberry Pi OS Lite)  
* Stabile Netzwerkverbindung (verkabeltes Ethernet empfohlen)  
* Externe Festplatte oder USB-Stick (für erweiterten Speicherplatz)  


**Portainer installieren**

Öffne das Terminal und gib die folgenden Befehle ein:

1. Docker installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Portainer installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Öffne deinen Browser und rufe deine Portainer-Adresse auf: ``http://<your-rpi-ip-address>:9443`` .

.. note::

   Standardmäßig wirst du eine Warnung sehen, dass die Seite ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer bekannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Webbrowser zeigen eine Warnung für solche Zertifikate an.  
   In diesem Fall kannst du die Warnung sicher ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png


4. Beim ersten Login musst du ein Admin-Passwort festlegen.

   .. image:: img/home_server_app/ptn_new_admin.png

5. Nach der Registrierung des Admin-Kontos gelangst du in die Portainer-Oberfläche. Klicke in der linken Navigationsleiste auf **Setting -> General**, finde **App Templates**, und gib die folgende URL in das Feld ein: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Klicke auf **Save Application Settings**. Die Einrichtung dauert etwa 10 Sekunden.


**NextCloud installieren**

1. Klicke in der linken Navigationsleiste auf **Home -> local -> Templates -> Application**. Gib in der Suchleiste oben rechts *nextcloud* ein und klicke darauf.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

2. Klicke auf **Deploy the stack**, und warte, bis die Bereitstellung abgeschlossen ist. Dies dauert in der Regel etwa zwei Minuten.

   .. image:: img/home_server_app/ptn_temp_deploy.png

Nach Abschluss ist NextCloud installiert.


**NextCloud verwenden**

1. Öffne deinen Browser und rufe deine NextCloud-Adresse auf: ``http://<your-rpi-ip-address>:32768`` .

.. note::

   Auch hier wirst du eine Warnung sehen, dass die Seite ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer bekannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Webbrowser zeigen eine Warnung für solche Zertifikate an.  
   In diesem Fall kannst du die Warnung sicher ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png

2. Beim ersten Login musst du ein Admin-Passwort festlegen.

   .. image:: img/home_server_app/nc_admin_install.png

3. Nach der Registrierung kannst du mit der Nutzung von NextCloud beginnen.

   .. image:: img/home_server_app/nc_dashboard.png
