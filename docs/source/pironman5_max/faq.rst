.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


快速故障排除
-------------------------------

* OLED 屏幕不工作 → :ref:`faq_oled_max`
* RGB 灯不工作 → :ref:`faq_rgb_max`
* GPIO 风扇不工作 → :ref:`faq_gpio_fans_max`
* CPU 风扇不转 → :ref:`faq_pwm_fan_max`
* 仪表盘不显示数据 → :ref:`faq_dashboard_max`
* NVMe SSD 无法识别 → :ref:`faq_nvme_max`



1. 硬件
-------------------------------


.. _com_os_max:

兼容系统
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


电源按钮
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


塔式散热器铜管尾端
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_ai_hat
   :end-before: end_faq_ai_hat


我能否使用 Pironman5 Max 的振动开关功能？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从 v1.3.6 版本开始，OLED 唤醒功能使用电源按键。您必须移除振动开关跳线，以避免占用 Raspberry Pi GPIO 引脚并防止潜在的冲突。请检查是否存在此跳线；如果没有，请忽略本通知。

.. image:: /pironman5_max/img/remove_vib_jumper.jpg


2. 散热与风扇
-------------------------------

.. _faq_pwm_fan_max:

CPU 风扇不工作？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


.. _faq_gpio_fans_max:

GPIO 风扇不工作？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_gpio_fans
   :end-before: end_faq_gpio_fans


3. OLED 与 RGB
-------------------------------


.. _faq_oled_max:

OLED 屏幕无显示？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_compatible_systems| replace:: :ref:`com_os_max`
.. |link_set_up_pironman5| replace:: :ref:`max_set_up_pironman5`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled

.. _faq_rgb_max:

RGB LED 无法工作？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


.. _faq_customize_oled_max:

如何自定义 OLED 显示？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


4. 仪表盘与软件
-------------------------------


.. _faq_dashboard_max:

仪表盘不显示数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


如何禁用 Web Dashboard？
------------------------------------------------------

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


如何卸载并重新安装 Pironman 5 软件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


如何使用 ``pironman5`` 命令控制组件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`max_view_control_commands`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


5. 启动与存储
-------------------------------

如果我设置了 OMV，还能使用 Pironman5 的功能吗？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

可以。OpenMediaVault 是在树莓派系统上进行的设置。请继续按照 :ref:`set_up_os_max` 的步骤完成配置。


PI5 无法启动（红灯常亮）？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail

.. _faq_nvme_max:

NVMe PIP 模块无响应？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. 确认 NVMe PIP 模块与 Raspberry Pi 5 的 FPC 线牢固连接。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. 确认 SSD 已牢固安装在 NVMe PIP 模块上。

#. 检查 NVMe PIP 模块 LED 状态：

   通电后观察模块上的两个指示灯：

   * **PWR LED**：应常亮。
   * **STA LED**：应闪烁，表示正常工作。

   .. image:: img/dual_nvme_pip_leds.png

   * 如果 **PWR LED** 亮但 **STA LED** 不闪烁，表示 NVMe SSD 未被识别。
   * 如果 **PWR LED** 不亮，可以短接模块上的 "Force Enable" 引脚。若此时亮起，可能是 FPC 线松动或系统不支持 NVMe。

   .. image:: img/dual_nvme_pip_j4.png

#. 确认 NVMe SSD 已安装可启动的操作系统，参考：:ref:`install_the_os_max`。

#. 如果问题仍然存在，请将以下日志文件发送给我们：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log


如何通过命令修改树莓派的启动顺序
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


如何用 Raspberry Pi Imager 修改启动顺序？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


如何将系统从 SD 卡复制到 NVMe SSD？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme


6. 高级用法
-------------------------------

如何撕下亚克力板的保护膜
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film
