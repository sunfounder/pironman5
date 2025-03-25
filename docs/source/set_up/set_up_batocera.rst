.. _set_up_batocera: 

在 Batocera.linux 上设置
=========================================================

如果你已经安装了 Batocera.linux 操作系统，可以通过 SSH 远程登录该系统，然后按照以下步骤完成配置。

#. 系统启动后，使用 ssh 远程连接到 Pironman5。对于 Windows 用户，可以打开 **Powershell**，对于 Mac OS X 和 Linux 用户，则可以直接打开 **Terminal**。

   .. image:: img/batocera_powershell.png
      :width: 90%
      

#. Batocera 系统的默认主机名是 ``batocera`` ，默认用户名为 ``root`` ，密码为 ``linux`` 。因此，你可以通过输入 ``ssh root@batocera.local`` 来登录，并输入密码 ``linux`` 。

   .. image:: img/batocera_login.png
      :width: 90%

#. 执行命令: ``/etc/init.d/S92switch setup`` 进入菜单设置页面。

   .. image:: img/batocera_configure.png  
      :width: 90%

#. 使用下箭头键导航到页面底部，选择并启用 **Pironman5** 服务。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. 启用 pironman5 服务后，选择 **OK**。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. 执行命令 ``reboot`` 来重启 Pironman5。

   .. code-block:: shell

      reboot

#. 重启后， ``pironman5.service`` 会自动启动。以下是 Pironman 5 的主要配置：

   * OLED 屏幕显示 CPU、RAM、磁盘使用情况、CPU 温度和 Raspberry Pi 的 IP 地址。
   * 四个 WS2812 RGB LED 灯会以蓝色呼吸模式亮起。

   .. note:: 
   
     RGB 风扇只有在温度达到 60°C 时才会开始转动。如需调整激活温度，请参见 :ref:`cc_control_fan`。

现在，你可以将 Pironman 5 连接到显示器、游戏控制器、耳机等，沉浸在你的游戏世界中。
