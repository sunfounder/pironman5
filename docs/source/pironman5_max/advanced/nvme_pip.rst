双 NVMe PIP
=====================

**Dual NVMe PIP** （PCIe 外设扩展板）是由树莓派基金会定义的专用 PCIe 转接板，主要用于 NVMe 固态硬盘。

树莓派 5 的 PCIe 接口原生只提供一条 **Gen2 x1** 通道（500 MB/s）。  
通过集成 **ASM1182e** PCIe 交换芯片，Dual NVMe PIP 可以扩展为 **两条独立的 Gen2 x1 通道**，从而支持连接：

* **两块 M.2 NVMe SSD**，或  
* **一块 M.2 NVMe SSD + 一块 M.2 Hailo-8/8L AI 加速器**

**注意事项**：

* 不支持 Gen3  
* 支持的 NVMe SSD 尺寸： **2230** 、 **2242** 、 **2260** 、 **2280** （均为 M.2 M-key 插槽）

.. image:: img/nvme_pip.png

* 该扩展板通过一条 16P 0.5mm 反向 FFC（柔性扁平线缆）或定制的阻抗匹配 FPC（柔性印刷电路线缆）连接。  
* **STA**：状态指示灯  
* **PWR**：电源指示灯  
* 板载 3.3V 电源可提供最高 3A 电流输出。但由于树莓派 PCIe 接口仅能提供 5V/1A（即 5W），若需要 3.3V/3A 的供电能力，可通过 J3 接口从 5V 电源额外供电。  
* **FORCE ENABLE**：板载电源由 PCIe 接口的开关信号激活。树莓派上电后，会发送信号开启 3.3V 电源。如果某些系统不支持该开关信号，或因其他原因无法触发，你可以通过在 J4 FORCE ENABLE 上焊接一根导线短接两焊盘，从而强制开启板载 3.3V 电源为 NVMe 供电。

关于型号
---------------------------

M.2 SSD 以其小巧的体积广受欢迎，主要根据其键位（接口缺口形状）和所使用的接口协议区分。以下是主要类型：

* **M.2 SATA SSD**：使用 SATA 接口，与传统 2.5 英寸 SATA SSD 相同，但采用更小巧的 M.2 封装，传输速率受限于 SATA III（最高约 600 MB/s）。通常采用 B key 或 B+M key 接口。
* **M.2 NVMe SSD**：使用 PCIe 通道的 NVMe 协议，传输速度远超 SATA 型 SSD，适用于游戏、视频编辑及其他高负载数据处理应用。此类 SSD 通常使用 M key 接口，基于 PCIe（外围组件互连快速通道）协议，常见版本有 3.0、4.0 和 5.0，每一代几乎将带宽翻倍。树莓派 5 支持 PCIe 3.0，理论最高传输速率可达 3500 MB/s。

M.2 SSD 分为三种键位类型：B key、M key 和 B+M key。其中，B+M key 综合了 B 和 M 两种接口的特性，最终逐步替代了单一的 B key，请参考下图：

.. image:: img/ssd_key.png


一般来说，M.2 SATA SSD 多为 B+M key（兼容 B key 和 M key 插槽），而支持 PCIe 3.0 x4 通道的 M.2 NVMe SSD 通常采用 M key。

.. image:: img/ssd_model2.png

关于长度
-----------------------

M.2 模块不仅用于存储设备，也可用于 Wi-Fi、WWAN、蓝牙、GPS 和 NFC 等设备，因此具有多种尺寸。

Pironman 5 MAX 支持四种 NVMe M.2 SSD（PCIe Gen 2.0 / Gen 3.0）长度规格：2230、2242、2260 和 2280。其中“22”表示宽度（单位为毫米），后两位数字表示长度。长度越大，可安装的 NAND 闪存芯片越多，容量也越大。


.. image:: img/m2_ssd_size.png
  :width: 600

