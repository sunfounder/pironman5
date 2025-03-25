.. _install_to_nvme_rpi:

在NVMe SSD上安装操作系统
===================================

如果你使用的是NVMe SSD，并且有适配器将其连接到电脑进行系统安装，你可以按照以下教程快速安装操作系统。

**所需组件**

* 一台个人电脑
* 一个NVMe SSD
* 一个NVMe转USB适配器
* 一张Micro SD卡和读卡器

.. _update_bootloader:

1. 更新启动引导程序
--------------------------------

首先，你需要更新Raspberry Pi 5的启动引导程序，使其能够从NVMe启动，然后再尝试USB和SD卡。

.. 
   .. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    在此步骤中，建议使用备用的Micro SD卡。首先将引导程序写入该Micro SD卡，然后立即将其插入Raspberry Pi，以启用从NVMe设备启动。
    
    另外，你也可以直接将引导程序写入NVMe设备，然后将其插入Raspberry Pi以更改启动方式。之后，连接NVMe SSD到电脑进行操作系统安装，安装完成后，将其重新插回Raspberry Pi。

#. 使用读卡器将备用的Micro SD卡或NVMe SSD插入到你的电脑或笔记本中。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi设备** ，并从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.jpg
      :width: 90%

#. 在 **操作系统** 选项卡中，向下滚动并选择 **Misc utility images** 。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)**。

   .. image:: img/nvme_bootloader.jpg
      :width: 90%


#. 选择 **NVMe/USB Boot** ，使Raspberry Pi 5能够从NVMe启动，然后再尝试USB和SD卡。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **存储** 选项中，选择适合安装的存储设备。

   .. note::

      确保选择正确的存储设备。如果连接了多个存储设备，为避免混淆，建议断开其他设备。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在你可以点击 **NEXT** 。如果存储设备中已有数据，请确保备份以防数据丢失。如果不需要备份，可以点击 **是** 继续。


   .. image:: img/os_continue.png
      :width: 90%

#. 很快，你将看到提示，显示 **NVMe/USB Boot** 已经写入存储设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 现在，你可以将Micro SD卡或NVMe SSD插入到Raspberry Pi中。为Raspberry Pi提供电源，使用Type C适配器，Micro SD卡或NVMe SSD上的引导程序将被写入Raspberry Pi的EEPROM。

.. note::

    之后，Raspberry Pi将从NVMe启动，然后再尝试USB和SD卡。
    
    关闭Raspberry Pi并移除Micro SD卡或NVMe SSD。


2. 将操作系统安装到NVMe SSD
-----------------------------------

现在你可以将操作系统安装到NVMe SSD上。


#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi设备** ，并从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.jpg
      :width: 90%

#. 选择 **操作系统** 并选择推荐的操作系统版本。

   .. image:: img/os_choose_os.jpg
      :width: 90%


#. 在 **存储** 选项中，选择适合安装的存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT** ，然后点击 **编辑设置** 以自定义你的操作系统设置。

   .. image:: img/os_enter_setting.jpg
      :width: 90%


   * 为你的Raspberry Pi定义一个 **主机名** 。主机名是你的Raspberry Pi在网络中的标识符。你可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问你的Pi。

     .. image:: img/os_set_hostname.jpg

   * 为Raspberry Pi的管理员账户创建一个 **用户名** 和 **密码**。设置唯一的用户名和密码对于保护你的Raspberry Pi至关重要，因为默认情况下没有密码。

     .. image:: img/os_set_username.jpg

   * 配置无线局域网，提供你网络的 **SSID** 和 **密码**。

     .. note::

       将 ``无线局域网国家/Wireless LAN country`` 设置为与你所在地区对应的两字母 `ISO/IEC alpha2代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.jpg

   * 要远程连接到你的Raspberry Pi，在服务选项卡中启用SSH。

     * 对于 **密码认证** ，使用常规选项卡中的用户名和密码。
     * 对于公钥认证，选择“仅允许公钥认证”。如果你有RSA密钥，它将被使用。如果没有，点击“运行SSH-keygen”生成一个新的密钥对。

     .. image:: img/os_enable_ssh.png

   * **选项** 菜单让你配置Imager在写入过程中行为，包括写入完成时播放声音、写入完成时弹出媒体和启用遥测。

     .. image:: img/os_options.png

#. 完成操作系统自定义设置后，点击 **保存/Save** 以保存自定义内容。然后点击 **是** 以在写入镜像时应用这些设置。

   .. image:: img/os_click_yes.jpg
      :width: 90%


#. 如果NVMe SSD上已有数据，请确保备份以防数据丢失。如果不需要备份，可以点击 **是** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当你看到“写入成功”的弹窗时，说明镜像已经完全写入并验证完成。现在，你可以从NVMe SSD启动Raspberry Pi了！

   .. image:: img/nvme_install_finish.png
      :width: 90%
