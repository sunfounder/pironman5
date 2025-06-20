.. _max_install_to_nvme_ubuntu:

将操作系统安装到 NVMe SSD
============================================

如果您正在使用 NVMe SSD，并且拥有将其连接到计算机的适配器来安装系统，可以参考以下教程快速完成安装。

**所需组件**

* 一台个人电脑
* 一块 NVMe 固态硬盘
* 一只 NVMe 转 USB 的适配器
* 一张 Micro SD 卡及读卡器

.. _max_update_bootloader:

1. 更新启动引导程序
----------------------------------

首先，您需要更新树莓派 5 的启动引导程序，使其在启动时优先从 NVMe 启动，其次才尝试 USB 和 SD 卡。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    此步骤建议使用一张备用的 Micro SD 卡。首先将启动引导程序写入这张 Micro SD 卡，并立即插入树莓派，从而启用 NVMe 启动功能。
    
    另一种方式是将启动引导程序直接写入 NVMe 设备，然后插入树莓派以修改启动方式。之后将 NVMe SSD 连接至电脑安装操作系统，安装完成后再次插入树莓派即可。

#. 将备用 Micro SD 卡或 NVMe SSD 插入电脑或笔记本，使用读卡器连接。

#. 在 |link_rpi_imager| 工具中，点击 **Raspberry Pi Device**，从下拉菜单中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 在 **Operating System** 选项卡中，向下滚动并选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. 选择 **NVMe/USB Boot**，启用树莓派 5 先从 NVMe 启动，然后再尝试 USB 和 SD 卡。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **Storage** 项中选择正确的存储设备进行写入。

   .. note::

      请务必选择正确的存储设备。若连接了多个存储设备，建议断开无关设备以避免混淆。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 点击 **NEXT**。如果该设备已有数据，请确保提前备份。若无需备份，点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 接下来将提示 **NVMe/USB Boot** 已成功写入您的存储设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 现在，将 Micro SD 卡或 NVMe SSD 插入树莓派。使用 Type C 电源适配器通电后，启动引导程序将写入树莓派的 EEPROM 中。

.. note::

    自此以后，树莓派将优先从 NVMe 启动，其次是 USB，最后是 SD 卡。
    
    请断电并移除 Micro SD 卡或 NVMe SSD。


2. 安装操作系统到 NVMe SSD
---------------------------------

现在可以将操作系统安装到您的 NVMe SSD 上。

**步骤**

#. 访问 |link_batocera_download| 页面，选择 **Raspberry Pi 5 B** 并点击下载。

   .. image:: img/batocera_download.png
      :width: 90%


#. 解压下载的文件 ``batocera-xxx-xx-xxxxxxxx.img.gz``。

#. 使用读卡器将 SD 卡插入电脑或笔记本。

#. 在 |link_rpi_imager| 中点击 **Operating System** 标签。

   .. image:: img/os_choose_os.png
      :width: 90%
      
#. 向下滚动到页面底部，选择 **Use Custom**。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. 选择刚才解压的系统镜像文件 ``batocera-xxx-xx-xxxxxxxx.img``，点击 **Open**。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. 在 **Storage** 选项中，选择目标 NVMe 存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. 点击 **NEXT**。如果设备中已有数据，请先备份。若不需要，点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%

      
#. 当出现 "Write Successful" 弹窗时，表示系统镜像已成功写入并验证完毕。现在您可以使用 NVMe SSD 启动树莓派了！
