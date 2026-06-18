.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _cpn_camera_module:

Modulo Fotocamera
====================================

**Descrizione**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Questo è un modulo fotocamera per Raspberry Pi da 5MP con sensore OV5647. È plug and play, collega il cavo a nastro incluso alla porta CSI (Camera Serial Interface) sul tuo Raspberry Pi e sei pronto per partire.

La scheda è piccola, circa 25mm x 23mm x 9mm, e pesa 3g, rendendola ideale per applicazioni mobili o altre applicazioni critiche per dimensioni e peso. Il modulo fotocamera ha una risoluzione nativa di 5 megapixel e ha una lente a fuoco fisso integrata che cattura immagini fisse a 2592 x 1944 pixel, e supporta anche video 1080p30, 720p60 e 640x480p90.

.. note:: 

   Il modulo è in grado solo di catturare immagini e video, non l'audio.

**Specifiche**

* **Risoluzione Immagini Fisse**: 2592×1944 
* **Risoluzione Video Supportata**: 1080p/30 fps, 720p/60fps e registrazione video 640 x480p 60/90 
* **Apertura (F)**: 1.8 
* **Angolo di Visione**: 65 gradi 
* **Dimensioni**: 24mm x 23.5mm x 8mm 
* **Peso**: 3g 
* **Interfaccia**: Connettore CSI 
* **SO Supportato**: Raspberry Pi OS (versione più recente consigliata)

**Assemblare il Modulo Fotocamera**
-------------------------------------

Sul modulo fotocamera o sul Raspberry Pi, troverai un connettore di plastica piatto. Tira fuori con cura l'interruttore di fissaggio nero finché non è parzialmente estratto. Inserisci il cavo FFC nel connettore di plastica nella direzione mostrata e spingi l'interruttore di fissaggio di nuovo in posizione.

Se il cavo FFC è installato correttamente, sarà dritto e non si sfilerà quando lo tiri delicatamente. In caso contrario, reinstalla di nuovo.

.. raw:: html

    <div style="text-align: center; margin: 16px 0;">
        <iframe width="560" height="315"
            src="https://www.youtube.com/embed/riUNPxS7sHs"
            title="Pironman 5 Pro MAX Camera Module Assembly"
            frameborder="0"
            allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
        </iframe>
    </div>

.. image:: img/connect_ffc.png

.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   Non installare la fotocamera con l'alimentazione accesa, potrebbe danneggiare la tua fotocamera.
