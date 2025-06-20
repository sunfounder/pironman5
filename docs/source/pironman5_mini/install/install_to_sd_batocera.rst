.. _install_to_sd_ubuntu_mini:

将操作系统安装到 Micro SD 卡
=============================================

如果您打算使用 Micro SD 卡安装系统，可以按照以下教程将操作系统写入 Micro SD 卡。


**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡及读卡器

**操作步骤**

#. 首先访问 |link_batocera_download| 页面，选择 **Raspberry Pi 5 B**，然后点击下载。

   .. image:: img/batocera_download.png
      :width: 90%


#. 解压下载的文件 ``batocera-xxx-xx-xxxxxxxx.img.gz``。



#. 使用读卡器将 Micro SD 卡插入电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Operating System** 选项卡。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动页面到底部，选择 **Use Custom**。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. 选择刚才解压出的系统镜像文件 ``batocera-xxx-xx-xxxxxxxx.img``，然后点击 **Open**。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. 点击 **Choose Storage**，选择用于安装的存储设备。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在点击 **NEXT**。如果存储设备中已有数据，请确保已备份以防数据丢失。若不需要备份，可直接点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 当您看到 “Write Successful” 的弹窗提示时，说明系统镜像已成功写入并验证完成。现在，您可以使用 Micro SD 卡启动 Raspberry Pi！
