.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!


3,5-Zoll-Touchscreen
=============================

.. note::

    Die Pironman-5-Serie enthält keinen 3,5-Zoll-Touchscreen.  
    Du musst einen selbst vorbereiten oder auf unserer offiziellen Website kaufen:

   * `3,5-Zoll-Touchscreen <https://www.sunfounder.com/products/touchscreen-02>`_

Der 3,5-Zoll-Touchscreen wird direkt an den GPIO-Header des Raspberry Pi angeschlossen  
und bietet sowohl Anzeige- als auch Touch-Steuerung für den Pironman 5.  
Bitte folge den Schritten sorgfältig, um eine korrekte Installation sicherzustellen und Hardware-Schäden zu vermeiden.

Weitere Details findest du hier:  
`3,5-Zoll-Touchscreen-Dokumentation <http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi>`_.


**Montage**

.. image:: img/lcd_to_pironman5.png
    :width: 340

.. image:: img/lcd_to_pironman5.jpg
    :width: 340


.. warning:: 
   
   Achte beim Installieren des 3,5-Zoll-Touchscreens auf den Pironman 5 darauf, dass die Pins perfekt ausgerichtet sind.  
   Der Header muss exakt mit der GPIO-Schnittstelle des Raspberry Pi übereinstimmen, ohne Versatz.  
   Eine falsche Ausrichtung kann den Bildschirm oder sogar den Raspberry Pi beschädigen.  
   Überprüfe die Verbindungen vor dem Einschalten doppelt!


**RGB-Jumper entfernen**

Beim Einsatz des Pironman 5 mit dem 3,5-Zoll-Touchscreen  
beachte, dass die RGB-LEDs am IO-Expander denselben SPI-MOSI-Pin (GPIO10) wie der Bildschirm verwenden.  
Um Konflikte zu vermeiden und einen ordnungsgemäßen Betrieb sicherzustellen:

1. Entferne auf dem IO-Expander die Jumper-Kappe von den **RGB-LED-Pins** (über J9).

   .. image:: img/lcd_to_max0.jpg
      :width: 600
      :align: center

2. Deaktiviere den RGB-LED-Steuerungsdienst:

   .. code-block:: bash

      pironman5 -re false
      sudo systemctl restart pironman5.service

Dies gibt die SPI-Schnittstelle für den 3,5-Zoll-Touchscreen frei und verhindert Anzeigefehler.


**Treiberinstallation**

Vor der Verwendung des 3,5-Zoll-Touchscreens musst du die Treiber installieren.

Allgemeine Tipps:

* Stelle sicher, dass git installiert ist (``sudo apt install git``).  
* Die Treiberinstallation dauert 1–3 Minuten.  
* Das System startet automatisch neu.

Folge den Anweisungen für dein Betriebssystem unten:

* **Für Raspberry Pi OS**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show 
     git clone https://github.com/sunfounder/LCD-show.git 
     chmod -R 755 LCD-show 
     cd LCD-show/ 
     sudo ./LCD35-show
  
  Nach der Installation wird der Desktop auf dem 3,5-Zoll-Touchscreen angezeigt.
  
  Um die Anzeige zu drehen:
  
  .. code-block:: bash
  
     cd LCD-show/
     sudo ./rotate.sh 90   
  
  Das System startet neu, und der Bildschirm wird um 90° gedreht.  
  Du kannst ``90`` durch ``0``, ``180`` oder ``270`` ersetzen.


* **Für Ubuntu**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show-ubuntu 
     git clone https://github.com/sunfounder/LCD-show-ubuntu.git 
     chmod -R 755 LCD-show-ubuntu 
     cd LCD-show-ubuntu/ 
     sudo ./LCD35-show
  
  Nach der Installation wird der Desktop auf dem 3,5-Zoll-Touchscreen angezeigt.
  
  Um zu drehen:
  
  .. code-block:: bash
  
     cd LCD-show-ubuntu/
     sudo ./rotate.sh 90   
  
  Der Neustart erfolgt automatisch.  
  Ersetze ``90`` durch ``0``, ``180`` oder ``270`` nach Bedarf.


* **Für Kali Linux**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show-kali 
     git clone https://github.com/sunfounder/LCD-show-kali.git 
     chmod -R 755 LCD-show-kali 
     cd LCD-show-kali/ 
     sudo ./LCD35-show
  
  Nach der Installation wird der Desktop auf dem 3,5-Zoll-Touchscreen angezeigt.
  
  Um zu drehen:
  
  .. code-block:: bash
  
     cd LCD-show-kali/
     sudo ./rotate.sh 90   
  
  Das System wird mit der neuen Ausrichtung neu gestartet.  
  Ersetze ``90`` durch ``0``, ``180`` oder ``270`` nach Bedarf.
