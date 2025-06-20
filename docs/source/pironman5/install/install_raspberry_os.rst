安装 Raspberry Pi OS
================================================================================

您可以根据手头是否有 Micro SD 卡或 NVMe SSD，选择适合的安装方式。

**仅使用 Micro SD 卡**

  如果您只使用 Micro SD 卡，只需按照下方的第一种方法进行安装即可。

**使用 M.2 NVMe SSD**

  * 如果您有一个 **M.2 NVMe SSD 硬盘盒适配器**，可使用该适配器将 SSD 连接到计算机，并参考第二种方法来安装操作系统。

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * 如果您没有上述适配器，可以先使用第一种方法将系统安装到 Micro SD 卡上，然后使用第三种方法将系统从 Micro SD 卡复制到 M.2 NVMe SSD。

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi