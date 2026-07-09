.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

常见问题（FAQ）
==================


快速故障排除
-------------------------------

* 电源按钮不工作 → :ref:`faq_power_button_not_work_5`
* OLED 屏幕不工作 → :ref:`faq_oled_5`
* RGB 灯不工作 → :ref:`faq_rgb_5`
* GPIO 风扇不工作 → :ref:`faq_gpio_fans_5`
* CPU 风扇不转 → :ref:`faq_pwm_fan_5`
* 仪表盘不显示数据 → :ref:`faq_dashboard_5`
* NVMe SSD 无法识别 → :ref:`faq_nvme_5`
* NVMe SSD 被识别但导致系统重启 → :ref:`faq_nvme_link_down_5`



1. 硬件
-------------------------------


.. _compatible_systems_5:

兼容系统
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_com_os

以下系统已通过 Raspberry Pi 5 的兼容性测试：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

.. end_faq_com_os


电源按钮
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_5`

.. start_faq_power_button

该电源按钮为 Raspberry Pi 5 的扩展电源键，功能与树莓派 5 自带电源按钮一致。

* 短按：开机 / 唤醒 OLED / 切换 OLED 页面。
* 长按 2 秒：安全关机（需配置 |link_safe_shutdown|）。
* 长按 5 秒：强制关机。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

.. end_faq_power_button


.. _faq_power_button_not_work_5:

电源按钮不工作？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_power_button_not_work

#. 首先，确认预期的电源按钮行为：

   * **Raspberry Pi OS Desktop**\ ：快速按两次电源按钮即可关机。长按 5 秒强制硬关机。关机状态下按一次开机。
   * **Raspberry Pi OS Lite**\ ：按一次电源按钮关机。长按 5 秒强制硬关机。关机状态下按一次开机。

#. 检查电源转换器引脚是否与 Raspberry Pi 5 的 J2 焊盘正确对齐（位于 RTC 电池连接器和板边之间）。

#. 检查电源转换器插座内的引脚是否与电源按钮连接器正确对齐。如有必要，重新连接电源按钮线缆。

#. 使用螺丝刀短暂短接电源转换器插座上连接按钮的两个引脚。如果 Pi 启动，则按钮本身可能有故障；否则，问题可能出在转换器板或 Pi 5 连接上。

.. end_faq_power_button_not_work


风道设计
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_airflow_direction

Pironman 5 机箱的内部风道经过精心设计，以最大化散热效率。冷空气主要从 GPIO 接口及其他开口进入机箱内部，并通过配备高性能风扇的塔式散热器进行降温，最后由侧边的两颗 GPIO 风扇将热空气排出。

详细演示请参考下方视频：

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

.. end_faq_airflow_direction


塔式散热器铜管尾端
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_copper_pipe_ends

塔式散热器顶部的 U 型热管在出厂时会进行压扁处理，以便更好地穿过铝制散热鳍片，这属于正常的生产工艺。

.. image:: img/tower_cooler1.png

.. end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_ai_hat

Raspberry Pi AI HAT+ 与 Pironman 5 不兼容。

.. image:: img/output3.png
    :width: 400

Raspberry Pi AI 套件由 Raspberry Pi M.2 HAT+ 与 Hailo AI 加速模块组成。

.. image:: img/output2.jpg
    :width: 400

您可以将 Hailo AI 加速模块从套件中拆下，直接插入 Pironman 5 的 NVMe PIP 模块中使用。

.. image:: img/output4.png
    :width: 800

.. end_faq_ai_hat



2. 散热与风扇
-------------------------------


.. _faq_pwm_fan_5:

CPU 风扇不转？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_pwm_fan

Pironman 5 上的 CPU 风扇由树莓派系统控制。CPU 风扇转速取决于树莓派 5 的 CPU 温度。

默认 CPU 风扇曲线：

* < 50°C：关闭（0%）
* 50°C+：低速（30%）
* 60°C+：中速（50%）
* 67.5°C+：高速（70%）
* 75°C+：全速（100%）

检查当前 CPU 温度（示例输出：\ ``temp=48.7'C``\ ）：

.. code-block:: shell

   vcgencmd measure_temp

您可以使用以下命令手动控制 CPU 风扇：

.. code-block:: shell

   pinctrl FAN_PWM op dl   # 启用风扇（低电平有效）
   pinctrl FAN_PWM op dh   # 禁用风扇（高电平有效）
   pinctrl FAN_PWM a0      # 自动模式

您也可以通过编辑以下文件来调整 CPU 风扇温度阈值：

.. code-block:: shell

   nano /boot/firmware/config.txt

添加：

.. code-block:: text

   dtparam=cooling_fan=on
   dtparam=fan_temp0=40000
   dtparam=fan_temp0_hyst=10000
   dtparam=fan_temp0_speed=125

此配置将在 40°C 时启动 CPU 风扇，PWM 速度级别为 125。

保存文件后，重启树莓派以使更改生效。

.. end_faq_pwm_fan


.. _faq_gpio_fans_5:

GPIO 风扇不工作？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_gpio_fans

首先，检查 IO 扩展板上的 FAN 跳线帽是否已正确安装。

.. image:: hardware/img/io_board_fan_j9.png

然后将 GPIO 风扇设置为 **Always On** 模式，检查风扇是否开始旋转。

.. code-block:: shell

   sudo pironman5 -gm 0

您也可以将 GPIO 风扇直接连接到树莓派的 ``5V`` 和 ``GND`` 引脚进行测试。

如果风扇直接连接时正常旋转，则问题可能与 IO 扩展板有关。请联系我们获取进一步支持。

如果问题仍然存在，请打开仪表盘的 **日志** 页面检查错误消息。您也可以将以下日志文件发送给我们：

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

.. end_faq_gpio_fans

3. OLED 与 RGB
-------------------------------


.. _faq_oled_5:

OLED 屏幕无法正常显示？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_5`
.. |link_compatible_systems| replace:: :ref:`compatible_systems_5`

