USB HDMI 转接板
==========================================

.. image:: img/hdmi_adapter.jpeg

这款 USB HDMI 转接板是专为 Raspberry Pi 5 设计的，主要用于将 USB 和 HDMI 接口位置调整至树莓派的 USB 接口侧，提升可接性并优化线缆管理。

此外，该转接板将 HDMI 接口转换为标准 HDMI Type A 接口，以实现更广泛的兼容性。

**NVMe 额外供电接口**

该板集成了一个 5V 电源插针，用于为 NVMe PIP 提供额外供电。配合扩展插针，可连接至 NVMe 的附加电源接口，增强电力支持。

**1220 RTC 电池座**

板载集成了一个 1220 RTC 电池座，便于安装实时时钟电池。通过 SH1.0 2P 反向线缆与树莓派的 RTC 接口连接。

该电池座兼容 CR1220 和 ML1220 电池。如果使用 ML1220（锂锰氧电池），可在树莓派中配置充电功能。请注意，CR1220 不可充电。

**启用涓流充电功能**

.. warning::

  如果您使用的是 CR1220 电池，请勿启用涓流充电，否则可能会对电池造成不可修复的损坏，甚至损坏主板。

默认情况下，电池的涓流充电功能是关闭的。可以通过以下 ``sysfs`` 文件查看当前的涓流充电电压及其范围限制：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

要启用涓流充电，请在 ``/boot/firmware/config.txt`` 文件中添加 ``rtc_bbat_vchg`` 参数：

  * 打开配置文件： ``/boot/firmware/config.txt`` 。

    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
* 在 ``/boot/firmware/config.txt`` 文件中添加 ``rtc_bbat_vchg`` 参数。

    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000

重启后，系统会显示如下信息：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

这表示电池已处于涓流充电状态。如需关闭该功能，只需从 ``config.txt`` 中移除该 ``dtparam`` 行即可。

