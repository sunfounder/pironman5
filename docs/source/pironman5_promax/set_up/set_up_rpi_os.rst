.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_pi_os:

Einrichtung unter Raspberry Pi/Ubuntu/Kali/Homebridge OS
=======================================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Wenn Sie Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf Ihrem Raspberry Pi installiert haben, müssen Sie den Pironman 5 Pro MAX über die Befehlszeile konfigurieren. Ausführliche Tutorials finden Sie unten:

.. note::

  Bevor Sie mit der Konfiguration beginnen, müssen Sie Ihren Raspberry Pi hochfahren und sich anmelden. Wenn Sie nicht wissen, wie Sie sich anmelden, besuchen Sie die offizielle Raspberry Pi-Website: |link_rpi_get_start|.


Konfigurieren des Herunterfahrens zur Deaktivierung der GPIO-Stromversorgung
----------------------------------------------------------------------------------------------------------------------------

Um zu verhindern, dass der OLED-Bildschirm und die RGB-Lüfter, die über die GPIOs des Raspberry Pi mit Strom versorgt werden, nach dem Herunterfahren aktiv bleiben, ist es wichtig, den Raspberry Pi für die Deaktivierung der GPIO-Stromversorgung zu konfigurieren.

#. Öffnen Sie das EEPROM-Konfigurationstool:

   .. code-block::

      sudo raspi-config

#. Navigieren Sie zu **Erweiterte Optionen → A12 Herunterfahrmodus**.

   .. image:: img/shutdown_behaviour.png

#. Wählen Sie **B1 Vollständige Abschaltung**.

   .. image:: img/run_power_off.png

#. Speichern Sie die Änderungen. Sie werden aufgefordert, neu zu starten, damit die neuen Einstellungen wirksam werden.


.. _promax_download_pironman5_module:

Herunterladen und Installieren des Moduls ``pironman5``
-----------------------------------------------------------

.. .. note::

..    Installieren Sie für Lite-Systeme zunächst Tools wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. Laden Sie den Code von GitHub herunter und installieren Sie das Modul ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Nach erfolgreicher Installation ist ein Systemneustart erforderlich, um die Installation zu aktivieren. Folgen Sie der entsprechenden Aufforderung auf dem Bildschirm.

   Nach dem Neustart wird der ``pironman5.service`` automatisch gestartet. Hier sind die primären Konfigurationen für den Pironman 5 Pro MAX:

   * Der OLED-Bildschirm zeigt CPU, RAM, Festplattenauslastung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.
   * Vier WS2812-RGB-LEDs leuchten blau im Atmungsmodus.

#. Sie können das ``systemctl``-Werkzeug verwenden, um den ``pironman5.service`` zu ``starten``, zu ``stoppen``, ``neu zu starten`` oder den ``Status`` zu überprüfen.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``: Verwenden Sie diesen Befehl, um alle Änderungen an den Einstellungen des Pironman 5 Pro MAX zu übernehmen.
   * ``start/stop``: Aktivieren oder deaktivieren Sie den ``pironman5.service``.
   * ``status``: Überprüfen Sie den Betriebsstatus des ``pironman5``-Programms mit dem ``systemctl``-Werkzeug.

.. note::

   An diesem Punkt haben Sie den Pironman 5 Pro MAX erfolgreich eingerichtet und er ist einsatzbereit.

   Informationen zur erweiterten Steuerung seiner Komponenten finden Sie unter :ref:`control_commands_dashboard_promax`.