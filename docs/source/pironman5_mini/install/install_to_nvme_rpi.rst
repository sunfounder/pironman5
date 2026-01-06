.. _install_to_nvme_mini:

在 NVMe SSD 上安装操作系统
===================================

如果你使用的是 NVMe SSD，并且有可将 NVMe SSD 连接到电脑进行系统安装的转接器，可以按照以下教程快速完成安装。

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 转接器
* Micro SD 卡及读卡器


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_mini:


2. 更新引导程序（Bootloader）
--------------------------------

首先，需要更新 Raspberry Pi 5 的引导程序，使其启动顺序优先为 **NVMe**，然后是 **USB**，最后才是 **SD 卡**。

.. note::

    建议在此步骤中使用一张 **备用的 Micro SD 卡**。
    
    - 方法一（推荐）：将引导程序写入一张 Micro SD 卡，插入 Raspberry Pi 并启动一次以应用设置。
    - 方法二：直接将引导程序写入 NVMe SSD。随后将 NVMe SSD 连接到电脑安装操作系统，最后再将其装回 Raspberry Pi。

#. 使用读卡器或转接器，将备用的 **Micro SD 卡或 NVMe SSD** 插入电脑。

#. 打开 Raspberry Pi Imager 后，你会看到 **Device** 页面。从列表中选择你的 Raspberry Pi 5 型号。

   .. image:: img/imager_device.png
      :width: 90%

#. 点击 **OS**。

   * 向下滚动并选择 **Misc utility images**。

     .. image:: img/nvme_misc.png
        :width: 90%

   * 选择 **Bootloader (Pi 5 family)**。

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * 选择 **NVMe/USB Boot** 以设置启动顺序，然后点击 **NEXT**。

     .. image:: img/nvme_boot.png
        :width: 90%


#. 在 **Storage** 中，选择正确的 Micro SD 卡或 NVMe SSD，然后点击 **NEXT**。

   .. note::

      请确认选择的是正确的设备。如有需要，请断开其他存储设备。

   .. image:: img/imager_storage.png
      :width: 90%


#. 检查设置无误后，点击 **WRITE** 开始写入。

   .. image:: img/nvme_write.png
      :width: 90%

#. 确认警告提示，允许 Raspberry Pi Imager 擦除并写入引导程序。

   .. image:: img/imager_erase.png
      :width: 90%

#. 等待直到显示 **Write complete!**，然后安全移除存储设备。

   .. image:: img/nvme_finish.png
      :width: 90%

#. 将 Micro SD 卡插入 Raspberry Pi，并上电启动一次以应用引导程序更新。

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. 当 Raspberry Pi 启动完成后，请至少等待 **10 秒**，然后关机并移除 Micro SD 卡或 NVMe SSD。

此时，Raspberry Pi 5 已准备好从 **NVMe** 启动。

.. end_update_bootloader

3. 将操作系统安装到 NVMe SSD
-----------------------------------

现在，你可以在 NVMe SSD 上安装操作系统了。

#. 使用转接器将 **NVMe SSD** 插入电脑。

2. 打开 Raspberry Pi Imager 后，你会看到 **Device** 页面。从列表中选择你的 Raspberry Pi 5 型号。

   .. image:: img/imager_device.png
      :width: 90%

3. 进入 **OS** 部分，选择推荐的 **Raspberry Pi OS (64-bit)**。

   .. image:: img/imager_os.png
      :width: 90%

4. 在 **Storage** 部分，选择你的 **NVMe SSD**。

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os
