.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


安装 Batocera OS
=============================================

按照以下教程将系统安装到 Micro SD 卡中。


**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡及读卡器

   .. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager


2. 将系统安装到 microSD 卡
------------------------------------------------


   .. |shared_link_batocera_linux| raw:: html

    <a href="https://updates.batocera.org/bcm2712/stable/last/batocera-bcm2712-42-20251007.img.gz" target="_blank">Batocera.Linux</a>


1. 从 |shared_link_batocera_linux| 网站下载最新版本的系统。

2. 使用读卡器将 microSD 卡插入电脑。  
   在继续之前，请备份卡中的重要数据，因为该过程会清空卡中的所有内容。

   .. image:: img/insert_sd.png
      :width: 90%

3. 打开 **Raspberry Pi Imager** 后，你会看到 **Device** 页面。  
   在列表中选择你的 **Raspberry Pi 5**\ 。

   .. image:: img/imager_device.png
      :width: 90%

4. 进入 **OS** 选项，滚动到页面底部，选择 **Username custom**\ 。

   .. image:: img/imager_use_custom.png
      :width: 90%

5. 选择刚刚下载的 **batocera-bcmxxxxxxx.img.gz** 文件，然后点击 **Open**\ 。

   .. image:: img/imager_choose_batocera.png
      :width: 90%

6. 在 **Storage** 选项中选择你的 microSD 卡。  
   为避免误选设备，建议先拔掉其他 USB 存储设备，这样列表中只会显示 microSD 卡。

   .. image:: img/imager_storage.png
      :width: 90%

#. 点击 **NEXT**\ ，进入 **Writing** 步骤，系统镜像将被写入 microSD 卡。

   .. image:: img/imager_betocera_write.png
      :width: 90%

#. 当出现 **“Write Successful”** 提示窗口时，说明镜像已经写入并校验完成。现在可以安全取出 microSD 卡，并用它来启动 Raspberry Pi。

   .. image:: img/imager_betocera_finish.png
      :width: 90%