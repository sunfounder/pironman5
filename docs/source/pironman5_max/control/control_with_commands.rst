.. _max_view_control_commands:

通过命令行控制
========================================
除了通过 Dashboard 查看 Pironman 5 MAX 的数据并控制各个模块外，你还可以使用命令行方式进行控制。

.. note::

  * 对于 **Home Assistant** 系统，只能通过访问 ``http://<ip>:34001`` 的网页 Dashboard 进行监控与控制。

.. * 对于 **Batocera.linux** 系统，只能通过命令行进行监控与控制。请注意，任何配置更改都需要通过 ``pironman5 restart`` 命令重启服务后方可生效。

查看基本配置
-----------------------------------

``pironman5`` 模块提供了 Pironman 的基础配置，可通过以下命令查看：

.. code-block:: shell

  sudo pironman5 -c

标准配置示例如下：

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

你可以根据需要自定义这些配置。

使用 ``pironman5`` 或 ``pironman5 -h`` 查看指令帮助。

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]     
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-od [OLED_DISK]]
                          [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]] [-vp [VIBRATION_SWITCH_PIN]]
                          [-vu [VIBRATION_SWITCH_PULL_UP]] [-os [OLED_SLEEP_TIMEOUT]]
                          [{start,restart,stop}]

  Pironman 5 MAX command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                          Debug level
    --background [BACKGROUND]
                          Run in background
    -rd, --remove-dashboard
                          Remove dashboard
    -cp [CONFIG_PATH], --config-path [CONFIG_PATH]
                          Config path
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
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
    -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                          GPIO fan LED state on/off/follow
    -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                          GPIO fan LED pin
    -oe [OLED_ENABLE], --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -od [OLED_DISK], --oled-disk [OLED_DISK]
                          Set to display which disk on OLED. 'total' or the name of the disk, like mmbclk or nvme
    -oi [OLED_NETWORK_INTERFACE], --oled-network-interface [OLED_NETWORK_INTERFACE]
                          Set to display which ip of network interface on OLED, 'all' or the interface name, like eth0 or      
                          wlan0
    -or [{0,180}], --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -vp [VIBRATION_SWITCH_PIN], --vibration-switch-pin [VIBRATION_SWITCH_PIN]
                          Vibration switch pin
    -vu [VIBRATION_SWITCH_PULL_UP], --vibration-switch-pull-up [VIBRATION_SWITCH_PULL_UP]
                          Vibration switch pull up True/False
    -os [OLED_SLEEP_TIMEOUT], --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds



.. note::

  每次更改 ``pironman5.service`` 状态后，需使用以下命令使配置生效：

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* 使用 ``systemctl`` 工具查看 ``pironman5`` 程序状态：

  .. code-block:: shell

    sudo systemctl status pironman5.service

* 或查看程序生成的日志文件：

  .. code-block:: shell

    ls /var/log/pironman5/


控制 RGB 灯效
----------------------

板载 4 个 WS2812 RGB LED，可进行开关控制、颜色设置、亮度调整、显示模式切换及变化速度设置。

.. note::

  每次更改 ``pironman5.service`` 状态后，需使用以下命令使配置生效：

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 设置 RGB 灯开启或关闭， ``true`` 表示开启， ``false`` 表示关闭：

.. code-block:: shell

  sudo pironman5 -re true

* 设置 RGB 灯颜色，输入所需的十六进制颜色值，如 ``fe1a1a``：

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* 设置亮度，范围为 0 ~ 100：

.. code-block:: shell

  sudo pironman5 -rb 100

* 设置 RGB 显示模式，支持的模式包括： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``：

.. note::

  如果设置为 ``rainbow``、 ``rainbow_reverse`` 或 ``hue_cycle``，将无法再设置自定义颜色。

.. code-block:: shell

  sudo pironman5 -rs breathing

* 设置变化速度，范围为 0 ~ 100：

.. code-block:: shell

  sudo pironman5 -rp 80

* 默认包含 4 个 RGB 灯，如连接更多，可使用以下命令修改数量：

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_max:

控制 RGB 风扇
---------------------

IO 扩展板支持最多两个 5V 非 PWM 风扇，风扇统一控制。

.. note::

  每次更改 ``pironman5.service`` 状态后，需使用以下命令使配置生效：

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 使用命令设置风扇运行模式，不同模式决定启动温度：

例如设置为 **1: Performance** 模式时，风扇将在 50°C 启动：

.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**：70°C 启动
* **3: Balanced**：67.5°C 启动
* **2: Cool**：60°C 启动
* **1: Performance**：50°C 启动
* **0: Always On**：始终运行

* 如更换风扇控制引脚，可使用如下命令：

.. code-block:: shell

  sudo pironman5 -gp 18


检查 OLED 屏幕
-----------------------------------

安装 ``pironman5`` 库后，OLED 屏幕将自动显示 CPU、内存、磁盘使用率、CPU 温度及树莓派 IP，每次开机时自动刷新。

若 OLED 无显示，请先检查 FPC 线缆是否连接牢固。

接着可通过以下命令查看日志确认问题：

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

或检查 OLED 的 i2c 地址 0x3C 是否被识别：

.. code-block:: shell

  i2cdetect -y 1

检查红外接收器
---------------------------------------



* 安装 ``lirc`` 模块：

  .. code-block:: shell

    sudo apt-get install lirc -y

* 使用以下命令测试红外接收功能：

  .. code-block:: shell

    mode2 -d /dev/lirc0

* 执行命令后，按下遥控器上的任意按键，即可在终端打印对应码值。

