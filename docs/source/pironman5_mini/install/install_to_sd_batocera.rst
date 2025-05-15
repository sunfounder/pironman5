.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenhilfe**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Kenntnisse zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorabinformationen.
    - **Spezielle Rabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Aktionen und Verlosungen zu Feiertagen**: Nimm an Gewinnspielen und Sonderaktionen teil.

    👉 Bereit für spannende Projekte? Klicke auf [|link_sf_facebook|] und werde jetzt Mitglied!

.. _install_to_sd_ubuntu_mini:

Installation des Betriebssystems auf einer Micro-SD-Karte
=============================================================

Wenn du eine Micro-SD-Karte verwendest, kannst du der folgenden Anleitung folgen, um das System auf die Karte zu installieren.

**Erforderliche Komponenten**

* Ein Computer oder Laptop
* Eine Micro-SD-Karte und ein Kartenleser


**Schritte**

#. Besuche zunächst die Seite |link_batocera_download|, wähle **Raspberry Pi 5 B** aus und starte den Download.

   .. image:: img/batocera_download.png
      :width: 90%


#. Entpacke die heruntergeladene Datei ``batocera-xxx-xx-xxxxxxxx.img.gz``.


#. Stecke deine SD-Karte über einen Kartenleser in den Computer oder Laptop.


#. Öffne den |link_rpi_imager| und klicke auf den Reiter **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scrolle nach ganz unten auf der Seite und wähle **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. Wähle die zuvor entpackte Systemdatei ``batocera-xxx-xx-xxxxxxxx.img`` aus und klicke auf **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Klicke auf **Choose Storage** und wähle das passende Speichermedium für die Installation.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Klicke nun auf **NEXT**. Wenn das Speichermedium bereits Daten enthält, sichere diese vorher. Klicke auf **Yes**, wenn keine Sicherung nötig ist.

   .. image:: img/os_continue.png
      :width: 90%


#. Sobald die Meldung „Write Successful“ erscheint, wurde das Image erfolgreich geschrieben und überprüft. Jetzt bist du bereit, deinen Raspberry Pi von der Micro-SD-Karte zu starten!
