.. _install_os_sd_rpi:

在 Micro SD 卡上安装操作系统
============================================================
如果您打算使用 Micro SD 卡安装系统，可以参考以下教程将操作系统写入 Micro SD 卡。

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Required Components**

* 一台个人电脑
* 一张 Micro SD 卡及其读卡器

**Steps**

#. 使用读卡器将 SD 卡插入您的电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device**，在下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 选择 **Operating System**，然后选择推荐的操作系统版本。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 点击 **Choose Storage**，选择用于安装的目标存储设备。

   .. image:: img/os_choose_sd.png
      :width: 90%

#. 点击 **NEXT**，然后点击 **EDIT SETTINGS**，进行系统个性化设置。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置 Raspberry Pi 的 **hostname**，该名称是设备在网络中的唯一标识。您可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问设备。

     .. image:: img/os_set_hostname.png


   * 为 Raspberry Pi 的管理员账户创建 **Username** 和 **Password**。由于系统默认没有密码，设置独有的用户名和密码对于保障设备安全至关重要。

     .. image:: img/os_set_username.png

   * 配置无线局域网，填写您网络的 **SSID** 和 **Password**。

     .. note::

       请根据所在国家或地区设置 ``Wireless LAN country``，填写对应的两个字母 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.png


   * 如需远程连接 Raspberry Pi，请在 Services 选项卡中启用 SSH 功能。

     * 若使用 **密码验证**，请输入在 General 标签中设置的用户名和密码。
     * 若使用公钥验证，请选择 "Allow public-key authentication only"。如果已有 RSA 密钥将会自动使用，若没有，请点击 "Run SSH-keygen" 生成新的密钥对。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 菜单中，您可以设置 Imager 在写入过程中的行为，例如写入完成后播放提示音、自动弹出存储设备，以及是否启用遥测功能。

     .. image:: img/os_options.png

#. 完成操作系统的个性化设置后，点击 **Save** 保存配置。接着点击 **Yes**，在写入镜像时应用这些设置。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 如果 SD 卡中已有数据，请确保提前备份以防数据丢失。如无需备份，可直接点击 **Yes** 继续操作。

   .. image:: img/os_continue.png
      :width: 90%


#. 当您看到 “Write Successful” 的提示弹窗时，说明系统镜像已成功写入并验证完成。现在，您可以使用这张 Micro SD 卡启动 Raspberry Pi！

   .. image:: img/os_finish.png
      :width: 90%
