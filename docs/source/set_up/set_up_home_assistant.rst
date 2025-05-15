.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Erhalten Sie Hilfe bei Problemen und technischen Herausforderungen nach dem Kauf – direkt von unserer Community und unserem Support-Team.
    - **Lernen & Teilen**: Profitieren Sie vom Austausch über Tipps und Tutorials zur Weiterentwicklung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Sichern Sie sich frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Freuen Sie sich auf exklusive Rabatte für unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und besonderen Aktionen zu Feiertagen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Set-up auf Home Assistant
============================================

Wenn Sie Home Assistant bereits installiert haben, müssen Sie die erforderlichen Add-ons hinzufügen und starten, um den Pironman 5 betriebsbereit zu machen.

.. note::

    Die folgende Methode gilt ausschließlich für Systeme mit nativ installiertem Home Assistant. Sie ist nicht für Raspberry Pi Systeme mit nachträglich installiertem Home Assistant oder für Docker-Installationen geeignet.

1. Anmeldung bei Home Assistant
----------------------------------

* Nach dem Start von Pironman 5 empfiehlt es sich, ein Ethernet-Kabel direkt anzuschließen. Öffnen Sie anschließend einen Browser und geben Sie ``homeassistant.local:8123`` ein, um auf Home Assistant zuzugreifen.

  .. image:: img/home_login.png
   :width: 90%


* Wählen Sie **MEIN SMARTES ZUHAUSE ERSTELLEN** und richten Sie anschließend Ihr Benutzerkonto ein.

  .. image:: img/home_account.png
   :width: 90%

* Folgen Sie den Anweisungen zur Auswahl Ihres Standorts und weiterer Einstellungen. Nach Abschluss gelangen Sie zum Home Assistant Dashboard.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Hinzufügen des SunFounder Add-ons Repository
----------------------------------------------------

Die Funktionen des Pironman 5 werden in Home Assistant über Add-ons bereitgestellt. Zunächst müssen Sie das **SunFounder** Add-ons Repository hinzufügen.

#. Navigieren Sie zu **Einstellungen** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Klicken Sie unten rechts auf das Pluszeichen, um den Add-on-Store zu öffnen.

   .. image:: img/home_addon.png
      :width: 90%

#. Öffnen Sie im Add-on-Store das Menü oben rechts und wählen Sie **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Geben Sie die URL des **SunFounder** Add-ons Repository ein: ``https://github.com/sunfounder/home-assistant-addon`` und klicken Sie auf **HINZUFÜGEN**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Nach erfolgreichem Hinzufügen schließen Sie das Pop-up-Fenster und aktualisieren die Seite. Suchen Sie anschließend nach der SunFounder Add-ons Liste.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Installation des **Pi Config Wizard** Add-ons
-------------------------------------------------------

Der **Pi Config Wizard** hilft bei der Konfiguration wichtiger Funktionen wie I2C und SPI für den Pironman 5. Wenn er später nicht mehr benötigt wird, kann er wieder entfernt werden.

#. Suchen Sie in der SunFounder Add-ons Liste den **Pi Config Wizard** und klicken Sie darauf.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Klicken Sie auf der Seite des **Pi Config Wizard** auf **INSTALLIEREN** und warten Sie, bis der Vorgang abgeschlossen ist.

   .. image:: img/home_config_install.png
      :width: 90%

#. Nach der Installation wechseln Sie zur **Protokoll**-Seite, um etwaige Fehlermeldungen zu überprüfen.

   .. image:: img/home_log.png
      :width: 90%

#. Wenn keine Fehler vorliegen, kehren Sie zur **Info**-Seite zurück und klicken Sie auf **STARTEN**, um das Add-on zu aktivieren.

   .. image:: img/home_start.png
      :width: 90%

#. Öffnen Sie nun die WEB-UI.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. In der Web-UI finden Sie die Option zum Einbinden der Boot-Partition. Klicken Sie auf **EINBINDEN**, um sie zu mounten.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Nach erfolgreichem Mounten erscheinen Optionen zum Aktivieren von I2C und SPI sowie zum Bearbeiten der Datei config.txt. Aktivieren Sie I2C und SPI. Sobald die Aktivierung bestätigt ist, klicken Sie auf **NEUSTART**, um den Raspberry Pi neu zu starten.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Nach dem Neustart aktualisieren Sie die Seite. Sie kehren erneut zur Einbindungsseite zurück. Klicken Sie wieder auf **EINBINDEN**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. In der Regel ist SPI jetzt aktiviert, während I2C möglicherweise noch deaktiviert ist, da dafür zwei Neustarts erforderlich sind. Aktivieren Sie I2C erneut und starten Sie den Raspberry Pi nochmals neu.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Nach dem zweiten Neustart öffnen Sie erneut die **EINBINDEN**-Seite. Nun sollten sowohl I2C als auch SPI als aktiviert angezeigt werden.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Falls Sie nach der Seitenaktualisierung nicht zur Einbindungsseite weitergeleitet werden, gehen Sie zu **Einstellungen** -> **Add-ons** -> **Pi Config Wizard**.
    * Prüfen Sie, ob das Add-on läuft. Falls nicht, klicken Sie auf **STARTEN**.
    * Anschließend auf **WEB-UI ÖFFNEN** und dann auf **EINBINDEN** klicken, um zu überprüfen, ob I2C und SPI aktiviert sind.

4. Installation des **Pironman 5** Add-ons
----------------------------------------------

Jetzt können Sie das **Pironman 5** Add-on installieren.

#. Gehen Sie zu **Einstellungen** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Klicken Sie unten rechts auf das Pluszeichen, um den Add-on-Store zu öffnen.

   .. image:: img/home_addon.png
      :width: 90%

#. Suchen Sie in der **SunFounder** Add-ons Liste nach **Pironman 5** und klicken Sie darauf.

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Installieren Sie nun das Add-on Pironman 5.

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. Nach Abschluss der Installation klicken Sie auf **STARTEN**, um das Add-on zu aktivieren. Das OLED-Display zeigt dann Informationen wie CPU-Auslastung und Temperatur des Raspberry Pi an. Die vier WS2812 RGB-LEDs leuchten im blauen Atemmodus.

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. Klicken Sie auf **WEB-UI ÖFFNEN**, um die Webseite von Pironman 5 zu öffnen. Sie können optional die Anzeige der Web-UI in der Seitenleiste aktivieren. So sehen Sie die Pironman 5 Option direkt in der linken Seitenleiste von Home Assistant und haben schnellen Zugriff.

   .. image:: img/home_web_ui.png
      :width: 90%

#. Auf der Webseite können Sie Informationen zum Raspberry Pi einsehen, die RGB-LEDs konfigurieren, den Lüfter steuern und weitere Einstellungen vornehmen.

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

    Weitere Informationen zur Nutzung der Pironman 5 Webseite finden Sie unter: :ref:`view_control_dashboard`.

