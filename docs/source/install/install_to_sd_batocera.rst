.. _install_to_sd_ubuntu: 

在Micro SD卡上安装操作系统
=============================================

如果你使用的是Micro SD卡，可以按照以下教程将系统安装到Micro SD卡上。

**所需组件**

* 一台个人电脑
* 一张Micro SD卡和一个读卡器

**步骤**

#. 首先，访问 |link_batocera_download| 页面，选择 **Raspberry Pi 5 B** ，然后点击下载。

   .. image:: img/batocera_download.png
      :width: 90%

#. 使用读卡器将SD卡插入到你的电脑或笔记本中。

#. 在 |link_rpi_imager| 中，点击 **操作系统** 选项卡。


   .. image:: img/os_choose_os.jpg
      :width: 90%

#. 向下滚动到页面底部并选择 **Use Custom** 。

   .. image:: img/batocera_os_use_custom.jpg
      :width: 90%

#. 选择你刚刚下载的系统文件 ``batocera-xxx-xx-xxxxxxxx.img.gz`` ，然后点击 **打开** 。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. 点击 **选择存储设备** 并选择适合安装的存储设备。


   .. image:: img/os_choose_sd.png
      :width: 90%

#. 现在你可以点击 **NEXT** 。如果存储设备中已有数据，请确保备份，以防数据丢失。如果不需要备份，可以点击 **是** 继续。

   .. image:: img/os_continue.png
      :width: 90%

#. 当你看到“写入成功”的弹窗时，说明镜像已经完全写入并验证完成。现在，你可以从Micro SD卡启动Raspberry Pi了！
