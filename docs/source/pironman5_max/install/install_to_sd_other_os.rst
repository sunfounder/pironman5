.. _max_install_to_sd_home_bridge:

在 Micro SD 卡上安装操作系统
=============================================

如果您使用的是 Micro SD 卡，可以按照以下教程将系统安装到 Micro SD 卡中。


**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡及读卡器

**操作步骤**

#. 使用读卡器将 Micro SD 卡插入您的电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device**，从下拉列表中选择 **Raspberry Pi 5** 模型。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. 点击 **Operating System** 选项卡。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 向下滚动页面至底部，选择您需要的操作系统。

   .. note::

      * 若选择 **Ubuntu** 系统，请点击 **Other general-purpose OS** -> **Ubuntu**，然后选择 **Ubuntu Desktop 24.04 LTS (64 bit)** 或 **Ubuntu Server 24.04 LTS (64 bit)**。
      * 若选择 **Kali Linux**、 **Home Assistant** 或 **Homebridge** 系统，请点击 **Other specific-purpose OS**，然后选择对应系统。

   .. image:: img/os_other_os.png
      :width: 90%

#. 在 **Storage** 选项中，选择用于安装的目标存储设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**。

   .. note::

      * 对于无法预先配置的系统，点击 **NEXT** 后将提示是否保留设备中的数据。若已完成备份，请选择 **Yes**。
      * 对于支持预设主机名、WiFi 和 SSH 配置的系统，会弹出提示是否应用这些设置，您可以选择 **Yes**、 **No**，或返回进一步编辑。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置您的树莓派 **hostname**。hostname 是树莓派在网络中的标识，可通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问。

     .. image:: img/os_set_hostname.png  

   * 创建树莓派管理员账户的 **Username** 和 **Password**。为系统安全起见，请设置一个唯一的用户名和密码，因为默认并不包含密码。

     .. image:: img/os_set_username.png
         
   * 配置无线网络，输入您网络的 **SSID** 和 **Password**。

     .. note::

        请将 ``Wireless LAN country`` 设置为您所在地区对应的两字母 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png
         
   * 若需远程连接树莓派，请在 Services 标签页中启用 SSH。

     * 若使用 **密码认证**，则使用 General 标签页中设置的用户名与密码。
     * 若使用 **公钥认证**，请选择 "Allow public-key authentication only"。若已有 RSA 密钥将直接使用，若没有可点击 "Run SSH-keygen" 自动生成新密钥对。

     .. image:: img/os_enable_ssh.png
         
   * 在 **Options** 菜单中可配置写入时的行为，例如写入完成时播放提示音、弹出介质以及启用遥测功能。

     .. image:: img/os_options.png

#. 完成所有系统自定义设置后，点击 **Save** 保存配置。然后点击 **Yes** 应用设置并写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 若 SD 卡中已有数据，请确保提前备份。确认无备份需求后，点击 **Yes** 开始写入。

   .. image:: img/os_continue.png
      :width: 90%


#. 当您看到 “Write Successful” 的弹窗时，说明镜像已成功写入并完成校验。现在，您已准备好使用这张 Micro SD 卡启动树莓派！
