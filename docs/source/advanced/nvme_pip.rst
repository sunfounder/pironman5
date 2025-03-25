Pi5 NVMe PIP
=================

Pi5 NVMe PIP（PCIe外设板），根据Raspberry Pi基金会的定义，是一个专为NVMe固态硬盘设计的PCIe适配器板。它支持四种不同尺寸的NVMe SSD：2230、2242、2260和2280，所有这些都可以插入M.2 M键槽。

.. image:: img/nvme_pip.png

* 该板通过16P 0.5mm反向FFC（柔性扁平电缆）或定制阻抗匹配的FPC（柔性印刷电路）电缆连接。
* **STA**：状态LED指示灯。
* **PWR**：电源LED指示灯。
* 板载3.3V电源可以支持最高3A的输出。然而，由于Raspberry Pi的PCIe接口限制只能提供5V/1A输出（相当于5W），对于3.3V/3A的使用需求，可以通过J3连接器从5V电源提供额外的电力。
* **FORCE ENABLE**：板载电源通过来自PCIe接口的开关信号激活。Raspberry Pi开机后，会发送信号开启3.3V电源。如果某些系统不支持开关信号或由于其他原因，可以通过在两个浮动焊盘之间焊接一根线来短接J4 FORCE ENABLE，从而强制板载3.3V电源为NVMe供电。

关于型号
---------------------------

M.2 SSD因其紧凑的尺寸而闻名，具有多种类型，主要通过其键槽（连接器上的缺口设计）和使用的接口进行区分。以下是主要类型：

* **M.2 SATA SSD**：这些SSD使用SATA接口，类似于2.5英寸的SATA SSD，但采用更小的M.2外形。它们受限于SATA III的最大速度约为600 MB/s。这些SSD兼容M.2插槽，适用于B键和M键。
* **M.2 NVMe SSD**：这些SSD通过PCIe通道使用NVMe协议，比M.2 SATA SSD更快。它们适用于需要高速读写的应用，如游戏、视频编辑和数据密集型任务。这些SSD通常需要M键插槽。它们使用PCIe（外设组件互连快速接口）接口，具有3.0、4.0和5.0等不同版本。每个新版本的PCIe有效地将前一版本的数据传输速度加倍。然而，Raspberry Pi 5使用的是PCIe 3.0接口，能够提供最高3,500 MB/s的传输速度。

M.2 SSD有三种键类型：B键、M键和B+M键。然而，后来推出了B+M键，它结合了B键和M键的功能。因此，它取代了单独的B键。请参阅下面的图片。

.. image:: img/ssd_key.png


通常，M.2 SATA SSD是B+M键（可以适配B键和M键模块的插槽），而适用于PCIe 3.0 x4通道的M.2 NVMe SSD是M键。

.. image:: img/ssd_model2.png

关于长度
-----------------------

M.2模块有不同的尺寸，也可以用于Wi-Fi、WWAN、蓝牙、GPS和NFC。

Pironman 5支持四种（PCIe Gen 2.0 / PCIe Gen 3.0）NVMe M.2 SSD尺寸，分别为2230、2242、2260和2280。 "22"表示宽度，单位为毫米（mm），后面的两个数字表示长度。硬盘越长，可以安装的NAND闪存芯片越多，因此容量也越大。


.. image:: img/m2_ssd_size.png
  :width: 600