.. start_faq_oled

若 OLED 屏幕没有显示或显示异常，请依照以下步骤排查：

#. 确保 OLED 屏幕的 FPC 排线已牢固连接。建议重新连接后再上电启动。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. 确认树莓派运行的是支持的操作系统。

   参见 |link_compatible_systems|。

#. OLED 屏幕首次通电可能只显示像素方块。您需要根据 |link_set_up_pironman5| 的说明完成配置，之后即可正常显示信息。

#. 使用以下命令检测 OLED 的 I2C 地址 ``0x3C`` 是否被识别：

   .. code-block:: shell

      sudo i2cdetect -y 1

   * 若检测到 I2C 地址 ``0x3C``\ ，请重启 Pironman 5 服务：

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * 若未检测到，请开启 I2C：

     .. code-block:: shell

        sudo nano /boot/firmware/config.txt

     添加：

     .. code-block:: shell

        dtparam=i2c_arm=on

     保存文件并重启树莓派。

#. 如果问题仍然存在，请将以下日志文件发送给我们：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_oled


.. _faq_rgb_5:

RGB 灯无法点亮？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_rgb

#. J9 上方的 IO 扩展板有两个引脚用于连接 RGB 灯至 GPIO10，请确保这两个引脚上的跳线帽已正确安装。

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. 确认树莓派运行的是兼容的操作系统。

   参见 |link_compatible_systems|。

#. 运行以下命令启用 SPI：

   .. code-block:: shell

      sudo raspi-config

   进入：

   ``3 Interfacing Options`` → ``I3 SPI`` → ``YES``

   然后重启树莓派。

#. 如果问题仍然存在，请将以下日志文件发送给我们：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_rgb

.. _faq_customize_oled_5:

如何自定义 OLED 显示？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_customize_oled

如果您想自定义 OLED 显示内容，例如添加自定义的 2-4 位图像显示，您可以通过以下两种方式修改 OLED 页面文件。

* **方法一：直接修改已安装的文件**

  #. 列出 OLED 页面文件：

     .. code-block:: shell

        ls /opt/pironman5/venv/lib/python3.13/site-packages/pm_auto/addons/oled/pages/

  #. 修改所需的 Python 文件。

  #. 重启服务以应用更改：

     .. code-block:: shell

        sudo systemctl restart pironman5.service


* **方法二：克隆并重新安装 ``pm_auto``**

  #. 克隆 ``pm_auto`` 仓库：

     .. code-block:: shell

        git clone -b 1.4.x https://github.com/sunfounder/pm_auto/

  #. 进行更改后，重新安装修改后的包：

     .. code-block:: shell

        sudo /opt/pironman5/venv/bin/pip3 uninstall pm_auto -y && \
        sudo /opt/pironman5/venv/bin/pip3 install ~/pm_auto --no-build-isolation && \
        sudo chown -R pironman5:pironman5 /opt/pironman5

  #. 重启服务：

     .. code-block:: shell

        sudo systemctl restart pironman5.service

