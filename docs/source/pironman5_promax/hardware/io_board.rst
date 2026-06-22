.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


IO 扩展板
================

.. image:: img/io_board.png


RGB 灯
------------

.. image:: img/io_board_rgb.png

该板配备了 18 个 WS2812 RGB LED （6个在电路板上，12个RGB风扇上），支持自定义控制。用户可以开启或关闭灯光、更改颜色、调整亮度、切换显示模式以及设置变化速度。


RGB 控制引脚
-------------------------

RGB LED 通过 SPI 驱动，并连接到 **GPIO10** （即 SPI 的 MOSI 引脚）。图中显示的两个引脚用于将 RGB 连接到 GPIO10。如果不需要使用 RGB，可以移除跳帽。

  .. image:: img/io_board_rgb_pin.png


RGB OUT 引脚
-------------------------

.. image:: img/io_board_rgb_out.png

WS2812 RGB LED 支持串联连接，因此可以连接外部 RGB LED 灯带。将 **SIG** 引脚连接到外部灯带的 **DIN** 引脚即可扩展。

默认配置包含 18 个 RGB LED。如果连接了额外的 LED，需要使用以下命令更新数量：

.. code-block:: shell

  sudo pironman5 --rgb-led-count [quantity]

示例：

.. code-block:: shell

  sudo pironman5 --rgb-led-count 24



OLED 屏幕接口
----------------------------

OLED 屏幕接口地址为 0x3C，是该扩展板的重要功能之一。

.. image:: img/io_board_oled.png

如果 OLED 屏幕没有显示或显示异常，可以按照以下步骤进行排查：

检查 OLED 屏幕的 FPC 排线是否正确连接。

#. 使用以下命令查看程序运行日志，并检查是否有错误信息。

    .. code-block:: shell

        cat /var/log/pironman5/pironman5.log

#. 也可以使用以下命令检查 OLED 的 i2c 地址 0x3C 是否被识别：
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. 如果前两个步骤未发现问题，可以尝试重启 pironman5 服务，看是否可以解决问题。

    .. code-block:: shell

        sudo systemctl restart pironman5.service



红外接收器
---------------------------

.. image:: img/io_board_receiver.png

* **型号**\ ：IRM-56384，工作频率为 38KHz。
* **连接方式**\ ：红外接收器连接到 **GPIO13**\ 。
* **D7**\ ：红外接收指示灯，当检测到信号时会闪烁。
* **J6**\ ：用于启用红外功能的跳线。默认已安装跳帽，可直接使用。如果不需要使用红外接收器，可移除跳帽以释放 GPIO13 引脚。

使用红外接收器前，请确认连接正常并安装所需模块：

* 测试连接：

  .. code-block:: shell

    sudo ls /dev |grep lirc

* 安装 ``lirc`` 模块：

  .. code-block:: shell

    sudo apt-get install lirc -y

* 运行以下命令测试红外接收器：

  .. code-block:: shell

    mode2 -d /dev/lirc0

* 运行命令后，按下遥控器上的任意按键，对应的按键编码将被打印出来。


RGB 风扇接口
---------------

.. image:: img/io_board_pin_fan.png

IO 扩展板支持最多三个 5V PWM 风扇，所有风扇统一控制。

风扇控制信号首先连接到 IO 扩展板上的 **FAN IN** 接口，然后分配到三个专用风扇接口。这三个接口从上到下分别为 **REAR UPPER**\ 、\ **REAR LOWER** 和 **CPU FAN**\ 。请按照丝印标识连接，否则可能会影响风扇的 RGB 控制。


GPIO 扩展排针
---------------

.. image:: img/io_board_pin_header.png

两个直角排针将 Raspberry Pi 的 GPIO 引脚引出。但需要注意，红外接收器、RGB LED 和风扇占用了部分引脚。如需将这些引脚用于其他功能，需要移除对应的跳帽。

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 MAX
    - Raspberry Pi 5
  * - IR Receiver(Optional)
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - FAN(Optional)
    - GPIO6
  * - FLED(Optional)
    - GPIO5  
  * - RGB(Optional)
    - GPIO10