.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Set-up auf Home Assistant
============================================

Wenn Sie das Home Assistant System installiert haben, müssen Sie die notwendigen Add-ons zu Home Assistant hinzufügen und sie starten, um den Pironman 5 zum Laufen zu bringen.

.. note::

    Die folgende Methode ist nur auf Systeme mit nativ installiertem Home Assistant anwendbar. Sie gilt nicht für Raspberry Pi Systeme, auf denen Home Assistant nachträglich installiert wurde, oder für Docker-Versionen von Home Assistant.

1. Anmeldung bei Home Assistant
----------------------------------

* Nach dem Start von Pironman 5 wird empfohlen, ein Ethernet-Kabel direkt anzuschließen. So können Sie Ihren Computer-Browser öffnen und ``homeassistant.local:8123`` eingeben, um auf Home Assistant zuzugreifen.

  .. image:: img/home_login.png
   :width: 90%


* Wählen Sie **MEIN SMARTES ZUHAUSE ERSTELLEN** und erstellen Sie dann Ihr Konto.

  .. image:: img/home_account.png
   :width: 90%

* Folgen Sie den Anweisungen, um Ihren Standort und andere Konfigurationen auszuwählen. Sobald dies abgeschlossen ist, gelangen Sie zum Home Assistant Dashboard.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Hinzufügen des SunFounder Add-ons Repository
----------------------------------------------------

Die Funktionen von Pironman 5 werden in Home Assistant in Form von Add-ons installiert. Zuerst müssen Sie das **SunFounder** Add-ons Repository hinzufügen.

#. Öffnen Sie **Einstellungen** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Klicken Sie unten rechts auf das Pluszeichen, um in den Add-on-Store zu gelangen.

   .. image:: img/home_addon.png
      :width: 90%

#. Klicken Sie im Add-on-Store auf das Menü in der oberen rechten Ecke und wählen Sie **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Geben Sie die URL des **SunFounder** Add-ons Repository ein: ``https://github.com/sunfounder/home-assistant-addon``, und klicken Sie auf **HINZUFÜGEN**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Nach erfolgreicher Hinzufügung schließen Sie das Pop-up-Fenster und aktualisieren die Seite. Suchen Sie die SunFounder Add-ons Liste.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Installation des **Pi Config Wizard** Add-ons
-------------------------------------------------------

Der **Pi Config Wizard** hilft bei der Aktivierung der für Pironman 5 benötigten Konfigurationen, wie I2C und SPI. Wenn er später nicht mehr benötigt wird, kann er entfernt werden.

#. Suchen Sie den **Pi Config Wizard** in der SunFounder Add-ons Liste und klicken Sie darauf.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Klicken Sie auf der Seite des **Pi Config Wizard** auf **INSTALLIEREN**. Warten Sie, bis die Installation abgeschlossen ist.

   .. image:: img/home_config_install.png
      :width: 90%

#. Nach Abschluss der Installation wechseln Sie zur **Protokoll**-Seite, um zu überprüfen, ob Fehler aufgetreten sind.

   .. image:: img/home_log.png
      :width: 90%

#. Wenn keine Fehler aufgetreten sind, kehren Sie zur **Info**-Seite zurück und klicken Sie auf **STARTEN**, um dieses Add-on zu starten.

   .. image:: img/home_start.png
      :width: 90%

#. Öffnen Sie nun die WEB-UI.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. In der Web-UI sehen Sie eine Option, die Boot-Partition einzubinden. Klicken Sie auf **EINBINDEN**, um die Partition zu mounten.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Nach erfolgreichem Einbinden sehen Sie Optionen zum Aktivieren von I2C und SPI sowie zum Bearbeiten der config.txt-Datei. Aktivieren Sie I2C und SPI. Sobald sie als aktiviert angezeigt werden, klicken Sie auf die Schaltfläche Neustart unten, um den Raspberry Pi neu zu starten.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Nach dem Neustart aktualisieren Sie die Seite. Sie kehren erneut zur Seite zur Einbindung der Boot-Partition zurück. Klicken Sie erneut auf **EINBINDEN**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Normalerweise sehen Sie, dass SPI aktiviert ist, aber I2C nicht, da I2C zwei Neustarts erfordert. Aktivieren Sie I2C erneut und starten Sie den Raspberry Pi neu.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Nach dem Neustart kehren Sie erneut zur **EINBINDEN**-Seite zurück. Sie sehen nun, dass sowohl I2C als auch SPI aktiviert sind.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Wenn Sie nach dem Aktualisieren der Seite nicht zur Einbindungsseite gelangen, können Sie auf **Einstellungen** -> **Add-ons** -> **Pi Config Wizard** klicken.
    * Überprüfen Sie, ob dieses Add-on gestartet wurde. Falls nicht, klicken Sie auf **STARTEN**.
    * Nach dem Starten klicken Sie auf **WEB-UI ÖFFNEN**, dann auf **EINBINDEN**, um zu bestätigen, ob I2C und SPI aktiviert sind.

4. Installation des **Pironman 5** Add-ons
----------------------------------------------

Nun starten Sie die Installation des **Pironman 5** Add-ons.

#. Öffnen Sie **Einstellungen** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Klicken Sie unten rechts auf das Pluszeichen, um in den Add-on-Store zu gelangen.

   .. image:: img/home_addon.png
      :width: 90%

#. Finden Sie **Pironman 5** in der **SunFounder** Add-ons Liste und klicken Sie darauf.

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Installieren Sie nun das Pironman 5 Add-on.

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. Nach Abschluss der Installation klicken Sie auf **STARTEN**, um dieses Add-on zu starten. Sie werden sehen, dass das OLED-Display die CPU des Raspberry Pi, die Temperatur und andere verwandte Informationen anzeigt. Vier WS2812 RGB-LEDs leuchten in einem blauen Atemmodus.

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. Nun können Sie auf **WEB-UI ÖFFNEN** klicken, um die Pironman 5 Webseite zu öffnen. Sie können auch die Option aktivieren, die Web-UI in der Seitenleiste anzuzeigen. Dadurch können Sie die Pironman 5 Option in der linken Seitenleiste von Home Assistant sehen und auf die Pironman 5 Seite zugreifen.

   .. image:: img/home_web_ui.png
      :width: 90%

#. Nun können Sie die Informationen über Ihren Raspberry Pi einsehen, die RGB-LEDs konfigurieren und den Lüfter steuern usw.

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

    Für weitere Informationen und die Verwendung dieser Pironman 5 Webseite lesen Sie bitte: :ref:`view_control_dashboard`.

