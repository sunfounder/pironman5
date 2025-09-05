.. _set_up_pironman5_mini:

在 Raspberry Pi OS / Ubuntu / Kali Linux / Homebridge 中进行设置
======================================================================

如果你在树莓派上安装了 Raspberry Pi OS、Ubuntu、Kali Linux 或 Homebridge 系统，则需要通过命令行对 Pironman 5 Mini 进行配置。请参考以下详细教程：

.. note::

  在开始配置前，请先启动并登录你的树莓派。如果你不清楚如何登录，可以访问树莓派官网：|link_rpi_get_start|。


关闭时自动关闭 GPIO 电源的配置
------------------------------------------------------------

为了防止由 GPIO 供电的 RGB 风扇在树莓派关机后仍然运行，你需要配置树莓派，在关机时关闭 GPIO 电源。

#. 通过以下命令手动编辑 ``EEPROM`` 配置文件：

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. 将文件中的 ``POWER_OFF_ON_HALT`` 设置改为 ``1``。示例如下：

   .. code-block:: shell

     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. 按 ``Ctrl + X``，再按 ``Y``，然后按 ``Enter`` 保存修改。


下载并安装 ``pironman5`` 模块
-----------------------------------------------------------

#. 对于 Lite 系统，首先需安装一些必要工具，如 ``git``、 ``python3``、 ``pip3``、 ``setuptools`` 等：

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. 接下来从 GitHub 下载代码并安装 ``pironman5`` 模块：

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py


   安装成功后，根据提示重启系统以使安装生效。

   重启后， ``pironman5.service`` 将自动启动。以下是 Pironman 5 的默认配置效果：


   * 四颗 WS2812 RGB LED 将以蓝色呼吸灯模式亮起。
   
   .. note::

     RGB 风扇默认在温度达到 60°C 时才会启动。如需调整温度阈值，请参见 :ref:`cc_control_fan_mini`。

#. 你可以使用 ``systemctl`` 工具来 ``start``、 ``stop``、 ``restart`` 或查看 ``pironman5.service`` 的 ``status`` 状态：

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``：当你更改了 Pironman 5 Mini 的配置后，使用此命令以应用更改。
   * ``start/stop``：手动启用或停止 ``pironman5.service`` 服务。
   * ``status``：使用 ``systemctl`` 查看 ``pironman5`` 程序当前的运行状态。


.. note::

   此时，你已经成功完成了 Pironman 5 Mini 的所有组件设置。  
   Pironman 5 Mini 的配置已完成。  
   现在你可以使用 Pironman 5 Mini 来控制你的 Raspberry Pi 和其他设备。  
   有关 Pironman 5 Mini 网页的更多信息和使用方法，请参考: :ref:`view_control_dashboard_mini`。
