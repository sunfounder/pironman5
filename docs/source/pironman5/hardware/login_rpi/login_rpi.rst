.. _login_rpi:

登录 Raspberry Pi OS
=====================================

本章将介绍如何登录 Raspberry Pi 系统。无论您是否连接了显示器，或是打算远程访问，本节都会指导您打开终端窗口，这将在后续章节中用于输入命令。

.. note::

    如果您已熟悉 Raspberry Pi 的基本操作，可以跳过本章。

使用屏幕登录
---------------------------

如果为 Raspberry Pi 连接了显示器，您将可以直接与系统交互，操作更加便捷。

**所需组件**

* Pironman 5
* 电源适配器
* 预装 Raspberry Pi OS 的 Micro SD 卡或 NVMe SSD
* 显示器电源适配器
* HDMI 线
* 显示器
* 鼠标
* 键盘

**操作步骤**

#. 将 Micro SD 卡插入 Pironman 5。

#. 将鼠标和键盘连接到 Pironman 5 的 USB 接口。

#. 使用 HDMI 线将显示器连接至 Pironman 5 的 HDMI 接口，并确保显示器已通电并打开。

#. 使用电源适配器启动 Pironman 5。不久后，您将在显示器上看到 Raspberry Pi OS 的桌面界面。

   .. image:: img/bookwarm.png
      :width: 90%


#. 进入桌面后，点击终端图标或在菜单中搜索终端以打开它，即可开始输入命令。

无屏远程登录
------------------------------------

如果您无法连接显示器，也可以通过远程方式登录 Raspberry Pi。

如需使用命令行，可通过 SSH 连接到 Raspberry Pi 的 Bash Shell，这是默认的 Linux 终端环境，可用于命令控制和设备管理。

如果您更偏好图形界面，可使用如 VNC Viewer 等远程桌面应用，在远程环境下进行文件管理和操作。

**所需组件**

* Pironman 5 
* 电源适配器
* 预装 Raspberry Pi OS 的 Micro SD 卡或 NVMe SSD

操作步骤：

#. 将 Micro SD 卡插入 Pironman 5。

#. 使用电源适配器为 Pironman 5 供电。

#. 针对不同操作系统设置远程访问的详细教程，请参考以下章节：

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


