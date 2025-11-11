
.. _set_up_umbrel_mini:

在 Umbrel OS 上的配置
======================================================================

如果你在 Raspberry Pi 5 上安装了 Umbrel OS，则需要使用命令行来配置 Pironman 5 Mini。以下是详细步骤说明：

#. 使用以太网线将 Raspberry Pi 5 连接到网络。此步骤非常重要，以确保设备能够访问互联网。

#. 在浏览器中访问：``http://umbrel.local``。  
   如果页面无法打开，请在路由器中查找 Umbrel 设备的 IP 地址，例如：``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. 创建你的 Umbrel 账户，设置用户名和密码。  
   该密码将用于今后远程登录 Umbrel，请务必记住。

   .. image:: img/umbrel_account.png

#. 点击 **Next** 以完成 Umbrel 配置并进入桌面环境。

   .. image:: img/umbrel_desktop.png

#. 打开终端。  
   在桌面中，点击 **Settings** 图标，然后选择 **Advanced Settings** 并点击 **Open**。

   .. image:: img/umbrel_setting.png

#. 点击 **Open Terminal**。

   .. image:: img/umbrel_open_terminal.png

#. 你可以选择在 Umbrel OS 内或在特定应用中打开终端。无论哪种方式，都会进入命令行界面。

   .. image:: img/umbrel_terminal.png

#. 从 GitHub 下载代码并安装 ``pironman5`` 模块。

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. 安装完成后，输入以下命令以重启 Raspberry Pi：

   .. code-block:: shell

      sudo reboot

#. 重启后，``pironman5.service`` 服务会自动启动。  
   以下是 Pironman 5 Mini 的主要配置：

   * 四个 WS2812 RGB 灯会以蓝色呼吸效果亮起。  
   * RGB 风扇默认设置为 **Always On（始终开启）** 模式。若需调整温度触发设置，请参阅 :ref:`cc_control_fan_mini`。

#. 你可以使用 ``systemctl`` 工具来 ``start``、 ``stop``、 ``restart`` 或检查 ``pironman5.service`` 服务的 ``status``。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``：使用此命令以应用 Pironman 5 Mini 设置的更改。  
   * ``start/stop``：启用或禁用 ``pironman5.service`` 服务。  
   * ``status``：使用 ``systemctl`` 工具检查 ``pironman5`` 程序的运行状态。

.. note::

   至此，你已成功配置 Pironman 5 Mini 并可以开始使用。  
   若需对其组件进行高级控制，请参阅 :ref:`control_commands_dashboard_mini`。
