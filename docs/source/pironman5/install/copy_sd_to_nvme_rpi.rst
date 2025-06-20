.. _copy_sd_to_nvme_rpi:

将操作系统从 Micro SD 卡复制到 NVMe 固态硬盘
==================================================================

如果你有 NVMe 固态硬盘但缺少连接电脑的适配器，可以选择以下第三种方法：先将系统安装到 Micro SD 卡中，待 Pironman 5 成功启动后，再将系统从 Micro SD 卡迁移至 NVMe 固态硬盘。

* 首先，你需要完成 :ref:`install_os_sd_rpi`。
* 然后，启动并登录到你的 Raspberry Pi。如果你不清楚如何登录，可以访问树莓派官网：|link_rpi_get_start|。

完成上述步骤后，继续按照以下说明操作。


1. 启用 PCIe
--------------------

默认情况下，PCIe 接口是未启用的。

* 打开 ``/boot/firmware/config.txt`` 文件：

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* 在文件中添加以下行启用 PCIe 外部连接器：

  .. code-block:: shell

    # 启用 PCIe 外部连接器
    dtparam=pciex1

* 你也可以使用更易记的别名 ``dtparam=nvme`` 添加到该文件中：

  .. code-block:: shell

    dtparam=nvme

* 该连接默认支持 Gen 2.0（5 GT/sec）速率。如需强制使用 Gen 3.0（10 GT/sec），可在配置中添加以下内容：

  .. code-block:: shell

    # 强制启用 Gen 3.0 速率
    dtparam=pciex1_gen=3

  .. warning::

    Raspberry Pi 5 并未官方认证支持 Gen 3.0，连接 PCIe 设备时可能存在不稳定情况。

* 按下 ``Ctrl + X``， ``Y``，然后回车保存更改。


2. 在 SSD 上安装操作系统
----------------------------------------

你可以通过两种方式将操作系统安装到 SSD 上：

**将系统从 Micro SD 卡复制到 SSD**

#. 连接显示器或通过 VNC Viewer 远程访问 Raspberry Pi 桌面，点击 **Raspberry Pi 图标** -> **Accessories** -> **SD Card Copier**。

   .. image:: img/ssd_copy.png


#. 确保正确选择 **Copy From** 和 **Copy To** 的设备，请务必不要选错。

   .. image:: img/ssd_copy_from.png

#. 勾选 “NEW Partition UUIDs” 选项，确保系统能正确区分各设备，避免挂载冲突或启动失败。

   .. image:: img/ssd_copy_uuid.png

#. 完成选择后，点击 **Start** 。

   .. image:: img/ssd_copy_click_start.png

#. 系统会提示 SSD 中内容将被清除。请提前备份数据，然后点击 Yes 继续。

   .. image:: img/ssd_copy_erase.png

#. 等待一段时间，系统将完成复制操作。


**使用 Raspberry Pi Imager 安装系统**

如果 Micro SD 卡中已安装桌面系统，可使用烧录工具（如 Raspberry Pi Imager）将系统烧录到 SSD。本例使用 Raspberry Pi OS Bookworm，其他系统可能需要先安装烧录工具。

#. 连接显示器或通过 VNC Viewer 进入树莓派桌面，点击 **Raspberry Pi 图标** -> **Accessories** -> **Imager**。

   .. image:: img/ssd_imager.png


#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi Device**，从下拉菜单中选择 **Raspberry Pi 5**。

   .. image:: img/ssd_pi5.png
      :width: 90%


#. 选择 **Operating System**，并选择推荐的操作系统版本。

   .. image:: img/ssd_os.png
      :width: 90%

#. 在 **Storage** 选项中，选择你插入的 NVMe 固态硬盘。

   .. image:: img/nvme_storage.png
      :width: 90%

#. 点击 **NEXT**，然后点击 **EDIT SETTINGS** 配置操作系统设置。

   .. note::

      如果你的 Raspberry Pi 已连接显示器，可跳过以下设置，点击 “Yes” 开始安装，后续可在设备上手动配置。

   .. image:: img/os_enter_setting.png
      :width: 90%

#. 设置 Raspberry Pi 的 **主机名** （hostname）。

   .. note::

      主机名是树莓派的网络识别名。你可以使用 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问设备。

   .. image:: img/os_set_hostname.png


#. 创建用于管理员账户的 **用户名** 和 **密码**。

   .. note::

      设置唯一的用户名和密码是确保设备安全的关键，系统默认不设置密码。

   .. image:: img/os_set_username.png


#. 配置无线局域网，填写网络的 **SSID** 和 **密码**。

   .. note::

      请将 ``Wireless LAN country`` 设置为你所在地对应的 ISO 两字母国家代码，参考 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

   .. image:: img/os_set_wifi.png

#. 若需远程访问，请在 **Services** 标签中启用 **SSH**。

   * 对于 **密码认证**，请使用 **General** 选项卡中设置的用户名和密码。  
   * 对于公钥认证，请选择 “Allow public-key authentication only”。如果你已有 RSA 密钥，将会自动使用该密钥；如果没有，请点击 “Run SSH-keygen” 生成新的密钥对。

   .. image:: img/os_enable_ssh.png



#. 在 **Options** 菜单中可配置烧录完成后的操作，例如烧录完成播放提示音、弹出设备、开启遥测等。

   .. image:: img/os_options.png

#. 完成操作系统设置后，点击 **Save** 保存设置，然后点击 **Yes** 应用设置并开始写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%

#. 如果 NVMe SSD 中已有数据，请提前备份。如无备份需求，点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%

#. 当弹出 “Write Successful” 提示框时，表示镜像写入并校验完成。你现在可以从 NVMe SSD 启动树莓派了！

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _configure_boot_ssd:

3. 配置从 SSD 启动
---------------------------------------

本节将引导你将树莓派设置为从 NVMe 固态硬盘启动，提供更快的启动速度与更高的系统性能。请按以下步骤操作：

#. 首先，在树莓派上打开终端并运行以下命令进入配置界面：

   .. code-block:: shell

      sudo raspi-config

#. 在 ``raspi-config`` 菜单中，使用方向键选择 **Advanced Options**，按 ``Enter`` 进入高级设置。

   .. image:: img/nvme_open_config.png

#. 在 **Advanced Options** 中选择 **Boot Order**，用于设置启动设备的优先级。

   .. image:: img/nvme_boot_order.png

#. 选择 **NVMe/USB boot**，设置树莓派优先从 NVMe 或 USB 启动设备启动，而不是 SD 卡。

   .. image:: img/nvme_boot_nvme.png

#. 完成设置后，点击 **Finish** 退出配置工具，或使用 **Escape** 键关闭。

   .. image:: img/nvme_boot_ok.png

#. 要使新的启动设置生效，请运行 ``sudo reboot`` 重新启动你的 Raspberry Pi。

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

重启后，Raspberry Pi 将优先尝试从连接的 NVMe 固态硬盘启动，为你的系统带来更高的性能和耐用性。


