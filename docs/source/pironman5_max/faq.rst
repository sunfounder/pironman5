
FAQ
============

1. 关于兼容系统
-------------------------------

以下系统已在 Raspberry Pi 5 上通过测试：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 关于电源按钮
--------------------------

该电源按钮直接引出 Raspberry Pi 5 的电源按钮，功能与 Raspberry Pi 5 的电源按钮完全一致。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **关机**

  * 如果运行 **Raspberry Pi OS Desktop** 系统，可以快速按两次电源按钮来关机。 
  * 如果运行 **Raspberry Pi OS Lite** 系统，单击一次电源按钮即可关机。
  * 长按电源键可强制关机。

* **开机**

  * 如果树莓派已关机但仍有电源，单击一次电源按钮即可开机。

* 如果运行的系统不支持关机按钮，可以长按 5 秒来强制关机，再单击一次开机。

3. 关于 Raspberry Pi AI HAT+
----------------------------------------------------------

Raspberry Pi AI HAT+ 不兼容 Pironman 5。

   .. image::  img/output3.png
        :width: 400

Raspberry Pi AI Kit 由 Raspberry Pi M.2 HAT+ 和 Hailo AI 加速模块组成。

   .. image::  img/output2.jpg
        :width: 400

你可以将 Hailo AI 加速模块从 Raspberry Pi AI Kit 中拆下，直接插入 Pironman 5 MAX 的 NVMe PIP 模块。

   .. .. image::  img/output4.png
   ..      :width: 800

4. 关于塔式散热器的铜管端部
----------------------------------------------------------

塔式散热器顶部的 U 型热管经过压缩处理，以便铜管能够穿过铝散热片，这是铜管生产工艺中的正常步骤。

   .. image::  img/tower_cooler1.png

5. PI5 无法启动（红灯常亮）？
-------------------------------------------

此问题可能由系统更新、启动顺序更改或引导程序损坏导致。你可以尝试以下方法来解决：

#. 检查 USB-HDMI 适配器连接

   * 请仔细检查 USB-HDMI 适配器是否牢固连接到 PI5。
   * 尝试拔下并重新插入 USB-HDMI 适配器。
   * 然后重新连接电源，检查是否能正常启动。

#. 在机箱外测试 PI5

   * 如果重新插拔适配器仍未解决问题：
   * 将 PI5 从 Pironman 5 机箱中取出。
   * 使用电源适配器直接为 PI5 供电（不通过机箱）。
   * 检查是否能正常启动。

#. 恢复引导程序

   * 如果 PI5 仍然无法启动，可能是引导程序已损坏。你可以参考此教程：:ref:`update_bootloader_max` 并选择从 SD 卡或 NVMe/USB 启动。
   * 将准备好的 SD 卡插入 PI5，上电后至少等待 10 秒。恢复完成后，取出并格式化 SD 卡。 
   * 然后使用 Raspberry Pi Imager 烧录最新的 Raspberry Pi OS，将卡插回并再次尝试启动。

6. OLED 屏幕无显示？
------------------------------

.. note:: OLED 屏幕可能在一段时间无操作后自动关闭以节省电源。你可以轻敲机箱触发振动传感器唤醒屏幕。

如果 OLED 屏幕未显示或显示异常，请按以下步骤排查：

1. **检查 OLED 屏幕连接**

   确认 OLED 屏幕的 FPC 排线正确连接。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Oled-11.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

2. **检查操作系统兼容性**

   确保运行在树莓派上的系统是兼容的。

3. **检查 I2C 地址**

   运行以下命令检查 OLED 的 I2C 地址 (0x3C) 是否被识别：

   .. code-block:: shell

      sudo i2cdetect -y 1

   如果未检测到，请使用以下命令启用 I2C：

   .. code-block:: shell

      sudo raspi-config

4. **重启 pironman5 服务**

   重启 `pironman5` 服务，查看问题是否解决：

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **检查日志文件**

   如果问题依旧，查看日志文件并将错误信息提供给技术支持：

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log

7. NVMe PIP 模块无响应？
---------------------------------------

1. 确认 NVMe PIP 模块与 Raspberry Pi 5 的 FPC 线牢固连接。  

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

2. 确认 SSD 已牢固安装在 NVMe PIP 模块上。  

3. 检查 NVMe PIP 模块 LED 状态：  

   通电后观察模块上的两个指示灯：  

   * **PWR LED**: 应常亮。  
   * **STA LED**: 应闪烁，表示正常工作。  

   .. image:: img/dual_nvme_pip_leds.png  

   * 如果 **PWR LED** 亮但 **STA LED** 不闪烁，表示 NVMe SSD 未被识别。  
   * 如果 **PWR LED** 不亮，可以短接模块上的 “Force Enable” 引脚。若此时亮起，可能是 FPC 线松动或系统不支持 NVMe。  

   .. image:: img/dual_nvme_pip_j4.png  

4. 确认 NVMe SSD 已安装可启动的操作系统，参考：:ref:`max_install_the_os`。  

5. 如果接线和系统都正确，但 NVMe SSD 仍无法启动，可先用 Micro SD 卡启动验证其他组件，再参考 :ref:`max_configure_boot_ssd` 配置 NVMe 启动。  

如果完成以上操作后问题依旧，请发送邮件至 service@sunfounder.com，我们会尽快回复。  

8. RGB LED 无法工作？
--------------------------

#. IO 扩展板上 J9 之上的两个引脚用于将 RGB LED 连接到 GPIO10，请确保跳帽正确插好。  

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. 确认树莓派运行的是兼容系统，Pironman 5 仅支持以下系统：  

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   如果已安装不兼容系统，请参考教程安装兼容系统：:ref:`install_the_os`。  

