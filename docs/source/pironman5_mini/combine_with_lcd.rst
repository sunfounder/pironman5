Combine With 3.5 inch LCD
=============================

Dieser Abschnitt richtet sich an Benutzer des Pironman 5, die auch den `3,5-Zoll-LCD-Bildschirm <https://www.sunfounder.com/products/touchscreen-02?_pos=2&_sid=839d5db5b&_ss=r>`_ erworben haben.

Der LCD-Bildschirm kann direkt auf die GPIO-Leiste des Raspberry Pi montiert werden und bietet visuelle Anzeige- und Touch-Steuerungsfunktionen für den Pironman 5. Bitte befolgen Sie die richtigen Installationsschritte, um einen ordnungsgemäßen Betrieb sicherzustellen und Hardwareschäden zu vermeiden.

Weitere Informationen über den LCD-Bildschirm und dessen Verwendung finden Sie unter folgendem Link:
`3,5-Zoll-LCD-Dokumentation <http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi>`_.


**Assemble**

.. image:: ../img/lcd_to_mini1.jpg
    :width: 340

.. image:: ../img/lcd_to_mini2.jpg
    :width: 340


.. warning:: Beim Einbau des 3,5-Zoll-LCD-Bildschirms in den Pironman 5 stellen Sie bitte sicher, dass die Pins exakt ausgerichtet sind. Der Header des LCD-Moduls muss genau mit der GPIO-Schnittstelle des Raspberry Pi übereinstimmen, ohne Versatz oder Fehlstellung. Falsche Verbindungen können den LCD-Bildschirm oder sogar den Raspberry Pi beschädigen. Überprüfen Sie vor dem Einschalten alle Verbindungen sorgfältig!


**Remove RGB Jumper**

Wenn Sie den Pironman 5 zusammen mit dem 3,5-Zoll-LCD-Bildschirm verwenden, teilen sich die RGB-LED und das LCD dieselben SPI-Pins. Um Konflikte zu vermeiden und sicherzustellen, dass der LCD-Bildschirm ordnungsgemäß funktioniert, muss die RGB-LED-Verbindung deaktiviert werden.

Führen Sie die folgenden Schritte aus:

1. Entfernen Sie auf der **IO-Erweiterungsplatine** den **Jumper, der mit den RGB-Pins verbunden ist**, um die RGB-LED von der SPI-Schnittstelle zu trennen.

   .. image:: ../img/lcd_to_mini0.jpg
      :width: 600
      :align: center


2. Führen Sie die folgenden Befehle aus, um **den Steuerdienst der RGB-LED zu deaktivieren**:

   .. code-block:: bash

      pironman5 -re false
      sudo systemctl restart pironman5.service 

Damit wird die SPI-Schnittstelle für den LCD-Bildschirm freigegeben, wodurch Konflikte oder Anzeigeprobleme vermieden werden.


**Driver Installation**

Dieses LCD-Modul erfordert die Installation eines Treibers vor der Verwendung. Die Installationsschritte variieren je nach Betriebssystem.

* Für Raspberry Pi OS können Sie den folgenden Befehl verwenden, um den Treiber zu installieren:

   .. code-block:: bash

      sudo rm -rf LCD-show 
      git clone https://github.com/sunfounder/LCD-show.git 
      chmod -R 755 LCD-show 
      cd LCD-show/ 
      sudo ./LCD35-show

   Nach erfolgreicher Ausführung wird der Raspberry Pi-Desktop auf dem 3,5-Zoll-LCD-Bildschirm angezeigt.

   Wenn Sie das Display drehen möchten, können Sie den folgenden Befehl ausführen:

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Nach der Ausführung wird das System automatisch neu gestartet, und der Bildschirm wird um 90 Grad gedreht mit korrekter Anzeige und Touch-Funktion. Sie können '90' durch 0, 90, 180 oder 270 ersetzen, um den gewünschten Drehwinkel einzustellen.

* Für Ubuntu können Sie den folgenden Befehl verwenden, um den Treiber zu installieren:

   .. code-block:: bash

      sudo rm -rf LCD-show-ubuntu 
      git clone https://github.com/sunfounder/LCD-show-ubuntu.git 
      chmod -R 755 LCD-show-ubuntu 
      cd LCD-show-ubuntu/ 
      sudo ./LCD35-show

   Nach erfolgreicher Ausführung wird der Raspberry Pi-Desktop auf dem 3,5-Zoll-LCD-Bildschirm angezeigt.

   Wenn Sie das Display drehen möchten, können Sie den folgenden Befehl ausführen:

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Nach der Ausführung wird das System automatisch neu gestartet, und der Bildschirm wird um 90 Grad gedreht mit korrekter Anzeige und Touch-Funktion. Sie können '90' durch 0, 90, 180 oder 270 ersetzen, um den gewünschten Drehwinkel einzustellen.

* Für Kali Linux können Sie den folgenden Befehl verwenden, um den Treiber zu installieren:

   .. code-block:: bash

      sudo rm -rf LCD-show-kali 
      git clone https://github.com/sunfounder/LCD-show-kali.git 
      chmod -R 755 LCD-show-kali 
      cd LCD-show-kali/ 
      sudo ./LCD35-show

   Nach erfolgreicher Ausführung wird der Raspberry Pi-Desktop auf dem 3,5-Zoll-LCD-Bildschirm angezeigt.

   Wenn Sie das Display drehen möchten, können Sie den folgenden Befehl ausführen:

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Nach der Ausführung wird das System automatisch neu gestartet, und der Bildschirm wird um 90 Grad gedreht mit korrekter Anzeige und Touch-Funktion. Sie können '90' durch 0, 90, 180 oder 270 ersetzen, um den gewünschten Drehwinkel einzustellen.
