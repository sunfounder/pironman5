电源开关扩展器
==============================

这是一个用于将 Raspberry Pi 5 电源开关引出至外部的模块。

.. image:: img/power_switch_conventor.jpeg

**添加电源按钮**

* Raspberry Pi 5 板载了一个 **J2** 跳线口，位于 RTC 电池接口和主板边缘之间。通过该跳线口，可以连接一个常开（NO）瞬时按钮，实现外接电源键的功能。短按该按钮即可模拟板载电源键的操作。

   .. image:: img/pi5_j2.jpg

* 在 Pironman 5 中，**电源开关扩展器**通过两个弹簧触点（Pogo Pin）将 **J2** 跳线口延伸至外部电源按钮。

   .. image:: img/power_switch_convertor.png

* 现在，你可以通过外部电源按钮对 Raspberry Pi 5 进行开机和关机操作。

   .. image:: img/pironman_button.JPG

**电源循环控制**

首次为 Raspberry Pi 5 通电时，设备会自动开机并启动操作系统，无需按下电源按钮。

如果你运行的是 Raspberry Pi 桌面版系统，短按电源按钮将启动系统的关机流程。屏幕上会弹出菜单，提供关机、重启或注销选项。选择其中任意一项，或再次按下电源按钮，即可执行安全关机。

.. image:: img/button_shutdown.png

**关机操作**

    * 若你运行的是 **Raspberry Pi OS Desktop** 桌面系统，快速连续按两下电源按钮可实现关机；
    * 若你使用的是 **Raspberry Pi OS Lite** 精简系统（无桌面环境），只需按下一次电源按钮即可关机；
    * 若需强制关机，请长按电源按钮。


**开机操作**

    * 当 Raspberry Pi 处于关机但仍通电状态时，单击电源按钮即可开机。

.. note::

    如果你运行的系统不支持软关机功能，可长按 5 秒强制关机，随后再次单击按钮即可开机。

