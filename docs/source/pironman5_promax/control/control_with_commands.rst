.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_view_control_commands:

Control with Commands
========================================
除了通过 Dashboard 查看 Pironman 5 Pro MAX 的数据并控制各类设备外，您也可以通过命令行进行控制。

.. .. note::

..   * 对于 **Home Assistant** 系统，只能通过访问网页 ``http://<ip>:34001`` 的 Dashboard 来监控和控制 Pironman 5 Pro MAX。
 
.. * 对于 **Batocera.linux** 系统，只能通过命令行方式监控和控制 Pironman 5 Pro MAX。需要注意的是，任何配置更改都必须执行 ``pironman5 restart`` 重启服务后才会生效。

查看基础配置
-----------------------------------

``pironman5`` 模块提供了一组 Pironman 的基础配置，您可以使用以下命令查看：

.. code-block:: shell

  sudo pironman5 -c

默认配置如下所示：

.. code-block:: 

  {
      "system": {
          "data_interval": 1,
          "enable_history": true,
          "rgb_color": "#ff3dbe",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 18,
          "temperature_unit": "C",
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "default_dashboard_page": "small",
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "debug_level": "INFO"
      }
  }

您可以根据需要修改这些配置。

使用 ``pironman5`` 或 ``pironman5 -h`` 查看命令说明。

