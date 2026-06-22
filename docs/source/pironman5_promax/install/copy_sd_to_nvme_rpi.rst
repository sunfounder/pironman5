.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _copy_sd_to_nvme_promax:

将系统从 Micro SD 复制到 NVMe SSD
==================================================================

如果你有 NVMe SSD，但没有适配器可以将其连接到电脑，可以采用第三种方法：先将系统安装到 Micro SD 卡上。当 Pironman 5 Pro MAX 成功启动后，再把系统从 Micro SD 卡迁移到 NVMe SSD。

* 首先需要完成 :ref:`install_os_sd_rpi_promax`。
* 然后启动并登录 Raspberry Pi。如果不知道如何登录，可以参考 Raspberry Pi 官方网站：|link_rpi_get_start|。

完成以上步骤后，再继续下面的操作。


1. 启用 PCIe
--------------------

默认情况下，PCIe 接口是未启用的。

* 要启用它，需要打开 ``/boot/firmware/config.txt`` 文件。

  .. code-block:: shell
    
     sudo nano /boot/firmware/config.txt

* 然后在文件中添加以下内容。

  .. code-block:: shell
    
     # Enable the PCIe External connector.
     dtparam=pciex1

* ``pciex1`` 还有一个更容易记忆的别名，因此你也可以在 ``/boot/firmware/config.txt`` 中添加 ``dtparam=nvme``\ 。

  .. code-block:: shell
    
     dtparam=nvme

* 你还需要关闭 PCIe 启动延迟，以便 Raspberry Pi 在启动时能够检测到通过 PCIe Switch 连接的 NVMe 硬盘。在 ``/boot/firmware/config.txt`` 中添加以下内容：

  .. code-block:: shell
  
     dtparam=pciex1_no_10s=on


* 按 ``Ctrl + X``\ 、 ``Y`` 和 ``Enter`` 保存更改。


**BOOT_ORDER**

如果你安装了两个 NVMe 系统盘并需要选择其中一个作为启动盘，可以修改 ``/boot/firmware/cmdline.txt`` 文件中的 ``ROOT=PARTUUID=xxxxxxxxx``\ ，将其改为你希望启动的磁盘 UUID。可以使用以下命令查看磁盘 UUID：

.. code-block:: shell

   ls /dev/disk/by-id/


.. start_copy_nvme

2. 在 SSD 上安装系统
----------------------------------------

在 SSD 上安装系统有两种方式：

**将系统从 Micro SD 卡复制到 SSD**

#. 连接显示器，或者通过 VNC Viewer 访问 Raspberry Pi 桌面。然后点击 **Raspberry Pi logo** → **Accessories** → **SD Card Copier**\ 。

   .. image:: img/ssd_copy.png
      
#. 确认正确选择 **Copy From** 和 **Copy To** 设备，避免选错。

   .. image:: img/ssd_copy_from.png
      
#. 记得勾选 **NEW Partition UUIDs**\ ，以确保系统能够正确区分设备，避免挂载冲突和启动问题。

   .. image:: img/ssd_copy_uuid.png
    
#. 选择完成后，点击 **Start**\ 。

   .. image:: img/ssd_copy_click_start.png

#. 系统会提示 SSD 上的内容将被清除。点击 Yes 前请确保已经备份数据。等待一段时间后，复制过程将完成。


**使用 Raspberry Pi Imager 安装系统**

如果 Micro SD 卡上安装的是带桌面的系统版本，你也可以使用镜像工具（例如 Raspberry Pi Imager）将系统写入 SSD。本示例使用 Raspberry Pi OS Bookworm，其他系统可能需要先安装镜像工具。

#. 连接显示器或通过 VNC Viewer 访问 Raspberry Pi 桌面。然后点击 **Raspberry Pi logo** → **Accessories** → **Raspberry Pi Imager**\ 。

   .. image:: img/ssd_imager.png

#. 使用读卡器将 MicroSD 卡插入电脑。在继续之前请备份重要数据。

   .. image:: img/insert_sd.png
      :width: 90%

#. 打开 Raspberry Pi Imager 后，会看到 **Device** 页面。从列表中选择你的 Raspberry Pi 5 型号。

   .. image:: img/imager_device.png
      :width: 90%

#. 进入 **OS** 选项，选择推荐的 **Raspberry Pi OS (64-bit)**\ 。

   .. image:: img/imager_os.png
      :width: 90%

#. 在 **Storage** 中选择你的 **NVMe SSD**\ 。

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_promax:

3. 配置从 SSD 启动
---------------------------------------

在本节中，我们将配置 Raspberry Pi 直接从 NVMe SSD 启动，从而获得比 SD 卡更快的启动速度和更好的系统性能。请按照以下步骤操作：

#. 首先，在 Raspberry Pi 上打开终端并运行以下命令进入配置界面：

   .. code-block:: shell
   
      sudo raspi-config

#. 在 ``raspi-config`` 菜单中，使用方向键选择 **Advanced Options**\ ，然后按 ``Enter`` 进入高级设置。

   .. image:: img/nvme_open_config.png

#. 在 **Advanced Options** 中，选择 **Boot Order**\ 。该选项用于设置 Raspberry Pi 搜索可启动设备的顺序。

   .. image:: img/nvme_boot_order.png

#. 然后选择 **NVMe/USB boot**\ 。这将使 Raspberry Pi 优先从 USB 连接的 SSD 或 NVMe 硬盘启动，而不是 SD 卡。

   .. image:: img/nvme_boot_nvme.png

#. 选择完成后，点击 **Finish** 退出 raspi-config。你也可以使用 **Escape** 键关闭配置工具。

   .. image:: img/nvme_boot_ok.png

#. 为使新的启动设置生效，请运行 ``sudo reboot`` 重启 Raspberry Pi。

   .. code-block:: shell

      sudo reboot
   
   .. image:: img/nvme_boot_reboot.png

重启后，Raspberry Pi 将尝试从已连接的 NVMe SSD 启动，从而为系统提供更高的性能和更好的可靠性。

.. end_copy_nvme
