.. _copy_sd_to_nvme_rpi:

将操作系统从Micro SD卡复制到NVMe SSD
==================================================================

如果你有一个NVMe SSD，但没有适配器将其连接到电脑，你可以选择第三种方法：首先在Micro SD卡上安装操作系统。Raspberry Pi 5成功启动后，你可以将系统从Micro SD卡转移到NVMe SSD。

* 首先，你需要 :ref:`install_os_sd_rpi` 。
* 然后，启动并登录到你的Raspberry Pi。如果你不确定如何登录，可以访问Raspberry Pi官方网站： |link_rpi_get_start| 。

在继续以下步骤之前，请完成上述步骤。


1. 启用PCIe
--------------------

默认情况下，PCIe连接器是未启用的。

* 要启用PCIe连接器，你需要打开 ``/boot/firmware/config.txt`` 文件。

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt

* 然后，在文件中添加以下行。

  .. code-block:: shell
  
    # 启用PCIe外部连接器
    dtparam=pciex1
  
* ``pciex1`` 有一个更容易记住的别名，你也可以选择在 ``/boot/firmware/config.txt`` 文件中添加 ``dtparam=nvme`` 。

  .. code-block:: shell
  
    dtparam=nvme

* 该连接已认证支持Gen 2.0速度（5 GT/sec），但如果你希望强制使用Gen 3.0（10 GT/sec），可以在 ``/boot/firmware/config.txt`` 文件中添加以下行。

  .. code-block:: shell
  
    # 强制使用Gen 3.0速度
    dtparam=pciex1_gen=3
  
  .. warning::

    Raspberry Pi 5不支持Gen 3.0速度，使用这些速度连接到PCIe设备可能会不稳定。

* 按 ``Ctrl + X`` ，然后按 ``Y`` 保存更改并按 ``Enter`` 退出。


2. 在SSD上安装操作系统
----------------------------------------

有两种方法可以在SSD上安装操作系统：

**将系统从Micro SD卡复制到SSD**

#. 连接显示器或通过VNC Viewer访问Raspberry Pi桌面。然后点击 **Raspberry Pi图标** -> **Accessories/附件** -> **SD Card Copier/SD卡复制工具**。

   .. image:: img/ssd_copy.png
      

#. 确保选择正确的 **复制来源** 和 **复制目标** 设备。小心不要弄错。

   .. image:: img/ssd_copy_from.png
      
#. 记得选择“新分区UUID”，以确保系统能够正确区分设备，避免挂载冲突和启动问题。

   .. image:: img/ssd_copy_uuid.png

#. 选择后，点击 **开始** 。

   .. image:: img/ssd_copy_click_start.png

#. 系统会提示你SSD上的内容将被清除。在点击“是”之前，请确保备份好数据。

   .. image:: img/ssd_copy_erase.png

#. 等待一段时间，复制过程完成。


**使用Raspberry Pi Imager安装系统**

如果你的Micro SD卡上已经安装了桌面版的操作系统，可以使用镜像工具（如Raspberry Pi Imager）将系统烧录到SSD上。本例使用的是Raspberry Pi OS bookworm，但其他系统可能需要先安装镜像工具。

#. 连接显示器或通过VNC Viewer访问Raspberry Pi桌面。然后点击 **Raspberry Pi图标** -> **附件** -> **Imager**。

   .. image:: img/ssd_imager.png


#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi设备** ，从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/ssd_pi5.jpg
      :width: 90%


#. 选择 **操作系统** 并选择推荐的操作系统版本。

   .. image:: img/ssd_os.jpg
      :width: 90%

#. 在 **存储** 选项中，选择插入的NVMe SSD。

   .. image:: img/nvme_storage.png
      :width: 90%

#. 点击 **下一步** ，然后点击 **编辑设置** 以自定义操作系统设置。

   .. note::

      如果你有显示器，可以跳过接下来的步骤，点击“是”开始安装。其他设置可以在显示器上稍后调整。

   .. image:: img/os_enter_setting.jpg
      :width: 90%

#. 为Raspberry Pi定义一个 **主机名** 。

   .. note::

      主机名是你Raspberry Pi的网络标识符。你可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问你的Pi。

   .. image:: img/os_set_hostname.jpg


#. 为Raspberry Pi的管理员账户创建一个 **Username** 和 **密码** 。

   .. note::

      设置唯一的用户名和密码对于保护你的Raspberry Pi至关重要，因为默认情况下没有密码。

   .. image:: img/os_set_username.jpg


#. 配置无线局域网，提供你网络的 **用户名** 和 **密码** 。

   .. note::

      将 ``无线局域网国家/Wireless LAN country`` 设置为与你所在地区对应的两字母 `ISO/IEC alpha2代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ 。

   .. image:: img/os_set_wifi.jpg

#. 为了远程连接到你的Raspberry Pi，在服务选项卡中启用SSH。

   * 对于 **密码认证/password authentication** ，使用 **General/常规** 选项卡中的用户名和密码。
   * 对于公钥认证，选择“仅允许公钥认证”。如果你有RSA密钥，它将被使用。如果没有，点击“运行SSH-keygen”生成一个新的密钥对。

   .. image:: img/os_enable_ssh.png



#. **选项** 菜单允许你配置Imager在写入过程中行为，包括写入完成时播放声音、写入完成时弹出媒体和启用遥测。

   .. image:: img/os_options.png

# 完成操作系统自定义设置后，点击 **保存** 以保存你的设置。然后点击 **是** ，在写入镜像时应用这些设置。

   .. image:: img/os_click_yes.jpg
      :width: 90%

#. 如果NVMe SSD上已有数据，请确保备份，以防数据丢失。如果不需要备份，可以点击 **是** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%

#. 当你看到“写入成功”的弹窗时，说明镜像已经完全写入并验证完成。现在，你可以从NVMe SSD启动Raspberry Pi了！

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _configure_boot_ssd:

3. 配置从SSD启动
---------------------------------------

在本节中，我们将配置你的Raspberry Pi直接从NVMe SSD启动，这样可以提供比SD卡更快的启动速度和更好的性能。请按照以下步骤操作：

#. 首先，在Raspberry Pi上打开终端，并运行以下命令进入配置界面：

   .. code-block:: shell

      sudo raspi-config

#. 在 ``raspi-config`` 菜单中，使用箭头键导航并选择 **高级选项/Advanced Options**。按 ``Enter`` 进入高级设置。

   .. image:: img/nvme_open_config.png

#. 在 **高级选项/Advanced Options** 中，选择 **启动顺序/Boot Order** 。这个设置允许你指定Raspberry Pi查找启动设备的顺序。

   .. image:: img/nvme_boot_order.png

#. 然后，选择 **NVMe/USB启动** 。这告诉Raspberry Pi优先从USB连接的SSD或NVMe驱动器启动，而不是从SD卡启动。

   .. image:: img/nvme_boot_nvme.png

#. 选择启动顺序后，按 **完成** 退出raspi-config。你也可以使用 **Esc** 键关闭配置工具。

   .. image:: img/nvme_boot_ok.png

#. 要应用新的启动设置，重新启动你的Raspberry Pi，运行 ``sudo reboot`` 。

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

重新启动后，Raspberry Pi应当从连接的NVMe SSD启动，为你的系统提供更高的性能和更好的耐用性。


