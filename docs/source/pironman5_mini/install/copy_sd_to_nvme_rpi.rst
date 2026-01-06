.. _copy_sd_to_nvme_mini:

将系统从 Micro SD 卡复制到 NVMe SSD
==================================================================

如果你没有 NVMe 转接器，可以先将操作系统安装在 **Micro SD 卡** 上，在 Pironman 5 成功启动后，再将系统复制到 **NVMe SSD**。

* 首先，完成 :ref:`install_os_sd_mini`。
* 然后，启动并登录你的 Raspberry Pi。如需登录帮助，请参阅：|link_rpi_get_start|。

在继续以下操作之前，请确保已完成上述步骤。


1. 启用 PCIe
--------------------

默认情况下，PCIe 接口是未启用的。

* 要启用它，请打开 ``/boot/firmware/config.txt`` 文件。

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* 然后在文件中添加以下一行内容。

  .. code-block:: shell
  
    # 启用 PCIe 外部接口
    dtparam=pciex1
  
* ``pciex1`` 还有一个更容易记忆的别名，因此你也可以在 ``/boot/firmware/config.txt`` 文件中添加 ``dtparam=nvme``。

  .. code-block:: shell
  
    dtparam=nvme

* 该连接通过了 Gen 2.0（5 GT/sec）速率认证，但如果你在 ``/boot/firmware/config.txt`` 中添加以下内容，也可以强制启用 Gen 3.0（10 GT/sec）。

  .. code-block:: shell
  
    # 强制使用 Gen 3.0 速率
    dtparam=pciex1_gen=3
  
  .. warning::
  
    Raspberry Pi 5 并未通过 Gen 3.0 速率认证，在该速率下与 PCIe 设备的连接可能不稳定。

* 按下 ``Ctrl + X``，然后按 ``Y`` 和 ``Enter`` 保存更改。

.. start_copy_nvme

2. 在 SSD 上安装操作系统
----------------------------------------

有两种方式可以在 SSD 上安装操作系统：

**将系统从 Micro SD 卡复制到 SSD**

#. 连接显示器，或通过 VNC Viewer 访问 Raspberry Pi 桌面。然后点击 **Raspberry Pi 图标** -> **Accessories（附件）** -> **SD Card Copier**。

   .. image:: img/ssd_copy.png
      
    
#. 请务必正确选择 **Copy From** 和 **Copy To** 设备，注意不要选反。

   .. image:: img/ssd_copy_from.png
      
#. 请记得勾选 “NEW Partition UUIDs”，以确保系统能够正确区分设备，避免挂载冲突和启动问题。

   .. image:: img/ssd_copy_uuid.png
    
#. 完成选择后，点击 **Start**。

   .. image:: img/ssd_copy_click_start.png

#. 系统会提示 SSD 上的数据将被清除。在点击 Yes 之前，请务必备份重要数据。等待一段时间后，复制过程将完成。

**使用 Raspberry Pi Imager 安装系统**

如果你的 Micro SD 卡中安装的是桌面版系统，可以使用镜像工具（如 Raspberry Pi Imager）将系统写入 SSD。本示例使用的是 Raspberry Pi OS bookworm，其他系统可能需要先安装该镜像工具。

#. 连接显示器，或通过 VNC Viewer 访问 Raspberry Pi 桌面。然后点击 **Raspberry Pi 图标** -> **Accessories（附件）** -> **Raspberry Pi Imager**。

   .. image:: img/ssd_imager.png

#. 使用读卡器将 microSD 卡插入电脑。在继续之前，请备份所有重要数据。

   .. image:: img/insert_sd.png
      :width: 90%

#. 当 Raspberry Pi Imager 打开后，你会看到 **Device** 页面。从列表中选择你的 Raspberry Pi 5 型号。

   .. image:: img/imager_device.png
      :width: 90%

#. 进入 **OS** 部分，选择推荐的 **Raspberry Pi OS (64-bit)**。

   .. image:: img/imager_os.png
      :width: 90%

#. 在 **Storage** 部分，选择你的 **NVMe SSD**。

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_mini:

3. 配置从 SSD 启动
---------------------------------------

在本节中，我们将配置 Raspberry Pi 直接从 NVMe SSD 启动，从而相比 SD 卡获得更快的启动速度和更好的性能。请按照以下步骤操作：

#. 首先，在 Raspberry Pi 上打开终端，运行以下命令进入配置界面。

   .. code-block:: shell

      sudo raspi-config

#. 在 ``raspi-config`` 菜单中，使用方向键选择 **Advanced Options**，然后按 ``Enter`` 进入高级设置。

   .. image:: img/nvme_open_config.png

#. 在 **Advanced Options** 中，选择 **Boot Order**。该选项用于指定 Raspberry Pi 查找可启动设备的顺序。

   .. image:: img/nvme_boot_order.png

#. 接着，选择 **NVMe/USB boot**。这将告诉 Raspberry Pi 优先从 USB 连接的 SSD 或 NVMe 设备启动，而不是 SD 卡等其他选项。

   .. image:: img/nvme_boot_nvme.png

#. 选择完成后，按 **Finish** 退出 raspi-config。你也可以使用 **Escape** 键关闭配置工具。

   .. image:: img/nvme_boot_ok.png

#. 为了使新的启动设置生效，请运行 ``sudo reboot`` 重启 Raspberry Pi。

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

重启后，Raspberry Pi 将尝试从已连接的 NVMe SSD 启动，从而为你的系统提供更高的性能和更好的耐用性。

.. end_copy_nvme
