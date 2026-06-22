.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


USB HDMI 适配器
==========================================

.. image:: img/hdmi_adapter.png

该 USB HDMI 适配器板专为 Raspberry Pi 5 设计，其主要功能是将 USB 和 HDMI 接口重新布局，使其与 Raspberry Pi 的 USB 接口侧对齐，从而提升接口的可访问性并优化线缆管理。

此外，该适配器还将 HDMI 接口转换为标准 HDMI Type A 接口，从而提供更广泛的兼容性。

**NVMe 额外供电**

该板配备了一个专用于 NVMe PIP 供电的 5V 电源接口。通过配合扩展接口，可以连接到 NVMe 的额外供电接口，为其提供附加电源。

**1220RTC 电池座**

该板集成了一个 1220RTC 电池座，方便安装 RTC 电池。它通过 SH1.0 2P 反向连接线与 Raspberry Pi 的 RTC 接口相连。

该电池座同时兼容 CR1220 和 ML1220 电池。如果使用 ML1220（锂锰电池），可以在 Raspberry Pi 上直接配置充电功能。需要注意的是，CR1220 电池不可充电。

**启用涓流充电**

.. warning::

  如果使用的是 CR1220 电池，请不要启用涓流充电，否则可能会对电池造成不可修复的损坏，并可能损坏电路板。

默认情况下，电池的涓流充电功能是关闭的。以下 ``sysfs`` 文件显示当前的涓流充电电压及其限制：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

要启用涓流充电，需要在 ``/boot/firmware/config.txt`` 中添加 ``rtc_bbat_vchg``\ ：

  * 打开 ``/boot/firmware/config.txt``\ 。
  
    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
  * 在 ``/boot/firmware/config.txt`` 中添加 ``rtc_bbat_vchg``\ 。
  
    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
重启后，系统将显示：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

这表明电池已经启用了涓流充电。如需关闭该功能，只需从 ``config.txt`` 中删除对应的 ``dtparam`` 行即可。



音频接口
---------------------------------

本节介绍该板的音频输出功能，包括扬声器输出接口和耳机接口。

.. image:: img/hdmi_speaker_port.png

**扬声器接口**

该板配备了双声道扬声器输出接口，可连接两个 4Ω 3W 扬声器。

**扬声器开关**

扬声器音频信号来源于 HDMI0。如果 HDMI0 连接了带内置扬声器的显示器，则 Pironman 5 Pro Max 的扬声器和显示器扬声器可能会同时播放声音。\ **SPEAKER** 跳线可以控制此行为。

* 将跳线连接到左侧两个引脚（\ **ON**\ ），扬声器将 **始终启用**\ 。
* 将跳线连接到右侧两个引脚（\ **AUTO**\ ），当插入耳机或 HDMI0 连接设备时，扬声器将 **自动关闭**\ 。

因此，如果在连接 HDMI 显示器时仍希望使用板载扬声器，可以：

* 将显示器连接到 **HDMI1** 接口。
* 或将 **SPEAKER** 跳线设置为 **ON** 位置。

**3.5mm 音频接口**

耳机接口与扬声器使用相同的音频源，但输出的是 **未放大的音频信号**\ 。该接口为带开关的插孔，当插入耳机时会自动 **关闭扬声器功放**\ ，避免同时播放声音。

该接口为 4 针 TRRS 连接器，但仅支持 **标准立体声输出**\ ：

* **Tip (T)：** 左声道  
* **Ring 1 (R1)：** 右声道  
* **Ring 2 (R2)：** 地线  
* **Sleeve (S)：** 地线  

这种设计确保与大多数常见的四段式耳机接口标准兼容。