* **测试和调试**

  查看运行日志：

  .. code-block:: shell

     journalctl -xefu pironman5.service

  您也可以停止服务并手动运行以加快测试：

  .. code-block:: shell

     sudo systemctl stop pironman5.service
     sudo systemctl restart pironman5.service

.. end_faq_customize_oled

4. 仪表盘与软件
-------------------------------


.. _faq_dashboard_5:

仪表盘不显示数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_dashboard

如果仪表盘不显示数据，请先打开仪表盘的 **日志** 页面，检查是否有与 ``influxdb`` 相关的错误消息。

常见错误包括：

* ``database not found``
* ``failed to connect to influxdb``
* ``connection refused``
* ``timeout``

您可以尝试以下步骤来解决问题。

#. 清除浏览器缓存，或使用 **无痕/隐私** 模式重新打开仪表盘页面。

#. 检查以下服务是否正常运行：

   .. code-block:: shell

      sudo systemctl status pironman5 --no-pager
      sudo systemctl status influxdb --no-pager

   两个服务都应显示：

   .. code-block:: text

      active (running)

#. 如果任一服务运行不正常，请重新启动它们：

   .. code-block:: shell

      sudo systemctl restart influxdb
      sudo systemctl restart pironman5

   然后等待约 30 秒，刷新仪表盘页面。

#. 检查 ``pironman5`` 数据库是否存在：

   .. code-block:: shell

      influx

   然后运行：

   .. code-block:: text

      SHOW DATABASES;

   您应该看到：

   .. code-block:: text

      pironman5
      _internal

#. 如果数据库缺失或损坏，您可以尝试从仪表盘中清除历史数据：

   ``Settings → Clear All Data``

#. 如果尝试以上所有步骤后问题仍然存在，我们建议重新安装 Raspberry Pi OS 和 Pironman 5 软件。

.. end_faq_dashboard


如何禁用 Web 控制面板？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_5`

.. start_faq_disable_dashboard

安装 ``pironman5`` 模块后，您可以访问 |link_view_control_dashboard|。

若不需要该功能，并希望减少 CPU 和内存占用，可以在安装 ``pironman5`` 时添加 ``--disable-dashboard`` 参数来禁用控制面板：

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

如果您已经安装了 ``pironman5``\ ，可以卸载仪表盘模块和 ``influxdb``\ ：

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. end_faq_disable_dashboard


如何卸载并重新安装 Pironman 5 软件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_reinstall_pironman5

#. 卸载当前的 ``pironman5`` 软件：

   .. code-block:: shell

      cd ~/pironman5
      sudo python3 install.py --uninstall

#. 按提示重启树莓派，然后删除 ``pironman5`` 目录：

   .. code-block:: shell

      cd ~/
      sudo rm -rf pironman5

#. 运行以下命令为您的 Pironman 5 型号重新安装软件：

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash

.. end_faq_reinstall_pironman5


如何使用 ``pironman5`` 命令控制组件？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`view_control_commands_5`

.. start_faq_pironman5_command

您可以参考以下教程，使用 ``pironman5`` 命令控制 Pironman 5 系列的组件。

* |link_view_control_commands|

.. end_faq_pironman5_command



5. 启动与存储
-------------------------------


PI5 无法启动（红灯常亮）？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_5`

.. start_faq_pi5_boot_fail

此问题可能是由于系统更新、启动顺序更改或引导程序损坏导致的。您可以尝试以下步骤来解决该问题：

#. 检查 USB-HDMI 适配器连接

   * 请仔细检查 USB-HDMI 适配器是否牢固连接到 PI5。
   * 尝试拔下并重新插入 USB-HDMI 适配器。
   * 然后重新连接电源，检查 PI5 是否能正常启动。

#. 在机箱外测试 PI5

   * 如果重新插拔适配器仍未解决问题：
   * 将 PI5 从 Pironman 5 机箱中取出。
   * 使用电源适配器直接为 PI5 供电（不通过机箱）。
   * 检查是否能够正常启动。

