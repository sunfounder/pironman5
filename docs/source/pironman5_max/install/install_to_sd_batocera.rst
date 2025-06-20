.. _max_install_to_sd_ubuntu:

在 Micro SD 卡上安装操作系统
=============================================

如果您使用的是 Micro SD 卡，可以按照以下教程将系统安装到 Micro SD 卡中。


**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡和读卡器

**操作步骤**

#. 首先访问 |link_batocera_download| 页面，选择 **Raspberry Pi 5 B**，点击进行下载。

   .. image:: img/batocera_download.png
      :width: 90%
      
#. 解压下载得到的文件 ``batocera-xxx-xx-xxxxxxxx.img.gz``。

#. 使用读卡器将 Micro SD 卡插入您的电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Operating System** 选项卡。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动页面至底部，选择 **Use Custom**。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. 选择刚刚解压得到的系统文件 ``batocera-xxx-xx-xxxxxxxx.img``，然后点击 **Open**。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. 点击 **Choose Storage**，选择正确的存储设备以进行安装。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 然后点击 **NEXT**。如果所选设备中已有数据，请提前备份。确认无须备份后点击 **Yes** 开始写入。

   .. image:: img/os_continue.png
      :width: 90%


#. 当您看到 “Write Successful” 的弹窗时，说明镜像已成功写入并完成校验。现在您已经可以使用这张 Micro SD 卡启动树莓派了！
