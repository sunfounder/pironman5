Installing Raspberry Pi OS
================================================================================

你可以根据手头是否有 Micro SD 卡或 NVMe SSD，选择合适的安装方式。

**仅使用 Micro SD 卡**

  如果你只使用 Micro SD 卡，可以直接按照下面的第一种方法进行安装。

**使用 M.2 NVMe SSD**

  * 如果你有 **M.2 NVMe SSD 硬盘盒转接器**，可以通过该转接器将 SSD 连接到电脑，并按照第二种方法安装操作系统。  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * 如果你没有上述转接器，可以先使用第一种方法将操作系统安装到 Micro SD 卡上，然后再使用第三种方法将系统从 Micro SD 卡复制到 M.2 NVMe SSD。  

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi
