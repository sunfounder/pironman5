.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Entdecke die Welt von Raspberry Pi, Arduino und ESP32 gemeinsam mit anderen Technikbegeisterten.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Problemen und Fragen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produktankündigungen und erhalte exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, gemeinsam mit uns kreativ zu werden? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _copy_sd_to_nvme_rpi_mini:

Kopieren des Betriebssystems von der Micro-SD-Karte auf die NVMe-SSD
========================================================================

Falls du eine NVMe-SSD hast, aber keinen Adapter, um sie mit deinem Computer zu verbinden, kannst du folgende Alternative wählen: Installiere das System zuerst auf einer Micro-SD-Karte. Sobald der Pironman 5 Mini erfolgreich hochgefahren ist, kannst du das System von der SD-Karte auf die NVMe-SSD übertragen.

* Installiere zunächst das Betriebssystem gemäß :ref:`install_os_sd_rpi_mini`.
* Starte und melde dich beim Raspberry Pi an. Wenn du nicht weißt, wie du dich anmeldest, besuche die offizielle Raspberry Pi-Webseite: |link_rpi_get_start|.

Schließe die obigen Schritte ab, bevor du mit den folgenden Anleitungen fortfährst.


1. PCIe aktivieren
--------------------

Standardmäßig ist der PCIe-Anschluss deaktiviert.

* Um ihn zu aktivieren, öffne die Datei ``/boot/firmware/config.txt``.

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* Füge folgende Zeile hinzu:

  .. code-block:: shell

    # PCIe-Externanschluss aktivieren
    dtparam=pciex1

* Alternativ kannst du auch den Alias ``dtparam=nvme`` verwenden:

  .. code-block:: shell

    dtparam=nvme

* Die Verbindung ist für Gen 2.0 (5 GT/s) zertifiziert, kann aber mit folgendem Eintrag auf Gen 3.0 (10 GT/s) erzwungen werden:

  .. code-block:: shell

    # Gen 3.0-Geschwindigkeit erzwingen
    dtparam=pciex1_gen=3

  .. warning::

    Der Raspberry Pi 5 ist nicht für Gen 3.0 zertifiziert. Der Betrieb bei dieser Geschwindigkeit kann zu Instabilitäten führen.

* Speichere die Änderungen mit ``Ctrl + X``, ``Y`` und ``Enter``.


2. Betriebssystem auf SSD installieren
----------------------------------------

Es gibt zwei Möglichkeiten, das Betriebssystem auf der SSD zu installieren:

**System von SD-Karte auf SSD kopieren**

#. Verbinde einen Monitor oder verwende VNC Viewer, um auf den Raspberry Pi-Desktop zuzugreifen. Klicke dann auf **Raspberry Pi logo** → **Accessories** → **SD Card Copier**.

   .. image:: img/ssd_copy.png


#. Wähle sorgfältig die richtigen Geräte für **Copy From** und **Copy To** aus.

   .. image:: img/ssd_copy_from.png

#. Aktiviere die Option "NEW Partition UUIDs", um Probleme mit der Gerätezurodnung zu vermeiden.

   .. image:: img/ssd_copy_uuid.png

#. Klicke auf **Start**.

   .. image:: img/ssd_copy_click_start.png

#. Bestätige den Hinweis, dass alle Daten auf der SSD gelöscht werden. Sichere wichtige Daten vorab.

   .. image:: img/ssd_copy_erase.png

#. Warte, bis der Kopiervorgang abgeschlossen ist.

**System mit Raspberry Pi Imager installieren**

Wenn auf deiner Micro-SD-Karte eine Desktop-Version des Betriebssystems installiert ist, kannst du ein Imaging-Tool (z. B. Raspberry Pi Imager) verwenden, um das System auf die SSD zu übertragen. In diesem Beispiel wird Raspberry Pi OS Bookworm verwendet, bei anderen Systemen muss das Imaging-Tool möglicherweise zuerst installiert werden.

#. Schließe ein Display an oder greife über VNC Viewer auf den Desktop des Raspberry Pi zu. Klicke dann auf **Raspberry Pi-Logo** → **Zubehör** → **Imager**.

   .. image:: img/ssd_imager.png


#. Im |link_rpi_imager| wähle **Raspberry Pi Gerät** und wähle **Raspberry Pi 5**.

   .. image:: img/ssd_pi5.png
      :width: 90%


#. Wähle **Betriebssystem** und entscheide dich für die empfohlene Version.

   .. image:: img/ssd_os.png
      :width: 90%

