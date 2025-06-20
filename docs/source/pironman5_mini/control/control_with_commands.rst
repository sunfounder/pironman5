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

  pironman5 -c

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

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]]
                                [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]]
                                [--background [BACKGROUND]]
                                [{start,restart,stop}]

  Pironman5 Mini

  位置参数:
   {start,restart,stop}  命令

  可选参数:
   -h, --help            显示帮助信息并退出
   -v, --version         显示版本号
   -c, --config          显示当前配置
   -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                         设置调试等级
   -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                         设置 RGB 颜色，16 进制格式（不含 #），如 00aabb
   -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                         设置 RGB 亮度，范围 0-100
   -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{...}]
                         设置 RGB 显示模式
   -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                         设置 RGB 变化速度，范围 0-100
   -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                         启用/禁用 RGB，取值 True/False
   -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                         设置 RGB LED 数量
   -u [{C,F}], --temperature-unit [{C,F}]
                         设置温度单位
   -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                         设置 GPIO 风扇模式，0: 始终开启，1: 性能，2: 清凉，3: 平衡，4: 安静
   -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                         设置 GPIO 风扇引脚
   -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                         设置风扇灯光状态 on/off/follow
   -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                         设置风扇灯光控制引脚
   --background [BACKGROUND]
                         后台运行

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

  pironman5 -re true

* 更改 RGB 颜色，输入对应的十六进制值，例如 ``fe1a1a``：

.. code-block:: shell

  pironman5 -rc fe1a1a

* 设置 RGB 灯亮度（范围：0 ~ 100%）：

.. code-block:: shell

  pironman5 -rb 100

* 切换 RGB 灯效模式，可选： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``：

.. note::

  若设置为 ``rainbow``、 ``rainbow_reverse`` 或 ``hue_cycle`` 模式，将无法再通过 ``pironman5 -rc`` 命令设置颜色。

.. code-block:: shell

  pironman5 -rs breathing

* 调节 RGB 灯变化速度（范围：0 ~ 100%）：

.. code-block:: shell

  pironman5 -rp 80

* 默认配置为 4 颗 RGB 灯，如有扩展请使用以下命令更新灯数：

.. code-block:: shell

  pironman5 -rl 12

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

* **4: Quiet**：70°C 启动风扇
* **3: Balanced**：67.5°C 启动风扇
* **2: Cool**：60°C 启动风扇
* **1: Performance**：50°C 启动风扇
* **0: Always On**：风扇始终运行

* 若将风扇控制引脚连接至 Raspberry Pi 的其他引脚，可通过以下命令修改控制引脚号：

.. code-block:: shell

  sudo pironman5 -gp 18
