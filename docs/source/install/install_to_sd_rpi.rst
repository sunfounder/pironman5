.. _install_os_sd_rpi:

将操作系统安装到 Micro SD 卡
============================================================
如果你使用的是 Micro SD 卡，可以按照以下教程将系统安装到你的 Micro SD 卡中。

.. 
   .. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**所需组件**

* 一台个人计算机
* 一张 Micro SD 卡及读卡器

**步骤**

#. 使用读卡器将 SD 卡插入计算机或笔记本电脑。

#. 在 |link_rpi_imager| 中，点击 **Raspberry Pi Device** 并从下拉列表中选择 **Raspberry Pi 5** 型号。

   .. image:: img/os_choose_device_pi5.jpg
      :width: 90%

#. 选择 **选择操作系统**，并选择推荐的操作系统版本。

   .. image:: img/os_choose_os.jpg
      :width: 90%

#. 点击 **选择SD卡**，选择适合安装的存储设备。

   .. image:: img/os_choose_sd.png
      :width: 90%

#. 点击 **NEXT**，然后点击 **编辑设置** 来定制你的操作系统设置。

   .. image:: img/os_enter_setting.jpg
      :width: 90%
      

   * 为 Raspberry Pi 设置一个 **主机名**。主机名是你 Raspberry Pi 的网络标识符。你可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 来访问你的 Pi。

     .. image:: img/os_set_hostname.jpg
   

   * 创建 Raspberry Pi 管理员账户的 **Username** 和 **密码**。设置一个独特的用户名和密码对于保护你的 Raspberry Pi 非常重要，因为它没有默认密码。

     .. image:: img/os_set_username.jpg      

   * 配置无线局域网，提供你的网络 **热点名** 和 **密码**。

     .. note::

       将 ``Wireless LAN country`` 设置为与你所在位置对应的两字母 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

     .. image:: img/os_set_wifi.jpg


   * 若要远程连接到 Raspberry Pi，启用 SSH 服务。

     * 对于 **密码认证**，使用常规选项卡中的用户名和密码。
     * 对于公钥认证，选择 "仅允许公钥认证"。如果你有 RSA 密钥，它将被使用；如果没有，可以点击 "运行 SSH-keygen" 生成一个新的密钥对。

     .. image:: img/os_enable_ssh.png

   * **Options** 菜单允许你配置 Imager 在写入过程中的行为，包括完成时播放声音、完成后弹出媒体设备和启用遥测功能。

     .. image:: img/os_options.png

#. 完成操作系统定制设置后，点击 **Save/保存** 保存设置。然后点击 **是**，在写入映像时应用这些设置。

   .. image:: img/os_click_yes.jpg
      :width: 90%
      

#. 如果 SD 卡中有现有数据，请确保备份以防丢失数据。如果不需要备份，点击 **是** 继续。

   .. image:: img/os_continue.png
      :width: 90%
      

#. 当你看到 "Write Successful" 弹窗时，表示映像已经成功写入并验证。你现在可以从 Micro SD 卡启动 Raspberry Pi 了！

   .. image:: img/os_finish.png
      :width: 90%
