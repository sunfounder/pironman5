.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Teil unserer Community!

.. _max_install_to_sd_ubuntu:

Installation des Betriebssystems auf einer Micro-SD-Karte
============================================================

Wenn du eine Micro-SD-Karte verwendest, kannst du dem folgenden Tutorial folgen, um das System auf die Karte zu installieren.


**Erforderliche Komponenten**

* Ein PC oder Laptop
* Eine Micro-SD-Karte und ein Kartenleser

**Schritte**

#. Rufe zunächst die Seite |link_batocera_download| auf, wähle **Raspberry Pi 5 B** aus und lade das System herunter.

   .. image:: img/batocera_download.png
      :width: 90%
      
#. Entpacke die heruntergeladene Datei ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Stecke deine SD-Karte mit einem Kartenleser in deinen Computer oder Laptop.

#. Öffne den |link_rpi_imager| und klicke auf den Reiter **Betriebssystem**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Scrolle ganz nach unten und wähle **Eigenes Image verwenden**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. Wähle die zuvor entpackte Systemdatei ``batocera-xxx-xx-xxxxxxxx.img`` aus und klicke auf **Öffnen**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Klicke auf **Speicher wählen** und wähle das passende Zielgerät für die Installation aus.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Jetzt kannst du auf **WEITER** klicken. Wenn das Speichergerät bereits Daten enthält, stelle sicher, dass du ein Backup gemacht hast. Klicke auf **Ja**, wenn kein Backup nötig ist.

   .. image:: img/os_continue.png
      :width: 90%


#. Wenn das Pop-up „Schreiben erfolgreich“ erscheint, wurde dein Image vollständig geschrieben und überprüft. Dein Raspberry Pi ist jetzt bereit, von der Micro-SD-Karte zu booten!
