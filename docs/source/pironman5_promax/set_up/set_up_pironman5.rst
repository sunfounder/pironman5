.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_set_up_pironman5:

4. 设置或安装软件
================================================

当系统已经写入 **Micro SD 卡** 或 **NVMe SSD** 后，你可以将其插入 Pironman 5 Pro MAX 的对应插槽，然后按下电源按钮启动设备。

开机后，你会看到各种电源指示灯亮起，但 **OLED 屏幕、RGB LED 和 RGB 风扇（机箱侧面的两个风扇）暂时不会工作**\ ，因为它们还需要进行软件配置。  
如果此时屏幕出现显示错乱，请暂时忽略，完成配置后即可恢复正常。

在开始配置之前，你需要先启动并登录 Raspberry Pi。  
如果不确定如何登录，可以访问 Raspberry Pi 官方网站：|link_rpi_get_start|。

完成登录后，可以根据你所使用的系统选择相应的配置教程。

.. toctree::
   :maxdepth: 1

   set_up_rpi_os
   set_up_umbrel

.. set_up_batocera

.. set_up_home_assistant


**关于电源按钮**

该电源按钮实际上是 Raspberry Pi 5 的电源按钮引出，因此其行为与 Raspberry Pi 5 的电源按钮完全一致。

* **关机**

  * 如果运行 **Raspberry Pi OS Desktop** 系统，可以 **快速按两次电源按钮** 来关机。
  * 如果运行 **Raspberry Pi OS Lite** 系统，\ **按一次电源按钮** 即可开始关机。
  * 若需要 **强制关机**\ ，可以 **长按电源按钮**\ 。

* **开机**

  * 如果 Raspberry Pi 已关机但仍然接通电源， **单击电源按钮** 即可重新启动。

* 如果运行的系统 **不支持关机按钮功能**\ ，可以 **长按 5 秒强制关机**\ ，然后 **单击按钮重新开机**\ 。