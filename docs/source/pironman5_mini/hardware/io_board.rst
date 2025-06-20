Pironman 5 Mini HAT
===========================================


.. image:: img/pironman5mini_hat.png

RGB 灯效
------------

.. image:: img/io_board_rgb.png

该主板配备了 4 颗 WS2812 RGB LED，支持多种自定义控制。用户可开启或关闭灯效、更改颜色、调节亮度、切换显示模式，以及设置变换速度。

* 控制 RGB 灯的开关状态，设置为 ``true`` 开启， ``false`` 关闭：

.. code-block:: shell

  pironman5 -re true

* 更改颜色，输入十六进制颜色值，例如 ``fe1a1a``：

.. code-block:: shell

  pironman5 -rc fe1a1a

* 设置亮度（范围：0 ~ 100%）：

.. code-block:: shell

  pironman5 -rb 100

* 切换显示模式，可选项包括： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``：

.. note::

  如果设置为 ``rainbow``、 ``rainbow_reverse`` 或 ``hue_cycle`` 模式，则无法再使用 ``pironman5 -rc`` 命令设置颜色。

.. code-block:: shell

  pironman5 -rs breathing

* 设置灯效变化速度（范围：0 ~ 100%）：

.. code-block:: shell

  pironman5 -rp 80

RGB 控制引脚
-------------------------

RGB 灯通过 SPI 驱动，连接至 **GPIO10**，该引脚也是 SPI 的 MOSI 引脚。RGB 与 GPIO10 的连接通过两根引脚实现，如无需此功能，可移除跳线帽。


 .. image:: img/io_board_rgb_pin.png

RGB OUT 扩展引脚
-------------------------

 .. image:: img/io_board_rgb_out.png

WS2812 RGB 支持串联扩展，可外接 RGB 灯带。请将 **SIG** 引脚连接至外部灯带的 **DIN** 引脚。

默认配置包含 4 颗 RGB 灯，如需扩展，可使用以下命令更新数量：

.. code-block:: shell

  pironman5 -rl 12



RGB 风扇引脚
---------------

IO 扩展板支持 5V 非 PWM 风扇。

请将风扇电源线连接至 FAN 接口。

 .. image:: img/io_board_fan.png

J9 下方的两组针脚分别控制风扇与风扇灯光的启用。默认跳线帽已插入，允许使用 GPIO6 和 GPIO5 控制风扇和其 RGB 灯的开关。若无需此功能，可移除跳线以释放对应 GPIO 引脚。

 .. image:: img/io_board_fan_j9.png

可通过命令配置 RGB 风扇的运行模式，不同模式决定风扇启动所需的温度条件：

  例如，设置为 **1: Performance** 模式时，风扇将在温度达到 50°C 时启动：

  .. code-block:: shell

    pironman5 -gm 3

  * **4: Quiet**：70°C 启动风扇
  * **3: Balanced**：67.5°C 启动风扇
  * **2: Cool**：60°C 启动风扇
  * **1: Performance**：50°C 启动风扇
  * **0: Always On**：风扇始终运行

若将风扇控制引脚连接至 Raspberry Pi 的其他 GPIO 引脚，可使用以下命令修改引脚编号：

.. code-block:: shell

  sudo pironman5 -gp 18


电源按钮连接器
--------------------------------------

**添加电源按钮**

* Raspberry Pi 5 上的 **J2** 跳线位于 RTC 电池接口与板边之间。通过该跳线，可外接一个常开（NO）瞬时按钮，实现与主板电源键相同的功能。

  .. image:: img/pi5_j2.jpg

* Pironman 5 Mini 通过两个弹片针将 **J2** 跳线延伸至外部电源按钮接口。

  .. image:: img/power_switch_j2.jpeg

  .. image:: img/power_switch_j2_2.jpeg

* 现在，您可以通过电源按钮控制 Raspberry Pi 5 的开关机。

  .. image:: img/pironman_button.JPG

**电源控制行为**

首次通电时，Raspberry Pi 5 将自动启动系统，无需按下电源键。

如果运行的是 Raspberry Pi 桌面系统，短按电源按钮将触发关机菜单，提供关机、重启、注销等选项。再次按下按钮或点击选项，即可执行干净关机。

.. image:: img/button_shutdown.png

**关机说明**

* 若运行的是 **Bookworm Desktop** 桌面系统，可快速双击电源键进行关机。
* 若运行的是不带桌面的 **Bookworm Lite** 系统，单击一次即可关机。
* 若需强制关机，请长按电源键。

