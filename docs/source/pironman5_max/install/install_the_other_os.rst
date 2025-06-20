安装 Ubuntu/Kali Linux/Homebridge/Home Assistant
=========================================================

您可以根据手头是否有 Micro SD 卡或 NVMe 固态硬盘选择相应的安装方式。

如果直接将系统安装到 NVMe 固态硬盘中，相比于安装到 Micro SD 卡，还需额外执行一步：更新树莓派的启动引导程序（bootloader），因为树莓派默认从 Micro SD 启动。通过更新引导程序，使其优先从 NVMe SSD 启动。


.. toctree::
    :maxdepth: 1

    install_to_sd_other_os
    install_to_nvme_other_os
