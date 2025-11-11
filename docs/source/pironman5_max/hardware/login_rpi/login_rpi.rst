.. _max_login_rpi:

登录 Raspberry Pi OS
=====================================

本章将指导您如何登录树莓派系统。无论是通过连接显示器的方式，还是远程访问，都将为您介绍如何打开终端，以便在后续章节中输入命令。

.. note::

    如果您已经熟悉树莓派的基本操作，可以跳过本章。

通过连接屏幕登录
---------------------------

为树莓派连接屏幕可以方便您直接与系统进行交互。

**所需组件**

* Pironman 5 MAX
* 电源适配器
* 预装了 Raspberry Pi OS 的 Micro SD 卡或 NVMe SSD
* 显示器电源适配器
* HDMI 线缆
* 显示器
* 鼠标
* 键盘

**操作步骤**

#. 将 Micro SD 卡插入 Pironman 5 MAX。

#. 将鼠标和键盘连接至 Pironman 5 MAX 的 USB 接口。

#. 使用 HDMI 线将显示器连接至 Pironman 5 MAX 的 HDMI 接口。确保显示器已接通电源并开启。

#. 使用电源适配器为 Pironman 5 MAX 供电。稍后您将在显示器上看到 Raspberry Pi OS 的桌面界面。

   .. image:: img/bookwarm.png
      :width: 90%


#. 当桌面界面出现后，点击终端图标或在菜单中搜索“终端”打开它，开始输入命令。

无屏幕远程登录
---------------------------

如果您无法连接显示器，仍然可以通过远程方式使用树莓派。

若您偏好命令行方式，可以通过 SSH 登录到树莓派的 Bash Shell，这是 Linux 默认的命令行接口，允许您通过命令远程管理设备。

如果您更喜欢图形化界面，可以使用 VNC Viewer 等远程桌面工具，以可视化方式远程管理文件与操作。

**所需组件**

* Pironman 5 MAX 
* 电源适配器
* 预装了 Raspberry Pi OS 的 Micro SD 卡或 NVMe SSD

操作步骤：

#. 将 Micro SD 卡插入 Pironman 5 MAX。

#. 使用电源适配器为 Pironman 5 MAX 供电。

#. 根据您所使用电脑的操作系统，参阅以下章节获取远程访问设置的详细教程：

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


