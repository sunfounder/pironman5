.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Konfiguration von Plex
=======================================

Plex ist eine leistungsstarke Medien-Server-Plattform, die es Ihnen ermöglicht, Ihre Filme, TV-Serien, Musik und Fotos auf mehreren Geräten zu organisieren, zu streamen und darauf zuzugreifen.
Durch die Einrichtung von Plex auf der Raspberry Pi-gesteuerten Pironman5-Serie können Sie ein kostengünstiges, energieeffizientes und rund um die Uhr laufendes Heim-Medienzentrum einrichten.
Die kompakte Größe, der niedrige Energieverbrauch und die Flexibilität des Raspberry Pi machen ihn zu einer hervorragenden Wahl für das Hosten von Plex und verwandeln Ihren Pi in einen persönlichen Unterhaltungs-Hub, auf den Sie über Ihr Heimnetzwerk oder sogar aus der Ferne zugreifen können.

**Vorbereitung**

* MicroSD-Karte (16 GB+, Klasse 10 empfohlen)
* Offizielles Raspberry Pi OS (oder Raspberry Pi OS Lite)
* Stabile Netzwerkverbindung (verkabelte Ethernet-Verbindung empfohlen)
* Externe Festplatte oder USB-Stick (für erweiterten Speicher)

**Portainer installieren**

Öffnen Sie das Terminal und geben Sie die folgenden Befehle ein:

1. Docker installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Portainer installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Starten Sie Ihren Raspberry Pi neu. (Führen Sie dann die folgenden Schritte **SOFORT** aus.)

4. Nachdem Ihr Raspberry Pi gestartet ist, öffnen Sie einen Webbrowser und besuchen Sie Ihre Portainer-Adresse: ``http://<Ihre-RPi-IP-Adresse>:9443``.

5. Standardmäßig sehen Sie eine Warnung, dass die Website ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer anerkannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Browser zeigen eine solche Warnung an. In diesem Fall können Sie sie gefahrlos ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png

#. Bei Ihrer ersten Anmeldung müssen Sie ein Administratorkennwort festlegen.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Nachdem Sie das Administratorkonto erstellt haben, gelangen Sie zur Portainer-Oberfläche. Gehen Sie in der linken Navigationsleiste zu **Settings (Einstellungen) -> General (Allgemein)**, suchen Sie **App Templates (Anwendungsvorlagen)** und geben Sie die folgende URL in das Feld ein: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Klicken Sie auf **Save Application Settings (Anwendungseinstellungen speichern)**. Die Konfiguration dauert etwa 10 Sekunden.

**Plex installieren**

1. Klicken Sie in der linken Navigationsleiste auf **Home (Startseite) -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2. Gehen Sie zu **Templates (Vorlagen) -> Application (Anwendung)**. Geben Sie *plex* in die Suchleiste oben rechts ein und klicken Sie darauf.

   .. image:: img/home_server_app/ptn_temp_plex.png

#. Setzen Sie den Netzwerkmodus auf **host (Host)**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

#. Klappen Sie **Show advanced options (Erweiterte Optionen anzeigen)** auf.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#. Im Abschnitt **volume mapping (Volume-Zuordnung)** konfigurieren Sie die Speicherpfade für Ihre Mediendateien und erteilen Sie Plex Lese-/Schreibberechtigungen. Die Standardpfade sind ``/portainer/TV`` und ``/portainer/Movies``, beide mit aktiviertem Lese-/Schreibzugriff.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#. Klicken Sie auf **Deploy (Bereitstellen)** und warten Sie, bis die Installation von Plex abgeschlossen ist.

**Plex-Server konfigurieren**

1. Öffnen Sie Ihren Browser und geben Sie ein: ``http://<Ihre_IP>:32400/web`` . Sie sollten nun die Plex-Oberfläche sehen.

   .. image:: img/home_server_app/plex_visit.png

2. Überspringen Sie das Premium-Abonnement-Angebot.

3. Als nächstes sehen Sie den **Server Setup (Server-Einrichtungs)**-Bildschirm. Sie können *Allow me to access my media outside my home (Mir erlauben, auf meine Medien außerhalb meines Zuhauses zuzugreifen)* aktivieren. Es wird jedoch empfohlen, diese Option vorerst deaktiviert zu lassen und sie später bei Bedarf zu konfigurieren.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Anschließend werden Sie aufgefordert, Ihre Medien zu organisieren. Sie können *Skip (Überspringen)* wählen und Medien später über die Einstellungen hinzufügen. Es wird jedoch empfohlen, die Speicherpfade, die Sie in der Volume-Zuordnung von Portainer konfiguriert haben, direkt hinzuzufügen, damit Plex Ihre Medien automatisch scannen und importieren kann.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Wählen Sie den Typ Ihrer Medienbibliothek aus, geben Sie Ihrer Bibliothek einen Namen und wählen Sie die Sprache.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Fügen Sie Ordner hinzu. Navigieren Sie zu den zuvor definierten Speicherpfaden Ihrer Medien und klicken Sie auf **Add Library (Bibliothek hinzufügen)**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Klicken Sie auf **Finish (Beenden)**. Ihr Plex-Server auf dem Raspberry Pi ist nun vollständig eingerichtet.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Sie sollten nun Ihre Mediendateien auf der Startseite des Plex-Servers angezeigt sehen.

   .. image:: img/home_server_app/plex_index.png