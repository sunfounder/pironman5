.. _omv_5:

设置 OpenMediaVault
=====================================

.. warning::

   OpenMediaVault **不支持** 在 Raspberry Pi OS 桌面版上安装。

   请确保您已安装正确的操作系统并完成网络配置。
   此处的操作流程与 :ref:`install_os_sd_rpi` 一致，但在选择镜像时，请从 Raspberry Pi OS（其他）中选择 Raspberry Pi OS Lite。

   .. image:: img/omv/omv-install-1.png

OpenMediaVault（简称 OMV）是一个基于 Debian Linux 的开源网络附加存储（NAS）操作系统，专为家庭用户和小型办公室环境设计，旨在简化存储管理并提供丰富的网络服务功能。

请按照以下步骤在 Raspberry Pi 上安装 OpenMediaVault：

1. 使用 SSH 连接到 Raspberry Pi
-----------------------------------------------------------

   在终端中输入以下命令：

   .. code-block:: bash

      ssh pi@raspberrypi.local

   如果您使用的是 Windows，请使用 PuTTY 或其他 SSH 客户端连接至 Raspberry Pi。

2. 安装 OpenMediaVault
----------------------------

   在终端中输入以下命令：

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   上述命令将下载并运行 OpenMediaVault 的安装脚本。安装完成后请勿重启 Raspberry Pi。

3. 访问 OpenMediaVault
-----------------------------

   在浏览器中输入以下地址访问 OpenMediaVault：

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: 如果无法访问上述地址，请尝试使用 IP 地址，例如：http://192.168.1.100。

   您将看到登录页面，请使用默认用户名和密码登录。默认用户名为 ``admin``，密码为 ``openmediavault``。

   .. image:: img/omv/omv-login.png

   登录后，您将进入 OpenMediaVault 的主界面。

   .. image:: img/omv/omv-main.png

   至此，您已成功安装并访问了 OpenMediaVault，可以开始配置和管理您的存储设备了。


4. 设置 RAID（可选）
---------------------------------------

   NVMe RAID 是一种将多个 NVMe 固态硬盘（SSD）通过 RAID 技术组合的存储方案，旨在兼顾 NVMe 协议的高速性能与 RAID 的冗余保护或性能增强功能。常见模式包括 RAID 0、1、5、10 等。对于双 NVMe SSD，最常用的是 RAID 0 和 RAID 1。

   * RAID 0 是一种条带化技术，将数据划分为多个条带并分布存储到多个硬盘中，从而提升读写速度。但 RAID 0 不具备冗余功能，任何一块硬盘损坏都会导致数据全部丢失。

   * RAID 1 是一种镜像技术，将数据复制到多块硬盘上，实现数据冗余保护。RAID 1 的读写速度取决于单块硬盘的速度。若某块硬盘损坏，其他硬盘仍可提供数据。

   .. note:: 配置 RAID 0 或 RAID 1 至少需要挂载两块硬盘。RAID 0 的容量为所有硬盘容量之和；RAID 1 的容量等于最小硬盘的容量。

   1. 在 ``System`` 菜单中点击 ``Plugins``，搜索并安装 ``openmediavault-md`` 插件。

   .. image:: img/omv/omv-raid-1.png

   2. 在 ``Storage`` 菜单中点击 ``Disks``，清除两块 SSD 数据。
   
   .. image:: img/omv/omv-raid-2.png

   3. 请注意，此操作将清除硬盘上的所有数据，请确保您已备份所有重要文件。

   .. image:: img/omv/omv-raid-3.png

   4. 擦除模式选择 ``QUICK`` 即可。

   .. image:: img/omv/omv-raid-4.png

   5. 进入 ``Multiple Device`` 标签页，点击 ``Create`` 创建新 RAID 设备。

   .. image:: img/omv/omv-raid-5.png

   6. 在 Level 选项中选择 Stripe（RAID 0）或 Mirror（RAID 1），在 Devices 中选择刚刚擦除的硬盘，点击 ``Save`` 并等待 RAID 配置完成。

   .. image:: img/omv/omv-raid-6.png

   .. note:: 若弹出错误提示（500 - Internal Server Error），请尝试重启 OMV 系统。

   7. 点击 ``Apply`` 应用配置。

   .. image:: img/omv/omv-raid-7.png

   8. RAID 配置完成后，请等待 RAID 状态显示为 ``100%``。

   .. image:: img/omv/omv-raid-8.png

   9. 此时，您的硬盘已成功配置为 RAID 0 或 RAID 1，可作为一个统一的存储设备使用。

