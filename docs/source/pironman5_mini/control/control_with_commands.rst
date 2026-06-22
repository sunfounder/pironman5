.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _view_control_commands_mini:

通过命令进行控制
========================================
除了使用仪表盘查看 Pironman 5 Mini 的运行数据和控制各项设备，您还可以通过命令行对其进行操作。

.. note::

  * 对于 **Home Assistant** 系统，仅支持通过浏览器访问 ``http://<ip>:34001`` 仪表盘进行监控与控制。
  * 请注意，任何配置更改后都必须通过 ``pironman5 restart`` 命令重启服务才能生效。

查看基础配置
-----------------------------------

``pironman5`` 模块提供了 Pironman 的基础配置，您可以通过以下命令查看当前配置：

.. code-block:: shell

  sudo pironman5 -c

标准配置如下所示：

.. code-block::

  {
      "system": {
          "rgb_color": "feff00",
          "rgb_brightness": 30,
          "rgb_style": "hue_cycle",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 12,
          "temperature_unit": "C",
          "gpio_fan_pin": 5,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "follow",
          "gpio_fan_led_pin": 6
      }
  }

您可以根据实际需求自定义上述配置。

使用 ``pironman5`` 或 ``pironman5 -h`` 可查看命令帮助说明。

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]]
                          [{start,restart,stop}]

  Pironman 5 command line interface

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

.. note::

  每次修改 ``pironman5.service`` 状态后，需使用以下命令使配置生效：

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* 使用 ``systemctl`` 工具检查 ``pironman5`` 程序状态：

  .. code-block:: shell

    sudo systemctl status pironman5.service

* 或查看程序生成的日志文件：

  .. code-block:: shell

    ls /var/log/pironman5/
    cat /var/log/pironman5/main.log

控制 RGB 灯效
----------------------

主板集成 4 颗 WS2812 RGB LED，可进行个性化控制。用户可以开启/关闭灯光、调节颜色与亮度、切换灯效模式并设置变化速度。

.. note::

  每次修改 ``pironman5.service`` 状态后，需使用以下命令使配置生效：

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 开关 RGB 灯光， ``true`` 表示开启， ``false`` 表示关闭：

.. code-block:: shell

  sudo pironman5 -re true

* 更改 RGB 颜色，输入对应的十六进制值，例如 ``fe1a1a``\ ：

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* 设置 RGB 灯亮度（范围：0 ~ 100%）：

.. code-block:: shell

  sudo pironman5 -rb 100

* 切换 RGB 灯效模式，可选： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``\ ：

.. note::

  若设置为 ``rainbow``\ 、 ``rainbow_reverse`` 或 ``hue_cycle`` 模式，将无法再通过 ``sudo pironman5 -rc`` 命令设置颜色。

.. code-block:: shell

  sudo pironman5 -rs breathing

* 调节 RGB 灯变化速度（范围：0 ~ 100%）：

.. code-block:: shell

  sudo pironman5 -rp 80

* 默认配置为 4 颗 RGB 灯，如有扩展请使用以下命令更新灯数：

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_mini:

控制 RGB 风扇
---------------------

扩展板支持连接 5V 非 PWM 风扇。

.. note::

  每次修改 ``pironman5.service`` 状态后，需使用以下命令使配置生效：

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 使用以下命令设置 RGB 风扇的工作模式，不同模式决定风扇的启动温度阈值：

例如，设置为 **1: Performance** 模式时，RGB 风扇将在温度达到 50°C 时启动。


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**\ ：70°C 启动风扇
* **3: Balanced**\ ：67.5°C 启动风扇
* **2: Cool**\ ：60°C 启动风扇
* **1: Performance**\ ：50°C 启动风扇
* **0: Always On**\ ：风扇始终运行

* 若将风扇控制引脚连接至 Raspberry Pi 的其他引脚，可通过以下命令修改控制引脚号：

.. code-block:: shell

  sudo pironman5 -gp 18


**关于核心风扇**

核心风扇连接到树莓派5上专用的4针PWM风扇接口。其默认的控制策略是一种由固件管理的、基于CPU温度的多级智能调速方案。这意味着，当你使用官方或兼容的PWM风扇并正确连接后，系统会根据CPU温度的变化自动调节风扇转速（在50°C以上开始运转），无需你进行任何手动干预。


