.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _cpn_camera_module:

Camera Module
====================================


**Description**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

This is a 5MP Raspberry Pi camera module with OV5647 sensor. It's plug and play, connect the included ribbon cable to the CSI (Camera Serial Interface) port on your Raspberry Pi and you're ready to go.

The board is small, about 25mm x 23mm x 9mm, and weighs 3g, making it ideal for mobile or other size and weight-critical applications. The camera module has a native resolution of 5 megapixels and has an on-board fixed focus lens that captures still images at 2592 x 1944 pixels, and also supports 1080p30, 720p60 and 640x480p90 video.

.. note:: 

   The module is only capable of capturing pictures and videos, not sound.



**Specification**

* **Static Images Resolution**: 2592×1944 
* **Supported Video Resolution**: 1080p/30 fps, 720p/ 60fps and 640 x480p 60/90 video recording 
* **Aperture (F)**: 1.8 
* **Visual Angle**: 65 degree 
* **Dimension**: 24mmx23.5mmx8mm 
* **Weight**: 3g 
* **Interface**: CSI connector 
* **Supported OS**: Raspberry Pi OS(latest version recommended) 



**Assemble the Camera Module**
-------------------------------------


On the camera module or Raspberry Pi, you will find a flat plastic connector. Carefully pull out the black fixing switch until the fixing switch is partially pulled out. Insert the FFC cable into the plastic connector in the direction shown and push the fixing switch back into place.

If the FFC wire is installed correctly, it will be straight and will not pull out when you gently pull on it. If not, reinstall it again.

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

   Do not install the camera with the power on, it may damage your camera.


   
