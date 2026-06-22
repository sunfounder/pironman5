.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


安装 Raspberry Pi OS
================================================================================

您可以根据是否拥有 Micro SD 卡或 NVMe SSD，选择不同的安装方式。

**仅使用 Micro SD 卡**

  如果您仅使用 Micro SD 卡，可以直接按照下面的第一种方法进行安装。

**使用 M.2 NVMe SSD**

  * 如果您拥有 **M.2 NVMe SSD 外接盒（Enclosure Adapter）**\ ，可以通过该适配器将 SSD 连接到电脑，并按照第二种方法安装操作系统。  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * 如果没有上述适配器，可以先通过第一种方法将系统安装到 Micro SD 卡，然后再使用第三种方法将系统从 Micro SD 卡复制到 M.2 NVMe SSD。  

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi