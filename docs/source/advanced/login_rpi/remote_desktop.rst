.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _remote_desktop:

Fernzugriff auf den Desktop für Raspberry Pi
==================================================

Für diejenigen, die eine grafische Benutzeroberfläche (GUI) dem Zugriff über die Befehlszeile vorziehen, unterstützt der Raspberry Pi die Remote-Desktop-Funktionalität. In dieser Anleitung erfahren Sie, wie Sie VNC (Virtual Network Computing) für den Fernzugriff einrichten und verwenden.

Wir empfehlen die Verwendung von `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ für diesen Zweck.

**Aktivieren des VNC-Dienstes auf dem Raspberry Pi**

Der VNC-Dienst ist im Raspberry Pi OS vorinstalliert, aber standardmäßig deaktiviert. Folgen Sie diesen Schritten, um ihn zu aktivieren:

#. Geben Sie den folgenden Befehl im Raspberry Pi-Terminal ein:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navigieren Sie mit der Pfeiltaste nach unten zu **Interfacing Options** und drücken Sie **Enter**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. Wählen Sie **VNC** aus den Optionen.

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. Verwenden Sie die Pfeiltasten, um **<Ja>** -> **<OK>** -> **<Beenden>** auszuwählen und die Aktivierung des VNC-Dienstes abzuschließen.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**Anmeldung über den VNC Viewer**

#. Laden Sie `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ herunter und installieren Sie ihn auf Ihrem Computer.

#. Nach der Installation starten Sie den VNC Viewer. Geben Sie den Hostnamen oder die IP-Adresse Ihres Raspberry Pi ein und drücken Sie Enter.

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. Geben Sie bei Aufforderung Ihren Benutzernamen und Ihr Passwort für den Raspberry Pi ein und klicken Sie auf **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. Sie haben nun Zugriff auf die Desktop-Oberfläche Ihres Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%
      
