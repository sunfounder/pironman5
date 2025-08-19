.. note::

    您好，欢迎加入 SunFounder 的 Raspberry Pi、Arduino 和 ESP32 爱好者 Facebook 社区！与其他爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的乐趣。

    **为什么要加入？**

    - **专家支持**：在社区和我们的团队帮助下解决售后问题和技术难题。
    - **学习与分享**：交流技巧与教程，提升您的技能。
    - **新品预览**：抢先了解新产品发布和内部预览。
    - **专属折扣**：享受我们最新产品的专属优惠。
    - **节日活动与赠品**：参与赠品抽奖和节日促销。

    👉 准备好加入我们一起探索与创作了吗？点击 [|link_sf_facebook|] 马上加入！

FAQ
============

如何禁用 Web 控制面板？
------------------------------------------------------

安装 ``pironman5`` 模块后，您将能够访问 :ref:`max_view_control_dashboard`。

如果您不需要此功能并希望减少 CPU 和内存占用，可以在安装 ``pironman5`` 时添加 ``--disable-dashboard`` 参数来禁用控制面板。

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

如果您已经安装了 ``pironman 5``，可以卸载 ``dashboard`` 模块和 ``influxdb``，然后重启 pironman5 以应用更改：

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. Pironman 5 MAX 支持复古游戏系统吗？
.. ------------------------------------------------------
.. 支持。但是，大多数复古游戏系统是精简版，无法安装和运行额外的软件。因此，Pironman 5 MAX 上的某些组件（如 OLED 显示屏、两个 RGB 风扇和四个 RGB LED）可能无法正常工作，因为这些组件依赖于 Pironman 5 MAX 的软件包。

.. .. note::

..     Batocera.linux 系统现已完全兼容 Pironman 5 MAX。Batocera.linux 是一个开源、完全免费的复古游戏发行版。

..     * :ref:`max_install_batocera`
..     * :ref:`max_set_up_batocera`

减少 ``pironman5`` 在 SYSLOG 中的日志输出
-----------------------------------------------
若要减少输出到 SYSLOG 的日志量，可以执行以下步骤：

首先，在 ``influxd`` 中禁用 HTTP 请求日志：

.. code-block:: bash

   sudo nano /etc/influxdb/influxdb.conf

找到 ``http`` 部分，并将 ``log-enabled`` 设置为 ``false``。

.. code-block:: bash
   :emphasize-lines: 22

   ###
   ### [http]
   ###
   ### 控制 HTTP 接口的配置方式。这些是 InfluxDB 数据交互的主要机制。
   ###

   [http]
   # 是否启用 HTTP 接口
   # enabled = true

   # HTTP 服务的绑定地址
   # bind-address = ":8086"

   # 是否启用 HTTP/HTTPS 用户认证
   # auth-enabled = false

   # 基本认证挑战返回的默认领域
   # realm = "InfluxDB"

   # 是否启用 HTTP 请求日志
   log-enabled = false

   # 启用日志时是否抑制写请求日志
   # suppress-write-log = false

   # 启用日志后指定日志路径，默认写入 stderr
   # log entries should be written. If unspecified, the default is to write to stderr, which
   # intermingles HTTP logs with internal InfluxDB logging.

保存文件后，重启 ``influxd`` 服务：

.. code-block:: bash

   sudo systemctl restart influxd.service

然后，将 ``pironman5`` 的日志等级降为 warning：

.. code-block:: bash

   sudo nano /etc/systemd/system/pironman5.service

在 ``Service`` 区段中，将 ``debug-level`` 设置为 ``warning``：

.. code-block:: bash
   :emphasize-lines: 10

   # https://www.freedesktop.org/software/systemd/man/systemd.service.html
   [Unit]
   Description=pironman5 服务
   # 最后启动，避免 GPIO 被占用
   After=multi-user.target

   [Service]
   Type=forking
   # WorkingDirectory=/opt/pironman5
   ExecStart=/usr/local/bin/pironman5 start --background --debug-level=warning
   # ExecStop=/usr/local/bin/pironman5 stop
   # PrivateTmp=False

   [Install]
   WantedBy=multi-user.target

保存后，重新加载 systemd 配置并重启 pironman5 服务：

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl restart pironman5.service

如何使用 ``pironman5`` 命令控制组件
----------------------------------------------------------------------
您可以参考以下教程，使用 ``pironman5`` 命令控制 Pironman 5 MAX 的各个组件：

* :ref:`max_view_control_commands`

如何使用命令修改树莓派的启动顺序？
-------------------------------------------------------------

如果您已登录到树莓派系统，可使用命令修改启动顺序，详见：

* :ref:`max_configure_boot_ssd`

