.. _copy_sd_to_nvme_rpi_mini:

将操作系统从 Micro SD 复制到 NVMe SSD
==================================================================

如果您有 NVMe SSD 但没有适配器将其连接到电脑，可以选择第三种方式：先将系统安装在 Micro SD 卡上，待 Pironman 5 Mini 成功启动后，再将系统从 Micro SD 卡迁移至 NVMe SSD。

* 首先，您需要完成 :ref:`install_os_sd_rpi_mini`。
* 然后启动并登录到 Raspberry Pi。如不确定登录方式，可访问官方 Raspberry Pi 网站：|link_rpi_get_start|。

完成上述步骤后，再继续以下操作。


1. 启用 PCIe
--------------------

默认情况下，PCIe 接口未启用。

* 要启用它，请编辑 ``/boot/firmware/config.txt`` 文件：

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt

* 向文件中添加以下内容：

  .. code-block:: shell
  
    # 启用 PCIe 外部接口
    dtparam=pciex1

* 也可以使用更易记的别名，将 ``dtparam=nvme`` 添加至 ``/boot/firmware/config.txt``：

  .. code-block:: shell
  
    dtparam=nvme

* 默认连接为 Gen 2.0（5 GT/sec），如需强制启用 Gen 3.0（10 GT/sec）可添加如下配置：

  .. code-block:: shell
  
    # 强制使用 Gen 3.0 速率
    dtparam=pciex1_gen=3

  .. warning::

    Raspberry Pi 5 未获得 Gen 3.0 的官方认证，在该速率下可能会出现不稳定的情况。

* 按 ``Ctrl + X``，然后按 ``Y`` 和 ``Enter`` 保存文件。


2. 安装系统至 SSD
----------------------------------------

有两种方式可将操作系统安装到 SSD：

**方式一：从 Micro SD 卡复制系统到 SSD**

#. 连接显示器或使用 VNC Viewer 访问 Raspberry Pi 桌面，点击 **Raspberry Pi 图标** -> **Accessories** -> **SD Card Copier**。

   .. image:: img/ssd_copy.png


#. 正确选择 **Copy From** 和 **Copy To** 设备，请确保不要混淆顺序。

   .. image:: img/ssd_copy_from.png

#. 勾选 “NEW Partition UUIDs”，以确保系统能正确识别设备，避免挂载冲突和启动错误。

   .. image:: img/ssd_copy_uuid.png

#. 选择完成后，点击 **Start**。

   .. image:: img/ssd_copy_click_start.png

#. 系统会提示 SSD 上数据将被清除，请先备份重要数据再点击 Yes。

   .. image:: img/ssd_copy_erase.png

#. 稍等片刻，系统复制完成。

**方式二：使用 Raspberry Pi Imager 安装系统**

如果您的 Micro SD 卡中已安装桌面系统，可通过图像烧录工具（如 Raspberry Pi Imager）将系统直接烧录至 SSD。本示例使用 Raspberry Pi OS Bookworm，其他系统可能需先安装烧录工具。

#. 连接显示器或使用 VNC Viewer 访问 Raspberry Pi 桌面，点击 **Raspberry Pi 图标** -> **Accessories** -> **Imager**。

   .. image:: img/ssd_imager.png


#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，选择 **Raspberry Pi 5** 机型。

   .. image:: img/ssd_pi5.png
      :width: 90%


#. 选择 **Operating System**，并选用推荐的操作系统版本。

   .. image:: img/ssd_os.png
      :width: 90%

#. 在 **Storage** 中选择已插入的 NVMe SSD。

   .. image:: img/nvme_storage.png
      :width: 90%

#. 点击 **NEXT**，然后点击 **EDIT SETTINGS** 自定义操作系统设置。

   .. note::

      如果您已连接显示器，可跳过后续步骤，直接点击“是”开始安装，稍后在桌面系统中再调整设置。

   .. image:: img/os_enter_setting.png
      :width: 90%

#. 设置 Raspberry Pi 的 **主机名**。

   .. note::

      主机名是设备在局域网中的标识，您可通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问它。

   .. image:: img/os_set_hostname.png


#. 创建 Raspberry Pi 管理员账户的 **用户名** 和 **密码**。

   .. note::

      为系统设置唯一的用户名和密码有助于安全防护，默认并未预设密码。

   .. image:: img/os_set_username.png


#. 设置无线网络信息，包括 **SSID** 和 **密码**。

   .. note::

      ``Wireless LAN country`` 需设置为您所在国家的 ISO/IEC Alpha-2 两位字母代码。

   .. image:: img/os_set_wifi.png

#. 如需远程连接，请在 **Services** 标签页中启用 **SSH**。

   * 若使用密码验证，将采用 “General” 中的用户名与密码。
   * 若使用公钥验证，请选择“仅允许公钥认证”。若已有 RSA 密钥将直接使用，否则可点击 “Run SSH-keygen” 生成新密钥对。

   .. image:: img/os_enable_ssh.png



#. 在 **Options** 菜单中可设置写入完成后的行为，例如播放提示音、弹出设备、启用遥测等。

   .. image:: img/os_options.png

#. 完成所有设置后，点击 **Save** 保存自定义配置，再点击 **Yes** 应用设置并开始写入。

   .. image:: img/os_click_yes.png
      :width: 90%

#. 若 SSD 上已有数据，请事先备份。确认无误后点击 **Yes** 开始写入。

   .. image:: img/nvme_erase.png
      :width: 90%

#. 出现 “Write Successful” 弹窗表示写入与校验完成。此时即可使用 NVMe SSD 启动 Raspberry Pi！

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _configure_boot_ssd_mini:

3. 配置从 SSD 启动
---------------------------------------

在本节中，我们将配置 Raspberry Pi 直接从 NVMe SSD 启动，相比 SD 卡能带来更快的启动速度和更稳定的系统性能。

#. 首先打开终端，运行以下命令进入配置界面：

   .. code-block:: shell

      sudo raspi-config

#. 在 ``raspi-config`` 菜单中使用方向键选择 **Advanced Options**，按 ``Enter`` 进入高级设置。

   .. image:: img/nvme_open_config.png

#. 在 **Advanced Options** 中选择 **Boot Order**，以设置系统启动顺序。

   .. image:: img/nvme_boot_order.png

#. 选择 **NVMe/USB boot**，优先从 USB 接口连接的 SSD 或 NVMe 启动，而非 SD 卡。

   .. image:: img/nvme_boot_nvme.png

#. 选择完成后，按 **Finish** 退出 raspi-config。您也可按 ``Esc`` 键返回。

   .. image:: img/nvme_boot_ok.png

#. 要使新的启动设置生效，请通过以下命令重启您的 Raspberry Pi：

   .. code-block:: shell

      sudo reboot

   .. image:: img/nvme_boot_reboot.png

重启后，Raspberry Pi 将尝试从已连接的 NVMe SSD 启动，为系统带来更优的性能与更强的耐用性。
