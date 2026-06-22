.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _cpn_camera_module:

Módulo de Cámara
====================================

**Descripción**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Este es un módulo de cámara de 5MP para Raspberry Pi con sensor OV5647. Es plug-and-play, conecte el cable plano incluido al puerto CSI (Interfaz Serial de Cámara) de su Raspberry Pi y estará listo para funcionar.

La placa es pequeña, de aproximadamente 25mm x 23mm x 9mm, y pesa 3g, lo que la hace ideal para aplicaciones móviles o con restricciones de tamaño y peso. El módulo de cámara tiene una resolución nativa de 5 megapíxeles y un lente de enfoque fijo integrado que captura imágenes fijas a 2592 x 1944 píxeles, y también soporta video a 1080p30, 720p60 y 640x480p90.

.. note::

   El módulo solo es capaz de capturar imágenes y videos, no sonido.

**Especificaciones**

* **Resolución de Imágenes Fijas**: 2592×1944
* **Resolución de Video Soportada**: 1080p/30 fps, 720p/60fps y grabación de video a 640x480p 60/90
* **Apertura (F)**: 1.8
* **Ángulo Visual**: 65 grados
* **Dimensiones**: 24mm x 23.5mm x 8mm
* **Peso**: 3g
* **Interfaz**: Conector CSI
* **SO Soportado**: Raspberry Pi OS (se recomienda la última versión)

**Ensamblar el Módulo de Cámara**
-------------------------------------

En el módulo de cámara o en la Raspberry Pi, encontrará un conector de plástico plano. Extraiga con cuidado el interruptor de fijación negro hasta que quede parcialmente extraído. Inserte el cable FFC en el conector de plástico en la dirección mostrada y vuelva a colocar el interruptor de fijación en su lugar.

Si el cable FFC está instalado correctamente, quedará recto y no se saldrá cuando tire suavemente de él. Si no es así, vuelva a instalarlo.

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

   No instale la cámara con la alimentación encendida, ya que podría dañar su cámara.