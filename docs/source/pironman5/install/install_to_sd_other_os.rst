.. _install_to_sd_home_bridge:

在 Micro SD 卡上安装操作系统
=============================================

如果您打算使用 Micro SD 卡安装系统，可以按照以下教程将系统写入 Micro SD 卡。


**Required Components**

* 一台个人电脑
* 一张 Micro SD 卡及其读卡器

**Steps**

#. 使用读卡器将 SD 卡插入您的电脑或笔记本。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi Device**，并从下拉列表中选择 **Raspberry Pi 5** 模型。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. 点击 **Operating System** 选项卡。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动至页面底部，选择您要安装的操作系统。

   .. note::

      * 如需安装 **Ubuntu** 系统，请点击 **Other general-purpose OS** -> **Ubuntu**，然后选择 **Ubuntu Desktop 24.04 LTS (64 bit)** 或 **Ubuntu Server 24.04 LTS (64 bit)**。
      * 如需安装 **Kali Linux**、 **Home Assistant** 或 **Homebridge** 系统，请点击 **Other specific-purpose OS**，然后选择对应的系统。

   .. image:: img/os_other_os.png
      :width: 90%

#. 在 **Storage** 选项中，选择正确的存储设备用于安装。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**。

   .. note::

      * 对于无法预设配置的系统，点击 **NEXT** 后会提示您是否保留设备中的数据。若已确认完成备份，可点击 **Yes** 继续操作。

      * 对于可以预设 Hostname、WiFi 和启用 SSH 的系统，会弹出窗口提示是否应用操作系统的自定义设置。您可以选择 **Yes**、 **No**，或返回进一步编辑。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置 Raspberry Pi 的 **hostname**。这是设备在网络中的标识，您可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问该设备。

     .. image:: img/os_set_hostname.png

   * 创建用于管理员账户的 **Username** 和 **Password**。由于系统默认不设置密码，建议您设置唯一的用户名和密码以确保系统安全。

     .. image:: img/os_set_username.png

   * 配置无线网络，填写您的网络 **SSID** 和 **Password**。

     .. note::

       请根据您所在地设置 ``Wireless LAN country``，使用对应的两个字母 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png

   * 若需远程连接 Raspberry Pi，可在 Services 标签页启用 SSH 功能。

     * 若使用 **密码验证**，请使用 General 标签页中设置的用户名和密码。
     * 若使用公钥验证，选择 "Allow public-key authentication only"。若已有 RSA 密钥将自动使用，否则点击 "Run SSH-keygen" 生成新的密钥对。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 菜单中，您可以设置写入过程中的行为，例如完成后播放声音、自动弹出介质以及启用遥测功能。

     .. image:: img/os_options.png

#. 完成所有操作系统自定义设置后，点击 **Save** 保存配置。然后点击 **Yes** 以便在写入镜像时应用设置。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 如果 SD 卡中已有数据，请确保提前备份以防数据丢失。如果无需备份，可点击 **Yes** 继续。

   .. image:: img/os_continue.png
      :width: 90%


#. 当您看到 “Write Successful” 的提示弹窗时，说明系统镜像已经成功写入并完成验证。现在，您可以使用这张 Micro SD 卡启动 Raspberry Pi！
