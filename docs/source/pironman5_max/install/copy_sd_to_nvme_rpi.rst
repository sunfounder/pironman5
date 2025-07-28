.. _max_copy_sd_to_nvme_rpi:

从 Micro SD 复制系统到 NVMe SSD
==================================================================

如果你拥有一块 NVMe 固态硬盘但没有转接器可将其连接至电脑，可以选择第三种方式：首先将系统安装在 Micro SD 卡中，待 Pironman 5 MAX 成功启动后，再将系统从 SD 卡复制到 NVMe SSD 上。

* 首先，请完成 :ref:`max_install_os_sd_rpi`。
* 然后启动并登录树莓派。如不确定如何登录，可参考树莓派官网：|link_rpi_get_start|。

完成以上步骤后，继续以下操作：


1. 启用 PCIe
--------------------

默认情况下，PCIe 接口未启用。

* 你需要先编辑 ``/boot/firmware/config.txt`` 文件：

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* 然后在文件末尾添加以下内容：

  .. code-block:: shell
  
    # 启用 PCIe 外部连接器
    dtparam=pciex1
  
* 你也可以使用更易记的别名 ``dtparam=nvme`` 来代替上面一行：

  .. code-block:: shell
  
    dtparam=nvme

.. * 默认连接认证支持 Gen 2.0（5 GT/sec）速率，如需强制使用 Gen 3.0（10 GT/sec）速率，可添加以下配置：

..   .. code-block:: shell
  
..     # 强制使用 PCIe Gen 3.0 速率
..     dtparam=pciex1_gen=3
  
..   .. warning::

..     树莓派 5 并未对 Gen 3.0 速率进行官方认证，部分 PCIe 设备在此速率下可能会出现不稳定情况。

* 为了让树莓派能够在启动时识别通过 PCIe Switch 连接的 NVMe 驱动器，你还需要关闭 PCIe 启动延迟。添加以下内容至 ``/boot/firmware/config.txt``：

   .. code-block:: shell

      dtparam=pciex1_no_10s=on


* 按 ``Ctrl + X``、 ``Y``，然后 ``Enter`` 保存文件。


**BOOT_ORDER**

若安装了两个 NVMe 系统盘并需要选择其中一个启动，请编辑 ``/boot/firmware/cmdline.txt`` 文件，将 ``ROOT=PARTUUID=xxxxxxxxx`` 修改为目标磁盘的 UUID。可通过以下命令查找磁盘 UUID：


.. code-block:: shell

   ls /dev/disk/by-id/


2. 在 SSD 上安装操作系统
----------------------------------------

以下两种方法可将系统安装到 SSD 上：

**从 Micro SD 卡复制系统至 SSD**

#. 连接显示器或使用 VNC Viewer 访问树莓派桌面，点击 **树莓派图标** -> **Accessories** -> **SD Card Copier**。

   .. image:: img/ssd_copy.png
      

#. 确保正确选择 **复制来源（Copy From）** 和 **复制目标（Copy To）**，切勿选错。

   .. image:: img/ssd_copy_from.png
      
#. 勾选 “NEW Partition UUIDs” 以避免设备识别冲突，确保系统正常挂载与启动。

   .. image:: img/ssd_copy_uuid.png
    
#. 确认无误后点击 **Start**。

   .. image:: img/ssd_copy_click_start.png

#. 系统会提示 SSD 数据将被清除，务必提前备份数据，再点击 Yes。

   .. image:: img/ssd_copy_erase.png

#. 稍作等待，复制过程完成。


**使用 Raspberry Pi Imager 安装系统**

若 Micro SD 卡已安装桌面版本系统，可使用 Raspberry Pi Imager 工具将系统烧录至 SSD。本例使用 Raspberry Pi OS bookworm，其它系统可能需先安装 Imager 工具。

#. 连接显示器或使用 VNC Viewer 访问树莓派桌面，点击 **树莓派图标** -> **Accessories** -> **Imager**。

   .. image:: img/ssd_imager.png


#. 在 |link_rpi_imager| 中点击 **Raspberry Pi Device**，选择 **Raspberry Pi 5** 型号。

   .. image:: img/ssd_pi5.png
      :width: 90%


#. 选择 **Operating System**，推荐使用官方推荐版本。

   .. image:: img/ssd_os.png
      :width: 90%
    
#. 在 **Storage** 选项中选择所插入的 NVMe SSD。

   .. image:: img/nvme_storage.png
      :width: 90%

#. 点击 **NEXT**，再点击 **EDIT SETTINGS** 进入系统配置。

   .. note::

      如果你连接了显示器，可直接点击 Yes 开始安装，其他设置可后续手动修改。

   .. image:: img/os_enter_setting.png
      :width: 90%

#. 设置树莓派的 **主机名（hostname）**。

   .. note::

      主机名是树莓派在网络中的标识，可通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问。

   .. image:: img/os_set_hostname.png


#. 创建用于管理员登录的 **用户名** 与 **密码**。

   .. note::

      建议使用唯一用户名与密码，以确保设备安全，树莓派默认不设密码。

   .. image:: img/os_set_username.png


#. 设置 Wi-Fi 网络的 **SSID** 与 **密码**。

   .. note::

      设置 ``Wireless LAN country`` 为你所在地区的 ISO 国家代码，例如“CN”。

   .. image:: img/os_set_wifi.png

#. 若需远程连接，请在 **Services** 中启用 **SSH**。

   * 若使用密码认证，请确保 General 中的用户名与密码设置完整；
   * 若使用公钥认证，可选择“只允许公钥认证”。如未生成公钥，可点击“Run SSH-keygen”生成一对密钥。

   .. image:: img/os_enable_ssh.png



#. 在 **Options** 菜单中可配置烧录完成后的行为，如提示音、自动弹出磁盘、启用遥测等。

   .. image:: img/os_options.png
    
#. 配置完成后点击 **Save** 保存，再点击 **Yes** 应用设置。

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. 若 NVMe SSD 中已有数据，请先备份，再点击 **Yes** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%

#. 当出现 “Write Successful” 弹窗时，说明镜像已成功写入并校验完成。此时你可以用 NVMe SSD 启动树莓派。

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _max_configure_boot_ssd:

3. 配置从 SSD 启动
---------------------------------------

本节将指导你将树莓派配置为从 NVMe SSD 启动，从而提升系统启动速度与整体性能。请依照以下步骤操作：

#. 首先，在树莓派终端中运行以下命令进入配置界面：

   .. code-block:: shell

      sudo raspi-config

#. 在 ``raspi-config`` 菜单中，使用方向键选择 **Advanced Options**，按 ``Enter`` 进入高级设置。

   .. image:: img/nvme_open_config.png

#. 进入 **Advanced Options** 后，选择 **Boot Order** 设置系统的启动优先顺序。

   .. image:: img/nvme_boot_order.png

#. 选择 **NVMe/USB boot**，表示优先从 USB 或 NVMe 启动而非 SD 卡。

   .. image:: img/nvme_boot_nvme.png

#. 设置完成后，按 **Finish** 退出配置工具，或按 **Esc** 键离开。

   .. image:: img/nvme_boot_ok.png

#. 为应用新的启动设置，请重启树莓派： ``sudo reboot`` 。

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

重启后，树莓派将尝试从所连接的 NVMe SSD 启动，为你的系统带来更高的性能与更强的耐用性。


