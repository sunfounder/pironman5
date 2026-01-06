Installing Umbrel OS
============================================

Umbrel 是一个开源、自托管的家庭服务器平台/操作系统，可让你运行自己的比特币节点，安装各种一键式自托管应用，并将你的硬件变成个人家庭云。这是一个开始实践自托管和隐私保护的绝佳方式。

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 转接器
* Micro SD 卡及读卡器

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. 在 NVMe SSD 上安装操作系统
-----------------------------------

现在你可以将操作系统安装到 **NVMe SSD** 上了。  
请仔细按照以下步骤操作——本指南面向初学者，简单易懂。

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Umbrel OS Releases</a>

#. 下载最新版本的 **Umbrel OS** 镜像并解压文件。如果你想使用指定版本，也可以访问 |link_umbrel_release| 页面。

   * :download:`最新 Umbrel OS 镜像 <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. 使用 **NVMe 转 USB 转接器** 将 **NVMe SSD** 连接到电脑。

#. 打开 **Raspberry Pi Imager**。在 **Device** 页面中，从列表里选择你的 **Raspberry Pi 5** 型号。

   .. image:: img/imager_device.png
      :width: 90%

#. 进入 **OS** 部分，向下滚动到页面底部，并选择 **Use custom**。

   .. image:: img/imager_use_custom.png
      :width: 90%

#. 选择你之前下载并解压好的 **Umbrel OS 镜像文件**，然后点击 **Open**。

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. 点击 **Next** 继续。

   .. image:: img/imager_custom_next.png
      :width: 90%

#. 在 **Storage** 部分，选择你的 **NVMe SSD**。请务必确认选择的是 NVMe SSD，而不是电脑上的其他磁盘。

   .. image:: img/nvme_storage.png
      :width: 90%

#. 仔细检查所有设置，然后点击 **WRITE**。

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. 如果 NVMe SSD 中已有数据，Raspberry Pi Imager 会提示所有数据将被清除。请再次确认选择了正确的磁盘，然后点击 **I UNDERSTAND, ERASE AND WRITE**。

   .. image:: img/imager_erase.png
      :width: 90%

#. 当出现 **“Write Complete”** 提示时，说明镜像已经成功写入并完成校验。

   .. image:: img/imager_umbrel_finish.png
      :width: 90%
