
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _view_control_dashboard_mini:

通过控制面板查看和控制
========================

成功安装 ``pironman5`` 模块后，\ ``pironman5.service`` 将在重启时自动启动。

现在，您可以在浏览器中打开监控页面，查看 Raspberry Pi 的信息、配置 RGB 以及控制风扇等。页面链接为：\ ``http://<ip>:34001``\ 。

此页面包含\ **仪表盘**\ 、\ **历史记录**\ 、\ **日志**\ 和\ **设置**\ 页面。

.. image:: img/dashboard_tab.png
  :width: 90%


仪表盘
---------

页面提供多个卡片，用于查看 Raspberry Pi 的相关状态，包括：

* **风扇**\ ：查看 Raspberry Pi 的 CPU 温度和 PWM 风扇转速。\ **GPIO 风扇状态**\ 指示 RGB 风扇的状态。在当前温度下，RGB 风扇处于关闭状态。

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%


* **存储**\ ：显示 Raspberry Pi 的存储容量，展示各个磁盘分区的已用和可用空间。

  .. image:: img/dashboard_storage.png
    :width: 90%


* **内存**\ ：显示 Raspberry Pi 的 RAM 使用量和百分比。

  .. image:: img/dashboard_memory.png
    :width: 90%


* **网络**\ ：显示当前网络连接类型、上传和下载速度。

  .. image:: img/dashboard_network.png
    :width: 90%


* **处理器**\ ：展示 Raspberry Pi 的 CPU 性能，包括四个核心的状态、运行频率和 CPU 使用率百分比。

  .. image:: img/dashboard_processor.png
    :width: 90%


历史记录
-----------

历史记录页面可让您查看历史数据。在左侧边栏中选择要查看的数据，然后选择时间范围以查看该时段的数据，您还可以点击下载。

.. image:: img/dashboard_history.png
  :width: 90%


日志
------

日志页面用于查看当前运行的 pironman5 服务的日志。pironman5 服务包含多个子服务，每个子服务都有各自的日志。选择要查看的日志，即可在右侧查看日志数据。如果显示空白，可能表示没有日志内容。

* 每个日志文件固定大小为 10MB。超出此大小时，将创建第二个日志文件。
* 同一服务的日志数量限制为 10 个。超出此数量时，最早的日志将被自动删除。
* 右侧日志区域上方提供过滤工具，您可以选择日志级别、按关键词筛选，以及使用多个便捷工具，包括\ **自动换行**\ 、\ **自动滚动**\ 和\ **自动更新**\ 。
* 日志也可以下载到本地。

.. image:: img/dashboard_log.png
  :width: 90%


设置
------

页面右上角有一个设置菜单。

.. note::

    修改后，您需要点击底部的\ **保存**\ 按钮来保存设置。

.. image:: img/dashboard_settings.png
  :width: 90%


* **深色模式**\ ：在浅色和深色主题之间切换。主题选项保存在浏览器缓存中。更换浏览器或清除缓存将恢复为默认的浅色主题。
* **温度单位**\ ：设置系统显示的温度单位。
* **风扇模式**\ ：您可以设置 RGB 风扇的工作模式。这些模式决定了 RGB 风扇的启动条件。

    * **静音**\ ：RGB 风扇在 70°C 时启动。
    * **平衡**\ ：RGB 风扇在 67.5°C 时启动。
    * **冷却**\ ：RGB 风扇在 60°C 时启动。
    * **性能**\ ：RGB 风扇在 50°C 时启动。
    * **常开**\ ：RGB 风扇始终保持运行。

    例如，如果设置为\ **性能**\ 模式，RGB 风扇将在 50°C 时启动。

    保存后，如果 CPU 温度超过 50°C，您将在仪表盘中看到 **GPIO 风扇状态**\ 变为 ON，RGB 风扇将开始转动。

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300


* **RGB 亮度**\ ：您可以通过滑块调节 RGB LED 的亮度。
* **RGB 颜色**\ ：设置 RGB LED 的颜色。
* **RGB 样式**\ ：选择 RGB LED 的显示模式。选项包括 **Solid**\ 、\ **Breathing**\ 、\ **Flow**\ 、\ **Flow_reverse**\ 、\ **Rainbow**\ 、\ **Rainbow Reverse** 和 **Hue Cycle**\ 。

.. note::

  如果将 **RGB 样式**\ 设置为 **Rainbow**\ 、\ **Rainbow Reverse** 和 **Hue Cycle**\ ，则无法设置颜色。


* **RGB 速度**\ ：设置 RGB LED 变化的速度。

**关于核心风扇**

核心风扇连接到 Raspberry Pi 5 专用的 4 针 PWM 风扇接口。其默认控制策略是基于 CPU 温度的固件管理多级智能调速方案。这意味着当您使用官方或兼容的 PWM 风扇并正确连接后，系统将根据 CPU 温度的变化自动调节风扇转速（50°C 以上开始运行），无需您进行任何手动干预。
