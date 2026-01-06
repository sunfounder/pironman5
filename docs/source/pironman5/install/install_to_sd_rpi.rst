.. _install_os_sd_5:

安装操作系统
===================================

在使用 Raspberry Pi 之前，你需要先将 **Raspberry Pi OS** 安装到一张 microSD 卡中。  
本指南将以简单、适合初学者的方式，介绍如何使用 **Raspberry Pi Imager** 完成安装。

**所需组件**

* 一台电脑（Windows、macOS 或 Linux）
* 一张 microSD 卡（容量 16GB 或以上；推荐品牌：SanDisk、Samsung）
* 一个 microSD 卡读卡器

-------------------

.. start_install_imager

1. 安装 Raspberry Pi Imager
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>   

#. 访问 Raspberry Pi Imager 官方下载页面：|shared_link_rpi_imager|，下载与你操作系统对应的安装程序。

   .. image:: img/imager_download.png
      :width: 70%

#. 按照安装提示完成安装（语言、安装路径、确认等）。安装完成后，从桌面或应用程序菜单启动 **Raspberry Pi Imager**。

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. 将操作系统安装到 microSD 卡
------------------------------------------------

1. 使用读卡器将 microSD 卡插入电脑。在继续之前，请备份卡中的所有重要数据。

   .. image:: img/insert_sd.png
      :width: 90%

2. 打开 Raspberry Pi Imager 后，你会看到 **Device** 页面。从列表中选择你的 Raspberry Pi 5 型号。

   .. image:: img/imager_device.png
      :width: 90%

3. 进入 **OS** 部分，选择推荐的 **Raspberry Pi OS (64-bit)**。

   .. image:: img/imager_os.png
      :width: 90%

4. 在 **Storage** 部分，选择你的 microSD 卡。

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. 点击 **Next**，进入自定义设置步骤。

   .. note::

      * 如果你打算直接为 Raspberry Pi 连接显示器、键盘和鼠标，可以点击 **SKIP CUSTOMISATION**。  
      * 如果你计划以 *无屏（Headless）* 方式设置 Raspberry Pi（通过 Wi-Fi 远程访问），则必须完成自定义设置。

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **设置主机名（Hostname）**

   * 为你的 Raspberry Pi 设置一个唯一的主机名。  
   * 之后可以通过 ``hostname.local`` 的方式连接到它。

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **设置本地化（Localisation）**

   * 选择你所在的城市。
   * Imager 会根据你的选择自动补全时区和键盘布局，如有需要也可以手动调整，然后点击 Next。
   
   .. image:: img/imager_custom_local.png
      :width: 90%

#. **设置用户名和密码**

   为你的 Raspberry Pi 创建一个用户账户。
   
   .. image:: img/imager_custom_user.png
      :width: 90%

#. **配置 Wi-Fi**

   * 输入你的 Wi-Fi **SSID**（网络名称）和 **密码**。  
   * Raspberry Pi 在首次启动时将自动连接该网络。
   
   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **启用 SSH（可选但推荐）**

   * 启用 SSH 可让你从电脑远程登录 Raspberry Pi。  
   * 你可以使用用户名/密码登录，或配置 SSH 密钥。
   
   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **启用 Raspberry Pi Connect（可选）**

   Raspberry Pi Connect 允许你通过网页浏览器访问 Raspberry Pi 的桌面。
   
   * 打开 **Raspberry Pi Connect**，然后点击 **OPEN RASPBERRY PI CONNECT**。
   
     .. image:: img/imager_custom_connect.png
        :width: 90%

   * Raspberry Pi Connect 网站将在默认浏览器中打开。登录你的 Raspberry Pi ID 账号；如果还没有账号，请先注册。

     .. image:: img/imager_custom_open.png
        :width: 90%

   * 在 **New auth key** 页面，创建一次性认证密钥。
      
      * 如果你的 Raspberry Pi ID 账号不属于任何组织，选择 **Create auth key and launch Raspberry Pi Imager**。
      * 如果你属于一个或多个组织，请选择对应的组织，然后创建密钥并启动 Imager。
      * 请确保在密钥过期前为 Raspberry Pi 上电并连接到互联网。
   
     .. image:: img/imager_custom_authkey.png
        :width: 90%
   
   * 浏览器可能会询问是否打开 Raspberry Pi Imager —— 请允许。

     * Imager 会在 Raspberry Pi Connect 标签页中打开，并显示认证令牌。
     * 如果令牌没有自动传输，请在 Raspberry Pi Connect 页面中打开 **Having trouble?**，复制令牌并手动粘贴到 Imager 中。

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. 检查所有设置无误后，点击 **WRITE**。

   .. image:: img/imager_writing.png
      :width: 90%

#. 如果存储卡中已有数据，Raspberry Pi Imager 会提示该设备上的所有数据将被清除。请再次确认选择了正确的设备，然后点击 **I UNDERSTAND, ERASE AND WRITE** 继续。

   .. image:: img/imager_erase.png
      :width: 90%

#. 等待写入和校验完成。完成后，Raspberry Pi Imager 会显示 **Write complete!** 以及你的配置摘要。存储设备将被自动弹出，你可以安全移除它。

   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. 取出 microSD 卡并将其插入 Raspberry Pi 底部的卡槽中。你的 Raspberry Pi 现在已经可以使用新的操作系统启动了！

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%
