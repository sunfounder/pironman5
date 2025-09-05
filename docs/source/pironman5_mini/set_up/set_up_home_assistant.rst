.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an festlichen Aktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und kreativ zu werden? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

Set-up unter Home Assistant
============================================

Wenn du das Home Assistant System installiert hast, musst du die erforderlichen Add-ons in Home Assistant hinzufügen und starten, um den Pironman 5 Mini zum Laufen zu bringen.

.. note::

    Die folgende Methode gilt nur für Systeme, bei denen Home Assistant nativ installiert wurde. Sie ist nicht anwendbar auf Systeme, bei denen Home Assistant nachträglich auf einem Raspberry Pi installiert wurde oder auf Docker-Versionen.

1. Anmeldung bei Home Assistant
----------------------------------

* Nach dem Start des Pironman 5 Mini wird empfohlen, direkt ein Ethernet-Kabel anzuschließen. So kannst du in deinem Browser ``homeassistant.local:8123`` eingeben, um auf Home Assistant zuzugreifen.

  .. image:: img/home_login.png
   :width: 90%


* Wähle **CREATE MY SMART HOME** und erstelle anschließend dein Konto.

  .. image:: img/home_account.png
   :width: 90%

* Folge den Anweisungen zur Standortwahl und weiteren Konfigurationen. Danach gelangst du zum Home Assistant Dashboard.

  .. image:: img/home_dashboard.png
   :width: 90%


2. SunFounder Add-ons Repository hinzufügen
----------------------------------------------------

Die Funktionen des Pironman 5 Mini werden in Home Assistant als Add-ons installiert. Zunächst musst du das **SunFounder** Add-ons Repository hinzufügen.

#. Öffne **Einstellungen** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Klicke unten rechts auf das Pluszeichen, um den Add-on Store zu öffnen.

   .. image:: img/home_addon.png
      :width: 90%

#. Im Add-on Store klicke oben rechts auf das Menü und wähle **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Gib die Repository-URL von **SunFounder** ein: ``https://github.com/sunfounder/home-assistant-addon`` und klicke auf **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Nach erfolgreichem Hinzufügen schließe das Pop-up-Fenster und aktualisiere die Seite. Du solltest nun die Liste der SunFounder Add-ons sehen.

   .. image:: img/home_addon_list.png
         :width: 90%

3. **Pi Config Wizard** Add-on installieren
------------------------------------------------------

Der **Pi Config Wizard** hilft dabei, die für den Pironman 5 Mini erforderlichen Konfigurationen wie I2C und SPI zu aktivieren. Nach der Einrichtung kann das Add-on wieder entfernt werden.

#. Finde **Pi Config Wizard** in der SunFounder Add-ons Liste und klicke darauf.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Auf der Seite des **Pi Config Wizard** klicke auf **INSTALL** und warte, bis die Installation abgeschlossen ist.

   .. image:: img/home_config_install.png
      :width: 90%

#. Wechsle nach der Installation zur Seite **Log**, um mögliche Fehler zu prüfen.

   .. image:: img/home_log.png
      :width: 90%

#. Wenn keine Fehler vorliegen, kehre zur Seite **Info** zurück und klicke auf **START**, um das Add-on zu starten.

   .. image:: img/home_start.png
      :width: 90%

#. Öffne nun das WEB UI.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Im Web UI findest du die Option zum Mounten der Boot-Partition. Klicke auf **MOUNT**, um diese Partition zu mounten.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Nach erfolgreichem Mounten erscheinen die Optionen zur Aktivierung von I2C, SPI und zum Bearbeiten der config.txt. Aktiviere I2C und SPI. Sobald beide als aktiviert angezeigt werden, klicke auf den Neustart-Button am unteren Rand, um den Raspberry Pi neu zu starten.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Nach dem Neustart aktualisiere die Seite. Du wirst erneut zur Seite **MOUNT** geleitet. Klicke erneut auf **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. In der Regel ist SPI nun aktiviert, I2C jedoch noch nicht, da I2C zwei Neustarts benötigt. Aktiviere I2C erneut und starte den Raspberry Pi erneut neu.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Nach dem Neustart siehst du auf der Seite **MOUNT**, dass nun sowohl I2C als auch SPI aktiviert sind.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Falls du nach dem Aktualisieren der Seite nicht zur Mount-Seite weitergeleitet wirst, klicke erneut auf **Einstellungen** -> **Add-ons** -> **Pi Config Wizard**.
    * Stelle sicher, dass das Add-on gestartet ist. Falls nicht, klicke auf **START**.
    * Nach dem Start öffne das **WEB UI**, klicke dann auf **MOUNT**, um den Status von I2C und SPI zu überprüfen.



.. .. 这里要改PIRONMAN5 MINI的ADD ON 图


4. **Pironman 5 Mini** Add-on installieren
------------------------------------------------

Jetzt beginnt die eigentliche Installation des **Pironman 5 Mini** Add-ons.

#. Öffne **Einstellungen** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Klicke unten rechts auf das Pluszeichen, um den Add-on Store zu öffnen.

   .. image:: img/home_addon.png
      :width: 90%

#. Suche in der SunFounder Add-ons Liste nach **Pironman 5 Mini** und klicke darauf.

   .. image:: img/home_pironman5_mini_addon.png
      :width: 90%

#. Installiere nun das Pironman 5 Mini Add-on.

   .. image:: img/home_pironman5_mini_addon_install.png
      :width: 90%

#. Nach Abschluss der Installation klicke auf **START**, um das Add-on zu starten. Du wirst sehen, dass vier WS2812-RGB-LEDs in blauem Atmungsmodus leuchten.

   .. image:: img/home_pironman5_mini_addon_start.png
      :width: 90%

#. Klicke nun auf **OPEN WEB UI**, um die Weboberfläche von Pironman 5 Mini zu öffnen. Aktiviere zusätzlich die Option, die Web UI in der Seitenleiste anzuzeigen. So kannst du in der linken Seitenleiste von Home Assistant direkt auf die Pironman 5 Mini Seite zugreifen.

   .. image:: img/home_pironman5_mini_webui.png
      :width: 90%

#. In der Oberfläche siehst du Informationen über deinen Raspberry Pi, kannst RGB-LEDs konfigurieren, den Lüfter steuern und vieles mehr.

   .. image:: img/home_web.png
      :width: 90%



.. note::

   Sie haben nun alle Komponenten des Pironman 5 mini erfolgreich eingerichtet. Die Konfiguration des Pironman 5 mini ist abgeschlossen.
   Sie können den Pironman 5 mini nun zur Steuerung Ihres Raspberry Pi und anderer Geräte verwenden.
   Weitere Informationen und Hinweise zur Nutzung dieser Pironman 5 mini-Webseite finden Sie unter: :ref:`view_control_dashboard_mini`.