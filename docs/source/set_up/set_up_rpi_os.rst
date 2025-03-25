在 Raspberry Pi/Ubuntu/Kali/Homebridge OS 上设置
===================================================

如果你已在 Raspberry Pi 上安装了 Raspberry Pi OS、Ubuntu、Kali Linux 或 Homebridge，你需要使用命令行来配置 Pironman 5。详细教程请参见下文：

.. note::

  在配置之前，你需要启动并登录到你的 Raspberry Pi。如果你不确定如何登录，可以访问 Raspberry Pi 官方网站： |link_rpi_get_start|。


配置关机以禁用 GPIO 电源
------------------------------------------------------------
为了防止由 Raspberry Pi GPIO 提供电源的 OLED 屏幕和 RGB 风扇在关机后仍然保持开启，必须配置 Raspberry Pi 以禁用 GPIO 电源。

#. 使用以下命令手动编辑 ``EEPROM`` 配置文件：

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. 修改文件中的 ``POWER_OFF_ON_HALT`` 设置为 ``1`` 。例如：

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. 按 ``Ctrl + X`` ，然后按 ``Y`` 和 ``Enter`` 保存更改。


下载并安装 ``pironman5`` 模块
-----------------------------------------------------------

#. 对于轻量系统，首先安装如 ``git`` 、 ``python3`` 、 ``pip3`` 、 ``setuptools`` 等工具。
  
   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. 然后从 GitHub 下载代码并安装 ``pironman5`` 模块。

   .. code-block:: shell

      cd ~
      git clone https://github.com/sunfounder/pironman5.git
      cd ~/pironman5
      sudo python3 install.py

   安装成功后，需要重启系统以激活安装。请按照屏幕上的重启提示操作。

   重启后， ``pironman5.service`` 会自动启动。以下是 Pironman 5 的主要配置：

   * OLED 屏幕显示 CPU、RAM、磁盘使用情况、CPU 温度以及 Raspberry Pi 的 IP 地址。
   * 四个 WS2812 RGB LED 灯将以呼吸模式亮起，颜色为蓝色。
     
   .. note:: 
   
     RGB 风扇只有在温度达到 60°C 时才会开始转动。如需调整激活温度，请参见 :ref:`cc_control_fan`。

#. 你可以使用 ``systemctl`` 工具来 ``start`` 、 ``stop`` 、 ``restart`` 或查看 ``pironman5.service`` 的 ``status`` 。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart`` ：使用此命令应用对 pironman5 设置所做的任何更改。
   * ``start/stop`` ：启用或禁用 ``pironman5.service`` 。
   * ``status`` ：使用 ``systemctl`` 工具检查 ``pironman5`` 程序的运行状态。
