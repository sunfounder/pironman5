.. _install_to_nvme_home_bridge:

在 NVMe SSD 上安装操作系统
============================================

如果您正在使用 NVMe SSD，并且有适配器可将其连接至电脑进行系统安装，可按照以下教程快速完成操作。

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* 一张 Micro SD 卡及读卡器

1. 更新启动加载器
----------------------------------

首先，需要将 Raspberry Pi 5 的启动加载器更新为优先从 NVMe 启动，其次为 USB，最后为 SD 卡。

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    建议使用一张备用的 Micro SD 卡。首先将启动加载器写入该 SD 卡，然后立即插入 Raspberry Pi，以启用从 NVMe 启动的能力。

    或者，也可以先将启动加载器写入 NVMe 设备，再插入 Raspberry Pi 以切换启动方式。之后，将 NVMe SSD 连接至电脑安装操作系统，完成后再重新插入回 Raspberry Pi。

#. 使用读卡器将备用的 Micro SD 卡或 NVMe SSD 插入电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device**，在下拉列表中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. 在 **Operating System** 标签中向下滚动，选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，使 Raspberry Pi 5 优先从 NVMe 启动。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 中选择正确的存储设备进行写入。

   .. note::

      请确保选择正确的设备。如连接了多个存储设备，建议先断开其他设备以避免混淆。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在点击 **NEXT**。如设备中已有数据，请先备份，以防数据丢失。确认无误后点击 **Yes**。

   .. image:: img/os_continue.png
      :width: 90%


#. 很快将提示您 **NVMe/USB Boot** 已成功写入目标存储设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 接下来，将该 Micro SD 卡或 NVMe SSD 插入 Raspberry Pi。使用 Type-C 电源适配器供电后，启动加载器会自动写入 Raspberry Pi 的 EEPROM。

.. note::

   此后，Raspberry Pi 将优先从 NVMe 启动，其次是 USB，再然后是 SD 卡。

   请断电并取出 Micro SD 卡或 NVMe SSD。


2. 安装操作系统到 NVMe SSD
---------------------------------

现在可以开始将操作系统安装到 NVMe SSD 上。

**步骤**

#. 使用读卡器将您的 SD 卡插入电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi Device**，从下拉列表中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. 点击 **Operating System** 标签。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动页面底部，选择您所需的操作系统。

   .. note::

      * 安装 **Ubuntu** 系统时，请点击 **Other general-purpose OS** -> **Ubuntu**，然后选择 **Ubuntu Desktop 24.04 LTS (64 bit)** 或 **Ubuntu Server 24.04 LTS (64 bit)**。
      * 安装 **Kali Linux**、 **Home Assistant** 或 **Homebridge** 时，请点击 **Other specific-purpose OS**，然后选择相应系统。

   .. image:: img/os_other_os.png
      :width: 90%

#. 在 **Storage** 中选择安装目标 NVMe SSD。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**。

   .. note::

      * 对于不支持预设配置的系统，点击 **NEXT** 后会弹出提示是否保留设备内数据。如已确认备份，请选择 **Yes**。

      * 对于支持配置主机名、WiFi 和启用 SSH 的系统，会弹出提示是否应用自定义设置。可选择 **Yes** 、 **No**，或返回进一步编辑。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置 Raspberry Pi 的 **hostname** （主机名），作为网络识别标识。您可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问设备。

     .. image:: img/os_set_hostname.png

   * 创建 Raspberry Pi 管理员账户的 **用户名** 和 **密码**。建议设置独立账号密码，以保障系统安全。

     .. image:: img/os_set_username.png

   * 配置无线网络，填写您的 **SSID** 和 **密码**。

     .. note::

       将 ``Wireless LAN country`` 设置为您所在地对应的 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png

   * 如需远程连接 Raspberry Pi，请在服务标签页启用 SSH。

     * 选择 **密码验证** 时，将使用常规设置页填写的用户名和密码。
     * 若启用 **仅允许公钥验证**，系统会使用现有 RSA 密钥；如无密钥，可点击 “Run SSH-keygen” 生成新密钥对。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 菜单中，可配置写入完成后的行为，如播放提示音、自动弹出设备、启用遥测等。

     .. image:: img/os_options.png



#. 完成所有设置后，点击 **Save** 保存自定义内容。然后点击 **Yes** 应用这些设置并开始写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 如果 NVMe SSD 中已有数据，请确保已完成备份。如无需备份，点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当弹出 “Write Successful” 提示时，表示系统镜像已成功写入并验证完成。现在，您已准备好通过该 NVMe SSD 启动 Raspberry Pi！