**开机说明**

* 当 Raspberry Pi 已关机但仍通电时，单击电源键可重新开机。

.. note::

    如果当前系统不支持关机按钮，可长按 5 秒强制关机，之后单击按钮实现开机。




NVMe 模块
-------------------------------------------


Pironman 5 Mini 集成了用于 NVMe SSD 的 PCIe 适配模块，支持 2230、2242、2260 和 2280 四种规格的 NVMe M.2 SSD，接口为 M key。

.. image:: img/nvme_p.png


* **STA**：状态指示灯  
* **PWR**：电源指示灯

  .. image:: img/nvme_led.png

* 模块通过 16Pin 0.5mm 反向 FFC（柔性扁平线）或定制阻抗匹配的 FPC（柔性电路板）进行连接。

  .. image:: img/nvme_pcie.png

* **FORCE ENABLE**：模块上电依赖于来自 PCIe 接口的开关信号。若某些系统不支持该信号，可通过将 J2 的两个焊盘短接，使 NVMe 强制上电。

  .. image:: img/nvme_j2.png

**关于型号**

M.2 SSD 根据接口与金手指凹槽的不同，主要分为以下几种：

* **M.2 SATA SSD**：使用 SATA 接口，传输速率约 600 MB/s，兼容 B key 与 M key 插槽。
* **M.2 NVMe SSD**：使用 NVMe 协议，基于 PCIe 通道，读写速度显著优于 SATA SSD，适合游戏、视频编辑、大数据处理等场景。一般需插入 M-key 插槽，常见版本有 PCIe 3.0、4.0、5.0，传输速率逐代翻倍。Raspberry Pi 5 支持 PCIe 3.0，最高传输速度可达 3500 MB/s。

M.2 SSD 的接口类型包括 B key、M key 和 B+M key。目前大多数 SATA 型 SSD 为 B+M key，NVMe 型 SSD 多为 M key。请参考下图：

.. image:: img/ssd_key.png


一般而言，M.2 SATA 为 B+M-key，M.2 NVMe（PCIe 3.0 x4）为 M-key。

.. image:: img/ssd_model2.png

**关于长度**

M.2 模块支持不同长度的规格，也常用于 Wi-Fi、WWAN、蓝牙、GPS 和 NFC 等用途。

Pironman 5 支持 4 种 NVMe M.2 SSD 尺寸（PCIe Gen 2.0 / Gen 3.0）：2230、2242、2260、2280。其中“22”表示宽度（单位 mm），后两位为长度。长度越大，可安装更多 NAND 闪存芯片，容量也越大。


.. image:: img/m2_ssd_size.png
  :width: 600


1220RTC 电池座
---------------------------------

.. image:: img/battery_holder.png


设备内置 1220 型 RTC 电池座，便于安装实时时钟电池。通过 SH1.0 2P 反向连接线与 Raspberry Pi 的 RTC 接口连接。

该电池座兼容 CR1220 和 ML1220 电池。如果使用可充电的 ML1220（锂二氧化锰电池），可在 Raspberry Pi 上配置涓流充电。请注意，CR1220 不可充电。

**启用涓流充电功能**

.. warning::

  若使用的是 CR1220 电池，请勿启用涓流充电，否则可能造成电池或主板永久损坏。

系统默认关闭涓流充电功能。通过 ``sysfs`` 可查看当前涓流充电电压与限制：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

启用涓流充电步骤如下，在 ``/boot/firmware/config.txt`` 文件中添加配置：

  * 打开配置文件：

    .. code-block:: shell

      sudo nano /boot/firmware/config.txt

  * 添加以下内容：

    .. code-block:: shell

      dtparam=rtc_bbat_vchg=3000000

重启后，可看到系统显示如下：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

说明当前电池已开启涓流充电。如需关闭，只需删除 ``config.txt`` 中对应的 ``dtparam`` 行。



引脚排针
--------------

.. image:: img/io_board_pin_header.png

主板设有两个直角引脚排针，用于扩展 Raspberry Pi 的 GPIO 功能。但请注意，红外接收器、RGB 灯和风扇已占用部分 GPIO 引脚。如需使用对应引脚，请先移除跳线帽释放资源。

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 Mini
    - Raspberry Pi 5
  * - FAN（可选）
    - GPIO6
  * - FAN RGB（可选）
    - GPIO5
  * - RGB（可选）
    - GPIO10