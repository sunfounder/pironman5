.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_dashboard:

通过仪表盘查看与控制
=========================================

成功安装 ``pironman5`` 模块后，系统将在重启后自动启动 ``pironman5.service`` 服务。

此时，你可以在浏览器中打开监控页面，查看树莓派的运行信息、配置 RGB 灯效、控制风扇等。访问地址为： ``http://<ip>:34001``。

该页面包含 **Dashboard（仪表盘）**、 **History（历史记录）**、 **Log（日志）** 和 **Settings（设置）** 四个子页面。

.. image:: img/dashboard_home.png


仪表盘
-----------------------

仪表盘页面通过多种卡片展示树莓派的实时状态信息，包括：

* **Temperature（温度）**：查看树莓派的 CPU/GPU 温度和 CPU 风扇转速。 **GPIO Fan State** 表示两个侧边 GPIO 风扇的运行状态。

  .. image:: img/dashboard_tem.png
    :width: 90%

* **Storage（存储）**：显示树莓派的存储容量，展示各个磁盘分区的已用与可用空间。

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Memory（内存）**：显示树莓派内存的使用情况及百分比。

  .. image:: img/dashboard_memory.png
    :width: 90%

* **Network（网络）**：显示当前的网络连接类型、上传速度和下载速度。

  .. image:: img/dashboard_network.png
    :width: 90%

* **Processor（处理器）**：展示树莓派 CPU 的性能情况，包括四个核心的状态、运行频率以及 CPU 占用率。

  .. image:: img/dashboard_processor.png
    :width: 90%


历史记录
--------------

在 History 页面中可以查看历史数据。勾选左侧栏要查看的项目，选择时间范围后即可查看该时段的记录，也可以点击下载保存。

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

日志
------------

Log 页面用于查看当前 Pironman5 服务的运行日志。

* 可按级别（Debug、Info、Warning、Error 或 Critical）筛选日志条目。
* 日志文件也可下载到本地保存。

.. image:: img/dashboard_log.png
  :width: 90%


设置
------------

Settings 页面允许你自定义仪表盘显示、系统偏好、OLED 屏幕、RGB 灯效和风扇行为。同时还显示基本的网络信息，如 MAC 地址和 IP 地址。

.. image:: img/dashboard_setting.png
    :width: 600


* **Interface（界面）**

  配置仪表盘的外观和显示行为。

  .. image:: img/dashboard_setting_interface.png
      :width: 600

  * **Dark mode（深色模式）**：启用或禁用深色主题。
  * **Show unmounted disk（显示未挂载磁盘）**：在存储卡片上显示未挂载的存储设备。
  * **Show all cores（显示所有核心）**：在处理器卡片上显示所有 CPU 核心。
  * **Card layout（卡片布局）**：自定义仪表盘的卡片布局。
  * **Temperature Unit（温度单位）**：在摄氏度和华氏度之间切换。
  * **Web UI Version（Web UI 版本）**：显示当前仪表盘的版本号。


* **OLED**

  配置 OLED 屏幕的显示和行为。

  .. image:: img/dashboard_setting_oled.png
      :width: 600

  * **OLED Enable（OLED 启用）**：启用或禁用 OLED 屏幕。
  * **OLED Rotation（OLED 旋转）**：将 OLED 显示方向在 ``0°`` 和 ``180°`` 之间切换。
  * **OLED Sleep Timeout（OLED 休眠超时）**：设置 OLED 屏幕在自动关闭前保持点亮的时间。
  * **OLED Pages（OLED 页面）**：配置 OLED 屏幕上显示的页面，并调整其显示顺序。

    可用的页面包括：

    * **IP Addresses（IP 地址）**：显示所有物理网络接口的 IP 地址。
    * **Disk Usage（磁盘使用率）**：显示所有磁盘的磁盘使用情况。
    * **Performance Metrics（性能指标）**：显示 CPU 使用率、CPU 温度、RAM 使用率和风扇转速。
    * **System Mix（系统综合）**：显示 CPU 使用率、CPU 温度和 IP 地址。


* **RGB**

  配置 RGB LED 灯效和行为。

  .. image:: img/dashboard_setting_rgb.png
      :width: 600

  * **RGB Enable（RGB 启用）**：启用或禁用 RGB LED。
  * **RGB Color（RGB 颜色）**：设置 RGB LED 的颜色。
  * **RGB Brightness（RGB 亮度）**：调整 RGB LED 的亮度。
  * **RGB Style（RGB 模式）**：选择 RGB 灯效，包括 ``None``、 ``Solid``、 ``Breathing``、 ``Flow``、 ``Flow Reverse``、 ``Rainbow``、 ``Rainbow Reverse`` 和 ``Hue Cycle``。
  * **RGB Speed（RGB 速度）**：调整所选 RGB 灯效的动画速度。
  * **RGB Led（RGB LED 数量）**：设置活跃的 RGB LED 数量。


* **GPIO Fans（GPIO 风扇）**

  配置两个 GPIO 风扇的工作模式和 LED 行为。

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  * **Fan LED（风扇 LED）**

    控制 GPIO 风扇的 RGB 灯光行为。

    * **ON**：风扇 LED 始终保持点亮。
    * **OFF**：风扇 LED 保持关闭。
    * **FOLLOW**：风扇 LED 跟随系统 RGB 灯效。

  * **GPIO Fan Mode（GPIO 风扇模式）**

    所选模式决定了 GPIO 风扇的启动温度。

    * **Quiet（静音）**：GPIO 风扇在 70°C 时启动。
    * **Balanced（均衡）**：GPIO 风扇在 67.5°C 时启动。
    * **Cool（凉爽）**：GPIO 风扇在 60°C 时启动。
    * **Performance（性能）**：GPIO 风扇在 50°C 时启动。
    * **Always On（始终开启）**：GPIO 风扇始终保持运行。


* **System（系统）**

  配置系统行为并查看设备信息。

  .. image:: img/dashboard_setting_system.png
      :width: 600

  * **Debug Level（调试级别）**：设置 Pironman 5 服务的日志记录级别。
  * **Mac Address（MAC 地址）**：显示树莓派网络接口的 MAC 地址。
  * **IP Address（IP 地址）**：显示树莓派网络接口的 IP 地址。
  * **History Retention（历史保留天数）**：设置历史数据的存储天数。
  * **Clear All Data（清除所有数据）**：清除所有记录的历史数据。
  * **Reboot（重启）**：从仪表盘远程重启树莓派。
  * **Shutdown（关机）**：从仪表盘远程安全关闭树莓派。
