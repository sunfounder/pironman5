常见问题解答（FAQ）
============================

如何禁用 Web 控制面板？
------------------------------------------

在完成 ``pironman5`` 模块的安装后，您将可以访问 :ref:`max_view_control_dashboard` 页面。

如果您不需要该功能，并希望减少 CPU 与内存占用，可以在安装 ``pironman5`` 时添加 ``--disable-dashboard`` 参数以禁用控制面板。

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

如果您已经安装了 ``pironman5``，可以卸载 ``dashboard`` 模块和 ``influxdb``，并重启 pironman5 服务以应用更改：

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

Pironman 5 是否支持复古游戏系统？
------------------------------------------
支持。但需要注意的是，大多数复古游戏系统是精简版系统，无法安装或运行额外软件。这将导致 Pironman 5 的部分组件（如 OLED 屏幕、RGB 风扇和 4 个 RGB 灯）无法正常工作，因为这些组件依赖于 Pironman 5 的软件包进行驱动。

.. note::

    目前 Batocera.linux 系统已完全兼容 Pironman 5。Batocera.linux 是一个开源且完全免费的复古游戏发行版。

    * :ref:`max_install_batocera`
    * :ref:`max_set_up_batocera`

如何使用 ``pironman5`` 命令控制组件？
------------------------------------------------
您可以参考以下教程，使用 ``pironman5`` 命令控制 Pironman 5 的各个组件：

* :ref:`max_view_control_commands`

如何通过命令更改树莓派的启动顺序？
-----------------------------------------------------
如果您已经登录到树莓派系统，可以使用命令修改启动顺序。详细步骤请参考：


* :ref:`max_configure_boot_ssd`


如何使用 Raspberry Pi Imager 修改启动顺序？
-------------------------------------------------------------
除了在 EEPROM 配置中更改 ``BOOT_ORDER`` 外，还可以使用 **Raspberry Pi Imager** 修改树莓派的启动顺序。

建议您使用备用卡执行此操作。


* :ref:`max_update_bootloader`

如何将系统从 SD 卡复制到 NVMe SSD？
------------------------------------------------------

如果您拥有 NVMe SSD，但没有合适的适配器将其连接到电脑，可以先将系统安装到 Micro SD 卡上。Pironman 5 成功启动后，可将系统从 SD 卡复制到 NVMe SSD。请参阅以下教程：


* :ref:`max_copy_sd_to_nvme_rpi`


OLED 屏幕无法显示？
-----------------------------

如果 OLED 屏幕不显示或显示异常，请尝试以下方法进行排查：

确认 OLED 屏幕的 FPC 排线是否连接牢固。

#. 使用以下命令查看程序日志并排查错误信息：

   .. code-block:: shell

      cat /opt/pironman5/log

#. 或者使用以下命令查看 OLED 的 i2c 地址（0x3C）是否被识别：

   .. code-block:: shell

      sudo i2cdetect -y 1

#. 如果上述操作未发现异常，尝试重启 pironman5 服务：


   .. code-block:: shell

      sudo systemctl restart pironman5.service

.. _max_openssh_powershell:

通过 PowerShell 安装 OpenSSH
---------------------------------------

当您尝试使用 ``ssh <用户名>@<主机名>.local``（或 ``ssh <用户名>@<IP 地址>``）登录树莓派时，若出现以下报错：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


说明您的 Windows 系统版本较老，未预装 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_，请按照以下步骤手动安装：

#. 在 Windows 搜索框中输入 ``powershell``，右键点击 ``Windows PowerShell``，选择“以管理员身份运行”。

   .. image:: img/powershell_ssh.png
      :width: 90%


#. 使用以下命令安装 ``OpenSSH.Client``：

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装完成后，您将看到如下输出：

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用以下命令验证安装状态：

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 如果输出结果为： ``OpenSSH.Client``  则表示已成功安装。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        如果没有上述提示，说明您的 Windows 系统版本过老，建议使用第三方 SSH 工具，如 |link_putty|。

#. 此时请重新启动 PowerShell，并继续以管理员身份运行。您即可使用 ``ssh`` 命令登录树莓派，并输入之前设置的密码。

   .. image:: img/powershell_login.png



如果我安装了 OMV，还能使用 Pironman5 的功能吗？
----------------------------------------------------------------

可以，OpenMediaVault 是基于树莓派系统构建的，您仍然可以按照 :ref:`max_set_up_pi_os` 中的步骤继续进行 Pironman5 的配置。