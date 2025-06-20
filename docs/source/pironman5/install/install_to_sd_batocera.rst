.. _install_to_sd_ubuntu:

在 Micro SD 卡上安装操作系统
=============================================

如果您打算使用 Micro SD 卡安装系统，可以按照以下教程将系统写入 Micro SD 卡中。


**Required Components**

* 一台个人电脑
* 一张 Micro SD 卡及其读卡器

**Steps**

#. 首先，访问 |link_batocera_download| 页面，选择 **Raspberry Pi 5 B**，然后点击下载。

    .. image:: img/batocera_download.png
      :width: 90%


#. 解压下载的文件 ``batocera-xxx-xx-xxxxxxxx.img.gz``。

#. 使用读卡器将 SD 卡插入您的电脑或笔记本电脑。

#. 打开 |link_rpi_imager|，点击 **Operating System** 选项卡。

    .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动页面底部，选择 **Use Custom**。

    .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. 选择刚刚解压的系统镜像文件 ``batocera-xxx-xx-xxxxxxxx.img``，然后点击 **Open**。

    .. image:: img/batocera_os_choose.png
      :width: 90%


#. 点击 **Choose Storage**，并选择正确的存储设备以进行安装。

    .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在可以点击 **NEXT**。如果存储设备中已有数据，请务必提前备份以防数据丢失。如果不需要备份，点击 **Yes** 继续操作。

    .. image:: img/os_continue.png
      :width: 90%


#. 当您看到 “Write Successful” 的弹窗提示时，说明系统镜像已经成功写入并校验完成。现在，您可以使用这张 Micro SD 卡启动 Raspberry Pi！
