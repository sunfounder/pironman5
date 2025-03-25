IO扩展板
=================

RGB LED
------------

.. image:: img/io_board_rgb.png

该板配备4个WS2812 RGB LED，提供可自定义的控制功能。用户可以开启或关闭它们，改变颜色，调节亮度，切换显示模式，并设置变化速度。

* 要修改RGB LED的开关状态，使用 ``true`` 开启RGB LED， ``false`` 关闭它们。

.. code-block:: shell

  pironman5 -re true

* 要更改颜色，输入所需的十六进制颜色值，例如 ``fe1a1a`` 。

.. code-block:: shell

  pironman5 -rc fe1a1a

* 要调整RGB LED的亮度（范围：0 ~ 100%）：

.. code-block:: shell

  pironman5 -rb 100

* 要切换RGB LED的显示模式，选择以下选项： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` ：

.. note::

  如果你将RGB LED显示模式设置为 ``rainbow`` 、 ``rainbow_reverse`` 或 ``hue_cycle`` ，你将无法使用 ``pironman5 -rc`` 设置颜色。

.. code-block:: shell

  pironman5 -rs breathing

* 要修改变化的速度（范围：0 ~ 100%）：

.. code-block:: shell

  pironman5 -rp 80

RGB控制引脚
-------------------------

RGB LED由SPI驱动并连接到 **GPIO10** ，该引脚也是SPI的MOSI引脚。J9上方的两个引脚用于将RGB LED连接到GPIO10。如果不需要，可以移除跳线。

  .. image:: img/io_board_rgb_pin.png

RGB输出引脚
-------------------------

.. image:: img/io_board_rgb_out.png

WS2812 RGB LED支持串联连接，允许外接RGB LED条。将 **SIG** 引脚连接到外接条的 **DIN** 引脚以进行扩展。

默认配置包含4个RGB LED。若要连接更多的LED并更新数量，可以使用以下命令：

.. code-block:: shell

  pironman5 -rl 12


OLED屏幕连接器
----------------------------

OLED屏幕连接器的地址为0x3C，这是其一个重要特性。

.. image:: img/io_board_oled.png

如果OLED屏幕没有显示或显示不正确，你可以按照以下步骤排查问题：

检查OLED屏幕的FPC电缆是否正确连接。

#. 使用以下命令查看程序的运行日志，并检查是否有错误信息。

    .. code-block:: shell

        cat /opt/pironman5/log

#. 或者，使用以下命令检查OLED的i2c地址0x3C是否被识别：

    .. code-block:: shell
        
        sudo i2cdetect -y 1


#. 如果前两步没有发现问题，可以尝试重新启动pironman5服务，看是否能解决问题。

    .. code-block:: shell

        sudo systemctl restart pironman5.service


红外接收器
---------------------------

.. image:: img/io_board_receiver.png

* **Model/型号**：IRM-56384，工作频率为38KHz。
* **Connection/连接**：红外接收器连接到 **GPIO13** 。
* **D1**：红外接收指示灯，接收到信号时闪烁。
* **J8**：启用红外功能的引脚。默认情况下，插入了一个跳线帽以立即启用功能。如果不使用红外接收器，可以移除跳线帽以释放GPIO13。

要使用红外接收器，验证其连接并安装必要的模块：

* 测试连接：

  .. code-block:: shell

    sudo ls /dev |grep lirc

* 安装 ``lirc`` 模块：

  .. code-block:: shell

    sudo apt-get install lirc -y

* 现在，通过运行以下命令测试红外接收器。

  .. code-block:: shell

    mode2 -d /dev/lirc0

* 运行命令后，按下遥控器上的按钮，按钮的代码将被打印出来。


RGB风扇引脚
----------------

IO扩展板最多支持两个5V非PWM风扇。两个风扇一起控制。

**FAN1** 和 **FAN2** 是两个风扇引脚。你需要将风扇的红线连接到“+”端，黑线连接到“-”端。

.. image:: img/io_board_fan.png

J9下方的两个引脚是RGB风扇的启用引脚。默认情况下，跳线已插入这些引脚，允许使用GPIO6控制风扇的开关状态。如果不需要风扇工作，可以移除跳线以释放GPIO6。

.. image:: img/io_board_fan_j9.png

**D2** 是风扇信号指示灯，当风扇启动时会亮起。

.. image:: img/io_board_fan_d2.png

你可以使用命令来配置两个RGB风扇的工作模式。这些模式决定了RGB风扇启动的条件。

例如，如果设置为 **1: Performance/高性能** 模式，RGB风扇将在50°C时启动。

.. code-block:: shell

  pironman5 -gm 3

* **4: uiet/静音**：RGB风扇将在70°C时启动。
* **3: Balanced/平衡**：RGB风扇将在67.5°C时启动。
* **2: Cool/冷却**：RGB风扇将在60°C时启动。
* **1: Performance/高性能**：RGB风扇将在50°C时启动。
* **0: Always On/始终开启**：RGB风扇始终开启。

如果你将RGB风扇的控制引脚连接到Raspberry Pi的不同引脚，可以使用以下命令更改引脚编号。

.. code-block:: shell

  sudo pironman5 -gp 18

引脚头
--------------

.. image:: img/io_board_pin_header.png

两个直角插针连接器扩展了Raspberry Pi的GPIO，但需要注意，红外接收器、RGB LED和风扇占用了部分引脚。移除相应的跳线帽即可将这些引脚用于其他功能。

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5
    - Raspberry Pi 5
  * - 红外接收器（可选）
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - 风扇（可选）
    - GPIO6
  * - RGB（可选）
    - GPIO10
  * - RGB（可选）
    - GPIO12
  * - RGB（可选）
    - GPIO21
