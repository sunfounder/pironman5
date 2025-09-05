.. _max_set_up_pi_os:

在 Raspberry Pi/Ubuntu/Kali/Homebridge 系统中配置
=====================================================

如果你在树莓派上安装了 Raspberry Pi OS、Ubuntu、Kali Linux 或 Homebridge 系统，则需要通过命令行来配置 Pironman 5 MAX。请参考以下详细教程：

.. note::

  在开始配置前，请确保你已经启动并登录至树莓派系统。如果你不确定如何登录，可以访问树莓派官网：|link_rpi_get_start|。


配置关机后关闭 GPIO 电源
------------------------------------------------------------
为了避免关机后 OLED 屏幕和 RGB 风扇（通过 GPIO 供电）继续运行，需要配置树莓派在关机时自动关闭 GPIO 电源。

#. 使用以下命令手动编辑 ``EEPROM`` 配置文件：

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. 将配置文件中的 ``POWER_OFF_ON_HALT`` 选项设置为 ``1``，例如：

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. 按 ``Ctrl + X``，然后 ``Y`` 和 ``Enter`` 保存更改。


下载并安装 ``pironman5`` 模块
-----------------------------------------------------------

#. 对于 Lite 系统，需先安装 ``git``、 ``python3``、 ``pip3``、 ``setuptools`` 等依赖工具。

   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. 接着，从 GitHub 下载并安装 ``pironman5`` 模块。

   .. code-block:: shell

      cd ~
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   安装完成后，系统会提示重启，请根据提示完成重启。

   重启后， ``pironman5.service`` 服务将自动启动。以下是 Pironman 5 MAX 的主要功能：

   * OLED 屏幕将显示 CPU、内存、磁盘使用率、CPU 温度及树莓派的 IP 地址。
   
   .. note:: OLED 屏幕可能会在一段时间不操作后自动关闭以节省电源。您可以轻轻敲击机箱，触发振动传感器来唤醒屏幕。

   
   * 四颗 WS2812 RGB 灯珠将以蓝色呼吸灯形式亮起。
     
   .. note::

     RGB 风扇默认在温度达到 60°C 时才会启动。如需自定义启动温度，请参考 :ref:`max_cc_control_fan`。

#. 你可以使用 ``systemctl`` 工具对 ``pironman5.service`` 进行 ``start``、 ``stop``、 ``restart`` 或查询 ``status`` 状态：

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service

   * ``restart``：用于使 pironman5 的配置更改生效。
   * ``start/stop``：启动或停止 ``pironman5.service`` 服务。
   * ``status``：使用 ``systemctl`` 工具查看 pironman5 服务的运行状态。


.. note::

   此时，你已经成功完成了 Pironman 5 MAX 的所有组件设置。  
   Pironman 5 MAX 的配置已完成。  
   现在你可以使用 Pironman 5 MAX 来控制你的 Raspberry Pi 和其他设备。  
   有关 Pironman 5 MAX 网页的更多信息和使用方法，请参考: :ref:`max_view_control_dashboard`。
