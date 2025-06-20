安装 Raspberry Pi 操作系统
================================================================================

你可以根据手头是否有 Micro SD 卡或 NVMe SSD 来选择安装方式。

* 相比于安装到 Micro SD 卡，直接安装到 NVMe SSD 需要多一步操作：你需要更新树莓派的启动加载器，因为默认启动顺序是从 Micro SD 卡启动。更新启动加载器后，系统将优先从 NVMe SSD 启动。
* 如果你拥有 NVMe SSD，但没有适配器将其连接到电脑，可以选择第三种方式：先将系统安装到 Micro SD 卡上。待 Pironman 5 成功启动后，再将系统从 Micro SD 卡复制到 NVMe SSD。


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi