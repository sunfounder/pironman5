.. _set_up_pironman5:

4. 设置或安装软件
================================================

现在，系统已经写入 Micro SD 卡或 NVMe SSD 中，你可以将其插入 Pironman 5 插槽。然后按下电源按钮打开设备。

开机后，你会看到各种电源指示灯亮起，但 OLED 屏幕、RGB LED 和 RGB 风扇（侧面两个风扇）还未启动，因为它们需要配置。如果出现屏幕乱码问题，请暂时忽略；配置完成后会解决。

在配置之前，你需要启动并登录到你的 Raspberry Pi。如果你不确定如何登录，可以访问 Raspberry Pi 官方网站： |link_rpi_get_start|。

然后，你可以根据你的系统选择相应的配置教程。


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_batocera


**关于电源按钮**

电源按钮启用了 Raspberry Pi 5 的电源按钮功能，操作方式与 Raspberry Pi 5 的电源按钮相同。

* **关机**

    * 如果你运行的是 Raspberry Pi **Bookworm Desktop** 系统，可以快速连续按下电源按钮两次进行关机。
    * 如果你运行的是 Raspberry Pi **Bookworm Lite** 系统，按一次电源按钮即可启动关机。
    * 若要强制关机，按住电源按钮不放。

* **开机**

    * 如果 Raspberry Pi 主板已经关机，但仍有电源供应，单次按压即可从关机状态开机。

* 如果你运行的系统不支持关机按钮，可以按住电源按钮 5 秒钟来强制关机，单次按压即可从关机状态开机。
