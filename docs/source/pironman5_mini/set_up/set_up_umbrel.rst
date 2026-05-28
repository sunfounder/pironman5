.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_umbrel_mini:

Konfiguration unter Umbrel OS
======================================================================

Wenn du Umbrel OS auf deinem Raspberry Pi 5 installiert hast, musst du den Pironman 5 Mini über die Befehlszeile konfigurieren. Nachfolgend findest du die detaillierten Anweisungen:

#. Verbinde deinen Raspberry Pi 5 über ein Ethernet-Kabel mit dem Netzwerk. Dieser Schritt ist entscheidend, um sicherzustellen, dass der Raspberry Pi Zugriff auf das Internet hat.

#. Öffne in deinem Browser: ``http://umbrel.local``.  
   Wenn die Seite nicht geöffnet wird, überprüfe im Router die IP-Adresse deines Umbrel-Geräts, z. B.: ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Erstelle dein Umbrel-Konto, indem du einen Benutzernamen und ein Passwort festlegst.  
   Dieses Passwort wird für zukünftige Remote-Anmeldungen bei Umbrel verwendet, also merke es dir gut.

   .. image:: img/umbrel_account.png

#. Klicke auf **Next**, um die Einrichtung von Umbrel abzuschließen und in die Desktop-Umgebung zu gelangen.

   .. image:: img/umbrel_desktop.png

#. Öffne das Terminal. Klicke auf dem Desktop auf das Symbol **Settings**, wähle **Advanced Settings** und klicke dann auf **Open**.

   .. image:: img/umbrel_setting.png

#. Klicke auf **Open Terminal**.

   .. image:: img/umbrel_open_terminal.png

#. Du kannst wählen, ob du das Terminal direkt in Umbrel OS oder innerhalb einer bestimmten App öffnen möchtest. Beide Optionen führen dich zur Terminaloberfläche.

   .. image:: img/umbrel_terminal.png

#. Lade den Code von GitHub herunter und installiere das Modul ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Nach Abschluss der Installation führe den folgenden Befehl aus, um deinen Raspberry Pi neu zu starten.

   .. code-block:: shell

      sudo reboot

#. Nach dem Neustart wird der Dienst ``pironman5.service`` automatisch gestartet.  
   Hier sind die Hauptkonfigurationen des Pironman 5 Mini:
   
   * Vier WS2812-RGB-LEDs leuchten blau mit einem Atemeffekt.  
   * Die RGB-Lüfter sind standardmäßig auf den Modus **Always On** eingestellt. Für unterschiedliche Einschalttemperaturen siehe :ref:`cc_control_fan_mini`.

#. Du kannst das Tool ``systemctl`` verwenden, um den Dienst ``pironman5.service`` zu ``starten``, ``stoppen``, ``neustarten`` oder seinen ``Status`` zu überprüfen.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Verwende diesen Befehl, um Änderungen an den Pironman-5-Mini-Einstellungen zu übernehmen.  
   * ``start/stop``: Aktiviert oder deaktiviert den Dienst ``pironman5.service``.  
   * ``status``: Überprüft den Betriebsstatus des Programms ``pironman5`` mithilfe des Tools ``systemctl``.

.. note::

   An diesem Punkt hast du den Pironman 5 Mini erfolgreich konfiguriert, und er ist einsatzbereit.  
   Für die erweiterte Steuerung seiner Komponenten siehe :ref:`control_commands_dashboard_mini`.
