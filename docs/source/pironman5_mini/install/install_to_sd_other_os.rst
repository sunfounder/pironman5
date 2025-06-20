.. _install_to_sd_home_bridge_mini:

将操作系统安装到 Micro SD 卡
=============================================

如果您打算使用 Micro SD 卡安装系统，可参考以下教程将操作系统写入 Micro SD 卡。


**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡及读卡器

**操作步骤**

#. 使用读卡器将 SD 卡插入您的电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device**，并从下拉列表中选择 **Raspberry Pi 5** 机型。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. 点击 **Operating System** 选项卡。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 滚动至页面底部，选择您所需的操作系统。

   .. note::

      * 若选择 **Ubuntu** 系统，请点击 **Other general-purpose OS** -> **Ubuntu**，然后选择 **Ubuntu Desktop 24.04 LTS (64 bit)** 或 **Ubuntu Server 24.04 LTS (64 bit)**。
      * 若选择 **Kali Linux**、 **Home Assistant** 或 **Homebridge** 系统，请点击 **Other specific-purpose OS**，然后选择相应系统。

   .. image:: img/os_other_os.png
      :width: 90%

#. 在 **Storage** 选项中，选择正确的安装设备。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. 点击 **NEXT**。

   .. note::

      * 若所选系统不支持提前配置，点击 **NEXT** 后会提示是否擦除设备数据。确认已完成备份后点击 **Yes**。

      * 若系统支持预设主机名、WiFi 和 SSH 配置，将弹出窗口询问是否应用自定义设置。您可选择 **Yes**、 **No** 或返回继续编辑。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置您的树莓派 **hostname**，作为设备在网络中的标识。您可通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问设备。

     .. image:: img/os_set_hostname.png

   * 创建树莓派的 **用户名** 和 **密码**。建议设定专属账户信息，以提高系统安全性（树莓派默认无密码）。

     .. image:: img/os_set_username.png

   * 配置无线网络，填写 WiFi 的 **SSID** 和 **密码**。

     .. note::

        请将 ``Wireless LAN country`` 设置为您所在国家的 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png

   * 若需远程连接树莓派，请在 Services 标签页中启用 SSH 服务。

     * 使用 **密码验证** 时，请输入您在 General 标签中设定的用户名和密码。
     * 使用 **公钥验证** 时，选择 “Allow public-key authentication only”。若已有 RSA 密钥，将直接使用；否则点击 “Run SSH-keygen” 生成新密钥对。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 菜单中，您可设置写入完成后的行为，如播放提示音、自动弹出设备、启用遥测等。

     .. image:: img/os_options.png

#. 设置完成后，点击 **Save** 保存设置，再点击 **Yes** 以在写入镜像时应用这些设置。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 如果 SD 卡中已有数据，请确认是否备份。若无备份需求，可点击 **Yes** 继续写入。

   .. image:: img/os_continue.png
      :width: 90%


#. 当看到 “Write Successful” 的提示窗口时，说明系统镜像已成功写入并验证完毕。现在您可以使用这张 Micro SD 卡启动树莓派了！
