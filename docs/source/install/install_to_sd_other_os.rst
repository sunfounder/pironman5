.. _install_to_sd_home_bridge:

在Micro SD卡上安装操作系统
=============================================

如果你使用的是Micro SD卡，可以按照下面的教程将操作系统安装到Micro SD卡上。


**所需组件**

* 一台个人电脑
* 一张Micro SD卡和一个读卡器

**步骤**

#. 将SD卡通过读卡器插入你的电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi设备** ，并从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.jpg
      :width: 90%


#. 点击 **操作系统** 选项卡。

   .. image:: img/os_choose_os.jpg
      :width: 90%

#. 向下滚动到页面底部并选择你需要的操作系统。

   .. note::

      * 对于 **Ubuntu** 系统，点击 **其他通用操作系统** -> **Ubuntu**，然后选择 **Ubuntu Desktop 24.04 LTS (64位)** 或 **Ubuntu Server 24.04 LTS (64位)**。
      * 对于 **Kali Linux** 、 **Home Assistant** 和 **Homebridge** 系统，点击 **其他特定用途操作系统**，然后选择相应的系统。

   .. image:: img/os_other_os.png
      :width: 90%

#. 在 **存储** 选项中，选择适合安装的存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **下一步** 。

   .. note::

      * 对于无法预先配置的系统，点击 **下一步** 后，会提示是否保存设备内的数据。如果你已经确认进行了备份，请选择 **是** 。

      * 对于可以预先配置主机名、WiFi和启用SSH的系统，会弹出提示是否应用操作系统的自定义设置。你可以选择 **是** 或 **否** ，或者返回进一步编辑。

   .. image:: img/os_enter_setting.jpg
      :width: 90%


   * 为你的Raspberry Pi定义一个 **主机名** 。主机名是你的Raspberry Pi在网络中的标识符。你可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问你的Pi。

     .. image:: img/os_set_hostname.jpg  

   * 为Raspberry Pi的管理员账户创建一个 **用户名** 和 **密码** 。设置唯一的用户名和密码对于保护你的Raspberry Pi至关重要，因为默认情况下没有密码。

     .. image:: img/os_set_username.jpg
         
   * 配置无线局域网，提供你网络的 **热点名** 和 **密码** 。

     .. note::

       将 ``无线局域网国家/Wireless LAN country`` 设置为与你所在地区对应的两字母 `ISO/IEC alpha2代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.jpg
         
   * 要远程连接到你的Raspberry Pi，在服务选项卡中启用SSH。

     * 对于 **密码认证**，使用常规选项卡中的用户名和密码。
     * 对于公钥认证，选择“仅允许公钥认证”。如果你有RSA密钥，它将被使用。如果没有，点击“运行SSH-keygen”生成一个新的密钥对。

     .. image:: img/os_enable_ssh.png
         
   * **选项** 菜单让你配置Imager在写入过程中行为，包括写入完成时播放声音、写入完成时弹出媒体和启用遥测。

     .. image:: img/os_options.png
            
#. 完成操作系统自定义设置后，点击 **保存** 以保存自定义内容。然后点击 **是** 以在写入镜像时应用这些设置。

   .. image:: img/os_click_yes.jpg
      :width: 90%


#. 如果SD卡上已有数据，请确保备份以防数据丢失。如果不需要备份，可以点击 **是** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 当你看到“写入成功”弹窗时，表示镜像已经完全写入并验证完成。现在你可以从Micro SD卡启动Raspberry Pi了！
