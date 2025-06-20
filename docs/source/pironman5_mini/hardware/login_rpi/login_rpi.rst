.. _login_rpi_mini:

登录 Raspberry Pi OS
=====================================

在本章节中，您将学习如何登录到 Raspberry Pi。无论是连接显示器直接操作，还是通过远程方式访问，本节将指导您打开终端，后续章节中您将通过终端输入相关命令。

.. note::

    如果您已经熟悉 Raspberry Pi 的操作，可以跳过本章节。

通过连接显示器登录
---------------------------

为 Raspberry Pi 连接显示器可以直接在系统中进行交互操作。

**所需组件**

* Pironman 5 Mini
* 电源适配器
* 预装 Raspberry Pi OS 的 Micro SD 卡或 NVMe SSD
* 显示器电源适配器
* HDMI 线缆
* 显示器
* 鼠标
* 键盘

**操作步骤**

#. 将 Micro SD 卡插入 Pironman 5 Mini。

#. 将鼠标和键盘连接到 Pironman 5 Mini 的 USB 接口。

#. 使用 HDMI 线将显示器连接至 Pironman 5 Mini 的 HDMI 接口。确保显示器已接通电源并打开。

#. 通过电源适配器为 Pironman 5 Mini 通电，稍后您将看到 Raspberry Pi OS 的桌面出现在显示器上。

   .. image:: img/bookwarm.png
      :width: 90%
      
#. 当桌面出现后，点击终端图标或在菜单中搜索“终端”以打开命令行界面，开始输入命令。


无显示器远程登录
----------------------------------------------

如果没有可用的显示器，您仍可通过远程方式登录并使用 Raspberry Pi。

若您习惯命令行操作，可以使用 SSH 远程连接至 Raspberry Pi 的 Bash Shell，这是默认的 Linux 命令行环境，可通过命令管理设备。

如果您更倾向图形化界面，可使用如 VNC Viewer 等远程桌面应用程序，以图形方式远程操作文件和管理系统。

**所需组件**

* Pironman 5 Mini 
* 电源适配器
* 预装 Raspberry Pi OS 的 Micro SD 卡或 NVMe SSD

操作步骤：

#. 将 Micro SD 卡插入 Pironman 5 Mini。

#. 使用电源适配器为 Pironman 5 Mini 通电。

#. 针对不同操作系统的远程访问配置，请参阅以下小节教程：

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


