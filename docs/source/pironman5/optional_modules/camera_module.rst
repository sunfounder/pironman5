摄像头模块
===========================================

.. note::

    Pironman 5 系列产品不包含摄像头模块。  
    你需要自行准备，或在我们的官方网站购买：

    * `摄像头模块 <https://www.sunfounder.com/products/ov5647-camera-module>`_

在本章节中，你将学习如何：

* 拆开 Pironman 5。  
* 将摄像头模块安装到树莓派 5。  
* 重新组装机箱。  
* 测试摄像头模块，包括拍照和录像。

完成本章节后，你将拥有一个完整安装并可正常使用的摄像头模块，随时可以投入项目使用。

组装摄像头模块
------------------------------------

按照以下步骤组装摄像头模块：

1. 从机箱上取下两块亚克力面板。

   .. image:: img/IN.CMR.1.png
      :align: center

2. 如图所示，拔下 2Pin 线和 FPC 线。

   .. image:: img/IN.CMR.2.png
      :align: center

3. 拆下固定 NVMe PIP 和电源开关转换模块组的四颗螺丝。

   .. image:: img/IN.CMR.3.png
      :align: center

4. 拆解模块组。这需要先移除一个铆钉，可以用螺丝刀将铆钉的中心轴顶出，再取下整个铆钉。

   .. image:: img/IN.CMR.4.png
      :align: center

5. 将摄像头模块连接到 FPC 线缆。

   .. image:: img/IN.CMR.5.png
      :align: center

6. 将 FPC 穿过机箱上的 CAMERA 孔。

   .. image:: img/IN.CMR.6.png
      :align: center

7. 继续将 FPC 完全穿过 CAMERA 孔。

   .. image:: img/IN.CMR.7.png
      :align: center

8. 将 FPC 连接到树莓派。此步骤空间较小，需要小心操作。

   .. image:: img/IN.CMR.8.png
      :align: center

9. 启动树莓派 5，检查摄像头模块是否正确连接。

   * 先连接显示器或通过 VNC 远程登录。  
   * 进入系统后，运行以下命令测试摄像头： ``libcamera-hello``  
   * 如果能看到预览窗口，说明摄像头工作正常。

10. 将电源开关转换模块重新安装回机箱。

   .. image:: img/IN.CMR.9.png
      :align: center

   .. image:: img/IN.CMR.10.png
      :align: center

11. 将 NVMe PIP 模块重新安装回机箱。

   .. image:: img/IN.CMR.11.png
      :align: center

   .. image:: img/IN.CMR.12.png
      :align: center

12. 装回机箱盖板。

   .. image:: img/IN.CMR.13.png
      :align: center


使用摄像头模块
---------------------------

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
