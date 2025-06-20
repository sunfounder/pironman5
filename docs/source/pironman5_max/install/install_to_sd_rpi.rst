.. _max_install_os_sd_rpi:

在 Micro SD 卡上安装操作系统
============================================================
如果您使用的是 Micro SD 卡，可以按照以下教程将系统写入 Micro SD 卡中。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡及读卡器

**操作步骤**

#. 使用读卡器将 SD 卡插入您的电脑或笔记本。

#. 打开 |link_rpi_imager|，点击 **Raspberry Pi Device**，从下拉列表中选择 **Raspberry Pi 5** 模型。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. 点击 **Operating System**，选择推荐的操作系统版本。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 点击 **Choose Storage**，选择用于安装的存储设备。

   .. image:: img/os_choose_sd.png
      :width: 90%

#. 点击 **NEXT**，然后点击 **EDIT SETTINGS** 进入系统配置界面。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * 设置树莓派的 **hostname**，它是树莓派在网络中的标识，可通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问。

     .. image:: img/os_set_hostname.png


   * 创建管理员账户的 **Username** 和 **Password**。为了保障系统安全，请设置唯一的用户名与密码，系统默认并无密码。

     .. image:: img/os_set_username.png      

   * 配置无线网络，填写您的 **SSID** 与 **Password**。

     .. note::

       请将 ``Wireless LAN country`` 设置为您所在地对应的 ISO 两字母国家代码。参考： `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_

     .. image:: img/os_set_wifi.png


   * 若需远程连接树莓派，请在 Services 标签页启用 SSH 功能。

     * 使用 **密码认证** 时，请填写 General 标签页中设置的用户名与密码。
     * 若选择 **公钥认证**，请勾选 "Allow public-key authentication only"。若已有 RSA 密钥将会使用；如未生成，可点击 "Run SSH-keygen" 创建一对新的密钥。

     .. image:: img/os_enable_ssh.png

   * 在 **Options** 菜单中，可设置写入完成时的操作，例如播放提示音、自动弹出介质及启用遥测。

     .. image:: img/os_options.png

#. 输入完所有系统配置后，点击 **Save** 保存设置，然后点击 **Yes** 应用这些设置并开始写入镜像。

   .. image:: img/os_click_yes.png
      :width: 90%


#. 若 SD 卡内已有数据，请确保已完成备份。如无需备份，点击 **Yes** 继续操作。

   .. image:: img/os_continue.png
      :width: 90%


#. 当您看到 “Write Successful” 的弹窗时，说明镜像已成功写入并验证完成。现在，您可以使用这张 Micro SD 卡启动您的树莓派了！

   .. image:: img/os_finish.png
      :width: 90%
