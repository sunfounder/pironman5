.. _install_to_nvme_home_bridge_mini:

在 NVMe SSD 上安装操作系统
============================================

如果您使用的是 NVMe SSD，并配有适配器可将其连接至电脑进行系统安装，可按照以下教程快速完成安装。

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* 一张 Micro SD 卡及读卡器

.. _update_bootloader_mini:

1. 更新启动引导程序
----------------------------------

首先，您需要更新 Raspberry Pi 5 的引导程序，使其在启动时优先从 NVMe 启动，其次是 USB，最后是 SD 卡。

.. note::

    在此步骤中，建议使用一张备用的 Micro SD 卡。请先将引导程序写入该 Micro SD 卡，然后立即插入 Raspberry Pi 中，以启用 NVMe 启动功能。

    或者，您也可以直接将引导程序写入 NVMe 设备，然后插入 Raspberry Pi 修改启动方式。之后再将 NVMe SSD 连接到电脑安装系统，安装完成后重新插入 Raspberry Pi 使用。

#. 通过读卡器将备用的 Micro SD 卡或 NVMe SSD 插入电脑或笔记本。

#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，从下拉菜单中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. 在 **Operating System** 选项卡中，向下滚动并选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，以启用 Raspberry Pi 5 从 NVMe 启动。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 选项中，选择要写入的存储设备。

   .. note::

      请确保选择正确的存储设备。如已连接多个设备，为避免混淆，建议断开其他存储设备。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 点击 **NEXT**。如果设备中已有数据，请务必提前备份。若无需备份，点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 不久后，您将看到提示，说明 **NVMe/USB Boot** 已成功写入目标设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 现在，您可以将 Micro SD 卡或 NVMe SSD 插入 Raspberry Pi。通电后，引导程序将写入 Raspberry Pi 的 EEPROM 中。

.. note::

    此后，Raspberry Pi 将按 NVMe → USB → SD 卡的顺序启动。

    关闭电源并移除 Micro SD 卡或 NVMe SSD。


2. 安装操作系统到 NVMe SSD
---------------------------------

现在您可以开始在 NVMe SSD 上安装操作系统。

**步骤**

#. 使用读卡器将 SD 卡插入电脑或笔记本。

#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，并选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. 点击 **Operating System** 选项卡。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动至页面底部，选择目标操作系统。

   .. note::

      * 对于 **Ubuntu** 系统，请点击 **Other general-purpose OS** -> **Ubuntu**，并选择 **Ubuntu Desktop 24.04 LTS (64 bit)** 或 **Ubuntu Server 24.04 LTS (64 bit)**。
      * 对于 **Kali Linux**、**Home Assistant** 或 **Homebridge**，请点击 **Other specific-purpose OS**，然后选择相应系统。

   .. image:: img/os_other_os.png
      :width: 90%

#. 在 **Storage** 选项中选择正确的目标存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**。

   .. note::

      * 对于无法预设配置的系统，点击 **NEXT** 后会提示是否保留设备中的数据。如已完成备份，请选择 **Yes**。

      * 对于支持预设主机名、WiFi、启用 SSH 等配置的系统，将弹出提示是否应用这些自定义设置。您可选择 **Yes** 或 **No**，也可返回进行修改。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置 **hostname**。主机名是 Raspberry Pi 的网络标识，您可通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问设备。

     .. image:: img/os_set_hostname.png

   * 创建 **Username** 和 **Password**。为确保设备安全，建议设置唯一的用户名和密码，因为系统默认不包含密码。

     .. image:: img/os_set_username.png

   * 配置无线局域网，填写您的网络 **SSID** 和 **Password**。

     .. note::

       请将 ``Wireless LAN country`` 设置为您所在地区的 `ISO/IEC alpha2 两字母国家代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png

   * 若需远程连接 Raspberry Pi，请在服务选项中启用 SSH。

     * 若使用 **密码认证**，请使用“常规”选项卡中设置的用户名与密码。
     * 若使用公钥认证，请选择“仅允许公钥认证”。如已有 RSA 密钥，将直接使用；若没有，可点击“Run SSH-keygen”生成新密钥对。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 菜单中，您可以设置 Imager 的写入行为，例如写入完成后播放提示音、自动弹出设备、启用遥测等。

     .. image:: img/os_options.png



#. 完成所有操作系统自定义设置后，点击 **Save** 保存设置，再点击 **Yes** 应用设置并开始写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 如果 NVMe SSD 中已有数据，请确保提前备份，以防数据丢失。若无需备份，点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当出现 “Write Successful” 提示框时，说明系统镜像已完整写入并验证成功。您现在可以使用 NVMe SSD 启动 Raspberry Pi！
