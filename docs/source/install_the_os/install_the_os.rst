.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

3. Installation des Betriebssystems
=======================================

In diesem Kapitel lernen Sie, wie Sie das Betriebssystem installieren.

.. note::

    Sie müssen ein Betriebssystem installieren, das den Raspberry Pi 5 unterstützt. Bitte verwenden Sie das neueste Raspberry Pi Imager-Tool für die Systeminstallation. Die derzeit getesteten Systeme sind:

    .. image:: img/compitable_os.png


1. 1. Installation des Betriebssystems auf die MicroSD-Karte
--------------------------------------------------------------------------

Wenn Sie eine MicroSD-Karte verwenden, können Sie dem folgenden Tutorial folgen, um das System auf Ihrer MicroSD-Karte zu installieren.

    .. toctree::
        :maxdepth: 1

        install_to_sd


2. Installation des Betriebssystems auf die NVMe-SSD
--------------------------------------------------------------

Wenn Sie eine NVMe-SSD verwenden und einen Adapter haben, um die NVMe-SSD für die Systeminstallation an Ihren Computer anzuschließen, können Sie das folgende Tutorial für eine schnelle Installation verwenden.

    .. toctree::
        :maxdepth: 1

        install_to_nvme

3. Kopieren des Betriebssystems von der MicroSD-Karte auf die NVMe-SSD
----------------------------------------------------------------------------------

.. note::

    Diese dritte Methode gilt nur für **Raspberry Pi OS**. Wenn Sie ein anderes System verwenden, müssen Sie entsprechende Ressourcen konsultieren, um zu erfahren, wie Sie das System von Ihrer Micro-SD-Karte auf Ihre NVMe-SSD kopieren können.

Wenn Sie eine NVMe-SSD haben, aber keinen Adapter, um Ihre NVMe mit Ihrem Computer zu verbinden, können Sie das System zuerst auf Ihrer Micro-SD-Karte installieren. Sobald der Pironman 5 erfolgreich gestartet ist, können Sie das System von Ihrer Micro-SD-Karte auf Ihre NVMe-SSD kopieren. Detaillierte Anweisungen sind wie folgt:

Sie müssen diese Schritte befolgen:

1. Installieren Sie das System auf Ihrer MicroSD-Karte.

* :ref:`install_os_sd`

2. Starten Sie den Raspberry Pi und melden Sie sich an.

* :ref:`login_rpi`

3. Kopieren Sie das System von der Micro SD-Karte auf die NVMe SSD oder verwenden Sie den Imager im Raspberry Pi-System, um das System direkt auf der NVMe SSD zu installieren. Richten Sie anschließend das Booten von der NVMe SSD ein.

* :ref:`boot_from_ssd`
