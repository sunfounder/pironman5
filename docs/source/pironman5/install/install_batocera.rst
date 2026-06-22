.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


安装 Batocera 操作系统
==========================================================

请按照以下教程在您的 microSD 卡上安装系统。

**所需组件**

* 个人电脑
* 一张 Micro SD 卡和一个读卡器

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. 在 microSD 卡上安装操作系统
-------------------------------------------------------------------

1.  使用读卡器将您的 microSD 卡插入电脑。
    在继续之前，请备份卡上的所有重要数据，因为它们将被清除。

   .. image:: img/insert_sd.png
      :width: 90%

2.  当 **Raspberry Pi Imager** 打开时，您会看到 **Device（设备）** 页面。
    从列表中选择您的 **Raspberry Pi 5** 型号。

   .. image:: img/imager_device.png
      :width: 90%

3.  进入 **OS（操作系统）** 部分，向下滚动到页面底部，然后选择您的操作系统。

   .. note::

      * 对于 **Ubuntu**\ ，请点击 **Other general-purpose OS（其他通用操作系统）** → **Ubuntu**\ ，然后选择
        **Ubuntu Desktop 24.04 LTS (64-bit)** 或 **Ubuntu Server 24.04 LTS (64-bit)**\ 。
      * 对于 **Kali Linux**\ 、 **Home Assistant** 和 **Homebridge**\ ，请点击
        **Other specific-purpose OS（其他专用操作系统）**\ ，然后选择相应的系统。

   .. image:: img/imager_other_os.png
      :width: 90%

4.  在 **Storage（存储）** 部分，选择您的 microSD 卡。
    为了更安全，建议拔下其他 USB 存储设备，以便只有 microSD 卡出现在列表中。

   .. image:: img/imager_storage.png
      :width: 90%

#. 点击 **NEXT（下一步）**\ 。

   .. note::

      * 对于 **无法进行预配置**\ 的系统，点击 **NEXT（下一步）** 将跳过 **Customisation（自定义）** 步骤，直接进入 **Writing（写入）**\ ，即操作系统被写入 microSD 卡。
      * 对于 **支持预配置** 的系统，请按照 **Customisation（自定义）** 步骤来配置诸如 **Hostname（主机名）**\ 、 **WiFi** 和 **SSH 启用** 等选项。

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. 当弹出窗口显示 **「Write Successful（写入成功）」** 时，表示镜像已完全写入并验证完毕。您现在可以安全地取出 microSD 卡，并用来启动您的 Raspberry Pi。