#. 运行命令 ``sudo raspi-config`` 打开配置菜单。进入 **3 Interfacing Options** -> **I3 SPI** -> **YES**，然后选择 **OK** 和 **Finish** 启用 SPI。启用后重启 Pironman 5。  

如果以上操作后问题仍未解决，请发送邮件至 service@sunfounder.com，我们会尽快回复。  

9. CPU 风扇不工作？
----------------------------------------------

当 CPU 温度未达到设定阈值时，风扇不会转动。  

**PWM 风扇温控逻辑**  

* **低于 50°C**: 风扇关闭（0% 转速）。  
* **50°C**: 风扇低速运行（30%）。  
* **60°C**: 风扇中速运行（50%）。  
* **67.5°C**: 风扇高速运行（70%）。  
* **75°C 及以上**: 风扇全速运行（100%）。  

更多详情请参考 :ref:`fan`  

10. 如何唤醒 OLED 屏幕？
---------------------------------------------------------------------------------

OLED 屏幕会在一段时间无操作后自动关闭以节能并延长寿命，这是正常设计，不影响功能。  

你可以轻敲机箱，触发振动传感器唤醒屏幕。  

.. note::

   有关 OLED 屏幕的配置（开/关、休眠时间、旋转等），请参考 :ref:`max_view_control_dashboard` 或 :ref:`max_view_control_commands`。  

11. 如何禁用 Web Dashboard？
------------------------------------------------------

在完成 ``pironman5`` 模块的安装后，你可以访问 :ref:`max_view_control_dashboard`。
      
如果你不需要此功能并希望降低 CPU 与内存占用，可以在安装 ``pironman5`` 时添加 ``--disable-dashboard`` 参数来禁用仪表盘。
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
如果你已经安装了 ``pironman5``，可以卸载 ``dashboard`` 模块和 ``influxdb``，然后重启 pironman5 使更改生效：
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. Pironman 5 MAX 是否支持复古游戏系统？
.. ------------------------------------------------------
.. 支持。但大多数复古游戏系统为精简版，无法安装并运行额外软件。这会导致 Pironman 5 MAX 的部分组件（如 OLED 屏、两枚 RGB 风扇和 4 颗 RGB LED）无法正常工作，因为这些组件需要安装 Pironman 5 MAX 的软件包。

.. .. note::

..     Batocera.linux 现已与 Pironman 5 MAX 完全兼容。Batocera.linux 是一款开源且完全免费的复古游戏发行版。

..     * :ref:`max_install_batocera`
..     * :ref:`max_set_up_batocera`

12. 如何使用 ``pironman5`` 命令控制组件
----------------------------------------------------------------------

你可以参考以下教程，使用 ``pironman5`` 命令控制 Pironman 5 MAX 的各个组件。

* :ref:`max_view_control_commands`

13. 如何通过命令修改树莓派的启动顺序
-------------------------------------------------------------

如果你已经登录到树莓派，可以通过命令修改启动顺序。详细步骤如下：

* :ref:`max_configure_boot_ssd`

14. 如何用 Raspberry Pi Imager 修改启动顺序？
---------------------------------------------------------------

除了在 EEPROM 配置中修改 ``BOOT_ORDER`` 外，你也可以使用 **Raspberry Pi Imager** 更改树莓派的启动顺序。

建议使用一张备用的 Micro SD 卡来进行此步骤。

* :ref:`update_bootloader_max`

15. 如何将系统从 SD 卡复制到 NVMe SSD？
-------------------------------------------------------------

如果你有 NVMe SSD，但没有转接器把 NVMe 连接到电脑，你可以先把系统安装在 Micro SD 卡上。待 Pironman 5 MAX 成功启动后，再将系统从 Micro SD 卡复制到 NVMe SSD。详细步骤如下：

* :ref:`max_copy_sd_to_nvme_rpi`

16. 如何撕下亚克力板的保护膜
-----------------------------------------------------------------

包装内包含两块亚克力板，正反两面都贴有黄色/透明保护膜以防刮花。保护膜可能较难撕下，可用螺丝刀轻轻从边角挑起，然后缓慢将整张膜撕下。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _max_openssh_powershell:

17. 如何通过 PowerShell 安装 OpenSSH？
--------------------------------------------------

当你使用 ``ssh <username>@<hostname>.local``（或 ``ssh <username>@<IP address>``）连接树莓派时，若出现如下错误：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

这表示你的电脑系统较旧，未预装 `OpenSSH <https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_。请按以下步骤手动安装：

#. 在 Windows 桌面搜索框输入 ``powershell``，右键点击 ``Windows PowerShell``，选择 **以管理员身份运行**。

   .. image:: img/powershell_ssh.png
      :width: 90%

#. 使用以下命令安装 ``OpenSSH.Client``：

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装完成后将看到如下输出：

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用以下命令验证安装结果：

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 若看到如下信息，表示 ``OpenSSH.Client`` 已成功安装：

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 

        如果没有出现上述提示，说明你的 Windows 系统版本仍然过旧，建议安装第三方 SSH 工具，例如 |link_putty|。

#. 现在重启 PowerShell，并继续以管理员身份运行。此时即可使用 ``ssh`` 命令登录树莓派，系统会提示输入先前设置的密码。

   .. image:: img/powershell_login.png

18. 我安装了 OMV，还能使用 Pironman5 的功能吗？
--------------------------------------------------------------------------------------------------------

可以。OpenMediaVault 是在树莓派系统上进行的设置。请继续按照 :ref:`max_set_up_pi_os` 的步骤完成配置。
