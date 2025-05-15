.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum der Community beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um dein Wissen zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorabinformationen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen und Verlosungen**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_install_batocera:

Batocera Linux installieren
======================================================

|link_batocera| ist eine quelloffene und vollständig kostenlose Retro-Gaming-Distribution, die auf einen USB-Stick oder eine SD-Karte kopiert werden kann. Damit lässt sich jeder (Mini-)Computer vorübergehend oder dauerhaft in eine Spielkonsole verwandeln.

Du kannst die Installationsmethode je nach verfügbarer Hardware wählen – entweder mit einer Micro SD-Karte oder einer NVMe-SSD.

Die direkte Installation auf eine NVMe-SSD erfordert im Vergleich zur SD-Karten-Installation einen zusätzlichen Schritt: Du musst den Bootloader des Raspberry Pi aktualisieren, da dieser standardmäßig von der Micro SD-Karte startet. Aktualisiere den Bootloader, um das Booten von der NVMe-SSD zu priorisieren.

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

