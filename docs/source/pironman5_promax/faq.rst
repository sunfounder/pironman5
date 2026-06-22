.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Quick Troubleshooting
-------------------------------

* 电源按钮无法工作 → :ref:`faq_power_button_not_work_promax`
* OLED 屏幕不工作 → :ref:`faq_oled_promax`
* RGB 灯不亮 → :ref:`faq_rgb_promax`
* 风扇不工作 → :ref:`promax_fan_faq`
* 仪表盘不显示数据 → :ref:`faq_dashboard_promax`
* NVMe SSD 无法识别 → :ref:`faq_nvme_promax`
* NVMe SSD 被识别但导致系统重启 → :ref:`faq_nvme_link_down_promax`
* PI5 无法启动 → :ref:`faq_pi5_boot_fail_promax`



1. Hardware
-------------------------------


.. _com_os_promax:

Compatible Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_promax`

Power Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_promax:

Power Button Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Copper Pipe Ends on the Tower Cooler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raspberry Pi AI HAT+ 与 Pironman 5 Pro MAX 不兼容。

.. image:: img/output3.png
    :width: 400

Raspberry Pi AI Kit 由 Raspberry Pi M.2 HAT+ 与 Hailo AI 加速模块组合而成。

.. image:: img/output2.jpg
    :width: 400

你可以将 Hailo AI 加速模块从 Raspberry Pi AI Kit 上拆下，直接插入 Pironman 5 Pro MAX 的 NVMe PIP 模块中使用。


4.3-Inch Screen Is Black / Not Displaying?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.3 英寸 DSI 屏幕即插即用，无需额外安装驱动。

.. note::

   HDMI/USB 板上的 **ON/AUTO** 跳线仅控制扬声器音频输出，\ **不影响**\ 屏幕显示。

如果屏幕黑屏或不显示，请检查以下事项：

#. 确保 DSI 排线已连接到 Raspberry Pi 5 的正确 DSI 端口。

#. 检查排线是否完全插入，卡扣是否压紧，触点方向是否正确。

#. 运行以下命令确认系统是否检测到 DSI 屏幕：

   .. code-block:: shell

      sudo dmesg | grep -i dsi

   如果检测到屏幕，你应该会看到类似 ``DSI display found`` 的输出。如果没有输出，则屏幕未被识别，请重新检查物理连接。


External HDMI Screen — Taskbar Only Appears on the 4.3-Inch Screen?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当你将外部 HDMI 显示器连接到 Pironman 5 Pro MAX 时，桌面任务栏可能仍然停留在内置的 4.3 英寸 DSI 屏幕上，而不是移动到外部显示器上。这是因为系统默认将 DSI 屏幕设置为主显示屏。

如果你希望将 HDMI 显示器设置为主屏幕，请按以下步骤操作：

#. 创建启动脚本：

   .. code-block:: shell

      sudo nano /usr/local/bin/fix-primary-screen.sh

#. 将以下内容添加到脚本中：

   .. code-block:: bash

      #!/bin/bash
      # Check if an external HDMI monitor is connected
      if wlr-randr | grep -q "HDMI-A-1"; then
          # Turn off the DSI screen first
          wlr-randr --output DSI-1 --off
          sleep 2
          # Re-enable DSI and place it to the right of HDMI
          wlr-randr --output DSI-1 --on --right-of HDMI-A-1
      fi

#. 赋予脚本可执行权限：

   .. code-block:: shell

      sudo chmod +x /usr/local/bin/fix-primary-screen.sh

#. 将脚本添加到自动启动。编辑 labwc 自动启动文件：

   .. code-block:: shell

      nano ~/.config/labwc/autostart

   添加以下行（\ ``&`` 表示在后台运行）：

   .. code-block:: text

      /usr/local/bin/fix-primary-screen.sh &


2. Cooling and Fans
-------------------------------


.. _promax_fan_faq:

Fan Not Working / Cannot Be Controlled?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pro MAX 采用官方 Raspberry Pi PWM 风扇控制方案。三个散热风扇均由 Raspberry Pi 系统直接控制，不依赖 pironman5 服务（因此你在命令行工具或仪表盘中不会看到风扇控制选项）。

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


Dashboard Does Not Show Fan Speed?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pro MAX 使用定制的 **5 针** 风扇，引脚定义如下：\ **PWM / 5V / GND / RGB Data In / RGB Data Out**\ 。

这些风扇 **没有** 转速计（速度反馈）引脚，因此系统无法读取实际 RPM。仪表盘不显示风扇速度是正常现象。

风扇速度由 Raspberry Pi 的原生 PWM 温度曲线控制：

* < 50°C：关闭（0%）
* 50°C+：低速（30%）
* 60°C+：中速（50%）
* 67.5°C+：高速（70%）
* 75°C+：全速（100%）



3. OLED and RGB
-------------------------------


.. _faq_oled_promax:

OLED Screen Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`promax_set_up_pi_os`
.. |link_compatible_systems| replace:: :ref:`com_os_promax`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled


.. _faq_customize_oled_promax:

How to Customize the OLED Display?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


.. _faq_rgb_promax:

RGB LEDs Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


How to Wake Up the OLED Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

为了节省电量并延长屏幕寿命，OLED 屏幕在一段时间无操作后会自动关闭。这是正常设计，不会影响设备功能。

.. note::

   如需配置 OLED 屏幕（如开关、休眠时间、旋转等），请参考 :ref:`promax_view_control_dashboard` 或 :ref:`promax_view_control_commands`。



4. Dashboard and Software
-------------------------------


.. _faq_dashboard_promax:

The Dashboard Shows No Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`promax_view_control_dashboard`

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


.. |link_view_control_commands| replace:: :ref:`promax_view_control_commands`

How to Control Components Using the ``pironman5`` Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


.. _faq_piper_tts_32bit_promax:

``pip install piper-tts`` Fails with "Could Not Find a Version"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 Pironman 5 Pro MAX 上安装 ``sunfounder-voice-assistant`` 时，可能会遇到以下错误：

.. code-block:: text

   ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
   ERROR: No matching distribution found for piper-tts==1.3.0

此错误的原因是 ``piper-tts`` 1.3.0 仅提供 **64 位**\ （\ ``aarch64``\ ）的 wheel 包。如果你的 Raspberry Pi 运行的是 **32 位** 操作系统，pip 无法找到兼容的包。

**解决方法：** 安装 64 位版本的 Raspberry Pi OS。

#. 检查当前系统架构：

   .. code-block:: shell

      uname -m

   * ``aarch64`` → 64 位（无问题）
   * ``armv7l`` → 32 位（需要升级）

#. 使用 `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`_ 将 **64 位** Raspberry Pi OS 镜像写入你的存储设备。

#. 安装 64 位操作系统后，重新安装 ``pironman5`` 软件和 ``sunfounder-voice-assistant``\ 。


5. Boot and Storage
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_promax`

