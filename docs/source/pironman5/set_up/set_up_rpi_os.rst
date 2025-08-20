在 Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge 上进行设置
==================================================================

如果您在树莓派上安装了 Raspberry Pi OS、Ubuntu、Kali Linux 或 Homebridge 系统，需要通过命令行对 Pironman 5 进行配置。请参考以下详细教程：

.. note::

  在进行配置之前，请先启动并登录树莓派系统。如果您不清楚如何登录，请访问树莓派官方网站：|link_rpi_get_start|。


配置关机后自动关闭 GPIO 电源
------------------------------------------------------------
为防止 OLED 屏幕和 RGB 风扇在树莓派关机后依然通过 GPIO 供电持续运行，您需要设置 GPIO 在关机时自动断电。

#. 使用以下命令手动编辑 ``EEPROM`` 配置文件：

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. 将配置文件中的 ``POWER_OFF_ON_HALT`` 设置修改为 ``1``，例如：

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. 按下 ``Ctrl + X``，然后按 ``Y``，再回车保存退出。


下载并安装 ``pironman5`` 模块
-----------------------------------------------------------

#. 对于 Lite 系统，首先安装必要工具，如 ``git``、 ``python3``、 ``pip3``、 ``setuptools`` 等：

   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. 接着从 GitHub 下载代码并安装 ``pironman5`` 模块：

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   安装成功后，系统会提示您重启设备以完成安装。根据提示重启系统。

   重启后， ``pironman5.service`` 将自动启动。Pironman 5 的主要功能包括：

   * OLED 屏幕显示 CPU、内存、磁盘使用情况、CPU 温度以及树莓派的 IP 地址；
   * 四颗 WS2812 RGB 灯将以蓝色呼吸灯模式点亮；
     
   .. note::

     RGB 风扇在温度未达到 60°C 前不会启动。如需自定义启动温度，请参阅 :ref:`cc_control_fan`。

#. 您可以使用 ``systemctl`` 工具对 ``pironman5.service`` 进行 ``start``、 ``stop``、 ``restart`` 或 ``status`` 操作：

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service

   * ``restart``：用于应用对 pironman 5 设置所做的修改；
   * ``start/stop``：启用或关闭 ``pironman5.service``；
   * ``status``：通过 ``systemctl`` 查看 pironman5 程序当前运行状态。
