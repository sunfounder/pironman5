.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _remote_desktop:

Fernzugriff auf den Desktop des Raspberry Pi
==================================================

Für diejenigen, die eine grafische Benutzeroberfläche (GUI) gegenüber dem Kommandozeilen-Zugang bevorzugen, unterstützt der Raspberry Pi die Fernzugriff-Funktionalität. Diese Anleitung zeigt Ihnen, wie Sie VNC (Virtual Network Computing) für den Fernzugriff einrichten und verwenden.

Wir empfehlen die Verwendung des `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ zu diesem Zweck.

**VNC-Dienst auf dem Raspberry Pi aktivieren**

Der VNC-Dienst ist im Raspberry Pi OS vorinstalliert, aber standardmäßig deaktiviert. Führen Sie die folgenden Schritte aus, um ihn zu aktivieren:

#. Geben Sie den folgenden Befehl im Terminal des Raspberry Pi ein:

    .. raw:: html

        <run></run>

    .. code-block:: shell

        sudo raspi-config

#. Navigieren Sie mit der Abwärtstaste zu **Interfacing Options** und drücken Sie **Enter**.

    .. image:: img/bookwarm_config_interface.png
        :align: center

#. Wählen Sie **VNC** aus den Optionen aus.

    .. image:: img/bookwarm_vnc.png
        :align: center

#. Wählen Sie mit den Pfeiltasten **<Ja>** -> **<OK>** -> **<Finish>**, um die Aktivierung des VNC-Dienstes abzuschließen.

    .. image:: img/bookwarn_vnc_yes.png
        :align: center

**Anmeldung über VNC Viewer**

#. Laden Sie den `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf Ihren Personal Computer herunter und installieren Sie ihn.

#. Starten Sie nach der Installation den VNC Viewer. Geben Sie den Hostnamen oder die IP-Adresse Ihres Raspberry Pi ein und drücken Sie Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Wenn Sie dazu aufgefordert werden, geben Sie den Benutzernamen und das Passwort Ihres Raspberry Pi ein und klicken Sie auf **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Sie haben nun Zugriff auf die Desktop-Oberfläche Ihres Raspberry Pi.

    .. image:: img/bookwarm.png
        :align: center
