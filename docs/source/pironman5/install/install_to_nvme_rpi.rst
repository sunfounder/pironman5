.. _install_to_nvme_rpi:

在 NVMe SSD 上安装操作系统
===================================

如果您正在使用 NVMe SSD，并且配备了适配器将其连接到计算机进行系统安装，可以参考以下教程快速完成安装。

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* 一张 Micro SD 卡和读卡器

.. _update_bootloader_5:

1. 更新启动加载器
--------------------------------

首先，需要将 Raspberry Pi 5 的启动加载器更新为优先从 NVMe 启动，其次尝试 USB，最后为 SD 卡启动。

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    此步骤建议使用一张备用 Micro SD 卡。先将启动加载器写入该 Micro SD 卡，然后立即插入 Raspberry Pi，以启用从 NVMe 启动的功能。
    
    或者，您也可以先将启动加载器写入 NVMe 设备，再插入 Raspberry Pi 以修改启动方式。之后将 NVMe SSD 连接至电脑进行系统安装，完成后再次插入回 Raspberry Pi。

#. 使用读卡器将备用的 Micro SD 卡或 NVMe SSD 插入电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi Device**，从下拉菜单中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 在 **Operating System** 选项卡中向下滚动，选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，使 Raspberry Pi 5 支持优先从 NVMe 启动。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 选项中，选择合适的存储设备进行安装。

   .. note::

      请确保选择正确的存储设备。如同时连接了多个设备，建议断开其他设备以避免混淆。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在可以点击 **NEXT**。如果设备已有数据，请确保已备份，以免数据丢失。如无需备份，点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 稍后系统会提示 **NVMe/USB Boot** 已成功写入您的设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 现在，将 Micro SD 卡或 NVMe SSD 插入 Raspberry Pi。使用 Type-C 电源适配器启动后，启动加载器将被写入 Raspberry Pi 的 EEPROM 中。

.. note::

    之后，Raspberry Pi 将优先从 NVMe 启动，然后是 USB，最后才是 SD 卡。

    关闭电源后，请取出 Micro SD 卡或 NVMe SSD。


2. 安装操作系统到 NVMe SSD
-----------------------------------

现在可以开始将操作系统安装到 NVMe SSD 上。


#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，从下拉列表中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 选择 **Operating System**，并选用推荐的操作系统版本。

   .. image:: img/os_choose_os.png
      :width: 90%


#. 在 **Storage** 选项中，选择目标 NVMe SSD。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**，然后点击 **EDIT SETTINGS** 进入系统设置界面。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置 Raspberry Pi 的 **hostname** （主机名），这是设备在网络中的唯一标识。您可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问该设备。

     .. image:: img/os_set_hostname.png

   * 创建 Raspberry Pi 管理员账户的 **用户名** 和 **密码**。由于系统默认无密码，设置独立账号可有效提升安全性。

     .. image:: img/os_set_username.png

   * 配置无线局域网，填写网络的 **SSID** 和 **密码**。

     .. note::

       请将 ``Wireless LAN country`` 设置为您所在地对应的 `ISO/IEC alpha2 代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png

   * 若需远程连接 Raspberry Pi，请在“服务”选项卡中启用 SSH。

     * 若使用 **密码验证**，则使用“常规”标签页中设置的用户名与密码。
     * 若使用公钥验证，请选择 “Allow public-key authentication only”。如已存在 RSA 密钥将直接使用；如无，点击 “Run SSH-keygen” 生成新密钥对。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 选项中可配置 Imager 的写入行为，如写入完成提示音、弹出设备、启用遥测等功能。

     .. image:: img/os_options.png

#. 完成系统定制设置后，点击 **Save** 保存设置，然后点击 **Yes** 应用设置并写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 如果 NVMe SSD 中已有数据，请确保已备份。如无需备份，点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当弹出 “Write Successful” 提示窗口时，说明镜像已成功写入并验证完毕。现在，您已经可以使用该 NVMe SSD 启动 Raspberry Pi 了！

   .. image:: img/nvme_install_finish.png
      :width: 90%
