.. _max_install_to_nvme_home_bridge:

在 NVMe SSD 上安装操作系统
============================================

如果您使用的是 NVMe SSD，并且具备用于连接电脑的 NVMe 转接器，可参考以下教程快速完成系统安装。

**所需组件**

* 一台个人电脑
* 一块 NVMe 固态硬盘
* 一个 NVMe 转 USB 适配器
* 一张 Micro SD 卡和读卡器

.. _max_update_bootloader:

1. 更新启动引导程序
----------------------------------

首先，您需要更新树莓派 5 的启动引导程序，使其优先从 NVMe 启动，其次是 USB，然后是 SD 卡。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    此步骤建议使用一张备用的 Micro SD 卡。首先将引导程序写入该卡，然后插入树莓派，即可启用从 NVMe 启动功能。
    
    或者，您也可以将引导程序直接写入 NVMe 设备，再将其插入树莓派以更改启动方式。之后将 NVMe SSD 连接至电脑进行系统安装，安装完成后重新插回树莓派即可。

#. 使用读卡器将备用的 Micro SD 卡或 NVMe SSD 插入电脑或笔记本。

#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，从下拉菜单选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. 在 **Operating System** 选项卡中向下滚动，选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，以启用树莓派 5 从 NVMe 启动，其次尝试 USB，再尝试 SD 卡。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 中选择用于写入的存储设备。

   .. note::

      请务必确认所选设备正确。若连接了多个存储设备，为避免混淆，建议断开其他设备。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 点击 **NEXT**。如果该设备已有数据，请先备份。如无需备份，请点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 很快，您将看到提示，**NVMe/USB Boot** 已成功写入存储设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 现在，将 Micro SD 卡或 NVMe SSD 插入树莓派。使用 Type C 适配器通电后，引导程序将写入树莓派 EEPROM 中。

.. note::

   之后，树莓派将优先从 NVMe 启动，再尝试 USB，最后是 SD 卡。
   
   完成后请断电并移除 Micro SD 卡或 NVMe SSD。


2. 安装操作系统至 NVMe SSD
---------------------------------

现在可以将操作系统写入您的 NVMe SSD。

**步骤**

#. 使用读卡器将 SD 卡插入电脑或笔记本。

#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. 点击 **Operating System** 选项卡。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动至底部，选择所需的操作系统。

   .. note::

      * 对于 **Ubuntu** 系统，请点击 **Other general-purpose OS** -> **Ubuntu**，并选择 **Ubuntu Desktop 24.04 LTS (64 bit)** 或 **Ubuntu Server 24.04 LTS (64 bit)**。
      * 对于 **Kali Linux**、 **Home Assistant** 和 **Homebridge** 系统，请点击 **Other specific-purpose OS**，然后选择相应系统。

   .. image:: img/os_other_os.png
      :width: 90%

#. 在 **Storage** 选项中，选择目标 NVMe 存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**。

   .. note::

      * 对于不支持提前配置的系统，点击 **NEXT** 后会提示是否保留设备数据。如已确认备份，可点击 **Yes**。
      * 对于可配置主机名、WiFi 和 SSH 的系统，将弹出窗口询问是否应用操作系统自定义设置，您可选择 **Yes**、**No**，或返回继续编辑。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置树莓派的 **主机名**，这是其在网络中的唯一标识。可通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问。

     .. image:: img/os_set_hostname.png

   * 创建 **用户名** 和 **密码**，用于管理员账户。设置唯一的凭据是保障系统安全的重要步骤，树莓派默认不带密码。

     .. image:: img/os_set_username.png

   * 配置无线网络，填写您的 **SSID** 和 **密码**。

     .. note::

       请将 ``Wireless LAN country`` 设置为您所在地的两个字母国家代码（参见 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_）。

     .. image:: img/os_set_wifi.png
         
   * 若需远程连接树莓派，请在 Services 标签中启用 SSH。

     * 若使用密码认证，使用 General 标签中设定的用户名和密码。
     * 若使用公钥认证，选择 "Allow public-key authentication only"。若已有 RSA 密钥将自动使用，否则点击 "Run SSH-keygen" 生成新密钥对。

     .. image:: img/os_enable_ssh.png

   * **Options** 菜单可配置 Imager 写入行为，如写入完成时播放提示音、自动弹出存储设备、启用遥测等。

     .. image:: img/os_options.png



#. 完成操作系统配置后，点击 **Save** 保存设置，然后点击 **Yes** 应用并开始写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%

      
#. 若 NVMe SSD 中已有数据，请确保备份后再继续。若无需备份，点击 **Yes**。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当您看到 “Write Successful” 的弹窗提示时，说明镜像已成功写入并验证完毕。现在，您可以使用 NVMe SSD 启动树莓派了！
