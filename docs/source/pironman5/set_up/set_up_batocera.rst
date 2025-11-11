.. _set_up_batocera:

在 Batocera.linux 上进行设置
=========================================================

如果您已经安装了 Batocera.linux 操作系统，可以通过 SSH 远程登录该系统，并按照以下步骤完成配置。

#. 系统启动后，使用 ssh 远程连接到 Pironman5。Windows 用户可打开 **Powershell**，Mac OS X 和 Linux 用户可直接打开 **Terminal**。

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Batocera 系统的默认主机名为 ``batocera``，默认用户名为 ``root``，密码为 ``linux``。因此，您可以通过输入 ``ssh root@batocera.local`` 并输入密码 ``linux`` 进行登录。

   .. image:: img/batocera_login.png
      :width: 90%

#. 执行命令：``/etc/init.d/S92switch setup`` 以进入菜单设置页面。

   .. image:: img/batocera_configure.png  
      :width: 90%

#. 使用方向键下移至底部，选择并启用 **Pironman5** 服务。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. 启用 pironman5 服务后，选择 **OK**。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. 执行命令 ``reboot``，重启 Pironman5。

   .. code-block:: shell

      reboot

#. 重启后， ``pironman5.service`` 会自动启动。以下是 Pironman 5 的主要配置功能：

   * OLED 屏幕将显示 CPU、内存、磁盘使用率、CPU 温度及树莓派的 IP 地址；
   * 四颗 WS2812 RGB 灯将以蓝色呼吸模式点亮。
   * RGB 风扇默认设置为 **Always On（始终开启）** 模式。如需自定义启用温度，请参阅 :ref:`cc_control_fan`。

现在，您可以将 Pironman 5 连接到显示器、游戏手柄、耳机等设备，尽情享受沉浸式的游戏体验。


.. note::

   此时，您已成功完成 Pironman 5 的安装，可以开始使用了。
   
   如需对其组件进行高级控制，请参考 :ref:`control_commands_dashboard_5`。
