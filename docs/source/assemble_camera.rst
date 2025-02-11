Zusammenbau des Kameramoduls
===========================================

Befolgen Sie diese Schritte, um das Kameramodul zusammenzubauen:

1. Entfernen Sie die beiden Acrylplatten aus dem Gehäuse.

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. Trennen Sie das 2-Pin-Kabel und das FPC, wie im Bild gezeigt.

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. Lösen Sie die vier Schrauben, um die NVMe PIP- und Power-Switch-Converter-Modulgruppe zu entfernen.

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. Zerlegen Sie die Modulgruppe. Dabei muss ein Niet entfernt werden. Drücken Sie dazu mit einem Schraubendreher die zentrale Achse des Nietes heraus und entfernen Sie anschließend den gesamten Niet.

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. Verbinden Sie das Kameramodul mit dem FPC-Kabel.

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. Führen Sie das FPC durch die KAMERA-Öffnung im Gehäuse.

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. Führen Sie das FPC weiter durch die KAMERA-Öffnung im Gehäuse.

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. Verbinden Sie das FPC mit dem Raspberry Pi. Dieser Schritt ist sehr kompakt und erfordert sorgfältige Handhabung.

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. Schalten Sie den Host ein und überprüfen Sie, ob das Kameramodul ordnungsgemäß angeschlossen ist.

   * Schließen Sie zunächst ein Display an den Raspberry Pi an oder stellen Sie eine VNC-Verbindung her.
   * Sobald das Display eingerichtet ist, öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus: ``raspistill -o test.jpg``
   * Wenn das Kameramodul ordnungsgemäß funktioniert, nimmt dieser Befehl ein Bild auf und speichert es als ``test.jpg``.
   * Öffnen Sie ``test.jpg``, um zu überprüfen, ob das Bild erfolgreich aufgenommen wurde.

10. Bauen Sie den Power-Switch-Converter wieder in das Gehäuse ein.

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. Bauen Sie das NVMe PIP wieder in das Gehäuse ein.

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. Setzen Sie die Gehäuseabdeckung wieder zusammen.

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center

