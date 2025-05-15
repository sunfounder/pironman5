.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum der Community beitreten?**

    - **Expertensupport**: Erhalte Unterstützung bei technischen Herausforderungen und Problemen nach dem Kauf – durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Nutze exklusive Rabatte auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an festlichen Aktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Installiere das Raspberry Pi OS
================================================================================

Du kannst die Installationsmethode entsprechend der verfügbaren Hardware wählen – je nachdem, ob du eine Micro SD-Karte oder eine NVMe-SSD zur Hand hast.

* Die direkte Installation auf eine NVMe-SSD erfordert einen zusätzlichen Schritt im Vergleich zur Installation auf eine Micro SD-Karte: Du musst den Bootloader des Raspberry Pi aktualisieren, da dieser standardmäßig von der SD-Karte bootet. Aktualisiere den Bootloader, um das Booten von der NVMe-SSD zu priorisieren.
* Falls du eine NVMe-SSD besitzt, aber keinen Adapter hast, um sie mit deinem Computer zu verbinden, wähle die dritte Option: Installiere das System zunächst auf deiner Micro SD-Karte. Sobald der Pironman 5 erfolgreich gestartet ist, kannst du das System von der Micro SD-Karte auf die NVMe-SSD übertragen.


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi