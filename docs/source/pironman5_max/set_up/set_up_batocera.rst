.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu Produktankündigungen und Einblicken hinter die Kulissen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_set_up_batocera:

Einrichtung unter Batocera.linux
=========================================================

Wenn du das Betriebssystem Batocera.linux installiert hast, kannst du dich über SSH mit dem System verbinden und die folgenden Schritte ausführen, um die Konfiguration abzuschließen.

#. Sobald das System hochgefahren ist, verbinde dich per SSH mit dem Pironman5. Unter Windows öffnest du **PowerShell**, unter macOS und Linux direkt das **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Der Standard-Hostname des Batocera-Systems lautet ``batocera``, mit dem Benutzernamen ``root`` und dem Passwort ``linux``. Melde dich also mit dem Befehl ``ssh root@batocera.local`` an und gib als Passwort ``linux`` ein.

   .. image:: img/batocera_login.png
      :width: 90%

#. Führe den folgenden Befehl aus, um das Menü zur Dienste-Konfiguration zu öffnen: ``/etc/init.d/S92switch setup``

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Navigiere mit der Pfeil-nach-unten-Taste zum Ende der Liste, wähle den Dienst **Pironman5** aus und aktiviere ihn.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Nachdem du den Dienst pironman5 aktiviert hast, wähle **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Starte den Pironman5 mit folgendem Befehl neu:

   .. code-block:: shell

      reboot

#. Nach dem Neustart wird der Dienst ``pironman5.service`` automatisch gestartet. Die wichtigsten Funktionen des Pironman 5 MAX sind:

   * Das OLED-Display zeigt CPU-, RAM- und Festplattenauslastung, CPU-Temperatur sowie die IP-Adresse des Raspberry Pi an.
   * Vier WS2812-RGB-LEDs leuchten blau im Atemmodus.

   .. note::

     Die RGB-Lüfter drehen sich erst, wenn die Temperatur 60 °C erreicht. Für andere Temperaturgrenzwerte siehe :ref:`max_cc_control_fan`.

Jetzt kannst du den Pironman 5 MAX mit einem Bildschirm, Gamecontrollern, Kopfhörern und mehr verbinden und voll in deine Gamingwelt eintauchen.
