.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_rpi_promax:

在 NVMe SSD 上安装操作系统
===================================

如果你使用的是 NVMe SSD，并且拥有可以将 NVMe SSD 连接到电脑进行系统安装的适配器，可以按照以下教程快速完成安装。

**所需组件**

* 一台电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* Micro SD 卡和读卡器


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager


.. start_update_bootloader

.. _update_bootloader_promax:


2. 更新 Bootloader
--------------------------------

首先更新 Raspberry Pi 5 的 bootloader，使其启动顺序为：\ **NVMe → USB → SD 卡**\ 。

.. note::

   建议使用一张 **备用 Micro SD 卡** 来完成此步骤。

   - 方法 1（推荐）：将 bootloader 写入 Micro SD 卡，插入 Raspberry Pi，启动一次以应用设置。
   - 方法 2：直接将 bootloader 写入 NVMe SSD，然后再将 NVMe 连接到电脑安装系统，最后再装回 Raspberry Pi。

#. 使用读卡器或适配器将备用 **Micro SD 卡或 NVMe SSD** 插入电脑。

#. 打开 Raspberry Pi Imager 后，你会看到 **Device** 页面。从列表中选择你的 Raspberry Pi 5。

   .. image:: img/imager_device.png
      :width: 90%

#. 点击 **OS**\ 。

   * 向下滚动并选择 **Misc utility images**\ 。

     .. image:: img/nvme_misc.png
        :width: 90%

   * 选择 **Bootloader (Pi 5 family)**\ 。

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * 选择 **NVMe/USB Boot** 作为启动顺序，然后点击 **NEXT**\ 。

     .. image:: img/nvme_boot.png
        :width: 90%


#. 在 **Storage** 中选择正确的 Micro SD 卡或 NVMe SSD，然后点击 **NEXT**\ 。

   .. note::
   
      请确认选择的是正确设备。如有必要，可断开其他存储设备以避免误选。
   
   .. image:: img/imager_storage.png
      :width: 90%

#. 检查设置无误后点击 **WRITE** 开始写入。

   .. image:: img/nvme_write.png
      :width: 90%

#. 确认警告提示，让 Raspberry Pi Imager 擦除并写入 bootloader。

   .. image:: img/imager_erase.png
      :width: 90%

#. 等待出现 **Write complete!** 提示，然后安全移除存储设备。

   .. image:: img/nvme_finish.png
      :width: 90%

#. 将 Micro SD 卡插入 Raspberry Pi 并启动一次，以应用 bootloader 更新。

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. 在 Raspberry Pi 完成启动后至少等待 **10 秒**\ ，然后关闭电源并取出 Micro SD 卡或 NVMe SSD。

此时 Raspberry Pi 5 已准备好从 **NVMe** 启动。

.. end_update_bootloader


3. 在 NVMe SSD 上安装操作系统
-----------------------------------

现在可以在 NVMe SSD 上安装操作系统。

#. 使用适配器将 **NVMe SSD** 插入电脑。

2. 打开 Raspberry Pi Imager 后，在 **Device** 页面选择你的 Raspberry Pi 5。

   .. image:: img/imager_device.png
      :width: 90%

3. 进入 **OS** 选项，选择推荐的 **Raspberry Pi OS (64-bit)**\ 。

   .. warning::

      请务必选择 **64 位（64-bit）** 版本。若安装 **32 位** 系统，部分软件包仅提供 ``aarch64``\ （64 位）版本，可能导致某些功能无法正常安装或使用。

   .. image:: img/imager_os.png
      :width: 90%

4. 在 **Storage** 选项中选择你的 **NVMe SSD**\ 。

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os