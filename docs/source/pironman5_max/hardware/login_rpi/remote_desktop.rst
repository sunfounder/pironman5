.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_remote_desktop:

Remote-Desktop-Zugriff für Raspberry Pi
==================================================

Für diejenigen, die eine grafische Benutzeroberfläche (GUI) der Kommandozeilenoberfläche vorziehen, unterstützt der Raspberry Pi die Remote-Desktop-Funktion. Diese Anleitung führt dich durch die Einrichtung und Nutzung von VNC (Virtual Network Computing) für den Remote-Zugriff.

Wir empfehlen die Verwendung von `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ für diesen Zweck.

**VNC-Dienst auf dem Raspberry Pi aktivieren**

Der VNC-Dienst ist im Raspberry Pi OS vorinstalliert, jedoch standardmäßig deaktiviert. Folge diesen Schritten, um ihn zu aktivieren:

#. Gib den folgenden Befehl im Raspberry Pi Terminal ein:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navigiere zu **Interfacing Options** mit den Pfeiltasten und drücke **Enter**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%


#. Wähle **VNC** aus den Optionen aus.

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. Verwende die Pfeiltasten, um **<Ja>** -> **<OK>** -> **<Fertig>** auszuwählen und die Aktivierung des VNC-Dienstes abzuschließen.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%


**Anmeldung über VNC Viewer**

#. Lade `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf deinem Computer herunter und installiere es.

#. Starte nach der Installation den VNC Viewer. Gib den Hostnamen oder die IP-Adresse deines Raspberry Pi ein und drücke Enter.

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. Gib, wenn du dazu aufgefordert wirst, den Benutzernamen und das Passwort deines Raspberry Pi ein und klicke auf **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. Jetzt hast du Zugriff auf die Desktop-Oberfläche deines Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%

