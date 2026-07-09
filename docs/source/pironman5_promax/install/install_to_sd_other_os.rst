.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_sd_other_promax:

在 Micro SD 卡上安装操作系统
=============================================

如果你使用的是 Micro SD 卡，可以按照下面的教程将系统安装到 Micro SD 卡上。

**所需组件**

* 一台电脑
* 一张 Micro SD 卡和读卡器

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager


2. 将操作系统安装到 microSD 卡
------------------------------------------------

1. 使用读卡器将 microSD 卡插入电脑。  
   在继续之前，请备份卡中的重要数据，因为该过程会清空卡中的所有内容。

   .. image:: img/insert_sd.png
      :width: 90%

2. 打开 **Raspberry Pi Imager** 后，你会看到 **Device** 页面。  
   从列表中选择你的 **Raspberry Pi 5**\ 。

   .. image:: img/imager_device.png
      :width: 90%

3. 进入 **OS** 选项，向下滚动到页面底部并选择你要安装的操作系统。

   .. note::

      * 对于 **Ubuntu**\ ，点击 **Other general-purpose OS** → **Ubuntu**\ ，然后选择 **Ubuntu Desktop 24.04 LTS (64-bit)** 或 **Ubuntu Server 24.04 LTS (64-bit)**\ 。
      * 对于 **Kali Linux** 和 **Homebridge**\ ，点击 **Other specific-purpose OS**\ ，然后选择对应的系统。

   .. warning::

      无论选择哪种系统，都请务必选择 **64 位（64-bit）** 版本。在 **32 位** 系统上，部分软件包仅提供 ``aarch64``\ （64 位）版本，可能导致某些功能无法正常安装或使用。

   .. image:: img/imager_other_os.png
      :width: 90%

4. 在 **Storage** 选项中选择你的 microSD 卡。  
   为避免误选设备，建议先拔掉其他 USB 存储设备，这样列表中只会显示 microSD 卡。

   .. image:: img/imager_storage.png
      :width: 90%

#. 点击 **NEXT**\ 。

   .. note::

      * 对于 **无法提前配置** 的系统，点击 **NEXT** 后会跳过 **Customisation** 步骤，直接进入 **Writing**\ ，系统将被写入 microSD 卡。
      * 对于 **支持预配置** 的系统，可以在 **Customisation** 步骤中设置 **Hostname**\ 、\ **WiFi**\ 、\ **Enable SSH** 等选项。

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. 当出现 **“Write Successful”** 提示窗口时，说明镜像已经写入并校验完成。现在可以安全地取出 microSD 卡，并用它来启动 Raspberry Pi。