5. 配置存储设备
-----------------------

   在 OpenMediaVault 主界面中，点击左侧菜单的 ``Storage``。在 ``Storage`` 页面中点击 ``Disks`` 标签页，您将看到所有已连接至 Raspberry Pi 的硬盘。确保您的 NVMe 扩展板已连接硬盘。

   .. image:: img/omv/omv-disk.png

   1. 在侧边栏点击 ``File System``，然后创建并挂载文件系统。文件系统类型请选择 ``ext4``。

   .. image:: img/omv/omv-mount.png

   2. 选择设备并点击保存。 
   
   .. note:: 如果您已设置 RAID，将在设备列表中看到 RAID 设备，选择并保存即可。

   .. image:: img/omv/omv-mount-2.png

   3. 弹出窗口提示正在创建文件系统，请稍等片刻。

   .. image:: img/omv/omv-mount-3.png

   4. 创建完成后进入 ``Mount`` 页面，选择刚刚创建的文件系统并将其挂载到 Raspberry Pi 上。

   .. image:: img/omv/omv-mount-4.png

   .. note:: 如果使用的是两块硬盘但未设置 RAID，需重复以上步骤挂载第二块硬盘。

   5. 挂载完成后点击 ``Apply``，然后您就可以在文件系统中看到硬盘数据。

   .. image:: img/omv/omv-mount-5.png

   至此，您已成功配置 OpenMediaVault 并挂载了硬盘，可使用其进行存储管理。


6. 创建共享文件夹
---------------------------------------

   1. 在 ``Storage`` 页面点击 ``Shared Folders`` 标签页，然后点击 ``Create`` 按钮。

   .. image:: img/omv/omv-share-1.png

   2. 在 ``Create Shared Folder`` 页面输入文件夹名称，选择要共享的硬盘、共享路径，并设置权限，点击 ``Save`` 保存。

   .. image:: img/omv/omv-share-2.png

   3. 现在您可以看到刚刚创建的共享文件夹，确认无误后点击 ``Apply``。

   .. image:: img/omv/omv-share-3.png

   至此，共享文件夹创建完成。


7. 创建新用户
---------------------------------------

   若需访问该文件夹，需要先创建一个新用户，请按以下步骤操作：

   1. 在 ``User`` 页面点击 ``Create`` 按钮。

   .. image:: img/omv/omv-user-1.png

   2. 在 ``Create User`` 页面输入用户名和密码，点击 ``Save`` 保存。

   .. image:: img/omv/omv-user-2.png

   新用户创建成功。


8. 设置新用户权限
---------------------------------------

   1. 在 ``Shared Folders`` 页面点击刚刚创建的共享文件夹，接着点击 ``Permissions`` 按钮。

   .. image:: img/omv/omv-user-3.png

   2. 在 ``Permissions`` 页面中设置权限，然后点击 ``Save`` 保存。

   .. image:: img/omv/omv-user-4.png

   3. 点击 ``Apply`` 应用配置。

   .. image:: img/omv/omv-user-5.png

   现在，您可以使用新创建的用户访问共享文件夹了。


9. 配置 SMB 服务
---------------------------------------

   1. 在 ``Services`` 页面找到 ``SMB/CIFS`` > ``Setting`` 标签页，勾选 ``Enable``，然后点击 ``Save``。

   .. image:: img/omv/omv-smb-1.png

   2. 点击 ``Apply`` 应用更改。

   .. image:: img/omv/omv-smb-2.png

   3. 进入 ``Shares`` 页面，点击 ``Create``。

   .. image:: img/omv/omv-smb-3.png

   4. 在 ``Create Share`` 页面选择共享文件夹路径，然后点击 ``Save`` 保存。此页面还有许多可根据需求配置的选项。

   .. image:: img/omv/omv-smb-4.png

   5. 点击 ``Apply``。

   .. image:: img/omv/omv-smb-5.png

   SMB 服务配置完成，您现在可以通过 SMB 协议访问共享文件夹。


10. 在 Windows 上访问共享文件夹
---------------------------------------

   1. 打开 ``此电脑``，点击 ``映射网络驱动器``。

   .. image:: img/omv/omv-network-location-1.png

   2. 在弹出窗口中，在 ``文件夹`` 一栏输入 Raspberry Pi 的 IP 地址，例如 ``\\192.168.1.100\``，或主机名，例如 ``\\pi.local\``。

   .. image:: img/omv/omv-network-location-2.png

   3. 点击浏览按钮，选择要访问的共享文件夹。此过程中需要输入之前创建的用户名和密码。

   .. image:: img/omv/omv-network-location-3.png

   4. 勾选“登录时重新连接”，然后点击 ``完成``。

   .. image:: img/omv/omv-network-location-4.png
   
   5. 您现在可以访问 NAS 上的共享文件夹了。

   .. image:: img/omv/omv-network-location-5.png

10. 在 Mac 上访问共享文件夹
-------------------------------------

   1. 在 ``前往`` 菜单中点击 ``连接服务器``。

   .. image:: img/omv/omv-mac-1.png

   2. 在弹出的窗口中输入 Raspberry Pi 的 IP 地址，例如 ``smb://192.168.1.100``，或主机名，例如 ``smb://pi.local``。

   .. image:: img/omv/omv-mac-2.png

   3. 点击 ``连接`` 按钮。

   .. image:: img/omv/omv-mac-3.png

   4. 在弹出窗口中输入之前创建的用户名和密码，点击 ``连接``。

   .. image:: img/omv/omv-mac-4.png

   5. 您现在可以访问 NAS 上的共享文件夹了。

   .. image:: img/omv/omv-mac-5.png
