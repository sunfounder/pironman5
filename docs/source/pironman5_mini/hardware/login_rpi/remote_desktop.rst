.. _remote_desktop_mini:

通过远程桌面访问 Raspberry Pi
==================================================

如果您更喜欢图形用户界面（GUI）而非命令行操作，Raspberry Pi 支持远程桌面功能。本指南将引导您通过 VNC（虚拟网络计算）配置并使用远程桌面访问功能。

我们推荐使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 来进行远程连接。

**启用 Raspberry Pi 的 VNC 服务**

Raspberry Pi OS 默认已预装 VNC 服务，但默认未启用。请按照以下步骤启用：

#. 在 Raspberry Pi 的终端中输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用方向键导航至 **Interfacing Options**，然后按 **Enter**。

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. 从选项中选择 **VNC**。

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. 使用方向键依次选择 **<Yes>** -> **<OK>** -> **<Finish>**，完成 VNC 服务启用。

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**使用 VNC Viewer 登录**

#. 在您的电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。

#. 安装完成后，启动 VNC Viewer，输入 Raspberry Pi 的主机名或 IP 地址，并按回车键。

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. 出现提示时，输入您的 Raspberry Pi 用户名和密码，然后点击 **OK**。

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. 您现在可以访问 Raspberry Pi 的图形化桌面界面了。

   .. image:: img/bookwarm.png
      :width: 90%

