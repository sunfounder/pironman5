.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_set_up_batocera:

在 Batocera.linux 上设置
=========================================================

如果你已经安装了 Batocera.linux 操作系统，可以通过 SSH 远程登录系统，然后按照以下步骤完成配置。

#. 系统启动后，通过 SSH 远程连接到 Pironman5。  
   在 Windows 上可以打开 **Powershell**\ ，在 Mac OS X 和 Linux 上可以直接打开 **Terminal**\ 。

   .. image:: img/batocera_powershell.png
      :width: 90%

#. Batocera 系统默认主机名为 ``batocera``\ ，默认用户名为 ``root``\ ，密码为 ``linux``\ 。  
   因此可以输入 ``ssh root@batocera.local`` 并输入密码 ``linux`` 进行登录。

   .. image:: img/batocera_login.png
      :width: 90%

#. 执行命令 ``/etc/init.d/S92switch setup`` 进入菜单设置界面。

   .. image:: img/batocera_configure.png
      :width: 90%

#. 使用键盘 **下方向键** 移动到菜单底部，选择并启用 **Pironman5** 服务。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. 启用 pironman5 服务后，选择 **OK**\ 。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. 执行 ``reboot`` 命令重启 Pironman5。

   .. code-block:: shell

      reboot

#. 重启后，\ ``pironman5.service`` 会自动启动。  
   Pironman 5 Pro MAX 的主要默认配置如下：

   * OLED 屏幕会显示 CPU、RAM、磁盘使用率、CPU 温度以及 Raspberry Pi 的 IP 地址。
   * 四个 WS2812 RGB LED 会以蓝色呼吸模式亮起。

现在，你可以将 Pironman 5 Pro MAX 连接到显示器、游戏手柄、耳机等设备，沉浸在你的游戏世界中。


.. note::

   至此，你已经成功完成 Pironman 5 Pro MAX 的基础设置，并可以开始使用。

   如果需要对设备组件进行更高级的控制，请参考 :ref:`control_commands_dashboard_promax`。