.. _faq_pi5_boot_fail_promax:

PI5 Fails to Boot (Red LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail


.. _faq_nvme_promax:

NVMe PIP Module Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_dual| replace:: :ref:`install_the_os_promax`

.. include:: ../pironman5_max/faq.rst
   :start-after: start_faq_nvme_pip_dual
   :end-before: end_faq_nvme_pip_dual

#. 如果线路连接正确且操作系统已安装，但 NVMe SSD 仍无法启动，请尝试使用 Micro SD 卡启动以验证其他组件功能。确认无误后，参考 :ref:`configure_boot_ssd_promax`。

#. 如果完成以上步骤后问题仍然存在，请发送邮件至 service@sunfounder.com。我们会尽快回复。


.. _faq_nvme_link_down_promax:

NVMe SSD Detected but Causes System Restart on Read/Write?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_promax`

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


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_promax`

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


.. _promax_openssh_powershell:

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


If I Set Up OMV, Can I Still Use the Pironman5's Function?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

可以。OpenMediaVault 是在 Raspberry Pi 系统上搭建的服务。请按照 :ref:`promax_set_up_pi_os` 的步骤继续配置，即可正常使用 Pironman5 的功能。


Raspberry Pi Camera Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当摄像头无法正常工作时，90% 的问题都与排线连接或摄像头硬件本身有关。

首先，使用 ``rpicam-hello --list-cameras`` 确认系统是否检测到摄像头。如果检测成功，你应该会看到类似如下的信息：

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

如果未检测到摄像头，请检查排线是否插反或未完全插入。如果问题仍然存在，请尝试更换排线或摄像头模组进行交叉测试。


Can I Install Home Assistant OS on the Pironman 5 Pro MAX?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pironman 5 Pro MAX 没有专用的 Home Assistant 插件。但你可以使用 **Pironman 5 MAX** 的插件代替——请按照 `SunFounder 插件仓库指南 <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5_max/set_up/set_up_home_assistant.html#add-the-sunfounder-add-ons-repository>`_ 操作。

请注意以下限制：

* **4.3 英寸屏幕**\ ：Home Assistant OS 是 **Lite** 系统，没有桌面环境。Pro MAX 内置的 4.3 英寸屏幕将无法显示任何内容。

* **NVMe PIP 双 SSD**\ ：Home Assistant OS 无法读取 Pro MAX 双 NVMe PIP 模块上的两个 NVMe SSD。

* **OLED 屏幕和 RGB LED**\ ：安装插件后这些组件正常工作，无需额外配置。

* **CPU 风扇**\ ：CPU 风扇需要在 Home Assistant OS 下手动配置。将以下内容添加到 ``/boot/firmware/config.txt``\ ：

  .. code-block:: text

     dtparam=cooling_fan=on
     dtparam=fan_temp0=40000
     dtparam=fan_temp0_hyst=10000
     dtparam=fan_temp0_speed=125

  保存并重启后，CPU 风扇将由 Raspberry Pi 系统根据 CPU 温度控制。你也可以通过 ``pinctrl`` 命令手动控制，详见 :ref:`promax_fan_faq`。
