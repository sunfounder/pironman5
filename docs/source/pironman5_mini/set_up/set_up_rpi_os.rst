.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum der Community beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitig Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Genieße exklusive Preisnachlässe auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an festlichen Aktionen und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu erschaffen? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!


Konfiguration unter Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

Wenn du Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf deinem Raspberry Pi installiert hast, musst du den Pironman 5 Mini über die Befehlszeile konfigurieren. Nachfolgend findest du detaillierte Anleitungen.

.. note::

  Bevor du mit der Konfiguration fortfährst, musst du deinen Raspberry Pi starten und dich anmelden.  
  Wenn du dir nicht sicher bist, wie du dich anmeldest, kannst du die offizielle Website von Raspberry Pi besuchen: |link_rpi_get_start|.


Konfiguration des Herunterfahrens zur Deaktivierung der GPIO-Stromversorgung
------------------------------------------------------------------------------

Um zu verhindern, dass der über den GPIO des Raspberry Pi gespeiste RGB-Lüfter nach dem Herunterfahren weiterläuft, ist es wichtig, den Raspberry Pi so zu konfigurieren, dass die GPIO-Stromversorgung deaktiviert wird.

#. Öffne das EEPROM-Konfigurationstool:

   .. code-block::

      sudo raspi-config

#. Gehe zu **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Wähle **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Speichere die Änderungen. Du wirst aufgefordert, einen Neustart durchzuführen, damit die neuen Einstellungen wirksam werden.


Download und Installation des Moduls ``pironman5``
-----------------------------------------------------------

.. note::

   Für „Lite“-Systeme installiere zunächst Werkzeuge wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Lade den Code von GitHub herunter und installiere das Modul ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Nach einer erfolgreichen Installation muss das System neu gestartet werden, um die Installation zu aktivieren. Folge der Aufforderung auf dem Bildschirm, um den Neustart durchzuführen.

   Nach dem Neustart wird der Dienst ``pironman5.service`` automatisch gestartet.  
   Hier sind die Hauptkonfigurationen des Pironman 5 Mini:
   
   * Vier WS2812-RGB-LEDs leuchten blau mit einem Atemeffekt.
     
   .. note::
    
     * Die RGB-Lüfter sind standardmäßig auf **Always On** eingestellt.  
       Um unterschiedliche Einschalttemperaturen festzulegen, siehe :ref:`cc_control_fan_mini`.

#. Du kannst das Tool ``systemctl`` verwenden, um den Dienst ``pironman5.service`` zu ``starten``, ``stoppen``, ``neustarten`` oder seinen ``Status`` zu überprüfen.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Verwende diesen Befehl, um Änderungen an den Pironman-5-Mini-Einstellungen zu übernehmen.  
   * ``start/stop``: Aktiviert oder deaktiviert den Dienst ``pironman5.service``.  
   * ``status``: Überprüft den Betriebsstatus des Programms ``pironman5`` mithilfe des Tools ``systemctl``.

.. note::

   An diesem Punkt hast du den Pironman 5 Mini erfolgreich konfiguriert, und er ist einsatzbereit.  
   Für die erweiterte Steuerung seiner Komponenten siehe :ref:`control_commands_dashboard_mini`.
