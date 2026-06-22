.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Quick Troubleshooting
-------------------------------

* 电源按钮无法工作 → :ref:`faq_power_button_not_work_mini`
* RGB 灯不亮 → :ref:`faq_rgb_mini`
* CPU 风扇不转 → :ref:`faq_pwm_fan_mini`
* 仪表盘不显示数据 → :ref:`faq_dashboard_mini`
* PI5 无法启动 → :ref:`faq_pi5_boot_fail_mini`



1. Hardware
-------------------------------


.. _com_os_mini:

Compatible Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


Power Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

电源按钮引出的是 Raspberry Pi 5 的电源按钮，其功能与 Raspberry Pi 5 的电源按钮完全一致。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Shutdown**

  * 如果运行 **Raspberry Pi OS Desktop** 系统，可以快速连续按两次电源按钮关机。
  * 如果运行 **Raspberry Pi OS Lite** 系统，按一次电源按钮即可关机。
  * 长按电源按钮可强制关机。

* **Power on**

  * 如果 Raspberry Pi 主板已关机但仍连接电源，按一次即可从关机状态开机。

* 如果你运行的系统不支持关机按钮功能，可长按 5 秒强制关机，之后再按一次即可从关机状态开机。


.. _faq_power_button_not_work_mini:

Power Button Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raspberry Pi AI HAT+ 与 Pironman 5 不兼容。

   .. image::  img/output3.png
        :width: 400

Raspberry Pi AI Kit 由 Raspberry Pi M.2 HAT+ 与 Hailo AI 加速模块组合而成。

   .. image::  img/output2.jpg
        :width: 400

你可以将 Hailo AI 加速模块从 Raspberry Pi AI Kit 上拆下，直接插入 Pironman 5 Mini 的扩展板中使用。


Micro HDMI Cable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们建议使用官方的 Raspberry Pi Micro HDMI 线缆。部分第三方线缆的接口长度小于 65 mm，可能会导致接触不良和显示问题。

.. image:: img/need_mini_hdmi.png
   :width: 400



2. Cooling and Fans
-------------------------------


.. _faq_pwm_fan_mini:

CPU Fan Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan



3. RGB
-------------------------------


.. |link_compatible_systems| replace:: :ref:`com_os_mini`

.. _faq_rgb_mini:

RGB LEDs Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb



4. Dashboard and Software
-------------------------------


.. _faq_dashboard_mini:

The Dashboard Shows No Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_mini`

How to Disable the Web Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


How to Uninstall and Reinstall the Pironman 5 Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


.. |link_view_control_commands| replace:: :ref:`view_control_commands_mini`

How to Control Components Using the ``pironman5`` Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command



5. Boot and Storage
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_mini`

.. _faq_pi5_boot_fail_mini:

PI5 Fails to Boot (Red LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

此问题可能是由于系统更新、启动顺序更改或引导程序损坏导致的。你可以尝试以下步骤来解决该问题：

#. 重新连接电源，检查 PI5 是否能够正常启动。

#. 在机箱外测试 PI5

   * 将 PI5 从 Pironman 5 Mini 机箱中取出。
   * 直接使用电源适配器给 PI5 供电（不安装在机箱内）。
   * 检查是否可以正常启动。

#. 恢复引导程序

   * 如果 PI5 仍无法启动，可能是引导程序已损坏。你可以参考此指南：|link_update_bootloader|，选择从 SD 卡或 NVMe/USB 启动。
   * 将准备好的 SD 卡插入 PI5，通电后至少等待 10 秒。恢复完成后，取出并重新格式化 SD 卡。
   * 然后使用 Raspberry Pi Imager 烧录最新的 Raspberry Pi OS，再尝试启动。


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_mini`

How to Change the Raspberry Pi Boot Order Using Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


How to Modify the Boot Order with Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_mini`

How to Copy the System from the SD Card to an NVMe SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme



6. Advanced Usage
-------------------------------


How to Remove the Protective Film
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film


.. _openssh_powershell_mini:

How to Install OpenSSH via Powershell?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当你使用 ``ssh <username>@<hostname>.local``\ （或 ``ssh <username>@<IP address>``\ ）连接 Raspberry Pi 时，出现以下错误提示：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

说明你的电脑系统版本过旧，未预装 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_，需按照以下教程手动安装。

#. 在 Windows 桌面搜索栏中输入 ``powershell``\ ，右键点击 ``Windows PowerShell``\ ，选择 **Run as administrator（以管理员身份运行）**\ 。

   .. image:: img/powershell_ssh.png
      :width: 90%


#. 使用以下命令安装 ``OpenSSH.Client``\ ：

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装完成后，将返回以下输出：

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用以下命令验证安装：

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 现在提示你 ``OpenSSH.Client`` 已成功安装：

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        如果没有出现上述提示，说明你的 Windows 系统版本仍然过旧，建议安装第三方 SSH 工具，如 |link_putty|。

#. 现在重启 PowerShell，继续以管理员身份运行。此时你将能够使用 ``ssh`` 命令登录 Raspberry Pi，系统将提示你输入之前设置的密码。

   .. image:: img/powershell_login.png
