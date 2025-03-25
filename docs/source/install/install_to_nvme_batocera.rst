.. _install_to_nvme_ubuntu:

在NVMe SSD上安装操作系统
============================================

如果你使用的是NVMe SSD，并且有适配器将其连接到电脑进行系统安装，可以参考以下教程进行快速安装。

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**所需组件**

* 一台个人电脑
* 一块NVMe SSD
* 一个NVMe转USB适配器
* 一张Micro SD卡和读卡器

.. _update_bootloader:

1. 更新引导程序
----------------------------------

首先，你需要更新Raspberry Pi 5的引导程序，使其能够优先从NVMe启动，然后再尝试USB和SD卡。

.. 
   .. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    在此步骤中，建议使用备用的Micro SD卡。首先将引导程序写入该Micro SD卡，然后立即将其插入Raspberry Pi，以启用从NVMe设备启动。
    
    另外，你也可以先将引导程序直接写入NVMe设备，然后将其插入Raspberry Pi以更改启动方式。之后，将NVMe SSD连接到电脑安装操作系统，安装完成后，再将其插回Raspberry Pi。

#. 使用读卡器将备用的Micro SD卡或NVMe SSD插入电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi设备** ，从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.jpg
      :width: 90%

#. 在 **操作系统** 选项卡中，向下滚动并选择 **Misc utility images** 。

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. 选择 **Bootloader (Pi 5 family)** 。

   .. image:: img/nvme_bootloader.jpg
      :width: 90%
      

#. 选择 **NVMe/USB Boot** ，使Raspberry Pi 5能够从NVMe启动，然后再尝试USB和SD卡。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **存储** 选项中，选择适合安装的存储设备。

   .. note::

      确保选择正确的存储设备。为避免混淆，建议断开其他存储设备。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在你可以点击 **NEXT** 。如果存储设备中已有数据，请确保进行备份，以防数据丢失。如果不需要备份，可以点击 **是** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 很快，你将看到提示，表示 **NVMe/USB Boot** 已经成功写入存储设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 现在，你可以将Micro SD卡或NVMe SSD插入Raspberry Pi。为Raspberry Pi提供电源后，Micro SD卡或NVMe SSD中的引导程序将被写入Raspberry Pi的EEPROM。

.. note::

    之后，Raspberry Pi将优先从NVMe启动，然后再尝试USB和SD卡。
    
    关闭Raspberry Pi并移除Micro SD卡或NVMe SSD。


2. 将操作系统安装到NVMe SSD
---------------------------------

现在你可以将操作系统安装到你的NVMe SSD上。

**步骤**

#. 首先，访问 |link_batocera_download| 页面，选择 **Raspberry Pi 5 B** ，并点击下载。

   .. image:: img/batocera_download.png
      :width: 90%


#. 使用读卡器将SD卡插入电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **操作系统** 选项卡。

   .. image:: img/os_choose_os.jpg
      :width: 90%
      
#. 向下滚动到页面底部并选择 **使用自定义** 。

   .. image:: img/batocera_os_use_custom.jpg
      :width: 90%


#. 选择你刚刚下载的系统文件 ``batocera-xxx-xx-xxxxxxxx.img.gz`` ，然后点击 **打开** 。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. 在 **存储** 选项中，选择适合安装的存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. 现在你可以点击 **NEXT**。如果存储设备中已有数据，请确保进行备份，以防数据丢失。如果不需要备份，可以点击 **是** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当你看到“写入成功”的弹窗时，说明镜像已经完全写入并验证完成。现在，你可以从NVMe SSD启动Raspberry Pi了！