#. 恢复引导程序

   * 如果 PI5 仍无法启动，可能是引导程序已损坏。您可以参考此教程：|link_update_bootloader|，并选择从 SD 卡或 NVMe/USB 启动。
   * 将准备好的 SD 卡插入 PI5，通电后至少等待 10 秒。恢复完成后，取出并重新格式化 SD 卡。
   * 然后使用 Raspberry Pi Imager 烧录最新的 Raspberry Pi OS，将卡插回并再次尝试启动。

.. end_faq_pi5_boot_fail


.. _faq_nvme_5:

NVMe PIP 模块无法正常工作？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os| replace:: :ref:`install_the_os_5`
.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_5`

.. start_faq_nvme_pip

#. 确保连接 NVMe PIP 模块与 Raspberry Pi 5 的 FPC 排线已牢固连接。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. 确认您的 SSD 已正确安装并固定在 NVMe PIP 模块上。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. 检查 NVMe PIP 模块上的指示灯状态：

   * **PWR LED**\ ：应常亮。
   * **STA LED**\ ：应闪烁，表示运行正常。

   .. image:: img/nvme_pip_leds.png

   * 若 **PWR LED** 亮但 **STA LED** 不闪烁，说明 NVMe SSD 未被识别。
   * 若 **PWR LED** 不亮，请短接 ``Force Enable`` 引脚（J4）。

     .. image:: img/nvme_pip_j4.png

#. 确认您的 NVMe SSD 上已正确安装操作系统。

   参见 |link_install_the_os|。

#. 如果 SSD 仍无法启动，请尝试从 Micro SD 卡启动，然后配置 NVMe 启动：

   * |link_configure_boot_ssd|

#. 如果问题仍然存在，请将以下日志文件发送给我们：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_nvme_pip


.. _faq_nvme_link_down_5:

NVMe SSD 被识别但在读写时导致系统重启？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_nvme_link_down

在某些情况下（尤其是 WD Blue SN5000），NVMe SSD 可能被 Raspberry Pi 5 识别，但在读写操作时导致系统重启。这是 SSD 与 Raspberry Pi 5 之间的 PCIe 兼容性/稳定性问题，\ **不是** Pironman 5 的硬件故障。

请尝试以下步骤解决问题：

#. 将 Raspberry Pi 5 引导程序更新到最新版本：

   .. code-block:: shell

      sudo rpi-eeprom-update -a
      sudo reboot

#. 在 ``/boot/firmware/config.txt`` 中添加以下行以强制使用 PCIe Gen3 速度：

   .. code-block:: text

      dtparam=pciex1_gen=3

#. 在内核命令行中添加 ``pcie_aspm=off`` 以禁用 ASPM（主动状态电源管理）。编辑 ``/boot/firmware/cmdline.txt`` 并将其附加到现有行末尾（\ **不要**\ 创建新行）：

   .. code-block:: text

      pcie_aspm=off

   .. note::

      ``pcie_aspm=off`` 通常是关键修复方法——PCIe ASPM 问题在 Raspberry Pi 5 上非常常见，可能导致 NVMe 驱动器在大量 I/O 操作时随机断开或重启系统。

#. 应用以上更改后，重新启动 Raspberry Pi：

   .. code-block:: shell

      sudo reboot

#. 如果问题仍然存在，请重新分区并格式化 NVMe SSD，然后重新安装操作系统。

.. end_faq_nvme_link_down


如何通过命令更改树莓派启动顺序？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_command

如果您已登录树莓派系统，可以通过命令修改启动顺序。

* |link_configure_boot_ssd|

.. end_faq_boot_order_command


如何通过 Raspberry Pi Imager 修改启动顺序？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_imager

除了在 EEPROM 配置中修改 ``BOOT_ORDER``\ ，您还可以使用 Raspberry Pi Imager 更改启动顺序。

* |link_update_bootloader|

.. end_faq_boot_order_imager


如何将系统从 SD 卡复制到 NVMe SSD？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_5`

.. start_faq_copy_sd_to_nvme

如果您没有 NVMe 转 USB 适配器，可以先将系统安装到 Micro SD 卡上，成功启动后，再将系统复制到 NVMe SSD。

* |link_copy_sd_to_nvme|

.. end_faq_copy_sd_to_nvme



6. 高级用法
-------------------------------


如何撕除亚克力板保护膜
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_remove_film

包装内包含两块亚克力板，正反两面均贴有黄色或透明保护膜，用于防止刮花。保护膜可能较难揭除，可使用螺丝刀轻轻刮起角落，再慢慢撕下整张膜。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. end_faq_remove_film
