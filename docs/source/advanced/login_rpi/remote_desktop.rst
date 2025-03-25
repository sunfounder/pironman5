远程桌面访问Raspberry Pi
==================================================

对于喜欢图形用户界面（GUI）而非命令行访问的用户，Raspberry Pi支持远程桌面功能。本指南将引导您通过VNC（虚拟网络计算）设置和使用远程访问。

我们推荐使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 来实现这一功能。

**在Raspberry Pi上启用VNC服务**

VNC服务在Raspberry Pi OS中已预安装，但默认情况下是禁用的。请按照以下步骤启用它：

#. 在Raspberry Pi终端中输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用下箭头键导航至 **Interfacing Options** ，然后按 **Enter** 。

   .. image:: img/bookwarm_config_interface.png
      :width: 90%


#. 从选项中选择 **VNC** 。

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. 使用箭头键选择 **<Yes>** -> **<OK>** -> **<Finish>** ，完成VNC服务的激活。

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%


**通过VNC Viewer登录**

#. 在您的个人电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。

#. 安装完成后，启动VNC Viewer。输入您的Raspberry Pi的主机名或IP地址，然后按Enter。

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. 系统提示时，输入您的Raspberry Pi用户名和密码，然后点击 **OK** 。

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. 现在，您将可以访问Raspberry Pi的桌面界面。

   .. image:: img/bookwarm.png
      :width: 90%
      
