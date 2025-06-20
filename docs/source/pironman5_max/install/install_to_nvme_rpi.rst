.. _max_install_to_nvme_rpi:

在 NVMe SSD 上安装操作系统
===================================
如果您使用的是 NVMe SSD，并且具备用于将其连接至电脑的转接器，可以按照以下教程快速完成系统安装。

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* 一张 Micro SD 卡和读卡器

.. _max_update_bootloader:

1. 更新启动引导程序
--------------------------------

首先，您需要更新树莓派 5 的启动引导程序，使其在启动时优先尝试 NVMe，其次为 USB，最后才是 SD 卡。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    此步骤建议使用一张备用的 Micro SD 卡。先将引导程序写入该卡，然后立即插入树莓派，以启用从 NVMe 启动的功能。
    
    或者，您也可以先将引导程序写入 NVMe 设备，再将其插入树莓派更改启动方式。随后将 NVMe SSD 连接至电脑安装操作系统，安装完成后再插回树莓派使用。

#. 使用读卡器将备用 Micro SD 卡或 NVMe SSD 插入您的电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device**，在下拉列表中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 在 **Operating System** 选项卡中向下滚动，选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，以启用树莓派 5 优先从 NVMe 启动，然后是 USB，最后是 SD 卡。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 选项中，选择正确的目标存储设备。

   .. note::

      请确认所选设备无误。如连接了多个存储设备，建议暂时断开其他设备以避免混淆。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在点击 **NEXT**。如果目标设备中已有数据，请先做好备份；若无需备份，点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 很快您将看到提示， **NVMe/USB Boot** 已成功写入目标设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 此时可将 Micro SD 卡或 NVMe SSD 插入树莓派。使用 Type-C 电源适配器启动后，引导程序将写入树莓派的 EEPROM。

.. note::

    之后，树莓派将按顺序尝试从 NVMe、USB、SD 卡启动。

    请断电并移除用于写入引导程序的 Micro SD 卡或 NVMe SSD。


2. 安装操作系统至 NVMe SSD
-----------------------------------

现在可以将操作系统安装到您的 NVMe SSD 上。


#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device**，从下拉列表中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 选择 **Operating System**，并选用推荐的操作系统版本。

   .. image:: img/os_choose_os.png
      :width: 90%


#. 在 **Storage** 选项中，选择目标 NVMe SSD。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**，然后点击 **EDIT SETTINGS** 进行操作系统配置。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置树莓派的 **hostname** （主机名）。主机名是设备在网络中的标识，您可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 来访问它。
 
     .. image:: img/os_set_hostname.png
         
   * 创建用于管理员权限的 **Username** 和 **Password**。为设备设置唯一的用户名和密码是确保系统安全的关键步骤，因为树莓派默认没有密码。

     .. image:: img/os_set_username.png
         
   * 配置无线局域网，填写您的 **SSID** （网络名称）和 **Password** （密码）。

     .. note::

       请将 ``Wireless LAN country`` 设置为您所在地区对应的两个字母国家代码（参见 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_）。

     .. image:: img/os_set_wifi.png
         
   * 若希望通过远程方式连接树莓派，可在 Services 标签页中启用 SSH。

     * 对于 **密码认证**，使用前面设置的用户名和密码。
     * 对于公钥认证，选择 "Allow public-key authentication only"。若系统已存在 RSA 密钥将自动使用；若无，可点击 "Run SSH-keygen" 生成新的密钥对。

     .. image:: img/os_enable_ssh.png
         
   * **Options** 菜单中可设置写入行为，如写入完成时播放提示音、写入完成后弹出设备、启用遥测功能等。

     .. image:: img/os_options.png

#. 完成自定义配置后，点击 **Save** 保存设置，然后点击 **Yes** 应用配置并开始写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 若您的 NVMe SSD 中已有数据，请提前做好备份。若无需备份，可点击 **Yes** 继续写入。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当您看到 “Write Successful” 的提示框时，表示镜像已写入并验证成功。现在，您已经可以使用该 NVMe SSD 启动树莓派了！

   .. image:: img/nvme_install_finish.png
      :width: 90%

