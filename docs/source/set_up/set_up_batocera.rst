.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Löse technische Probleme und Herausforderungen nach dem Kauf mit Hilfe unseres Teams und der Community.
    - **Lernen & Teilen**: Teile Tipps und Anleitungen, um dein Wissen zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugriff auf Produktneuheiten und exklusive Einblicke.
    - **Sonderrabatte**: Sichere dir exklusive Rabatte auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an Verlosungen und besonderen Aktionen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und kreativ zu werden? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _set_up_batocera:

Einrichtung unter Batocera.linux
=========================================================

Wenn du das Betriebssystem Batocera.linux installiert hast, kannst du dich über SSH mit dem System verbinden und anschließend die folgenden Schritte ausführen, um die Konfiguration abzuschließen.

#. Sobald das System gestartet ist, stelle per SSH eine Verbindung zum Pironman 5 her. Unter Windows kannst du **PowerShell** öffnen, unter macOS und Linux direkt das **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Der Standard-Hostname für Batocera lautet ``batocera``, mit dem Standard-Benutzernamen ``root`` und dem Passwort ``linux``. Du kannst dich also mit dem Befehl ``ssh root@batocera.local`` anmelden und das Passwort ``linux`` eingeben.

   .. image:: img/batocera_login.png
      :width: 90%

#. Führen Sie den Befehl ``/etc/init.d/S92switch setup`` aus, um das Konfigurationsmenü aufzurufen.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Navigiere mit der Pfeil-nach-unten-Taste zum Ende des Menüs, wähle dort **Pironman5** aus und aktiviere den Dienst.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Nachdem der Dienst aktiviert wurde, wähle **OK**, um fortzufahren.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Geben Sie den Befehl ``reboot`` ein, um den Pironman 5 neu zu starten.

   .. code-block:: shell

      reboot

#. Nach dem Neustart wird der Dienst ``pironman5.service`` automatisch gestartet. Die wichtigsten Funktionen sind:

   * Das OLED-Display zeigt CPU-Auslastung, RAM-Nutzung, Festplattenauslastung, CPU-Temperatur sowie die IP-Adresse des Raspberry Pi an.
   * Vier WS2812-RGB-LEDs leuchten im blauen Atemmodus.

   .. note::

     Der RGB-Lüfter dreht sich erst, wenn die Temperatur 60 °C erreicht. Für andere Schwellenwerte siehe :ref:`cc_control_fan`.


Jetzt kannst du deinen Pironman 5 mit einem Bildschirm, Gamepads, Kopfhörern und anderen Geräten verbinden und in dein Retro-Gaming-Erlebnis eintauchen.

