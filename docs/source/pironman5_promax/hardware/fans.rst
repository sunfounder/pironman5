.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


风扇
============

PWM 风扇
-----------

Pironman 5 Pro MAX 配备了 3 个 PWM 风扇。

Pironman 5 Pro MAX 上的 PWM 风扇由 Raspberry Pi 系统进行控制。

在 Raspberry Pi 5 的散热方案设计中，尤其是在高负载情况下，Pironman 5 Pro MAX 采用了智能散热系统。它包含一个主 PWM 风扇和两个辅助 RGB 风扇，整体散热策略与 Raspberry Pi 5 的温度管理系统紧密结合。

PWM 风扇的工作根据 Raspberry Pi 5 的温度自动调节：

* 温度低于 50°C 时，PWM 风扇停止运行（0% 转速）。
* 达到 50°C 时，风扇以低速启动（30% 转速）。
* 达到 60°C 时，风扇提升至中速（50% 转速）。
* 达到 67.5°C 时，风扇提升至高速（70% 转速）。
* 达到 75°C 及以上时，风扇以全速运行（100% 转速）。

当温度下降时，同样按照上述温度区间进行调节，并带有 5°C 的迟滞机制。当温度比对应阈值低 5°C 时，风扇转速才会降低。

* 监控 PWM 风扇状态的命令。查看 PWM 风扇当前状态：

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* 查看 PWM 风扇转速：

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

在 Pironman 5 Pro MAX 中，PWM 风扇是维持设备最佳运行温度的重要组件，尤其是在执行高负载任务时，可确保 Raspberry Pi 5 高效且稳定地运行。

**风扇规格**

.. image:: img/size_fan.png

* **外形尺寸**\ ：40×40×10MM
* **额定输入功率**\ ：5V / 0.106A
* **额定转速**\ ：4000RPM
* **重量**\ ：13.5±5g/pcs
* **寿命**\ ：30,000 小时（室温 25°C）
* **噪音**\ ：22.31dBA
* **最大风量**\ ：2.46CFM
* **最大风压**\ ：0.62mm-H2O
* **工作温度**\ ：-10℃ ~ +60℃
* **存储温度**\ ：-20℃ ~ +70℃

**引脚定义**

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Pin
     - Color
     - Description
   * - 1
     - Blue
     - 用于控制风扇转速的 PWM 信号
   * - 2
     - Red
     - 5V 电源
   * - 3
     - Black
     - 接地
   * - 4
     - Yellow
     - 内置 RGB LED 数据输入
   * - 5 
     - Green
     - 内置 RGB LED 数据输出


塔式散热器
----------------------------

Pro MAX 配备的塔式散热器是一种高性能散热解决方案，可在高负载任务下保持 Raspberry Pi 5 的最佳工作温度。它采用大型铝制散热片和可通过 PWM 控制的风扇，根据需要自动调整散热性能。该塔式散热器专为 Raspberry Pi 5 设计，并可通过随附的螺丝和安装支架轻松安装。


.. image:: img/size_tower_cooler.png

**警告**

请勿触碰风扇叶片，也不要让电源线缠绕在风扇上或用力拉扯电源线，以免损坏风扇。

请勿在存在可燃气体或其他危险环境中使用。

当风扇运行时，请不要长时间阻挡风扇转动，否则持续的阻转会产生高温并导致风扇烧毁。

安装风扇时，请特别注意因共振或振动产生的噪音问题。

请勿从高处跌落 Icecube Tower Cooler，否则可能影响风扇叶片的平衡。