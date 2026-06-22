.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_commands_5:

通过命令行进行控制
========================================

除了通过 Dashboard 查看 Pironman 5 的运行数据和控制各类设备，您还可以使用命令行实现同样的控制功能。

.. note::

  * 在 **Home Assistant** 系统中，仅可通过网页 ``http://<ip>:34001`` 使用 Dashboard 进行监控与管理。

.. * 在 **Batocera.linux** 系统中，仅支持使用命令行对 Pironman 5 进行监控与控制。请注意，修改配置后需执行 ``pironman5 restart`` 以使更改生效。

查看基本配置
-----------------------------------

``pironman5`` 模块提供了 Pironman 的基础配置，您可以通过以下命令查看当前配置项。

.. code-block:: shell

  sudo pironman5 -c

标准配置如下所示：

.. code-block::

  {
      "system": {
          "data_interval": 1,
          "database_retention_days": 30,
          "temperature_unit": "C",
          "enable_history": true,
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "rgb_enable": true,
          "rgb_color": "#0a1aff",
          "rgb_brightness": 100,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_led_count": 4,
          "rgb_led_count_min": 4,
          "gpio_fan_pin": 6,
          "gpio_fan_mode": 0,
          "debug_level": "INFO"
      }
  }

您可以根据需求自定义这些配置。

使用 ``pironman5`` 或 ``pironman5 -h`` 查看命令使用说明。

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl [{debug,info,warning,error,critical}]] [--background [BACKGROUND]] [-rd] [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-oe [OLED_ENABLE]]
                          [-od [OLED_DISK]] [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]]
                          [{start,restart,stop}]

  Pironman 5 command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Database retention days
    -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                          Debug level
    -rd, --remove-dashboard
                          Remove dashboard
    -cp, --config-path [CONFIG_PATH]
                          Config path
    -eh, --enable-history [ENABLE_HISTORY]
                          Enable history, True/true/on/On/1 or False/false/off/Off/0
    -re, --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rs, --rgb-style [RGB_STYLE]
                          RGB style: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
    -rc, --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u, --temperature-unit [{C,F}]
                          Temperature unit
    -gm, --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp, --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -oe, --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          OLED pages, split by ',': mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds

  Subcommands:
    {start,stop,launch-browser}
      start               Start Pironman5
      stop                Stop Pironman5
      launch-browser      Launch browser

.. note::

  每次修改 ``pironman5.service`` 状态后，需使用以下命令重启服务，使配置生效。

  .. code-block:: shell

     sudo systemctl restart pironman5.service


* 可使用 ``systemctl`` 工具查看 ``pironman5`` 程序状态：

  .. code-block:: shell

     sudo systemctl status pironman5.service

* 或通过日志文件检查程序运行状态：

  .. code-block:: shell

     cat /var/log/pironman5/pironman5.log


控制 RGB 灯效
----------------------

主板配备了 4 颗 WS2812 RGB LED，支持个性化控制。用户可开启/关闭灯效，变更颜色，调整亮度，设置显示模式以及动效速度。

.. note::

  每次修改 ``pironman5.service`` 状态后，需使用以下命令使配置更改生效。

  .. code-block:: shell

     sudo systemctl restart pironman5.service

* 开关 RGB 灯：使用 ``true`` 开启， ``false`` 关闭：

  .. code-block:: shell

     sudo pironman5 -re true

* 更改颜色：输入十六进制颜色值，例如 ``fe1a1a``\ ：

  .. code-block:: shell

     sudo pironman5 -rc fe1a1a

* 设置亮度（范围：0~100）：

  .. code-block:: shell

     sudo pironman5 -rb 100

* 更换 RGB 显示模式，可选项包括：

  ``solid`` / ``breathing`` / ``flow`` / ``flow_reverse`` / ``rainbow`` / ``rainbow_reverse`` / ``hue_cycle``

  .. note::

     若设置为 ``rainbow``\ 、 ``rainbow_reverse`` 或 ``hue_cycle`` 模式，将无法再使用 ``pironman5 -rc`` 指定颜色。

  .. code-block:: shell

     sudo pironman5 -rs breathing

* 设置动画速度（范围：0~100）：

  .. code-block:: shell

     sudo pironman5 -rp 80

* 默认配置为 4 颗 RGB LED。如您连接了更多 LED，可使用以下命令修改数量：

  .. code-block:: shell

     sudo pironman5 -rl 12

.. _cc_control_fan:

控制 GPIO 风扇
---------------------

IO 扩展板支持连接两颗 5V 非 CPU 风扇，两个风扇同步控制。

.. note::

  每次修改 ``pironman5.service`` 状态后，需使用以下命令使配置更改生效。

  .. code-block:: shell

     sudo systemctl restart pironman5.service

* 使用命令设置 GPIO 风扇的运行模式，不同模式对应不同的启动温度阈值。

  例如：选择 **1: Performance** 模式，风扇将在温度达到 50°C 时自动启动。

  .. code-block:: shell

     sudo pironman5 -gm 3

* **4: Quiet（静音）**\ ：温度达 70°C 启动风扇
* **3: Balanced（均衡）**\ ：温度达 67.5°C 启动
* **2: Cool（凉爽）**\ ：温度达 60°C 启动
* **1: Performance（性能）**\ ：温度达 50°C 启动
* **0: Always On（始终开启）**\ ：风扇始终运行

* 若您将风扇控制引脚连接至其他 GPIO 引脚，可使用以下命令修改：

  .. code-block:: shell

     sudo pironman5 -gp 18


关于 CPU 风扇
------------------------

CPU 风扇连接到树莓派 5 上专用的 4 针 CPU 风扇接口。其默认的控制策略是一种由固件管理的、基于 CPU 温度的多级智能调速方案。当您使用官方或兼容的 CPU 风扇并正确连接后，系统会根据 CPU 温度的变化自动调节风扇转速（在 50°C 以上开始运转），无需您进行任何手动干预。


检查 OLED 显示屏
-----------------------------------

安装 ``pironman5`` 模块后，OLED 显示屏将在每次开机时显示 CPU 使用率、内存使用率、磁盘使用情况、CPU 温度及设备 IP 地址。

若屏幕未显示内容，请首先检查 OLED 的 FPC 软排线是否正确连接。

随后可通过查看日志判断问题所在：

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

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
