.. _install_batocera_mini:

安装 Batocera Linux
======================================================

|link_batocera| 是一款开源且完全免费的复古游戏系统发行版，可通过复制到 U 盘或 Micro SD 卡中，将任意电脑或微型计算机临时或永久变成游戏主机。

您可以根据手头是否有 Micro SD 卡或 NVMe SSD 来选择安装方式。

相比于安装到 Micro SD 卡，直接安装到 NVMe SSD 需要额外执行一步操作：更新 Raspberry Pi 的启动引导程序（bootloader）。因为默认情况下，Raspberry Pi 会从 Micro SD 卡启动。请更新 bootloader，以优先从 NVMe SSD 启动。

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera
    
