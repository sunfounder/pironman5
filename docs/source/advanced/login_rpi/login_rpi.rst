登录Raspberry Pi OS
=====================================

本章将向你介绍如何登录Raspberry Pi。无论是通过连接显示器进行本地操作，还是需要远程访问，本节将指导你如何打开终端，之后你将使用终端输入命令。

.. note::

    如果你已经熟悉Raspberry Pi的操作，可以跳过本章。

通过屏幕登录
---------------------------

连接显示器的Raspberry Pi便于直接与系统交互。

**所需组件**

* Pironman 5
* 电源适配器
* 已预装Raspberry Pi OS的Micro SD卡或NVMe SSD
* 显示器电源适配器
* HDMI线
* 显示器
* 鼠标
* 键盘

**步骤**

#. 将Micro SD卡插入Pironman 5。

#. 将鼠标和键盘连接到Pironman 5的USB端口。

#. 使用HDMI线将显示器连接到Pironman 5的HDMI端口。确保显示器连接到电源并已打开。

#. 使用电源适配器启动Pironman 5。几秒钟后，你应该能在显示器上看到Raspberry Pi OS的桌面界面。

   .. image:: img/bookwarm.png
      :width: 90%


#. 当桌面界面显示后，点击终端图标或在菜单中搜索终端，开始输入命令。

没有显示器的远程登录
------------------------------------

如果你没有显示器，也可以通过远程登录使用Raspberry Pi。

对于命令行访问，你可以通过SSH连接到Raspberry Pi的Bash shell，这是默认的Linux shell，允许你通过命令管理设备。

如果你更喜欢图形界面，可以使用像VNC Viewer这样的远程桌面应用，以可视化的方式远程管理文件和操作。

**所需组件**

* Pironman 5
* 电源适配器
* 已预装Raspberry Pi OS的Micro SD卡或NVMe SSD

**步骤：**

#. 将Micro SD卡插入Pironman 5。

#. 使用电源适配器将Pironman 5连接到电源。

#. 根据你的计算机操作系统，参考以下章节了解如何设置远程访问：

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


