.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_view_control_dashboard:

通过 Dashboard 查看与控制
=========================================

成功安装 ``pironman5`` 模块后，\ ``pironman5.service`` 会在系统重启时自动启动。

现在您可以在浏览器中打开监控页面，查看 Raspberry Pi 的相关信息、配置 RGB 等。页面地址为： ``http://<ip>:34001``\ 。

.. image:: img/dashboard_prm5promax.png
  :width: 90%


该页面包含 **Dashboard**\ 、\ **History**\ 、\ **Log** 和 **Settings** 四个主要页面。


.. image:: img/dashboard_tab.png
  :width: 90%
  
Dashboard
-----------------------

该页面包含多个信息卡片，用于查看 Raspberry Pi 的运行状态，包括：

* **Temperature**\ ：查看 Raspberry Pi 的 CPU 和 GPU 温度。

  .. image:: img/dashboard_temp.png
    :align: center
    

* **Storage**\ ：显示 Raspberry Pi 的存储容量，包括各磁盘分区的已用空间和可用空间。

  .. image:: img/dashboard_storage.png
    :align: center
    

* **Memory**\ ：显示 Raspberry Pi 的内存使用情况及使用比例。

  .. image:: img/dashboard_memory.png
    :align: center
    

* **Network**\ ：显示当前网络连接类型、上传速度和下载速度。

  .. image:: img/dashboard_network.png
    :align: center
    

* **Processor**\ ：展示 Raspberry Pi 的 CPU 运行状态，包括四个核心的状态、运行频率以及 CPU 使用率。

  .. image:: img/dashboard_processor.png
    :align: center
    

History
--------------

History 页面用于查看历史数据。  
在左侧栏中选择要查看的数据类型，然后选择时间范围即可查看对应时间段的数据，同时也可以点击下载数据。

.. image:: img/dashboard_history1.png
  :width: 90%
  
.. image:: img/dashboard_history2.png
  :width: 90%


Log
------------

Log 页面用于查看当前运行的 Pironman5 服务日志。Pironman5 服务包含多个子服务，每个子服务都有独立的日志文件。选择需要查看的日志后，右侧会显示对应的日志内容。如果为空，说明当前没有日志记录。

* 每个日志文件大小固定为 10MB。当超过该大小时，会生成新的日志文件。
* 每个服务最多保留 10 个日志文件。超过该数量时，最旧的日志会被自动删除。
* 日志区域上方提供筛选工具，可以选择日志级别、按关键字过滤，并提供一些辅助功能，包括 **Line Wrap**\ 、\ **Auto Scroll** 和 **Auto Update**\ 。
* 日志也可以下载到本地。

.. image:: img/dashboard_log1.png
  :width: 90%
  
.. image:: img/dashboard_log2.png
  :width: 90%


Settings
-----------------

页面 **右上角** 提供设置菜单，您可以根据需要自定义配置。修改后设置会自动保存。如有需要，可以点击底部的 **CLEAR** 按钮清除历史数据。

.. image:: img/dashboard_setting_darkmode.png
  :width: 600

* **Dark Mode**\ ：在浅色主题和深色主题之间切换。主题设置保存在浏览器缓存中，更换浏览器或清除缓存后将恢复为默认浅色主题。
* **Show Unmounted Disk**\ ：是否在仪表板中显示未挂载的磁盘。
* **Show All Cores**\ ：是否在仪表板中显示所有 CPU 核心。
* **Card layout**\ ：设置仪表板卡片布局。
* **Temperature Unit**\ ：设置系统显示的温度单位。

**关于 OLED 屏幕**

.. image:: img/dashboard_setting_oled.png
  :width: 600

* **OLED Enable**\ ：是否启用 OLED 显示。
* **OLED Rotation**\ ：设置 OLED 屏幕旋转方向。
* **OLED Sleep Timeout**\ ：设置 OLED 自动休眠时间。

* **OLED Page**\ ：设置 OLED 循环显示的页面，包括 **System Mix**\ 、\ **Performance Metrics**\ 、\ **Disk Usage**\ 、\ **IP Addresses**\ 。



**关于 RGB 灯**

.. image:: img/dashboard_setting_rgb.png
  :width: 600

* **RGB Enable**\ ：是否启用 RGB LED。
* **RGB Color**\ ：设置 RGB LED 的颜色。
* **RGB Brightness**\ ：通过滑块调节 RGB LED 的亮度。
* **RGB Style**\ ：选择 RGB LED 的显示模式，可选 **Solid**\ 、\ **Breathing**\ 、\ **Flow**\ 、\ **Flow_reverse**\ 、\ **Rainbow**\ 、\ **Rainbow Reverse**\ 、\ **Hue Cycle**\ 。
* **RGB Speed**\ ：设置 RGB 动画变化速度。
* **RGB Led**\ ：设置需要控制的 RGB LED 数量。


**关于数据**

.. image:: img/dashboard_setting_debug.png
  :width: 600

* **Debug Level**\ ：设置日志级别，可选 **Info**\ 、\ **Warning**\ 、\ **Error**\ 、\ **Critical**\ 。
* **History Retention**\ ：设置历史数据保存的天数。
* **Clear All Data**\ ：清除所有历史数据。
* **Reboot**\ ：重启系统。
* **Shutdown**\ ：关闭系统。
* **Restart service**\ ：重启系统服务。


**风扇**

风扇通过 Raspberry Pi 5 上的专用 4 针 PWM 风扇接口连接。其默认控制策略为基于 CPU 温度的固件级多档智能调速机制。这意味着，当您使用官方或兼容的 PWM 风扇并正确连接后，系统会根据 CPU 温度变化自动调节风扇转速（约在 50°C 以上开始工作），无需手动干预。 

