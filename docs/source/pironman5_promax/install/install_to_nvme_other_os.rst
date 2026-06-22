.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_other_promax:

在 NVMe SSD 上安装操作系统
============================================

如果你使用的是 NVMe SSD，并且拥有可以将 NVMe SSD 连接到电脑进行系统安装的适配器，可以按照下面的教程快速完成安装。

   .. image:: img/m2_nvme_adapter.png
      :width: 300
      :align: center

**所需组件**

* 一台电脑
* 一块 NVMe SSD
* 一个 NVMe 转 USB 适配器
* Micro SD 卡和读卡器

   .. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. 将系统安装到 NVMe SSD
------------------------------------------------

#. 使用适配器将 **NVMe SSD** 插入电脑。

2. 打开 **Raspberry Pi Imager** 后，会看到 **Device** 页面。  
   从列表中选择你的 **Raspberry Pi 5**\ 。

   .. image:: img/imager_device.png
      :width: 90%

3. 进入 **OS** 选项，向下滚动到页面底部并选择你要安装的操作系统。

   .. note::

      * 对于 **Ubuntu**\ ，点击 **Other general-purpose OS** → **Ubuntu**\ ，然后选择 **Ubuntu Desktop 24.04 LTS (64-bit)** 或 **Ubuntu Server 24.04 LTS (64-bit)**\ 。
      * 对于 **Kali Linux** 和 **Homebridge**\ ，点击 **Other specific-purpose OS**\ ，然后选择对应系统。

   .. image:: img/imager_other_os.png
      :width: 90%

4. 在 **Storage** 选项中选择你的 **NVMe SSD**\ 。

   .. image:: img/nvme_storage.png
      :width: 90%

#. 点击 **NEXT**\ 。

   .. note::

      * 对于 **无法提前配置** 的系统，点击 **NEXT** 后会跳过 **Customisation** 步骤，直接进入 **Writing**\ ，系统将被写入 NVMe SSD。
      * 对于 **支持预配置** 的系统，可以在 **Customisation** 步骤中设置 **Hostname**\ 、\ **WiFi**\ 、\ **Enable SSH** 等选项。

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. 当出现 **“Write Successful”** 提示时，说明镜像已经写入并校验完成。现在可以安全地移除 NVMe SSD，并用它来启动 Raspberry Pi。