.. _max_set_up_batocera:

在 Batocera.linux 系统中进行设置
=========================================================

如果您已经安装了 Batocera.linux 操作系统，可以通过 SSH 远程登录该系统，并按照以下步骤完成配置。

#. 系统启动后，通过 SSH 远程连接到 Pironman5。在 Windows 上可以打开 **Powershell**，在 macOS 或 Linux 上可以直接打开 **Terminal**。

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Batocera 系统的默认主机名为 ``batocera``，默认用户名为 ``root``，默认密码为 ``linux``。因此，您可以输入 ``ssh root@batocera.local`` 并输入密码 ``linux`` 来登录系统。

   .. image:: img/batocera_login.png
      :width: 90%

#. 执行以下命令以进入菜单设置界面： ``/etc/init.d/S92switch setup``。

   .. image:: img/batocera_configure.png  
      :width: 90%

#. 使用方向键向下移动到末尾，选择并启用 **Pironman5** 服务。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. 启用 pironman5 服务后，选择 **OK**。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. 执行命令 ``reboot`` 重启 Pironman5。

   .. code-block:: shell

      reboot

#. 重启后， ``pironman5.service`` 将自动启动。Pironman 5 MAX 的主要功能配置如下：

   * OLED 屏幕将显示 CPU、内存、磁盘使用率、CPU 温度和树莓派的 IP 地址；
   * 四颗 WS2812 RGB 灯将以蓝色呼吸模式点亮。
   
   .. note::

     默认情况下，RGB 风扇在温度达到 60°C 前不会启动。如需设置不同的启动温度，请参见 :ref:`max_cc_control_fan`。

现在，您可以将 Pironman 5 MAX 连接显示器、游戏手柄、耳机等设备，畅享沉浸式游戏体验。


.. note::

   此时，你已经成功完成了 Pironman 5 MAX 的所有组件设置。  
   Pironman 5 MAX 的配置已完成。  
   现在你可以使用 Pironman 5 MAX 来控制你的 Raspberry Pi 和其他设备。  
   有关 Pironman 5 MAX 网页的更多信息和使用方法，请参考: :ref:`max_view_control_dashboard`。