.. code-block::

  usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]]
                  [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-oe [OLED_ENABLE]]
                  [-or [{0,180}]] [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                  {start,stop,launch-browser} ...

  Pironman 5 Pro Max command line interface

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

  每次修改 ``pironman5.service`` 的配置后，都需要执行以下命令使配置生效。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* 使用 ``systemctl`` 工具检查 ``pironman5`` 程序的运行状态。

  .. code-block:: shell

    sudo systemctl status pironman5.service

* 也可以查看程序生成的日志文件。

  .. code-block:: shell

    ls /var/log/pironman5/


**控制 RGB 灯**
----------------------
该主板配备了 18 个 WS2812B 可编程 RGB 灯：其中 6 个位于主板上，另外 12 个集成在 RGB 风扇中。用户可以控制灯光的开关、颜色、亮度、显示模式、动画速度以及启用的 LED 数量。 

.. note::

  修改 ``pironman5.service`` 的配置后，必须重启服务才能生效：

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* **启用/禁用 RGB 灯**\ ：使用 ``true`` 开启，\ ``false`` 关闭。

  .. code-block:: shell

    sudo pironman5 -re true

* **更改颜色**\ ：使用十六进制颜色值（不带 `#`），例如 ``fe1a1a`` 表示红色。

  .. code-block:: shell

    sudo pironman5 -rc fe1a1a

* **调整亮度**\ ：设置范围为 0% 到 100%。

  .. code-block:: shell

    sudo pironman5 -rb 75

* **更改显示模式**\ ：可选多种动画模式：

  * ``solid``\ ：静态颜色  
  * ``breathing``\ ：呼吸效果（渐亮渐暗）  
  * ``flow`` / ``flow_reverse``\ ：颜色流动效果  
  * ``rainbow`` / ``rainbow_reverse``\ ：彩虹循环效果  
  * ``hue_cycle``\ ：色相平滑循环  

  .. code-block:: shell

    sudo pironman5 -rs breathing

  .. note::

    当使用 ``rainbow``\ 、 ``rainbow_reverse`` 或 ``hue_cycle`` 模式时，通过 ``pironman5 -rc`` 设置的颜色将被自动循环效果覆盖。

* **调整动画速度**\ ：设置效果速度，范围为 0%（最慢）到 100%（最快）。

  .. code-block:: shell

    sudo pironman5 -rp 50

* **设置 LED 数量**\ ：系统默认控制 18 个 LED。如果您扩展了额外的 WS2812B 灯带，请相应修改总数量。

  .. code-block:: shell

    sudo pironman5 -rl 12


**风扇**
--------------------------------

风扇通过 Raspberry Pi 5 上的专用 4 针 PWM 风扇接口连接。其默认控制策略为基于 CPU 温度的固件级多档智能调速机制。这意味着，当您使用官方或兼容的 PWM 风扇并正确连接后，系统会根据 CPU 温度变化自动调节风扇转速（约在 50°C 以上开始工作），无需手动干预。 



**检查 OLED 屏幕**
-----------------------------------

在安装 ``pironman5`` 库并重启后，0.96 英寸 OLED 屏幕默认会显示系统信息（CPU、内存、磁盘、温度、IP）。

如果 OLED 屏幕没有显示：

1. 确认 OLED 的 FPC 排线已牢固连接到主板。  
2. 检查服务日志是否有报错：

    .. code-block:: shell

      sudo journalctl -u pironman5.service -f

    或查看专用日志：

    .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

3. 确认 OLED 已在 I2C 总线上被检测到（地址为 `0x3C`）：

    .. code-block:: shell

      i2cdetect -y 1

**OLED 配置命令**

* **启用/禁用 OLED**\ ：打开或关闭 OLED 显示。

  .. code-block:: shell
  
    sudo pironman5 -oe false

* **旋转屏幕**\ ：设置显示方向为 ``0`` （默认）或 ``180`` 度。

  .. code-block:: shell
  
    sudo pironman5 -or 180

* **配置显示页面**\ ：选择循环显示的信息页面。可选页面包括： ``mix`` （总览）、 ``performance`` （CPU/内存详情）、 ``ips`` （网络 IP）、 ``disk`` （存储）。多个页面用逗号分隔。

  .. code-block:: shell
  
    sudo pironman5 -op mix,ips,disk
  
* **设置休眠时间**\ ：设置 OLED 在无操作时自动关闭的时间（单位：秒，0 表示不休眠）。

  .. code-block:: shell
  
    sudo pironman5 -os 120

**检查红外接收器**
---------------------------------------

内置红外接收器支持通过遥控器进行控制。

1. 安装所需软件：

  .. code-block:: shell
  
    sudo apt-get install lirc -y

2. 测试接收器。运行以下命令，然后用遥控器对准设备并按键，应能看到原始信号输出。

  .. code-block:: shell
  
    mode2 -d /dev/lirc0
  
3. 若需要配置特定遥控器按键（例如用于 Kodi 或 Volumio），则需要在 `/etc/lirc/lircd.conf` 文件中配置对应的遥控器编码。



**通用系统命令**
----------------------------

* **显示版本**\ ：显示已安装的 ``pironman5`` 软件包版本。

  .. code-block:: shell
  
    sudo pironman5 -v

* **显示当前配置**\ ：显示所有当前配置设置。

  .. code-block:: shell
  
    sudo pironman5 -c

* **设置温度单位**\ ：在摄氏度（\ ``C``\ ）和华氏度（\ ``F``\ ）之间切换温度显示单位。

  .. code-block:: shell
  
    sudo pironman5 -u F

* **配置数据记录**\ ：

  * **设置数据库保留天数**\ ：控制历史数据（例如温度记录）保留的天数。

    .. code-block:: shell

      sudo pironman5 -drd 30

  * **启用/禁用历史记录**\ ：开启或关闭数据采集。

    .. code-block:: shell

      sudo pironman5 -eh false

* **设置日志详细级别**\ ：调整系统日志的详细程度。可选项： ``DEBUG``\ 、 ``INFO``\ 、 ``WARNING``\ 、 ``ERROR``\ 、 ``CRITICAL``\ 。

  .. code-block:: shell
  
    sudo pironman5 -dl DEBUG

* **移除 Web 仪表板**\ ：卸载可选的基于网页的管理界面。

  .. code-block:: shell
  
    sudo pironman5 -rd

* **指定自定义配置路径**\ ：使用位于非默认路径的配置文件。

  .. code-block:: shell
  
    sudo pironman5 -cp /home/pi/my_custom_config.json

**服务管理子命令**
-----------------------------------

* **启动 Pironman5 服务**\ ：手动启动后台服务，该服务负责管理 LED、风扇、OLED 等设备。

  .. code-block:: shell
  
    sudo pironman5 start

* **停止 Pironman5 服务**\ ：安全停止后台服务。

  .. code-block:: shell
  
    sudo pironman5 stop

* **在浏览器中打开 Web 仪表板**\ ：如果已安装 Web 仪表板，该命令会在默认浏览器中打开它。

  .. code-block:: shell
  
    sudo pironman5 launch-browser