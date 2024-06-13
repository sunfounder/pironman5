.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Pironman 5 auf Home Assistant einrichten
============================================

1. Anmeldung bei Home Assistant
----------------------------------

* Nach dem Start von Pironman 5 wird empfohlen, direkt ein Ethernet-Kabel anzuschließen. So können Sie Ihren Computer-Browser öffnen und eingeben: ``homeassistant.local:8123``, um auf Home Assistant zuzugreifen.

.. image:: img/home_login.png

* Wählen Sie **CREATE MY SMART HOME** und erstellen Sie dann Ihr Konto.

.. image:: img/home_account.png

* Folgen Sie den Anweisungen, um Ihren Standort und andere Konfigurationen auszuwählen. Nach Abschluss gelangen Sie zum Home Assistant Dashboard.

.. image:: img/home_dashboard.png


2. Das SunFounder Add-ons Repository hinzufügen
----------------------------------------------------

Die Funktionalität von Pironman 5 wird auf Home Assistant in Form von Add-ons installiert. Zuerst müssen Sie das **SunFounder** Add-ons Repository hinzufügen.

#. Öffnen Sie **Einstellungen** -> **Add-ons**.

    .. image:: img/home_setting_addon.png

#. Klicken Sie auf das Pluszeichen in der unteren rechten Ecke, um den Add-on-Store zu öffnen.

    .. image:: img/home_addon.png

#. Klicken Sie im Add-on-Store auf das Menü in der oberen rechten Ecke und wählen Sie **Repositories**.

    .. image:: img/home_add_res.png

#. Geben Sie die URL des **SunFounder** Add-ons Repository ein: ``https://github.com/sunfounder/home-assistant-addon``, und klicken Sie auf **ADD**.

    .. image:: img/home_res_add.png

#. Nach erfolgreichem Hinzufügen schließen Sie das Pop-up-Fenster und aktualisieren Sie die Seite. Finden Sie die SunFounder Add-ons Liste.

    .. image:: img/home_addon_list.png
        
3. Installieren Sie das **Pi Config Wizard** Add-on
------------------------------------------------------

Der **Pi Config Wizard** kann helfen, die für Pironman 5 erforderlichen Konfigurationen wie I2C und SPI zu aktivieren. Wenn er danach nicht mehr benötigt wird, kann er entfernt werden.

#. Finden Sie **Pi Config Wizard** in der SunFounder Add-ons Liste und klicken Sie darauf.

    .. image:: img/home_pi_config.png
    
#. Klicken Sie auf der **Pi Config Wizard** Seite auf **INSTALL**. Warten Sie, bis die Installation abgeschlossen ist.

    .. image:: img/home_config_install.png

#. Nach Abschluss der Installation wechseln Sie zur **Log** Seite, um zu überprüfen, ob Fehler vorliegen.

    .. image:: img/home_log.png
    
#. Wenn keine Fehler vorliegen, kehren Sie zur **Info** Seite zurück und klicken Sie auf **START**, um dieses Add-on zu starten.

    .. image:: img/home_start.png
    
#. Öffnen Sie nun die WEB-Oberfläche.

    .. image:: img/home_open_web_ui.png

#. In der Web-Oberfläche sehen Sie eine Option zum Einbinden der Boot-Partition. Klicken Sie auf **MOUNT**, um die Partition einzubinden.

    .. image:: img/home_mount_boot.png

#. Nach erfolgreichem Einbinden sehen Sie Optionen zum Aktivieren von I2C, SPI und zum Bearbeiten der config.txt-Datei. Aktivieren Sie I2C und SPI. Sobald sie als aktiviert angezeigt werden, klicken Sie auf die Schaltfläche zum Neustarten unten, um den Raspberry Pi neu zu starten.

    .. image:: img/home_i2c_spi.png

#. Nach dem Neustart aktualisieren Sie die Seite. Sie gelangen erneut zur Seite zur Einbindung der Boot-Partition. Klicken Sie erneut auf **MOUNT**.

    .. image:: img/home_mount_boot.png
    
#. In der Regel sehen Sie, dass SPI aktiviert ist, aber I2C nicht, da I2C zwei Neustarts erfordert. Aktivieren Sie I2C erneut und starten Sie den Raspberry Pi neu.

    .. image:: img/home_enable_i2c.png

#. Nach dem Neustart kehren Sie erneut zur **MOUNT** Seite zurück. Sie werden sehen, dass sowohl I2C als auch SPI aktiviert sind.

    .. image:: img/home_i2c_spi_enable.png

.. note::

    * Wenn Sie nach dem Aktualisieren der Seite nicht zur Einbindungsseite gelangen, können Sie erneut auf **Einstellungen** -> **Add-ons** -> **Pi Config Wizard** klicken.
    * Überprüfen Sie, ob dieses Add-on gestartet ist. Wenn nicht, klicken Sie auf **START**.
    * Nach dem Start klicken Sie auf **OPEN WEB UI** und dann auf **MOUNT**, um zu bestätigen, ob I2C und SPI aktiviert sind.

4. Installieren Sie das **Pironman 5** Add-on
-------------------------------------------------

Beginnen Sie nun offiziell mit der Installation des **Pironman 5** Add-ons.

#. Öffnen Sie **Einstellungen** -> **Add-ons**.

    .. image:: img/home_setting_addon.png

#. Klicken Sie auf das Pluszeichen in der unteren rechten Ecke, um den Add-on-Store zu öffnen.

    .. image:: img/home_addon.png

#. Finden Sie **Pironman 5** in der **SunFounder** Add-ons Liste und klicken Sie darauf.

    .. image:: img/home_pironman5_addon.png

#. Installieren Sie nun das Pironman 5 Add-on.

    .. image:: img/home_install_pironman5.png

#. Nach Abschluss der Installation klicken Sie auf **START**, um dieses Add-on zu starten. Sie werden sehen, dass das OLED-Display die CPU, Temperatur und andere relevante Informationen des Raspberry Pi anzeigt. Vier WS2812 RGB-LEDs leuchten blau im Atmungsmodus.

    .. image:: img/home_start_pironman5.png

#. Nun können Sie auf **OPEN WEB UI** klicken, um die Pironman 5 Webseite zu öffnen. Sie können auch die Option aktivieren, um die Web-Oberfläche in der Seitenleiste anzuzeigen. Dadurch können Sie die Pironman 5 Option in der linken Seitenleiste von Home Assistant sehen und auf die Pironman 5 Seite klicken.

    .. image:: img/home_web_ui.png

#. Nun können Sie die Informationen Ihres Raspberry Pi sehen, das RGB konfigurieren und den Lüfter steuern usw.

    .. image:: img/home_web.png
    
.. note::

    Weitere Informationen und die Verwendung dieser Pironman 5 Webseite finden Sie unter: :ref:`view_control_dashboard`.
