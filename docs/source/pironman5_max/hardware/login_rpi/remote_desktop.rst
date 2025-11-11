.. _max_remote_desktop:

树莓派远程桌面访问
==================================================

如果您更倾向于使用图形用户界面（GUI）而非命令行操作，树莓派同样支持远程桌面功能。本指南将带您完成使用 VNC（Virtual Network Computing）进行远程访问的设置与操作。

我们推荐使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 来实现远程桌面访问。

**启用树莓派的 VNC 服务**

在 Raspberry Pi OS 中，VNC 服务默认已预安装，但未启用。请按以下步骤进行启用：

#. 在树莓派终端中输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用方向键导航至 **Interfacing Options**，然后按 **Enter** 键。

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. 从选项中选择 **VNC**。

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. 使用方向键依次选择 **<Yes>** -> **<OK>** -> **<Finish>**，以完成 VNC 服务的启用。

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%

**通过 VNC Viewer 登录树莓派**

#. 在您的个人电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。


#. 安装完成后，启动 VNC Viewer。输入您树莓派的主机名或 IP 地址，然后按 Enter 键。

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. 在弹出的登录窗口中输入树莓派的用户名与密码，然后点击 **OK**。

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. 您现在就可以访问树莓派的桌面界面了。

   .. image:: img/bookwarm.png
      :width: 90%

