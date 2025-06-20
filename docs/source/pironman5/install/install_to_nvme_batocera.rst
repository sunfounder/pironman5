.. _install_to_nvme_ubuntu:

在 NVMe SSD 上安装操作系统
============================================

如果您正在使用 NVMe SSD，并且拥有将其连接到电脑进行系统安装的适配器，可以按照以下教程快速完成安装。

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* 一张 Micro SD 卡及读卡器

.. _update_bootloader:

1. 更新启动加载器
----------------------------------

首先，您需要将 Raspberry Pi 5 的启动加载器更新为支持优先从 NVMe 启动，然后才是 USB 和 SD 卡。

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    推荐使用一张备用的 Micro SD 卡。首先将启动加载器写入该 SD 卡，然后立即插入到 Raspberry Pi 中，以启用从 NVMe 启动的功能。
    
    或者，您也可以先将启动加载器写入 NVMe 设备中，然后插入到 Raspberry Pi 以更改其启动方式。之后再将 NVMe SSD 连接到电脑，安装操作系统，完成后重新插回 Raspberry Pi。

#. 将备用的 Micro SD 卡或 NVMe SSD 使用读卡器插入电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device** 并从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 在 **Operating System** 选项中向下滚动并选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，以便 Raspberry Pi 5 优先从 NVMe 启动，其次是 USB，再然后是 SD 卡。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 选项中选择正确的存储设备用于写入。

   .. note::

      请务必选择正确的存储设备。为避免混淆，如连接了多个存储设备，请断开其他设备。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在可以点击 **NEXT**。如果该设备已有数据，请提前备份，以防数据丢失。如无需备份，点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 稍后系统将提示您已成功将 **NVMe/USB Boot** 写入到您的存储设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 此时您可以将 Micro SD 卡或 NVMe SSD 插入 Raspberry Pi，通电后，启动加载器将从中写入到 Raspberry Pi 的 EEPROM 中。

.. note::

    从此之后，Raspberry Pi 将优先从 NVMe 启动，其次是 USB，最后是 SD 卡。
    
    请断电并移除 Micro SD 卡或 NVMe SSD。


2. 将操作系统安装至 NVMe SSD
---------------------------------

接下来，您可以将操作系统安装到 NVMe SSD。

**操作步骤**

#. 首先，访问 |link_batocera_download| 页面，选择 **Raspberry Pi 5 B** 并点击下载。

   .. image:: img/batocera_download.png
      :width: 90%


#. 解压下载的文件 ``batocera-xxx-xx-xxxxxxxx.img.gz``。

#. 将您的 SD 卡插入电脑或笔记本电脑。

#. 打开 |link_rpi_imager|，点击 **Operating System** 标签。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动至页面底部，选择 **Use Custom**。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. 选择刚刚解压的系统镜像 ``batocera-xxx-xx-xxxxxxxx.img``，然后点击 **Open**。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. 在 **Storage** 选项中选择用于安装的正确存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. 点击 **NEXT**。如存储设备中已有数据，请先备份，以防丢失。确认无误后点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当看到 “Write Successful” 的弹窗时，说明系统镜像已成功写入并验证完毕。现在您可以使用该 NVMe SSD 启动 Raspberry Pi！
