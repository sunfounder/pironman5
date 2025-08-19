.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Camera Module
===========================================

.. note::

    The Pironman 5 series does not include a camera module.  
    You will need to prepare one yourself or purchase it from our official website:

    * `Camera Module <https://www.sunfounder.com/products/ov5647-camera-module>`_

In this section, you will learn how to test the camera module by capturing photos and recording videos.

By the end of this section, you will have a fully installed and functional camera module ready for your projects.


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

