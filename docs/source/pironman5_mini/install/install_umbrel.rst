
安装 Umbrel OS
============================================

Umbrel 是一个开源的家庭服务器平台/操作系统，让你可以运行自己的比特币节点，一键安装各种自托管应用，并将你的硬件变成个人云端。它是开始学习自我托管与隐私保护的绝佳方式。

**所需组件**

* 一台个人电脑  
* 一块 NVMe SSD  
* 一个 NVMe 转 USB 适配器  
* 一张 Micro SD 卡和读卡器  

1. 更新启动加载程序
--------------------------------

首先，需要更新 Raspberry Pi 5 的启动加载程序，使其能够优先从 NVMe 启动，其次是 USB，最后是 SD 卡。

.. note::

    * 建议在此步骤中使用备用的 Micro SD 卡。先将启动加载程序写入这张卡，然后立即将其插入 Raspberry Pi，以启用从 NVMe 设备启动。  
    * 或者，你也可以直接将启动加载程序写入 NVMe 设备，然后将其插入 Raspberry Pi 来修改启动方式。之后，将 NVMe SSD 连接到电脑以安装操作系统，完成安装后再插回 Raspberry Pi。

#. 使用读卡器将 Micro SD 卡或 NVMe SSD 插入电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi Device**，然后从下拉菜单中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 在 **Operating System** 选项卡中，向下滚动并选择 **Misc utility images**。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. 选择 **NVMe/USB Boot**，以便 Raspberry Pi 5 可以优先从 NVMe 启动，其次是 USB，最后是 SD 卡。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      
#. 在 **Storage** 选项中，选择正确的存储设备以进行安装。

   .. note::

      请务必选择正确的存储设备。为避免混淆，如果连接了多个存储设备，请断开不必要的设备。

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. 现在可以点击 **NEXT**。如果存储设备中已有数据，请先备份以防数据丢失。如果不需要备份，请点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%
      

#. 很快会提示你 **NVMe/USB Boot** 已写入到你的存储设备中。

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. 将 Micro SD 卡或 NVMe SSD 插入 Raspberry Pi。连接 Type-C 电源后，启动加载程序会从 Micro SD 卡或 NVMe SSD 写入到 Raspberry Pi 的 EEPROM 中。

   .. note::

      * 更新完成后，Raspberry Pi 将按 NVMe → USB → Micro SD 的顺序启动。  
      * 等待一到两分钟，然后关闭 Raspberry Pi 并移除 Micro SD 卡或 NVMe SSD。

2. 在 NVMe SSD 上安装操作系统
-------------------------------------------------------------

**步骤**

1. 下载最新的 Umbrel OS 镜像文件并解压。你也可以访问 `Umbrel 发布页面 <https://github.com/getumbrel/umbrel/releases>`_ 来选择特定版本。

   * :download:`最新的 Umbrel OS 镜像 <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. 在 |link_rpi_imager| 中，点击 **Raspberry Pi Device**，然后从下拉菜单中选择 **Raspberry Pi 5**。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. 启动 **Raspberry Pi Imager** 并点击 **CHOOSE OS**。

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. 滚动到页面底部并选择 **Use custom**。

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. 选择你之前下载的 Umbrel OS 镜像文件，然后点击 **Open**。

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. 在 **Storage** 部分，选择 NVMe SSD 作为安装目标设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. 点击 **NEXT**，然后选择 **NO**。Umbrel OS 会在首次启动时自动初始化系统并配置用户，因此不会使用 Raspberry Pi Imager 中设置的用户名或密码。

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. 如果 NVMe SSD 中已有数据，请在继续前备份以防数据丢失。如果不需要备份，点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%

9. 当出现 “Write Successful” 提示时，表示镜像已成功写入并验证完成。你的 NVMe SSD 现在已准备好用于启动 Raspberry Pi！

   .. image:: img/umbrel_finish.png
      :width: 90%

