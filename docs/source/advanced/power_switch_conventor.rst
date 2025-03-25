Power Switch Converter
==============================

这是一个将Raspberry Pi 5的电源开关扩展到外部的模块。

.. image:: img/power_switch_conventor.jpeg

**添加电源按钮**

* Raspberry Pi 5配有一个 **J2** 跳线，位于RTC电池连接器与板边之间。通过连接一个常开（NO）瞬时开关到两个焊盘之间，可以为Raspberry Pi 5添加自定义电源按钮。短暂按下该开关，可以模拟板载电源按钮的功能。

   .. image:: img/pi5_j2.jpg

* 在Pironman 5上，有一个 **电源开关转换器** ，它通过两个Pogo针将 **J2** 跳线扩展到外部电源按钮。

   .. image:: img/power_switch_convertor.png

* 现在，可以使用电源按钮打开和关闭Raspberry Pi 5。

   .. image:: img/pironman_button.JPG

**电源循环**

在首次为Raspberry Pi 5供电时，它会自动开机并启动操作系统，无需按下按钮。

如果运行Raspberry Pi Desktop，简短按下电源按钮将启动干净的关机过程。将出现一个菜单，提供关机、重启或注销的选项。选择一个选项或再次按下电源按钮将启动干净的关机。

.. image:: img/button_shutdown.png

**关机**

    * 如果你运行的是Raspberry Pi **Bookworm Desktop** 系统，可以快速连续按下电源按钮两次进行关机。
    * 如果你运行的是没有桌面的Raspberry Pi **Bookworm Lite** 系统，按一次电源按钮即可启动关机。
    * 要强制硬关机，按住电源按钮。

**开机**

    * 如果Raspberry Pi板已关机，但仍有电源供应，单次按下按钮即可从关机状态开机。

.. note::

    如果你运行的系统不支持关机按钮，你可以按住电源按钮5秒钟以强制硬关机，并单次按下按钮从关机状态开机。

