.. _install_to_nvme_ubuntu_mini:

在 NVMe SSD 上安装操作系统
============================================

如果您使用的是 NVMe SSD，并且拥有将其连接到电脑进行系统安装的适配器，可以按照以下教程快速完成安装。

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一只 NVMe 转 USB 的适配器
* 一张 Micro SD 卡及读卡器

.. _update_bootloader_mini:

1. 更新启动引导程序
----------------------------------

在尝试从 NVMe 启动前，首先需要更新 Raspberry Pi 5 的引导程序，使其能够优先从 NVMe 启动，其次是 USB，然后才是 SD 卡。

.. note::

    本步骤推荐使用一张备用的 Micro SD 卡。您需要先将引导程序写入该 Micro SD 卡，并立即插入到 Raspberry Pi 中，以启用从 NVMe 设备启动的功能。

    或者，您也可以直接将引导程序写入 NVMe 设备，再插入 Raspberry Pi 以更改启动方式。随后将 NVMe SSD 连接到电脑，安装操作系统，安装完成后再插回 Raspberry Pi 使用。

#. 使用读卡器将备用 Micro SD 卡或 NVMe SSD 插入您的电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi Device**，从下拉菜单中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 在 **Operating System** 选项卡中，向下滚动并选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，以启用 Raspberry Pi 5 优先从 NVMe 启动。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 选项中，选择正确的目标存储设备。

   .. note::

      请务必选择正确的设备。如连接了多个存储设备，为避免混淆，请断开不必要的设备。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在点击 **NEXT**。如该设备已有数据，请提前备份。若无备份需求，点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 稍等片刻，提示 **NVMe/USB Boot** 已写入完成。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 现在，您可以将 Micro SD 卡或 NVMe SSD 插入 Raspberry Pi。接通 Type-C 电源后，引导程序将写入 Raspberry Pi 的 EEPROM 中。

.. note::

    此后，Raspberry Pi 将按 NVMe → USB → SD 的顺序启动。

    请关闭电源并移除 Micro SD 卡或 NVMe SSD。


2. 安装操作系统到 NVMe SSD
---------------------------------

现在您可以将操作系统安装到 NVMe SSD 上。

**操作步骤**

#. 首先访问 |link_batocera_download| 页面，选择 **Raspberry Pi 5 B**，点击下载。

   .. image:: img/batocera_download.png
      :width: 90%


#. 解压下载的文件 ``batocera-xxx-xx-xxxxxxxx.img.gz``。


#. 使用读卡器将 SD 卡插入您的电脑或笔记本。

#. 在 |link_rpi_imager| 中点击 **Operating System** 选项卡。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 滚动至页面底部，选择 **Use Custom**。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. 选择刚刚解压出的系统镜像文件 ``batocera-xxx-xx-xxxxxxxx.img``，然后点击 **Open**。


   .. image:: img/batocera_os_choose.png
      :width: 90%


#. 在 **Storage** 选项中选择正确的目标存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. 点击 **NEXT**。如设备已有数据，请提前备份。若无备份需求，点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 出现 "Write Successful" 提示时，说明系统镜像已成功写入并验证完毕。您现在可以从 NVMe SSD 启动 Raspberry Pi 了！
