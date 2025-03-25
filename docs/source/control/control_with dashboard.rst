.. _view_control_dashboard:

通过仪表盘查看和控制
=========================================

成功安装 ``pironman5`` 模块后， ``pironman5.service`` 将在重启时自动启动。

现在，你可以通过浏览器打开监控页面，查看你的Raspberry Pi信息，配置RGB，控制风扇等。页面链接为： ``http://<ip>:34001`` 。

该页面包括 **仪表盘** 、 **历史记录** 、 **日志** 和 **设置** 页面。

.. image:: img/dashboard_tab_new.jpg



仪表盘
-----------------------

仪表盘中有多个卡片，展示Raspberry Pi的相关状态，包括：

* **风扇**：查看Raspberry Pi的CPU温度和PWM风扇转速。 **GPIO风扇状态** 显示两个侧面RGB风扇的状态。当前温度下，两个RGB风扇处于关闭状态。

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%


* **存储**：显示Raspberry Pi的存储容量，包括各个磁盘分区的已用空间和可用空间。

  .. image:: img/dashboard_storage.png
    :width: 90%


* **内存**：显示Raspberry Pi的RAM使用情况和百分比。

  .. image:: img/dashboard_memory.png
    :width: 90%


* **网络**：显示当前的网络连接类型，以及上传和下载速度。

  .. image:: img/dashboard_network.png
    :width: 90%


* **处理器**：展示Raspberry Pi的CPU性能，包括四个核心的状态、工作频率和CPU使用率。

  .. image:: img/dashboard_processor.png
    :width: 90%


历史记录
--------------

历史记录页面允许你查看历史数据。通过左侧边栏选择你想查看的数据，然后选择时间范围查看该时间段的数据，亦可点击下载。

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

日志
------------

日志页面用于查看当前正在运行的Pironman5服务的日志。Pironman5服务包括多个子服务，每个子服务都有自己的日志。选择你要查看的日志，你可以在右侧查看日志数据。如果日志为空，可能表示没有日志内容。

* 每个日志的大小为10MB，当超过此大小时，会自动创建第二个日志。
* 同一服务的日志数量限制为10个。如果数量超过此限制，最旧的日志将被自动删除。你也可以手动删除日志。
* 日志区域右上方有过滤工具。你可以选择日志级别，按关键字过滤，并使用一些便捷工具，包括 **换行/Line Wrap** 、 **自动滚动/Auto Scroll** 和 **自动更新/Auto Update** 。
* 日志也可以下载到本地。

.. image:: img/dashboard_log1.png
  :width: 90%

.. image:: img/dashboard_log2.png
  :width: 90%

设置
-----------------

页面右上角有一个设置菜单，你可以根据个人喜好自定义设置。修改后，系统会自动保存更改。如有需要，你可以点击底部的CLEAR按钮清除历史数据。

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **暗黑模式/Dark Mode**：切换明暗模式主题。主题选项会保存在浏览器缓存中，换浏览器或清除缓存后会恢复为默认的明亮主题。
* **温度单位/Temperature Unit**：设置系统显示的温度单位。

**关于OLED屏幕**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **启用OLED/OLED Enable**：是否启用OLED。
* **OLED磁盘/OLED Disk**：设置OLED磁盘。
* **OLED网络接口/OLED Network Interface**：

  * **all**：依次显示以太网IP和Wi-Fi IP。
  * **eth0**：仅显示以太网IP。
  * **wlan0**：仅显示Wi-Fi IP。

* **OLED旋转/OLED Rotation**：设置OLED旋转角度。

**关于RGB LED**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **启用RGB/RGB Enable**：是否启用RGB LED。
* **RGB颜色/RGB Color**：设置RGB LED的颜色。
* **RGB亮度/RGB Brightness**：你可以通过滑块调整RGB LED的亮度。
* **RGB样式/RGB Style**：选择RGB LED显示模式。选项包括 **固态/Solid** 、 **呼吸/Breathing** 、 **流动/Flow** 、 **反向流动/Flow_reverse** 、 **彩虹/Rainbow** 、 **反向彩虹/Rainbow Reverse** 和 **色相循环/Hue Cycle** 。

  .. note::

     如果将 **RGB样式/RGB Style** 设置为 **彩虹/Rainbow**、 **反向彩虹/Rainbow Reverse** 和 **色相循环/Hue Cycle** ，你将无法设置颜色。

* **RGB速度/RGB Speed**：设置RGB LED变化的速度。

**关于RGB风扇**

.. image:: img/RGB_FAN2.png
  :width: 600

.. * **Fan LED**: You can set the FAN LED to ON, OFF, or FOLLOW mode.

* **GPIO风扇模式/GPIO Fan Mode**：你可以设置两个RGB风扇的工作模式，这些模式决定了RGB风扇的启用条件。

    * **静音/Quiet**：RGB风扇在70°C时启动。
    * **平衡/Balanced**：RGB风扇在67.5°C时启动。
    * **冷却/Cool**：RGB风扇在60°C时启动。
    * **高性能/Performance**：RGB风扇在50°C时启动。
    * **常开/Always On**：RGB风扇始终开启。

例如，如果设置为 **Performance/高性能** 模式，RGB风扇将在50°C时启动。

保存后，如果CPU温度超过50°C，你将在仪表盘中看到 **GPIO风扇状态** 变为开启，两个侧面RGB风扇将开始旋转。

.. image:: img/dashboard_rgbfan_on.png
  :width: 300







