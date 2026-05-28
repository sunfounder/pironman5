.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Set-up unter Home Assistant
============================================

Wenn du das Home Assistant-System installiert hast, musst du die erforderlichen Add-ons hinzufügen und starten, um den Pironman 5 MAX vollständig nutzen zu können.

.. note::

    Die folgende Methode gilt nur für Systeme mit nativer Home Assistant-Installation. Sie ist nicht für Systeme gedacht, bei denen Home Assistant über ein bestehendes Raspberry-Pi-System installiert wurde oder in einer Docker-Version läuft.

1. Anmeldung bei Home Assistant
-------------------------------------

* Nach dem Start des Pironman 5 MAX empfiehlt es sich, direkt ein Ethernet-Kabel anzuschließen. Öffne dann einen Browser auf deinem Computer und rufe ``homeassistant.local:8123`` auf, um Home Assistant zu erreichen.

  .. image:: img/home_login.png
   :width: 90%


* Wähle **CREATE MY SMART HOME** und erstelle dein Konto.

  .. image:: img/home_account.png
   :width: 90%

* Folge den Anweisungen zur Auswahl deines Standorts und weiterer Einstellungen. Danach gelangst du zum Dashboard von Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Hinzufügen des SunFounder-Add-on-Repositories
----------------------------------------------------

Die Funktionen des Pironman 5 MAX werden in Home Assistant über Add-ons bereitgestellt. Zuerst musst du das **SunFounder**-Add-on-Repository hinzufügen.

#. Öffne **Einstellungen** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Klicke unten rechts auf das Pluszeichen, um den Add-on-Store zu öffnen.

   .. image:: img/home_addon.png
      :width: 90%

#. Klicke im Add-on-Store oben rechts auf das Menü und wähle **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Gib die URL des **SunFounder**-Add-on-Repositories ein: ``https://github.com/sunfounder/home-assistant-addon`` und klicke auf **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Nach erfolgreichem Hinzufügen schließe das Fenster und aktualisiere die Seite. Du solltest nun die Add-ons von SunFounder sehen.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Installation des **Pi Config Wizard** Add-ons
------------------------------------------------------

Der **Pi Config Wizard** hilft dir, für den Pironman 5 MAX benötigte Funktionen wie I2C und SPI zu aktivieren. Nach der Einrichtung kann das Add-on wieder entfernt werden.

#. Wähle in der Liste der SunFounder-Add-ons **Pi Config Wizard** aus.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Klicke auf der **Pi Config Wizard**-Seite auf **INSTALL**. Warte, bis die Installation abgeschlossen ist.

   .. image:: img/home_config_install.png
      :width: 90%

#. Wechsle danach auf die Seite **Log**, um sicherzustellen, dass keine Fehler aufgetreten sind.

   .. image:: img/home_log.png
      :width: 90%

#. Wenn keine Fehler angezeigt werden, kehre zur Seite **Info** zurück und klicke auf **START**, um das Add-on zu starten.

   .. image:: img/home_start.png
      :width: 90%

#. Öffne jetzt die WEB-Oberfläche.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. In der Web-Oberfläche kannst du die Boot-Partition einhängen, indem du auf **MOUNT** klickst.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Danach kannst du I2C und SPI aktivieren. Sobald beide als aktiviert angezeigt werden, klicke unten auf REBOOT, um den Raspberry Pi neu zu starten.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Nach dem Neustart aktualisiere die Seite und klicke erneut auf **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. In der Regel wird SPI sofort aktiviert, I2C jedoch erst nach einem zweiten Neustart. Aktiviere I2C erneut und starte das Gerät erneut.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Danach siehst du beim erneuten Öffnen der Seite, dass sowohl I2C als auch SPI aktiviert sind.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Wenn nach dem Aktualisieren der Seite die Mount-Seite nicht erscheint, gehe zu **Einstellungen** -> **Add-ons** -> **Pi Config Wizard**.
    * Überprüfe, ob das Add-on gestartet ist. Falls nicht, klicke auf **START**.
    * Öffne dann die **WEB-Oberfläche** erneut und klicke auf **MOUNT**, um den Status von I2C und SPI zu prüfen.

4. Installation des **Pironman 5 MAX** Add-ons
-------------------------------------------------

Nun kannst du das Add-on **Pironman 5 MAX** installieren.

#. Öffne **Einstellungen** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Klicke unten rechts auf das Pluszeichen, um den Add-on-Store zu öffnen.

   .. image:: img/home_addon.png
      :width: 90%

#. Suche in der Liste der **SunFounder**-Add-ons nach **Pironman 5 MAX** und öffne es.

   .. image:: img/home_pironman5_max_addon.png
      :width: 90%

#. Installiere das Add-on nun durch Klick auf INSTALL.

   .. image:: img/home_pironman5_max_addon_install.png

#. Nach erfolgreicher Installation klicke auf **START**, um den Dienst zu starten. Auf dem OLED-Display erscheinen nun CPU-Temperatur und weitere Informationen. Vier WS2812-RGB-LEDs leuchten im blauen Atemmodus.

   .. image:: img/home_pironman5_max_addon_start.png
      :width: 90%

#. Klicke anschließend auf **OPEN WEB UI**, um die Pironman 5 MAX-Weboberfläche zu öffnen. Aktiviere optional die Sidebar-Anzeige, um den Zugriff zu erleichtern.

   .. image:: img/home_pironman5_max_webui.png
      :width: 90%

#. Jetzt kannst du Systeminformationen einsehen, RGB konfigurieren, den Lüfter steuern und vieles mehr.

   .. image:: img/home_web.png
      :width: 90%

.. note::

    Weitere Informationen zur Nutzung der Pironman 5 MAX-Weboberfläche findest du unter: :ref:`view_control_dashboard`.


.. note::

   Zu diesem Zeitpunkt haben Sie den Pironman 5 MAX erfolgreich eingerichtet, und er ist einsatzbereit.
   
   Für die erweiterte Steuerung seiner Komponenten siehe bitte :ref:`control_commands_dashboard_max`.
