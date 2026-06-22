.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _intro_pironman5_promax:

Pironman 5 Pro MAX
================================================================================

感谢选择 |link_pironman5_promax|。

.. image:: img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

使用 |link_pironman5_promax|，全面提升你的 Raspberry Pi 5 使用体验。这是我们全新的旗舰级高性能铝合金机箱，专为极致散热、强大扩展能力以及完整的桌面级体验而设计，非常适合 NAS、AI 开发、媒体中心以及各种高级项目。

**主要特点：**

* **双 NVMe 与 AI 扩展中心**\ ：内置 PCIe Gen 2 交换芯片，提供两个 M.2 M-key 插槽（2230/2242/2260/2280），可用于 SSD 或 AI 加速卡（完全兼容 Hailo-8 / Hailo-8L）。可配置为 RAID 0/1 NAS、SSD+AI 或双 AI 方案。

* **完整散热系统**\ ：配备大型塔式散热器和 PWM 风扇，同时拥有 **三个** 可编程 RGB PWM 风扇，即使在满负载情况下也能保持优秀的散热性能。

* **双显示与多媒体支持**\ ：

  * **4.3 英寸 DSI 触摸屏** （800×480）：可作为副屏信息显示、系统状态面板，甚至作为主桌面显示器使用。
  * **0.96 英寸智能 OLED 屏幕**\ ：实时显示 CPU、内存、温度、磁盘使用率和 IP 地址。
  * **立体声 3W 扬声器与 5MP 摄像头支持**\ ：适用于多媒体、视频会议或计算机视觉项目。

* **增强的用户交互与控制**\ ：

  * **可定制 RGB 灯效系统**\ ：6 个位于IO板上的 WS2812B 可编程 RGB LED 与 3 个同步 RGB 风扇，实现动态灯效。
  * **红外接收器**\ ：支持媒体中心遥控（如 Kodi、Volumio）。
  * **复古风格金属电源按钮**\ ：支持安全关机与开机。
  * **RTC 电池仓** （CR1220）用于系统时间保持。

* **专业级接口布局**\ ：

  * **后面板接口重排**\ ：电源输入与双 HDMI 标准接口重新布局，与 USB 接口对齐，带来整洁统一的线缆管理。
  * **完整接口支持**\ ：双 HDMI、千兆 LAN、2× USB 3.0、2× USB 2.0。
  * **外置 GPIO 扩展排针（带标签）**\ ，方便连接各类扩展设备。

* **高端工业设计**\ ：坚固的深色阳极氧化铝合金机身，搭配深色亚克力侧板、弹簧式 microSD 卡槽，以及现代桌面电脑风格外观设计。

.. note::

   强烈建议为 Pironman 5 Pro Max 使用 **官方 Raspberry Pi 27W 电源** 或兼容的高品质电源，例如 |link_sf_27w_supply|。  
   电源功率不足可能会在高负载情况下（尤其是使用 NVMe SSD 和外设时）导致 Raspberry Pi 5 出现不稳定或自动重启的情况。

-------------------------------------------------------------------------------------

**目录**

.. raw:: html

   <br/>

.. toctree::
    :maxdepth: 1

    About this Kit <self>
    what_do_we_need
    assembly_instructions
    install/install_the_os
    set_up/set_up_pironman5
    control/control_pironman5
    hardware/hardware
    optional_modules/optional_modules
    home_server/home_server
    ai_interaction/ai_interaction
    compitable_nvme_ssd
    faq

-------------------------------------------------------------------------------------

**规格参数**

* **尺寸**\ ：140.9 × 77.0 × 138.7 mm 
* **材质**\ ：

    * 主机外壳：深色阳极氧化铝合金
    * 侧面面板：深色亚克力

* **支持平台**\ ：仅支持 Raspberry Pi 5
* **电源输入**\ ：USB Type-C，5V/5A（建议至少 27W）
* **接口与端口**\ ：

    * **Raspberry Pi 40 针 GPIO** （外部引出，并带有清晰标识）
    * **MicroSD 卡槽** （带弹簧弹出机制）
    * **后面板**\ ：

        * USB Type-C 电源输入
        * 2 × USB 2.0
        * 2 × USB 3.0
        * 千兆以太网（RJ45）
        * 2 × 标准 HDMI（Type A）接口（支持 4Kp60）

* **散热系统**\ ：

    * 1 × 大型塔式散热器（带 PWM 控制风扇）
    * 3 × 可编程 RGB PWM 风扇（GPIO 控制，支持同步）

* **显示与多媒体**\ ：

    * 4.3 英寸 DSI 电容触摸屏（800 × 480 像素）
    * 0.96 英寸 OLED 显示屏（128×64，用于显示系统信息）
    * 立体声 3W 扬声器
    * 支持 500 万像素摄像头模块

* **存储与扩展**\ ：

    * 内置 PCIe Gen 2 交换芯片
    * 2 × PCIe 2.0 x1 M.2 M-Key 插槽
    * 支持 SSD / AI 加速卡尺寸：2230、2242、2260、2280

* **控制、灯效与功能**\ ：

    * 18 × WS2812B 可编程 RGB LED（6个在板子上，12个在RGB风扇上）
    * 红外接收器（38kHz）
    * 金属电源按键（支持安全关机）
    * 实时时钟（RTC）电池座（适用于 CR1220 电池）

* **做工与设计**\ ：采用精密 CNC 加工铝合金机身，搭配深色钢化亚克力面板，兼顾耐用性与高级质感。



