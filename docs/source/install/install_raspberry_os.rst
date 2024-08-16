.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Installieren Sie das Raspberry Pi OS
================================================================================

Sie können die Installationsmethode basierend auf der Verfügbarkeit einer Micro-SD-Karte oder einer NVMe-SSD wählen.

* Die direkte Installation auf der NVMe-SSD erfordert einen zusätzlichen Schritt im Vergleich zur Installation auf der Micro-SD-Karte: Sie müssen den Bootloader des Raspberry Pi aktualisieren, da dieser standardmäßig vom Micro-SD-Kartenslot bootet. Aktualisieren Sie den Bootloader, um das Booten von der NVMe-SSD zu priorisieren.
* Wenn Sie eine NVMe-SSD haben, aber keinen Adapter, um diese mit Ihrem Computer zu verbinden, sollten Sie die dritte Option in Betracht ziehen: Installieren Sie das System zuerst auf Ihrer Micro-SD-Karte. Sobald der Pironman 5 erfolgreich hochgefahren ist, können Sie das System von der Micro-SD-Karte auf Ihre NVMe-SSD kopieren.


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi