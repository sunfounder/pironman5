.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit Gleichgesinnten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und festlichen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!


Setting up Plex
=======================================

Plex ist eine leistungsstarke Media-Server-Plattform, mit der du deine Filme, TV-Sendungen, Musik und Fotos auf mehreren Geräten organisieren, streamen und abrufen kannst.  
Wenn du Plex auf der Pironman5-Serie mit Raspberry Pi einrichtest, kannst du ein erschwingliches und energieeffizientes Heim-Mediencenter schaffen, das rund um die Uhr läuft.  
Die kompakte Größe, der geringe Stromverbrauch und die Flexibilität des Raspberry Pi machen ihn zu einer ausgezeichneten Wahl für das Hosten von Plex und verwandeln deinen Pi in ein persönliches Entertainment-Hub, das über dein Heimnetzwerk oder sogar aus der Ferne zugänglich ist.


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

   Standardmäßig kann es sein, dass du eine Warnung siehst, dass die Seite ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer bekannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Webbrowser zeigen eine solche Warnung an.  
   In diesem Fall kannst du die Warnung sicher ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png


4. Beim ersten Login wirst du aufgefordert, ein Administrator-Passwort festzulegen.

   .. image:: img/home_server_app/ptn_new_admin.png

5. Nachdem du das Admin-Konto erstellt hast, gelangst du in die Portainer-Oberfläche. Gehe in der linken Navigationsleiste zu **Setting -> General**, finde **App Templates**, und gib die folgende URL in das Feld ein:  
   ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Klicke auf **Save Application Settings**. Die Einrichtung dauert etwa 10 Sekunden.


**Plex installieren**

1. Klicke in der linken Navigationsleiste auf **Home -> local -> Templates -> Application**. Gib in der Suchleiste oben rechts *plex* ein und wähle es aus.

   .. image:: img/home_server_app/ptn_temp_plex.png

2. Stelle den Netzwerkmodus auf **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

3. Erweitere **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

4. Konfiguriere im Abschnitt **volume mapping** die Speicherpfade für deine Mediendateien und gewähre Plex Lese-/Schreibrechte. Die Standardpfade sind ``/portainer/TV`` und ``/portainer/Movies``, beide mit aktiviertem Lese-/Schreibzugriff.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

5. Klicke auf **Deploy** und warte, bis die Installation von Plex abgeschlossen ist.


**Plex Server konfigurieren**

1. Öffne deinen Browser und gib ein: ``http://<your_ip>:32400/`` . Du solltest nun die Plex-Oberfläche sehen.

   .. image:: img/home_server_app/plex_visit.png

2. Überspringe das Premium-Abonnement-Angebot.

3. Als Nächstes siehst du den Bildschirm **Server Setup**. Du kannst *Allow me to access my media outside my home* aktivieren. Es wird jedoch empfohlen, dies zunächst deaktiviert zu lassen und es später bei Bedarf zu konfigurieren.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Danach wirst du aufgefordert, deine Medien zu organisieren. Du kannst *Skip* wählen und Medien später über die Einstellungen hinzufügen. Es wird jedoch empfohlen, direkt die Speicherpfade hinzuzufügen, die du zuvor im Volume Mapping von Portainer eingerichtet hast, sodass Plex deine Medien automatisch scannen und importieren kann.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Wähle den Typ deiner Medienbibliothek, gib deiner Bibliothek einen Namen und wähle die Sprache.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Füge Ordner hinzu. Suche die zuvor eingerichteten Medienspeicherpfade und klicke auf **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Klicke auf **Finish**. Dein Raspberry Pi Plex-Server ist nun vollständig konfiguriert.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Du solltest nun deine Mediendateien auf der Plex-Server-Startseite sehen.

   .. image:: img/home_server_app/plex_index.png
