USB HDMI适配器
==========================================

.. image:: img/hdmi_adapter.jpeg

该USB HDMI适配器板专为Raspberry Pi 5设计，其主要功能是将USB和HDMI连接端口重新定位，使其与Raspberry Pi的USB接口侧对齐，从而提高可接入性和电缆管理的便利性。

此外，HDMI端口被转换为标准的HDMI Type A接口，提供更广泛的兼容性。

**NVMe额外电源供应**

该板配有专门用于NVMe PIP电源的5V电源引脚。配合扩展头，可以连接到NVMe的额外电源接口，以提供额外的电力。

**1220RTC电池座**

板上集成了一个1220RTC电池座，便于安装RTC电池。它通过SH1.0 2P反向电缆连接到Raspberry Pi的RTC接口。

该电池座兼容CR1220和ML1220电池。如果使用ML1220（锂锰二氧化物电池），可以直接在Raspberry Pi上配置充电。请注意，CR1220电池不可充电。

**启用涓流充电**

.. warning::

  如果使用CR1220电池，请不要启用涓流充电功能，因为这可能会对电池造成无法修复的损害，并且有可能损坏电路板。

默认情况下，电池的涓流充电功能是禁用的。 ``sysfs`` 文件显示当前的涓流充电电压和限制：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

要启用涓流充电，请将 ``rtc_bbat_vchg`` 添加到 ``/boot/firmware/config.txt`` ：

  * 打开 ``/boot/firmware/config.txt`` 。

    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
          
  * 将 ``rtc_bbat_vchg`` 添加到 ``/boot/firmware/config.txt`` 。

    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
重启后，系统会显示：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

这确认了电池现在正在进行涓流充电。要禁用此功能，只需从 ``config.txt`` 中删除 ``dtparam`` 行。

