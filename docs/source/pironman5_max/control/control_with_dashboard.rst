
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_dashboard:

通过控制面板查看和控制
========================

成功安装 ``pironman5`` 模块后，\ ``pironman5.service`` 将在重启时自动启动。

现在，您可以在浏览器中打开监控页面，查看 Raspberry Pi 的信息、配置 RGB 以及控制风扇等。页面链接为：\ ``http://<ip>:34001``\ 。

此页面包含\ **仪表盘**\ 、\ **历史记录**\ 、\ **日志**\ 和\ **设置**\ 页面。

.. image:: img/dashboard_home.png


仪表盘
---------

页面提供多个卡片，用于查看 Raspberry Pi 的相关状态，包括：

* **温度**\ ：查看 Raspberry Pi 的 CPU/GPU 温度和 CPU 风扇转速。\ **GPIO 风扇状态**\ 显示两侧 GPIO 风扇的状态。

  .. image:: img/dashboard_tem.png
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

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

日志
------

日志页面显示 Pironman5 服务的运行日志。

* 可按级别（调试、信息、警告、错误或严重）过滤日志条目。
* 日志文件也可以下载到本地。

.. image:: img/dashboard_log.png
  :width: 90%

设置
------

设置页面允许您自定义仪表盘显示、系统偏好、OLED 屏幕、RGB 灯效和风扇行为。它还显示基本的网络信息，如 MAC 地址和 IP 地址。

.. image:: img/dashboard_setting.png
    :width: 600


* **界面**

  配置仪表盘的外观和显示行为。

  .. image:: img/dashboard_setting_interface.png
      :width: 600

  * **深色模式**\ ：启用或禁用深色主题。
  * **显示未挂载磁盘**\ ：在存储卡片上显示未挂载的存储设备。
  * **显示所有核心**\ ：在处理器卡片上显示所有 CPU 核心。
  * **卡片布局**\ ：自定义仪表盘卡片布局。
  * **温度单位**\ ：在摄氏度和华氏度之间切换。
  * **Web UI 版本**\ ：显示当前仪表盘版本。


* **OLED**

  配置 OLED 屏幕显示和行为。

  .. image:: img/dashboard_setting_oled.png
      :width: 600

  * **OLED 启用**\ ：启用或禁用 OLED 屏幕。
  * **OLED 旋转**\ ：将 OLED 显示旋转 ``0°`` 或 ``180°``\ 。
  * **OLED 休眠超时**\ ：设置 OLED 屏幕在自动关闭前保持点亮的时间。
  * **OLED 页面**\ ：配置在 OLED 屏幕上显示的页面并调整其显示顺序。

    可用页面包括：

    * **IP 地址**\ ：显示所有物理网络接口的 IP 地址。
    * **磁盘使用情况**\ ：显示所有磁盘的磁盘使用信息。
    * **性能指标**\ ：显示 CPU 使用率、CPU 温度、RAM 使用率和风扇转速。
    * **系统综合**\ ：显示 CPU 使用率、CPU 温度和 IP 地址。


* **RGB**

  配置 RGB LED 灯效和行为。

  .. image:: img/dashboard_setting_rgb.png
      :width: 600

  * **RGB 启用**\ ：启用或禁用 RGB LED。
  * **RGB 颜色**\ ：设置 RGB LED 颜色。
  * **RGB 亮度**\ ：调节 RGB LED 亮度。
  * **RGB 样式**\ ：选择 RGB 灯效，包括 ``None``\ 、\ ``Solid``\ 、\ ``Breathing``\ 、\ ``Flow``\ 、\ ``Flow Reverse``\ 、\ ``Rainbow``\ 、\ ``Rainbow Reverse`` 和 ``Hue Cycle``\ 。
  * **RGB 速度**\ ：调节所选 RGB 效果的动画速度。
  * **RGB LED**\ ：设置活动的 RGB LED 数量。


* **GPIO 风扇**

  配置两个 GPIO 风扇的工作模式和 LED 行为。

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  * **风扇 LED**

    控制 GPIO 风扇的 RGB 灯效。

    * **ON**\ ：风扇 LED 始终保持点亮。
    * **OFF**\ ：风扇 LED 保持关闭。
    * **FOLLOW**\ ：风扇 LED 跟随系统 RGB 灯效。

  * **GPIO 风扇模式**

    所选模式决定了 GPIO 风扇的启动条件。

    * **静音**\ ：GPIO 风扇在 70°C 时启动。
    * **平衡**\ ：GPIO 风扇在 67.5°C 时启动。
    * **冷却**\ ：GPIO 风扇在 60°C 时启动。
    * **性能**\ ：GPIO 风扇在 50°C 时启动。
    * **常开**\ ：GPIO 风扇始终保持运行。


* **系统**

  配置系统行为并查看设备信息。

  .. image:: img/dashboard_setting_system.png
      :width: 600

  * **调试级别**\ ：设置 Pironman 5 服务的日志级别。
  * **MAC 地址**\ ：显示 Raspberry Pi 网络接口的 MAC 地址。
  * **IP 地址**\ ：显示 Raspberry Pi 网络接口的 IP 地址。
  * **历史保留天数**\ ：设置历史数据的保存天数。
  * **清除所有数据**\ ：清除所有记录的历史数据。
  * **重启**\ ：通过仪表盘远程重启 Raspberry Pi。
  * **关机**\ ：通过仪表盘远程安全关闭 Raspberry Pi。
