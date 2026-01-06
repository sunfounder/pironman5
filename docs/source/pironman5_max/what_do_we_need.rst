1. 还需要准备什么？
===================================

在组装和使用 Pironman 5 MAX 之前，请确保你已准备好以下组件。其中一部分是基本运行所必需的，其他则为可选组件，取决于你计划如何使用 Raspberry Pi。

必需组件
------------------------------

* **Raspberry Pi 5**

  Pironman 5 MAX 与 Raspberry Pi 5 完全兼容。

  .. image:: img/need_pi5.jpg
     :width: 500

* **27W 电源适配器**

  建议为 Pironman 5 系列产品使用官方 27W 电源适配器或 |link_sf_27w_supply|，以避免供电不足导致 Raspberry Pi 5 重启。

  .. image:: img/need_power.png
     :width: 600

* **Micro SD 卡**

  Raspberry Pi 本身没有内置硬盘，系统启动和所有文件都存储在 **Micro SD 卡** 中。  
  
  .. image:: img/need_sd.jpg
    :width: 200

  * 最小容量：**16GB**  
  * 推荐容量：**32GB** （稳定性更好）  
  * 品牌建议：选择 **SanDisk** 或 **Samsung** 等可靠品牌，以避免读写错误  

可选组件
------------------------

* **M.2 NVMe SSD**

  Pironman 5 MAX 配备了一个 NVMe PIP，提供两个 M.2 SSD 接口，支持四种 NVMe M.2 SSD 规格：2230、2242、2260 和 2280。接口工作在 PCIe Gen2.0 速度（不支持 Gen3）。

  .. image:: img/need_nvme.png
    :width: 500

* **显示器（HDMI 显示器或电视）** 

  对于初学者，我们强烈建议准备一台带 HDMI 输入的显示设备，以便更方便地配置 Raspberry Pi OS 并运行图形界面程序。  

  .. image:: img/need_screen.png
    :width: 400
    
* **HDMI 线缆**

  Raspberry Pi 5 的 HDMI 接口通过 USB HDMI 转接器转换为标准 HDMI Type-A 接口。因此，需要一根标准的 HDMI 对 HDMI 线缆，将 Pironman 5 MAX 连接到显示器。

  .. image:: img/need_hdmi.png
    :width: 400
    
* **键盘和鼠标**

  在 Raspberry Pi OS 的初始设置阶段非常有用。后续你可以切换到远程访问（SSH/VNC），但对于初学者，仍然建议准备一套基本的 USB 或无线键盘鼠标。  

  .. image:: img/need_keyboard_mouse.png
    :width: 500
 

**准备小提示**

* 如果你购买的是整套套件，大多数配件都已包含，但仍需要单独准备 Raspberry Pi 主板、Micro SD 卡和电源适配器。  
* 不确定该买什么？最稳定、最通用的组合是：**Raspberry Pi 5（2GB）+ 官方电源适配器 + 32GB Micro SD 卡**。  
