安装 Umbrel OS
============================================

Umbrel 是一个开源的自托管家庭服务器平台/操作系统，可用于运行自己的 Bitcoin 节点、安装各种一键式自托管应用，并将你的硬件变成个人家庭云服务器。这是开始学习自托管、数据自主和隐私保护的一个很好的平台。

**所需组件**

* 一台电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* Micro SD 卡和读卡器

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. 将系统安装到 NVMe SSD
-----------------------------------

现在可以将操作系统安装到 **NVMe SSD** 上。  
只需按照以下步骤操作即可——本指南为初学者设计，步骤简单易懂。

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Umbrel OS Releases</a>

#. 下载最新版本的 **Umbrel OS** 镜像并解压。如果需要特定版本，也可以访问 |link_umbrel_release| 页面。

   * :download:`Latest Umbrel OS Image <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. 使用 **NVMe 转 USB 适配器** 将 **NVMe SSD** 插入电脑。

#. 打开 **Raspberry Pi Imager**\ 。在 **Device** 页面中，从列表中选择 **Raspberry Pi 5**\ 。

   .. image:: img/imager_device.png
      :width: 90%

#. 进入 **OS** 选项，向下滚动到页面底部，选择 **Use custom**\ 。

   .. image:: img/imager_use_custom.png
      :width: 90%

#. 选择之前下载并解压的 **Umbrel OS 镜像文件**\ ，然后点击 **Open**\ 。

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. 点击 **Next** 继续。

   .. image:: img/imager_custom_next.png
      :width: 90%

#. 在 **Storage** 选项中选择你的 **NVMe SSD**\ 。请确认选择的是 NVMe SSD，而不是电脑中的其他硬盘。

   .. image:: img/nvme_storage.png
      :width: 90%

#. 仔细检查所有设置，然后点击 **WRITE**\ 。

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. 如果 NVMe SSD 中已有数据，Raspberry Pi Imager 会提示所有数据将被删除。请再次确认选择的是正确设备，然后点击 **I UNDERSTAND, ERASE AND WRITE**\ 。

   .. image:: img/imager_erase.png
      :width: 90%

#. 当出现 **“Write Complete”** 提示时，说明系统镜像已经写入并验证成功。

   .. image:: img/imager_umbrel_finish.png
      :width: 90%