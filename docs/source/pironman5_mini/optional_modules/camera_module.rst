.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


Módulo de Cámara
===========================================

.. note::

    La serie Pironman 5 no incluye un módulo de cámara.  
    Necesitarás preparar uno por tu cuenta o comprarlo en nuestro sitio web oficial:

    * `Módulo de Cámara <https://www.sunfounder.com/products/ov5647-camera-module>`_

En esta sección, aprenderás cómo probar el módulo de cámara capturando fotos y grabando videos.

Al final de esta sección, tendrás un módulo de cámara completamente instalado y funcional listo para tus proyectos.


**Probar la Cámara**

Raspberry Pi OS (Bookworm y posteriores) utiliza la pila **libcamera**.  
Después de iniciar el sistema, ejecuta el siguiente comando para comprobar si la cámara funciona:

.. code-block:: bash

    libcamera-hello

Si ves una ventana de vista previa, la cámara está funcionando correctamente.

**Tomar una Foto**

.. code-block:: bash

    libcamera-jpeg -o test.jpg

Esto capturará una imagen fija y la guardará como ``test.jpg``.

**Grabar un Video**

.. code-block:: bash

    libcamera-vid -t 10000 -o test.h264

* ``-t 10000`` significa grabar durante 10 segundos.  
* ``-o test.h264`` guarda la salida como video H.264.

Para convertir el video a formato MP4:

.. code-block:: bash

    ffmpeg -i test.h264 -c copy test.mp4

**Ejemplo en Python**

También puedes controlar la cámara con Python usando la librería ``picamera2``.

Instala las dependencias:

.. code-block:: bash

    sudo apt install python3-picamera2 -y

Crea un archivo Python:

.. code-block:: bash

    nano camera_test.py

Luego pega el siguiente código:

.. code-block:: python

    from picamera2 import Picamera2
    import time

    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)
    picam2.capture_file("image.jpg")

Guarda y sal de nano presionando ``CTRL+O``, luego ``ENTER``, y ``CTRL+X``.

Ejecuta el script:

.. code-block:: bash

    python3 camera_test.py
