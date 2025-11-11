电源开关转换器
==============================

该模块用于将 Raspberry Pi 5 的电源开关功能扩展至机箱外部，方便用户操作。

.. image:: img/power_switch_conventor.jpeg

**添加电源按钮**

* Raspberry Pi 5 板载了一个 **J2** 跳线接口，位于 RTC 电池座与主板边缘之间。通过在该接口连接一个常开（NO）瞬时按键，可自定义外接电源按钮。短按该按钮可实现与主板电源按钮相同的功能。

   .. image:: img/pi5_j2.jpg

* 在 Pironman 5 中，配备了一个 **电源开关转换器**，通过两个 Pogo 弹簧针将 **J2** 引脚扩展至外部电源按钮。

   .. image:: img/power_switch_convertor.png

* 现在，您可以通过电源按钮控制 Raspberry Pi 5 的开关机。

   .. image:: img/pironman_button.JPG

**电源循环**

首次为 Raspberry Pi 5 接通电源时，设备将自动启动并进入操作系统，无需按下电源按钮。

如果运行的是 Raspberry Pi Desktop 桌面系统，短按电源按钮将触发系统弹出关机菜单，提供关机、重启或注销选项。选择任意选项，或再次按下电源按钮，即可执行系统安全关机。

.. image:: img/button_shutdown.png

**关机操作**

    * 若使用的是 **Raspberry Pi OS Desktop** 桌面系统，快速连续按下电源按钮两次可执行关机操作。
    * 若使用的是无桌面环境的 **Raspberry Pi OS Lite** 系统，单击一次电源按钮即可关机。
    * 如需强制关机，长按电源按钮即可。


**开机操作**

    * 若 Raspberry Pi 处于关机但仍通电状态，单击电源按钮即可开机。

.. note::

    如果您的系统不支持关机按钮功能，可长按电源按钮 5 秒以强制关机，再通过单击按钮实现开机。

