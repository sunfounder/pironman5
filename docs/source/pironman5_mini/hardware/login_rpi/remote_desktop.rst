.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Entdecke gemeinsam mit anderen Technikbegeisterten noch mehr über Raspberry Pi, Arduino und ESP32.

    **Warum solltest du beitreten?**

    - **Expertenhilfe**: Erhalte Unterstützung bei technischen Problemen und Fragen nach dem Kauf – direkt durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um dein Wissen zu erweitern.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produkten und erhalte exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an saisonalen Gewinnspielen und Aktionen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und kreativ zu werden? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _remote_desktop_mini:

Fernzugriff auf den Raspberry Pi per Remote-Desktop
=========================================================

Für alle, die lieber mit einer grafischen Benutzeroberfläche (GUI) als über die Kommandozeile arbeiten, bietet der Raspberry Pi die Möglichkeit zum Remote-Desktop-Zugriff. Diese Anleitung zeigt dir, wie du VNC (Virtual Network Computing) einrichtest und verwendest.

Wir empfehlen die Nutzung des `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_.

**VNC-Dienst auf dem Raspberry Pi aktivieren**

Der VNC-Dienst ist in Raspberry Pi OS vorinstalliert, jedoch standardmäßig deaktiviert. Folge diesen Schritten, um ihn zu aktivieren:

#. Gib im Terminal des Raspberry Pi folgenden Befehl ein:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navigiere mit der Pfeiltaste nach unten zu **Interfacing Options** und bestätige mit **Enter**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%


#. Wähle **VNC** aus der Liste.

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. Verwende die Pfeiltasten, um **<Yes>** -> **<OK>** -> **<Finish>** auszuwählen und den VNC-Dienst zu aktivieren.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%


**Anmeldung über VNC Viewer**

#. Lade `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ herunter und installiere ihn auf deinem Computer.

#. Starte VNC Viewer nach der Installation. Gib den Hostnamen oder die IP-Adresse deines Raspberry Pi ein und drücke Enter.

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. Gib den Benutzernamen und das Passwort deines Raspberry Pi ein und klicke auf **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. Nun erhältst du Zugriff auf die Desktop-Oberfläche deines Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%

