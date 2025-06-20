.. _install_os_sd_rpi_mini:

将操作系统安装到 Micro SD 卡
============================================================

**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡及读卡器

**安装步骤**

#. 使用读卡器将 SD 卡插入您的电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device**，从下拉列表中选择 **Raspberry Pi 5** 机型。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 选择 **Operating System**，并推荐使用官方推荐的操作系统版本。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 点击 **Choose Storage**，选择正确的存储设备进行安装。

   .. image:: img/os_choose_sd.png
      :width: 90%

#. 点击 **NEXT**，然后点击 **EDIT SETTINGS** 自定义系统设置。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置您的树莓派 **hostname**，作为网络中的标识。您可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问设备。

     .. image:: img/os_set_hostname.png


   * 创建树莓派的 **用户名** 和 **密码**。为系统设置独立的账户信息，有助于提升安全性，因为默认系统没有密码。

     .. image:: img/os_set_username.png

   * 配置无线网络，输入 WiFi 的 **SSID** 和 **密码**。

     .. note::

        请将 ``Wireless LAN country`` 设置为您所在地区对应的两位字母 `ISO/IEC alpha2 代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png


   * 若需远程连接树莓派，请在 Services 标签页中启用 SSH 服务：

     * 使用 **密码认证** 时，请输入您在 General 标签页设置的用户名和密码；
     * 使用 **公钥认证** 时，选择 “Allow public-key authentication only”。如已存在 RSA 密钥则直接使用，如无则点击 “Run SSH-keygen” 生成新密钥对。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 菜单中，您可以设置写入完成后的行为，例如完成后播放提示音、自动弹出介质、启用遥测等。

     .. image:: img/os_options.png

#. 完成操作系统的自定义设置后，点击 **Save** 保存设置，然后点击 **Yes** 应用这些设置并开始写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 若 SD 卡中已有数据，请务必提前备份以避免数据丢失。确认无需备份后，点击 **Yes** 继续写入。

   .. image:: img/os_continue.png
      :width: 90%


#. 当出现 “Write Successful” 弹窗时，表示镜像已成功写入并完成验证。您现在可以使用这张 Micro SD 卡启动树莓派了！

   .. image:: img/os_finish.png
      :width: 90%
