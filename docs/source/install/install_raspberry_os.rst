安装Raspberry Pi操作系统
================================================================================

你可以根据是否拥有Micro SD卡或NVMe SSD来选择合适的安装方法。

**仅使用Micro SD卡**

  如果你只使用Micro SD卡，可以按照下面的第一种方法进行安装。

**使用M.2 NVMe SSD**

  * 如果你有 **M.2 NVMe SSD外接适配器** ，可以通过适配器将SSD连接到电脑，然后按照第二种方法安装操作系统。

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * 如果你没有上述适配器，可以先使用第一种方法在Micro SD卡上安装操作系统，然后使用第三种方法将系统从Micro SD卡复制到你的M.2 NVMe SSD。

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi