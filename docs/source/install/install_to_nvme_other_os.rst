.. _install_to_nvme_home_bridge: 

在NVMe SSD上安装操作系统
============================================

如果你使用的是NVMe SSD，并且有适配器将其连接到电脑进行系统安装，可以按照以下教程进行快速安装。

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**所需组件**

* 一台个人电脑
* 一块NVMe SSD
* 一个NVMe转USB适配器
* 一张Micro SD卡和读卡器

.. _update_bootloader:

1. 更新启动引导程序
----------------------------------

首先，你需要更新Raspberry Pi 5的启动引导程序，使其能够优先从NVMe启动，然后再尝试USB和SD卡。

.. 
   .. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    在此步骤中，建议使用备用的Micro SD卡。首先将引导程序写入此Micro SD卡，然后立即将其插入Raspberry Pi，以启用从NVMe设备启动。
    
    另外，你也可以直接将引导程序写入NVMe设备，然后将其插入Raspberry Pi，修改启动方式。之后，将NVMe SSD连接到电脑安装操作系统，安装完成后，再将其插回Raspberry Pi。

#. 使用读卡器将备用的Micro SD卡或NVMe SSD插入到你的电脑或笔记本中。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi设备** ，并从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.jpg
      :width: 90%
      
#. 在 **操作系统** 选项卡中，向下滚动并选择 **Misc utility images** 。

   .. image:: img/nvme_misc.png
      :width: 90%

#. 选择 **Bootloader (Pi 5 family)** 。

   .. image:: img/nvme_bootloader.jpg
      :width: 90%


#. 选择 **NVMe/USB Boot**，使Raspberry Pi 5能够从NVMe启动，然后再尝试USB和SD卡。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. 在 **存储** 选项中，选择适合安装的存储设备。

   .. note::

      确保选择正确的存储设备。为避免混淆，如果连接了多个存储设备，建议断开其他设备。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. 现在你可以点击 **下一步** 。如果存储设备中已有数据，请确保备份，以防数据丢失。如果不需要备份，可以点击 **是** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 很快，你会看到提示，表示 **NVMe/USB Boot** 已成功写入存储设备。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 现在，你可以将Micro SD卡或NVMe SSD插入Raspberry Pi。为Raspberry Pi提供电源，使用Type C适配器，Micro SD卡或NVMe SSD上的引导程序将被写入Raspberry Pi的EEPROM。

.. note::

    之后，Raspberry Pi将从NVMe启动，然后再尝试USB和SD卡。
    
    关闭Raspberry Pi并移除Micro SD卡或NVMe SSD。


2. 将操作系统安装到NVMe SSD
---------------------------------

现在你可以将操作系统安装到NVMe SSD上。

**步骤**

#. 使用读卡器将SD卡插入电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi设备**，并从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.jpg
      :width: 90%


#. 点击 **操作系统** 选项卡。

   .. image:: img/os_choose_os.jpg
      :width: 90%

#. 向下滚动到页面底部并选择你要安装的操作系统。

   .. note::

      * 对于 **Ubuntu** 系统，点击 **其他通用操作系统** -> **Ubuntu**，并选择 **Ubuntu Desktop 24.04 LTS (64位)** 或 **Ubuntu Server 24.04 LTS (64位)**。
      * 对于 **Kali Linux** 、 **Home Assistant** 和 **Homebridge** 系统，点击 **其他特定用途操作系统** ，然后选择相应的系统。

   .. image:: img/os_other_os.png
      :width: 90%

#. 在 **存储** 选项中，选择适合安装的存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**。

   .. note::

      * 对于无法预先配置的系统，点击 **NEXT** 后，系统会提示是否保存设备中的数据。如果你确认已备份，请选择 **是**。

      * 对于可以预先配置主机名、WiFi和启用SSH的系统，弹出窗口会询问是否应用操作系统的自定义设置。你可以选择 **是** 或 **否**，或者返回编辑。

   .. image:: img/os_enter_setting.jpg
      :width: 90%


   * 为你的Raspberry Pi定义一个 **主机名**。主机名是你Raspberry Pi在网络中的标识符。你可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问你的Pi。

     .. image:: img/os_set_hostname.jpg

   * 为Raspberry Pi的管理员账户创建一个 **用户名** 和 **密码**。为Raspberry Pi设置唯一的用户名和密码非常重要，因为默认情况下没有密码。

     .. image:: img/os_set_username.jpg

   * 配置无线局域网，提供你网络的 **热点名** 和 **密码**。

     .. note::

       将 ``无线局域网国家/Wireless LAN country`` 设置为与你所在地区对应的两字母 `ISO/IEC alpha2代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ 。

     .. image:: img/os_set_wifi.jpg
         
   * 为了远程连接到你的Raspberry Pi，在服务选项卡中启用SSH。

     * 对于 **密码认证** ，使用常规选项卡中的用户名和密码。
     * 对于公钥认证，选择“仅允许公钥认证”。如果你有RSA密钥，它将被使用。如果没有，点击“运行SSH-keygen”生成一个新的密钥对。

     .. image:: img/os_enable_ssh.png

   * **选项** 菜单允许你配置Imager在写入过程中的行为，包括写入完成时播放声音、写入完成时弹出媒体和启用遥测。

     .. image:: img/os_options.png



#. 完成操作系统自定义设置后，点击 **保存/Save** 以保存你的设置。然后点击 **是** ，在写入镜像时应用这些设置。

   .. image:: img/os_click_yes.jpg
      :width: 90%


#. 如果NVMe SSD上已有数据，请确保备份，以防数据丢失。如果不需要备份，可以点击 **是** 继续。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 当你看到“写入成功”的弹窗时，说明镜像已经完全写入并验证完成。现在，你可以从NVMe SSD启动Raspberry Pi了！
