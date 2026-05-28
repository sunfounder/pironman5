.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_batocera:

Einrichtung auf Batocera.linux
=========================================================

Wenn Sie das Batocera.linux Betriebssystem installiert haben, können Sie sich per SSH mit diesem System verbinden und dann die folgenden Schritte ausführen, um die Konfiguration abzuschließen.

#. Sobald das System hochgefahren ist, verwenden Sie ssh, um sich aus der Ferne mit Pironman5 zu verbinden. Unter Windows können Sie **Powershell** öffnen, während Sie unter Mac OS X und Linux direkt **Terminal** öffnen können.

   .. image:: img/batocera_powershell.png
      :width: 90%
      

#. Der Standard-Hostname für das Batocera-System lautet ``batocera``, mit dem Standardbenutzernamen ``root`` und dem Passwort ``linux``. Daher können Sie sich mit dem Befehl ``ssh root@batocera.local`` anmelden und das Passwort ``linux`` eingeben.

   .. image:: img/batocera_login.png
      :width: 90%

#. Führen Sie den Befehl ``/etc/init.d/S92switch setup`` aus, um die Einstellungsseite des Menüs aufzurufen.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Verwenden Sie die Abwärtspfeiltaste, um nach unten zu navigieren, und aktivieren Sie die **Pironman5**-Dienste.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Nachdem Sie den Pironman5-Dienst aktiviert haben, wählen Sie **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Führen Sie den Befehl ``reboot`` aus, um Pironman5 neu zu starten.

   .. code-block:: shell

      reboot

#. Nach dem Neustart wird der Dienst ``pironman5.service`` automatisch gestartet. Hier sind die Hauptkonfigurationen für den Pironman 5:

   * Das OLED-Display zeigt CPU, RAM, Festplattennutzung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.
   * Vier WS2812 RGB-LEDs leuchten in einem blauen Atemmodus.
   * Die GPIO-Lüfter sind standardmäßig auf den Modus **ausgewogen** eingestellt. Für andere Temperaturgrenzwerte siehe :ref:`cc_control_fan_max`.


Nun können Sie den Pironman 5 mit einem Bildschirm, Gamecontrollern, Kopfhörern und vielem mehr verbinden, um in Ihre Gaming-Welt einzutauchen.

.. note::

   Zu diesem Zeitpunkt haben Sie den Pironman 5 erfolgreich eingerichtet, und er ist einsatzbereit.
   
   Für die erweiterte Steuerung seiner Komponenten siehe bitte :ref:`view_control_commands_5`.
