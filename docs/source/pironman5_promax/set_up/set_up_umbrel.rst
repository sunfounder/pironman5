.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_umbrel_promax:

在 Umbrel OS 上设置
======================================================================

如果你在 Raspberry Pi 5 上安装了 Umbrel OS，需要通过命令行来配置 Pironman 5 Pro MAX。具体步骤如下：

#. 使用网线将 Raspberry Pi 5 连接到网络。  
   这一步非常重要，以确保设备可以访问互联网。

#. 在浏览器中访问： ``http://umbrel.local``  
   如果无法打开，请在路由器中查找 Umbrel 设备的 IP 地址，例如： ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. 创建 Umbrel 账户（设置用户名和密码）。  
   该密码用于后续远程访问，请务必妥善保存。

   .. image:: img/umbrel_account.png

#. 点击 **Next** 完成 Umbrel 初始化，并进入桌面界面。

   .. image:: img/umbrel_desktop.png

#. 打开终端：在桌面点击 **Settings（设置）** → **Advanced Settings（高级设置）** → **Open（打开）**\ 。

   .. image:: img/umbrel_setting.png

#. 点击 **Open Terminal（打开终端）**\ 。

   .. image:: img/umbrel_open_terminal.png

#. 你可以选择在 Umbrel OS 或某个应用中打开终端，两者都会进入终端界面。

   .. image:: img/umbrel_terminal.png

#. 下载 GitHub 代码并安装 ``pironman5`` 模块：

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. 安装完成后，执行以下命令重启 Raspberry Pi：

   .. code-block:: shell

      sudo reboot

#. 重启后，\ ``pironman5.service`` 会自动启动，默认配置如下：

   * OLED 屏幕显示 CPU、内存、磁盘使用率、CPU 温度以及 IP 地址  
   * 4 个 WS2812 RGB LED 以蓝色呼吸模式亮起  

#. 你可以使用 ``systemctl`` 管理 ``pironman5.service``\ ：

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``\ ：应用配置更改  
   * ``start/stop``\ ：启动或停止服务  
   * ``status``\ ：查看服务运行状态  

.. note::

   至此，你已经成功完成 Pironman 5 Pro MAX 的设置，可以开始使用。

   如需更高级的控制功能，请参考 :ref:`control_commands_dashboard_promax`。