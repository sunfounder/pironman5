.. _view_control_commands:

通过命令行进行控制
========================================

除了通过控制面板查看 Pironman 5 的运行数据和控制各类设备，您还可以使用命令行实现同样的控制功能。

.. note::

  * 在 **Home Assistant** 系统中，仅可通过网页 ``http://<ip>:34001`` 使用控制面板进行监控与管理。

.. * 在 **Batocera.linux** 系统中，仅支持使用命令行对 Pironman 5 进行监控与控制。请注意，修改配置后需执行 ``pironman5 restart`` 以使更改生效。

查看基本配置
-----------------------------------

``pironman5`` 模块提供了 Pironman 的基础配置，您可以通过以下命令查看当前配置项。

.. code-block:: shell

  pironman5 -c

标准配置如下所示：

.. code-block::

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

您可以根据需求自定义这些配置。

使用 ``pironman5`` 或 ``pironman5 -h`` 查看命令使用说明。

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]
                          [{start,stop}]

  Pironman5

  位置参数:
    {start,stop}          控制命令

  可选参数:
    -h, --help            显示帮助信息并退出
    -c, --config          显示当前配置
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          以十六进制设置 RGB 颜色，可带或不带 '#'（如 #FF0000 或 00aabb）
    -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                          设置 RGB 亮度，范围为 0–100
    -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{...}]
                          设置 RGB 显示样式
    -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                          设置 RGB 动效速度，范围 0–100
    -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                          启用或关闭 RGB，True/False
    -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                          设置 RGB LED 的数量（整数）
    -u [{C,F}], --temperature-unit [{C,F}]
                          设置温度单位
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          设置风扇模式，0: 始终开启，1: 高性能，2: 清凉，3: 平衡，4: 静音
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          设置风扇 GPIO 引脚号

.. note::

  每当修改 ``pironman5.service`` 状态后，需使用以下命令重启服务，使配置生效。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* 可使用 ``systemctl`` 工具查看 ``pironman5`` 程序状态：

  .. code-block:: shell

    sudo systemctl status pironman5.service

* 或通过日志文件检查程序运行状态：

  .. code-block:: shell

    cat /opt/pironman5/log


控制 RGB 灯效
----------------------
主板配备了 4 颗 WS2812 RGB LED，支持个性化控制。用户可开启/关闭灯效，变更颜色，调整亮度，设置显示模式以及动效速度。

.. note::

  每当您修改 ``pironman5.service`` 的状态后，都需要执行以下命令，使配置更改生效。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 开关 RGB 灯：使用 ``true`` 开启， ``false`` 关闭：

.. code-block:: shell

  pironman5 -re true

* 更改颜色：输入十六进制颜色值，例如 ``fe1a1a``：

.. code-block:: shell

  pironman5 -rc fe1a1a

* 设置亮度（范围：0–100%）：

.. code-block:: shell

  pironman5 -rb 100

* 更换 RGB 显示模式，可选项包括： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``

.. note::

  若设置为 ``rainbow``、 ``rainbow_reverse`` 或 ``hue_cycle`` 模式，将无法再使用 ``pironman5 -rc`` 指定颜色。

.. code-block:: shell

  pironman5 -rs breathing

* 设置动画速度（范围：0–100%）：

.. code-block:: shell

  pironman5 -rp 80

* 默认配置为 4 颗 RGB LED。如您连接了更多 LED，可使用以下命令修改数量：

.. code-block:: shell

  pironman5 -rl 12

.. _cc_control_fan:

控制 RGB 风扇
---------------------
IO 扩展板支持连接两颗 5V 非 PWM 风扇，两个风扇同步控制。

.. note::

  每次修改 ``pironman5.service`` 服务的状态后，都需要执行以下命令，使配置更改生效。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 使用命令设置 RGB 风扇的运行模式，不同模式对应不同的启动温度阈值：

例如：选择 **1: Performance** 模式，风扇将在温度达到 50°C 时自动启动。


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**：温度达 70°C 启动风扇  
* **3: Balanced**：温度达 67.5°C 启动  
* **2: Cool**：温度达 60°C 启动  
* **1: Performance**：温度达 50°C 启动  
* **0: Always On**：风扇始终运行

* 若您将风扇控制引脚连接至其他 GPIO 引脚，可使用以下命令修改：

.. code-block:: shell

  sudo pironman5 -gp 18


检查 OLED 显示屏
-----------------------------------

安装 ``pironman5`` 模块后，OLED 显示屏将在每次开机时显示 CPU、内存、磁盘使用情况、CPU 温度及设备 IP 地址。

若屏幕未显示内容，请首先检查 OLED 的 FPC 软排线是否正确连接。

随后可通过查看日志判断问题所在：

.. code-block:: shell

  cat /var/log/pironman5/

或检查 OLED 是否被识别，地址应为 0x3C：

.. code-block:: shell

  i2cdetect -y 1

检查红外接收器
---------------------------------------


* 安装 ``lirc`` 模块：

  .. code-block:: shell

    sudo apt-get install lirc -y

* 使用以下命令测试红外接收器：

  .. code-block:: shell

    mode2 -d /dev/lirc0

* 执行命令后，按下遥控器按钮，终端将输出该按钮的码值。