#. Wähle unter **Speicher** deine angeschlossene NVMe-SSD.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Klicke auf **NEXT**, danach auf **EDIT SETTINGS**, um die OS-Konfiguration anzupassen.

   .. note::

      Falls ein Monitor angeschlossen ist, kannst du die weiteren Schritte überspringen und direkt mit 'Ja' fortfahren.

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Vergib einen **Hostname** für deinen Raspberry Pi.

   .. note::

      Du erreichst deinen Pi unter ``<hostname>.local`` oder ``<hostname>.lan``.

   .. image:: img/os_set_hostname.png


#. Lege einen **Benutzernamen** und ein **Passwort** fest.

   .. note::

      Ein individuelles Passwort erhöht die Sicherheit deines Systems.

   .. image:: img/os_set_username.png


#. Konfiguriere das drahtlose Netzwerk, indem du die **SSID** und das **Passwort** deines WLANs eingibst.

   .. note::

      Stelle sicher, dass du das ``Wireless LAN country`` auf den zweistelligen `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ für dein Land einstellst.

   .. image:: img/os_set_wifi.png

#. Um dich aus der Ferne mit deinem Raspberry Pi zu verbinden, **aktiviere SSH** im Reiter **Dienste**.

   * Für die **password authentication** verwende den Benutzernamen und das Passwort aus dem Reiter **General**.
   * Für die Authentifizierung per öffentlichem Schlüssel wähle „Nur Authentifizierung mit öffentlichem Schlüssel zulassen“. Wenn du bereits einen RSA-Schlüssel hast, wird dieser verwendet. Andernfalls klicke auf „SSH-keygen ausführen“, um ein neues Schlüsselpaar zu generieren.

   .. image:: img/os_enable_ssh.png



#. Im Menü **Optionen** kannst du das Verhalten des Imagers während des Schreibvorgangs anpassen – z. B. Ton abspielen nach Abschluss, Medium auswerfen oder Telemetrie aktivieren.

   .. image:: img/os_options.png

#. Wenn du alle gewünschten Einstellungen vorgenommen hast, klicke auf **Speichern**, um die Anpassungen zu sichern. Danach auf **Ja**, um sie beim Schreiben des Abbilds anzuwenden.

   .. image:: img/os_click_yes.png
      :width: 90%

#. Falls sich bereits Daten auf der NVMe-SSD befinden, sichere diese vorher, um Datenverlust zu vermeiden. Wenn keine Sicherung erforderlich ist, fahre mit **Ja** fort.

   .. image:: img/nvme_erase.png
      :width: 90%

#. Sobald das Fenster „Write Successful“ erscheint, wurde dein Abbild erfolgreich geschrieben und verifiziert. Du kannst den Raspberry Pi jetzt direkt von der NVMe-SSD starten!

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _configure_boot_ssd_mini:

3. Boot von der SSD konfigurieren
---------------------------------------

In diesem Abschnitt konfigurieren wir deinen Raspberry Pi so, dass er direkt von einer NVMe-SSD startet. Dies ermöglicht schnellere Bootzeiten und eine bessere Systemleistung im Vergleich zur SD-Karte. Folge diesen Schritten sorgfältig:

#. Öffne zunächst ein Terminal auf deinem Raspberry Pi und führe folgenden Befehl aus, um das Konfigurationsmenü zu öffnen:

   .. code-block:: shell

      sudo raspi-config

#. Navigiere im Menü ``raspi-config`` mit den Pfeiltasten zu **Erweiterte Optionen** (**Advanced Options**) und drücke ``Enter``, um die erweiterten Einstellungen aufzurufen.

   .. image:: img/nvme_open_config.png

#. Wähle im Menü **Erweiterte Optionen** den Punkt **Boot-Reihenfolge** (**Boot Order**). Hier legst du fest, in welcher Reihenfolge der Raspberry Pi nach startfähigen Geräten sucht.

   .. image:: img/nvme_boot_order.png

#. Wähle anschließend **NVMe/USB-Boot**, damit der Raspberry Pi bevorzugt von über USB angeschlossenen SSDs oder NVMe-Laufwerken startet, anstatt von der SD-Karte.

   .. image:: img/nvme_boot_nvme.png

#. Drücke nach der Auswahl der Boot-Reihenfolge auf **Fertigstellen** (**Finish**), um das raspi-config-Menü zu verlassen. Alternativ kannst du auch die **Escape**-Taste verwenden.

   .. image:: img/nvme_boot_ok.png

#. Um die neuen Boot-Einstellungen zu übernehmen, starte den Raspberry Pi neu mit folgendem Befehl: ``sudo reboot``.

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

Nach dem Neustart sollte dein Raspberry Pi versuchen, direkt von der angeschlossenen NVMe-SSD zu booten – das sorgt für höhere Leistung und bessere Systemstabilität.
