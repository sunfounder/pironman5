.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _set_up_pironman5:

4. Einrichtung des Pironman 5
===================================

Vor der Konfiguration
--------------------------
Nach dem Einschalten sehen Sie nur die verschiedenen Power-LEDs leuchten, aber der OLED-Bildschirm (bei einem Anzeigeproblem ignorieren Sie es bitte, da es sich nach der Konfiguration löst), die RGB-LEDs und die RGB-Lüfter (die beiden Lüfter an den Seiten) funktionieren noch nicht, da sie noch nicht konfiguriert wurden.

Der Power-Button fungiert wie der Power-Button des Raspberry Pi 5 und funktioniert genauso.

**Herunterfahren**

    * Wenn Sie das Raspberry Pi **Bookworm Desktop**-System verwenden, können Sie den Power-Button zweimal schnell hintereinander drücken, um das Gerät herunterzufahren.
    * Wenn Sie das Raspberry Pi **Bookworm Lite**-System verwenden, drücken Sie den Power-Button einmal, um das Herunterfahren zu starten.
    * Um ein erzwungenes Herunterfahren durchzuführen, halten Sie den Power-Button gedrückt.

**Einschalten**

    * Wenn das Raspberry Pi Board heruntergefahren, aber noch mit Strom versorgt ist, drücken Sie einmal, um es aus dem Heruntergefahren-Zustand einzuschalten.

.. note::

    Wenn Sie ein System verwenden, das keinen Shutdown-Button unterstützt, können Sie ihn 5 Sekunden lang gedrückt halten, um ein erzwungenes Herunterfahren durchzuführen, und einmal drücken, um aus dem Heruntergefahren-Zustand einzuschalten.

Software-Konfiguration
--------------------------

1. Wenn Sie Raspberry Pi OS, Ubuntu oder Kali auf Ihrem Raspberry Pi installiert haben, müssen Sie den Pironman 5 über die Kommandozeile konfigurieren. Detaillierte Anleitungen finden Sie unten:


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 

2. Wenn Sie das Home Assistant System installiert haben, müssen Sie die notwendigen Add-ons zu Home Assistant hinzufügen und starten, um den Pironman 5 in Betrieb zu nehmen.

.. note::

    Die folgende Methode gilt nur für Systeme mit nativer Installation von Home Assistant. Sie gilt nicht für Raspberry Pi Systeme mit darauf installiertem Home Assistant oder für Docker-Versionen von Home Assistant.


.. toctree::
    :maxdepth: 1  

    set_up_home_assistant
