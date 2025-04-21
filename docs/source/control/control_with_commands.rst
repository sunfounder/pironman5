.. _view_control_commands:

通过命令控制
========================================
除了通过仪表盘查看Pironman 5的数据并控制各种设备外，你还可以使用命令来进行控制。

.. note::

  * 对于 **Home Assistant** 系统，你只能通过打开 ``http://<ip>:34001`` 的网页访问仪表盘来监控和控制Pironman 5。
  * 对于 **Batocera.linux** 系统，你只能通过命令来监控和控制Pironman 5。需要注意的是，任何配置的更改都需要重启服务，使用 ``pironman5 restart`` 命令才能生效。

查看基本配置
-----------------------------------

``pironman5`` 模块提供了Pironman的基本配置，你可以通过以下命令查看：

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

根据需要定制这些配置。

使用 ``pironman5`` 或 ``pironman5 -h`` 来获取更多指令。

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format with or without # (e.g. #FF0000 or 00aabb)
    -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                          RGB style
    -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin

.. note::

  每次修改 ``pironman5.service`` 的状态时，需要使用以下命令使配置更改生效。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* 使用 ``systemctl`` 工具验证 ``pironman5`` 程序的状态。

  .. code-block:: shell

    sudo systemctl status pironman5.service

* 或者，查看程序生成的日志文件。

  .. code-block:: shell

    cat /opt/pironman5/log


控制RGB LED
----------------------
该板配备4个WS2812 RGB LED，提供可自定义的控制功能。用户可以开启或关闭它们，改变颜色，调节亮度，切换RGB LED显示模式，并设置变化的速度。

.. note::

  每次修改 ``pironman5.service`` 的状态时，需要使用以下命令使配置更改生效。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 要修改RGB LED的开关状态，使用 ``true`` 开启RGB LED， ``false`` 关闭它们。

.. code-block:: shell

  pironman5 -re true

* 要改变RGB LED的颜色，输入所需的十六进制颜色值，例如 ``fe1a1a`` 。

.. code-block:: shell

  pironman5 -rc fe1a1a

* 要调整RGB LED的亮度（范围：0 ~ 100%）：

.. code-block:: shell

  pironman5 -rb 100

* 要切换RGB LED显示模式，从以下选项中选择： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` ：

.. note::

  如果你将RGB LED显示模式设置为 ``rainbow`` 、 ``rainbow_reverse`` 或 ``hue_cycle`` ，你将无法使用 ``pironman5 -rc`` 设置颜色。

.. code-block:: shell

  pironman5 -rs breathing

* 要修改变化速度（范围：0 ~ 100%）：

.. code-block:: shell

  pironman5 -rp 80

* 默认配置包括4个RGB LED。连接额外的LED并更新数量：

.. code-block:: shell

  pironman5 -rl 12

.. _cc_control_fan:

控制RGB风扇
---------------------
IO扩展板支持最多两个5V非PWM风扇。两个风扇一起控制。

.. note::

  每次修改 ``pironman5.service`` 的状态时，需要使用以下命令使配置更改生效。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 你可以使用命令来配置两个RGB风扇的工作模式。这些模式决定了RGB风扇启动的条件。

例如，如果设置为 **1: Performance/高性能** 模式，RGB风扇将在50°C时启动。

.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet/静音**：RGB风扇将在70°C时启动。
* **3: Balanced/平衡**：RGB风扇将在67.5°C时启动。
* **2: Cool/冷却**：RGB风扇将在60°C时启动。
* **1: Performance/高性能**：RGB风扇将在50°C时启动。
* **0: Always On/始终开启**：RGB风扇始终开启。

* 如果你将RGB风扇的控制引脚连接到Raspberry Pi的不同引脚，可以使用以下命令更改引脚编号。

.. code-block:: shell

  sudo pironman5 -gp 18


查看OLED屏幕
-----------------------------------

安装 ``pironman5`` 库后，OLED屏幕将显示CPU、RAM、磁盘使用情况、CPU温度和Raspberry Pi的IP地址，并在每次重启时显示这些信息。

如果你的OLED屏幕没有显示任何内容，你需要首先检查OLED的FPC电缆是否连接正确。

然后，你可以通过以下命令查看程序日志，了解可能出现的问题。

.. code-block:: shell

  cat /var/log/pironman5/

或者，检查OLED的i2c地址0x3C是否被识别：

.. code-block:: shell

  i2cdetect -y 1

检查红外接收器
---------------------------------------


* 安装 ``lirc`` 模块：

  .. code-block:: shell

    sudo apt-get install lirc -y

* 现在，通过运行以下命令测试红外接收器。

  .. code-block:: shell

    mode2 -d /dev/lirc0

* 运行命令后，按下遥控器上的按钮，按钮的代码将被打印出来。

