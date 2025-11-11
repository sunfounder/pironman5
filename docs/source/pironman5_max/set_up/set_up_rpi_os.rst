.. _max_set_up_pi_os:

在 Raspberry Pi / Ubuntu / Kali / Homebridge OS 上的配置
===================================================================

如果你在 Raspberry Pi 上安装了 Raspberry Pi OS、Ubuntu、Kali Linux 或 Homebridge，则需要使用命令行来配置 Pironman 5 MAX。以下是详细教程。

.. note::

  在进行配置之前，请先启动并登录到你的 Raspberry Pi。  
  如果不确定如何登录，可以访问 Raspberry Pi 官方网站：|link_rpi_get_start|。


配置关机时关闭 GPIO 电源
-------------------------------------------------------------------------------

为防止 Raspberry Pi 关机后由 GPIO 供电的 OLED 屏幕和 RGB 风扇仍保持运行，必须配置 Raspberry Pi 以在关机时关闭 GPIO 电源。

#. 打开 EEPROM 配置工具：

   .. code-block::

      sudo raspi-config

#. 进入 **Advanced Options → A12 Shutdown Behaviour**。

   .. image:: img/shutdown_behaviour.png

#. 选择 **B1 Full Power Off**。

   .. image:: img/run_power_off.png

#. 保存更改。系统会提示你重启以使新设置生效。

下载并安装 ``pironman5`` 模块
-----------------------------------------------------------

.. note::

   对于 “lite” 系统，请先安装以下工具：``git``、 ``python3``、 ``pip3``、 ``setuptools`` 等。
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. 从 GitHub 下载代码并安装 ``pironman5`` 模块。

   .. code-block:: shell

      cd ~
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   安装成功后，需要重启系统以激活安装。请根据屏幕提示重启。

   重启后，``pironman5.service`` 服务会自动启动。  
   以下是 Pironman 5 MAX 的主要功能配置：
   
   * OLED 屏幕显示 CPU、RAM、磁盘使用率、CPU 温度及 Raspberry Pi 的 IP 地址。  

   .. note:: OLED 屏幕在一段时间无操作后会自动关闭以节省电能。  
      你可以轻触机壳，触发震动传感器以重新点亮屏幕。

   * 四个 WS2812 RGB 灯会以蓝色呼吸灯效果亮起。  
   * RGB 风扇默认设置为 **Always On（始终开启）** 模式。若需设置不同的启用温度，请参阅 :ref:`cc_control_fan_max`。

#. 你可以使用 ``systemctl`` 工具来 ``start``、 ``stop``、 ``restart`` 或检查 ``pironman5.service`` 服务的 ``status``。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``：使用此命令以应用 Pironman 5 MAX 设置的更改。  
   * ``start/stop``：启用或禁用 ``pironman5.service`` 服务。  
   * ``status``：使用 ``systemctl`` 工具检查 ``pironman5`` 程序的运行状态。

.. note::

   至此，你已成功配置 Pironman 5 MAX 并可以开始使用。  
   若需对其组件进行高级控制，请参阅 :ref:`control_commands_dashboard_max`。
