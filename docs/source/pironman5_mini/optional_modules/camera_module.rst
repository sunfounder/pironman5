摄像头模块
===========================================

.. note::

    Pironman 5 系列产品不包含摄像头模块。  
    你需要自行准备，或在我们的官方网站购买：

    * `摄像头模块 <https://www.sunfounder.com/products/ov5647-camera-module>`_

在本章节中，你将学习如何测试摄像头模块，包括拍照和录像。

完成本章节后，你将拥有一个完整安装并可正常使用的摄像头模块，随时可以投入项目使用。


**测试摄像头**

Raspberry Pi OS（Bookworm 及以后版本）使用 **libcamera** 驱动。  
启动系统后，运行以下命令测试摄像头：

.. code-block:: bash

    libcamera-hello

如果能看到预览窗口，说明摄像头工作正常。

**拍照**

.. code-block:: bash

    libcamera-jpeg -o test.jpg

此命令会拍摄一张照片，并保存为 ``test.jpg``。

**录像**

.. code-block:: bash

    libcamera-vid -t 10000 -o test.h264

* ``-t 10000`` 表示录像 10 秒。  
* ``-o test.h264`` 将输出保存为 H.264 视频。  

如需转换为 MP4 格式：

.. code-block:: bash

    ffmpeg -i test.h264 -c copy test.mp4

**Python 示例**

你也可以通过 Python 使用 ``picamera2`` 库控制摄像头。

安装依赖：

.. code-block:: bash

    sudo apt install python3-picamera2 -y

创建一个 Python 文件：

.. code-block:: bash

    nano camera_test.py

将以下代码粘贴进去：

.. code-block:: python

    from picamera2 import Picamera2
    import time

    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)
    picam2.capture_file("image.jpg")

在 nano 中保存并退出，按 ``CTRL+O`` → ``ENTER`` → ``CTRL+X``。

运行脚本：

.. code-block:: bash

    python3 camera_test.py
