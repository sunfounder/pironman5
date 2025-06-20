.. _remote_desktop:

Raspberry Pi 远程桌面访问
==================================================

如果您更倾向于图形用户界面（GUI）而非命令行操作，Raspberry Pi 同样支持远程桌面功能。本指南将引导您通过 VNC（虚拟网络计算）方式实现远程访问。

我们推荐使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 作为远程访问工具。

**启用 Raspberry Pi 上的 VNC 服务**

Raspberry Pi OS 系统已预装 VNC 服务，但默认处于禁用状态。请按照以下步骤启用：

#. 在 Raspberry Pi 的终端中输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. 使用方向键选择 **Interfacing Options（接口选项）** ，然后按 **Enter** 键。

   .. image:: img/bookwarm_config_interface.png
      :width: 90%


#. 在列表中选择 **VNC**。

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. 使用方向键依次选择 **<Yes>** -> **<OK>** -> **<Finish>**，完成 VNC 服务的启用。

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%


**使用 VNC Viewer 登录**

#. 在您的个人电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 。

#. 安装完成后，启动 VNC Viewer。在输入框中填入 Raspberry Pi 的主机名或 IP 地址，按下 Enter 键。

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. 出现提示后，输入 Raspberry Pi 的用户名和密码，然后点击 **OK**。

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. 此时，您将成功访问 Raspberry Pi 的图形桌面界面。

   .. image:: img/bookwarm.png
      :width: 90%

