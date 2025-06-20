.. _max_install_batocera:

安装 Batocera Linux
======================================================

|link_batocera| 是一个开源且完全免费的复古游戏操作系统发行版，可以被写入到 U 盘或 SD 卡中，旨在将任意电脑或微型计算机临时或永久变成游戏主机。

你可以根据手头是否有 Micro SD 卡或 NVMe SSD 来选择合适的安装方式。

相比安装到 Micro SD 卡，直接安装到 NVMe SSD 多了一步：你需要更新树莓派的启动加载器，因为其默认从 Micro SD 卡启动。更新启动加载器后，树莓派将优先从 NVMe SSD 启动。

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

