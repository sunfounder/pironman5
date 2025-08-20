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

En esta sección aprenderás a:

* Desarmar el Pironman 5.  
* Instalar el módulo de cámara en la Raspberry Pi 5.  
* Reensamblar la carcasa.  
* Probar el módulo de cámara capturando fotos y grabando videos.

Al final de esta sección, tendrás un módulo de cámara completamente instalado y funcional listo para tus proyectos.

Ensamblar el Módulo de Cámara
------------------------------------

Sigue estos pasos para ensamblar el Módulo de Cámara:

1. Retira los dos paneles acrílicos de la carcasa.

   .. image:: img/IN.CMR.1.png
      :align: center

2. Desconecta el cable de 2 pines y el FPC como se muestra en la imagen.

   .. image:: img/IN.CMR.2.png
      :align: center

3. Desatornilla los cuatro tornillos para retirar el grupo de módulos NVMe PIP y el Convertidor de Interruptor de Encendido.

   .. image:: img/IN.CMR.3.png
      :align: center

4. Desarma el grupo de módulos. Esto implica quitar un remache, lo cual debe hacerse empujando el eje central del remache con un destornillador y luego retirando todo el remache.

   .. image:: img/IN.CMR.4.png
      :align: center

5. Conecta el Módulo de Cámara al cable FPC.

   .. image:: img/IN.CMR.5.png
      :align: center

6. Pasa el FPC a través del orificio **CAMERA** de la carcasa.

   .. image:: img/IN.CMR.6.png
      :align: center

7. Continúa pasando el FPC a través del orificio **CAMERA** de la carcasa.

   .. image:: img/IN.CMR.7.png
      :align: center

8. Conecta el FPC a la Raspberry Pi. Este paso es muy compacto y requiere un manejo cuidadoso.

   .. image:: img/IN.CMR.8.png
      :align: center

9. Enciende la Raspberry Pi 5 y verifica si el Módulo de Cámara está conectado correctamente.

   * Primero, conecta una pantalla a la Raspberry Pi o establece una conexión VNC.  
   * Después de iniciar el sistema, ejecuta el siguiente comando para comprobar si la cámara funciona: ``libcamera-hello``  
   * Si ves una ventana de vista previa, la cámara está funcionando correctamente.

10. Vuelve a ensamblar el Convertidor de Interruptor de Encendido en la carcasa.

   .. image:: img/IN.CMR.9.png
      :align: center

   .. image:: img/IN.CMR.10.png
      :align: center

11. Vuelve a ensamblar el NVMe PIP en la carcasa.

   .. image:: img/IN.CMR.11.png
      :align: center

   .. image:: img/IN.CMR.12.png
      :align: center

12. Vuelve a ensamblar la tapa de la carcasa.

   .. image:: img/IN.CMR.13.png
      :align: center


Usar el Módulo de Cámara
---------------------------

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
