安装 Raspberry Pi OS
================================================================================
您可以根据自己是否拥有 Micro SD 卡或 NVMe SSD 来选择合适的安装方式。

**仅使用 Micro SD 卡**

  如果您只使用 Micro SD 卡，可以直接参考下方的第一种方法进行安装。

**使用 M.2 NVMe SSD**

  * 如果您有一款 **M.2 NVMe SSD 外接盒适配器**，可以通过该适配器将 SSD 连接到电脑，并参考第二种方法来安装操作系统。

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center

  * 如果您没有上述适配器，可以先按照第一种方法将操作系统安装到 Micro SD 卡上，再使用第三种方法将系统从 Micro SD 卡复制到 M.2 NVMe SSD 上。


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi