.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an saisonalen Verlosungen und Aktionsangeboten teil.

    👉 Bereit zum Entdecken und Entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _install_batocera_mini:

Installation von Batocera Linux
======================================================

|link_batocera| ist eine quelloffene und vollkommen kostenlose Retro-Gaming-Distribution, die auf einen USB-Stick oder eine SD-Karte kopiert werden kann, um jeden Computer oder Einplatinenrechner temporär oder dauerhaft in eine Spielekonsole zu verwandeln.

Die Installationsmethode richtet sich danach, ob du eine Micro-SD-Karte oder eine NVMe-SSD zur Verfügung hast.

Die direkte Installation auf eine NVMe-SSD erfordert einen zusätzlichen Schritt im Vergleich zur Installation auf einer Micro-SD-Karte: Du musst den Bootloader des Raspberry Pi aktualisieren, da dieser standardmäßig von der SD-Karte bootet. Aktualisiere den Bootloader, um das Booten von der NVMe-SSD zu priorisieren.

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