如何使用 Raspberry Pi Imager 修改启动顺序？
---------------------------------------------------------------

除了通过 EEPROM 配置文件中的 ``BOOT_ORDER`` 修改启动顺序，还可以使用 **Raspberry Pi Imager** 来更改树莓派的启动顺序。

建议使用备用 TF 卡进行此操作。

* :ref:`max_update_bootloader`

如何将系统从 SD 卡复制到 NVMe SSD？
-------------------------------------------------------------

如果您有 NVMe SSD 但没有 NVMe 到电脑的转接器，可以先在 Micro SD 卡上安装系统。当 Pironman 5 MAX 成功启动后，可以将系统从 SD 卡复制到 NVMe SSD。详细步骤参见：

* :ref:`max_copy_sd_to_nvme_rpi`

NVMe PIP 模块无法正常工作？
---------------------------------------

1. 请确认 NVMe PIP 模块到树莓派 5 的 FPC 排线连接牢固。  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               您的浏览器不支持 video 标签。
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               您的浏览器不支持 video 标签。
           </video>
       </div>

2. 请确保 SSD 正确安装在 NVMe PIP 模块上。  

3. 检查 NVMe PIP 模块的指示灯状态：

   在确认连接无误后，给 Pironman 5 MAX 供电，观察模块上的两个指示灯：  

   * **PWR LED**：应常亮。  
   * **STA LED**：应闪烁，表示工作正常。  

   .. image:: img/dual_nvme_pip_leds.png  

   * 如果 **PWR LED** 亮但 **STA LED** 不闪，说明树莓派未识别到 NVMe SSD。  
   * 如果 **PWR LED** 不亮，请短接模块上的 “Force Enable” 引脚；若此时亮起，可能是排线松动或系统配置不支持 NVMe。

   .. image:: img/dual_nvme_pip_j4.png  

4. 请确认您的 NVMe SSD 上已正确安装操作系统，参考：:ref:`max_install_the_os`。

5. 如果接线与系统均无问题但仍无法启动，请尝试从 Micro SD 卡启动系统确认其他部件功能，再参考：:ref:`max_configure_boot_ssd` 进行配置。

若尝试上述操作仍无法解决，请发送邮件至 service@sunfounder.com，我们会尽快为您回复。

OLED 屏幕不工作？
--------------------------

.. note:: OLED 屏幕可能因节能而在一段时间后自动关闭。您可以轻轻敲击机壳以触发震动传感器唤醒屏幕。

如果 OLED 屏幕无显示或显示异常，请按以下步骤排查：

1. **检查 OLED 屏幕连接**

   确保 OLED 屏幕的 FPC 排线连接正确。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Oled-11.mp4" type="video/mp4">
               您的浏览器不支持 video 标签。
           </video>
       </div>

2. **检查操作系统兼容性**

   请确认您的树莓派运行的是兼容的操作系统。

3. **检查 I2C 地址**

   运行以下命令查看 OLED 的 I2C 地址（0x3C）是否被识别：

   .. code-block:: shell

      sudo i2cdetect -y 1

   若未识别，请启用 I2C：

   .. code-block:: shell

      sudo raspi-config

4. **重启 pironman5 服务**

   重启 pironman5 服务以尝试解决问题：

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **查看日志文件**

   如果问题仍然存在，可查看日志文件，并将错误信息提供给客服协助分析：

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log

.. _max_openssh_powershell:

使用 PowerShell 安装 OpenSSH
-----------------------------------

当你使用 ``ssh <username>@<hostname>.local``（或 ``ssh <username>@<IP address>``）连接树莓派时，若出现如下错误信息：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

这意味着你的 Windows 系统版本过旧，未预装 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_，请按照以下步骤手动安装：

#. 在 Windows 桌面搜索框中输入 ``powershell``，右键点击 ``Windows PowerShell``，选择“以管理员身份运行”。

   .. image:: img/powershell_ssh.png
      :width: 90%

#. 输入以下命令安装 ``OpenSSH.Client``：

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装完成后会返回如下信息：

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用下列命令确认是否安装成功：

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 若成功，将看到类似以下信息：

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 

        如果未出现上述提示，说明系统版本仍不兼容，建议使用第三方 SSH 工具，如 |link_putty|。

#. 重启 PowerShell 并继续以管理员身份运行，此时即可使用 ``ssh`` 命令登录树莓派，系统将提示你输入之前设置的密码。

   .. image:: img/powershell_login.png

如果我安装了 OMV，还能使用 Pironman5 的功能吗？
--------------------------------------------------------------------------------------------------------

可以，OpenMediaVault 是在树莓派操作系统基础上进行安装的。请继续按照 :ref:`max_set_up_pi_os` 步骤进行配置。
