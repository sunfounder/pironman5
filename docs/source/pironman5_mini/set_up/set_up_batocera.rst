.. _set_up_batocera_mini:

在 Batocera.linux 上进行设置
=========================================================

如果你已经安装了 Batocera.linux 系统，可以通过 SSH 远程登录该系统，并按照以下步骤完成配置。

#. 系统启动后，通过 SSH 远程连接到 Pironman5。Windows 用户可以打开 **Powershell**，Mac OS X 和 Linux 用户可直接打开 **Terminal**。

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Batocera 系统的默认主机名为 ``batocera``，默认用户名为 ``root``，密码为 ``linux``。因此，可以通过输入 ``ssh root@batocera.local`` 并输入密码 ``linux`` 登录系统。

   .. image:: img/batocera_login.png
      :width: 90%

#. 执行命令：``/etc/init.d/S92switch setup``，进入菜单设置界面。

   .. image:: img/batocera_configure.png  
      :width: 90%

#. 使用方向键向下滚动至底部，选择并启用 **Pironman5** 服务。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. 启用 pironman5 服务后，选择 **OK**。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. 执行命令 ``reboot`` 以重启 Pironman5。

   .. code-block:: shell

      reboot

#. 重启后， ``pironman5.service`` 将会自动启动。以下是 Pironman 5 的主要配置：

   * 四颗 WS2812 RGB 灯珠将以蓝色呼吸灯模式点亮。

   .. note::

     RGB 风扇在温度达到 60°C 前不会启动。若需设置其他温度触发值，请参考 :ref:`cc_control_fan_mini`。

现在，你可以将 Pironman 5 连接到显示器、游戏手柄、耳机等设备，尽情畅玩属于你的游戏世界。
