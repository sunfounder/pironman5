.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Camera Module
===========================================

.. note::

    The Pironman 5 series does not include a camera module.  
    You will need to prepare one yourself or purchase it from our official website:

    * `Camera Module <https://www.sunfounder.com/products/ov5647-camera-module>`_

In this section, you will learn how to:

* Disassemble the Pironman 5.  
* Install the camera module onto the Raspberry Pi 5.  
* Reassemble the case.  
* Test the camera module by capturing photos and recording videos.

By the end of this section, you will have a fully installed and functional camera module ready for your projects.

Assemble the Camera Module
------------------------------------

Follow these steps to assemble the Camera Module:

1. Remove the two acrylic panels from the case.

   .. image:: img/IN.CMR.1.png
      :align: center

2. Detach the 2-pin wire and FPC as shown in the image.

   .. image:: img/IN.CMR.2.png
      :align: center

3. Unscrew the four screws to remove the NVMe PIP and Power Switch Converter module group.

   .. image:: img/IN.CMR.3.png
      :align: center

4. Disassemble the module group. This involves removing a rivet, which should be done by pushing the central shaft of the rivet out with a screwdriver, then removing the entire rivet.

   .. image:: img/IN.CMR.4.png
      :align: center

5. Connect the Camera Module to the FPC cable.

   .. image:: img/IN.CMR.5.png
      :align: center

6. Thread the FPC through the CAMERA hole in the case.

   .. image:: img/IN.CMR.6.png
      :align: center

7. Continue to thread the FPC through the CAMERA hole in the case.

   .. image:: img/IN.CMR.7.png
      :align: center

8. Connect the FPC to the Raspberry Pi. This step is very compact and requires careful handling.

   .. image:: img/IN.CMR.8.png
      :align: center

9. Power on the Raspberry Pi 5 and check if the Camera Module is properly connected.

   * First, connect a display to the Raspberry Pi or establish a VNC connection.
   * After booting into the system, run the following command to check if the camera works: ``libcamera-hello``
   * If you see a preview window, the camera is working correctly.

10. Reassemble the Power Switch Converter back into the case.

   .. image:: img/IN.CMR.9.png
      :align: center

   .. image:: img/IN.CMR.10.png
      :align: center

11. Reassemble the NVMe PIP back into the case.

   .. image:: img/IN.CMR.11.png
      :align: center

   .. image:: img/IN.CMR.12.png
      :align: center

12. Reassemble the case cover.

   .. image:: img/IN.CMR.13.png
      :align: center


Use the Camera Module
---------------------------

**Test the Camera**

Raspberry Pi OS (Bookworm and later) uses the **libcamera** stack.  
After booting into the system, run the following command to check if the camera works:

.. code-block:: bash

    libcamera-hello

If you see a preview window, the camera is working correctly.

**Take a Photo**

.. code-block:: bash

    libcamera-jpeg -o test.jpg

This will capture a still image and save it as ``test.jpg``.

**Record a Video**

.. code-block:: bash

    libcamera-vid -t 10000 -o test.h264

* ``-t 10000`` means recording for 10 seconds.
* ``-o test.h264`` saves the output as H.264 video.

To convert the video to MP4 format:

.. code-block:: bash

    ffmpeg -i test.h264 -c copy test.mp4

**Python Example**

You can also control the camera with Python using the ``picamera2`` library.

Install dependencies:

.. code-block:: bash

    sudo apt install python3-picamera2 -y

Create a Python file:

.. code-block:: bash

    nano camera_test.py

Then paste the following code:

.. code-block:: python

    from picamera2 import Picamera2
    import time

    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)
    picam2.capture_file("image.jpg")

Save and exit nano by pressing ``CTRL+O``, then ``ENTER``, and ``CTRL+X``.

Run the script:

.. code-block:: bash

    python3 camera_test.py

