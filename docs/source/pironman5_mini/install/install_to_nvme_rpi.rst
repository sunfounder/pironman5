.. _install_to_nvme_rpi_mini:

在 NVMe SSD 上安装操作系统
===================================
如果您正在使用 NVMe SSD，并且拥有用于连接该 SSD 至电脑的适配器，那么可以按照下方教程快速安装操作系统。

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* 一张 Micro SD 卡及读卡器

.. _update_bootloader_mini:

1. 更新引导程序
--------------------------------

首先，您需要更新 Raspberry Pi 5 的引导程序，使其启动顺序为先从 NVMe 启动，再尝试 USB，最后是 SD 卡。

.. note::

    在此步骤中，建议使用一张备用 Micro SD 卡。请先将引导程序写入该 Micro SD 卡，然后立即插入 Raspberry Pi，以启用从 NVMe 启动。

    或者，您也可以直接将引导程序写入 NVMe 设备，随后将其插入 Raspberry Pi 更改启动方式。之后再将 NVMe SSD 连接至电脑安装操作系统，安装完成后重新插入 Raspberry Pi 使用。

#. 使用读卡器将备用的 Micro SD 卡或 NVMe SSD 插入电脑或笔记本。

#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，并从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 在 **Operating System** 选项卡中向下滚动，选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，以便 Raspberry Pi 5 先从 NVMe 启动。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 选项中，选择目标存储设备。

   .. note::

      请确保选择正确的设备。如已连接多个存储设备，建议断开其他设备以避免混淆。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 点击 **NEXT**。如果目标设备已有数据，请提前备份。若无需备份，可点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 系统将提示您， **NVMe/USB Boot** 已成功写入目标设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 将 Micro SD 卡或 NVMe SSD 插入 Raspberry Pi，使用 Type C 电源适配器通电后，引导程序将写入至 Raspberry Pi 的 EEPROM。

.. note::

    从此以后，Raspberry Pi 将按照 NVMe → USB → SD 卡 的顺序启动。

    关机后请移除 Micro SD 卡或 NVMe SSD。


2. 安装操作系统至 NVMe SSD
-----------------------------------

现在您可以将操作系统安装到 NVMe SSD 上了。


#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 选择 **Operating System**，并选择推荐的操作系统版本。

   .. image:: img/os_choose_os.png
      :width: 90%


#. 在 **Storage** 中选择目标 NVMe SSD。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**，然后点击 **EDIT SETTINGS** 以定制系统设置。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置您的 Raspberry Pi 的 **hostname**。这是设备在网络中的标识，您可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 进行访问。

     .. image:: img/os_set_hostname.png

   * 创建管理员账户的 **Username** 和 **Password**。Raspberry Pi 默认不设密码，设置唯一账户信息对保障安全至关重要。

     .. image:: img/os_set_username.png

   * 配置无线局域网，输入 Wi-Fi 的 **SSID** 和 **Password**。

     .. note::

          将 ``Wireless LAN country`` 设置为您所在地区对应的两位字母 `ISO/IEC alpha2 代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png

   * 如需远程连接 Raspberry Pi，请在服务页签中启用 SSH。

     * 若使用 **密码认证**，请使用上面设置的用户名和密码。
     * 若使用公钥认证，请选择“仅允许公钥认证”。已有 RSA 密钥将自动使用，若无可点击 “Run SSH-keygen” 生成新密钥对。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 中可设置 Imager 的行为，例如完成后播放提示音、自动弹出介质、启用遥测等。

     .. image:: img/os_options.png

#. 完成操作系统个性化设置后，点击 **Save** 保存设置，再点击 **Yes** 应用设置并写入系统镜像。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 若 NVMe SSD 上已有数据，请提前备份以防数据丢失。确认后点击 **Yes**。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当您看到“Write Successful”提示框时，说明系统镜像已成功写入并验证完成。您现在可以使用该 NVMe SSD 启动 Raspberry Pi！

   .. image:: img/nvme_install_finish.png
      :width: 90%