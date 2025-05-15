Zusammenbau des Kameramoduls 
===========================================

Befolgen Sie die folgenden Schritte, um das Kameramodul korrekt zusammenzusetzen:

1. Entfernen Sie die beiden Acrylplatten aus dem Gehäuse.

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. Trennen Sie das 2-Pin-Kabel und das FPC-Kabel wie im Bild dargestellt.

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. Entfernen Sie die vier Schrauben, um die NVMe-PIP- und Power-Switch-Converter-Modulgruppe auszubauen.

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. Zerlegen Sie die Modulgruppe. Dabei muss ein Niet entfernt werden. Drücken Sie mit einem Schraubendreher die zentrale Achse des Nietes heraus und nehmen Sie anschließend den gesamten Niet heraus.

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. Verbinden Sie das Kameramodul mit dem FPC-Kabel.

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. Führen Sie das FPC-Kabel durch die KAMERA-Öffnung im Gehäuse.

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. Ziehen Sie das FPC-Kabel vollständig durch die KAMERA-Öffnung hindurch.

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. Schließen Sie das FPC-Kabel an den Raspberry Pi an. Dieser Schritt erfordert besondere Sorgfalt aufgrund des begrenzten Platzes.

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. Starten Sie den Host und prüfen Sie, ob das Kameramodul korrekt angeschlossen ist.

   * Schließen Sie zunächst ein Display an den Raspberry Pi an oder stellen Sie eine VNC-Verbindung her.
   * Sobald das Display aktiv ist, öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus: ``raspistill -o test.jpg``
   * Wenn das Kameramodul richtig funktioniert, wird ein Bild aufgenommen und unter ``test.jpg`` gespeichert.
   * Öffnen Sie ``test.jpg``, um das aufgenommene Bild zu überprüfen.

10. Setzen Sie den Power-Switch-Converter wieder in das Gehäuse ein.

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. Montieren Sie das NVMe-PIP-Modul erneut im Gehäuse.

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. Bringen Sie die Gehäuseabdeckung wieder an.

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center

