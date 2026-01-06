.. _install_to_nvme_other_max:

在 NVMe SSD 上安装操作系统
============================================

如果你使用的是 NVMe SSD，并且有可将 NVMe SSD 连接到电脑进行系统安装的转接器，可以按照以下教程快速完成安装。

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**所需组件**

* 一台个人电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 转接器
* Micro SD 卡及读卡器

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. 将操作系统安装到 microSD 卡
------------------------------------------------

#. 使用转接器将 **NVMe SSD** 插入电脑。

2. 打开 **Raspberry Pi Imager** 后，你将看到 **Device** 页面。  
   从列表中选择你的 **Raspberry Pi 5** 型号。

   .. image:: img/imager_device.png
      :width: 90%

3. 进入 **OS** 部分，向下滚动到页面底部并选择你的操作系统。

   .. note::

      * 对于 **Ubuntu**，点击 **Other general-purpose OS** → **Ubuntu**，然后选择  
        **Ubuntu Desktop 24.04 LTS (64-bit)** 或 **Ubuntu Server 24.04 LTS (64-bit)**。
      * 对于 **Kali Linux**、**Home Assistant** 和 **Homebridge**，点击  
        **Other specific-purpose OS**，然后选择对应的系统。

   .. image:: img/imager_other_os.png
      :width: 90%

4. 在 **Storage** 部分，选择你的 **NVMe SSD**。

   .. image:: img/nvme_storage.png
      :width: 90%

#. 点击 **NEXT**。

   .. note::

      * 对于 **不支持提前配置** 的系统，点击 **NEXT** 将跳过 **Customisation** 步骤，并直接进入 **Writing**，系统镜像将被写入 microSD 卡。
      * 对于 **支持预配置** 的系统，请按照 **Customisation** 步骤设置 **Hostname**、**WiFi** 以及 **启用 SSH** 等选项。

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. 当出现 **“Write Successful”** 弹窗时，表示镜像已经完整写入并通过校验。此时你可以安全地移除 microSD 卡，并使用它来启动你的 Raspberry Pi。
