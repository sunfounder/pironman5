常见问题解答
============

1. 关于兼容系统
------------------

以下系统已通过 Raspberry Pi 5 的兼容性测试：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 关于电源按钮
-------------------

该电源按钮即为 Raspberry Pi 5 的电源按钮，其功能与官方电源按钮完全一致。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **关机**

  * 使用 **Raspberry Pi OS Desktop** 系统时，快速连续按下电源按钮两次即可关机。
  * 使用 **Raspberry Pi OS Lite** 系统时，单击电源按钮即可关机。
  * 长按电源按钮可强制关机。

* **开机**

  * 如果 Raspberry Pi 主板已关闭但仍通电，单击电源按钮可重新开机。

* 如果所使用的系统不支持关机按钮，可长按 5 秒强制关机，之后再单击即可重新开机。

3. 关于 Raspberry Pi AI HAT+
-------------------------------

Raspberry Pi AI HAT+ 不兼容 Pironman 5。

.. image::  img/output3.png
    :width: 400

Raspberry Pi AI 套件由 Raspberry Pi M.2 HAT+ 与 Hailo AI 加速模块组合而成。

.. image::  img/output2.jpg
    :width: 400

你可以将 Hailo AI 加速模块从 AI 套件中拆下，直接插入 Pironman 5 Mini 的 拓展板中。

   .. .. image::  img/output4.png
   ..      :width: 800

4. 关于 Micro HDMI线
-------------------------------------

我们建议使用官方的 Raspberry Pi Micro HDMI 线缆。部分第三方线缆的接口长度小于 65 mm，可能会导致接触不良和显示问题。

  .. image:: img/need_mini_hdmi.png
     :width: 400

5. PI5 无法启动（红灯常亮）？
-------------------------------------------

此问题可能是由于系统更新、启动顺序更改或引导程序损坏导致的。您可以尝试以下步骤来解决该问题：

#. 重新连接电源，并检查 PI5 是否能够正常启动。

#. 恢复引导程序

   * 如果 PI5 仍无法启动，可能是引导程序已损坏。您可以参考此教程：:ref:`update_bootloader_mini`，并选择从 SD 卡或 NVMe/USB 启动。
   * 将准备好的 SD 卡插入 PI5，上电后至少等待 10 秒。恢复完成后，取出并重新格式化 SD 卡。 
   * 然后使用 Raspberry Pi Imager 烧录最新的 Raspberry Pi OS，将卡插回，再尝试启动。

6. RGB 灯不亮？
------------------

#. IO 扩展板上的两个引脚用于通过 GPIO10 驱动 RGB 灯，确保这两个引脚正确插上跳线帽。

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. 确认 Raspberry Pi 正在运行支持的操作系统。Pironman 5 仅支持以下版本：

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   如果你安装的是不支持的系统，请参考教程安装兼容的系统：:ref:`install_the_os_mini`。

#. 运行命令 ``sudo raspi-config`` 打开配置菜单，选择 **3 Interfacing Options** -> **I3 SPI** -> **YES**，点击 **OK** 和 **Finish** 启用 SPI。启用后请重启设备。

如果以上方法无效，请发送邮件至 service@sunfounder.com，我们会尽快回复。

7. CPU 风扇不转？
--------------------

当 CPU 温度未达到设定阈值时，风扇不会运行。

**基于温度的风扇转速控制**

PWM 风扇会根据 Raspberry Pi 5 的温度动态调整转速：

* **低于 50°C**：风扇关闭（0% 转速）  
* **达到 50°C**：风扇低速运行（30% 转速）  
* **达到 60°C**：风扇中速运行（50% 转速）  
* **达到 67.5°C**：风扇高速运行（70% 转速）  
* **75°C 及以上**：风扇全速运行（100% 转速）  

更多详情请参考：:ref:`fan_mini`

8. 如何关闭 Web 控制面板？
----------------------------

安装 ``pironman5`` 模块后，你将能够访问 :ref:`view_control_dashboard_mini`。

如果你不需要该功能并希望减少 CPU 与内存占用，可以在安装 ``pironman5`` 时添加 ``--disable-dashboard`` 参数来禁用面板。

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

如果你已安装 ``pironman5``，可卸载 ``dashboard`` 模块与 ``influxdb``，并重启 pironman5：

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

9. 如何使用 ``pironman5`` 命令控制组件？
--------------------------------------------

可参考以下教程使用 ``pironman5`` 命令控制 Pironman 5 的各组件：

* :ref:`view_control_commands_mini`

10. 如何通过命令修改 Raspberry Pi 的启动顺序？
------------------------------------------------

如果你已登录 Raspberry Pi，可通过命令修改启动顺序。详细说明请见：

* :ref:`configure_boot_ssd_mini`


11. 如何使用 Raspberry Pi Imager 修改启动顺序？
---------------------------------------------------

除了在 EEPROM 中修改 ``BOOT_ORDER``，你也可以使用 **Raspberry Pi Imager** 工具更改启动顺序。

推荐使用一张备用 SD 卡进行此操作：

* :ref:`update_bootloader_mini`

12. 如何将系统从 SD 卡复制到 NVMe SSD？
----------------------------------------

如果你有 NVMe SSD，但没有适配器将其连接到电脑，你可以先将系统安装到 Micro SD 卡中。Pironman 5 启动成功后，再将系统从 SD 卡复制到 NVMe SSD。详见：

* :ref:`copy_sd_to_nvme_mini`

13. 如何撕除亚克力板保护膜？
------------------------------

包装中包含的两块亚克力板，正反两面均贴有黄色或透明保护膜，用于防止运输过程中的刮花。保护膜可能较难撕开，可使用螺丝刀轻轻从边角刮起，再慢慢撕除整块膜。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center



.. _openssh_powershell_mini:

14. 如何通过 PowerShell 安装 OpenSSH？
---------------------------------------

当你使用 ``ssh <用户名>@<主机名>.local``（或 ``ssh <用户名>@<IP地址>``）连接 Raspberry Pi 时，出现如下错误提示：

.. code-block::

    ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
    spelling of the name, or if a path was included, verify that the path is correct and try again.


说明你的电脑系统版本过旧，未预装 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_，需手动安装：

#. 在 Windows 桌面搜索栏中输入 ``powershell``，右键点击 ``Windows PowerShell``，选择“以管理员身份运行”。

   .. image:: img/powershell_ssh.png
      :width: 90%


#. 输入以下命令安装 ``OpenSSH.Client``：

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装完成后，会返回如下内容：

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用下列命令验证安装情况：

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 输出内容表明 ``OpenSSH.Client`` 已成功安装：

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        如果没有出现上述提示，说明 Windows 系统版本太旧，建议安装第三方 SSH 工具，如 |link_putty|。

#. 重启 PowerShell，再次以管理员身份运行。此时即可使用 ``ssh`` 命令连接 Raspberry Pi，系统将提示你输入之前设置的密码。

   .. image:: img/powershell_login.png
