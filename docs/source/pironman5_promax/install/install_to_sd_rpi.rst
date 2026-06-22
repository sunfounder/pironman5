.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_os_sd_rpi_promax:

安装操作系统
===================================

在使用 Raspberry Pi 之前，需要先将 **Raspberry Pi OS** 安装到 microSD 卡中。  
本指南将介绍如何使用 **Raspberry Pi Imager** 以简单、适合初学者的方式完成安装。

**所需组件**

* 一台电脑（Windows、macOS 或 Linux）
* 一张 microSD 卡（16GB 或更大；推荐品牌：SanDisk、Samsung）
* 一个 microSD 读卡器


.. start_install_imager

1. 安装 Raspberry Pi Imager
-------------------------------------------

#. 访问 Raspberry Pi Imager 官方下载页面：|link_rpi_imager|，下载适用于你操作系统的安装程序。

   .. image:: img/imager_download.png
      :width: 70%

#. 按照安装提示完成安装（语言、安装路径、确认等）。安装完成后，从桌面或应用程序菜单启动 **Raspberry Pi Imager**\ 。

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager



2. 将操作系统安装到 microSD 卡
------------------------------------------------

1. 使用读卡器将 microSD 卡插入电脑。在继续之前，请备份卡中的重要数据。

   .. image:: img/insert_sd.png
      :width: 90%

2. 打开 Raspberry Pi Imager 后，你会看到 **Device** 页面。从列表中选择 **Raspberry Pi 5**\ 。

   .. image:: img/imager_device.png
      :width: 90%

3. 进入 **OS** 选项，选择推荐的 **Raspberry Pi OS (64-bit)**\ 。

   .. image:: img/imager_os.png
      :width: 90%

4. 在 **Storage** 选项中选择你的 microSD 卡。

   .. image:: img/imager_storage.png
      :width: 90%

.. start_install_os

5. 点击 **Next** 进入自定义配置步骤。

.. note::

   * 如果你会直接连接显示器、键盘和鼠标到 Raspberry Pi，可以点击 **SKIP CUSTOMISATION**\ 。  
   * 如果你计划进行 **无显示器安装（Headless）** 并通过 Wi-Fi 远程连接，则必须完成以下配置。

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **设置主机名（Hostname）**

   * 为 Raspberry Pi 设置一个唯一名称。
   * 以后可以通过 ``hostname.local`` 进行连接。

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **设置地区（Localisation）**

   * 选择你的城市。
   * Imager 会自动填写时区和键盘布局，你也可以自行调整，然后点击 Next。

   .. image:: img/imager_custom_local.png
      :width: 90%

#. **设置用户名和密码**

   为 Raspberry Pi 创建用户账户。

   .. image:: img/imager_custom_user.png
      :width: 90%

#. **配置 Wi-Fi**

   * 输入 Wi-Fi **SSID（网络名称）** 和 **密码**\ 。
   * Raspberry Pi 在首次启动时会自动连接该网络。

   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **启用 SSH（可选但推荐）**

   * 启用 SSH 可以让你通过电脑远程登录 Raspberry Pi。
   * 可以使用用户名密码登录，或配置 SSH 密钥。

   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **启用 Raspberry Pi Connect（可选）**

   Raspberry Pi Connect 允许你通过浏览器访问 Raspberry Pi 桌面。

   * 打开 **Raspberry Pi Connect**\ ，然后点击 **OPEN RASPBERRY PI CONNECT**\ 。

     .. image:: img/imager_custom_connect.png
        :width: 90%

   * Raspberry Pi Connect 网站将在浏览器中打开。登录 Raspberry Pi ID 账户，如果没有账户则注册一个。

     .. image:: img/imager_custom_open.png
        :width: 90%

   * 在 **New auth key** 页面创建一次性认证密钥。

      * 如果你的 Raspberry Pi ID 没有加入任何组织，选择 **Create auth key and launch Raspberry Pi Imager**\ 。
      * 如果属于某个组织，先选择组织，然后创建密钥并启动 Imager。
      * 请确保在密钥过期前开启 Raspberry Pi 并连接互联网。

     .. image:: img/imager_custom_authkey.png
        :width: 90%

   * 浏览器可能会提示打开 Raspberry Pi Imager — 允许即可。

     * Imager 会自动打开 Raspberry Pi Connect 页面并显示认证 Token。
     * 如果 Token 没有自动填入，可以在 **Having trouble?** 页面复制 Token 并手动粘贴到 Imager。

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. 检查所有设置后点击 **WRITE**\ 。

   .. image:: img/imager_writing.png
      :width: 90%

#. 如果存储卡已有数据，Imager 会提示所有数据将被删除。请确认选择的是正确设备，然后点击 **I UNDERSTAND, ERASE AND WRITE**\ 。

   .. image:: img/imager_erase.png
      :width: 90%

#. 等待写入和校验完成。当显示 **Write complete!** 时，说明系统已经写入成功。存储设备会自动弹出，可以安全移除。

   .. image:: img/imager_finish.png
        :width: 90%

.. end_install_os

#. 取出 microSD 卡，并将其插入 Raspberry Pi 底部的卡槽。现在你的 Raspberry Pi 已准备好使用新的操作系统启动！

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%