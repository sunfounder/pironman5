.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Enthusiasten tiefer in Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _install_to_sd_home_bridge:

Installation des Betriebssystems auf einer Micro-SD-Karte
===================================================================

Wenn Sie eine Micro-SD-Karte verwenden, können Sie der folgenden Anleitung folgen, um das System auf Ihrer Micro-SD-Karte zu installieren.


**Erforderliche Komponenten**

* Ein Personal Computer
* Eine Micro-SD-Karte und Kartenleser

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installation des Betriebssystems auf der microSD-Karte
----------------------------------------------------------------------

1. Setzen Sie Ihre microSD-Karte mithilfe eines Kartenlesers in Ihren Computer ein.  
   Sichern Sie vor dem Fortfahren alle wichtigen Daten auf der Karte, da sie gelöscht werden.

   .. image:: img/insert_sd.png
      :width: 90%

2. Wenn der **Raspberry Pi Imager** geöffnet wird, sehen Sie die Seite **Device**.  
   Wählen Sie Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

3. Wechseln Sie zum Abschnitt **OS**, scrollen Sie bis zum Ende der Seite und wählen Sie Ihr Betriebssystem aus.

   .. note::

      * Für **Ubuntu** klicken Sie auf **Other general-purpose OS** → **Ubuntu** und wählen anschließend  
        **Ubuntu Desktop 24.04 LTS (64-bit)** oder **Ubuntu Server 24.04 LTS (64-bit)** aus.
      * Für **Kali Linux**, **Home Assistant** und **Homebridge** klicken Sie auf  
        **Other specific-purpose OS** und wählen dann das entsprechende System aus.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Wählen Sie im Abschnitt **Storage** Ihre microSD-Karte aus.  
   Aus Sicherheitsgründen wird empfohlen, andere USB-Speichergeräte zu trennen, sodass nur die microSD-Karte in der Liste angezeigt wird.

   .. image:: img/imager_storage.png
      :width: 90%

#. Klicken Sie auf **NEXT**.

   .. note::

      * Bei Systemen, die **nicht im Voraus konfiguriert werden können**, überspringt ein Klick auf **NEXT** den Schritt **Customisation** und wechselt direkt zu **Writing**, wobei das Betriebssystem auf die microSD-Karte geschrieben wird.
      * Bei Systemen, die eine **Vorkonfiguration unterstützen**, folgen Sie den **Customisation**-Schritten, um Optionen wie **Hostname**, **WiFi** und **SSH aktivieren** zu konfigurieren.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Wenn das Popup **„Write Successful“** erscheint, wurde das Image vollständig geschrieben und verifiziert. Sie können die microSD-Karte nun sicher entfernen und damit Ihren Raspberry Pi starten.
