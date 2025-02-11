Assemblaggio del modulo fotocamera
===========================================

Seguire questi passaggi per assemblare il modulo fotocamera:

1. Rimuovere i due pannelli acrilici dalla custodia.

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. Scollegare il cavo a 2 pin e il FPC come mostrato nell'immagine.

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. Svitare le quattro viti per rimuovere il gruppo modulo NVMe PIP e il convertitore dell'interruttore di alimentazione.

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. Smontare il gruppo modulo. Ciò comporta la rimozione di un rivetto, che deve essere fatto spingendo fuori l'asta centrale del rivetto con un cacciavite, quindi rimuovendo l'intero rivetto.

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. Collegare il modulo fotocamera al cavo FPC.

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. Inserire il FPC attraverso il foro "CAMERA" della custodia.

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. Continuare a far passare il FPC attraverso il foro "CAMERA" della custodia.

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. Collegare il FPC al Raspberry Pi. Questo passaggio è molto compatto e richiede un'attenta manipolazione.

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. Accendere il dispositivo host e verificare se il modulo fotocamera è correttamente collegato.

   * Innanzitutto, collegare un display al Raspberry Pi o stabilire una connessione VNC.
   * Una volta configurato il display, aprire un terminale ed eseguire il seguente comando: ``raspistill -o test.jpg``
   * Se il modulo fotocamera funziona correttamente, questo comando acquisirà un'immagine e la salverà come ``test.jpg``.
   * Aprire ``test.jpg`` per verificare che l'immagine sia stata catturata correttamente.

10. Rimontare il convertitore dell'interruttore di alimentazione nella custodia.

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. Rimontare l'NVMe PIP nella custodia.

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. Rimontare il coperchio della custodia.

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center

