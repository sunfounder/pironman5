.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


1. 还需要准备什么？
===================================

在组装和使用 Pironman 5 Pro MAX 之前，请确保你已经准备好以下组件。其中一些是基本运行所必需的，另一些则是根据你的使用需求选择的可选组件。

必需组件
------------------------------

* **Raspberry Pi 5**

  Pironman 5 Pro MAX 完全兼容 Raspberry Pi 5。

  .. image:: img/need_pi5.jpg
     :width: 500

* **27W 电源适配器**

  建议使用官方 **27W 电源适配器** 或 |link_sf_27w_supply| 为 Pironman 5 系列供电，以避免电源功率不足导致 Raspberry Pi 5 重启或运行不稳定。

  .. image:: img/need_power.png
     :width: 600

* **Micro SD 卡**

  Raspberry Pi 本身没有内置硬盘，系统启动和所有文件都存储在 **Micro SD 卡** 中。

  .. image:: img/need_sd.jpg
    :width: 200

  * 最低容量：\ **16GB**
  * 推荐容量：\ **32GB** （更稳定）
  * 品牌建议：使用 **SanDisk** 或 **Samsung** 等可靠品牌，以避免读写错误


可选组件
------------------------

* **M.2 NVMe SSD**

  Pironman 5 Pro MAX 配备 NVMe PIP 模块，提供两个 M.2 SSD 接口，支持以下 NVMe SSD 规格：2230、2242、2260 和 2280。  
  接口工作在 **PCIe Gen2.0** 速度（不支持 Gen3）。

  .. image:: img/need_nvme.png
    :width: 500

* **显示器（HDMI 或电视）**

  对于初学者，强烈建议准备一台带 **HDMI 输入** 的显示器，这样可以更方便地安装和配置 Raspberry Pi OS 以及运行图形界面程序。

  .. image:: img/need_screen.png
    :width: 400

* **HDMI 线**

  Raspberry Pi 5 的 HDMI 接口通过 USB HDMI 转接板转换为 **标准 HDMI Type-A 接口**\ ，因此需要使用 **标准 HDMI-HDMI 线** 连接 Pironman 5 Pro MAX 与显示器。

  .. image:: img/need_hdmi.png
    :width: 400

* **键盘与鼠标**

  在 Raspberry Pi OS 的初始设置阶段非常有用。  
  之后你可以使用 **SSH 或 VNC 远程连接**\ ，但对于初学者来说，建议准备一套基础的 USB 或无线键鼠。

  .. image:: img/need_keyboard_mouse.png
    :width: 500


**准备建议**

* 如果你购买的是套件，大部分配件已经包含，但仍需要单独准备 **Raspberry Pi 主板、Micro SD 卡以及电源适配器**\ 。
* 如果不确定如何选择，最稳定、通用的配置是：

::

   Raspberry Pi 5 (2GB) + 官方电源适配器 + 32GB Micro SD 卡